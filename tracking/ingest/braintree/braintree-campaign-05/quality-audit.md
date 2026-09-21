# Braintree C05 final retrieval audit

Result: 10/10 PASS; zero extra full raw reads or query repairs.
Two disjoint groups form the one planned audit. Group A pending-catalog note
predates aggregation, whose final entries passed the mechanical close checks.

# Braintree C05 final query audit — group A

## Timing (UTC)

- Actual start: `2026-09-20T13:37:50Z`
- Analysis end: `2026-09-20T13:39:32Z`
- Handoff: `2026-09-20T13:39:48Z`

## Routes and fixed questions

### `customer-create-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-customer-create-node]]`) → `wiki/sources/braintree/source-braintree-customer-create-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/customer/create/node-2026-09-16.md`.

1. **Question:** Where is Node customer creation, with or without a payment method, documented?
   **Object/action match:** Yes — Node `Customer: Create`, `gateway.customer.create()`; this is customer creation, not customer lookup or standalone payment-method creation.
   **Direct answer:** `[[source-braintree-customer-create-node]]` routes to the collected Node customer-create request guide. The raw states that a customer can be created by itself or with a payment method and supplies the base callback plus payment-method callback/Promise variants.
   **Exact raw locator:** `# Customer: Create`, lines 17 and 24–40; `## Examples > ### Customer with a payment method`, lines 77–106.
   **Verdict:** **PASS**.

2. **Question:** Where are customer-ID, billing-address, card-verification and custom-field variants documented, and what evidence gaps must be retained?
   **Object/action match:** Yes — all requested variants are within the same Node customer-create operation; no neighboring API is substituted.
   **Direct answer:** Merchant-supplied customer IDs are documented at lines 46–69 (including case-insensitivity); the nested billing-address variant at lines 109–153; validation-versus-verification behavior, account-wide verification recommendation, manual `verifyCard: true`, and the Premium Fraud Management Tools `device_data` advisory at lines 155–192; and Control Panel configuration plus custom-field callback/Promise examples at lines 197–242. Retain two collected-evidence gaps: the transaction-and-customer NOTE is missing its action/option names (lines 20–21), and the Blank customer section has no invocation example (lines 72–75). Neither gap is reconstructed.
   **Exact raw locator:** `## Examples > ### Specify your own customer ID`, lines 46–69; `#### Customer with a payment method and billing address`, lines 109–153; `#### Card verification`, lines 155–192; `### Use custom fields`, lines 197–242; gap locators lines 20–21 and 72–75.
   **Verdict:** **PASS**.

### `payment-method-find-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-payment-method-find-node]]`) → `wiki/sources/braintree/source-braintree-payment-method-find-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/payment-method/find/node-2026-09-16.md`.

3. **Question:** Where is lookup of a stored payment method by token documented?
   **Object/action match:** Yes — stored payment-method token lookup through `gateway.paymentMethod.find()`; the route and source explicitly distinguish this from payment-method nonce lookup.
   **Direct answer:** `[[source-braintree-payment-method-find-node]]` routes to the Node `Payment Method: Find` reference, whose general example passes a token to `gateway.paymentMethod.find()`.
   **Exact raw locator:** `# Payment Method: Find > ### Node`, lines 19–24.
   **Verdict:** **PASS**.

4. **Question:** What result-limitation notice is stated and where is the PayPal-account example?
   **Object/action match:** Yes — the notice applies to Payment Method Find results, and the requested example is the single-PayPal-account token lookup on that page.
   **Direct answer:** The page states only that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. The external legal policy was not read, so no hidden/returned-data or legal interpretation is added. The Single PayPal account section shows callback and Promise forms of `gateway.paypalAccount.find("theToken")`; it also routes a missing account to `notFoundError`.
   **Exact raw locator:** `# Payment Method: Find`, lines 16–17; `## Examples > ### Single PayPal account > ### Callback`, lines 29–36; `### Promise`, lines 38–43.
   **Verdict:** **PASS**.

## Shared checks

- Raw SHA-256 checks match the pinned manifest: customer-create `62e6f0e9e904d801ad59af1dfae9ee88fb87bb38911d29aa7e2dc1aac97acaa2`; payment-method-find `98c6a27f2f160d38642bf7948db4ede797a96a1727f1549b5b3d65c8a828649a`.
- Every link in both actual routes resolves, and both source pages reciprocally link `[[braintree-server-sdk]]`. The provider index's direct source catalog and other close aggregates are still pending, but the required root → provider → concept → source → raw routes already work.
- Gap sweep: filename and action-text searches surfaced the customer/payment-method guides, standalone payment-method create, payment-method response, and payment-method-nonce create/find pages. No additional page was needed to answer these four fixed questions; no extra raw was read in full or used as evidence. No material conflict was found. Older same-canonical snapshots were not required because no question asks for history/version comparison and no relevant conflict required investigation.
- Missing raw content is reported as missing, not guessed. The linked external PayPal legal policy remains unread and is not interpreted.

**Group verdict: PASS (4/4).**

# Braintree C05 final query audit — Group B

Scope: `webhooks-payment-method-node`, `customer-delete-node`, and
`customer-find-node`; the six fixed questions in
`tracking/ingest/braintree/braintree-campaign-05/selection-review.md`.

Rules read before audit: `CLAUDE.md`, `rules/query-and-synthesis.md`,
`rules/ingest.md`, `rules/psp/braintree-ingest.md`, the adopted
`rules/psp/metronome-ingest.md`, and the C05 dispatch and selection contracts.

Timing:

- actual_start_utc: `2026-09-20T13:42:16Z`
- analysis_end_utc: `2026-09-20T13:42:57Z`
- handoff_utc: `2026-09-20T13:44:19Z`

## `webhooks-payment-method-node`

Actual route: `[[index]]` -> `[[braintree-index]]` ->
`[[braintree-webhooks]]` ->
`[[source-braintree-webhooks-payment-method-node]]` ->
`[[raw/braintree/docs/reference/general/webhooks/payment-method/node-2026-09-16]]`.

1. **Navigation question — Where are payment-method revocation notifications and their payload routes documented?**
   - Object/action match: PASS — the reached Node page is the Payment Method webhook reference; it documents notification kinds/triggers and routes to notification payload attributes.
   - Direct answer: use `source-braintree-webhooks-payment-method-node`, whose pinned raw documents the revocation and customer-data-update kinds under **Notification kinds** and the notification/payment-method/customer payload routes under **Attributes**.
   - Exact raw locator: `raw/braintree/docs/reference/general/webhooks/payment-method/node-2026-09-16.md`, lines 17-24 and 27-29.
   - Verdict: **PASS**.

2. **Detail question — Which triggers and payment-method scope does this page state?**
   - Object/action match: PASS — this asks for the trigger conditions and instrument scope stated by the same Payment Method webhook page, not webhook delivery behavior generally.
   - Direct answer: `payment_method_revoked_by_customer` covers a previously enabled payment instrument revoked by the customer or Venmo, but is **currently** sent only when a customer cancels a PayPal billing agreement, removes a Venmo connection, or Venmo suspends the account for suspicious activity on that customer's Venmo account. `payment_method_customer_data_updated` covers updated customer data on a payment method, but its **currently** stated only trigger is a customer updating Enriched Customer Data in Venmo, provided the merchant enabled that feature. The page therefore states current PayPal/Venmo-specific triggers; it does not establish coverage for every stored payment method or every customer-data change.
   - Exact raw locator: same raw, notification table lines 21-24 (especially rows 23-24).
   - Verdict: **PASS**.

## `customer-delete-node`

Actual route: `[[index]]` -> `[[braintree-index]]` ->
`[[braintree-server-sdk]]` -> `[[source-braintree-customer-delete-node]]` ->
`[[raw/braintree/docs/reference/request/customer/delete/node-2026-09-16]]`.

3. **Navigation question — Where is Node customer deletion by ID documented?**
   - Object/action match: PASS — the reached page is the Node Customer Delete operation and takes a customer ID; it is not payment-method deletion.
   - Direct answer: `source-braintree-customer-delete-node` routes to the pinned Node reference, which documents customer deletion by ID and shows `gateway.customer.delete("theCustomerId", ...)`.
   - Exact raw locator: `raw/braintree/docs/reference/request/customer/delete/node-2026-09-16.md`, heading/input lines 13-16 and Node invocation lines 17-21.
   - Verdict: **PASS**.

4. **Detail question — What effects on associated payment methods and subscriptions does the page state?**
   - Object/action match: PASS — this asks for the cascade from deleting the customer, not deletion of one payment method or subscription.
   - Direct answer: when the customer is deleted, **all associated payment methods are also deleted**, and **all associated recurring billing subscriptions are canceled**. The page does not state cancellation timing, refund, proration, or paid-term effects.
   - Exact raw locator: same raw, lines 15-16.
   - Verdict: **PASS**.

## `customer-find-node`

Actual route: `[[index]]` -> `[[braintree-index]]` ->
`[[braintree-server-sdk]]` -> `[[source-braintree-customer-find-node]]` ->
`[[raw/braintree/docs/reference/request/customer/find/node-2026-09-16]]`.

5. **Navigation question — Where is lookup of a single customer by ID documented?**
   - Object/action match: PASS — the reached page is Customer Find for one customer by customer ID, not a customer search/list operation.
   - Direct answer: `source-braintree-customer-find-node` routes to the pinned Customer Find reference, which says to use the find method to look up a single customer using its ID and separately links the Customer response-object reference.
   - Exact raw locator: `raw/braintree/docs/reference/request/customer/find/node-2026-09-16.md`, lines 13-16.
   - Verdict: **PASS**.

6. **Detail question — Does the collected page contain a usable Node invocation example, and what evidence is missing?**
   - Object/action match: PASS — this checks invocation evidence in the collected Node page itself; it does not authorize reconstruction from another SDK, repository, or neighboring page.
   - Direct answer: **No.** The Node code block contains only `Code snippet NOT FOUND`. This pinned page therefore does not evidence a usable invocation, SDK method signature, callback-versus-Promise form, returned-object structure, or failure behavior. It does identify the lookup purpose/ID input and links elsewhere for the Customer response object; no absent invocation code is reconstructed.
   - Exact raw locator: same raw, purpose/response-object route at lines 15-16 and missing Node code at lines 17-20.
   - Verdict: **PASS**.

## Shared gap sweep, integrity, and conflicts

- Selected evidence was read completely: 3 raws, 71 lines total (29 + 22 + 20). Extra full raw reads: **none**.
- Filename/topic and content sweeps found no second snapshot for any exact selected canonical page. The Venmo guide repeats Enriched Customer Data webhook context, and the Grant API page contains a Customer Find navigation phrase, but neither was selected: the fixed questions ask what the selected Payment Method/Customer pages themselves state, the Grant API is a different webhook object, and no relevant conflict required another full read. No historical equivalence is inferred.
- Manifest SHA-256 checks: **PASS 3/3** — `1b427273...888ae`, `1f599f1a...aab9`, and `fb02cd74...3fd3` exactly match the three selected raw files.
- Canonical URL and `raw_files` ownership checks: **PASS 3/3** — manifest, raw `Source URL`, source `canonical_url`, and source-owned nested raw path agree for every page.
- Reciprocal/live-route checks: **PASS 3/3** — root links Braintree index; Braintree index links each source; `braintree-webhooks` or `braintree-server-sdk` links each source; each source links its concept and exact raw. No missing or duplicate selected route was found.
- Conflicts/repairs: **none**. The coordinator's concurrent shared-file aggregation is visible in the working tree, but this read-only audit found no semantic conflict in the live routes and made no repository changes. Audit result: **6/6 PASS; no query repair required**.
