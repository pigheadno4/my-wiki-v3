# Braintree C03 final retrieval audit

Ten fixed page-scoped questions PASS. Group B discovered one material
cross-document qualification requiring a bounded post-audit correction before
closure; do not equate the ten query passes with zero content repairs.
Group A catalog-pending observation predates final aggregation.

# Braintree C03 final query audit — group A

## transaction-submit-for-settlement-node

**Actual route:** `wiki/index.md` § PSP Indexes → `[[braintree-index]]` → `wiki/braintree-index.md` § Concepts → `[[braintree-server-sdk]]` → `wiki/concepts/braintree-server-sdk.md` § Related → `[[source-braintree-transaction-submit-for-settlement-node]]` → `wiki/sources/braintree/source-braintree-transaction-submit-for-settlement-node.md` § Raw Sources → `raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16.md`.

1. **Question:** Where is explicit Node transaction submission for settlement documented?
   - **Object/action match:** Yes — Node `transaction.submitForSettlement()` for explicitly submitting an existing transaction for settlement; not transaction sale or partial settlement.
   - **Direct answer:** `[[source-braintree-transaction-submit-for-settlement-node]]` is the retrieval entry. Its exact raw documents the operation under `# Transaction: Submit For Settlement > ### Node`, including the Node callback call and success/error branches.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16.md`, lines 13–25.
   - **Verdict:** PASS

2. **Question:** Where are settlement-amount adjustments, availability qualifications and supplemental-data examples documented?
   - **Object/action match:** Yes — amount changes, authorization adjustments, and extra data supplied through Node `submitForSettlement()`; not generic authorization or sale-request fields.
   - **Direct answer:** The exact raw's `## Examples > ### Specifying settlement amount` documents changed versus omitted amounts, the once-only lower-amount path, and the separate partial-settlement route. Its nested `#### Authorization adjustments` and `#### Availability` qualify automatic adjustments as applying to eligible/select merchants and processors and route real-time declines to validation errors. `### Specifying Level 2 and 3 data` contains the approval-gated Node callback/Promise examples and states that this data overrides sale-request data and should be supplied at one request point, not both. `### Shipping address information` gives the same override/either-or rule and internal-approval qualification for shipping fields; `### Specifying order ID` contains the Node callback/Promise examples for that additional information.
   - **Exact raw locator:** same raw, lines 30–52 (settlement amount), 33–42 (adjustments and availability), 54–129 (Level 2/3 qualification and Node examples), 131–136 (shipping qualification), and 137–166 (order-ID Node examples).
   - **Verdict:** PASS

## client-token-generate-node

**Actual route:** `wiki/index.md` § PSP Indexes → `[[braintree-index]]` → `wiki/braintree-index.md` § Concepts → `[[braintree-server-sdk]]` → `wiki/concepts/braintree-server-sdk.md` § Related → `[[source-braintree-client-token-generate-node]]` → `wiki/sources/braintree/source-braintree-client-token-generate-node.md` § Raw Sources → `raw/braintree/docs/reference/request/client-token/generate/node-2026-09-16.md`.

1. **Question:** Where is Node client-token generation documented?
   - **Object/action match:** Yes — Node `clientToken.generate()` returning authorization/configuration for client-SDK initialization; not payment authorization.
   - **Direct answer:** `[[source-braintree-client-token-generate-node]]` is the retrieval entry. Its exact raw documents the token's initialization role and both callback and Promise forms under `# Client Token: Generate`.
   - **Exact raw locator:** `raw/braintree/docs/reference/request/client-token/generate/node-2026-09-16.md`, lines 13–29.
   - **Verdict:** PASS

2. **Question:** Where is the customer-ID variant documented, and what qualifications does this page state?
   - **Object/action match:** Yes — customer-scoped Node client-token generation for a customer already in the merchant vault; not customer creation or a generic authentication guarantee.
   - **Direct answer:** `## Examples > ### Specify a customer ID` documents callback and Promise calls with `customerId`. The page qualifies the variant as enabling Drop-in to present a returning customer with saved payment methods when the customer's vault ID is provided; if the customer is not found, the response contains `Customer specified by customer_id does not exist`. It states no broader failure semantics.
   - **Exact raw locator:** same raw, lines 34–54.
   - **Verdict:** PASS

## Shared checks

- **Gap sweep:** Filename and content sweeps found adjacent settlement, partial-settlement, authorization-adjustment, transaction-response, customer, and client-token material. No extra raw was selected for full reading: both fixed page-specific questions were answered by the fully read exact canonical raws, neither promoted source lists a related raw API reference, and the sweep exposed no conflict requiring investigation. Older-snapshot equivalence was not inferred.
- **Reciprocal links and provenance:** PASS — each source links to `[[braintree-server-sdk]]`; that concept links back to each source; each source's Raw Sources link resolves to its pinned raw. SHA-256 matches the manifest: submit-for-settlement `83ed4cc7250f0a35cb0a3879b1d2c1d05d12f2d263f051ff7a4156ac69f13d98`; client-token generation `bb50a91e4bd0978238021940dc3031e40695315e82e1df8afb4c59eee31144d2`.
- **Aggregation boundary:** The root-index → Braintree-index → existing `braintree-server-sdk` concept routes are live. The two sources are not yet aggregated into the provider index's Website documentation list, consistent with the stated pending company/provider-index close work; this does not break either audited route.
- **Extra full reads:** None beyond the two selected exact raws.
- **Repairs:** None.

## Timing (UTC)

- Started: `2026-09-19T12:39:27Z`
- Analysis ended: `2026-09-19T12:41:21Z`
- Handoff: `2026-09-19T12:41:26Z`

# Braintree C03 final query audit — group B

## Timing (UTC)

- Started: `2026-09-19T12:43:39Z`
- Analysis ended: `2026-09-19T12:45:53Z`
- Handoff: `2026-09-19T12:46:50Z`

## authorization-overview

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-web-sdk.md` → `wiki/sources/braintree/source-braintree-authorization-overview.md` → `raw/braintree/docs/guides/authorization/overview-2026-09-16.md`

1. **Navigation — compare client tokens and tokenization keys for client authorization.** Object/action match: client-SDK authorization credential comparison, not payment authorization. Direct answer: the Braintree client-authorization overview source is the comparison route; its raw defines both authorization forms and supplies their capability comparison. Exact raw locator: `# Overview`, line 16; `## Types of authorization`, lines 21–25; `### Capabilities`, lines 30–44. **PASS**
2. **Detail — capability differences and selection guidance.** Object/action match: locate the comparison and guidance for choosing the client-authorization form. Direct answer: capability differences are in the `### Capabilities` table; tokenization-key guidance is under `## When to use tokenization keys`, client-token guidance under `## When to use client tokens`, and mixed guest/registered use under `## Using both`. Exact raw locator: lines 30–44, 47–58, and 61–63. **PASS**

## transaction-void-node

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-server-sdk.md` → `wiki/sources/braintree/source-braintree-transaction-void-node.md` → `raw/braintree/docs/reference/request/transaction/void/node-2026-09-16.md`

3. **Navigation — Node transaction-void operation.** Object/action match: Node server-SDK transaction void, not refund or client authorization. Direct answer: the transaction-void source routes to the Node `gateway.transaction.void()` operation and its result handling. Exact raw locator: `# Transaction: Void`, lines 13–23 (invocation at lines 18–22). **PASS**
4. **Detail — eligible states and authorization-reversal qualification stated by this page.** Object/action match: void eligibility plus the page-stated reversal effect. Direct answer: this page states `authorized` and `submitted for settlement` are eligible, with `settlement pending` eligible for PayPal; when voided, Braintree performs an authorization reversal **if possible** to remove the pending card charge. Exact raw locator: `# Transaction: Void`, line 15. **PASS** for the page-scoped question; see the material cross-document qualification in the shared gap notes.

## authorization-client-token

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-web-sdk.md` → `wiki/sources/braintree/source-braintree-authorization-client-token.md` → `raw/braintree/docs/guides/authorization/client-token-2026-09-16.md`

5. **Navigation — client token and server-to-client role.** Object/action match: client-SDK application authorization and token delivery, not transaction authorization or payment success. Direct answer: a client token is a signed JWT carrying client-SDK configuration and authorization; the server generates and provides it, and the client obtains it and initializes the SDK so the application can communicate directly with Braintree. Exact raw locator: `# Client Token`, lines 16–20. **PASS**
6. **Detail — validity or reuse qualifications stated by this guide.** Object/action match: client-token lifetime and invalidation, not payment-method-token reuse. Direct answer: client tokens are valid for **up to** 24 hours; a token containing a customer ID is invalidated if it creates an excessive number of payment methods. The fully read guide gives no numeric threshold, fixed use count, or broader reuse guarantee. Exact raw locator: `# Client Token`, line 22 (full raw ends at line 23). **PASS**

## Shared checks and gap notes

- **Pinned evidence:** all three selected raws match the C03 manifest SHA-256 values: authorization overview `3449c348a8fc8a56ab70d5d6fa01dcca984d9957a825c6c9a90669dca7733c85`; transaction void `4c2dc7bfd845476b74de0f13b30f4072833cb87fa822ee32fdf5c8027f62efcf`; client token `60163770c2e79dbd7b5e47aff3c8a617d4ec2e94540fedf7b4441b4285b65082`.
- **Reciprocal/navigation links:** root → Braintree index, provider index → each source and relevant concept, concept → each assigned source, and each source → concept plus exact raw all resolve. Each selected raw has the expected single source owner.
- **Gap sweep:** searched Braintree raw filenames and content for authorization/client-token/void variants and the answer-bearing phrases. No extra full read was needed for the two authorization pages; their fixed questions are answered by their exact raws. Two related void authorities were read completely: `raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16.md` and `raw/braintree/docs/reference/general/statuses-2026-09-16.md`. No historical raw was selected because no question asks for history/version comparison and no historical read was needed to answer.
- **Material qualification:** the selected Node raw broadly says PayPal `settlement pending` at line 15, while the Control Panel article narrows that case to PayPal multiple partial settlements at lines 109–115 and the statuses page says “certain PayPal transactions” at lines 93–97. This is an unresolved upstream scope difference. It does not defeat the fixed page-stated question, but the selected source/raw answer must not be generalized into universal PayPal `settlement pending` eligibility without that warning and those evidence routes.
- **Result:** 6/6 fixed questions have live routes, correct object/action matches, direct raw-supported answers, and exact locators; no retrieval miss. The void qualification above is the only material uncertainty found.


---

# Braintree C03 transaction-void post-audit correction review

## Timing (UTC)

- Started: `2026-09-19T12:48:34Z`
- Ended: `2026-09-19T12:50:40Z`

## Verdict

**Approved as a minimal narrow correction.** The pinned primary raw remains the owner and is unchanged. The two fully read related raws are supplemental conflict evidence for the warning below; they should be added to this source page's `raw_files` and `## Raw Sources`, but must not receive standalone source pages in this correction.

## Evidence and context

- Primary owner: `raw/braintree/docs/reference/request/transaction/void/node-2026-09-16.md`
  - SHA-256: `4c2dc7bfd845476b74de0f13b30f4072833cb87fa822ee32fdf5c8027f62efcf`
  - `# Transaction: Void`, line 15 states `settlement pending` eligibility broadly for PayPal and qualifies authorization reversal with `if possible`.
- Supplemental conflict evidence: `raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16.md`
  - SHA-256: `3a0958ef16c50bacd409e48cd447695d41ff18cf6b1dcb1d7d45737e9669bf92`
  - `## Voids`, lines 109-115 says the `settlement pending` exception applies to PayPal transactions submitted as multiple partial settlements.
- Supplemental conflict evidence: `raw/braintree/docs/reference/general/statuses-2026-09-16.md`
  - SHA-256: `66260212baa543d60468cbc0f752f35e096cebf58edeaa47c44fbe37550ce0fa`
  - `## Transaction > ### Voided`, lines 93-97 limits the exception to "certain PayPal transactions" and routes to partial settlement.
- Current affected context is `wiki/sources/braintree/source-braintree-transaction-void-node.md` line 18 and `wiki/concepts/braintree-server-sdk.md` line 41. No standalone source owner was found for either supplemental raw.

The current primary-source statement remains useful as page-stated evidence, but without a visible warning it can be generalized into universal PayPal `settlement pending` eligibility. The smallest safe correction preserves the primary claim, adds the two supporting evidence routes, and narrows the concept route.

## Exact approved source-page snippets

In `wiki/sources/braintree/source-braintree-transaction-void-node.md`, replace the existing `raw_files` block with:

```yaml
raw_files:
  - "braintree/docs/reference/request/transaction/void/node-2026-09-16.md"
  - "braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16.md"
  - "braintree/docs/reference/general/statuses-2026-09-16.md"
```

Insert this warning immediately after the final `## Key takeaways` bullet and before `## Scope boundary`:

```markdown
> [!warning] Cross-document PayPal qualification
> The primary Node page states PayPal `settlement pending` eligibility broadly. [[raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16|Braintree's Control Panel article]] limits that case to PayPal multiple partial settlements, while [[raw/braintree/docs/reference/general/statuses-2026-09-16|the statuses reference]] says only "certain PayPal transactions." Do not infer that every PayPal transaction in `settlement pending` can be voided.
```

Replace the current `## Raw Sources` list with:

```markdown
- [[raw/braintree/docs/reference/request/transaction/void/node-2026-09-16|Braintree Node.js transaction-void reference]] - primary complete page covering eligibility, invocation, qualified authorization reversal, and result handling
- [[raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16|Braintree refunds, voids, and detached credits article]] - fully read supplemental conflict evidence; `## Voids`, lines 109-115 narrows PayPal `settlement pending` eligibility to multiple partial settlements
- [[raw/braintree/docs/reference/general/statuses-2026-09-16|Braintree statuses reference]] - fully read supplemental conflict evidence; `## Transaction > ### Voided`, lines 93-97 limits eligibility to certain PayPal transactions
```

## Exact approved concept-route replacement

In `wiki/concepts/braintree-server-sdk.md`, replace the existing transaction-void route with exactly:

```markdown
- [[source-braintree-transaction-void-node]] - Node.js `transaction.void()` reference for `authorized` and `submitted for settlement` transactions, the cross-document warning that only certain PayPal `settlement pending` transactions are eligible (identified elsewhere as multiple partial settlements), and the if-possible authorization-reversal effect
```

## Scope decision

No other source prose, concept prose, catalog entry, company page, log entry, raw file, or campaign job needs semantic replay for this bounded correction. Do not create standalone source pages for the two supplemental raws as part of this correction.

The coordinator applied these exact independently approved snippets. Initial
worker candidate and review remain immutable historical evidence; the canonical
Void source differs only by this explicitly reviewed post-audit correction.
