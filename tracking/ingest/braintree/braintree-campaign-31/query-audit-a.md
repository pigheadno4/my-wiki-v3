# C31 fixed query group A — 4/4 PASS

Pinned evidence: `lpm-overview` hash `7df3ee083b4c365376e5e32a9fda71cbaa980aaab8fa4feea9207f3b332bcd71`; `lpm-configuration-javascript-v3` hash `ad1c8037e45f79f2c384746bdb907090254d6b28069a9b88cdbae5b6aae25950`. Both recomputed hashes match `manifest.json` lines 116–119 and 143–146.

## Q1 — overview exact route — PASS

`wiki/index.md:11` → `wiki/braintree-index.md:376` (`[[braintree-payment-methods]]`) → `wiki/concepts/braintree-payment-methods.md:28` (`[[source-braintree-local-payment-methods-overview]]`) → source frontmatter `raw_files` at `wiki/sources/braintree/source-braintree-local-payment-methods-overview.md:7-9` → `raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16.md`. This is an unversioned Braintree developer-guide **Overview** captured 2026-09-16; it names no client/server platform or SDK version and is website documentation, not exact-SHA package evidence. The reverse ownership lookup returns this one source page.

## Q2 — overview principal flow/applicability — PASS

Local Payment Methods are region-specific bank, wallet, or other choices (`overview` raw line 16). The page's snapshot table has 15 named methods mapped to customer countries and stated transaction limits (lines 21–39), but it is not uniform/current eligibility proof: only Boleto Bancário, Multibanco, and OXXO are labeled non-instant; MyBank is limited access (49–50); and Swish is Web-SDK-only (53–54). Giropay and Klarna Pay Now / SOFORT remain in the “currently supported” table while same-page notices say PayPal stopped support for Giropay on 2024-07-01 and Sofort on 2024-04-18 (21–46); that internal snapshot conflict is unresolved. Vaulting and recurring transactions are unsupported (57–59). The principal integration flow is only the route `configure prerequisites → integrate client → integrate server` (62–67), not evidence of initiation, authorization, completion, settlement, or funding.

Currency qualification: the fully read same-date article owner says transactions are automatically presented in EUR (`raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md:19-21`), while the developer table expresses limits in PLN, EUR, BRL, GBP, MXN, and SEK (`overview` raw 23–39). The sources do not explain whether limit denomination differs from presentment currency; no harmonization or current eligibility is inferred.

## Q3 — JavaScript v3 configuration exact route — PASS

`wiki/index.md:11` → `wiki/braintree-index.md:376` (`[[braintree-payment-methods]]`) → `wiki/concepts/braintree-payment-methods.md:24` (`[[source-braintree-local-payment-methods-configuration-javascript-v3]]`) → source frontmatter `raw_files` at `wiki/sources/braintree/source-braintree-local-payment-methods-configuration-javascript-v3.md:7-9` → `raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16.md`. The raw title/slug identify document type **Configuration**, platform **JavaScript**, version **v3** (raw lines 5–9). It is a 2026-09-16 website snapshot, not exact-SHA package evidence. The reverse ownership lookup returns this one source page.

## Q4 — JavaScript v3 configuration responsibility/prerequisite — PASS

Before accepting Local Payment Methods, the merchant must create, verify, and link a valid PayPal Business Account in the Braintree Control Panel (raw 16–19). The merchant server generates the client token; the JavaScript client uses it to initialize components and integrates Local Payment Methods (20–25). The server separately creates the local-payment transaction, and the merchant separately configures Braintree webhooks (28–29). The page's consequential final checklist item is to process a transaction successfully in Sandbox **or** Production (30); it does not say success in one proves the other. Its v3 statement is the introduction point for the JavaScript SDK; the adjacent iOS v4/Android v2 statement is not evidence for native implementation behavior. This checklist does not prove current SDK support, method/merchant/buyer eligibility, account setup, webhook delivery, transaction success, settlement, or funding.

## Shared gap sweep / extra full reads

- The provider index's direct C31 source-catalog entries are pending at audit time, but the real root → provider → concept → source → raw routes above resolve. This is not a navigation failure.
- Exact-route search found no older overview or JavaScript-v3 configuration raw to read. The broader bounded filename sweep found the expected local-method platform, server, testing, method, webhook, GraphQL, and deferred WeChat files. None was needed to answer these four questions.
- One supporting raw was fully read: `raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md`, solely to verify the overview's EUR-presentment conflict and article-owner boundary. No other related raw was used as factual authority.

**Verdict: 4/4 PASS.**

Answers match the requested objects/actions, use exact raw locators, preserve the overview table/deprecation/currency tensions, and do not invent current support or eligibility.
