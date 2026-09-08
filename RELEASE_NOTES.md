<!-- release: v2.12.1249 -->

## What's Changed

**Tesla Fleet charge commands no longer depend on a separate Wake button**
PowerSync now lets Home Assistant's official Tesla Fleet command entities perform their own wake-up before starting or stopping charging, changing the charge limit, or setting charge current. This keeps the supported Fleet control path usable when its Charge switch is available with Vehicle Charging Commands but the separate Wake button is absent because Vehicle Commands was not granted.

The existing explicit wake flow remains in place for other Tesla providers. Home Assistant service acceptance still is not proof that the vehicle physically changed state; PowerSync's existing ownership, eligibility, and post-command checks remain unchanged.

Update available via HACS
