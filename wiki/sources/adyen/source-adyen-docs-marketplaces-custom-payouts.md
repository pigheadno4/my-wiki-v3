---
title: "Adyen Marketplace-path custom payouts to user bank accounts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, transfers, bank-accounts]
---

## Overview

This 2023-modified, 2026-09-15-captured Marketplace-path overview routes a user's funds from the user's balance account to that user's verified bank account through scheduled or on-demand custom payout requests. It contrasts managed payouts with platform-controlled settlement delay, cadence and API initiation. Sending funds to third-party bank accounts is a separate Business Accounts product with additional verification. See [[adyen]] and [[adyen-platforms]]; the Marketplace path does not make this a Classic Platforms account payout. The page describes request routes and conditions, not an executed payout or beneficiary-bank receipt.

## Key takeaways

- Requirements include an Adyen for Platforms integration, a Transfers API credential with **TransferService Webservice Initiate role**, a Customer Area user with **Initiate payouts to transfer instruments**, and the user's `sendToTransferInstrument` capability. The account holder and bank-account transfer instrument must link to the same legal entity. To use the same bank account for both local and cross-border payouts, the guide says to create separate transfer instruments with local and `numberAndBic` identification. Transfer and Transaction webhooks are available to track movement; possession of a role or capability is not evidence of a specific payout.
- Local payouts are described as within the same country and currency, with route-dependent `regular`, `fast`, `instant` and `wire` priorities. Cross-border payouts use only `crossBorder` priority. The cross-border prose instructs POST `/transfers` with `NumberAndBicAccountIdentification`, account number/IBAN and BIC, but the route matrix requires `iban` for some destinations and offers it as an option for others. Its CZK-to-Slovakia example also exceeds the cross-border matrix's listed EUR/GBP/USD currencies. Use the applicable route/contract rather than resolving these discrepancies from this snapshot.
- The guide excludes USD cross-border payouts to Canadian or Hong Kong users with US bank accounts. Correspondent-bank routes can have uncertain arrival times, lifting fees and restrictions on non-domestic bank accounts; its hosted-onboarding example limits adding such accounts to EU/EEA, Switzerland or UK residents. These are dated route descriptions, not current user eligibility.
- Cutoff, settlement-delay and amount limits vary by location, currency, priority and local timezone. Before-cutoff processing is described as *typical*, while later requests shift processing; neither promises bank receipt. The narrative SEPA wire example uses a 16:30 **ET** cutoff, whereas the table says 16:55 **CET** for SEPA wire. Check the current route and time zone before planning a payout. A higher-priority choice incurs higher fees per the guide.
- The TEST section supplies successful and unsuccessful `POST /transfers` bank fixtures by country, currency and priority, with return or failure reason codes. Use those details only in TEST. Some successful test rows use `cashout`, which is absent from this page's four local priorities and sole cross-border priority; a fixture is not live route availability or completion proof. The page links separate schedule, on-demand, payout-webhook and internal-transfer guides for detailed flows.

## Detail locators

- Purpose, managed/custom distinction, Business Accounts boundary and three custom routes: raw lines 15–33. Roles, capability, same-entity and dual-instrument setup: lines 35–48.
- Local/cross-border priorities, exceptions, arrival and fee qualifications: lines 50–80. Country/currency/format matrices, including cross-border IBAN-versus-numberAndBic and EUR/GBP/USD rows: lines 82–123.
- Cutoff explanation, narrative examples and location/currency/priority/time-zone/amount matrix: lines 125–192. Priority descriptions: lines 194–201. TEST-only fixtures, `cashout` rows and return/failure reason codes: lines 203–349. Child routes: lines 351–367.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — modern balance-platform model.
- [[source-adyen-docs-platforms-custom-payouts]] — separately pinned Platforms-path overview with the same general route.
- [[source-adyen-docs-marketplaces-managed-payouts]] — alternative managed-payout route.
- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts-approve-cancel-payouts]] — separate review and cancellation process, not established by this overview.

## Related raw API references

- The raw page links to Transfers API, custom schedule/on-demand, webhook and Business Accounts guides; their detailed current behavior and approval/return rules require separate authority.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/2026-09-15|Adyen Docs: Custom payouts (2026-09-15 snapshot; page last modified 2023-02-09)]]
