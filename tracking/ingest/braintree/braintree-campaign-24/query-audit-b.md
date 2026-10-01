# Braintree C24 Fixed Query Audit — Group B

Scope: `recurring-article-subscriptions` and `recurring-response-subscription-node`. Both pinned raws were read completely (200 and 55 file lines).

## Evidence integrity

- `raw/braintree/articles/guides/recurring-billing/subscriptions-2026-09-16.md` — SHA-256 `b8388bf5d730c0deaf5039aab2ac127f57bc65ac06231a7dcd9b07e9508d6cb6`; **MATCH** manifest.
- `raw/braintree/docs/reference/response/subscription/node-2026-09-16.md` — SHA-256 `e839df3c281f22c44835d8ab8bc2c313b01d3f928fb3f92ad35bf5158cc659da`; **MATCH** manifest.

## Subscriptions article

**Actual route:** `wiki/index.md` (`[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (`[[braintree-recurring-billing]]`, line 271) → `wiki/concepts/braintree-recurring-billing.md` (`[[source-braintree-recurring-article-subscriptions]]`, line 30) → `wiki/sources/braintree/source-braintree-recurring-article-subscriptions.md` (`## Raw Sources`, lines 61–63) → pinned raw above.

1. **Where is the recurring-billing subscriptions article?**
   - **Requested object/action match:** Article-level, Control Panel-oriented subscription administration; not a Node guide, request schema, or response reference. **MATCH**.
   - **Direct answer:** Follow the actual route above to the pinned raw `subscriptions-2026-09-16.md`.
   - **Exact raw locator:** `# Subscriptions`, lines 14–16; `## Creating a subscription`, line 19.
   - **Verdict:** **PASS**.

2. **What subscription actions and boundaries does this article itself state?**
   - **Requested object/action match:** The raw describes creating, updating, retrying, refunding, canceling, and searching subscriptions in the article/Control Panel scope. **MATCH**.
   - **Direct answer:** Creation requires an existing plan; trial risks must be reviewed, and unlimited subscriptions per payment method plus no duplicate-subscription checking can cause overbilling. Updates are status-qualified: Pending/Active permit the listed broader changes, Past Due permits only subscription ID, payment method, merchant account and descriptor, and Expired/Canceled require a new subscription. EU merchants must give four weeks' notice before a price change or billing after six or more months without payment. Adding a Vault payment method does not retarget subscriptions; update the subscription token, after which the new card is charged on the next billing date. Plan price changes affect only future subscriptions, so existing prices require direct edits. Past Due charges can be retried; refunds apply to the associated sale transaction only while Settled/Settling and may be partial. Canceling an Active subscription retains its history. Search CSV omits cancellation date, which must be captured through the Subscription Canceled webhook and stored locally.
   - **Exact raw locator:** `## Creating a subscription`, lines 22–49; `## Updating a subscription`, lines 55–90; `### Subscription payment method`, lines 93–111; `### Subscription price`, lines 114–129; `## Retrying a Past Due subscription`, lines 132–148; `## Refunding a subscription`, lines 151–167; `## Canceling an Active subscription`, lines 170–184; `## Searching for subscriptions`, lines 189–197.
   - **Verdict:** **PASS**.

## Node Subscription response reference

**Actual route:** `wiki/index.md` (`[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (`[[braintree-recurring-billing]]`, line 271) → `wiki/concepts/braintree-recurring-billing.md` (`[[source-braintree-subscription-response-node]]`, line 61) → `wiki/sources/braintree/source-braintree-subscription-response-node.md` (`## Raw Sources`, lines 46–48) → pinned raw above.

3. **Where is the Node subscription response reference?**
   - **Requested object/action match:** Node.js Subscription response-history reference; not a request/action guide or article-level lifecycle overview. **MATCH**.
   - **Direct answer:** Follow the actual route above to the pinned raw `raw/braintree/docs/reference/response/subscription/node-2026-09-16.md`.
   - **Exact raw locator:** `# Subscription`, line 14; `## Subscription history`, line 21.
   - **Verdict:** **PASS**.

4. **Which response meanings or states does this reference itself establish?**
   - **Requested object/action match:** Response-history meanings and enumerated states, not subscription transitions or billing actions. **MATCH**.
   - **Direct answer:** Each returned subscription-history object documents `balance` as the subscription balance, `price` as its price, `status` with possible values `Active`, `Canceled`, `Expired`, `PastDue`, and `Pending`, and `subscription_source` as where the event was created with values `api`, `control_panel`, and `recurring`. Callback and Promise examples read `subscription.statusHistory[0].balance` after `gateway.subscription.find()`. The reference names states and event origins but does not define transitions, billing consequences, or guarantee a first history entry; it also carries a linked policy limitation on results.
   - **Exact raw locator:** results limitation at `# Subscription`, lines 17–18; field meanings and values at `## Subscription history`, lines 21–36; callback/Promise access examples at lines 38–55.
   - **Verdict:** **PASS**.

## Shared group checks

- **Bounded relevant gap sweep:** Exact-canonical-URL search found the subscriptions raw plus two discovery sitemap inventories, and only the pinned response raw for the Node response URL. A bounded filename sweep found adjacent recurring-billing articles, Node guides, request references, and a webhook reference; these govern different objects/actions, while both exact page-scoped questions were fully answered by the pinned raws. No historical snapshot or relevant unlinked evidence required an extra full read. **PASS**.
- **Reciprocal links:** The recurring-billing concept links to both source pages (lines 30 and 61); each source links back to `[[braintree-recurring-billing]]` (subscriptions line 47; response line 40) and links its exact pinned raw. The provider index links the concept and also catalogs both sources (lines 34 and 39). **PASS**.
- **Preserved scope warning:** The subscriptions raw does not discuss Marketplace compatibility; the concept/source correctly keep the recorded Marketplace conflict unresolved rather than inferring support. The response reference is correctly bounded to history values rather than lifecycle semantics. **PASS**.

**Group B result: 4/4 PASS; route, integrity, gap-sweep, and reciprocal-link checks PASS.**
