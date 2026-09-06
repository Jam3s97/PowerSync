<!-- release: v2.12.1239 -->

## What's Changed

### Enphase Reference Capacity Preservation

PowerSync now refreshes the Enphase gateway's current Reference Max Capacity immediately before every DPEL curtailment write. Installer corrections are no longer replaced by an older cached or microinverter-derived value, and stale capacity aliases are removed from cached payloads when the gateway cannot confirm its current value.

### Demand Charge Setup Recovery

Demand-charge billing days are now normalized to whole numbers before billing-cycle keys are built, fixing entry setup failures caused by Home Assistant submitting values such as `1.0`. Legacy saved day selections such as `all` are also migrated to the current selector values when the form is opened or saved.

### Battery Connection Setup Recovery

Battery connection setup can now recover from an earlier failed or unloaded PowerSync entry when the restore service was never registered, instead of stopping with `monitoring_cleanup_failed`. The safety guard remains fail-closed whenever force-control state or a pending reserve restoration still needs cleanup.

Update available via HACS.
