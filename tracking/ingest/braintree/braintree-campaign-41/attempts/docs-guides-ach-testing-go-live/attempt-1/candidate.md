---
title: "Braintree ACH Testing and Go Live"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/testing-go-live"
raw_files:
  - "braintree/docs/guides/ach/testing-go-live-2026-09-16.md"
tags: [braintree, ach, direct-debit, sandbox, testing, go-live]
---

## Overview

This unversioned Braintree website snapshot documents sandbox fixtures for ACH Direct Debit verification and transaction-response simulations, followed by a short production-transition checklist. The fixtures exercise synthetic sandbox responses; they are not evidence of a live bank debit, bank-account ownership, production enablement, settlement, funding or present merchant eligibility.

## Key takeaways

- The page limits the route to eligible merchants able to build a custom client-side integration with JavaScript v3 and says ACH Direct Debit is not available in Drop-in UI. These snapshot statements do not prove that a particular merchant is eligible or enabled.
- For sandbox verification, the page allows any real nine-digit routing number. It provides account-number tables for network-check and micro-transfer response simulations, including processor response codes and, for micro-transfers, displayed deposit amounts and an instant-settlement flag. Independent-check verification is described as successful in sandbox for any 4–17-digit account number. Use the exact tables at the raw locators rather than treating these test values as production bank-account data.
- The micro-transfer fixture for account `1000000001` simulates a three-business-day settlement delay before a later verification transition and requires the displayed micro-deposit amounts. The captured raw omits the name of the destination verification state, so this source does not reconstruct it. For other unlisted account numbers, the page says sandbox verification succeeds but assigns random, unavailable micro-deposit amounts, as in production.
- Sandbox transaction outcomes require a verified bank-account payment method. Listed amounts simulate one immediate failure and several settlement-pending-to-settlement-declined paths; amounts outside that table are described as successful in sandbox. The footnote specifically says webhook notification is received for final Settlement Declined outcomes due to insufficient funds or unauthorized transaction. These simulations do not establish live authorization, debit, final settlement or funding behavior.
- The go-live checklist says to mirror tested sandbox account settings in production, recreate sandbox transaction webhooks in the production account with production endpoints, and contact Braintree to enable ACH Direct Debit in production. Completing those configuration steps is not proof of enablement or of a successful live payment.

## Evidence boundaries

> [!warning] Sandbox simulations are not production proof
> The account numbers, micro-deposit amounts and transaction amounts on this page select simulated sandbox responses. They do not verify a real bank account, initiate a live debit, demonstrate production credentials or configuration, or prove settlement and funding.

> [!warning] Captured state labels are incomplete
> Several sentences in the collected raw lost the verification-state label (`astate`, `thestate`, and `markedin`). Preserve the surrounding timing and prerequisite only; consult a complete applicable authority before depending on an exact state transition.

## Detail locators

- Availability, JavaScript v3 custom-integration condition and Drop-in exclusion: `**AVAILABILITY**`, lines 17–18.
- Sandbox routing-number rule and network-check account/response table: `## Test values for sandbox verifications` through `#### For network check verifications`, lines 21–45.
- Micro-transfer account fixtures, deposit amounts, instant-settlement column and timing narratives: `#### For micro-transfer verifications`, lines 48–64.
- Independent-check digit-length fixture: `#### For independent check verifications`, lines 65–67.
- Sandbox transaction prerequisite, unsuccessful-amount table, final-status values and qualified webhook footnote: `## Test values for sandbox transactions`, lines 68–85.
- Successful sandbox transaction conditions: `### Amounts for successful transactions`, lines 86–92.
- Production account-setting, webhook recreation and enablement checklist: `## Go live`, lines 95–100.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- ACH lifecycle and eligibility guide: [[source-braintree-payment-methods-ach]]

## Raw Sources

- [[raw/braintree/docs/guides/ach/testing-go-live-2026-09-16|Braintree ACH Testing and Go Live (collected 2026-09-16)]] - complete collected page covering sandbox verification fixtures, simulated transaction outcomes and the production-transition checklist
