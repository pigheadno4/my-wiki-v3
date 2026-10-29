---
title: "Afterpay iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/ios-component"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/ios-component/2026-09-15.md"
tags: [adyen, afterpay, ios, components, redirect, capture]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds Afterpay to an **existing iOS Components integration**, with separate Sessions and Advanced server-flow sections. It describes method-specific additions, not a complete base integration or evidence that a merchant is currently enabled. The related [[source-adyen-docs-payment-methods-afterpaytouch]] overview states the Afterpay AU/CA/NZ product scope and regional naming; this guide's AUD/AU examples and US sandbox-account option do not establish a wider live product scope. See [[adyen-online-payments]].

## Key takeaways

- **Sessions prerequisites and request:** The guide requires an existing iOS Components Sessions integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Afterpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` required; `telephoneNumber` is optional if provided (raw lines 38–53). The AUD/AU test request and versioned API-library examples are examples, not account eligibility or universal SDK requirements (raw lines 55–737).
- **Advanced prerequisites and request:** The Advanced section requires an existing Advanced iOS Components integration, redirect handling and Customer Area method setup; its `/payments` table adds required `paymentMethod: afterpaytouch` to the same required shopper/address/item fields and optional telephone number (raw lines 811–866). The requirement text says **iOS Components** but its base integration link has `integration=Drop-in`; follow the correct Components base guide rather than assuming the linked Drop-in route proves Component setup (raw line 819). The shown `/payments` response has `resultCode: RedirectShopper` and `action.type: redirect`, not a final payment result (raw lines 1581–1595).
- **Component setup:** Both flow sections say no Afterpay-specific configuration parameters are needed and initialize `InstantPaymentComponent` for method `afterpaytouch` after checking it is supported in returned payment methods. Sessions delegates to the session, while Advanced delegates to the merchant's component handler (raw lines 739–765, 823–848).
- **Capture boundary:** Depending on merchant account configuration, capture is automatic after authorisation or manual. Capture delay/manual capture is needed to capture after shipping, and **manual capture is required for partial capture**. The page says capture must occur within **13 days** of authorisation; the first installment is charged during authorisation, and if uncaptured by that deadline Afterpay cancels and refunds it. Test authorisations expire in **one day**, requiring manual test capture within that day (raw lines 769–777, 1597–1605).
- **Partial capture:** Manual `/payments/{paymentPspReference}/captures` specifies full or partial `amount.value`; `lineItems` is optional. An initial partial capture cancels the unclaimed balance unless the account is enabled for **multiple** partial captures. The latter requires contacting Support and creates a new invoice per capture (raw lines 779–788, 1607–1616). The guide does not give a refund procedure.
- **Test/live distinction:** The page requires an Afterpay sandbox shopper account to test, separate accounts by country/region for multiple-region tests, and a test card. Its sandbox account selector lists AU, NZ, US and CA, whereas the overview product table lists AU, CA and NZ; the sandbox option alone does not establish live US eligibility. Before live acceptance, the guide says to submit an Afterpay request in live Customer Area (raw lines 790–809, 1618–1637). No live approval or successful payment is evidenced by this capture.

## Detail locators

- Sessions requirements and `/sessions` field table: pinned raw lines 25–53; TEST curl and SDK examples lines 55–737.
- Sessions Component initialization and capture/test notes: pinned raw lines 739–809.
- Advanced requirements, mismatched base-guide link, Component setup and `/payments` fields: pinned raw lines 811–866.
- Advanced TEST examples and redirect response: pinned raw lines 868–1595.
- Advanced capture, partial-capture Support gate, test and live request: pinned raw lines 1597–1637.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — method and region overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/ios-component/2026-09-15|Afterpay iOS Component guide, captured 2026-09-15]]
