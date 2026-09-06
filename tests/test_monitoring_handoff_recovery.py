"""Regression tests for configuration recovery after a failed setup."""

from __future__ import annotations

import asyncio
import importlib
import sys
import types
from pathlib import Path
from types import SimpleNamespace

import pytest


COMPONENT_ROOT = (
    Path(__file__).resolve().parent.parent / "custom_components" / "power_sync"
)


def _load_monitoring_module():
    names = ("power_sync", "power_sync.const", "power_sync.monitoring")
    saved = {name: sys.modules.get(name) for name in names}

    power_sync = types.ModuleType("power_sync")
    power_sync.__path__ = [str(COMPONENT_ROOT)]
    const = types.ModuleType("power_sync.const")
    const.DOMAIN = "power_sync"
    const.SERVICE_RESTORE_NORMAL = "restore_normal"
    sys.modules["power_sync"] = power_sync
    sys.modules["power_sync.const"] = const
    sys.modules.pop("power_sync.monitoring", None)
    module = importlib.import_module("power_sync.monitoring")

    def restore() -> None:
        for name, previous in saved.items():
            if previous is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous

    return module, restore


def test_monitoring_handoff_allows_failed_entry_configuration_recovery():
    """A failed setup has no service or live control state to clean up."""
    monitoring, restore_module = _load_monitoring_module()
    try:
        execute_lock = asyncio.Lock()

        async def async_call(*args, **kwargs):
            raise AssertionError("missing service must not be called")

        hass = SimpleNamespace(
            data={
                "power_sync": {
                    "entry-1": {
                        "optimization_coordinator": SimpleNamespace(
                            _execute_lock=execute_lock,
                            _pre_idle_backup_reserve=None,
                        )
                    }
                }
            },
            services=SimpleNamespace(
                has_service=lambda domain, service: False,
                async_call=async_call,
            ),
        )

        asyncio.run(
            monitoring.async_prepare_monitoring_handoff(
                hass,
                SimpleNamespace(entry_id="entry-1"),
            )
        )
        assert execute_lock.locked() is False
    finally:
        restore_module()


def test_monitoring_handoff_blocks_when_control_state_still_needs_cleanup():
    """Never bypass cleanup when the failed entry still tracks live control."""
    monitoring, restore_module = _load_monitoring_module()
    try:
        hass = SimpleNamespace(
            data={
                "power_sync": {
                    "entry-1": {"force_charge_state": {"active": True}}
                }
            },
            services=SimpleNamespace(
                has_service=lambda domain, service: False,
                async_call=lambda *args, **kwargs: None,
            ),
        )

        with pytest.raises(
            RuntimeError,
            match="control state still requires cleanup",
        ):
            asyncio.run(
                monitoring.async_prepare_monitoring_handoff(
                    hass,
                    SimpleNamespace(entry_id="entry-1"),
                )
            )
    finally:
        restore_module()
