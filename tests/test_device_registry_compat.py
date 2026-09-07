"""Regression coverage for Home Assistant device-registry API compatibility."""

from __future__ import annotations

import ast
import importlib.util
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parent.parent
COMPONENT_ROOT = ROOT / "custom_components" / "power_sync"
PRODUCTION_PATHS = (
    COMPONENT_ROOT / "__init__.py",
    COMPONENT_ROOT / "sensor.py",
    COMPONENT_ROOT / "automations" / "actions.py",
    COMPONENT_ROOT / "automations" / "ev_charging_planner.py",
    COMPONENT_ROOT / "optimization" / "ev_coordinator.py",
    COMPONENT_ROOT / "inverters" / "foxess_entity.py",
)


def _compat_module():
    spec = importlib.util.spec_from_file_location(
        "registry_compat",
        COMPONENT_ROOT / "registry_compat.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_device_iterator_preserves_old_mapping_and_new_iterable_entries():
    module = _compat_module()
    old_entries = {"a": SimpleNamespace(id="a")}
    new_entries = [SimpleNamespace(id="b")]

    assert [entry.id for entry in module.iter_device_entries(SimpleNamespace(devices=old_entries))] == ["a"]
    assert [entry.id for entry in module.iter_device_entries(SimpleNamespace(devices=new_entries))] == ["b"]


def test_production_code_never_uses_deprecated_device_mapping_methods():
    deprecated: list[str] = []
    for path in PRODUCTION_PATHS:
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if not isinstance(node, ast.Attribute) or node.attr not in {"values", "get"}:
                continue
            if isinstance(node.value, ast.Attribute) and node.value.attr == "devices":
                deprecated.append(f"{path.relative_to(ROOT)}:{node.lineno}")

    assert not deprecated, "deprecated DeviceRegistry.devices access: " + ", ".join(deprecated)
