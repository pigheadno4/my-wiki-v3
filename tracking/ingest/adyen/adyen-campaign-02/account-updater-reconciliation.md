# Account Updater overview reconciliation

Decision: **semantically approved** for coordinator application. The already-promoted `wiki/sources/adyen/source-adyen-docs-online-payments-account-updater.md:19` follows its own older overview raw at `raw/adyen/docs/online-payments/account-updater/2026-09-15.md:40`, which says updated information is returned synchronously. The later detailed guide makes receipt optional and configured (`raw/adyen/docs/online-payments/account-updater/real-time-account-updater/2026-09-15.md:20,44-64`), with full PAN subject to a separate fully PCI-compliant, Support-enabled JWE path (`:85-98`). Preserve the overview's Real Time versus Batch distinction and automatic token update.

In the second `## Key takeaways` bullet of the overview source, replace only this sentence:

> Updated card information is returned synchronously in the payment response; when Adyen tokenization is used, the token storing the details is updated automatically.

with:

> Updated card details can be included synchronously in the payment response when the optional Customer Area additional-data settings are enabled; receiving the full updated card number requires the separate fully PCI-compliant, Support-enabled encrypted response path. When Adyen tokenization is used, the token storing the details is updated automatically.

Under that source's `## Related`, add this reciprocal detail route:

> - Real Time detail: [[source-adyen-docs-online-payments-account-updater-real-time-account-updater]] — eligibility, optional response data, encrypted PAN path, statuses, and testing.

This resolves the broad overview phrasing without changing the immutable overview raw or making the older summary appear to establish live eligibility.

## Attribution-preserving replacement (preferred)

**Semantically approved with one retained condition.** Replace the same sentence at `wiki/sources/adyen/source-adyen-docs-online-payments-account-updater.md:19` with the following, keeping that source's sole `raw_files` entry unchanged:

> The overview says updated card information is returned synchronously in the payment response and, when Adyen tokenization is used, the stored token is updated automatically. The detailed Real Time guide qualifies response data as optional and configured, with full updated PAN requiring its separate fully PCI-compliant, Support-enabled encrypted path. [[source-adyen-docs-online-payments-account-updater-real-time-account-updater]]

The added "when Adyen tokenization is used" condition is necessary: the overview raw states it at `raw/adyen/docs/online-payments/account-updater/2026-09-15.md:40`, and the detailed raw repeats it at `raw/adyen/docs/online-payments/account-updater/real-time-account-updater/2026-09-15.md:20`. The detailed-response qualification is supported by detailed raw lines `20,44-64,85-98`. Retain the `## Related` reciprocal link above as a navigation route in addition to the in-text attribution.
