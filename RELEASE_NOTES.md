<!-- release: v2.12.1243 -->

## What's Changed

**FoxESS IDLE holds preserve your minimum SOC**

Smart Optimization now holds FoxESS batteries in Backup mode without raising the inverter's minimum SOC to the current battery level. Previously, that extra reserve change could remain elevated if a Home Assistant restart lost the pending restore target, preventing the battery from serving the house after returning to Self Use. The fix applies to direct Modbus, foxess_modbus entity, and FoxESS Cloud connections.

Failed or unavailable Backup-mode commands now leave the action pending for retry, without falling back to a minimum-SOC change. Pending reserve restores from an existing legacy hold are still retained.

**If your minimum SOC is already elevated**

After updating, reset the inverter's minimum SOC to your intended value once. This release does not automatically lower existing settings that may belong to you or another controller. FoxCloud Mode Scheduler and third-party/VPP control locks are separate; if a reset is blocked or the value returns, check that control ownership and capture logs covering the recurrence.

Update available via HACS
