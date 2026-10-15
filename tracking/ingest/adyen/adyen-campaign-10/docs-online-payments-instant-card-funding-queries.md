# Instant card funding retrieval checks

Canonical route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-online-payments-instant-card-funding.md` → `raw/adyen/docs/online-payments/instant-card-funding/2026-09-15.md`. Compare outbound flows through `adyen-card-payouts`.

## Q1 — purpose, scope, and what not to infer

Instant card funding is a card-sourced pay-in for movement toward another card, wallet or bank account; the page gives top-ups and P2P-transfer funding as examples and names Visa/Mastercard (`raw/adyen/docs/online-payments/instant-card-funding/2026-09-15.md:14–26`). The documented operation is Checkout `/payments` with funding context (`:38–40`), not a merchant goods purchase, outbound `/payout` or proof of completed P2P delivery. This 2025-modified snapshot does not establish current card, account, country, MCC, amount/velocity or scheme eligibility, payout speed, transaction success, seller/payee/MOR allocation or settlement (`:10`).

## Q2 — central capability, prerequisites, and warnings

Enablement requires compliance documents, a stated use case, card-scheme requirements and Account Manager discussion, followed by Support configuration after compliance is complete (`:28–36`). Top-up `/payments` requests identify the sender and recipient wallet/account; standard `shopperName`/`billingAddress` may stand in for those repeated `fundOrigin` values (`:42–52`). P2P funding additionally identifies the origin wallet/account and recipient name, address and destination identifier (`:92–105`). Missing data can be refused. Additional validation applies to transfers between different entities (`:158–160`), with specific name/address restrictions at `:162–178`. The page says ASCII only but lists an em dash among allowed characters (`:162,170`), so acceptance is unresolved. Its partial-authorization paragraph refers to **online payouts** even though this page is about **funding** (`:180–182`); do not transfer that recommendation to this pay-in or infer partial-authorization eligibility. The linked instant-card-payout guide is a separate outbound path (`:184–186`).
