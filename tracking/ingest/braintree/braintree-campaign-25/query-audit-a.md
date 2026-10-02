# Braintree C25 fixed query audit — Group A (Overview + Connect)

Analysis end: `2026-10-02T09:58:11Z`
Final handoff: `2026-10-02T09:58:45Z`

## auth-overview

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-auth]]` → `[[source-braintree-auth-overview]]` → `[[raw/braintree/docs/guides/braintree-auth/overview-2026-09-16]]`.

1. **Where is the Braintree Auth overview guide?**
   - **Object/action match:** Yes — the reached source and raw are the Braintree Auth product overview, not generic payment-transaction authorization.
   - **Direct answer:** `wiki/sources/braintree/source-braintree-auth-overview.md`, backed by `raw/braintree/docs/guides/braintree-auth/overview-2026-09-16.md` (canonical URL `https://developer.paypal.com/braintree/docs/guides/braintree-auth/overview`).
   - **Exact raw locator:** `raw/braintree/docs/guides/braintree-auth/overview-2026-09-16.md`, source URL at line 1 and `# Overview` at line 14.
   - **Verdict:** **PASS**.

2. **What purpose and applicability does this overview itself state?**
   - **Object/action match:** Yes — the answer uses the exact overview raw and its product-purpose/use-case statements.
   - **Direct answer:** The snapshot labels Braintree Auth **closed beta** and describes it for ecommerce platforms and merchant service providers that connect with Braintree merchants and take authorized actions on their behalf. It names service connections for invoicing, accounting, or analytics with customer/transaction-data access; a single merchant onboarding route for credit cards, debit cards, PayPal, and Apple Pay on the web; Shared Vault transactions using payment methods stored in the platform's vault; and Grant API sharing of saved methods with other connected Braintree merchants. These are overview routes, not proof of current access or implementation detail.
   - **Exact raw locator:** `# Overview > AVAILABILITY`, lines 16–17; purpose/roles at line 19; stated service and payment use cases at lines 22–25.
   - **Verdict:** **PASS**.

## auth-connect

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-auth]]` → `[[source-braintree-auth-connect]]` → `[[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16]]`.

3. **Where is the Braintree Auth connect guide?**
   - **Object/action match:** Yes — the reached source and raw are the merchant-facing Braintree Auth Connect flow, not the separate server-side code or token-exchange guide.
   - **Direct answer:** `wiki/sources/braintree/source-braintree-auth-connect.md`, backed by `raw/braintree/docs/guides/braintree-auth/connect-2026-09-16.md` (canonical URL `https://developer.paypal.com/braintree/docs/guides/braintree-auth/connect`).
   - **Exact raw locator:** `raw/braintree/docs/guides/braintree-auth/connect-2026-09-16.md`, source URL at line 1 and `# Merchant Connect Flow` at line 14.
   - **Verdict:** **PASS**.

4. **What connection flow and limitations does this guide itself state?**
   - **Object/action match:** Yes — the answer follows the exact merchant-facing connection flow and its stated controls, without importing the separate OAuth token exchange.
   - **Direct answer:** In this **closed-beta** snapshot, a platform places a **Connect with Braintree** button in its dashboard; the merchant is redirected to a Braintree-hosted, cobranded page. An existing merchant logs in with PayPal or Braintree credentials, authorizes only the permissions defined by the platform's OAuth scope, and **Agree and Return** sends the merchant to an allowlisted URI. Signup is offered by default for merchants without an account, but the platform can enable login-only; signup requires personal and business information, allows documented fields to be pre-populated, and offers **Finish Later**, which redirects to a platform-defined URI and lets the merchant resume later.
   - **Exact raw locator:** closed-beta qualification at lines 16–17; button purpose at line 19; hosted login/default-signup/login-only boundary at line 24; OAuth-scope and allowlisted-return boundary at line 29; signup/pre-population/Finish Later at line 34.
   - **Verdict:** **PASS**.

## Shared checks

- **Complete selected-raw reads:** Both pinned raws were read in full. SHA-256 values match the C25 manifest: overview `58cc8239…e5d017`; connect `39c37b3c…e2a5c72`.
- **Bounded gap sweep:** Filename and content sweeps across `raw/braintree/` found the adjacent Braintree Auth guide set, six out-of-C25 client/branding variants, Extend OAuth pages, and the Braintree Auth webhook reference. The source pages' related-raw routes (configuration, Merchant API, Shared Vault, server-side, and Node reference) were inspected as navigation. None was needed to answer these four fixed questions, and no relevant conflict or older same-canonical snapshot was found.
- **Extra full reads:** None beyond the two assigned raws; the questions were answered directly and no conflict/history trigger arose.
- **Reciprocal/navigation links:** Root index → Braintree index, Braintree index → `braintree-auth`, concept → both source pages, each source → concept, and each source → exact raw are present. The provider index's direct overview-source line has a nonblocking `+-` list-marker typo at `wiki/braintree-index.md:17`; the required route through `braintree-auth` remains intact.
