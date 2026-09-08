<!-- release: v2.12.1255 -->

## Automatic AGL/Ausgrid seasonal import scheduling

- Added an explicit opt-in AGL/Ausgrid seasonal TOU import schedule. Enter the rates from the configured address-specific offer and PowerSync authors Summer and Winter import periods through the existing custom-tariff path.
- Manual and custom AGL tariffs remain the default and are unchanged unless the automatic schedule is selected.
- Battery Rewards continues to apply its 17:00–21:00 export overlay after the import tariff is authored, preserving import rates and the immutable base tariff across edits and reloads.

## Verified AI forecast evidence

- AI Plan Explanation now shows timestamped solar and load forecast values from the exact optimizer snapshot that generated the displayed schedule.
- Forecast evidence is checked for matching server-generated schedule identity and complete timestamp alignment. Missing, mismatched, incomplete, or changed forecast data is labelled unavailable or changed instead of being presented as a causal decision link.
- AI explanations remain descriptive: only PowerSync's server-generated evidence can associate forecast values with an action window.

Update available via HACS
