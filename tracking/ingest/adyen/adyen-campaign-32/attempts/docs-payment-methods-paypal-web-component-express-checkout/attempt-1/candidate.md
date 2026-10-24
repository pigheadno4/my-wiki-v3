---
title: "Adyen PayPal Express Checkout Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/web-component/express-checkout"
raw_files:
  - "adyen/docs/payment-methods/paypal/web-component/express-checkout/2026-09-15.md"
tags: [adyen, paypal, express-checkout, web-components, wallets]
---

## Overview

This [[adyen]] guide describes rendering a PayPal Express Checkout button outside the usual checkout page, such as on a product page, using an existing PayPal **Web Component** integration and Web Component **v5.59.0 or later**. It covers **Sessions** and **Advanced** flows, PayPal lightbox delivery changes, Adyen order updates, and optional Advanced-flow review. The captured page is dated 2026-09-15, but its metadata says last modified 2023-04-04 while its v5.59.0 prerequisite links a 2024-02-26 release note; the metadata and body chronology conflict. See [[adyen-online-payments]].

## Key takeaways

- **Flow identity:** In Sessions, the merchant server creates a `/sessions` payment session and stores `sessionId`; in Advanced, `onSubmit` leads the **merchant server** to call `/payments`, and it stores the response `pspReference`. The top-level Advanced sketch says the Component makes `/payments`, whereas the detailed step assigns that call to the server; preserve the server boundary. The PayPal lightbox may show delivery methods for the default address or omit them. Address and, when shown, method changes can alter the final amount. See pinned raw lines 19–59, 73–79 and 962–966.
- **Amount updates and latest state:** If the final amount changes, a server endpoint calls Checkout `/paypal/updateOrder`: Sessions identifies the order with `sessionId`, Advanced with `pspReference`. Both carry the current `paymentData` and the new amount in minor units including delivery fees and tax; `taxTotal` is additional when supplied, and its tax must also be included in the payment amount. Address/method fields depend on what changed and whether methods are shown, with one selected method in the examples. Each successful update returns a **new** `paymentData` to pass back to the Component; reusing an earlier blob is contrary to the page. A failed update can return `errorCode`, `errorType` and `message`, and the example rejects multiple selected methods. The broad “no additional action” statement for unchanged amount sits beside later instructions to make an **initial** update when `onShippingAddressChange` fires as the lightbox opens; apply that distinction carefully rather than dropping the initial callback. See pinned raw lines 81–104, 837–861, 968–992 and 1725–1749.
- **Client callbacks and completion:** Set `isExpress: true`. The guide uses PayPal `onShippingAddressChange` on lightbox open and later address changes, and `onShippingOptionsChange` only when default delivery methods are presented; examples call a merchant backend update function and replace the Component's payment data. Rejected shipping choices and update errors need handling. For Sessions it says the Component makes an authorization request and `onPaymentCompleted` can redirect to a confirmation page; for Advanced the merchant implements `onAdditionalDetails` and sends `state.data.details` plus `state.data.paymentData` to server `/payments/details` for authorization. Closing the PayPal lightbox, receiving shopper details, invoking a callback, or submitting details does not by itself prove authorization, capture, settlement or payout. See pinned raw lines 863–958 and 1751–1878.
- **Review-page boundary:** An extra payment review page is **not available with Sessions**. Advanced can set `userAction: 'continue'`, collect shopper details and final `state.data` after the lightbox, then wait for the shopper's **Pay** action on the merchant review page before `/payments/details`. This differs from immediate Advanced detail submission. The request examples around `/payments/details` contain malformed JSON (including an unterminated `"details` key and unquoted member names), so use them as field locators, not executable payloads. See pinned raw lines 1841–1958.
- **Tokenization and example limits:** The page says PayPal Express supports recurring tokens and strongly **recommends** explicit shopper permission for future charges. It forbids zero-value authorizations to create a token and says token creation fails if the PayPal configuration includes `intent: "tokenize"`; other token behavior is delegated to linked general guides. The many test v72 and language-SDK examples are illustrative, with a USD narrative/curl versus EUR library snippets and Go v10.4.0 labels importing `/v9/` paths. They do not prove current PayPal merchant enablement, working code, consent, token creation or a live payment outcome. See pinned raw lines 104–835, 992–1723 and 1960–1973.

## Detail locators

- Existing PayPal Web Component, v5.59.0+, Sessions/Advanced sketches and lightbox modes: pinned raw lines 19–59.
- Sessions `/sessions`, `sessionId`, `/paypal/updateOrder` fields and test v72 examples: pinned raw lines 69–861. The narrative/curl uses USD but several language snippets use EUR (lines 104–172).
- Sessions `isExpress`, address/method callbacks, shopper details and `onPaymentCompleted`: pinned raw lines 863–958.
- Advanced `/payments`/`pspReference`, `/paypal/updateOrder` fields and examples: pinned raw lines 960–1749.
- Advanced callbacks, `/payments/details`, optional review page, `userAction` and malformed JSON snippets: pinned raw lines 1751–1958.
- Recurring consent recommendation and tokenization exceptions: pinned raw lines 1960–1973.

## Related

- [[adyen-online-payments]] — main online-wallet payment route.
- [[adyen-tokenization]] — general recurring consent and token lifecycle.
- [[source-adyen-docs-payment-methods-paypal-web-component]] — prerequisite PayPal Web Component guide; this page does not replace its setup.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/web-component/express-checkout/2026-09-15|PayPal Express Checkout Web Component guide, captured 2026-09-15]]
