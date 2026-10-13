---
title: "Dynamic Currency Conversion for POS | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/currency-conversion"
raw_files:
  - "adyen/docs/point-of-sale/currency-conversion/2026-09-15.md"
tags: [adyen, point-of-sale, dynamic-currency-conversion, foreign-exchange, terminal-api]
---

## Overview

Adyen's POS Dynamic Currency Conversion (DCC) guide describes offering an eligible foreign-card shopper a terminal choice between the merchant's local currency and the card's billing currency. If the shopper chooses the billing currency, DCC conversion is applied; choosing local currency continues without DCC. The pinned webpage was fetched 2026-09-15 and reports `last_modified` 2025-03-03. Its eligibility, rate, markup, reporting and rules language is snapshot evidence, not a current legal opinion, FX quote, account enablement or transaction result. [[adyen]] [[adyen-terminal-api]] [[adyen-currencies-and-fx]]

## Key takeaways

- The page covers Terminal API integrations with payment terminals and standalone POS. It says DCC is available/certified for **contact chip and contactless Visa, Mastercard, and Maestro** payments and authorization adjustments, within specified currencies and countries/regions. This is an eligibility boundary, not a promise that every card, terminal, issuer, account, or region will receive an offer. Its dated region list explicitly excludes Brazil and qualifies the United Kingdom to include Guernsey and the Isle of Man but not Jersey or other UK overseas territories/crown dependencies.
- Enable DCC at a company, merchant, store, or terminal settings scope in Customer Area or with a Management API `PATCH /terminalSettings` containing `dcc.enableDcc: true`. The API path needs the **Management API—Terminal settings read and write** credential role; Customer Area enablement uses the listed company- or merchant-level POS Terminal Management roles, while DCC reports/overviews require listed POS report roles. Check configured Visa/Mastercard/Maestro currencies for `ANY` and contact Support if the configuration must change. Support also enables DCC reporting per merchant account and optionally DCC for pre-authorization/authorization adjustment. Standard webhooks are a prerequisite if DCC is used for authorization adjustment.
- The shopper must be offered a real choice, see the conversion cost, and may decline DCC for local-currency payment. The page describes exchange rate and markup disclosure on the terminal and Adyen-generated receipt. For a merchant-defined receipt, it lists the exchange rate, rate source, markup, both currency amounts, and DCC acceptance statement. For DCC on pre-authorization/authorization adjustment, use webhooks and include final `CAPTURE` details on the receipt or invoice. Its scheme-rule description and compliance claim need current scheme and local-rule verification before operational use.
- DCC may alter reconciliation. The guide says funds settle in the merchant's settlement currency: the original pre-DCC transaction amount is paid to the merchant, plus its share of the markup. Its example is illustrative; it does not define a guaranteed merchant commission, rate, spread, or net proceeds for an account. The settlement report can expose a DCC markup credit after the DCC Markup column is configured, and the Payment Details/DCC reports distinguish offered from accepted. Keep this shopper-choice DCC markup route distinct from the generic Adyen FX management-fee description in [[adyen-currencies-and-fx]].
- The page forbids applying a **surcharge and DCC to the same transaction**. The guide says the feature needs no extra contract, but that statement is dated and does not replace actual account or card-scheme enablement checks.

## Detail locators

- DCC purpose, listed payment-method modes, integration/role prerequisites and surcharge exclusion: pinned raw, introduction and `## Requirements` (lines 15–37).
- Shopper terminal choice and accepted/declined currency outcome: pinned raw, `## How it works` (lines 39–53).
- Customer Area and Management API settings, role context, currency configuration and Support steps: pinned raw, `## Enable DCC` (lines 55–108).
- Card-scheme choice, terminal/receipt disclosures, merchant-defined receipt fields and authorization-adjustment webhook/CAPTURE path: pinned raw, `## Complying with regulations` (lines 110–152).
- Reconciliation, illustrative settlement and markup credit/reporting fields: pinned raw, `## Reconciliation` and `## Financial reports and overviews` (lines 154–175).
- Dated DCC currency/country list, Brazil exception and UK scope note: pinned raw, `## Supported currencies and countries/regions` (lines 177–212).

## Related

- [[adyen-currencies-and-fx]] — provider currency and generic FX concept; DCC is a separate shopper-choice POS feature.
- [[adyen-terminal-api]] — in-person Terminal API boundary.
- [[adyen]] — provider hub.

## Related raw API references

- [[raw/adyen/docs/point-of-sale/currency-conversion/download-and-use-the-dcc-overview-file/2026-09-15|DCC Overview file]] — linked navigation only; not read for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/currency-conversion/2026-09-15|Dynamic Currency Conversion — 2026-09-15 snapshot]]
