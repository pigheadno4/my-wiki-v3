# C31 fixed query group H — 4/4 PASS

Analysis end (UTC): 2026-10-04T02:27:19Z

## 1. Boleto Bancário exact route — PASS

- Object/action match: Braintree **Local Payment Methods / Boleto Bancário**, an unversioned named-method website guide captured 2026-09-16; it is not a client/server SDK-version page or exact-SHA package evidence.
- Required route: `wiki/index.md:11` → `wiki/braintree-index.md:399` (`[[braintree-payment-methods]]`) → `wiki/concepts/braintree-payment-methods.md:32` → `wiki/sources/braintree/source-braintree-local-payment-methods-boleto-bancario.md:2,6-10` → `raw/braintree/docs/guides/local-payment-methods/boleto-bancario-2026-09-16.md`. The provider index also directly catalogs the source at line 121.
- Exact locators: primary raw `title`/`slug` at lines 6-7 and `# Boleto Bancário` at line 14. SHA-256 `39b764bd8761b550b4a1974f6bb153cd05820dbdf4d6b31fe7fd4e95b5ecf77c` matches `manifest.json:80-84`.

## 2. Boleto Bancário flow and applicability — PASS

- The snapshot limits Boleto to pilot merchants in Brazil (primary raw 20-21). It is a cash voucher created online and paid at a bank branch or named authorized processors, with up to three days for buyer payment; the merchant must have a created, verified and linked valid PayPal business account (23-26).
- The page directs server-side transaction creation to GraphQL (29-33). There is no capture call: only after Braintree receives confirmation that the voucher was paid does it associate a transaction for the merchant (36-38). A webhook integration is required for successful-payment confirmation and expired-voucher notification (48-50). The funded/expired payloads, including example `BRL` and `settled`, are examples rather than execution, settlement or bank-funding proof (52-79).
- Sandbox lifecycle is kept exact: the approval-URL modal can simulate successful, expired or unapproved payment; successful produces a webhook in 2-3 minutes and a settled-associated payment context, expired produces a webhook in 2-3 minutes and an expired context, and unapproved expires the context (39-43). These are Sandbox simulator outcomes, not Production timing.
- Unresolved support boundary: the fully read GraphQL guide names Boleto/BRL in Requirements and says Sandbox is open to all merchants while Production requires enablement (GraphQL 20-23), but its `currently supports` list names Multibanco, OXXO and Trustly and omits Boleto (26-35). The primary page's GraphQL direction does not resolve that same-date conflict.
- Unresolved currency boundary: the umbrella article says Local Payment Method transactions are automatically presented in EUR and settle to the PayPal account in its primary currency (article 19-21), while GraphQL requires a funding-source-matching PayPal currency and names BRL for Boleto (GraphQL 20-22); the primary funded-webhook payload also shows example BRL (primary 52-68). No single universal presentment rule is inferred.

## 3. OXXO exact route — PASS

- Object/action match: Braintree **Local Payment Methods / OXXO**, an unversioned named-method website guide captured 2026-09-16; it is not a platform/SDK-version page or exact-SHA package evidence.
- Required route: `wiki/index.md:11` → `wiki/braintree-index.md:399` (`[[braintree-payment-methods]]`) → `wiki/concepts/braintree-payment-methods.md:30` → `wiki/sources/braintree/source-braintree-local-payment-methods-oxxo.md:2,6-9` → `raw/braintree/docs/guides/local-payment-methods/oxxo-2026-09-16.md`. The provider index also directly catalogs the source at line 124.
- Exact locators: primary raw `title`/`slug` at lines 6-7 and `# OXXO` at line 14. SHA-256 `4ab1b70a8ac95fd39659fdd698efd3ad31c1d421a6ae7b2cb12a681195901f97` matches `manifest.json:107-111`.

## 4. OXXO flow and applicability — PASS

- The snapshot limits OXXO to pilot merchants in Mexico (primary raw 20-21). It is a cash voucher created online and paid at an OXXO convenience store, with up to three days for buyer payment; the merchant must have a created, verified and linked valid PayPal business account (23-26).
- There is no capture call; Braintree associates a transaction only after receiving confirmation that the voucher was paid (29-31). The page routes server-side local-payment transaction creation to GraphQL (38-42) and requires webhooks for successful-payment confirmation and expired-voucher notification (45-47).
- Sandbox outcome scope is exact: its approval-URL modal can simulate successful, expired or unapproved payment; the primary page promises the 2-3-minute webhook and associated transaction specifically for selected success (34-35). The shared GraphQL guide records the fuller simulated success/expired/unapproved context outcomes (43-50). Neither simulation, initiation, event label nor the example `settled` status proves a real completed payment, Production timing, settlement or bank funding.
- The fully read GraphQL guide includes OXXO in its current-support list (30-35), gives OXXO-specific required fields and an optional `expiryDate` that defaults to **today + 3 days** when omitted (143-159), and shows illustrative MXN request/response values (186-229). It separately requires MXN for the targeted OXXO funding source and Production enablement (20-23). The umbrella article's automatic-EUR wording (article 19-21) conflicts with that requirement and with the primary funded-webhook's example `MXN`/`settled` transaction (primary 49-65); the example is not a universal runtime guarantee.

## Shared gap sweep / extra full reads

- Both selected source pages and primary raws were read completely. Primary `raw_files` reverse lookup returns exactly one source owner for each selected raw. The concept links to both sources (`braintree-payment-methods.md:30,32`), and both sources link back to the concept (Boleto source line 53; OXXO source line 44).
- The bounded Braintree filename sweep found only the two selected raws plus the umbrella article and GraphQL non-instant guide relevant to these facts. Those two shared supporting raws were read completely once because they carry the EUR/currency and Boleto-support conflicts. Webhook/setup references remain unread navigation and supplied no factual claim.
- No seven-day rule applies to either selected method in this evidence: both primary pages say up to three days, and the OXXO GraphQL default is today + three days. The GraphQL guide's seven-day statements belong only to sibling Multibanco and Trustly sections (71 and 248) and were not imported into group H.

**Verdict: 4/4 PASS.** The answers match the named methods and requested actions, resolve through the required route with exact locators and pinned hashes, and preserve pilot, non-instant cash-voucher, no-capture, lifecycle, support-list and currency/example boundaries without claiming current eligibility or execution.
