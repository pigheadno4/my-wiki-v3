---
title: "Multibanco API-only integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/api-only"
raw_files:
  - "adyen/docs/payment-methods/multibanco/api-only/2026-09-15.md"
tags: [adyen, multibanco, api-only, voucher, portugal]
---

## Overview

This 2026-09-15-captured Multibanco API-only page gives method-specific additions to an existing **Advanced-flow API-only** integration. It names a `voucher` action, PT/EUR discovery, no extra Multibanco `/payments` parameters, and test/live Customer Area setup. It relies on the main integration guide and does not demonstrate voucher redemption or a successful live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for voucher lifecycle.

## Key takeaways

- Prerequisites are an existing API-only integration, additional-action handling for `action.type: voucher`, and Multibanco added in Customer Area. For `/paymentMethods`, the page specifies `countryCode: PT` and `amount.currency: EUR`; an example response includes method type `multibanco`, not a guarantee it will appear for every merchant (raw lines 23–29, 46–85).
- The page says the merchant-built payment form need not collect shopper information, and says **no additional Multibanco parameters** are needed for `/payments`. This is method-specific add-on guidance, not a complete base request schema. The workflow's purchased-item sentence has no corresponding method-specific item/order-line field; do not invent one from that prose (raw lines 31–44, 87–89).
- Before testing, submit a Multibanco request in the **test Customer Area**. In test, simulate a pending offer becoming a sale by selecting its PSP reference under **Payments > Offers** and choosing **Promote offer to sale**; use that to test reconciliation. Paid payments, including promoted test offers, appear in **Payment list**. A separate request in the **live Customer Area** is needed before live acceptance. Test promotion does not prove a real shopper redeemed a voucher (raw lines 91–106).

> [!warning] Contradiction — fulfillment timing conflicts with voucher lifecycle
> The child page's “How it works” step 4 says to fulfill the order after making the payment request (raw lines 31–36). The [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] says the shopper receives a voucher at checkout and later pays at an ATM or online bank (overview pinned raw lines 23–32); the child itself calls test payments pending offers until promotion (raw lines 93–104). Do **not** infer payment finality or ship goods merely from a `/payments` request or voucher action. Verify paid status through the applicable base/result and reconciliation guidance before fulfillment.

> [!warning] Incomplete workflow/example wording
> The workflow says the shopper “enters their details” and the payment request includes purchased-item information, while the same child page says the payment form need not collect shopper information and lists no additional Multibanco `/payments` fields (raw lines 33–42, 87–89). Do not infer required shopper/item fields from those generic steps. The `/paymentMethods` curl sample omits a continuation between `-X POST` and `-d` (raw lines 62–63); it is not a paste-ready command.

## Detail locators

- Scope, API-only/voucher prerequisites and generic workflow: raw lines 15–36.
- Form and PT/EUR discovery example: raw lines 38–85.
- No-extra `/payments` fields and test/live offer promotion: raw lines 87–106.
- Main API-only guide navigation: raw `## See also` lines 108–110.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/api-only/2026-09-15|Multibanco API-only guide, captured 2026-09-15]]
