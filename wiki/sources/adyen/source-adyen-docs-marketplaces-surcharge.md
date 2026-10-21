---
title: "Surcharge | Adyen Marketplaces"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/surcharge"
raw_files:
  - "adyen/docs/marketplaces/surcharge/2026-09-15.md"
tags: [adyen, marketplaces, platforms, surcharge, online-payments, pilot]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplace-path guide describes a **pilot** API-only online-card surcharge in [[adyen-surcharging]] and the Adyen for Platforms balance-account model. A marketplace must have agreements with its users about how payment acceptance fees are charged; the users may pass those costs to customers. By default, the customer-paid surcharge is booked to the platform's liable balance account, while an explicit `Surcharge` split can book it to a user's balance account. This is distinct from platform commission and underlying payment fees (raw lines 15–21, 324–354).

## Key takeaways

- The documented route requires Adyen for Platforms with API-only online card payments using raw or encrypted card data, an API key with the Checkout webservice role, and a server receiving Standard webhooks; Transfer and Transaction webhooks are available for fund tracking. The pilot may be restricted and the page directs platforms to their Adyen contact. Collecting raw card data requires full PCI compliance according to the guide (raw **Requirements** and **Get card details**, lines 23–35, 55–70). These snapshot requirements are not proof of enrollment, live eligibility or compliance.
- The platform server calls `/cardDetails`, uses returned card brand, funding source, commercial-card flag and issuer country to decide whether a surcharge is permitted and calculate its amount, then discloses the amount before `/payments`. The feature does not automate global compliance enforcement; the snapshot cites EEA-issued consumer cards used in the EEA and US debit cards as examples of prohibited surcharges. Applicable legal, local and scheme rules need separate current verification (raw **Compliance**, **How it works**, **Get card details**, lines 37–53, 290–322).
- `/payments` includes `surcharge.value` and sets `amount.value` to the original transaction amount plus the surcharge. A `type: Surcharge` split can direct the surcharge to a user's balance account; otherwise the page states a liable-account default. The illustrated EUR 400 payment allocates EUR 394 to user goods/services, EUR 2 surcharge to that user's balance account, EUR 4 platform commission, and transaction fees to the user (raw lines 324–354, 360–419). **Source discrepancy:** the surcharge split-field table marks `amount.currency` required (line 341), but its illustrated split amount objects contain only `value` (for example lines 394–407); confirm the actual API contract before copying this example.
- The pilot guide says a surcharge cannot be added to authorization adjustments or overcaptures, and the amount cannot exceed what was shown at purchase (raw lines 32–35). A `/payments` response example with `resultCode: Authorised` is not captured balance-account credit. For a `Surcharge` split, the page describes a separate incoming transfer tracked through `transfer.created` received, `transfer.updated` authorised and captured with a `transactionId`, and `transaction.created` booked; samples are in the test environment and are not proof of an actual payout or bank receipt (raw lines 1092–1125, 1142–1441).

## Detail locators

- Versioned test `/cardDetails` snippets and card-characteristic response: raw lines 74–322; `/payments` samples and result: lines 356–1112. Library versions vary by language and are sample labels.
- Per-split webhook identification uses `category: platformPayment`, `direction: incoming`, `type: payment`, and `platformPaymentType: Surcharge`; transfer updates retain previous events and `sequenceNumber` (raw lines 1114–1138).
- The page recommends a Surcharge Amount column in PAR/SDR and says a `Surcharge` split generates extra BPAR/BPSR lines (raw **Reports and reconciliation**, lines 1444–1454). These rows support reconciliation of balance-platform activity, not external bank receipt.

## Related

- [[adyen-surcharging]] — surcharge concept and other channel-specific source routes.
- [[adyen-platforms]] — balance-platform and user/liable account context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/surcharge/2026-09-15|Surcharge, captured 2026-09-15]]
