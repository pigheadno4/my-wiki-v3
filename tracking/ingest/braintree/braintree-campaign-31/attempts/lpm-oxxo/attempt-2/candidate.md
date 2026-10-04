---
title: "Braintree OXXO Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/oxxo"
raw_files:
  - "braintree/docs/guides/local-payment-methods/oxxo-2026-09-16.md"
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
tags: [braintree, local-payment-methods, oxxo, cash-voucher, mexico]
---

## Overview

This collected, unversioned Braintree developer guide describes OXXO as a non-instant cash-based Local Payment Method created online and paid at an OXXO convenience store. It is a retrieval route for the page's Mexico pilot applicability, linked PayPal business-account prerequisite, paid-voucher transaction association, server-side GraphQL route, sandbox simulation and required outcome webhooks. The 2026-09-16 snapshot does not establish current availability, merchant enablement, buyer eligibility or successful execution.

## Key takeaways

- The page says OXXO is in limited release for pilot merchants in Mexico and requires a valid PayPal business account created, verified and linked in the Braintree Control Panel. These statements are snapshot qualifications, not proof that a particular merchant is enabled.
- OXXO is non-instant: the buyer may take up to three days to pay the online-created voucher at an OXXO store. The page says there is no capture call; Braintree associates a transaction for the merchant after receiving confirmation that the voucher was paid. Voucher creation or payment initiation therefore is not itself transaction association, funding or settlement evidence.
- The page directs the server side to GraphQL to create a local-payment transaction. It does not identify a client SDK or client platform on this page; its approval-URL modal instruction is specifically a sandbox simulation path.
- An OXXO webhook integration is required for successful-payment confirmation and expired-voucher notification. The raw examples provide `local_payment_funded` and `local_payment_expired` payload shapes, including IDs and a sample transaction, but example values and event labels do not prove a real payment, universal settlement state or settlement timing.

## Evidence boundaries

> [!warning] Currency wording remains unresolved
> The separately collected umbrella Local Payment Methods article says transactions are automatically presented in euros, while this OXXO page's illustrative funded-webhook transaction uses `currency_iso_code` `MXN`. The OXXO page does not state its presentment-currency rule, and an example payload is not a guarantee; these snapshots do not establish whether the fields describe the same currency stage or which wording governs OXXO.

> [!warning] Environment and lifecycle scope
> The two-to-three-minute webhook timing and selectable successful, expired or unapproved outcomes belong to the sandbox approval-URL simulation described by the page. Do not carry that timing into production or treat initiation, approval, a webhook label or the sample `settled` status as independent proof of completed funding or settlement.

## Detail locators

- Limited-release Mexico pilot applicability, non-instant cash-voucher identity, three-day payment window and linked PayPal business-account prerequisite: `### Configuration`, lines 17-26.
- No-capture behavior, Braintree transaction association after paid-voucher confirmation and sandbox approval-modal outcomes/timing: `### Capturing Non-Instant Transaction`, lines 29-35.
- Server-side GraphQL creation route: `### Server Side with GraphQL`, lines 38-42.
- Required successful-payment and expired-voucher webhooks: `### Configure webhooks`, lines 45-49.
- Illustrative `local_payment_funded` and `local_payment_expired` payloads, including sample IDs, amount, `MXN`, date and `settled` status: `### JSON`, lines 50-77.
- Umbrella Local Payment Methods EUR-presentment, PayPal primary-currency settlement and customer-conversion wording: supporting article `## Availability`, line 21.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Umbrella Local Payment Methods scope and currency wording: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following dated raw pages are navigation only and were not read as behavioral evidence for this entry:

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|PayPal setup guide]]
- [[raw/braintree/graphql/integration_guides/non_instant_local_payments-2026-09-16|GraphQL non-instant local payments integration guide]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/oxxo-2026-09-16|Braintree OXXO guide]] - complete collected page covering pilot applicability, cash-voucher timing, transaction association, GraphQL routing, sandbox simulation and outcome webhooks
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods article]] - complete supporting page for the umbrella EUR-presentment wording retained in the unresolved currency warning
