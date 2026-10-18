# Fixed retrieval checks — Platforms balance-account top-up overview

Q1. What is a top-up here, which accounts can it target, and what must not be inferred?
- Expected: This 2026-09-15 Adyen for Platforms hub defines a top-up as an incoming external transfer that increases a platform user's balance account; it also says the platform can top up its liable balance account if needed. Use cases include covering negative balances caused by refunds/chargebacks and providing funds for a transfer. Initiating a top-up or triggering an incoming transfer does not prove an external-source debit completed, a user/liable balance-account credit booked, a deficit was cured, a subsequent transfer succeeded, source-bank/legal ownership, current eligibility or bank receipt. The hub does not define the detailed method, role, fee or event rules.
- Raw locators: `raw/adyen/docs/platforms/top-up-balance-account/2026-09-15.md:15-28`, `:30-37`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-platforms.md` → `wiki/sources/adyen/source-adyen-docs-platforms-top-up-balance-account.md` → `raw/adyen/docs/platforms/top-up-balance-account/2026-09-15.md`.
- Canonical URL: `https://docs.adyen.com/platforms/top-up-balance-account`.

Q2. How do scheduled and on-demand routes differ at this hub, and where are outcomes resolved?
- Expected: The hub routes scheduled top-ups to a timing/amount-triggered schedule and on-demand top-ups to manual initiation when needed, either alongside or instead of a schedule. Its page description mentions a pull sweep/direct debit from a verified transfer instrument, while the body covers both routes, so do not impose that funding method on every on-demand top-up. After either initiation, Adyen says it triggers an incoming external transfer from the specified source into a balance account. The linked scheduled and on-demand pages own their distinct request conditions; the linked top-up webhook page is the route for status updates; this hub does not define the event meanings. This hub alone supplies no retry, reversal, terminal, region, currency, cutoff or finality guarantee.
- Raw locators: `raw/adyen/docs/platforms/top-up-balance-account/2026-09-15.md:6-19`, `:30-37`, `:39-51`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-platforms.md` → `wiki/sources/adyen/source-adyen-docs-platforms-top-up-balance-account.md` → `raw/adyen/docs/platforms/top-up-balance-account/2026-09-15.md`.
- Canonical URL: `https://docs.adyen.com/platforms/top-up-balance-account`.
