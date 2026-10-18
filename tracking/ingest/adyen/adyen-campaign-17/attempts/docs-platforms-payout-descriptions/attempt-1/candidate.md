---
title: "Adyen for Platforms payout descriptions"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payout-descriptions"
raw_files:
  - "adyen/docs/platforms/payout-descriptions/2026-09-15.md"
tags: [adyen, platforms, payouts, transfer-descriptions, reconciliation]
---

## Overview

This Adyen for Platforms page explains how a payout's originator name, `description`, `referenceForBeneficiary` and banking identifiers can reach a beneficiary's bank statement. Adyen transmits submitted descriptor data through the clearing network, but the beneficiary bank decides what to display. The page covers managed/custom scheduled payouts and static descriptions for on-demand Transfers API or Cashout requests. Descriptor submission or display is not evidence that a payout was booked or received. [[adyen]] [[adyen-platforms]]

## Key takeaways

- **Originator and remittance identity:** the originator name can be Adyen's legal-entity name or the platform's legal-entity name, depending on region. If the platform's name is used, a Doing Business As name may be supplied through hosted onboarding or the Legal Entity Management API, then the Adyen contact must set it as originator name. This is a display-name route, not proof of legal seller, bank-account owner or successful transfer.
- **Transmission is not display:** `description` and `referenceForBeneficiary` are supplied through Transfers API or Customer Area, passed through clearing according to network capabilities and limits, then shown to the extent the beneficiary bank chooses. The country/currency/priority tables distinguish characters Adyen accepts from characters visible on statements; some combinations show zero visibility even when the request accepts the field.
- **Scheduled descriptors:** managed and custom payout schedules can use static text or placeholders in `description` or `referenceForBeneficiary`; an Adyen contact can also configure them at balance-platform level. Placeholders include balance account/account-holder IDs, references and descriptions, plus transfer references. `$shortTransferReference` applies only to custom scheduled payouts. For custom scheduled payouts, balance-account-level descriptor settings override balance-platform-level settings; without a configured descriptor, the guide shows a default descriptor at raw line 69. The page recommends the short reference for reconciliation and lists Customer Area, confirmation-letter, report and bank-statement routes, but bank display still varies by route.
- **On-demand and Cashout:** manual Transfers API requests require static `description` and `referenceForBeneficiary` strings; scheduled placeholders are unsupported. The page names `/transfers` and `/cashouts` request routes and recommends unique internal references in the description for reconciliation. It does not establish equivalent product eligibility, approval or bank-receipt behavior for those endpoints.
- **Limits and evidence boundary:** accepted character sets, maximum lengths and statement-visible lengths depend on counterparty location, currency and priority. For example, the table gives SEPA EUR instant `referenceForBeneficiary` zero visible characters, PLN regular both fields zero, and SGD wire both fields zero; it also shows Australia fast statement capacity greater than Adyen's accepted maximum. The broad statement that `$shortTransferReference` is provided by all banks should not be read as a guarantee of visible statement text for every listed rail. This snapshot gives no account-specific bank statement or live transfer outcome.

## Detail locators

- Raw lines 15–35: payout descriptor purpose, submission/clearing/bank display and originator/remittance components.
- Raw lines 37–69: scheduled placeholders, managed versus custom transfer-reference lengths, short-reference reconciliation and custom balance-account precedence/default.
- Raw lines 71–76: on-demand Transfers API and Cashout static-string rule, `/transfers` and `/cashouts` routes.
- Raw lines 78–187: Europe/SEPA and UK acceptance versus statement-visibility tables.
- Raw lines 189–255: North America and Asia Pacific acceptance versus visibility, including zero-visible and over-capacity examples.

## Related

- [[source-adyen-docs-platforms-managed-payouts]] — managed payout schedule context.
- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts]] — on-demand payout request, status and bank-transfer route.
- [[source-adyen-docs-platforms-payout-webhooks]] — payout status evidence after descriptor submission.

## Raw Sources

- [[raw/adyen/docs/platforms/payout-descriptions/2026-09-15|Payout descriptions snapshot, fetched 2026-09-15]]
