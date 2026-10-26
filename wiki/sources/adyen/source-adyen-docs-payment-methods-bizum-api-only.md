---
title: "Bizum for API only"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bizum/api-only"
raw_files:
  - "adyen/docs/payment-methods/bizum/api-only/2026-09-15.md"
tags: [adyen, bizum, api-only, online-payments, redirect]
---

## Overview

Adyen's 2026-09-15 Bizum guide adds the method to an existing Web API-only Advanced-flow integration. It covers method discovery, a Bizum `/payments` request, a POST redirect, `/payments/details` after return, and shopper-facing result handling. It is a documentation snapshot, not evidence of current merchant eligibility or a completed live transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The existing integration must handle `action.type: redirect`. The guide directs activation to obtain a MID and Terminal ID and adding Bizum in Customer Area before starting (raw lines 23–30).
- For `/paymentMethods`, specify `countryCode: ES` and `amount.currency: EUR` to include Bizum in the response (lines 45–52). The response showing `type: bizum` is an example (lines 330–341), not a promise for every account.
- The form section states no additional fields are required (lines 39–43). The Bizum `/payments` section marks a unique alphanumeric `reference` of 4–125 characters required (lines 343–350); its example uses `paymentMethod.type: bizum` and a `returnUrl` (lines 351–373).
- The `/payments` response includes a redirect action (lines 661–684). The guide says to POST to `action.url` with action `data` key-value pairs using `x-www-form-urlencoded`, then send the URL-decoded `redirectResult` to `/payments/details` after the shopper returns (lines 686–711).
- Use the `/payments/details` `resultCode` for the shopper display, while the AUTHORISATION webhook conveys the asynchronous outcome; when the shopper does not return, wait for webhooks (lines 942–974). `Pending` or `Received` means the final result is unknown, and `Authorised` is described as sent to the bank for processing; manual capture still requires capture (lines 960–966).

## Detail locators

- Integration requirements and flow: raw lines 19–43.
- Discovery request, ES/EUR conditions, sample Checkout v72 and library versions: raw lines 45–341.
- `/payments` parameter table and examples: raw lines 343–657. The table prints a reference regex ending `$)`; use the prose length/character condition and verify the expression before implementing it.
- Redirect action, POST and details request: raw lines 659–940. The `/payments/details` examples use older library versions than the earlier `/payments` examples (for example Java v27.0.0 versus v40.0.1); they do not establish one combined library recipe.
- Results, webhook actions and test fixtures: raw lines 942–989. Test guidance names `telephoneNumber: 700 000 000`, although the form section says no additional fields and the displayed `/payments` request omits it. The test amounts have stated outcomes only for less than 10 and more than 15; the page gives no outcome for the interval between them.
- Source wording conflict: “How it works” says the payment request includes additional information about intended purchase items (raw line 36), but the method-specific `/payments` parameter table lists only `reference` (lines 343–350). Do not infer an item schema from this page.

## Related

- [[adyen-online-payments]] — main Adyen online-payments concept and route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bizum/api-only/2026-09-15|Bizum for API only, captured 2026-09-15]]
