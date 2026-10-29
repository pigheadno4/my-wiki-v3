---
title: "Adyen MB WAY Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mb-way/web-drop-in/2026-09-15.md"
tags: [adyen, mb-way, web, drop-in, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds MB WAY to an existing Web Drop-in integration. It separates Sessions and Advanced request additions, shows `Pending` with an await action, and includes an optional **mobile** App2App branch inside the Web page. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-mb-way]] for the PT/EUR payment-method overview.

## Key takeaways

- **Sessions:** use an existing Web Drop-in Sessions flow, Checkout API **v68 or later**, and MB WAY added in Customer Area. The `/sessions` table marks `shopperStatement` required as bank-statement text. The TEST v71 PT/EUR request is illustrative; its `adyencheckout://your.package.name` `returnUrl` is mobile styled in this Web guide, so configure the actual Web return path from the base integration. See raw lines 25–66.
- `MBWay` can be imported individually with Adyen Web/Dropin for optional tree shaking and performance optimization. This is optional in both Sessions and Advanced sections, not a prerequisite to use MB WAY. See raw lines 68–78 and 115–125.
- **Advanced standard Web flow:** use the existing Web Drop-in Advanced flow, handle `action.type: await`, and add MB WAY in Customer Area. The `/payments` table requires `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber`; `shopperStatement` is not marked required here. The TEST v72 example yields `resultCode: Pending` and an await action for a waiting screen while the shopper completes payment in MB WAY. Pending is not final authorization. The v68 minimum is stated in the Sessions requirements table only; do not extend it to Advanced from this page. See raw lines 103–180.
- **Optional mobile App2App branch:** the page says `channel: iOS` or `Android` plus `returnUrl` removes manual phone entry and links directly to the MB WAY app; omitted or Web `channel` uses the standard phone-number flow. For a successful request, `action.url` contains an `mbway://` deep link with the supplied return URL appended. Open the returned action URL; after authorization in MB WAY the shopper is redirected back to the application. This mobile branch appears within a Web Drop-in guide and does not remove the standard Web phone requirement or make app return a final payment result. See raw lines 182–237.
- Test instructions allow any telephone number (example `+351234567890`), direct status checks to test Customer Area, and give `shopperStatement` suffixes for `/payments` test responses: `-c1` Authorised/default, `-c3` Pending, `-c5` Refused. Live acceptance requires adding MB WAY in live Customer Area. The Sessions section also phrases these suffixes as `/payments` requests; do not claim `/sessions` suffix behavior from that example. See raw lines 80–101 and 239–260.

## Detail locators

- Sessions prerequisites, field and TEST request: raw lines 25–66. The curl sample omits a shell continuation after `-X POST`.
- Optional Web import: raw lines 68–78 and 115–125.
- Advanced prerequisites, field table and Pending/await response: raw lines 103–180.
- Mobile App2App channel, deep link and return: raw lines 182–237; the JSON snippets contain inline comments and are illustrative, not literal parseable JSON.
- Test result-code suffixes and live setup: raw lines 80–101 and 239–260.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/web-drop-in/2026-09-15|Fully read MB WAY Web Drop-in raw]]
