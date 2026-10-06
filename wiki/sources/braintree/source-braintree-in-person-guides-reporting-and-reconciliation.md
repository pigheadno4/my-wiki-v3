---
title: "Braintree In-Person Reporting and Reconciliation"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/reporting-and-reconciliation"
raw_files:
  - "braintree/in-person/guides/reporting-and-reconciliation-2026-09-16.md"
tags: [braintree, in-person, reporting, reconciliation, settlement, order-id, custom-fields]
---

## Overview

This collected [[braintree|Braintree]] In-Person website guide routes transaction-lifecycle and status definitions, outlines a qualified pass-through settlement/funding example, and describes how a POS-supplied `orderId` and merchant-account custom fields can support in-store reporting and reconciliation. It is an unversioned website snapshot fetched 2026-09-16, not GitHub or exact-commit schema evidence, current account or report eligibility, or proof that a payment was authorized, captured, settled, funded, deposited, or successfully reconciled.

## Key takeaways

- The page does not define transaction statuses itself; it links to the Braintree transaction-lifecycle article and general status documentation. A status value or report row therefore must not be treated as final settlement or funding unless the applicable lifecycle authority explicitly establishes that meaning.
- For the page's in-store pass-through payout model, Braintree says it disburses settled funds as it receives them from card schemes and describes T+2 as typical, while expressly qualifying timing by card scheme, weekday and bank closure. The Monday-to-Wednesday table is labeled a happy-path example, not a universal timeline, account promise, or proof that funds reached a merchant bank account.
- The page describes `orderId` as a POS-provided unique transaction identifier used to link POS sale reporting to Braintree settlement reporting, and says the submitted value appears in that reporting. A POS order number is the expected example; concatenating store, terminal or other useful identifiers is presented as an option, not a required format. Exact character limits remain in the linked GraphQL API reference.
- `orderId` is the report-correlation field documented here. This page does not define reader ID, In-Store Context ID or Braintree transaction ID lifecycle semantics; use the dedicated In-Person transaction and query guides for those objects, and do not substitute context completion or report visibility for a transaction's settlement or funding state.
- For more granular searchable POS data, the page recommends merchant-account custom fields and says Store and Pass Back values can be searched in the Braintree Control Panel. The Store ID, Terminal ID and Cashier ID names are examples. If an application supplies custom fields in an API request, those fields must already be configured on the merchant account or the transaction will fail.
- The page links generic samples for Daily Transactions, Daily Disbursement and Daily Disputes reports and warns that their shape may vary with the merchant's account structure. The sample files are examples, not exact-current report schemas, proof of report access, or evidence of any payment, settlement, disbursement or deposit.

> [!warning] Reporting and lifecycle evidence are distinct
> `orderId`, custom-field searchability, transaction search results and sample reports help retrieve or correlate records. They do not by themselves prove authorization, capture, final settlement, funding, bank arrival, report completeness or successful reconciliation. Preserve the relevant account, card-scheme, environment and time qualifications and consult the linked lifecycle/status authority for the transaction state being interpreted.

## Detail locators

- Transaction-lifecycle and platform-status navigation: `## Transaction Lifecycle`, raw lines 19-21. The linked pages, not this snapshot, own the status definitions.
- Pass-through payout description, typical T+2 statement, card-scheme variation and happy-path/weekday qualification: `### In-Store Transaction Settlement Timelines`, raw lines 24-29.
- Illustrative Monday request/settlement through Wednesday merchant-deposit sequence and escalation route: raw lines 31-38. The table is an example, not outcome evidence.
- Own-AMEX-service-establishment-number exception and direct-AMEX disbursement route: `### AMEX External Settlement`, raw lines 41-43.
- Settlement-reporting navigation: `## General Information on Braintree Settlement Reporting`, raw lines 46-48.
- `orderId` purpose, reporting visibility, expected POS-generated value, optional concatenation and external character-limit route: `## Using the Order ID field to reconcile with Braintree settlement reports`, raw lines 51-58.
- Merchant-account custom-field purpose, Store and Pass Back search behavior, example identifiers and configuration-before-transaction failure condition: `## Configuring Custom Fields for In-Store Reporting`, raw lines 61-68.
- Named sample reports, generic-example qualification, account-structure variation and file links: `## Sample Braintree Reports`, raw lines 71-75.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]
- Cross-provider context: [[payment-reconciliation-reporting]]
- In-Store Context and transaction lifecycle route: [[source-braintree-in-person-guides-making-a-transaction]]
- Reader, location and transaction-query route: [[source-braintree-in-person-guides-additional-api-calls]]

## Related raw API references

- Braintree transaction lifecycle (`/braintree/articles/get-started/transaction-lifecycle/`) and general status definitions (`/braintree/docs/reference/general/statuses/`) — linked navigation only; not read as evidence for this entry.
- Wells IC settlement funding timeline (`/braintree/articles/wells-ic/transactions/settlement-funding-timeline/`) — linked navigation only; the current page's own timing remains qualified and illustrative.
- Settlement Batch Summary (`/braintree/articles/control-panel/reporting/settlement-batch-summary`) — linked navigation only; exact report access, fields and behavior require that dedicated source.
- GraphQL `InStoreTransactionInput` (`/braintree/graphql/reference/#Input--InStoreTransactionInput`) — linked navigation only; exact `orderId` and other input constraints require the reference.
- Braintree Control Panel custom fields (`/braintree/articles/control-panel/custom-fields/`) — linked navigation only; exact field types, permissions and configuration behavior require the dedicated source.
- In-Person account structure (`/braintree/in-person/get-started-1/account-structure/`) — linked navigation only from the sample-report qualification.

## Raw Sources

- [[raw/braintree/in-person/guides/reporting-and-reconciliation-2026-09-16|Braintree In-Person Reporting and Reconciliation (fetched 2026-09-16)]] - complete collected page covering qualified settlement/funding timing, `orderId` correlation, custom-field setup and generic sample-report routes
