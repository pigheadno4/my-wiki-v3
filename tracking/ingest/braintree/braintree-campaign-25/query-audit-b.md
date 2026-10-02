# Braintree C25 fixed query audit — Group B

Scope: `auth-configuration` and `auth-oauth-flow-node`; four predetermined questions. Selected raws were read completely. Analysis ended: `2026-10-02T09:57:50Z`.

## auth-configuration

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-auth]]`) → `wiki/concepts/braintree-auth.md` (`## Sources` → `[[source-braintree-auth-configuration]]`) → `wiki/sources/braintree/source-braintree-auth-configuration.md` (`## Raw Sources`) → `raw/braintree/docs/guides/braintree-auth/configuration-2026-09-16.md`.

1. **Where is the Braintree Auth configuration guide?**
   - **Object/action match:** Braintree Auth platform OAuth-application configuration, not the merchant Connect interaction or post-Connect code exchange — match.
   - **Direct answer:** The route above reaches the dedicated configuration source and its exact collected raw.
   - **Exact raw locator:** `# Configuration`, raw lines 14–45; identity metadata and canonical source URL at lines 1–9.
   - **Verdict:** **PASS**.

2. **What setup roles and prerequisites does this guide itself state?**
   - **Object/action match:** Platform-owned OAuth application setup and prerequisites — match.
   - **Direct answer:** The page marks Braintree Auth closed beta; only after beta acceptance can the platform create an OAuth application. The platform selects the Production or Sandbox Control Panel for the environment, creates the app, supplies required merchant-facing identity/support information, and registers full redirect URIs in advance (HTTPS is required in production). The resulting environment credentials are the platform's `client_id` and `client_secret`; they must be kept securely on the platform's server for server-SDK calls and the later Connect flow. Merchants see the configured identity/support information and later authorize the app, but this page assigns configuration to the platform and does not prove beta acceptance, merchant authorization, or payment readiness.
   - **Exact raw locator:** availability and beta prerequisite at `# Configuration > AVAILABILITY`, lines 16–19; environment and Control Panel steps at lines 22–26; configured information at lines 28–43; redirect prerequisite at line 41; credential ownership/use at line 45.
   - **Verdict:** **PASS**.

## auth-oauth-flow-node

Actual route: `wiki/index.md` (`[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-auth]]`) → `wiki/concepts/braintree-auth.md` (`## Sources` → `[[source-braintree-auth-oauth-flow-node]]`) → `wiki/sources/braintree/source-braintree-auth-oauth-flow-node.md` (`## Raw Sources`) → `raw/braintree/docs/guides/braintree-auth/oauth-flow/node-2026-09-16.md`.

1. **Where is the Braintree Auth Node OAuth-flow guide?**
   - **Object/action match:** Node.js Braintree Auth authorization-code exchange and credential lifecycle, not generic transaction authorization or Connect URL construction — match.
   - **Direct answer:** The route above reaches the dedicated Node OAuth-flow source and its exact collected raw.
   - **Exact raw locator:** `# OAuth Flow`, raw lines 14–125; identity metadata and canonical source URL at lines 1–9.
   - **Verdict:** **PASS**.

2. **What authorization sequence, roles and credential boundaries does this guide itself state?**
   - **Object/action match:** Post-Connect OAuth authorization sequence, actors, and credentials — match.
   - **Direct answer:** After the merchant completes Connect, Braintree redirects the merchant to the platform-provided `redirect_uri` with the returned `state`, Braintree `merchantId`, and authorization `code`. The platform's Node server configures `BraintreeGateway` with its OAuth `clientId` and `clientSecret`, exchanges the code through `gateway.oauth.createTokenFromCode()`, and receives an access token, expiration, and refresh token. The access token is then used for Merchant API actions on that connected merchant's behalf; this page does not choose or enumerate OAuth scopes. The guide states a 24-hour access-token lifetime and a 180-day initial refresh-token lifetime; refresh returns a new access token and refresh token but does not itself establish revocation of the original. The platform can revoke an access token, while the connected merchant can revoke OAuth access in the Control Panel; use of a revoked token through the Merchant API produces an authentication error. The selected page labels Braintree Auth closed beta and does not prove current eligibility or enablement.
   - **Exact raw locator:** redirect and returned values at `## Redirect and authorization grant`, line 23; platform credential configuration and code exchange at `## Getting an access token`, lines 26–57; merchant-scoped use at `## Using an access token`, lines 59–61; token lifetimes/refresh at `## Managing access tokens`, lines 64–97; platform and merchant revocation boundaries at lines 98–125.
   - **Verdict:** **PASS**.

## Shared gap sweep, extra reads, and reciprocity

- **Bounded sweep:** Filename and targeted-content searches covered the Braintree Auth capsule plus OAuth-named Braintree raws. The six client-side/branding variants and the separate Extend OAuth guides did not answer either selected page's exact question. No older snapshot of either selected canonical page was found.
- **Extra full read:** `raw/braintree/docs/reference/general/webhooks/oauth/node-2026-09-16.md`, selected because the OAuth-flow raw links it and the sweep exposed an availability qualification. Its lines 17–18 say OAuth is closed beta in production and open beta in sandbox, while the selected OAuth-flow guide says Braintree Auth is closed beta without an environment split. This is a source-scoped availability tension: it does not alter the guide-specific answers or cause a retrieval failure, but the unqualified selected-page notice must not be generalized into a current cross-document availability claim. No further related raw was needed.
- **Reciprocity:** **PASS**. The root routes to the Braintree index; the Braintree index routes to `[[braintree-auth]]` and both selected source pages; the concept routes to both sources; each source links back to `[[braintree-auth]]` and links its exact owned raw under `## Raw Sources`; each `raw_files` entry matches that raw path. No broken or wrong-object route was found.

Final handoff: `2026-10-02T09:58:41Z`.
