---
title: "Adyen ANCV API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ancv/api-only"
raw_files:
  - "adyen/docs/payment-methods/ancv/api-only/2026-09-15.md"
tags: [adyen, ancv, api-only, await, partial-payments, online-payments]
---

## Overview

This captured [[adyen]] guide adds ANCV to an existing Web Advanced-flow API-only integration. It describes FR/EUR method discovery, required ANCV beneficiary identification, an `await` action and waiting screen, `/payments/details` outcome retrieval, partial authorization, and test/live setup. It is method-specific guidance under [[adyen-online-payments]], not proof of current merchant enablement or an operational payment.

## Key takeaways

- **Prerequisites and discovery:** The page assumes an existing API-only integration able to handle `action.type: await`, with ANCV added in Customer Area. To display ANCV, it specifies `countryCode: FR` and `amount.currency: EUR` for `/paymentMethods`; the response example has type `ancv`. Discovery inputs and example response do not guarantee account or shopper eligibility (raw lines 23–58, 335–347).
- **Request and shopper identity:** The `/payments` table marks `paymentMethod.type: ancv` and `paymentMethod.beneficiaryId` required. The beneficiary ID is the shopper's ANCV ID collected during checkout, either an email address or 11-digit value. The example request includes an `order` object with PSP reference and `orderData`; that example does not by itself make `order` universally required on an initial payment (raw lines 349–385).
- **Await and status sequence:** The `/payments` response example has `resultCode: Pending`, an `await` action, and `action.paymentData`. The shopper must finish in the ANCV app while the merchant shows a waiting screen. The guide says to send the paymentData from `/payments` to `/payments/details` to obtain status and to **ignore `order.orderData` in the `/payments` response**, using the value from `/payments/details` instead for partial-payment continuation. The examples show `PartiallyAuthorised` with remaining amount and `Authorised` with zero remaining, followed by an `AUTHORISATION` webhook after shopper completion (raw lines 728–839).
- **Partial authorization visibility:** The guide warns that Customer Area may show only the requested amount when the shopper authorizes less. It says the correct authorized amount is in `/payments/details` and the `AUTHORISATION` webhook's `additionalData.authorisedAmountValue`. The partial response's 2500 requested/2400 authorized/100 remaining figures are illustrative, not a real transaction or guaranteed outcome (raw lines 780–808, 871–903). The ANCV overview separately says merchants handling partial authorization must use the partial-payments feature.
- **Testing and example caveats:** ANCV supplies the test app onboarding and credentials directly to the merchant; the page calls for end-to-end and partial-payment testing. Live setup requires adding ANCV in live Customer Area and providing the ANCV Merchant ID (`shopID`). The discovery and payment curl examples put `-X POST` on a line without a continuation before `-d`. The `/payments/details` example is fenced as JSON though it is a curl command and lacks a closing shell quote; the partial details and partial webhook JSON examples omit commas. Treat these snippets as illustrative, not copy-ready (raw lines 62–70, 363–368, 767–808, 873–903, 905–909).

## Detail locators

- Purpose, prerequisites and method discovery: pinned raw lines 15–58; discovery examples: lines 60–347.
- Required ANCV payment fields and request examples: pinned raw lines 349–726.
- Await/Pending action, waiting screen and details outcomes: pinned raw lines 728–839.
- Webhook, partial authorized amount caveat and test/live: pinned raw lines 839–913.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-ancv]] — captured ANCV overview and partial-payment orderData rule.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ancv/api-only/2026-09-15|ANCV API-only guide, captured 2026-09-15]]
