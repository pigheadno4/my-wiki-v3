# Braintree C42 Query Audit D — Correction Amendment

- Checked (UTC): `2026-10-07T01:05:10Z`
- Scope: only the three questions marked FAIL in `/tmp/braintree-c42-query-audit-d.md`
- Amended verdict: **PASS — 8/8 questions pass (three corrected failures rechecked; five original passes unchanged)**

## Correction evidence

1. **`docs-guides-paypal-testing-go-live-ios-v7`, question 2 — FIXED/PASS.** The promoted source now states that the production merchant ID and API keys differ from Sandbox, while only the public/private keys are both environment- and user-specific (`wiki/sources/braintree/source-braintree-docs-guides-paypal-testing-go-live-ios-v7.md:22`). This exactly matches raw lines 262–284: all identifiers differ across Sandbox/Production, API keys belong to individual users, and public/private keys are explicitly environment- and user-specific. The amendment is the sole diff from the final promoted attempt candidate in this source.

2. **`docs-guides-paypal-recurring-payments-android-v5`, question 2 — FIXED/PASS.** The promoted source now warns that the captured Kotlin example omits the comma between `totalAmount` and `productName`, needs syntax repair, and is not directly runnable as captured (`wiki/sources/braintree/source-braintree-docs-guides-paypal-recurring-payments-android-v5.md:24`). Raw lines 162–173, specifically 165–166, show the omission. The amendment is the sole diff from the promoted attempt candidate in this source.

3. **`docs-guides-venmo-client-side-ios-v7`, question 2 — FIXED/PASS.** The promoted source now qualifies the failure as an attempt **to vault** a `.singleUse` authorization through `PaymentMethod.create` or `Customer.create` (`wiki/sources/braintree/source-braintree-docs-guides-venmo-client-side-ios-v7.md:20`). This matches raw lines 293–316, including the separate rule that `transaction.sale` vault flags do not vault the nonce. The amendment is the sole diff from the promoted attempt candidate in this source.

## Unchanged evidence pins

- iOS PayPal testing/go-live raw: `aaa7beec0ba17fed34a81d5153e978aa1de17e9a14a2f048078ef743610a5235` — matches manifest.
- Android recurring raw: `e3a3801f45c2df127639b718763d789c4455f33abd895b174c98e424c48aa512` — matches manifest.
- iOS Venmo raw: `0a34d19edee0a4dd87045ccbe475756577913cceee54c80a8cb570e4519c6e0c` — matches manifest.

No other questions or evidence were re-audited. The initial failure report remains unchanged at `/tmp/braintree-c42-query-audit-d.md`. No repository files were modified by this amendment audit.
