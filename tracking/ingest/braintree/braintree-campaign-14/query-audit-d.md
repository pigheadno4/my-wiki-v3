# Braintree C14 query audit — Group D

Scope: exactly the four fixed Group D questions for Disbursement and Sub-merchant Account webhooks. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): start `2026-09-22T13:34:03Z`; analysis end `2026-09-22T13:34:27Z`; handoff `2026-09-22T13:34:32Z`.

## `webhooks-disbursement-node`

Actual route: `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-disbursement-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-disbursement-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16.md`.

1. **Where is Braintree Disbursement Webhooks documented?**
   - **Object/action match:** Node.js notification reference for Braintree disbursement events, not payout initiation, settlement submission or merchant receipt.
   - **Direct answer:** The promoted Disbursement Webhooks source routes to the collected `# Disbursement` reference at the raw path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Disbursement`, lines 14–21.
   - **Verdict:** PASS.

2. **What event conditions and payload categories are stated, without inferring merchant payout guarantees?**
   - **Object/action match:** webhook trigger meanings and payload routes for Braintree-managed funding, not a payout-arrival or settlement-finality guarantee.
   - **Direct answer:** `disbursement` means Braintree sent a disbursement, described as leaving its bank that day, and is sent once per merchant account per day; deprecated `transaction_disbursed` means a transaction was marked for disbursement, also described as leaving Braintree's bank that day. Both are limited to Braintree-funded merchant accounts, and receipt requires Braintree-managed funding for the selected account, indicated by Disbursement Summary report availability. The concatenated attributes text routes kind, UTC trigger time, disbursement ID/amount/date/debit-or-credit type, associated transaction IDs, merchant account, retry and success indicators. Bank departure does not establish merchant receipt timing, settlement finality or payout success.
   - **Exact locator:** event table and funding/per-account boundaries at lines 23–33; payload and managed-funding categories at lines 36–38.
   - **Verdict:** PASS.

## `webhooks-sub-merchant-account-node`

Actual route: `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-sub-merchant-account-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-sub-merchant-account-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/sub-merchant-account/node-2026-09-16.md`.

3. **Where is Braintree Sub-merchant Account Webhooks documented?**
   - **Object/action match:** Node.js reference for sub-merchant approval/decline notifications, not merchant-account creation or onboarding submission.
   - **Direct answer:** The promoted Sub-merchant Account Webhooks source routes to the collected `# Sub-merchant Account` reference at the raw path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Sub-merchant Account`, lines 14–21.
   - **Verdict:** PASS.

4. **Which account-event conditions and payload routes are stated, distinct from creating or activating an account?**
   - **Object/action match:** notifications that report an approval or decline decision; the webhook does not create, submit, approve or activate an account.
   - **Direct answer:** `sub_merchant_account_approved` is triggered when a sub-merchant has been approved; `sub_merchant_account_declined` is triggered when one has been declined. Payload routes are the notification kind, UTC trigger date/time and a `MerchantAccount` object. Declined notifications link to the Marketplace onboarding guide for additional attributes, but that unread page remains navigation-only. The selected raw establishes no creation, activation, funding-readiness, transaction-eligibility, decision-criteria, reason or timing behavior.
   - **Exact locator:** event conditions at lines 17–26; payload categories at lines 29–31; declined-attribute route at line 33.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- Both complete raw hashes match campaign pins: Disbursement `c4b0f55c373ed4293b032c158372e4636bccacfb1864aa909ea85435614c1eb7`; Sub-merchant `ade199556b01935c07a94666cd86ba9910deb9fc894b01215a4318c4801fe0b6`.
- The bounded filename/reference sweep surfaced only the two selected raws plus the linked Marketplace confirmation guide; the latter was not needed to answer the fixed questions and remains navigation-only.
- Provider index, concept, reciprocal source links and exact raw backlinks resolve for both pages. All 4/4 questions include object/action match, direct answer, locator and verdict; no repair is required.

**Group verdict: PASS (4/4).**
