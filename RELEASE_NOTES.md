<!-- release: v2.12.1244 -->

## What's Changed

**EPEX custom forecast safety**
Custom EPEX price sensors with an unsupported structured `forecast` attribute now keep the native EPEX price horizon instead of silently replacing it with the current scalar price. PowerSync logs the unsupported shape so the sensor can be corrected to the documented `price_values` format.

**SolarEdge confirmed-control state**
After a confirmed SolarEdge force-discharge command, a transient persistence failure no longer reports the mode as inactive while its active status and expiry timer remain in effect. The response reports the restart-persistence warning truthfully.

Update available via HACS
