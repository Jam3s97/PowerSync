<!-- release: v2.12.1254 -->

## What's Changed

**Fix incorrect “Vehicle is not plugged in” errors with multiple Tesla integrations**
Manual EV controls now use the same vehicle-specific provider selection as charging actions. When Tesla Fleet has unknown or unavailable entities but Teslemetry has valid data for the same car, PowerSync can use the healthy provider, including Home Assistant's numbered entity names such as `_2`. Disabled entities are ignored, and a second vehicle's BLE plug cache cannot authorize the first vehicle's charge.

**Confirm vehicle wake before relying on Tesla BLE control**
A bridge being online or discovering the car is no longer treated as proof that the vehicle is awake. PowerSync requires fresh vehicle wake evidence before BLE start, current-limit and charge-limit writes. A failed wake allows the configured Both-mode fallback provider to run, with a short per-bridge delay to avoid repeating the same failed wake during the following command.

**Handle uncertain BLE charging commands without claiming success**
BLE writes now require fresh vehicle readback. Charging confirmation supports both BLE sensor naming formats and checks measured current or power. A sent command with an uncertain result is not immediately repeated through another provider: an uncertain start uses the existing vehicle-specific physical confirmation process, then requests a stop for that same car if charging cannot be confirmed. Cancellation also requests a scoped stop. This prevents an HA service acknowledgement from being mistaken for successful charging.

These changes improve detection and recovery from BLE communication failures; a bridge that repeatedly loses its radio connection may still need attention. Combined-provider fallback requires a working alternative Tesla integration.

Update available via HACS
