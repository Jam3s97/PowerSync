"""Currency helper tests."""

from __future__ import annotations

import ast
import sys
import types
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parent.parent / "custom_components" / "power_sync"
_ps = types.ModuleType("power_sync")
_ps.__path__ = [str(ROOT)]
sys.modules["power_sync"] = _ps

from power_sync.currency import (  # noqa: E402
    currency_for_entry,
    currency_for_provider,
    currency_metadata,
    display_currency_for_entry,
    major_price_unit,
    minor_currency_unit,
    minor_price_unit,
    money_unit,
    presentation_currency_metadata_for_entry,
    selector_unit_for_provider,
)


def _hass(currency: str | None):
    return SimpleNamespace(config=SimpleNamespace(currency=currency))


def test_provider_currency_defaults():
    assert currency_for_provider("amber", _hass("GBP")) == "AUD"
    assert currency_for_provider("flow_power", _hass("GBP")) == "AUD"
    assert currency_for_provider("agl", _hass("GBP")) == "AUD"
    assert currency_for_provider("octopus", _hass("AUD")) == "GBP"
    assert currency_for_provider("epex", _hass("AUD")) == "EUR"
    assert currency_for_provider("nz", _hass("AUD")) == "NZD"


def test_generic_provider_uses_home_assistant_currency_with_aud_fallback():
    assert currency_for_provider("other", _hass("GBP")) == "GBP"
    assert currency_for_provider("tou_only", _hass("eur")) == "EUR"
    assert currency_for_provider("other", _hass(None)) == "AUD"


def test_entry_currency_uses_options_before_data():
    entry = SimpleNamespace(
        data={"electricity_provider": "octopus"},
        options={"electricity_provider": "other"},
    )

    assert currency_for_entry(entry, _hass("NZD")) == "NZD"


def test_entry_currency_metadata_uses_home_assistant_currency():
    entry = SimpleNamespace(
        data={"electricity_provider": "other"},
        options={},
    )

    assert currency_metadata(currency_for_entry(entry, _hass("GBP"))) == {
        "currency": "GBP",
        "price_unit": "GBP/kWh",
        "minor_price_unit": "p/kWh",
    }


def test_currency_unit_helpers():
    assert money_unit("gbp") == "GBP"
    assert major_price_unit("GBP") == "GBP/kWh"
    assert selector_unit_for_provider("octopus", _hass("AUD"), "major_rate") == "GBP/kWh"
    assert minor_currency_unit("GBP") == "p"
    assert minor_currency_unit("EUR") == "ct"
    assert minor_currency_unit("SEK") == "öre"
    assert minor_currency_unit("NZD") == "c"
    assert minor_price_unit("GBP") == "p/kWh"
    assert minor_price_unit("EUR") == "ct/kWh"
    assert minor_price_unit("SEK") == "öre/kWh"
    assert minor_price_unit("AUD") == "c/kWh"


def test_display_currency_metadata_is_explicit_but_never_converts_source_values():
    entry = SimpleNamespace(
        data={"electricity_provider": "octopus"},
        options={"display_currency": "SEK"},
    )

    metadata = presentation_currency_metadata_for_entry(entry, "GBP")

    assert currency_for_entry(entry, _hass("SEK")) == "GBP"
    assert metadata["currency"] == "GBP"
    assert metadata["price_unit"] == "GBP/kWh"
    assert metadata["minor_price_unit"] == "p/kWh"
    assert metadata["source_currency"] == "GBP"
    assert metadata["requested_display_currency"] == "SEK"
    assert metadata["display_currency"] == "GBP"
    assert metadata["display_currency_fallback"] is True


def test_display_currency_matching_sek_uses_ore_and_invalid_values_fall_back():
    sek_entry = SimpleNamespace(data={}, options={"display_currency": "sek"})
    invalid_entry = SimpleNamespace(data={}, options={"display_currency": "JPY"})
    automatic_entry = SimpleNamespace(data={}, options={})

    sek_metadata = presentation_currency_metadata_for_entry(sek_entry, "SEK")
    assert display_currency_for_entry(sek_entry) == "SEK"
    assert sek_metadata["display_currency"] == "SEK"
    assert sek_metadata["minor_price_unit"] == "öre/kWh"
    assert sek_metadata["display_currency_fallback"] is False

    for entry in (invalid_entry, automatic_entry):
        metadata = presentation_currency_metadata_for_entry(entry, "EUR")
        assert display_currency_for_entry(entry) is None
        assert metadata["currency"] == "EUR"
        assert metadata["display_currency"] == "EUR"
        assert metadata["requested_display_currency"] == "automatic"
        assert metadata["display_currency_fallback"] is False


def _class_method_source(class_name: str, method_name: str) -> str:
    init_path = ROOT / "__init__.py"
    source = init_path.read_text()
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or node.name != class_name:
            continue
        for child in node.body:
            if isinstance(child, ast.AsyncFunctionDef) and child.name == method_name:
                method_source = ast.get_source_segment(source, child)
                assert method_source is not None
                return method_source
    raise AssertionError(f"{class_name}.{method_name} not found")


def test_mobile_config_endpoints_expose_fail_closed_currency_presentation_metadata():
    """Generic tariffs must not make mobile clients fall back to AUD."""

    expected = "presentation_currency_metadata_for_entry("
    assert expected in _class_method_source("ConfigView", "get")
    assert expected in _class_method_source("ProviderConfigView", "get")


def test_options_flow_has_an_independent_non_converting_display_currency_page():
    source = (ROOT / "config_flow.py").read_text()

    assert '"display_currency"' in source
    assert "async_step_display_currency" in source
    assert "CONF_DISPLAY_CURRENCY" in source
    assert "DISPLAY_CURRENCY_AUTOMATIC" in source
    assert "_save_connection_and_reload(\n                    {}, {CONF_DISPLAY_CURRENCY: selected}" in source
