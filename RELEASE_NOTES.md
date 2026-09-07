<!-- release: v2.12.1246 -->

## What's Changed

**EPEX options now apply after a reload**
Changes made in the EPEX options flow now take effect after Home Assistant reloads the integration. Region, import surcharge, tax, and fixed export rate consistently use the saved options instead of stale setup values, so the optimizer values import prices with the configured surcharge and tax.

**Swedish price metadata uses öre**
SEK price metadata now labels its minor unit as öre/kWh rather than generic cents/kWh. Native EPEX pricing remains EUR/ct unless an explicitly configured source provides another currency.

Update available via HACS
