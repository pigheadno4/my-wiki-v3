---
title: "Adyen Platforms Transactions components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/transactions-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/transactions-component/2026-09-15.md"
tags: [adyen, platforms, ui-components, transactions, refunds]
---

## Overview

This 2026-09-15 guide describes Transactions Overview and Transaction Details Platform Experience components for a platform's user portal. The overview lists and filters transactions for a selected balance account and period, shows balances and transaction insights, and exports CSV. Details opens by default as a modal or can be initialized on a separate page. A role-gated refund action can submit a refund request through Adyen's API. The page explains component integration and UI behavior, not a guarantee of final refund outcome or shopper receipt.

## Key takeaways

- Prerequisites are an Adyen for Platforms integration, Balance Platform API credential, and Adyen-assigned **Transactions Overview Component: View** role. **Transactions Overview Component: Manage Refunds** must be assigned to the credential and included in the authentication session to enable refunds. The server creates a Session Authentication API `POST /sessions` token for a specific `accountHolder` resource, with `product=platform`, allowed origin, and roles; the live origin must use HTTPS. The client initializes the library using the session response. The example URL is a test endpoint, not a live operation.
- Transactions Overview displays a balance-account transaction list, available and reserved balances, and Insights for a selected period and currency. Period Result is net incoming less outgoing; incoming/outgoing totals are grouped by transaction type. Filters include balance account, time period (in the balance account's timezone; default last 180 days), transaction type, currency, and exact PSP reference. A PSP-reference search is still subject to the other active filters.
- CSV export is limited to the first 100 matching transactions and CSV format. It is a filtered UI export, not a complete ledger or a reconciliation result. Transaction Details shows summary, references and associated refunds, and a timeline when available; user-defined display fields may be added.
- When a user confirms a supported full or partial refund, the components call Adyen's API to process the request and then show a refund status message and label. Payment-method support controls availability. Multiple partial refunds are described as possible while their total does not exceed the original payment amount. A submitted request or displayed status must not be treated as proof of final settlement or shopper receipt; use refund-specific evidence for that lifecycle.
- Available guidance and features depend on library version. Localization, appearance, and data customization are optional, and the guide lists 11 supported languages. The broader component-suite guide supplies country/region and browser boundaries. The `availableTranslations` property is deprecated; current locale files are fetched from CDN.

## Detail locators

- `## Requirements`: integration, credential roles, CSV limits, country/browser cross-reference.
- `## Transactions Overview component` and `## Transaction Details component`: displayed data, filters, export, insights, detail tabs.
- `## Processing refunds through components`: role, user action, API request, partial-refund condition, status display.
- `## 1. Create an authentication session from your server`: account-holder scoped session, roles, product, origin, test example.
- `## Supported languages`: language list.

## Related

- [[adyen-platform-components]] — main component-suite concept.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/transactions-component/2026-09-15|Adyen Transactions components guide (fetched 2026-09-15)]]
