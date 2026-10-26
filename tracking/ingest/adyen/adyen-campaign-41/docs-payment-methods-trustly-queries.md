# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-trustly.md` → pinned raw.

This 2025-modified, 2026-09-15-captured overview describes Trustly bank-account payment in Europe, with a Trustly-hosted bank redirect, shopper bank authentication and return to the merchant (raw `adyen/docs/payment-methods/trustly/2026-09-15.md:15-32`). Its table says Online Banking/Redirect, “International” countries and DKK/EUR/NOK/SEK, with dated feature marks (raw lines 34-36). These are not proof of present country/bank/merchant eligibility or a payment's cleared funds. Platform links to Web, iOS, Android, API-only and Pay by Link are navigation, not detailed implementation contracts (raw lines 55-85). Source stem: `source-adyen-docs-payment-methods-trustly`.

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-trustly.md`.

The shopper chooses Trustly, selects a bank and account on its hosted page, authenticates and confirms with a one-time code before returning to the merchant (raw `adyen/docs/payment-methods/trustly/2026-09-15.md:25-32`). A successful `AUTHORISATION` webhook means verification passed and transfer initiation succeeded, **not** that Adyen received funds; shopper cancellation or delayed bank processing can still cause failure, and Adyen says it may not be informed of that failure (raw lines 38-45). Status remains `SentForSettle` until funds arrive; if absent after eight calendar days, the page describes a `Settled` then `Chargeback` sequence with `CHARGEBACK` webhook. The chargeback cannot be defended; late arrival yields `CHARGEBACK_REVERSED` (raw lines 47-53). The table marks recurring/capture variants unavailable and refund variants/chargebacks available in the dated snapshot (raw lines 34-36), without establishing current account setup or outcome.
