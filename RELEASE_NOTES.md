<!-- release: v2.12.1247 -->

## What's Changed

**Platform Auto Update now works when HACS has stale release metadata**
Platform Auto Update now verifies the latest published PowerSync release before treating an install-capable HACS update entity as up to date. If HACS has not yet refreshed its cached release list, PowerSync asks the same HACS update entity to install the explicitly published release version. This remains fail-closed: no install is attempted if the published release cannot be verified, is not newer than the installed version, or the HACS entity does not support explicit versions.

**HACS stays the installation boundary**
The scheduler does not access HACS private repository internals. It continues to use Home Assistant's supported update service and retains the existing restart and once-per-day safeguards.

Update available via HACS
