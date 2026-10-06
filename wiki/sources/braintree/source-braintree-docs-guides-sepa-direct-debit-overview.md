---
title: "Braintree SEPA Direct Debit Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/overview"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/overview-2026-09-16.md"
tags: [braintree, sepa, direct-debit, mandates, settlement]
---

## Overview

This 2026-09-16 Braintree website snapshot is an overview of a limited-release, pilot-only SEPA Direct Debit checkout and mandate flow. It routes the page's IBAN-to-hosted-mandate sequence, one-time or recurrent mandate acceptance, mandate-management lifecycle, Instant-versus-Delayed settlement distinction, eligibility list, regulatory obligations and material return/dispute risks. It is not proof of current availability, pilot admission, merchant-account configuration, buyer or bank-account eligibility, an exact API or SDK contract, a successful debit, settlement finality or funding.

## Key takeaways

- The page limits SEPA Direct Debit to pilot merchants and directs interested merchants to contact Braintree. It describes euro-denominated bank-account payments in the Single Euro Payments Area and says the bank-account holder must accept a mandate authorizing the debit.
- In the documented checkout sequence, the customer supplies an IBAN that the page says PayPal validates, is redirected to a PayPal-hosted mandate page, accepts the mandate and returns to the merchant checkout to complete the purchase. PayPal stores and manages the accepted mandate, which can be specified for one-time or recurrent use. Mandate acceptance is authorization to debit; it does not by itself establish that a debit request succeeded or that funds settled.
- The Mandate Management API is described as a route to view mandate details and revoke accepted mandates for future payments. The page also says a stored mandate acceptance is automatically revoked after 36 months without transaction activity or if it fails routine risk checks. Exact API requests and responses belong to the linked references, not this overview.
- The page says SEPA Direct Debit transactions usually take 2–3 business days to settle and distinguishes account-configured Instant from Delayed Settlement. Instant Settlement can place funds with the merchant before the customer's bank debit completes; insufficient-funds failures may be re-presented, settled funds may later be debited from the merchant account, and an initial failure plus failed re-presentment can produce two return fees. Delayed Settlement waits until the amount has been debited and does not offer re-presentment according to the captured comparison.
- The page requires customer notification after a successful debit for one-off and recurring transactions and a means to cancel mandates. It says disputes within eight weeks are automatically honored, an unauthorized-transaction dispute can be raised after eight weeks and up to thirteen months, and a return can still be initiated against an original transaction that the merchant previously refunded.

## Material warnings

> [!warning] Mandate and request are not payment finality
> The mandate authorizes future account debits, while the same page says the scheme does not guarantee funds and documents later disputes, returns, re-presentment and merchant-account debits. Do not equate IBAN validation, mandate acceptance, a debit request, an Instant Settlement credit or a recurring-use setup with a successful debit, irreversible settlement or final funding.

> [!warning] Account and snapshot qualifications
> Limited-release pilot access, the supported-country list and Instant-versus-Delayed Settlement configuration are page- and account-qualified statements captured on 2026-09-16. Contact and account-manager routes are prerequisites or configuration paths, not evidence that a particular merchant, buyer, bank account or environment is eligible or enabled today.

> [!warning] Method-specific lifecycle
> Keep this SEPA Direct Debit overview distinct from ACH Direct Debit and card authorization/capture rules. It is unversioned website documentation, not commit-qualified GitHub evidence or an exact Mandate Management API or SDK contract.

## Detail locators

- Pilot-only availability, SEPA identity and account-holder mandate prerequisite: `# Overview`, raw lines 17–24.
- Checkout selection, IBAN validation, PayPal-hosted acceptance and return to merchant checkout: `## How it works` and `### Checkout flow`, raw lines 25–40.
- Mandate display, authorization storage, detail lookup, revocation and automatic-revocation conditions: `### Mandate management`, raw lines 43–53.
- Two-to-three-business-day statement, Instant-versus-Delayed comparison, account-manager configuration, re-presentment and return fees: `### Settlement`, raw lines 56–73.
- Eight-week automatically honored dispute period, unauthorized-dispute period through thirteen months and return-code navigation: `### Disputes and returns`, raw lines 76–83.
- Supported bank-account countries in the captured solution: `## Eligibility`, raw lines 84–105.
- Successful-debit notification, no-questions-asked dispute allowance, cancellation means and optional mandate communication: `## SEPA Regulatory Guidelines`, raw lines 107–113.
- Non-guaranteed funds, bank returns, fees, Instant Settlement clawback and returns against previously refunded transactions: `## SEPA risks`, raw lines 116–124.
- Vaulting and recurring-transaction support statement: `## Recurring transactions and Vault support`, raw lines 127–131.
- Linked configuration, client and server integration routes: `## Integration steps`, raw lines 132–137.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Complementary method guide: [[source-braintree-payment-methods-sepa-direct-debit]]

## Related raw API references

The page links configuration, client-side, server-side, vaulting, help and return-code resources. Those targets were not read for this entry and are navigation only; they do not establish exact request or response schemas, SDK behavior, environment availability, merchant enablement or a successful payment lifecycle.

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/overview-2026-09-16|Braintree SEPA Direct Debit overview]] - complete collected page covering pilot availability, checkout and mandate lifecycle, settlement modes, disputes, eligibility, regulatory guidance, risks, recurring support and integration navigation
