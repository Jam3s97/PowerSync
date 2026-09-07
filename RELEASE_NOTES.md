<!-- release: v2.12.1245 -->

## What's Changed

**EPEX custom-price forecast boundary**
Finite custom EPEX `price_values` series may still be padded internally for optimization, but their synthetic tail is no longer shown as source-provided pricing in the LP forecast, schedule data, or price references. This prevents a custom series from appearing to extend beyond its actual supplied horizon.

**Home Assistant device-registry compatibility**
PowerSync now uses the supported device-registry iteration and lookup APIs across setup, sensors, EV planning, charger capability detection, and FoxESS model detection. This removes the current deprecation warnings and preserves compatibility with both the minimum supported Home Assistant version and the upcoming 2027.9 registry API removal.

Update available via HACS
