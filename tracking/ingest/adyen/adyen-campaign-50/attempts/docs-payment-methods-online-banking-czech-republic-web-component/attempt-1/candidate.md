---
title: "Online banking Czech Republic Web Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/web-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/web-component/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, web, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Czech Republic to an existing Web Components integration** through Sessions or Advanced server-side flow. It covers redirect prerequisites, optional bank-picker configuration, the `OnlineBankingCZ` Component and test/live setup. Redirect initiation is not payment completion. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK bank-redirect and capability context.

## Key takeaways

- **Sessions flow** requires existing Web Components Sessions, Checkout API **v68 or later**, `action.type: redirect` handling and Customer Area addition. The page says no Czech-specific `/sessions` parameters are needed (raw lines 25–42). This does not remove fields required by the underlying Sessions integration.
- Sessions imports `OnlineBankingCZ` from `@adyen/adyen-web` and initializes that Component (raw lines 44–54, 91–105). Optional configuration includes `showImage` (default true), `issuer` to preselect a bank, `highlightedIssuers` to put banks atop the dropdown (added in Web **v5.22.0**), and `placeholder` (default “Select your bank,” overridden by custom translation) (raw lines 56–67). These are optional UI choices.
- **Issuer example conflict:** the configuration descriptions request **issuer IDs**, and the table lists **Česká spořitelna → `cs`**, but the sample configuration assigns the **bank name** `"Česká spořitelna"` to both `issuer` and `highlightedIssuers` (raw lines 65–88). Use the ID table and relevant SDK contract to resolve accepted value shapes; do not present the displayed bank-name values as validated IDs.
- **Advanced flow** requires existing Web Components Advanced, redirect handling and Customer Area addition (raw lines 115–123). It imports and initializes `OnlineBankingCZ` (raw lines 125–151) and says no **additional Czech-specific** `/payments` parameters are needed (raw lines 153–157). This does not assert that the base `/payments` request has no fields. The Advanced requirements table does not state a Checkout API minimum, and this section does not separately specify the Sessions optional configuration table.
- For both flows, the guide directs testing with real payment details and small amounts, checking status in test Customer Area **Payments > Payment list**, and adding the method in Customer Area to accept live payments (raw lines 107–113, 159–165). These are captured instructions, not evidence of successful test or live payment.

> [!warning] Bank-name sample versus issuer IDs
> The Sessions configuration table describes `issuer` and `highlightedIssuers` as issuer-ID values (raw lines 65–66), and the list maps Česká spořitelna to `cs` (raw line 84). The sample uses the bank name instead (raw lines 73–74). Do not silently treat that example as a valid issuer-ID recipe.

## Detail locators

- Sessions prerequisites and no additional `/sessions` fields: raw `## Sessions flow Component`, lines 25–42.
- Sessions import, optional bank UI and issuer ID mismatch: raw lines 44–88.
- Sessions Component initialization and testing: raw lines 91–113.
- Advanced prerequisites, import/initialize and no extra `/payments` fields: raw `## Advanced flow Component`, lines 115–157.
- Advanced testing and live method addition: raw lines 159–165.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/web-component/2026-09-15|Online banking Czech Republic Web Component, captured 2026-09-15]]
