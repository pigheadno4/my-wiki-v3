---
title: "Adyen PayBright iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paybright/ios-drop-in/2026-09-15.md"
tags: [adyen, paybright, affirm, ios, drop-in, buy-now-pay-later]
---

## Overview

Adyen's captured iOS Drop-in guide describes adding PayBright to an existing Sessions or Advanced integration. It opens with a material lifecycle warning: PayBright was acquired by Affirm and Adyen will not accept new PayBright integrations. The later live section still describes requesting PayBright in live Customer Area; treat that as legacy setup text, not evidence that new onboarding is open. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Use an existing iOS Drop-in Sessions or Advanced flow and add PayBright in Customer Area for an existing integration. The page calls `/sessions` the Drop-in v5.0.0-or-later default, with `/payments` for an additional use case. Neither Drop-in v5+ nor v4.x.x has required PayBright-specific client configuration.
- Both API tables mark `shopperName` (first and last), `dateOfBirth`, `shopperEmail`, `telephoneNumber`, `countryCode`, `billingAddress`, and a unique `shopperReference` of at least three characters as required. `deliveryAddress` falls back to billing address if absent/blank; `shopperLocale` and `lineItems` are optional, with line items recommended for approval. The examples are Canadian (`countryCode: CA`) and use an iOS return URL, but many required-field and currency values are empty placeholders. Some /payments Java/PHP examples use USD while most others leave currency blank; these snippets do not establish an accepted currency or runnable request.
- By default, the guide says PayBright payments capture automatically after authorization; capturing after goods ship or making a partial capture requires capture delay or manual capture. At capture, the shopper is charged the first installment. Partial capture is unavailable when automatic capture is enabled in Customer Area. A legacy `/capture` example uses `modificationAmount` and optional `additionalData.openinvoicedata`; unclaimed amount after partial capture is automatically cancelled unless the account is enabled for multiple partial captures. Multiple partial captures require Support setup and create a separate invoice per capture.
- The guide separates cancel before capture from refund after capture. Its partial-refund prose links Checkout `/payments/{paymentPspReference}/refunds` but names `modificationAmount` and `additionalData.openinvoicedata`, and the example is labeled `/refund` with `originalReference`. Treat this as a mixed endpoint/request-shape example and verify the selected API before implementation.
- The final “See also” integration guide links to iOS **Components** even though this is a Drop-in page. Test details and test Customer Area status are documented, but do not establish live payment success; the stated no-new-integration warning remains controlling for new onboarding.

## Detail locators

- No-new-integration warning and Sessions/Advanced requirements: raw lines 15–40.
- /sessions field table and TEST v69 sample: raw lines 41–126; language-library examples through line 788. /payments field table and TEST v72 snippets: lines 789–1310. The /payments Java/PHP USD values conflict with blank currency in curl and other examples (lines 886–887, 975–976).
- No required Drop-in configuration for v5+ or v4.x.x: raw lines 1312–1320.
- Default capture, partial capture and remainder behavior: raw lines 1322–1381. Cancel/refund and mixed partial-refund endpoint wording: lines 1383–1427.
- Testing, live request text and mismatched Components “See also” link: raw lines 1429–1441.

## Related

- [[adyen-online-payments]] — provider integration context.
- [[adyen-payment-capture]] — general capture lifecycle.
- [[adyen-refunds]] — general refund lifecycle.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/ios-drop-in/2026-09-15|PayBright iOS Drop-in, captured 2026-09-15]]
