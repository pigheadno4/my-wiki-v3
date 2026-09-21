# Braintree C07 final query audit

Overall: 10/10 PASS; no extra selected raw reads or post-audit repairs.
All aggregate mechanical checks passed; the pending catalog observation in group A was resolved before closure.

# Braintree C07 final query audit — group A

Timing (UTC): actual_start `2026-09-20T14:43:03Z`; analysis_end `2026-09-20T14:44:06Z`; handoff `2026-09-20T14:44:09Z`.

## `address-create-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-address-create-node]]`) → `wiki/sources/braintree/source-braintree-address-create-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/address/create/node-2026-09-16.md`.

1. **Navigation question — Where is Node Vault address creation documented?**
   - **Object/action match:** Yes — the route reaches Node `Address: Create` and `gateway.address.create(...)`; this is creation of a customer-associated Vault address, not address lookup, update, deletion, customer creation, or payment-method creation.
   - **Direct answer:** `[[source-braintree-address-create-node]]` routes to the pinned Node address-create reference. The operation's Node section shows `gateway.address.create(...)` with address fields and `customerId` in callback form.
   - **Exact raw locator:** `# Address: Create`, lines 13–19; `### Node`, lines 22–38, with the invocation at lines 24–36.
   - **Verdict:** **PASS**.

2. **Detail question — What customer association, address-ID scope and per-customer limit does the page state?**
   - **Object/action match:** Yes — these are the page-stated creation constraints for a Vault address and its customer-scoped identity, not neighboring address-operation semantics.
   - **Direct answer:** The page says `customer_id` is the only required creation attribute because a Vault address must be associated with a customer. The caller cannot specify the address ID: the gateway generates it as two alphanumeric characters. The ID is unique only within that customer, so different customers can have the same address ID. A customer can save at most 50 addresses.
   - **Exact raw locator:** required association, generated ID and customer-only uniqueness at `# Address: Create`, line 17; 50-address-per-customer limit at line 19.
   - **Verdict:** **PASS**.

## `webhooks-dispute-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-dispute-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-dispute-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/dispute/node-2026-09-16.md`.

3. **Navigation question — Where are Node dispute notification kinds and payload routes documented?**
   - **Object/action match:** Yes — the reached page is the Node dispute-webhook event reference, not general webhook delivery, parsing, retries, merchant dispute actions, or a complete dispute lifecycle.
   - **Direct answer:** `[[source-braintree-webhooks-dispute-node]]` routes to the raw page's `Notification kinds` table for the eight dispute kinds and their named trigger conditions, then to `Attributes` for notification-field descriptions and the linked direction to use `transaction` on the Dispute object.
   - **Exact raw locator:** `# Dispute > ### Notification kinds`, lines 17–46; `### Attributes`, lines 49–51.
   - **Verdict:** **PASS**.

4. **Detail question — Where are the event-specific trigger conditions and notification attributes documented?**
   - **Object/action match:** Yes — the answer uses the dispute event rows and this page's collected Attributes section; event names are not treated as delivery guarantees or a universal state sequence.
   - **Direct answer:** The table states accepted, automatically accepted, disputed, expired, lost, opened, under-review and won conditions; only `dispute_under_review` adds the qualification that the dispute is under internal review with PayPal. The collected Attributes line describes notification kind and UTC trigger time, then gives a deprecation direction to use `transaction` on the Dispute object. The rendering omits the deprecated attribute's label, so neither the source nor this audit identifies that field or reconstructs a complete payload. This is a preserved upstream/collection evidence defect, not a retrieval-route failure; the requested section and limitation are directly reachable.
   - **Exact raw locator:** event-specific rows at `# Dispute > ### Notification kinds`, lines 23–46, including the PayPal-qualified row at lines 41–43; collected attribute/deprecation prose at `### Attributes`, line 51.
   - **Verdict:** **PASS**.

## Shared checks

- **Gap sweep / extra reads:** Filename, action-text and exact-claim sweeps surfaced adjacent address find/update/delete pages, the Node dispute response object, and the general webhook parse guide. Neither fixed question needs those authorities: the two selected raws directly answer the requested create constraints and dispute event/attribute locations, while the unresolved deprecated-attribute label is explicitly preserved as an evidence defect rather than silently filled from a neighboring page. Extra full reads: none. No relevant conflict was found, and no sibling-operation, delivery, lifecycle, historical-equivalence, or response-object behavior was inferred.
- **Reciprocal routes:** **PASS** — all links in both actual routes resolve. Each source links back to its main concept; each main concept contains the source exactly once; each source contains the exact path-qualified raw link. The dispute source also has one relevant cross-cutting `[[disputes]]` reciprocal route. Direct provider-source catalog entries and other aggregate edits are still pending, but both required concept-led routes are live.
- **Raw identity:** **PASS 2/2** — manifest URL, raw Source URL, source `canonical_url`, `raw_files` owner and path-qualified Raw Sources link agree. Each raw has one source owner. Computed SHA-256 values match: address create `dc84b944256be24c0c66030ca105c10df508d9db1776b253aa1336547e6c56c2`; dispute webhooks `487d69812fe86a346e593e1a33a435360a16792d8af3bc6694a8bb798b630149`.
- **Completeness:** 2 pages; exactly 4/4 predetermined questions; 4 PASS, 0 FAIL, 0 unresolved; no retrieval repair required.

**Group verdict: PASS (4/4).**

# Braintree C07 final query audit — Group B

Scope: `address-update-node`, `address-delete-node`, and `plan-all-node`; the final six fixed questions in `tracking/ingest/braintree/braintree-campaign-07/selection-review.md`. This is group B of the single ten-question C07 audit, not an additional audit.

## Timing (UTC)

- Actual start: `2026-09-20T14:45:21Z`
- Analysis end: `2026-09-20T14:46:23Z`
- Handoff: `2026-09-20T14:46:46Z`

## Routes and fixed questions

### `address-update-node`

Actual route: `wiki/index.md` (`## PSP Indexes` -> `[[braintree-index]]`) -> `wiki/braintree-index.md` (`## Concepts` -> `[[braintree-server-sdk]]`) -> `wiki/concepts/braintree-server-sdk.md` (`## Related` -> `[[source-braintree-address-update-node]]`) -> `wiki/sources/braintree/source-braintree-address-update-node.md` (`## Raw Sources`) -> `raw/braintree/docs/reference/request/address/update/node-2026-09-16.md`.

1. **Question: Where is Node address updating documented?**
   - **Object/action match:** Yes — the reached page is Node `Address: Update` and invokes `gateway.address.update()`; it is not the separate customer-update or payment-method-update operation.
   - **Direct answer:** `[[source-braintree-address-update-node]]` routes to the collected Node address-update reference. The raw documents the operation under `# Address: Update` and shows the Node invocation under `### Node`.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/address/update/node-2026-09-16.md`, lines 13-18.
   - **Verdict:** **PASS**.

2. **Question: Which identifiers and result handling appear in the update example, and what update qualifications does this page state, if any?**
   - **Object/action match:** Yes — the identifiers and callback belong to the direct Node address-update example; the adjacent customer/payment-method links are retained only as alternative routes.
   - **Direct answer:** The example passes `"theCustomerId"`, `"theAddressId"`, an address-attribute object, and a callback receiving `err` and `result`. The page defines no `result` fields or success condition. It says an address can also be updated while updating a customer or payment method, but states no qualifications or field behavior for those linked operations. If the address or customer cannot be found, it routes to `notFoundError`.
   - **Exact raw locator:** direct invocation and callback at `# Address: Update > ### Node`, lines 18-30; alternative routes at `**NOTE**`, lines 33-34; not-found route at line 36.
   - **Verdict:** **PASS**.

### `address-delete-node`

Actual route: `wiki/index.md` (`## PSP Indexes` -> `[[braintree-index]]`) -> `wiki/braintree-index.md` (`## Concepts` -> `[[braintree-server-sdk]]`) -> `wiki/concepts/braintree-server-sdk.md` (`## Related` -> `[[source-braintree-address-delete-node]]`) -> `wiki/sources/braintree/source-braintree-address-delete-node.md` (`## Raw Sources`) -> `raw/braintree/docs/reference/request/address/delete/node-2026-09-16.md`.

3. **Question: Where is Node address deletion documented?**
   - **Object/action match:** Yes — the reached page is Node `Address: Delete` and invokes `gateway.address.delete()`; it is not customer deletion or payment-method deletion.
   - **Direct answer:** `[[source-braintree-address-delete-node]]` routes to the collected Node address-delete request reference, whose `### Node` example shows the deletion call.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/address/delete/node-2026-09-16.md`, `# Address: Delete`, lines 13-20.
   - **Verdict:** **PASS**.

4. **Question: Which identifiers are required, and what deletion effect or error guidance does this page explicitly provide?**
   - **Object/action match:** Yes — the requested identity, effect, and failure route are all stated for deleting a customer address, not for deleting its customer, payment methods, or subscriptions.
   - **Direct answer:** Both a customer ID and an address ID are required. Deleting the address from the customer also removes that address from any Vault payment methods that reference it for billing or shipping; the page does not say those payment methods, the customer, or subscriptions are deleted. If the address or customer cannot be found, the page routes to `notFoundError`.
   - **Exact raw locator:** required two-part identity at lines 15-16; invocation at lines 17-21; billing/shipping-reference removal effect at `**NOTE**`, lines 23-24; not-found route at line 26.
   - **Verdict:** **PASS**.

### `plan-all-node`

Actual route: `wiki/index.md` (`## PSP Indexes` -> `[[braintree-index]]`) -> `wiki/braintree-index.md` (`## Concepts` -> `[[braintree-server-sdk]]`) -> `wiki/concepts/braintree-server-sdk.md` (`## Related` -> `[[source-braintree-plan-all-node]]`) -> `wiki/sources/braintree/source-braintree-plan-all-node.md` (`## Raw Sources`) -> `raw/braintree/docs/reference/request/plan/all/node-2026-09-16.md`.

5. **Question: Where is Node retrieval of all plans documented?**
   - **Object/action match:** Yes — the reached page is Node `Plan: All` and documents collection retrieval through `gateway.plan.all()`; it is not plan creation, subscription creation or behavior, or merchant enablement.
   - **Direct answer:** `[[source-braintree-plan-all-node]]` routes to the collected Node plan-all request reference. The raw states that the operation returns a collection of Plan objects and shows callback and Promise forms.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/plan/all/node-2026-09-16.md`, `# Plan: All`, lines 13-15; callback and Promise examples at lines 16-26.
   - **Verdict:** **PASS**.

6. **Question: Where are the returned collection and callback/Promise result forms documented?**
   - **Object/action match:** Yes — the collection statement and both result forms belong to the same Node plan-listing operation; the recurring-billing See Also link is navigation only.
   - **Direct answer:** Line 15 states that the operation returns a collection of Plan objects. The callback example assigns the displayed `gateway.plan.all(function(err, result) { ... })` call expression to `plans`; the Promise example assigns the displayed `gateway.plan.all().then(result => { ... })` chain to `plans`. The page does not define Plan fields or establish plan creation, subscription behavior, or recurring-billing enablement.
   - **Exact raw locator:** returned collection at line 15; `### Callback`, lines 16-20; `### Promise`, lines 22-26; navigation-only recurring-billing link at `## See Also`, lines 28-31.
   - **Verdict:** **PASS**.

## Shared checks

- All three actual routes resolve through the live root index, Braintree index, `[[braintree-server-sdk]]` concept, promoted source, and exact path-qualified raw link. Each source reciprocally links `[[braintree-server-sdk]]`; the concept and provider catalog each contain one route to each audited source.
- All three selected raw files were read completely. Their source `raw_files` entries and `## Raw Sources` links resolve to those exact files.
- Gap sweep: exact filename and action-text searches for the two address operations and `gateway.plan.all()` found only the three selected Node raws. No additional raw was needed or read in full. The address-delete exceptions reference, address-update response/customer/payment-method routes, and plan response/recurring-billing routes remain navigation only because the selected raws directly answer every fixed question.
- Relevant conflict check: no competing same-object Node statement or material conflict was found. Adjacent customer deletion, payment-method deletion, customer/payment-method update, plan creation, subscription, and enablement semantics were not imported. Older same-canonical evidence was not selected because no question asks for history and no conflict required it.
- Concrete retrieval failures: none. Repairs required: none.

**Group verdict: PASS (6/6).**
