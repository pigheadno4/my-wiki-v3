---
title: "Adyen testing risk features"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/risk-features"
raw_files:
  - "adyen/docs/development-resources/testing/risk-features/2026-09-15.md"
tags: [adyen, payment-testing, risk-management, avs, auto-rescue, chargebacks]
---

## Overview

This Adyen **test-only** guide routes merchants through simulated chargebacks, configured risk-rule triggers, AVS fixtures and Auto Rescue scenarios before going live. It is a set of testing entry points and example triggers, not proof of production risk rules, issuer AVS responses, live chargebacks, authorization rates or successful recovery. See [[adyen]], [[adyen-payment-testing]] and [[adyen-risk-management]].

## Key takeaways

- **Chargebacks:** the guide links to a chargeback-simulation flow, then says a simulated dispute can be handled in test Customer Area or the Disputes API. The detailed prerequisites, timing and supported scenarios belong to that separate guide; this page does not turn a test chargeback into a live dispute.
- **Risk rules:** the page uses the legacy **RevenueProtect** name and conditions rule testing on risk rules already turned on and configured. It links to a specific risk-rule trigger guide. No unconditional rule execution or actual fraud decision follows from the link.
- **AVS:** billing-address details must be included in the payment request to enable and test AVS. The page lists test-card/address fixtures, then instructs making a test card payment and looking up the AVS result in the corresponding PSP reference's API response or webhook. The fixture data and response route do not establish what a live issuer will return; use the dedicated AVS guide for its scheme/region and simulated-response qualifications.
- **Auto Rescue:** enable the feature in **test Customer Area** for shopper-not-present transactions, such as subscription renewals. The listed test `merchantReference` trigger strings cover a first-retry success, second-retry success, all retries failing, and fraud refusal with **no retry**. For triggered retry scenarios, the guide says an `AUTHORISATION` webhook arrives for each retry and its `success` field reports that retry's result. The page calls the trigger input `merchantReference` in a test `/payments` request; use this as a documented fixture label, not an independently verified Checkout request schema.
- The optional **Pay by Link after failed rescue** path applies **if the merchant enabled sending a link**. The test sequence uses the all-fail trigger, receives an `AUTORESCUE` webhook with `paymentLink.url`, opens and completes a separate Pay by Link test payment, then receives an `AUTHORISATION` webhook. A failed rescue does not imply automatic link delivery without that setting, and the link/payment webhooks do not prove a live recovery or settlement.

## Detail locators

- `## Chargebacks` and `## Risk management` (lines 19–28): simulation route and configured legacy risk-rule condition.
- `## Address Verification System (AVS)` (lines 30–52): billing-address prerequisite, test fixtures and PSP-reference response/webhook lookup.
- `## Auto Rescue` and `### Retry attempts` (lines 54–69): test-environment enablement, shopper-not-present scope, `merchantReference` triggers and per-retry webhook signal.
- `### Failed retry attempt that sends a payment link` (lines 71–81): optional setting, all-fail trigger, `AUTORESCUE` link URL and distinct link-test payment.

## Related

- [[adyen-payment-testing]] — primary test-fixture concept and reciprocal source route.
- [[adyen-risk-management]] — risk-setting context.
- [[source-adyen-docs-risk-management-disputes-api-test-applicable-dispute-reasons]] — detailed simulated chargeback route.
- [[source-adyen-docs-risk-management-avs-checks]] — AVS support, simulated response and rule timing.
- [[source-adyen-docs-online-payments-auto-rescue]] — non-test Auto Rescue overview and webhook conditions.

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/risk-features/2026-09-15|Testing risk features, captured 2026-09-15]]
