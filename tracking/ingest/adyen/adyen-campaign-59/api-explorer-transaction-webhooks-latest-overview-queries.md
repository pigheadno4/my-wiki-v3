# C59 fixed query answers — Transaction webhooks overview

## Q1

The captured API Explorer page is explicitly titled **Transaction webhooks v4**. It says Adyen sends transaction-information webhooks after a transfer is booked in a balance account, suggests dashboard balance updates and incoming/outgoing fund tracking, and lists one incoming route: `POST balancePlatform.transaction.created`. The overview does not provide a payload schema, resource or transfer IDs, required fields, amount/currency, or debit/credit ledger-entry shape; those need the event reference and related transaction-webhook guide. The route's `latest` segment does not override the captured v4 heading. [Raw: lines 5–20] Canonical route: [[source-adyen-api-explorer-transaction-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/transaction-webhooks/latest/overview

## Q2

The overview describes a webhook family associated with booked balance-account transfers; it does not prove a booking for a particular account or that a recipient bank received funds. Its single catalog row supplies no event-payload or ledger-entry identifiers, failure/reversal semantics, delivery order, retry/deduplication, signature-verification, or finality guarantees. The v4 label is explicit in the captured heading, while current live version and availability are not established by this dated snapshot. [Raw: lines 1–20] Canonical route: [[source-adyen-api-explorer-transaction-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/transaction-webhooks/latest/overview
