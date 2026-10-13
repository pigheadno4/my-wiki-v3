---
title: "Adyen POS Donations Using Giving"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/donate"
raw_files:
  - "adyen/docs/point-of-sale/donate/2026-09-15.md"
tags: [adyen, point-of-sale, giving, donations, terminal-api, nonprofit, webhooks]
---

## Overview

This Adyen guide covers Giving at a payment terminal after an in-store purchase. The shopper can make a **separate donation transaction** using the same payment method as the original purchase; the nonprofit is the donation beneficiary, and Adyen says it settles the full donation amount directly to the nonprofit's bank account while covering fees. The merchant selects an onboarded nonprofit and participating merchant accounts/stores in a Customer Area campaign, then the terminal offers eligible shoppers a donation. The 2026-09-15 snapshot lists `last_modified` 2025-04-07. This is the POS Terminal API or standalone route; online Giving's Web Components, Sessions and Advanced-flow implementations have separate evidence.

## Key takeaways

- A campaign starts **inactive** after creation; it must be started, and an ended campaign cannot be restarted. The nonprofit must already be onboarded or selected from Adyen's pre-approved library; availability is constrained by the participating legal entities and regions. Viewer and manager Customer Area donation roles have distinct campaign permissions and do **not** grant access to payment information. Campaign edits/state changes reach terminals on the next maintenance call, usually overnight.
- The base terminal-software requirement is **1.109 or later**, with model and option gates at 1.110 or later; the terminal table adds a **1.124** gate for combined round-up plus fixed amount in one-step and a **1.125** one-step gate for SFO1. Use the exact terminal/model row. Region, currency, nonprofit and original payment method also constrain prompting; the source says gift-card payments do not prompt. Its POS method table does not imply ecommerce Giving support.
- The campaign can prompt automatically after a payment, including standalone, or a Terminal API merchant can ask through `AskGiving` in `SaleData.SaleToAcquirerData` after contacting Support for that option. The **one-step** shopper interaction needs one card presentation and displays purchase and donation together, but still comprises two transactions. The **two-step** interaction needs a second card presentation, supports more listed methods and lets a Terminal API POS retrieve the donation response for a receipt. Fixed amount, round-up and combined donation types have campaign/model qualifications.
- The purchase `PaymentResponse` does not itself report the donation outcome because the terminal initiates the separate donation transaction. In the two-step flow, its `AdditionalResponse` supplies `adyen_giving_sale_id` and `adyen_giving_service_id` for a later `TransactionStatusRequest`; using `AdyenGiving` without the donation service ID selects the latest donation on that terminal, while the service ID targets a particular donation. This response retrieval is available only for two-step. The Adyen Giving merchant webhook with `eventCode: DONATION` reports donation outcome and `originalReference` links it to the original purchase; the shown success payload is a TEST example.
- Donations cannot complete while internet is down, even if offline purchase payments are enabled: the terminal may still prompt, but shows the donation as declined while the offline purchase follows its own processing path. This guide does not state a POS donation refund mechanism or that a purchase refund automatically reverses its separate donation.

## Detail locators

- `## Requirements`, `## How it works`, `## Nonprofit organizations` — POS integration, roles/webhooks, onboarded nonprofit and campaign/store choices, supported-scope gates.
- `## Donation campaigns` — company-account Customer Area setup, inactive-to-started lifecycle, irreversible end, terminal maintenance timing.
- `## Donation options` — automatic versus request-triggered moment, one/two-step interaction, gift-card/offline behavior and fixed/round-up choices.
- `## (Optional) Ask for a donation through a payment request` — Terminal API `AskGiving` formats and `AdditionalResponse` identifiers; JSON/Java are examples, not SDK-version proof.
- `## (Optional) Get the two-step donation response` — `TransactionStatusRequest` and `RepeatedMessageResponse.PaymentReceipt`; omitted service ID selects latest terminal donation.
- `## Giving webhook` — merchant `DONATION` event, `success`, `originalReference` and example payload.
- `## Supported terminals and donation options`, `## Supported regions and currencies`, `## Supported payment methods and flows` — model/software, nonprofit-region/currency, method and one/two-step tables; Apple Pay/Google Pay one-step requires a supporting card in the wallet, Cartes Bancaires in-person requires a French nonprofit, and Singapore fundraising requires a local nonprofit.

## Related

- Company: [[adyen]]
- Giving concept, including separately evidenced online flows: [[adyen-giving]]
- POS message and status-request context: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/donate/2026-09-15|2026-09-15 Adyen POS Giving guide snapshot]]
