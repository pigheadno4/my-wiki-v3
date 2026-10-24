---
title: "Adyen Touch'n Go API-only redirect integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/api-only"
raw_files:
  - "adyen/docs/payment-methods/touchngo/api-only/2026-09-15.md"
tags: [adyen, touchngo, malaysia, api-only, redirect, online-payments]
---

## Overview

This Adyen guide, last modified 2019-09-06 and captured 2026-09-15, describes adding **Touch'n Go to an existing API-only integration** with a merchant-owned form and a redirect wallet payment flow. It documents example requests, return handling and result/webhook branches; none proves current merchant eligibility or that a particular payment was authorized. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Setup and discovery:** The page requires an existing API-only integration and instructs the merchant to contact Adyen Support for Customer Area addition before beginning. It says no shopper information needs collecting in the Touch'n Go payment form. For `/paymentMethods`, it specifies `countryCode: MY`, `amount.currency: MYR` and an amount value. This is the guide's method-discovery scope, not a claim that every merchant can currently enable it. (raw lines 21–38)
- **Server request and action:** The merchant sends `/payments` with `paymentMethod.type: touchngo`; the illustrative TEST request also shows merchant account, reference, MYR amount and `returnUrl`. The sample response has `resultCode: RedirectShopper` and an `action` with GET URL and `type: redirect`. This is an instruction to send the shopper through the wallet redirect, not a final payment result. (raw lines 40–64, 347–361)
- **Redirect and return:** The guide instructs redirecting to `action.url`. For in-app GET redirects it recommends SFSafariViewController or Chrome Custom Tabs over WebView and strongly recommends the device default browser for mobile compatibility. After the shopper returns to the website, the server POSTs `/payments/details` with the URL-decoded `redirectResult`, then uses `resultCode` for shopper messaging and `pspReference` as transaction ID. Its examples use a **v68** TEST `/payments` URL and a **v72** TEST `/payments/details` URL; the page does not state an overall minimum API version or prove the examples were executed together. (raw lines 49–64, 363–406)
- **Outcome branches:** `Authorised` is the successful result described by the page; `Error` and `Refused` have separate failure guidance. For `Pending` or `Received`, the shopper has completed the payment step but the **final result is not yet known**: inform the shopper that the order was received and await an `AUTHORISATION` webhook. The guide says the offer closes if not authorised within **30 minutes**, with optional `OFFER_CLOSED` notification. If the shopper closes the browser and does not return, use webhooks; `AUTHORISATION`/success=false is failure and success=true is completion. A return redirect, the sample `Authorised` body, or a pending code alone is not observed authorization or settlement. (raw lines 404–423)
- **TEST/live boundary:** The page points to test-payment status in the test Customer Area. For live acceptance it separately says to contact Adyen Support to add Touch'n Go in the **live Customer Area**. A TEST request or Support instruction is not proof that live processing has been enabled. (raw lines 424–428)

## Detail locators

- API-only and Support prerequisites; MY/MYR discovery: raw lines 15–38.
- `touchngo` request type, TEST v68 sample and redirect action: raw lines 40–64, 347–361.
- App/browser redirect recommendations and returned `redirectResult` v72 details call: raw lines 363–406.
- Result codes, 30-minute pending limit and webhook fallback: raw lines 404–423.
- Test versus live Customer Area instructions: raw lines 424–428.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/api-only/2026-09-15|Adyen Touch'n Go API-only guide, 2026-09-15 snapshot]]
