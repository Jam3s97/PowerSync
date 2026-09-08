<!-- release: v2.12.1253 -->

## What's Changed

**SolarEdge rejected force commands no longer leave a stale active override**
When SolarEdge cannot safely release an active-power curtailment because control is busy or requires reconciliation, PowerSync now returns that fail-closed result before cancelling an existing Force Charge or Force Discharge timer or publishing a new force state. A rejected pre-hardware request therefore cannot leave the optimizer suppressed or the Battery Mode status claiming a new active force command. Confirmed SolarEdge command, readback, reconciliation, Monitoring Mode, and hardware safety gates are unchanged.

Update available via HACS
