<!-- release: v2.12.1241 -->

## What's Changed

**Safer SolarEdge control after uncertain writes**
SolarEdge control now stops when a write may have reached the inverter but cannot be confirmed. PowerSync retains the previous settings and blocks further commands until supervised reconciliation verifies a safe baseline. The control block survives Home Assistant restart; startup does not replay SolarEdge force commands or expiry timers from an interrupted session. Battery and curtailment operations share a lock, and rejected controls propagate failure to service callers and optimizer handling.

**Reliable SolarEdge timer cleanup**
Changing the backup reserve during a timed force charge or discharge no longer invalidates its expiry timer. Replacement force commands still supersede older timers. A confirmed Self-Consumption expiry restore clears the matching manual override so automatic optimization can resume, while failed restores preserve the recovery state.

**Preserve safe storage baselines**
A self-consumption baseline remains valid with a non-zero command timeout. Native active charging and discharging modes are recognized and rejected as unsafe baselines before dispatch. Restoration changes only settings PowerSync changed.

**SolarEdge recovery guidance**
The Battery Integration Details sensor exposes control health and the last control mutation. The new `power_sync.reconcile_solaredge_control` service uses fresh storage readback and sends no inverter writes. Follow the [SolarEdge Control Recovery guide](https://github.com/bolagnaise/PowerSync/wiki/SolarEdge-Control-Recovery) before using it. Storage reconciliation cannot clear an uncertain active-power curtailment write; that requires separate validation of the active-power controls.

Update available via HACS
