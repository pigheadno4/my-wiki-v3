# Braintree C25 fixed query audit — Group D

Scope: `auth-multi-currency-node` + `auth-reference-node` (four predetermined questions). Repository remained read-only.

Timing (UTC): analysis ended `2026-10-02T10:01:01Z`; handoff prepared `2026-10-02T10:01:44Z`.

## Page route: Multi-Currency (Node.js)

`wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:37` → `wiki/sources/braintree/source-braintree-auth-multi-currency-node.md:50-52` → `raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16.md` (complete 85-file-line read; SHA-256 `9b11eca34743ff2f07beea0e4cfe50874645b8dbcf166ffd036d93ea631290ec`, matching the C25 manifest).

1. **Navigation — Where is the Braintree Auth Node multi-currency guide?**
   - Object/action match: **yes** — this is the Node.js Braintree Auth route for adding and listing presentment-currency merchant accounts for connected merchants, not the generic currencies guide or a standalone merchant-account reference.
   - Direct answer: the route above lands on `source-braintree-auth-multi-currency-node`; its exact raw is `raw/braintree/docs/guides/braintree-auth/multi-currency/node-2026-09-16.md`, canonical URL `https://developer.paypal.com/braintree/docs/guides/braintree-auth/multi-currency/node`.
   - Exact raw locator: source URL line 1; title/slug lines 6-7; `# Multi-Currency` line 14.
   - Verdict: **PASS**.

2. **Detail — What account/currency scope and conditions does this guide itself state?**
   - Object/action match: **yes** — the selected guide states the connected-account origin, access-token, currency-add/list and payment-method support conditions requested.
   - Direct answer: the snapshot marks Braintree Auth closed beta and limits currency addition to connected merchants whose Braintree accounts were created through Braintree Auth; attaching an existing non-OAuth account to an OAuth application does not qualify and returns a validation error. After the OAuth flow supplies the merchant access token, the platform uses the Merchant API to create a merchant account for a currency with `gateway.merchantAccount.createForCurrency()` and lists existing merchant-account currencies with `gateway.merchantAccount.all()`. The general rule says every payment method the merchant accepts must support the new currency or validation fails and no new merchant account is created. Preserve the guide's unreconciled Amex qualification: it separately limits Amex presentment to GBP, EUR, SEK and USD, says adding another currency can succeed for other cards without enabling Amex, and says a later Amex transaction against that account returns a transaction validation error. These page-scoped statements do not establish current availability or merchant/currency eligibility.
   - Exact raw locator: availability and eligible account origin lines 17-22; access-token prerequisite and create/list operations lines 25-65; general all-payment-method condition lines 68-72; Amex qualification lines 75-76.
   - Verdict: **PASS**.

## Page route: Reference (Node.js)

`wiki/index.md:11` → `wiki/braintree-index.md:284` → `wiki/concepts/braintree-auth.md:41` → `wiki/sources/braintree/source-braintree-auth-reference-node.md:49-51` → `raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16.md` (complete 189-file-line read; SHA-256 `13eeb68df627137a621092f033a9b2047de64e240ae4024e8c985f6342ce2422`, matching the C25 manifest).

3. **Navigation — Where is the Braintree Auth Node guide reference?**
   - Object/action match: **yes** — this is the Node-route Braintree Auth guide reference for signup/login controls, OAuth scope navigation, merchant identity, downloadable-software connection guidance and Auth-specific merchant-account validation errors, not a generic Node SDK API reference.
   - Direct answer: the route above lands on `source-braintree-auth-reference-node`; its exact raw is `raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16.md`, canonical URL `https://developer.paypal.com/braintree/docs/guides/braintree-auth/reference/node`.
   - Exact raw locator: source URL line 1; title/slug lines 6-7; `# Reference` line 14.
   - Verdict: **PASS**.

4. **Detail — What objects or operations and qualifications does this reference itself describe?**
   - Object/action match: **yes** — the exact reference covers the requested Braintree Auth controls, identifiers, security pattern and validation catalog.
   - Direct answer: the snapshot marks Braintree Auth closed beta and frames account creation or existing-merchant login through a Connect URL within OAuth scope. It documents user and business signup-field prepopulation; `login_only` for an existing-merchant-only landing page; standard OAuth scopes plus a rendered Auth scope table; the redirect-returned `merchantId` for support and Control Panel deep links; an intermediary-server sequence for downloadable software so platform `client_id`/`client_secret` values remain secret; and Auth-specific merchant-account validation errors. Preserve the scope-count inconsistency: prose says **three** additional scopes, but the rendered table has four rows (`manage_disputes`, `oauth_app_receive_dispute_webhooks`, `read_only`, `read_write`) and does not identify which rows it counts as additional, so no corrected count is inferred. The worked downloadable-software `state` example is explicitly insecure and points to the server-side guide for proper handling.
   - Exact raw locator: closed-beta/product frame lines 17-22; signup fields lines 23-61; `login_only` lines 64-67; scope prose/table inconsistency lines 70-77; `merchantId` lines 80-85; downloadable-software/intermediary flow and secret/state warnings lines 86-101; Auth merchant-account validation-error catalog lines 104-188.
   - Verdict: **PASS**.

## Shared gap sweep and link checks

- One bounded filename and phrase sweep covered Braintree Auth guides plus merchant-account/currency reference raws. It surfaced the selected raws, adjacent Auth lifecycle pages, client/branding variants, the generic currency reference and dedicated merchant-account operation references. No second snapshot or question-relevant conflict was found. **No extra full reads** were needed: both selected complete raws directly answer the fixed questions; adjacent pages remain navigation-only.
- Reciprocity passes: root index → Braintree index; Braintree index → `braintree-auth`; concept → both sources (`wiki/concepts/braintree-auth.md:37,41`); each source → concept and its exact raw. Multi-Currency is also reciprocally linked from `braintree-currencies` and the Braintree company page; Reference is linked from the company page. **Group verdict: 4/4 PASS; no repair required.**
