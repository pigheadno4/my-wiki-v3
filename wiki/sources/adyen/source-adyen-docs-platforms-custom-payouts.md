---
title: "Adyen Platforms custom payouts to user bank accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts"
raw_files:
  - "adyen/docs/platforms/custom-payouts/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, transfers, bank-accounts]
---

## Overview

This Adyen for Platforms custom-payouts overview, last modified 2024-06-06 and captured 2026-09-15, routes user funds from that user's balance account to that user's verified bank account through scheduled or on-demand bank transfer requests. Unlike the linked managed-payout route, it lets the platform choose a settlement delay, payout schedule, and on-demand initiation. Third-party bank transfers are presented as a separate Business Accounts product with additional verification. This overview is about available request paths and route constraints; it does not establish an actual transfer outcome or beneficiary bank receipt.

## Key takeaways

- Prerequisites include an Adyen for Platforms integration, a Transfers API credential with `TransferService Webservice Initiate role`, a Customer Area user with `Initiate payouts to transfer instruments`, and the user's `sendToTransferInstrument` capability. The account holder and transfer instrument must link to the same legal entity. For local and cross-border payouts to the same bank account, the page requires separate transfer instruments: one with local account identification and one with `numberAndBic`. Transfer and transaction webhooks are optional subscriptions for tracking platform fund movements.
- Local payouts use a matching country and currency, with route-dependent `regular`, `fast`, `instant`, and `wire` priorities. Cross-border payouts have only `crossBorder` priority. The overview prose instructs a POST `/transfers` with bank account number/IBAN and BIC under `NumberAndBicAccountIdentification`, while its route table allows or requires `iban` for some destinations; use the applicable current contract and route row. The detailed table qualifies country, currency, bank format, priority, transfer description, and amount availability; its cross-border table lists EUR, GBP, and USD while the prose gives a CZK-to-Slovakia example. Do not infer CZK route eligibility from that example without checking current route rules.
- The cross-border route excludes USD payouts to Canadian or Hong Kong users with US bank accounts. Correspondent banks can make arrival timing uncertain and deduct lifting fees; non-domestic bank account onboarding also has geographic restrictions in the hosted-onboarding example. A bank transfer request or internal booked event is not proof of beneficiary bank credit.
- Payout cutoff and settlement delay depend on location, currency, priority, amount, local timezone, and business day. Requests before a cutoff are described as *typically* processed within the stated delay; after-cutoff requests shift processing. The narrative SEPA wire example uses a 16:30 ET cutoff, while the table lists 16:55 CET for SEPA wire. Treat both as dated illustrative values and verify the current route and local cutoff before relying on a schedule.
- `## Testing` supplies TEST-only successful and unsuccessful bank details for `POST /transfers` with matching currency and priority, including return and failure scenarios/reason codes. Some testing rows use `cashout`, which the `## Transfer priority` list does not define. Test details do not prove live route availability or receipt. This overview links separate schedule, on-demand, webhook, and internal-transfer guides; it does not state approval, cancellation, retry, or irreversible-booking rules for a particular payout.

## Detail locators

- `# Custom payouts` and `## Next steps`: managed/custom contrast, settlement-delay, scheduled and on-demand child routes, and separate third-party Business Accounts scope.
- `## Requirements`: API and Customer Area roles, user capability, same-legal-entity transfer instrument, dual local/cross-border instrument setup, webhook subscriptions.
- `## Payout types` and `## Payout countries, currencies, and priorities`: local versus cross-border routing, exceptions, country/currency/bank-format matrix.
- `## Transfer cut-off times` and `## Transfer priority`: dated local cutoff/delay/min-max table and priority descriptions; conflicting SEPA example/table time.
- `## Testing`: TEST-only successful and unsuccessful scenario bank details, including return/failure reason codes and `cashout` inconsistency.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/2026-09-15|Adyen custom payouts (fetched 2026-09-15)]]
