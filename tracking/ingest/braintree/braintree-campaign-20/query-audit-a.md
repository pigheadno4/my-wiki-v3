# Braintree C20 fixed query audit — Group A

**Verdict: PASS (4/4).** The two routes are complete, the four predetermined questions answer the requested object/action, and the evidence keeps Control Panel login 2FA separate from API-key rotation.

## Two-Factor Authentication

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-control-panel.md` → `wiki/sources/braintree/source-braintree-control-panel-security-two-factor-authentication.md` → `raw/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication-2026-09-16.md`

**Pinned evidence:** SHA-256 `401662db8100f94b16ada64a19b38abb3f6561de93f6e7df8797dd4f62a15e86` verified. Manifest URL, source `canonical_url`, and raw line 1 all match `https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication`.

1. **Where is Braintree Control Panel two-factor authentication documented?**
   - **Object/action match:** Yes — the route reaches Braintree user login protection for the Control Panel, not payment authentication, 3D Secure, fraud screening, or API-key handling.
   - **Direct answer:** It is documented by `source-braintree-control-panel-security-two-factor-authentication`, backed by the pinned raw article above. The article identifies 2FA as an extra access-control layer on a Control Panel user and states its collected access requirement and sign-in flow.
   - **Exact raw locator:** `# Two-Factor Authentication`, lines 14–18.
   - **Verdict:** PASS.

2. **Which access, setup and recovery boundaries does this page itself document?**
   - **Object/action match:** Yes — the answer is limited to access, setup, fallback, and recovery boundaries stated by this 2FA page itself.
   - **Direct answer:** The page says that, starting in September 2023, every Braintree user must enable 2FA to access the Control Panel and then signs in with a normal password plus a separate app or SMS code. It provides automatic and manual setup routes; after 2FA is enabled, a WebAuthn U2F-compatible hardware key can be registered, subject to browser support. At sign-in it orders hardware key, authenticator app, then SMS and permits fallback. If no factor works, an Account Admin can temporarily disable another user's 2FA so it is set up again at next login; only Account Admins can do that, and support is the route when no admin is available. Users cannot disable 2FA for themselves; self-service reset is for changing a phone number or authenticator app, and an incomplete reset requires setup again.
   - **Exact raw locator:** access and factors at lines 16–18; setup at `## How to enable 2FA`, lines 21–37; hardware-key setup/prerequisite at lines 40–55; sign-in order/fallback at lines 60–77; administrator recovery at lines 94–113; self-service reset boundary at lines 116–131.
   - **Verdict:** PASS.

## Rotating API Keys

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-control-panel.md` → `wiki/sources/braintree/source-braintree-control-panel-security-rotating-api-keys.md` → `raw/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys-2026-09-16.md`

**Pinned evidence:** SHA-256 `670283bdca303091e58b43700fd1e8506c47fc0495522cd7e55b7b667c5f34b1` verified. Manifest URL, source `canonical_url`, and raw line 1 all match `https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys`.

3. **Where is Braintree API-key rotation documented?**
   - **Object/action match:** Yes — the route reaches server API-credential rotation, not Control Panel login 2FA or customer/payment authentication.
   - **Direct answer:** It is documented by `source-braintree-control-panel-security-rotating-api-keys`, backed by the pinned raw article above. The article defines generating replacement API keys after possible exposure or compromise as rotating API keys.
   - **Exact raw locator:** `# Rotating API Keys`, lines 14–18.
   - **Verdict:** PASS.

4. **Which rotation triggers and access boundaries does this page itself state?**
   - **Object/action match:** Yes — the answer covers the rotation trigger and the page's stated generation/access scope, without importing role eligibility from another page.
   - **Direct answer:** Generate new keys whenever there is any chance of exposure or compromise; the page gives a developer leaving or keys being sent by email as examples. It says to generate a new set **for your user** through Control Panel → gear → **API** → **API Keys**; it does not state which roles or permissions may do so. New keys do not revoke old keys: old keys remain valid until deletion. Update code, confirm the new keys work, and only then delete the old keys.
   - **Exact raw locator:** trigger and examples at line 16; overlapping validity at line 18; deletion warning at lines 21–22; per-user Control Panel route at lines 26–33; code-update/confirmation/deletion order at line 35.
   - **Verdict:** PASS.

## Group checks

- **Bounded gap sweep:** One filename/content sweep covered `two-factor`, `2FA`, `rotating API keys`, `API key` rotation, and the source-declared related raw reference. It found the two pinned pages plus adjacent `important-gateway-credentials`, `log-in-with-paypal`, `managing-users-roles`, and SSO material. None is needed for these questions, which explicitly ask what each selected page itself documents. The credential inventory remains navigation-only; the PayPal-login 2FA page concerns a separate login mode and was not used to broaden Braintree-login claims.
- **Extra full reads:** None. Both selected pinned raw files were read completely; no gap or conflict required another raw file.
- **Reciprocal-link check:** PASS. `wiki/index.md` routes to `braintree-index`; the provider index links both source pages and the `braintree-control-panel` concept; the concept links both sources; each source links back to the concept and to its exact path-qualified raw file. Source `raw_files` entries match the manifest paths.
