# Fixed retrieval checks: CVC/CVV/CID result-code testing

## Q1 — Eligible test flow and trigger

**Query:** How does Adyen's guide trigger a simulated CVC/CVV/CID result, and which integrations and environment does it cover?

**Expected answer:** The guide covers Advanced flow and Sessions flow with additional methods before live use. In test Customer Area, enable `additionalData.cvcResult` under Developers > Additional data > Acquirer result. Use unencrypted test card details for the test `/payments` request. Put `00` before a table value in `paymentMethod.cvc`, so `004` requests simulated result code 4. The separate sentence about encrypted-card integrations receiving the same response information in live does not authorize these test trigger values in live traffic. The sample request has an extra closing brace near its end and should not be copied as runnable JSON.

**Raw locators:** flow and issuer context, lines 15–24; field enablement, lines 26–32; test restriction and trigger, lines 33–60. **Canonical retrieval route:** [[adyen-payment-testing]] → [[source-adyen-docs-development-resources-testing-result-codes-cvc-cvv-cid-result-codes]] → [[raw/adyen/docs/development-resources/testing/result-codes/cvc-cvv-cid-result-codes/2026-09-15|pinned raw]].

## Q2 — CVC result versus payment result

**Query:** Does a simulated CVC table row labeled Approval prove payment authorization, and what does the example response show?

**Expected answer:** No. The table maps simulated values 0–6 to CVC descriptions and Approval/Decline expectations; it is a test fixture, not a real issuer card check or an individual payment guarantee. The example for `004` returns `additionalData.cvcResult` as code 4, `cvcResultRaw` as `S`, and overall `resultCode` as `Refused`. The CVC result and payment result are separate fields. The guide says issuer CVC checks may affect online approval and post-authorization risk rules, but it gives no shopper-disclosure rule for the detailed check or refusal information.

**Raw locators:** issuer and risk context, line 24; response example, lines 62–80; simulated result table, lines 82–92. **Canonical retrieval route:** [[adyen-payment-testing]] → [[source-adyen-docs-development-resources-testing-result-codes-cvc-cvv-cid-result-codes]] → [[raw/adyen/docs/development-resources/testing/result-codes/cvc-cvv-cid-result-codes/2026-09-15|pinned raw]].
