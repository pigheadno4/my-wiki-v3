# Retrieval checks — docs-issuing-authorisation-transaction-rules-examples

## Q1 — Main purpose and scopes

What rule examples does the 2022-modified Issuing page give, and what are their scopes? It illustrates channel and US country/MCC blocklists (raw lines 21-97), per-transaction and monthly amount/count limits including two separate US/Canada fuel rules (raw lines 99-229), international limits on one payment instrument, 12-hour balance-platform and daily balance-account limits, and a two-week platform ATM limit (raw lines 231-396). Score examples target a payment instrument (raw lines 398-461). They are sample configurations, not live authorization results. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation-transaction-rules-examples]] → [[raw/adyen/docs/issuing/authorisation/transaction-rules/examples/2026-09-15]].

## Q2 — Material failure/conflict

Can the examples be pasted as verified payloads or used to settle rule condition semantics? No. The balance-account daily-limit JSON lacks closing structure (raw lines 323-353), the ATM decline example lacks `outcomeType` (raw lines 355-396), and the time-score prose says 11:00–18:00 Europe/Amsterdam while its JSON gives 10:00–17:00 +01:00 (raw lines 404, 418-428). The general and creation guides conflict on all-versus-any condition matching; inspect [[source-adyen-docs-issuing-authorisation-transaction-rules]] and [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] before asserting evaluation behavior. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation-transaction-rules-examples]] → [[raw/adyen/docs/issuing/authorisation/transaction-rules/examples/2026-09-15]].
