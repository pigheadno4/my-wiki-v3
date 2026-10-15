---
title: "Adyen test CVC/CVV/CID result-code triggers"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/result-codes/cvc-cvv-cid-result-codes"
raw_files:
  - "adyen/docs/development-resources/testing/result-codes/cvc-cvv-cid-result-codes/2026-09-15.md"
tags: [adyen, payment-testing, cvc, result-codes, checkout-api]
---

## Overview

This [[adyen]] test guide shows how an Advanced flow or Sessions flow with additional methods can simulate card CVC/CVV/CID check results before going live. It uses a test `/payments` request and a special `paymentMethod.cvc` value to select a returned `additionalData.cvcResult`. This is a test fixture for response handling, not a live issuer CVC check, card eligibility decision, shopper disclosure rule, or proof of payment authorization. See [[adyen-payment-testing]] for the wider simulation boundary.

## Key takeaways

- The merchant first enables the `additionalData.cvcResult` response field in the **test** Customer Area through **Developers → Additional data → Acquirer result**. For the exercise, the page says to use unencrypted test card details; its separate live-environment sentence says encrypted-card integrations receive the same response information, but this does not authorize using these test trigger values in live traffic.
- In a test Checkout `/payments` request, prepend `00` to a listed result-code value and put it in `paymentMethod.cvc`; for example, `004` selects result code 4. The sample response reports `cvcResult` and `cvcResultRaw` and also shows `resultCode=Refused`. The requested CVC test result and overall payment result are distinct fields.
- The table maps simulated values 0–6 to descriptions and Approval/Decline expectations. A simulated `Matches` or `Unknown` row is not evidence that a real issuer verified a real card, and a table's Approval label is not a guarantee of authorization for an individual request. The sample request JSON in the snapshot appears to have an extra closing brace near its end; use the field guidance and raw locators rather than copying it as runnable JSON.
- The page notes issuer CVC checks can affect an online transaction and feed post-authorization risk rules. It specifies response data for integration testing; it does not tell the merchant which detailed check or refusal information to show a shopper.

## Detail locators

- **Flow scope, real-issuer context, and test Customer Area field enablement:** raw lines 15–32, under `# Testing card CVC/CVV/CID result codes` and `## Requirements`.
- **Test-card restriction, `00` trigger construction, and illustrative request:** raw lines 33–60, under `## Step 1: Make a test payment request`; extra brace visible at lines 58–59.
- **Returned CVC field versus payment result example:** raw lines 62–80, under `## Step 2: Get the result code in the response`.
- **Simulated CVC result-code table:** raw lines 82–92, under `## Result code values`.

## Related

- [[adyen]]
- [[adyen-payment-testing]]
- [[source-adyen-docs-development-resources-testing-result-codes]]
- [[source-adyen-docs-development-resources-test-cards-and-credentials-test-card-numbers]]

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/result-codes/cvc-cvv-cid-result-codes/2026-09-15|Adyen CVC/CVV/CID test result-code guide — collected 2026-09-15]]
