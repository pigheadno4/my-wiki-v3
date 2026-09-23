# Braintree C15 query audit — Group E

Scope: exactly the four fixed Group E questions for the Node.js Server SDK Migration Guide and Upgrade to Braintree SDKs. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): start `2026-09-23T11:30:02Z`; analysis end `2026-09-23T11:33:08Z`; handoff `2026-09-23T11:33:20Z`.

## `server-sdk-migration-guide-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-server-sdk-migration-guide-node]]`) → `wiki/sources/braintree/source-braintree-server-sdk-migration-guide-node.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/reference/general/server-sdk-migration-guide/node-2026-09-16.md`.

1. **Where is Braintree Server SDK Migration Guide (Node.js) documented?**
   - **Object/action match:** Node.js server-SDK major-version migration guidance, not the generic historical integration Upgrade page or a current support matrix.
   - **Direct answer:** `source-braintree-server-sdk-migration-guide-node.md` is the promoted retrieval entry and routes to the complete collected `# Server SDK Migration Guide` Node raw at the path above.
   - **Exact locator:** raw provenance and canonical path at lines 1 and 6–7; page identity at line 14; Node applicability row and skip condition at lines 17–26.
   - **Verdict:** PASS.

2. **Which language/version scope and migration changes are documented, distinct from a universal current upgrade requirement?**
   - **Object/action match:** migration from Braintree Node SDK `2.24.0` or below to major version 3, not a requirement for new integrations, later SDK majors, or current Node/npm support.
   - **Direct answer:** The Node row limits applicability to integrations migrating from SDK `2.24.0` or below; the page says a new integration using the latest SDK can skip the guide. For the major-version-3 migration, SDK `3.0.0` targets Node 10+ and npm CLI 6+; the old gateway setup function is preserved only in the damaged rendering `functionconnect()`, with deprecation at `2.15.0`, removal at `3.0.0`, and replacement by construction of `braintree.BraintreeGateway`. The guide also changes `CreditCardGateway.expired` and `expiringBetween` from arrays of card IDs to an iterable response or stream of full card objects, renames Down For Maintenance exceptions to Service Unavailable exceptions, and adds timeout exceptions distinguishing client-request from gateway-response sources. These are migration-era statements; they do not establish current runtime, SDK, deprecation, or upgrade requirements.
   - **Exact locator:** applicability and skip condition at lines 17–26; semantic-versioning purpose and changelog route at lines 29–33; Node/npm targets at lines 36–41; damaged legacy-function rendering and constructor replacement at lines 42–53; expiring-card result correction at lines 55–57; exception changes at lines 60–66.
   - **Verdict:** PASS.

## `upgrade`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-upgrade]]`) → `wiki/sources/braintree/source-braintree-upgrade.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/reference/general/upgrade-2026-09-16.md`.

3. **Where is Braintree Upgrade to Braintree SDKs documented?**
   - **Object/action match:** historical migration guidance for three previous/legacy integration models, not the Node SDK major-version migration guide or proof of current feature availability.
   - **Direct answer:** `source-braintree-upgrade.md` is the promoted retrieval entry and routes to the complete collected `# Upgrade to Braintree SDKs` raw at the path above.
   - **Exact locator:** raw provenance and canonical path at lines 1 and 6–7; page identity at line 14; collected integration comparison at lines 17–27; legacy-upgrade scope at lines 30–34.
   - **Verdict:** PASS.

4. **Which historical integration paths and upgrade routes are described, without asserting current feature availability?**
   - **Object/action match:** unversioned historical routes from Server-to-Server, Transparent Redirect, and old Braintree.js, not a current product recommendation, compatibility matrix, or payment-method availability guarantee.
   - **Direct answer:** For Server-to-Server, the page adds client SDKs and changes the server to accept a payment-method nonce instead of credit-card details. For Transparent Redirect, it states that Drop-in replaces the integration, adds the Drop-in form, and changes the server handoff from redirect confirmation to a payment-method nonce. For old Braintree.js, it adds client SDKs and changes the server from encrypted card fields to a payment-method nonce. The page also says existing Vault users can retain access to previously vaulted customer and payment information when upgrading. Its feature table and replacement routes name no SDK versions or effective date, so they remain collected historical evidence rather than current availability or recommendation proof.
   - **Exact locator:** collected feature table at lines 17–27; legacy scope and Vault continuity at lines 30–34; Server-to-Server route at lines 37–43; Transparent Redirect route at lines 46–52; Braintree.js route at lines 55–61.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- **Full selected evidence:** both raws were read from provenance through their final sections. SHA-256 identities match the campaign pins: Node migration guide `1e5908665d025bcc9384679bbe6f5f2bcb32e1e02dfdf238689e6968c1f58ab4`; Upgrade `9d741205653f099a75cf22d6dc10fda5e6a8bd1181f8c1ebf14b499b40cb46a0`.
- **Bounded gap sweep:** filename and source-reference checks surfaced the two selected raws, their promoted sources, the lifecycle policy route, and Upgrade's navigation-only SDK overview. The selected raws directly answer all four fixed questions; alternate-language migration guides, changelog, lifecycle, client/server start pages and SDK overview remain navigation-only because no answer required additional facts from them.
- **Route integrity:** the root index links the Braintree provider index; the provider index links `braintree-server-sdk`; that concept lists both promoted sources once; each source reciprocally links the concept and its exact raw. Aggregate provider-index source rows remain pending the coordinator's campaign-close catalog update, but the required live concept routes already resolve, so this is not a source or retrieval defect.
- **Completeness:** 4/4 fixed questions include object/action match, direct answer, exact locator and verdict. Historical/version qualifications and the damaged `functionconnect()` rendering are preserved. No retrieval repair, additional promotion or extra question is required.

**Group verdict: PASS (4/4).**
