---
title: "Adyen Mirakl connector test and go-live guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/test-and-go-live"
raw_files:
  - "adyen/docs/plugins/mirakl/test-and-go-live/2026-09-15.md"
tags: [adyen, mirakl, marketplace, testing, go-live]
---

## Overview

This 2026-09-15-captured guide gives a **Mirakl Marketplace connector** test checklist followed by separate live connector configuration and pilot-seller checks. It recommends test-environment integration testing first, then live testing with a small number of sellers because real payouts cannot be tested in Adyen's test environment. It describes checks to perform, not results for any actual merchant or seller. See [[adyen-mirakl]] and [[adyen]].

## Key takeaways

- **Test scope and seller identity:** The checklist covers Mirakl seller onboarding/synchronization to Adyen, Hosted Onboarding Page KYC including a failed-KYC seller, and connector operator emails. A synchronized seller or test KYC scenario does not establish a verified live seller, actual marketplace permission or payout eligibility.
- **Payment and modification checks:** Test `/payments` for use cases with split data **excluding commissions**, and verify `applicationInfo` appears in Customer Area. Test full and partial captures; each partial capture should have a unique reference so amounts remain separately reconcilable rather than merged. Test partial/full refunds and chargebacks; the guide restricts refunds to a balance account in the original split payment/capture using the same unique split reference. These are requested test flows, not proof of authorization, capture, refund or dispute outcome.
- **Billing-cycle check versus bank receipt:** The guide asks for seller invoice generation in Mirakl, invoice presence in Customer Area, and Mirakl marking it **Paid** after seller payout. A report or invoice label alone does not prove bank receipt; the guide explicitly directs a small **live** pilot to ensure payouts reach seller bank accounts because real payouts are unavailable in test.
- **Live setup gate and side effects:** After satisfactory test results, an Adyen contact can configure the connector in the live environment. Before contacting them, check Mirakl Operator API key roles, live **KYC Status** and **Payment Confirmation** features, and a small starter seller list. By default, the connector manages seller payment blocking and unsuspends newly KYC-verified shops; the operator can ask Adyen to disable either behavior. Those defaults can affect seller operation, so confirm desired controls before live configuration. The page gives no migration cutoff, merchant-of-record allocation or grant of live approval.

## Detail locators

- Lines 15–23: test-first and limited live-pilot sequence.
- `### KYC` and `### Payments`, lines 25–33: synchronization, pass/fail KYC, split data excluding commission and `applicationInfo`.
- `### Captures` and `### Refunds`, lines 35–52: full/partial captures, unique references and refund balance-account/split-reference restriction.
- `### Payouts` and `### Operational checks`, lines 54–62: invoice/payout label and operator email checks.
- `## Go live`, lines 64–77: Adyen live setup, Operator API key roles, feature flags and default seller blocking/unsuspension.
- `### Test in live environment`, lines 79–90: inability to test real payout in test, pilot sellers and repeated checks.

## Related

- [[adyen-mirakl]] — connector ownership and separate pay-in boundary.
- [[source-adyen-docs-plugins-mirakl-set-up-the-connector]] — Operator key roles, feature flags and connector settings.
- [[source-adyen-docs-plugins-mirakl-set-up-payment-flows]] — operator-implemented payment/split behavior.
- [[source-adyen-docs-partners-application-information]] — `applicationInfo` partner-request metadata.

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/test-and-go-live/2026-09-15|Mirakl connector test and go-live, captured 2026-09-15]]
