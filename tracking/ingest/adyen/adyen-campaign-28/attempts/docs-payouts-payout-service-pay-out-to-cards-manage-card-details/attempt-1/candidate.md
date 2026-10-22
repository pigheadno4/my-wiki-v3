---
title: "Adyen Payout Service third-party card-detail preparation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/manage-card-details"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-cards/manage-card-details/2026-09-15.md"
tags: [adyen, payout-service, card-payouts, tokenization, checkout-api]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Payout Service guide prepares **third-party recipient cards** for later payout requests. It uses Checkout API `/payments` to check card payout eligibility through a zero-value authorization and, where needed, tokenize card details; the actual card payout is a separate Transfers API step linked at the end. This Payout Service path is distinct from the legacy Online Payout API card-payout guide. See [[adyen-card-payouts]] and [[adyen-financial-products]].

## Key takeaways

- **Access and card-data boundary:** The page requires a Payout Service integration, Checkout API for tokenization, relevant Checkout/recurring/encrypted-card or raw-PCI credential roles, webhook reception and Adyen feature enablement. Only a fully PCI-compliant integration may send raw card data in API requests; otherwise it must use the Card Component to collect and encrypt details. A non-fully-PCI integration, or one planning recurring card payouts, must tokenize before the payout request. Do not treat raw-card examples as permission to handle card data outside that condition. See pinned raw lines 19–43.
- **Eligibility probe:** After enabling additional response data in Customer Area, send Checkout `POST /payments` with amount value `0`, card-applicable currency, card details, merchant account, unique reference and return URL. `additionalData.payoutEligible` values have scheme-specific meaning: `Y` means eligible, `D` is Mastercard domestic-only but Visa not applicable, and `N`/`U` are not eligible. `fundsAvailability` is returned only for `Y`/`D`; `I` means Visa fast-funds support but for Mastercard denotes prepaid or debit product type. The test examples' `resultCode: Authorised` and eligibility fields do not prove that a later payout will succeed. See pinned raw lines 45–78 and 793–847.
- **Tokenization request and timing:** The guide uses a separate Checkout `/payments` request, optionally combined with a zero-auth probe, with `enablePayOut: true`, `storePaymentMethod: true`, billing address, cardholder `shopperReference`, and `recurringProcessingModel` set to `CardOnFile` for one-off or `Subscription` for recurring payouts. It says the token is created after a successful payment authorization. The `storedPaymentMethodId` is available in the successful authorization response only when additional data was enabled, or in the `recurring.token.created` webhook. Store that ID together with the tokenization shopper reference and supply both for the later card payout request. See pinned raw lines 849–874 and 1845–1909.
- **Version/example boundary:** The curl snippets target Checkout test v68; SDK snippets show several older per-language versions and placeholder data. They are implementation illustrations, not live account eligibility or card-funding evidence. The page does not itself execute a Transfers API disbursement or establish cardholder receipt. See pinned raw lines 82–790, 876–1843 and 1911–1915.

## Detail locators

- Product purpose, PCI boundary, roles and account enablement: pinned raw lines 15–43.
- Additional-data configuration and zero-auth request constraints: pinned raw lines 45–80.
- Raw/encrypted test request variants and scheme-specific eligibility response: pinned raw lines 82–847.
- Tokenization conditions, required request parameters and test examples: pinned raw lines 849–1843.
- Authorization-to-token transition, token location/pairing and next-step route: pinned raw lines 1845–1915.

## Related

- [[adyen-card-payouts]] — reciprocal card-payout concept; distinguishes Payout Service from legacy Payout API.
- [[adyen-financial-products]] — Payout Service product-family context.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/manage-card-details/2026-09-15|Payout Service card-detail guide, captured 2026-09-15]]
