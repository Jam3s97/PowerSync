<!-- release: v2.12.1248 -->

## What's Changed

**See why the minimum battery export price blocks stored-energy export**
The Current Action sensor and optimizer API now expose the configured minimum battery export price, the evaluated feed-in price, and the price-gate reason under `battery_export_price_policy`. Solar Export eligibility and charge-hold state remain separately visible under `profit_max_solar_export`, so a battery-only price restriction can be distinguished from a rejected solar-export opportunity.

**Verified lower-price solar export with a separate battery floor**
The existing Minimum battery export price setting supports a 30c battery floor while Profit Max considers solar export at 9c now and solar charging at 3c later. Added regressions verify that combination through both HiGHS and the fallback optimizer, including continued household battery use, insufficient replenishment, deadlines, and execution below the floor. This release adds diagnostics and coverage; it does not introduce a second price setting or change the existing export policy.

Use Minimum battery export price in Optimization options, enable Profit Maximisation for conditional solar diversion, and disable Chip Mode for this use case. Supported charge-hold capability, export limits, reserves and cheaper-replenishment checks still apply. The price floor governs optimizer battery export; it does not restrict user-owned manual force controls or guarantee physical zero export.

Update available via HACS
