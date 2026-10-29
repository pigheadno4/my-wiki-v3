---
title: "PayBright API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/api-only"
raw_files:
  - "adyen/docs/payment-methods/paybright/api-only/2026-09-15.md"
tags: [adyen, paybright, api-only, redirect, canada, capture, refund]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, describes PayBright for an existing Web API-only integration: the merchant builds the payment form, collects shopper and item data, sends a server-side payment request, redirects the shopper and handles the return. It explicitly says PayBright was acquired by Affirm and Adyen will not accept new PayBright integrations. See [[source-adyen-docs-payment-methods-paybright|PayBright overview]], [[source-adyen-docs-payment-methods-affirm|Affirm]] and [[adyen-online-payments]]. The snapshot does not prove current enablement or completed payment execution.

## Key takeaways

- The guide assumes an existing API-only integration and PayBright added in the test Customer Area. Its `/paymentMethods` discovery example uses Canada, `countryCode: CA` and `amount.currency: CAD`. The merchant-built form must collect full name, date of birth, email, phone, billing and delivery addresses for PayBright risk checks, and the page calls for purchased-item `lineItems`. The server sends `/payments` with `paymentMethod.type: paybright`, shopper details, item data and `returnUrl`; `shopperLocale` is optional. The curl example targets Checkout API v68 TEST; library snippets name their own versions.
- Read the returned `action` and redirect the shopper to its `action.url`. For iOS GET presentation, the page recommends `SFSafariViewController` over WebView, and for mobile redirects strongly recommends the device default browser for compatibility and authentication handling. After return, send the URL-decoded `redirectResult` in `details` to `POST /payments/details`; use its `resultCode` for the shopper-facing outcome. The listed outcomes are Authorised, Cancelled and Refused. If the shopper does not return, await the AUTHORISATION webhook and inspect `success`. A redirect return or sample `Authorised` response is not itself evidence that any real payment occurred.
- The page says PayBright payments are automatically captured after authorization by default and that capture charges the first installment. For capture after shipment, the page suggests a capture delay or manual capture. It also mentions those options for partial capture, but separately says partial capture is unavailable when automatic capture is enabled in Customer Area. A delay alone does not establish partial-capture eligibility; the page does not reconcile these statements. Its `/capture` example uses `modificationAmount` and optional `additionalData.openinvoicedata`. An unclaimed balance after partial capture is automatically cancelled unless the account has multiple partial captures enabled through Support; each such capture creates a new invoice.
- Cancel before capture; refund after capture. For partial refund, the prose names `/payments/{paymentPspReference}/refunds` with `modificationAmount` and optional invoice data, while the example is a `/refund` shape with `originalReference`. The page does not reconcile these API forms, so use the applicable endpoint schema rather than combining their fields.
- The test section points to PayBright test details and says to request PayBright in live Customer Area before live payments. That instruction conflicts with the page's opening statement that Adyen accepts no new PayBright integrations; it cannot establish a route for new merchant onboarding.

> [!warning] Partial-capture example arithmetic
> The sample `modificationAmount` is CAD 45.00, but its invoice lines list shoes CAD 40.00 plus one pair of socks CAD 15.00, with no discount line. The documented values therefore do not reconcile within that example. Check the amount and invoice line details for the actual order before reusing its payload.

## Detail locators

- Acquisition and onboarding warning, API-only scope, risk inputs and CA/CAD discovery: pinned raw lines 15–53.
- Server `/payments` fields and TEST v68 curl example: lines 55–141; language-specific examples: 143–826. The example is a payment request, not a completed transaction.
- Redirect action, browser recommendations, `/payments/details` return and result codes: lines 828–895. No-return AUTHORISATION webhook path: lines 897–902.
- Automatic/partial capture, first-installment timing, unclaimed-balance cancellation and Support gate: lines 904–963. Cancel/refund lifecycle and endpoint/example mismatch: lines 965–1009.
- Test/live instructions and contradiction with the opening warning: lines 1011–1017.

## Related

- [[adyen-online-payments]] — provider online integration concept
- [[source-adyen-docs-payment-methods-paybright]] — CA/CAD method overview and no-new-integration warning
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm method

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/api-only/2026-09-15|PayBright API-only guide, fetched 2026-09-15]]
