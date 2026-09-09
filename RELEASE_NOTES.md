<!-- release: v2.12.1257 -->

## Tesla BLE charging status keeps unknown power distinct from zero

- When a connected Tesla BLE vehicle reports Charging but its current watt measurement is unavailable or stale, PowerSync now preserves the Charging state while showing power as unavailable rather than as measured `0 W` or Idle.
- The Home Assistant EV Power sensor, PowerSync widgets, and built-in Energy Flow card now render the unavailable reading as `--`; the card keeps the charging status visible but does not draw or invent a watt flow.
- The canonical status aggregation and Solar Surplus status endpoint now handle incomplete active-EV attribution safely. Home Load remains unavailable while it cannot be safely calculated, and no charger command or hardware behavior is inferred from the display state.

Update available via HACS
