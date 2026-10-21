---
title: "Adyen Marketplace Transaction components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/transactions-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/transactions-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, transactions, refunds]
---

## Overview

This 2026-09-15 Marketplace-path guide describes Platform Experience Transactions Overview and Transaction Details components for a marketplace user's portal. They render balance-account transaction lists, insights, details, filtered CSV export and an optional role-gated refund action. The page still states an Adyen for Platforms integration prerequisite; the Marketplace URL is not a separate product or refund guarantee. See [[adyen]] and [[adyen-platform-components]].

## Key takeaways

- **Access and integration:** A Balance Platform API key needs the Adyen-assigned **Transactions Overview Component: View** role to create a server-side Session Authentication API `POST /sessions` token. Its policy scopes the resource to an `accountHolderId` with `type: accountHolder`, sets `product: platform`, and includes View in roles. The session request also takes `allowOrigin`; LIVE supports HTTPS only. The client initializes the library and supplies an `onSessionCreate` callback to retrieve or refresh the session. The documented curl endpoint is TEST. Country/region, browser and language availability come from linked component-library guidance and the listed locales (raw lines 44–57, 221–286, 337–350, 879–893).
- **Transaction grain and limits:** Overview lists transactions for a selected balance account and period, shows available/reserved balances, and computes Insights period result and incoming/outgoing totals for the selected currency and filters. Its time range uses the selected balance account's timezone; the default is last 180 days. Filters include transaction type, currency and exact PSP reference, with other filters still applying. CSV export is only the first 100 matching transactions, not a complete ledger. Details shows summary, references and refund information, plus timeline when available; it can appear as the default modal or on a separate page (raw lines 59–167).
- **Refund action:** **Transactions Overview Component: Manage Refunds** must be assigned to the API credential and included in the session request. A user can submit a full or partial payment refund through the component when the payment method supports it; multiple partial requests are described within the original payment amount cap. The component calls Adyen's API and displays a refund status message/label, with the refund transaction linked to its payment record after issue/processing. A click, submitted request, or UI label alone is not proof of final refund settlement or shopper receipt (raw lines 178–216).
- **Version and customization:** Features can vary by component-library version. npm or script/stylesheet embedding is shown; the latter calls for version-specific SRI hashes. Optional locale, appearance and data customization lets the marketplace extend displayed records through `dataCustomization` and `onDataRetrieve`; custom field names should start with an underscore and returned records must retain source data. `availableTranslations` is deprecated in favor of on-demand CDN locale loading (raw lines 36–38, 291–893).

## Detail locators

- Requirements, roles and CSV export bound: pinned raw lines 44–57.
- Overview/Insights, account balance, first-100 CSV export, filters and account timezone: pinned raw lines 59–153.
- Details and refund flow: pinned raw lines 155–216.
- Server-scoped session, TEST example, allowed origin and role policy: pinned raw lines 221–286.
- Library loading, initialization, SRI and deprecated option: pinned raw lines 288–481.
- Customization and supported languages: pinned raw lines 482–893.

## Related

- [[adyen-platform-components]] — main Platform Experience component concept.
- [[adyen-platforms]] — platform and marketplace context.
- [[source-adyen-docs-platforms-components-overview-after-payment-transactions-component]] — parallel Platforms-path Transactions component guide.
- [[adyen-reporting]] — separate report and reconciliation evidence context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/transactions-component/2026-09-15|Marketplace Transaction components, captured 2026-09-15]]
