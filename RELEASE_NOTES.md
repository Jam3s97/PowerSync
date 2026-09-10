<!-- release: v2.12.1271 -->

## Display currency selection

- Added an Options-flow display-currency preference: Automatic, AUD, EUR, GBP, NZD, or SEK.
- Monetary presentation now exposes requested, effective, and source-currency metadata. SEK sources use öre/kWh.
- This release does not convert provider prices or change tariff data, billing/history values, thresholds, or optimizer calculations. A source currency that differs from the selected display preference remains visibly in its native currency and unit.
- Formatting safely falls back to a native code-and-decimal label when browser locale support is unavailable.

Update available via HACS
