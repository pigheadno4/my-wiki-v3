# C26 fixed query audit — Group B

**Verdict: PASS — 4/4 fixed questions answered from exact sources and hash-matched full raws.**

Scope: Braintree Auth client-side JavaScript v3 plus branding JavaScript v3. This audit treats `wiki/index.md`, `wiki/braintree-index.md`, and `wiki/concepts/braintree-auth.md` as retrieval only; the source pages and fully read immutable raws supply the answers.

## 1. Where is the JavaScript v3 Auth client-side connect guide?

- **Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:15-32` → `wiki/concepts/braintree-auth.md:26-33` → `wiki/sources/braintree/source-braintree-auth-client-side-javascript-v3.md` → `raw/braintree/docs/guides/braintree-auth/client-side/javascript/v3-2026-09-16.md`.
- **Object/action match:** PASS. The source and raw are specifically the JavaScript v3 browser-side Braintree Auth **Client-side Connect Flow**, not generic transaction authorization or another client variant.
- **Canonical locator:** `https://developer.paypal.com/braintree/docs/guides/braintree-auth/client-side/javascript/v3`; source frontmatter lines 2-8; raw metadata/title lines 1-14.
- **Raw integrity:** PASS. Full raw read, 53 lines. SHA-256 `99322a25cd502f661d4d01f9966639f4f1f514f75fd93dff80d780352e318820`, matching `tracking/ingest/braintree/braintree-campaign-26/manifest.json`.

## 2. What client flow, responsibilities and qualifications does this variant state?

- **Direct answer:** The platform page loads `braintree-oauth-connect.js`, instantiates `BraintreeOAuthConnect`, and supplies a `connectUrl` generated on the platform server by the Braintree server library. The page renders **Connect with Braintree** in a required container. `connectUrl` and `container` are required; `onError` is optional and receives an object with a `message`; `environment` is optional and accepts `production` (default) or `sandbox`. If a new-signup merchant selects **Finish Later**, Braintree returns the merchant to the configured **redirect URI** with `error=access_denied&error_description=user%20denied%20access`; the platform can parse it and leave the Connect button available for a later attempt.
- **Responsibility boundary:** The server generates the forward `connect_url`; the browser library receives it and renders the button. The `redirect URI` is the distinct return destination after OAuth completion or Finish Later. The assigned page does not document the later authorization-code exchange.
- **Qualifications:** The snapshot labels Braintree Auth closed beta and supplies a contact route. It proves neither present availability/account eligibility nor completed connection, live payment acceptance, payment authorization, or parity with native variants. It does not state that the merchant experience opens in a modal, new window, or any other particular presentation surface.
- **Exact raw locators:** availability lines 16-17; library plus server-generated `connect_url` lines 20-22; constructor example lines 23-37; required/optional parameter table lines 38-45; Finish Later denial return and retry state lines 48-50.
- **Verdict:** PASS.

## 3. Where is the JavaScript v3 Auth branding guide?

- **Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:15-32` → `wiki/concepts/braintree-auth.md:26-33` → `wiki/sources/braintree/source-braintree-auth-branding-javascript-v3.md` → `raw/braintree/docs/guides/braintree-auth/branding/javascript/v3-2026-09-16.md`.
- **Object/action match:** PASS. The source and raw are specifically the JavaScript v3 Braintree Auth **Branding** guide for merchant-facing presentation and Connect-button behavior, not an SDK-capability or payment-acceptance guide.
- **Canonical locator:** `https://developer.paypal.com/braintree/docs/guides/braintree-auth/branding/javascript/v3`; source frontmatter lines 2-8; raw metadata/title lines 1-14.
- **Raw integrity:** PASS. Full raw read, 103 lines. SHA-256 `c91b8ad5a2872835a95f5a412d9e9cc99a892d68540fca887d3fcd827ff31b54`, matching the C26 manifest.

## 4. Which branding actions and required/optional conditions does this variant state?

- **Brand and dashboard presentation:** Present the unified experience under the merchant-facing brand **PayPal powered by Braintree** and use one of the supplied horizontal or vertical dashboard logos (raw lines 20, 23-40).
- **Payment-mark condition:** Use the combined image when presenting major credit/debit cards plus PayPal; use the cards-only image for credit/debit cards only (lines 44-60). These marks are presentation assets, not proof of current enablement, eligibility, or acceptance.
- **Recommended conditional copy:** The guide recommends explanatory copy and supplies a generic learn-more link. If the platform intends to create transactions for merchants, use the acceptance-oriented copy; if it only connects existing Braintree merchants without running transactions, use the account-linking call to action (lines 65-82). This copy is recommended, not stated as mandatory.
- **Button choices and required redirect:** Display **Connect with Braintree**. Using `braintree-oauth-connect.js` is preferred; manually adding the supplied image is the stated alternative (lines 84-92). After click, the merchant **must be redirected** to the unified card-and-PayPal signup form using the server-generated `connect_url` (line 93).
- **Post-authorization condition:** Only after the merchant authorizes the application and returns to the platform dashboard, do not initialize `braintree-oauth-connect.js` or display the Connect button (line 95). This condition belongs to the branding source; it does not create a broader modal rule.
- **Optional resource route:** Download the partner-assets archive to host the assets, or use the provided code (lines 100-102).
- **Qualification:** Closed-beta snapshot only (lines 17-18); no current-support, account-eligibility, OAuth-permission, cross-variant-parity, or payment-authorization/acceptance inference.
- **Verdict:** PASS.

## Shared gap, extra-read and reciprocal checks

- **Bounded gap sweep:** Inspected the Braintree Auth raw inventory and exact matches for `modal`, `connect_url`, redirect terms, `braintree-oauth-connect`, and **Connect with Braintree**. No additional assigned authority was needed. The iOS/Android variants remain distinct evidence and were not used to infer parity.
- **Relevant extra full reads:** Read `raw/braintree/docs/guides/braintree-auth/connect-2026-09-16.md` (39 lines) and `raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16.md` (78 lines), through their source pages, solely to verify the hosted-flow and URL-responsibility boundary. They confirm: the `connect_url` is server-built and sends the merchant into OAuth; the redirect URI is the allowlisted return target; the Connect guide describes a redirect to a Braintree-hosted cobranded page. Neither creates a modal claim for the assigned JavaScript client-side raw.
- **Reciprocal checks:** Both source `canonical_url` and `raw_files` entries match the raw metadata/paths; all quoted detail locators resolve to the stated raw lines; both source pages link back to `[[braintree-auth]]`, and that concept routes back to both sources. The current `wiki/braintree-index.md:32` phrase “modal/redirect distinctions” is catalog navigation, not factual modal evidence; the exact branding raw states redirect behavior, and the exact client-side raw is silent on presentation surface.
- **Gap result:** No factual gap affecting the four fixed questions; no promotion recommendation because all used raws already have source pages.
- **Aggregate boundary:** The provider catalog may be changing concurrently; coordinator owns catalog completeness. This audit makes no aggregate-count or campaign-completion claim.

Analysis end: `2026-10-02T11:10:22Z`
Handoff UTC: `2026-10-02T11:10:22Z`
