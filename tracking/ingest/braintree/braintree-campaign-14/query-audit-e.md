# Braintree C14 query audit — Group E

Scope: exactly the four fixed Group E questions for Test and Braintree Auth webhooks. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): start `2026-09-22T13:40:56Z`; analysis end `2026-09-22T13:41:16Z`; handoff `2026-09-22T13:41:23Z`.

## `webhooks-test-node`

Actual route: `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-test-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-test-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/test/node-2026-09-16.md`.

1. **Where is Braintree Test Webhooks documented?**
   - **Object/action match:** Node.js reference for a webhook test notification, not the broader testing/go-live workflow or a production gateway event.
   - **Direct answer:** The promoted Test Webhook source routes to the complete collected `# Test` reference at the path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Test`, lines 14–21.
   - **Verdict:** PASS.

2. **What triggers the test notification and what payload limits are documented, distinct from a real payment event?**
   - **Object/action match:** Control Panel-triggered webhook check metadata, not a transaction, payment, subscription or other production event.
   - **Direct answer:** The sole listed kind is `check`, triggered by a test notification in the Control Panel. The Attributes section documents only notification kind and UTC trigger time; it establishes no transaction, payment, customer or other business-object payload and does not prove production delivery or payment processing.
   - **Exact locator:** kind and Control Panel trigger at lines 17–27; documented attributes at lines 30–32.
   - **Verdict:** PASS.

## `webhooks-braintree-auth-node`

Actual route: `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-braintree-auth-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-braintree-auth-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/braintree-auth/node-2026-09-16.md`.

3. **Where is Braintree Braintree Auth Webhooks documented?**
   - **Object/action match:** Node.js reference for Braintree Auth connected-merchant notifications, not OAuth access-revocation or Grant API payment-instrument events.
   - **Direct answer:** The promoted Braintree Auth Webhooks source routes to the complete collected `# Braintree Auth` reference at the path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Braintree Auth`, lines 14–25.
   - **Verdict:** PASS.

4. **What beta scope, event conditions and payload categories are stated without importing OAuth or Grant behavior?**
   - **Object/action match:** closed-beta Braintree Auth notifications that report connected-merchant events; they do not perform underwriting, application submission, PayPal linking, OAuth revocation or Grant operations.
   - **Direct answer:** Braintree Auth is stated to be closed beta, with no separate sandbox/production split on this page. `connected_merchant_status_transitioned` fires when underwriting status changes or an application is submitted. `connected_merchant_paypal_status_changed` fires when the connected merchant's PayPal account is successfully linked or unlinked to its Braintree gateway. Payload categories are notification kind, UTC trigger date/time, connected-merchant ID and OAuth application client ID, with kind-specific attributes routed to a separate unread Braintree Auth guide. The OAuth client ID is payload context and does not import OAuth access-revocation or Grant payment-instrument semantics.
   - **Exact locator:** closed-beta notice at lines 17–18; notification-kind scope at lines 23–25; event conditions at lines 27–30; payload categories and additional-attribute route at lines 33–35.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- Both complete raw hashes match campaign pins: Test `6ebaf82862bef931ae4e3d269c2f2076f2e68fffbb59c36740b3d862001cc1fd`; Braintree Auth `f10925a21668ea9883d15d1742fabd01e7d4976b44171b96b0cc7747704ca8c4`.
- The bounded filename/reference sweep surfaced the selected raws plus the linked testing/go-live and Braintree Auth guide pages. The fixed questions are complete from the selected evidence; adjacent guides remain navigation-only.
- Provider index, concept, reciprocal source links and exact raw backlinks resolve for both pages. All 4/4 questions include object/action match, direct answer, locator and verdict; no repair is required.

**Group verdict: PASS (4/4).**
