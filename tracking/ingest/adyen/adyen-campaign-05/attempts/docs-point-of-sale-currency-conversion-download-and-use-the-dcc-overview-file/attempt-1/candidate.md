---
title: "View the DCC dashboard | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/currency-conversion/download-and-use-the-dcc-overview-file"
raw_files:
  - "adyen/docs/point-of-sale/currency-conversion/download-and-use-the-dcc-overview-file/2026-09-15.md"
tags: [adyen, point-of-sale, dcc, customer-area, reporting]
---

## Overview

Despite the URL's “overview file” wording, this captured Adyen Docs page is titled **View the DCC dashboard**. It describes a **live Customer Area reporting dashboard** and CSV export for Dynamic Currency Conversion (DCC) in Terminal API or standalone terminal solutions. Management/operations teams can use historical dashboard data to review shopper home-currency choice, merchant markup share, performance dimensions, and reasons DCC was not offered for individual transactions. See [[adyen]] and [[adyen-currencies-and-fx]].

## Key takeaways

- Dashboard access requires the **Merchant view POS Payment Report** and **Merchant POS Report role** Customer Area roles listed on the page, and Adyen Support must enable **DCC reporting for the merchant account**. The steps use the **live Customer Area**: Reports → Point of sale → Dynamic Currency Conversion (DCC), then select a reporting period and filters and Export CSV. The exported file is limited to the selected dashboard filters; Adyen recommends using the dashboard itself for analysis.
- The reported acceptance rate counts shoppers who chose to pay in their home currency, and the revenue view quantifies the merchant's share of the DCC markup generated at terminals. Breakdown dimensions include merchant account, store, terminal, issuer country, payment method, and currency pair. These are reporting views, not a live terminal offer, shopper consent record, quoted exchange rate, guaranteed markup amount, or forecast from a card BIN.
- The not-offered table gives **historical transaction reasons** and an “Actionable” column. It lists refunds and non-card transactions as not DCC-supported; invalid/zero transaction currency or amount, unsupported issuer currency or BIN, unknown issuer country, and same transaction/shopper currency as other non-actionable reasons. The **merchant-account not configured** row points to enabling DCC, with Support contact for pre-authorization or authorization-adjustment DCC. The **cost-contract not configured** row points to an Account Manager or Support for markup setup. The page says DCC is supported only for Visa and Mastercard **acquirer accounts** in that table; do not turn this into a rule about every Visa/Mastercard card or merchant.
- The dashboard, CSV, and reason table do **not** specify a rate formula, rate timestamp, shopper disclosure/choice UI, credential secret, API authentication method, or full DCC eligibility contract. The linked DCC and financial-reporting pages are navigation until read. This 2026-09-15 capture has a 2019 `last_modified` value and cannot prove present merchant enablement, current markets/schemes, or a particular transaction's offer or outcome.

## Detail locators

- `View the DCC dashboard`, lines 15–28: page identity, management/operations purpose, acceptance/markup metrics, dimensions and transaction not-offered lookup.
- `Requirements`, lines 30–39: Terminal API or standalone scope, two Customer Area report roles, Support enablement for the merchant account.
- `View and download the DCC dashboard`, lines 41–50: live Customer Area route, period/filter selection, CSV Export, filter-limited output.
- `DCC not-offered reasons`, lines 52–66: exact reason/actionable table, including refunds/cards/currency/amount, merchant and acquirer account configuration, issuer-country and BIN eligibility, same-currency and cost-contract cases.
- `See also`, lines 68–71: financial DCC reporting and currency-conversion guides are navigation only for this entry.

## Related

- [[adyen]] — provider page.
- [[adyen-currencies-and-fx]] — DCC and currency-context concept; this source is a POS reporting view, separate from transaction-time FX behavior.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/currency-conversion/download-and-use-the-dcc-overview-file/2026-09-15|View the DCC dashboard (2026-09-15 snapshot)]]
