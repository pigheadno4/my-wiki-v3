# C32 Query Audit A — 8/8 PASS

- Campaign: `braintree-campaign-32`
- Approved group: A
- Mode: query audit only; no ingest/review and no repository edits
- Prompt path: `/root/c32_audit_a`

## `extend-oauth-overview` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-extend-oauth]]` → `[[source-braintree-extend-oauth-overview]]` → `[[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned Braintree Extend **OAuth Overview** webpage at canonical URL `/braintree/docs/guides/extend/oauth/overview`, pinned to `raw/braintree/docs/guides/extend/oauth/overview-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `daa10bbed4c602d3c120d01807b98b6cb6375aaa5d0e04164931532a9204a8bf` (verified).
2. **Q2 — PASS.** Its central purpose is end-to-end orientation for OAuth between separate Braintree accounts: the platform server creates a Connect URL with requested scopes and redirect URI; the merchant logs in and consents; Braintree returns an authorization code; and the server exchanges it for an access token used for delegated API calls on that merchant's behalf. In this snapshot OAuth is closed beta in production and open beta in sandbox. The overview does not establish current eligibility, completed consent, issued credentials, successful API execution or payment acceptance, and it is Extend—not authority for the separate Braintree Auth product. Exact evidence: raw lines 16–19 and 22–29; source answer/qualification at lines 14 and 18–20, with locators at 24–27.

## `extend-oauth-configuration` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-extend-oauth]]` → `[[source-braintree-extend-oauth-configuration]]` → `[[raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned Braintree Extend **OAuth Configuration** webpage at canonical URL `/braintree/docs/guides/extend/oauth/configuration`, pinned to `raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `d008d5117b26e18c49a734b3af6a46ac5de4a1584d1300f175b0604390b14a90` (verified).
2. **Q2 — PASS.** Its actual responsibility is environment-specific Control Panel creation/configuration of an OAuth application: merchant-facing display, website, logo and support data; redirect allowlisting; and internal/partner-tracking fields. Sandbox exposes OAuth Apps by default, while production access must be enabled; the snapshot labels production closed beta and sandbox open beta. The Connect URL redirect must match the allowlist, be a full URI and use HTTPS in production. This page does not expose client credentials or prescribe secret storage, and configuration does not prove merchant consent, credential issuance, API authority or payment acceptance. Exact evidence: raw lines 16–17, 20–30 and 32–47; source answer/qualifications at lines 14 and 18–32, with locators at 36–41.

## `extend-oauth-reference` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-extend-oauth]]` → `[[source-braintree-extend-oauth-reference]]` → `[[raw/braintree/docs/guides/extend/oauth/reference-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned Braintree Extend **OAuth Reference** webpage and scope catalog at canonical URL `/braintree/docs/guides/extend/oauth/reference`, pinned to `raw/braintree/docs/guides/extend/oauth/reference-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `ed921c8918d6c941aef6f28de49172248af557bdb0110d5fb143b2cff9052330` (verified).
2. **Q2 — PASS.** Its central purpose is to catalog resource-oriented and additional OAuth scopes for an application acting on a connected merchant's behalf. Dispute `/facilitated` variants and `read_facilitated_transactions` are explicitly limited to cases where the connected OAuth application was a facilitator; that restriction is not generalized to unqualified scopes. The snapshot says production closed beta and sandbox open beta. A listed scope or linked operation is not proof of enablement, merchant consent, credential issuance, operation authorization, payment acceptance or settlement; adjacent-link concatenation and the blank `dispute:search` label are preserved rendering limits. Exact evidence: raw lines 14–17, 20–79 and 82–89; source answer/qualifications at lines 14 and 18–21 and 31–37, with locators at 25–29.

## `extend-oauth-connect-urls-node` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-extend-oauth]]` → `[[source-braintree-extend-oauth-connect-urls-node]]` → `[[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16]]`.

1. **Q1 — PASS.** The exact platform-specific document is the collected Braintree Extend **OAuth Connect URLs (Node.js)** guide at canonical URL `/braintree/docs/guides/extend/oauth/connect-urls/node`, pinned to `raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and Node slug are at raw lines 1–10. Manifest SHA-256: `9ce775fd7825784187f1419e351edbf24cd7470692da7e6faa41672f0354fa8c` (verified).
2. **Q2 — PASS.** Its actual responsibility is the first Extend OAuth stage: a Node server uses the OAuth application's `clientId` and `clientSecret` with `gateway.oauth.connectUrl()` to construct the Braintree merchant login/consent URL, supplying required `redirect_uri` and `scope` plus optional `state`. Credentials must come from the matching environment; the redirect must be allowlisted and HTTPS in production. CSRF protection requires non-guessable, escaped state and an exact returned-value comparison. Own-application consent additionally intersects requested scopes with the user's current API privileges and revokes the token if that intersection changes. The snapshot labels production closed beta and sandbox open beta; placeholder credentials and URL generation do not prove secure storage, consent, issued tokens, API success or payment acceptance. Exact evidence: raw lines 14–19, 21–44, 47–57 and 60–85; source answer/qualifications at lines 14 and 18–34, with locators at 38–44.

## Shared gap sweep, extra reads, and link checks

- Fully read primary evidence: all four selected source pages and all four pinned raw files. The overview/configuration/reference/Connect pages cross-link one another; where they overlap this audit, each was already fully read as selected primary evidence. No separate related raw was needed to resolve a fact or conflict.
- Related/unlinked sweep: inspected the complete `raw/braintree/docs/guides/extend/oauth/` family and raw matches for `OAuth sequence`, `OAuth Apps`, `connect URL`, resource-oriented scopes, `shared_vault_transactions`, and `grant_payment_method`. Access-token, Shared Vault, client-side and linked operation pages were navigation-only for these questions and were not used as evidence. Matching Braintree Auth files belong to the separate product route and were not imported. No older duplicate of any exact selected page was found, so no history/conflict read was triggered.
- Link resolution: root `[[braintree-index]]` exists; the Braintree index links `[[braintree-extend-oauth]]`; that concept reciprocally links all four assigned sources; every source links the concept, declares exactly one matching `raw_files` owner and includes its exact dated Raw Sources target; all targets exist. Forward and reverse concept/source/raw lookups therefore pass. The global company/source catalog update remains pending coordinator close; the required live concept route is ready.
- Hashes: all four current raw SHA-256 values equal the approved manifest. This verifies pinned-byte provenance and immutability only; it does not prove present availability, eligibility, consent, authority, credential issuance or execution.
- Coordinator boundary: aggregate company/source catalogs and final campaign close checks remain coordinator-owned and are not closed by this group audit.

Analysis ended / handoff: `2026-10-04T03:16:35Z` UTC.
