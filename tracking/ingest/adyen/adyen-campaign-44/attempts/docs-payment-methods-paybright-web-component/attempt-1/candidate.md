---
title: "PayBright Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/web-component"
raw_files:
  - "adyen/docs/payment-methods/paybright/web-component/2026-09-15.md"
tags: [adyen, paybright, affirm, web-components, buy-now-pay-later]
---

## Overview

This 2026-09-15 Adyen Docs guide describes adding PayBright to an **existing Web Components** Sessions or Advanced integration. Its opening states that PayBright was acquired by Affirm and **Adyen will not accept new PayBright integrations**. Treat the subsequent setup, live-request and test instructions as historical/existing-integration guidance, not an invitation or proof that a new merchant can enable PayBright. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- Both flow tabs require a built Web Components integration and PayBright added in Customer Area. `/sessions` is described as the default with Components v5.0.0 or later; `/payments` is for an additional use case. The captured examples are versioned TEST snippets, not live payment evidence.
- Both API field tables mark `shopperName` (first/last), `dateOfBirth`, `shopperEmail`, `telephoneNumber`, `countryCode`, `billingAddress` and `shopperReference` (minimum three characters) required for this PayBright guide. `deliveryAddress` defaults to billing if missing; `shopperLocale` is optional. Introductory prose says to provide purchased-item `lineItems`, but both tables label `lineItems` **optional** and recommend them to improve approval rates. Preserve this prose/table difference instead of making the field unconditionally required. Shopper data is used for PayBright risk checks.
- The Web Component uses `paybright`: the v6.0.0-or-later example mounts a `Redirect` Component with `{ type: 'paybright' }`, while the v5.x.x-or-earlier example uses `checkout.create('paybright')`. The CA/CAD and shopper details in request snippets are fixtures. Some Advanced Java/PHP snippets instead show USD with Canadian country/locale, and the Java discount line is positive where the other examples use a negative discount; do not use those snippets as verified currency or invoice arithmetic rules.
- PayBright payments are captured automatically by default after authorization; capture charges the shopper's first installment. Delayed or manual capture is the route for capture after shipping or partial capture. Partial captures are unavailable when automatic capture is enabled in Customer Area. The `/capture` example uses `modificationAmount` and optional `additionalData.openinvoicedata` item information. After a single partial capture, the unclaimed authorization is automatically cancelled; **multiple partial captures** require Support enablement, leave the remaining amount open after the initial capture and create a new invoice per capture.
- An uncaptured payment can be cancelled. Once captured, returning funds requires a refund; the partial-refund example uses `/payments/{paymentPspReference}/refunds`, `modificationAmount` and optional `openinvoicedata` about returned items. A request example does not establish actual capture, cancellation or refund outcome.
- The test section points to PayBright test details and Customer Area test-status lookup, then says to submit a PayBright request in live Customer Area. Read that later route subject to the opening **no-new-integrations** notice; the snapshot does not establish current account eligibility or an exception.

## Detail locators

- Acquisition/no-new-integration notice, scope and shopper/line-item overview: raw lines 19–26.
- Sessions/Advanced prerequisites and endpoint selection: `## Requirements`, lines 28–44, and `## API reference`, lines 46–52 and 794–796.
- Required/optional field tables and versioned CA/CAD TEST examples: `/sessions` lines 54–793; `/payments` lines 797–1315. The introductory `lineItems` instruction at line 26 differs from optional table rows at lines 65 and 809. Advanced Java/PHP USD sample values and Java positive discount appear in lines 886–966 and 967–1048.
- Version-specific `Redirect` versus `checkout.create` mounting: `## Component configuration`, lines 1317–1347.
- Capture default, first installment, partial-capture eligibility, invoice data and unclaimed-amount effect: `## Capture the payment`, lines 1349–1408.
- Cancel-before-capture, refund-after-capture and optional partial-refund item data: `## Refunds`, lines 1410–1454.
- Test-status and live-request instructions, qualified by the opening notice: `## Test and go live`, lines 1456–1462.

## Related

- [[adyen-online-payments]] — provider online-payments context.
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm method overview; acquisition does not make the two guides interchangeable.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/web-component/2026-09-15|2026-09-15 PayBright Web Component guide, examples and lifecycle]]
