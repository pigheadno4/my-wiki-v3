# Cash App Pay Android Component retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the Cash App Pay Android Component guide add, which version does it target, and what does it not prove?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android-component.md` → `raw/adyen/docs/payment-methods/cash-app-pay/android-component/2026-09-15.md` heading `# Cash App Pay Component integration`, lines 14–18. Expected answer: a 2026-09-15-captured method-specific addition to existing Android Components Sessions/Advanced integrations, for minimum v5.0.0 (released October 2023), with an earlier-version guide for older versions. It does not prove present merchant enablement or a completed live payment. The approved `source-adyen-docs-payment-methods-cash-app-pay` provides separate US/USD wallet overview context; this child must not be confused with Cash App Afterpay.

## Q2 — Fields, finality, tokens and test

Query: What extra fields/configuration are needed, when is a payment final, and under what condition can future token payments bypass shopper approval?

Expected route: same root/provider/concept/source/pinned-raw chain. Verify canonical stem `/payment-methods/cash-app-pay/android-component`, raw lines 20–64 (both flow prerequisites, no additional method fields/configuration), 66–78 (resultCode and asynchronous webhook), 80–84 (tokenization, permission and recommendation), 86–90 (test magic values and live Customer Area). Expected answer: both flows require existing Android Components v5.0.0+ and method setup; no extra Cash App Pay fields or configuration beyond the base integration. `Received` is pending, `AUTHORISATION` webhook supplies the update, `Authorised` is successful but manual capture still requires capture. `Cancelled`, `Error`, and `Refused` differ. Future recurring/card-on-file token payments can bypass shopper approval only after permission to save details at token creation; explicit permission and schedule/amount transparency are strongly recommended. Magic values are sandbox tests; live acceptance needs live Customer Area setup, without proving actual execution.
