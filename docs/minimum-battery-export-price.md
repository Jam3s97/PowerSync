# Minimum battery export price and Solar Export

Ticket: https://discord.com/channels/1443943629130567874/1536320018898358302

## Behavior

Set **Minimum battery export price** in PowerSync's Optimization options to
the lowest real feed-in price at which the optimizer may intentionally export
stored battery energy. The UI and API use c/kWh; persisted configuration uses
currency units/kWh. A value of 30 means 30c/kWh, with equality permitted.
Zero disables the additional floor and preserves existing tariff policies.
Other reserve, economic, site-limit, ownership, and monitoring checks still apply.

This setting does not prevent the battery supplying household loads or natural
solar export. It is an optimizer policy, not a physical zero-export guarantee
or a restriction on user-owned manual force controls or external controllers.

For solar diversion below the battery floor, enable Profit Maximisation and
disable Chip Mode. Chip Mode independently suppresses below-threshold solar
prices. Profit Max Solar Export also requires a supported charge-hold adapter,
a finite positive export limit, and sufficient cheaper reachable replenishment.
Charge By Time requires that replenishment to fit before its deadline.

Example: with a 30c battery floor, 9c solar now and 3c solar later, PowerSync can
hold battery charging and export the current solar surplus, then release the
hold and charge from cheaper later solar. Stored battery export below 30c is
blocked. A shrinking solar forecast or deadline can remove the hold. Prices
above the floor permit battery export but do not force it.

## Implementation and verification

Reuse the existing `optimization/export_policy.py` predicate, coordinator
permission masks, and execution gate. Keep solar revenue unchanged in the LP;
restrict battery-to-grid energy rather than rewriting export prices or
disabling household discharge. Both HiGHS and the greedy fallback consume the
battery permission and solar charge-hold masks.

The Current Action sensor (`sensor.power_sync_optimization_status`) and API
include `battery_export_price_policy`, containing the configured minimum,
evaluated price in c/kWh, whether that price passes the floor, and its reason.
`disabled` means this additional floor is off; passing it does not imply that
all other export checks passed or that an inverter accepted a command.
The separate `profit_max_solar_export` section explains solar eligibility and
hold state. Prices are evaluated from the coordinator's available tariff
snapshot, not independent live hardware telemetry.

Regression coverage combines the 9c/3c/30c scenario with both solver backends,
checks household discharge and subsequent solar charging, tests insufficient
replenishment and deadline rejection, and checks below/exact/above-floor
execution and unavailable prices. Existing hold lifecycle tests cover failed
apply, cleanup, and startup reconciliation. No physical behavior is established
by these software tests.
