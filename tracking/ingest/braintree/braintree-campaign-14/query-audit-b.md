# Braintree C14 query audit — Group B

Scope: exactly the four fixed Group B questions from `selection-review.md` for Recurring Billing Create and Manage. Both selected raw pages were read completely; the bounded gap sweep did not expand the factual evidence set.

Timing (UTC): actual start `2026-09-22T13:22:02Z`; analysis end `2026-09-22T13:23:26Z`; handoff `2026-09-22T13:28:07Z`.

## `recurring-billing-create-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[recurring-payments]]`) → `wiki/concepts/recurring-payments.md` (`## Sources` → `[[source-braintree-recurring-billing-create-node]]`) → `wiki/sources/braintree/source-braintree-recurring-billing-create-node.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/guides/recurring-billing/create/node-2026-09-16.md`.

1. **Where is Braintree Recurring Billing Create documented?**
   - **Object/action match:** Braintree's Node.js guide for creating a recurring-billing subscription, not the dedicated request-field reference or later subscription management.
   - **Direct answer:** `source-braintree-recurring-billing-create-node.md` is the promoted retrieval entry and routes to the complete collected **Create Subscriptions** guide at the exact raw path above.
   - **Exact locator:** selected raw provenance and page identity at lines 1 and 6–7; `# Create Subscriptions`, lines 14–20.
   - **Verdict:** PASS — the live generic-concept route reaches the requested create guide and its owned raw evidence.

2. **What prerequisites, plan inheritance and transaction-flow or timing qualifications are documented?**
   - **Object/action match:** prerequisites and initial creation/charge behavior for a Braintree subscription, not later update, retry or refund behavior.
   - **Direct answer:** Creation uses a vaulted payment method and a `plan_id`; a token is the usual route, while a nonce is permitted only under linked conditions. Tokens carry no 3DS data, so applying 3DS to the first transaction requires a 3DS-enriched nonce. The subscription takes the plan's price, trial duration, billing details, add-ons and discounts, with named creation-time override categories left in the raw. A selected merchant account must use the plan currency or attempted subscription transactions trigger a validation error. With no trial and immediate billing, Braintree attempts the charge and submits it for settlement immediately; success creates an `Active` subscription and failure creates none. Future billing creates a `Pending` subscription immediately, then the first billing-date attempt moves it to `Active` or `Past Due`. A trial creates it as `Active`, charges at trial end, and a failed attempt moves it to `Past Due`; the guide separately requires consulting the linked trial risks and requirements. A subscription day runs midnight to midnight in the gateway-account time zone. Settlement submission is not evidence of completed settlement.
   - **Exact locator:** prerequisites and inheritance at lines 16–20; first-transaction 3DS at line 40; merchant-account default/currency condition at lines 43–47; overrides at lines 72–84; immediate, future-date and trial flows at lines 87–125; full-flow route at line 127; subscription-day timing at lines 128–130.
   - **Verdict:** PASS — the route exposes the prerequisites, inherited/override boundary and all material initial-flow and timing qualifications without turning the source into a request schema.

## `recurring-billing-manage-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[recurring-payments]]`) → `wiki/concepts/recurring-payments.md` (`## Platform-Specific Implementation` and `## Sources` → `[[source-braintree-recurring-billing-manage-node]]`) → `wiki/sources/braintree/source-braintree-recurring-billing-manage-node.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/guides/recurring-billing/manage/node-2026-09-16.md`.

3. **Where is Braintree Recurring Billing Manage documented?**
   - **Object/action match:** Braintree's Node.js guide for managing existing subscriptions, not subscription creation or a single update/retry/refund endpoint.
   - **Direct answer:** `source-braintree-recurring-billing-manage-node.md` is the promoted retrieval entry and routes to the complete collected **Manage Subscriptions / Manage subscription scenarios** guide at the exact raw path above.
   - **Exact locator:** selected raw provenance and page identity at lines 1 and 6–7; `# Manage Subscriptions` and `# Manage subscription scenarios`, lines 14–20.
   - **Verdict:** PASS — the live generic-concept route reaches the requested management guide and its owned raw evidence.

4. **What status-dependent update, proration, retry and refund qualifications matter, and where are detailed scenarios located?**
   - **Object/action match:** management of existing subscriptions across update eligibility, mid-cycle billing, Past Due recovery and transaction refunds; it does not import creation behavior or equate authorization/settlement submission with settlement completion.
   - **Direct answer:** Pending and Active subscriptions may receive the listed updates; Canceled and Expired subscriptions cannot be changed; Past Due updates are limited to subscription ID, payment method, merchant account and descriptor. A same-frequency plan change does not inherit the new price, a different-frequency change does, and either can take an explicit price override. EU merchants have the stated four-week notice duties. Deleting a payment method immediately cancels associated subscriptions and forfeits paid remaining days; changing a Past Due payment method automatically retries only when proration is enabled. Proration may charge or credit for a mid-cycle price change, uses days remaining and applies the recalculated amount immediately; without proration the change starts next cycle. By default a failed proration charge prevents the update, unless configured to continue and add the failed amount to the balance. Past Due subscriptions are charged automatically at each new billing cycle, can have configured between-cycle retries, and some declines are not retried. A successful manual retry sets the subscription balance to zero regardless of retry amount; automatic settlement submission is only described for the unnamed `latest` server SDK versions, while older versions submit separately, and authorization returns the subscription to `Active` or `Expired` when cycles are exhausted. Refunds apply to an existing `Settled` or `Settling` sale transaction, may be partial, and do not cancel future billing; subscription cancellation is separate. Detailed update/add-on examples remain at the dedicated update route, while advanced settings, retry/decline rules, settlement, refund and cancellation scenarios remain at the links named by the guide.
   - **Exact locator:** update eligibility, EU notice and Canceled/Expired limit at lines 20–62; plan-price and payment-method qualifications at lines 65–80; add-on/discount scenarios at lines 83–168; proration and failed-proration behavior at lines 169–184; balance/Past Due scope and retry detail routes at lines 188–220; negative balance at lines 221–223; manual retry, decline-rule route, settlement version boundary and resulting status at lines 224–242; refund eligibility, partial refund and separate cancellation at lines 243–252; further scenario routes at lines 253–260.
   - **Verdict:** PASS — the source/raw pair answers the management question with the material status, billing, retry, settlement and refund boundaries and provides exact routes for deeper scenarios.

## Shared gap sweep and completeness

- **Full selected evidence:** both raws were read from provenance through their final sections. SHA-256 identities match the campaign pins: Create `1d4904f9ceb4506f7162275a1ceecbff27d8477179b5a09f7fcbf2e5ff5ae471`; Manage `8569e3a6d3fe2d377ab67d88d3782b47f977a46b3f03a498359535d274f3319a`.
- **Bounded gap sweep:** filename and source-reference checks surfaced the two selected guides plus the already-linked subscription create/update/retry/cancel, payment-method delete, transaction refund and advanced-settings authorities. The assigned guides directly answer the four fixed questions, so those adjacent pages remain navigation-only and no extra factual read was needed.
- **Route integrity:** the root index exposes `[[recurring-payments]]`; the concept Sources section lists each promoted source once; each source reciprocally links the concept and its exact raw. The normalized Manage fact snippet is present under `## Platform-Specific Implementation`, its reciprocal link is present under `## Sources`, and the phrase `Past Due updates are limited to non-price fields` remains bounded by the source's exact four-field list.
- **Completeness:** 4/4 fixed questions include object/action match, direct answer, exact locator and verdict. No retrieval repair, additional promotion or extra question is required.

**Group verdict: PASS (4/4).**
