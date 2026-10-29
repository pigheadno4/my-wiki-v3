---
title: "Afterpay iOS Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/ios-drop-in/2026-09-15.md"
tags: [adyen, afterpay, ios, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen Docs page gives **Afterpay-specific additions** to an existing iOS Drop-in integration, split into Sessions and Advanced server-side flows. It links the corresponding base integration guides rather than supplying a complete returned-shopper or payment-result procedure. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-afterpaytouch]] and [[adyen]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions flow using **Checkout API v68 or later**, with Afterpay added in Customer Area (raw lines 25–34). Its `/sessions` table marks shopper name/email/reference (reference minimum three characters), country code, billing/delivery addresses and line items required; phone is optional (lines 38–51). The AU/AUD TEST examples are fixtures, not a general eligibility or successful-payment demonstration (lines 53–735).
- Neither flow needs additional **Afterpay-specific Drop-in configuration** (Sessions lines 737–741; Advanced lines 799–803). The Sessions NodeJS JavaScript and TypeScript examples use `Config` and `EnvironmentEnum.TEST` without importing them in the shown snippets (lines 374–383, 659–668). Those examples are not verified standalone setup recipes; this does not establish a general SDK defect.
- Advanced requires an existing iOS Drop-in Advanced flow, `action.type: redirect` handling and Afterpay added in Customer Area (lines 787–797). Its `/payments` table additionally specifies `paymentMethod: afterpaytouch` and the same shopper/country/address/item fields, with optional phone (lines 805–821). The sample initial response has `resultCode: RedirectShopper` and a redirect `action` (lines 1536–1550); this is not final authorisation or capture proof. Its Go request example labels the library v10.4.0 but imports `/v9/src` packages (lines 1230–1235); verify the intended module/version before copying.
- Capture can be automatic after authorisation or manual, depending on merchant-account configuration. Delayed capture needs delay setup or manual capture; partial capture needs manual capture. Afterpay requires capture within **13 days** after authorisation; otherwise it cancels and refunds the first instalment charged during authorisation. Test authorisations expire in **one day** (Sessions lines 745–753; Advanced lines 1552–1560). A partial manual capture cancels the unclaimed remainder unless **multiple partial captures** are enabled for the account; that requires contacting Support and creates a new invoice per capture (lines 755–764 and 1562–1571).
- Sandbox testing needs a shopper test account and test card, with separate accounts per test region. This child's sandbox selector lists AU, NZ, US and CA (lines 766–785, 1575–1594), while the linked Afterpay overview method matrix lists **AU, CA and NZ** and assigns the US separate Cash App Afterpay/$Afterpay branding (overview raw lines 23–31). The US test-account choice does not prove US live Afterpay eligibility. The child page says a request in live Customer Area is needed before accepting live Afterpay payments; it does not prove a specific merchant's enablement or settlement.

## Detail locators

- Page scope and Sessions requirements: raw lines 15–34.
- Sessions request table and TEST examples: lines 38–735; NodeJS snippet setup warning at lines 374–383 and 659–668.
- Sessions no-extra-configuration, capture and sandbox/live: lines 737–785.
- Advanced requirements, no-extra-configuration, request table and TEST examples: lines 787–1534; Go library/import mismatch at lines 1230–1235.
- Advanced redirect response, capture and sandbox/live repetition: lines 1536–1594.
- Related overview country/branding qualification: `raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — product/country overview and US branding.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/ios-drop-in/2026-09-15|2026-09-15 Afterpay iOS Drop-in Sessions and Advanced guide]]
