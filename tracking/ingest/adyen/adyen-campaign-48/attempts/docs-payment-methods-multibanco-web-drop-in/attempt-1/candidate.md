---
title: "Multibanco Web Drop-in integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/multibanco/web-drop-in/2026-09-15.md"
tags: [adyen, multibanco, web, drop-in, voucher]
---

## Overview

This 2026-09-15-captured Multibanco Web Drop-in page gives method-specific additions for existing **Sessions** and **Advanced** Web Drop-in integrations. It relies on the base flow guides. A generated voucher/pending offer is not a completed shopper payment; see [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for PT/EUR scope, voucher redemption and expiry context. This snapshot does not prove current account enablement or a live paid transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** requires an existing Web Sessions Drop-in integration, Checkout API **v68 or later**, and Multibanco added in Customer Area. No additional Multibanco parameters are specified for `/sessions`. Importing `Multibanco` individually is **optional** for tree shaking, not mandatory setup (raw lines 25–53).
- **Advanced:** requires an existing Web Advanced Drop-in integration, handling of an additional action with `action.type: voucher`, and Multibanco added in Customer Area. No additional Multibanco parameters are specified for `/payments`. Importing the `Multibanco` class individually is optional (raw lines 74–102).
- **Test and live gates:** before testing, submit a Multibanco request in the **test Customer Area**. In test, a pending payment can be simulated as paid by opening **Payments > Offers**, selecting the pending payment's PSP reference and choosing **Promote offer to sale**; the page instructs testing reconciliation this way. Paid payments, including promoted test offers, appear in **Payment list**. Before accepting live payments, submit a separate request in the **live Customer Area**. A test promotion is simulation, not evidence of shopper voucher redemption or live acceptance (raw lines 55–72, 104–121).

> [!warning] Advanced base-link wording
> The Advanced integration requirement URL contains an unresolved encoded `{{getParameter('platform')}}` value despite the Web Drop-in label, and the `voucher` action-handling link uses a fragment named “handle the redirect” (raw lines 82–83). Preserve the specified `voucher` action type; follow the correct Web Advanced base guide and actual returned action rather than treating that link fragment as a redirect-action requirement.

## Detail locators

- Sessions requirements, no-extra-parameters and optional import: raw `## Sessions flow Drop-in` lines 25–53.
- Sessions test-offer promotion, reconciliation and live request: raw lines 55–72.
- Advanced prerequisites, `voucher` action, optional import and no-extra-parameters: raw `## Advanced flow Drop-in` lines 74–102.
- Advanced test-offer promotion and live request: raw lines 104–121.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/web-drop-in/2026-09-15|Multibanco Web Drop-in guide, captured 2026-09-15]]
