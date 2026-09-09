<!-- release: v2.12.1259 -->

## What's Changed

**Tesla Fleet active-charge status now preserves unavailable power**
When Home Assistant's Tesla Fleet integration still reports that a vehicle is
charging but its charge-power entity is unavailable, PowerSync now keeps the
loadpoint active with unknown power. Home Load accounting is marked incomplete
instead of presenting that condition as a measured 0 W idle state.

**Direct Wall Connector readings remain authoritative**
A current, safely matched Tesla Wall Connector measurement continues to replace
an unavailable Fleet reading for the same vehicle.

Update available via HACS
