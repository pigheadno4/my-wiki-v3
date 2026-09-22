# Braintree C14 query audit — Group A

Scope: exactly the four fixed Group A questions for Recurring Billing Overview and Plans. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): start `2026-09-22T13:35:57Z`; analysis end `2026-09-22T13:36:24Z`; handoff `2026-09-22T13:36:29Z`.

## `recurring-billing-overview`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[recurring-payments]]`) → `wiki/concepts/recurring-payments.md` (`## Sources` → `[[source-braintree-recurring-billing-overview]]`) → `wiki/sources/braintree/source-braintree-recurring-billing-overview.md` (`## Raw Sources`) → `raw/braintree/docs/guides/recurring-billing/overview-2026-09-16.md`.

1. **Where is Braintree Recurring Billing Overview documented?**
   - **Object/action match:** Braintree's product overview and subscription-status guide, not a request endpoint or Marketplace subscription alternative.
   - **Direct answer:** The promoted Recurring Billing Overview source routes to the complete collected `# Overview` guide at the path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Overview`, lines 14–19.
   - **Verdict:** PASS.

2. **What availability boundary, integration flow and subscription-status meanings are documented?**
   - **Object/action match:** product availability, setup sequence and status meanings for Braintree recurring billing, not exact request schema or settlement finality.
   - **Direct answer:** Braintree says recurring billing is incompatible with Braintree Marketplace and charges automatically in monthly increments. Setup requires a plan created by API or Control Panel plus a customer and payment method in the Vault; subscription creation associates the preferred payment method with the plan, and the stated sequence is plans → subscriptions → management. `Pending` has not started, including a future billing date; `Active` charges on the next billing date and includes trial subscriptions. `Past Due` commonly follows payment failure but may also reflect an unprocessable balance or merchant-account setup that prevents transaction creation; payment failures route to manual or configured automatic retries, with payment-method-update retry conditioned on proration. A successful retry before the final billing date returns `Active`; unsuccessful retries grow the balance and continue each billing cycle either indefinitely or until the subscription's specified number of cycles is reached. The status remains `Past Due` until that cycle count changes it to `Expired` or the subscription is canceled. `Expired` means the cycle count was reached; `Canceled` stops further billing.
   - **Exact locator:** Marketplace/monthly/setup boundary at lines 16–19; Vault prerequisite and three-step route at lines 22–29; `Pending` and `Active` at lines 37–44; `Past Due` causes/retries/transitions at lines 47–52; `Expired` and `Canceled` at lines 55–62.
   - **Verdict:** PASS.

## `recurring-billing-plans-node`

Actual route: `wiki/index.md` (`## Concepts (generic)` → `[[recurring-payments]]`) → `wiki/concepts/recurring-payments.md` (`## Sources` → `[[source-braintree-recurring-billing-plans-node]]`) → `wiki/sources/braintree/source-braintree-recurring-billing-plans-node.md` (`## Raw Sources`) → `raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16.md`.

3. **Where is Braintree Recurring Billing Plans documented?**
   - **Object/action match:** Braintree's Node.js recurring-billing plan guide, not only the dedicated plan-create/update references or subscription creation.
   - **Direct answer:** The promoted Recurring Billing Plans source routes to the complete collected `# Plans` guide at the path above.
   - **Exact locator:** raw provenance and page identity at lines 1 and 6–7; `# Plans`, lines 14–16.
   - **Verdict:** PASS.

4. **What role do plans and add-ons or discounts play, and which creation or modification boundaries are stated?**
   - **Object/action match:** plan-template and add-on/discount inheritance boundaries for new subscriptions, not propagation guarantees for existing subscriptions.
   - **Direct answer:** A plan must exist before a subscription and acts as its template for plan name/description, trial and billing schedule, amount and currency; creation supplies `plan_id`. The guide displays API plan creation, while add-ons and discounts themselves are created in the Control Panel and cannot be created or updated through the API. They may be applied case by case or associated with plans; automatic inheritance is stated for new subscriptions, while inherited details may be overridden when a subscription is created or updated. This is the raw's actual boundary and does not authorize a claim that later plan or association changes automatically propagate to existing subscriptions. EU merchants must give four weeks' notice before changing plan price and before billing after six or more months without payment; outside the EU the guide calls the notices good practice rather than required.
   - **Exact locator:** plan prerequisite/template attributes at lines 16–26; Node creation examples at lines 28–46; `plan_id` and EU notice at lines 47–49; Control Panel/API boundary at lines 52–54; case-by-case/plan association, new-subscription inheritance and override route at line 58; response routes at lines 69–73.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- Both complete raw hashes match campaign pins: Overview `8a1981226ceba54b93957207cf46ead00559374064a980e43d6802e73927867a`; Plans `56a221c8db65df502e5b33dcadbb3b62c5168b47de076f5f8f32d74a27191ec8`.
- The bounded filename/reference sweep surfaced the selected guides, older support-article overview/plans pages and dedicated Plan All/Create/Update references. The selected raws directly answer the fixed questions; adjacent pages remain outside the factual evidence set.
- Root index, concept reciprocal links, source pages and exact raw backlinks resolve for both pages. All 4/4 questions include object/action match, direct answer, locator and verdict; no repair is required.

**Group verdict: PASS (4/4).**
