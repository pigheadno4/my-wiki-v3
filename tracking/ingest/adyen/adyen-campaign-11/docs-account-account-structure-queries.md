# Retrieval checks — Adyen account structure

## Q1. What is this page for, what is its scope, and what must a reader not infer?

The historical Adyen page explains how a business's company account, merchant accounts, optional account groups, and optional POS stores relate. It says one company account has one or more merchant sub-accounts; groups can organize several merchants, and POS stores can represent physical locations under a merchant account (`raw/adyen/docs/account/account-structure/2026-09-15.md:15-21`). The snapshot was last modified 2023-10-19 and fetched 2026-09-15. It does not identify a legal entity or merchant of record, define an organization account, allocate contractual liability or beneficiary ownership, establish complete funds flow, prove live payouts, or make the tea-shop region example mandatory.

Canonical retrieval route: `wiki/index.md` → `wiki/adyen-index.md` → proposed `wiki/concepts/adyen-account-structure.md` → `wiki/sources/adyen/source-adyen-docs-account-account-structure.md` → `raw/adyen/docs/account/account-structure/2026-09-15.md`. The coordinator must add the new concept to the provider index if approved. Canonical URL: https://docs.adyen.com/account/account-structure.

## Q2. What central capability or process does it describe, with prerequisites and warnings?

The company account holds merchant accounts and users and receives the monthly invoice by default (`raw/adyen/docs/account/account-structure/2026-09-15.md:23-25`). Merchant accounts process payments, receive payouts and reconciliation reports, and hold payment-method, currency, and risk-override configuration; the page says a single merchant account suffices for many customers, while others may need multiple (`raw/adyen/docs/account/account-structure/2026-09-15.md:27-33`). If there are several merchant accounts, optional account groups can give role-qualified users cross-account search/report access, but a merchant account can be in only one group (`raw/adyen/docs/account/account-structure/2026-09-15.md:37-46`). POS stores are optional sub-levels for physical locations (`:21`). The page links separate guides for choosing and managing the structure (`:52-60`); it does not provide those procedures or establish who is merchant of record or how all funds legally flow.

Canonical retrieval route: `wiki/index.md` → `wiki/adyen-index.md` → proposed `wiki/concepts/adyen-account-structure.md` → `wiki/sources/adyen/source-adyen-docs-account-account-structure.md` → `raw/adyen/docs/account/account-structure/2026-09-15.md`.
