---
title: "Adyen MB WAY iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/ios-component"
raw_files:
  - "adyen/docs/payment-methods/mb-way/ios-component/2026-09-15.md"
tags: [adyen, mb-way, ios, component, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds MB WAY to an existing iOS Components integration. It covers Sessions and Advanced flows, including `MBWayComponent`, an Advanced `Pending`/await action, and an optional mobile App2App switch. The latter changes the phone-number condition; do not collapse it into the standard flow. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-mb-way]] for the method overview.

## Key takeaways

- **Sessions:** start with an existing iOS Components Sessions flow, **Checkout API v68 or later**, and MB WAY added in Customer Area. The `/sessions` table marks `shopperStatement` required, describing the bank-statement text. No additional MB WAY configuration parameters are specified. Initialize using `MBWayComponent` after checking that `MBWayPaymentMethod` is available; the example delegates to the session. The v71 PT/EUR request and custom-scheme `returnUrl` are test examples. See raw lines 25–97.
- **Advanced standard flow:** start with an existing iOS Components Advanced integration, handle the additional `action.type: await`, and add MB WAY in Customer Area. No extra method configuration is specified; initialize `MBWayComponent` and delegate to the Component handler. The `/payments` table requires `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber`; `shopperStatement` is shown without a required mark. Its TEST v72 example returns `resultCode: Pending` with an await action to display a waiting screen while the shopper completes payment in MB WAY. Pending and app return are not final authorization. See raw lines 120–215.
- **Optional App2App under Advanced:** to skip manual phone entry, send `channel: iOS` (the page also names Android) and `returnUrl` with `paymentMethod.type: mbway`. If `channel` is missing or `Web`, the standard phone-number flow applies. A successful request returns an action whose `url` contains an `mbway://` deep link with the return URL appended; open that action URL directly, without an intermediate glue page. After authorization in MB WAY, the shopper returns through `returnUrl`, but the page does not equate that return with final payment status. See raw lines 217–273.
- The Advanced requirements row is labeled iOS Components but links a base URL selecting `integration=Drop-in`; nearby action and payment links select Components. Confirm the intended Components base flow. The App2App request/response snippets include inline comments in JSON, so they are illustrations rather than literal parseable JSON. See raw lines 126–130 and 230–265.
- For testing, the page says any phone number can be used (example `+351234567890`), directs status checks to test Customer Area, and lists `shopperStatement` suffixes `-c1` (Authorised/default), `-c3` (Pending), `-c5` (Refused) for `/payments` test responses. Live acceptance requires adding MB WAY in live Customer Area. The Sessions subsection also points to a `/payments` request for these suffixes; do not infer they are demonstrated through `/sessions`. See raw lines 99–118 and 275–294.

## Detail locators

- Sessions prerequisites, required statement, TEST request and Component setup: raw lines 25–97.
- Advanced prerequisites, component, request table and Pending action: raw lines 120–215.
- App2App channel/return/deep-link flow: raw lines 217–273.
- Test numbers, result-code suffixes and live Customer Area: raw lines 99–118 and 275–294.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/ios-component/2026-09-15|Fully read MB WAY iOS Component raw]]
