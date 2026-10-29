---
title: "Afterpay Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/android-component"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/android-component/2026-09-15.md"
tags: [adyen, afterpay, android, components, redirect]
---

## Overview

This 2026-09-15 Adyen Docs page adds **Afterpay** to an existing Android Components integration. It has separate **Sessions** and **Advanced** flow instructions, with a redirect action in both. These are method-specific additions to linked base integration guides, not an end-to-end payment-result recipe. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-afterpaytouch]] and [[adyen]].

## Key takeaways

- Sessions requires an existing Android Components Sessions flow, **Checkout API v68 or later**, redirect handling and Afterpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks `shopperName`, `shopperEmail`, `shopperReference` (minimum three characters), `countryCode`, `billingAddress`, `deliveryAddress` and `lineItems` as required; `telephoneNumber` is optional (lines 40–53). The AU/AUD TEST request at lines 55–737 is an example, not a general eligibility rule.
- Both flows import `com.adyen.checkout:instant`; the Jetpack Compose variant also imports `components-compose`. No extra Afterpay configuration parameters are given. Both launch an `InstantPaymentComponent`: Sessions gets `afterpaytouch` from the checkout session, while Advanced selects it from `/paymentMethods`. Compose samples say to generate a new Component key for a different screen/session or reset (Sessions lines 739–821; Advanced lines 877–961).
- Advanced requires an existing Android Components Advanced flow, redirect action handling and Afterpay added in Customer Area (lines 867–875). Its `/payments` table adds `paymentMethod: afterpaytouch` and the same required shopper, country, address and line-item data, with optional phone (lines 963–979). Its sample `/payments` response is `RedirectShopper` with a redirect `action` (lines 1694–1708); that initial response is not final authorisation or capture proof. The page does not itself specify the returned-shopper/details or webhook result procedure; follow the linked base flow.
- Capture can be automatic after authorisation or manual according to merchant-account configuration. Delayed capture needs delay setup or manual capture; partial capture needs manual capture. Authorisations must be captured within **13 days**, or Afterpay cancels and refunds the first instalment already charged during authorisation. Test authorisations expire in **one day** (Sessions lines 825–833; repeated for Advanced lines 1710–1718). A partial manual capture automatically cancels the unclaimed remainder unless the account is enabled for **multiple partial captures**; that feature requires contacting Support and creates a new invoice per capture (lines 835–844, 1720–1729).
- Sandbox testing needs a test shopper account, separate for each test region, and a test card. The page lists AU, NZ, US and CA in its **sandbox account selector** (lines 846–865, 1731–1750); the linked Afterpay overview's payment-method matrix lists only **AU, CA and NZ** (overview raw lines 23–31). The US sandbox selection does not establish US live Afterpay eligibility; the overview says the US service has separate **Cash App Afterpay/$Afterpay** branding. Before accepting live Afterpay payments, this child page says to submit a request in live Customer Area. No example or test status proves live enablement or a settled payment.

## Detail locators

- Scope and base-flow split: raw lines 15–25.
- Sessions requirements, request table and TEST examples: lines 25–737. In the NodeJS JavaScript and TypeScript samples, `Config` and `EnvironmentEnum.TEST` are used but not imported in the shown snippets (lines 376–385, 661–670); treat those samples as incomplete standalone setup, not evidence of a general SDK defect.
- Sessions imports, `InstantPaymentComponent`, capture and sandbox/live: lines 739–865.
- Advanced requirements, imports, `InstantPaymentComponent`, request table and TEST examples: lines 867–1692; redirect response lines 1694–1708. The Go sample labels Library v10.4.0 but imports `/v9/src` packages (lines 1388–1393); verify the intended module/version before copying.
- Advanced capture and sandbox/live repetition: lines 1710–1750.
- Related overview country/branding qualification: `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — product, country/currency and US branding overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/android-component/2026-09-15|2026-09-15 Afterpay Android Component Sessions and Advanced guide]]
