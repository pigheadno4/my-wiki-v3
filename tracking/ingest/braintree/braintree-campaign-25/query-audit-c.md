# Braintree C25 fixed query audit — Group C

Scope: `auth-server-side-node` + `auth-merchant-api-node` (four predetermined questions). Repository remained read-only.

Timing (UTC): analysis ended `2026-10-02T09:58:19Z`; handoff prepared `2026-10-02T09:58:31Z`.

## Page route: Node Server Side

`wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:34` → `wiki/sources/braintree/source-braintree-auth-server-side-node.md:46-48` → `raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16.md` (complete 78-file-line read; SHA-256 `c971b773b3263a01f32a5647be03b26d07f5e46e4571bceea3d1aafe9b942c4a`, matching the C25 manifest).

1. **Navigation — Where is the Braintree Auth Node server-side guide?**
   - Object/action match: **yes** — this is the Node.js server-side start of the Braintree Auth merchant Connect/OAuth flow, not generic transaction authorization or Merchant API execution.
   - Direct answer: the route above lands on source `source-braintree-auth-server-side-node`, whose exact raw evidence is `raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16.md`; its canonical URL is `https://developer.paypal.com/braintree/docs/guides/braintree-auth/server-side/node`.
   - Exact raw locator: source URL at line 1; title/slug at lines 6-7; `# Server-side Connect Flow` at line 14.
   - Verdict: **PASS**.

2. **Detail — What server responsibilities and boundaries does this guide itself state?**
   - Object/action match: **yes** — requested server construction and security boundaries are present in this exact guide.
   - Direct answer: Braintree Auth is labeled closed beta. For signup-capable or login-only integrations, the server SDK builds the `connect_url`; the merchant follows it to begin OAuth. The platform supplies an allowlisted return URI, requests only scopes needed for its operations (comma-separated for multiple scopes, with resource-specific read-only scopes), and uses a non-guessable `state`, verifies the returned value matches, and escapes/encodes its contents. Downloadable software is routed to separate guidance. Optional Connect controls cover landing page, login-only, and signup prefill; for signups, country fixes the domestic transaction currency, multiple presentment currencies require the separate API route, credit card + PayPal are enabled by default, credit-card-only is allowed, and PayPal-only is not. These statements describe the collected guide, not current availability or payment success.
   - Exact raw locator: closed beta lines 17-18; first-step/server-SDK responsibility and downloadable-software boundary lines 20-22; Node `connectUrl` example lines 25-46; redirect allowlisting lines 49-51; least-privilege/multiple-scope rules lines 52-56; CSRF `state` controls line 61; landing/login/signup boundaries lines 62-79.
   - Verdict: **PASS**.

## Page route: Merchant API

`wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:39` → `wiki/sources/braintree/source-braintree-auth-merchant-api-node.md:43-45` → `raw/braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16.md` (complete 90-file-line read; SHA-256 `14c812f3fa8e167cb4cb22214d4f58deee94ebe60e39998969f9cafe3a14f6c8`, matching the C25 manifest).

3. **Navigation — Where is the Braintree Auth Node Merchant API guide?**
   - Object/action match: **yes** — this is the Node.js guide for acting on behalf of a connected merchant with an access token, not the earlier Connect setup or token-exchange guide.
   - Direct answer: the route above lands on source `source-braintree-auth-merchant-api-node`, whose exact raw evidence is `raw/braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16.md`; its canonical URL is `https://developer.paypal.com/braintree/docs/guides/braintree-auth/merchant-api/node`.
   - Exact raw locator: source URL at line 1; title/slug at lines 6-7; `# Merchant API` at line 14.
   - Verdict: **PASS**.

4. **Detail — What merchant-scoped actions and prerequisites does this guide itself state?**
   - Object/action match: **yes** — the exact guide states the access-token prerequisite and demonstrates connected-merchant transaction/customer actions.
   - Direct answer: Braintree Auth is labeled closed beta. The guide begins once the platform already has an `access_token`; to act for that merchant, it instantiates `BraintreeGateway` with the access token instead of the client ID and secret used for a merchant acting for itself. It demonstrates `gateway.transaction.sale()` and `gateway.customer.create()` in callback and Promise forms. A merchant may revoke the authorization grant at any time, after which attempts to act on the merchant's behalf return `exceptions.AuthenticationError`. The examples are not evidence of every permitted operation or successful transaction/customer creation; granted scope is selected in the separate server-side Connect authority above.
   - Exact raw locator: closed beta lines 17-18; access-token prerequisite and credential distinction lines 20-22; transaction action lines 23-52; customer action lines 54-87; revocation/authentication-error boundary lines 89-91. Scope qualification is established by the other fully read selected raw at server-side lines 52-56.
   - Verdict: **PASS**.

## Shared gap sweep and link checks

- One bounded sweep covered filenames under `raw/braintree/docs/guides/braintree-auth/`, targeted hits for `connect_url`, `access_token`, `transaction:sale`, `customer:create`, and “perform actions on behalf,” plus exact-path searches across `raw/`. It surfaced adjacent configuration, Connect, OAuth-flow, reference, multi-currency, testing and client-side/branding routes, but no second snapshot of either selected canonical page and no question-relevant conflict. No extra raw was fully read; adjacent files remain navigation-only because the two selected complete reads answered the questions.
- Reciprocal navigation passes: root index → Braintree index; Braintree index → `braintree-auth` concept and both sources; concept → both sources (`wiki/concepts/braintree-auth.md:34,39`); each source → concept (`server-side:35`, `merchant-api:36`) and exact raw (`server-side:46-48`, `merchant-api:43-45`). No repair is required for Group C.
