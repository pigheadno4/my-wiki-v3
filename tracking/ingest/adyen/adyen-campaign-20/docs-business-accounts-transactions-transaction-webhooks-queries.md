# Transaction webhook retrieval checks

## Q1 — When is a transaction webhook sent, and how does it differ from a Transfer webhook?

**Answer:** The page says transaction webhooks are sent when funds are credited to or debited from a balance account, while Transfer webhooks report each transfer status change. It describes booked outgoing and incoming events for external bank and internal balance-account movements. The requirements table calls for an Adyen for Platforms, Issuing or Payouts integration, Transaction and Standard webhook subscriptions, and a server that accepts webhooks; Transfer webhook subscription is shown as optional. The TEST examples do not prove live operation or counterparty-bank receipt.

**Evidence:** `raw/adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15.md:17-45,83-91,169-177,229-239,286-296`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-transactions-transaction-webhooks]]` → `[[raw/adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15]]`.

## Q2 — Can the sample amount and internal debit account IDs be copied as a consistent mapping?

**Answer:** No. The outgoing external prose says EUR 100.00, the request example says `value: 150000`, and the outgoing webhook says `value: -10000`. In the internal debit example, the outgoing table describes `balanceAccount` as the request-receiving/debited account, yet the negative event names the initiating request account; the incoming table describes it as the initiating/credited account, yet the positive event names the request's counterparty. The page leaves these conflicts unresolved. Verify current API definitions and actual webhook data before implementing a mapping.

**Evidence:** `raw/adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15.md:49-65,102-107,143-175,187-214,288-296,307-332`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-transactions-transaction-webhooks]]` → `[[raw/adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15]]`.
