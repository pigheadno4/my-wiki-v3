---
title: "Adyen Issuing-path transaction components"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/components-overview/after-payment/transactions-component"
raw_files:
  - "adyen/docs/issuing/components-overview/after-payment/transactions-component/2026-09-15.md"
tags: [adyen, issuing, platforms, ui-components, transactions, refunds]
---

## Overview

This 2026-09-15 Issuing-path page describes the Platform Experience Transactions Overview and Transaction Details components for a platform's user portal. Its own requirements specify an **Adyen for Platforms integration**, and its authentication session uses `product=platform`. It does not describe an Issuing card-transaction component or establish an Issuing-specific entitlement. The overview shows balance-account transactions, balances and insights; details can show transaction references, amounts, fees and refund information. Supported users can submit payment-refund requests through the components.

## Key takeaways

- A Balance Platform API credential needs Adyen-assigned **Transactions Overview Component: View** to create a server-side Session Authentication API `POST /sessions` session. Scope the policy to the account holder linked to the balance account, include the View role, set `product=platform`, and provide the allowed origin; live origins must use HTTPS. Pass the returned session object to the client initializer. The example endpoint is TEST.
- Refunds additionally require **Transactions Overview Component: Manage Refunds** on the API credential **and** in the session request. The component calls Adyen's API when a user requests a refund; full and partial refund support depends on the payment method. Multiple partial refunds are described only while their total does not exceed the original payment amount. The UI shows a status after the request is processed; this guide alone does not prove final refund settlement or shopper receipt.
- Transactions Overview filters a selected balance account by period (using that account's time zone), type, currency and exact PSP reference; other active filters still constrain a PSP-reference search. Insights show period net incoming minus outgoing and grouped totals. CSV export is CSV-only and contains the first 100 matching transactions, so it is not a complete ledger.
- Transaction Details is embedded as a modal by default or may be initialized separately. Its Summary and Timeline tabs appear when data is available. Optional localization, appearance and data customization are version-dependent; the guide directs readers to the component-libraries page for country/region and browser support. `availableTranslations` is deprecated.

## Detail locators

- `## Requirements`: Adyen for Platforms prerequisite, credential roles, CSV constraints and support cross-reference.
- `## Transactions Overview component`, `### Available filters`, `## Transaction Details component`: account and transaction views, timezone, default last-180-days period, filter values, conditional detail tabs.
- `## Processing refunds through components`: refund role, payment-method and partial-amount conditions, request and displayed status.
- `## 1. Create an authentication session from your server`, `## 2. Install component library in your front end`, `## 3. Initialize components`: scoped session policy, platform product, TEST example, client mounting and deprecated setting.
- `## 4. Optional: Localize components` through `## Supported languages`: optional UI controls and supported locale list.

## Related

- [[adyen]] — provider context.

- [[adyen-platform-components]] — main component-suite concept and parallel Platforms-path guide.
- [[adyen-platforms]] — required product integration.
- [[adyen-issuing]] — Issuing navigation context; this page's stated component requirement is Platforms.
- [[source-adyen-docs-platforms-components-overview-after-payment-transactions-component]] — parallel Platforms-path snapshot.

## Raw Sources

- [[raw/adyen/docs/issuing/components-overview/after-payment/transactions-component/2026-09-15|Issuing-path transaction components guide (fetched 2026-09-15)]]
