<!-- release: v2.12.1264 -->

## What's Changed

**Full Solcast forecast coverage for rolling plans**
PowerSync now reads the full forecast cache exposed by current Solcast Solar releases through the loaded integration runtime. This keeps the configured rolling optimizer horizon populated when the Today and Tomorrow sensors alone do not cover its later intervals, avoiding an artificial forecast drop or jump as those daily sensors roll over.

The legacy Solcast cache and sensor-attribute fallbacks remain available for existing installations.

Update available via HACS
