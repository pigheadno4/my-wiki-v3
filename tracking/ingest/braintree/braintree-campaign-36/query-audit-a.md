# Braintree C36 fixed query audit A

- Analysis completed UTC: `2026-10-04T07:05:38Z`
- Coverage: `4/4` exact pages, `8/8` predetermined questions, `4/4` pinned raw SHA-256 values.
- Verdict: **PASS** (`8/8` question cells).
- Material failures: **none**.

## `articles-aib-af-reconciliation-lr` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:527` `[[payment-reconciliation-reporting]]` → `wiki/concepts/payment-reconciliation-reporting.md:117` `[[source-braintree-articles-aib-af-reconciliation-lr]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-reconciliation-lr.md:49` → `raw/braintree/articles/aib-af/reconciliation-lr-2026-09-16.md`. Pinned and actual SHA-256: `f7dcdaf4f09ea2f011b94a8eb7439ecf0bdb6308faa3e456b04232c52d5cfe64`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted AIB AF `Reconciliation (LR)` document. It covers AIB Merchant Statement Funding Totals and the Transaction Fee Report for Braintree AIB funded accounts, including net- and gross-settlement handling. It does not establish ordinary AIB AF reconciliation, AIB BF behavior, current independent bank authority, a general region, or deposit arrival. Only `Card Type Group` and `Region Relation` are explicitly EMEA-only (`raw:154-155`); the raw states no broader region/pricing eligibility.
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Compare Funding Totals with bank deposits (`raw:17-24`), then match Transfer ID and Transaction Disbursement Key, total settlement/fees/chargebacks, truncate rather than round, and proceed only after all disbursement-impacting items are present (`raw:72-89`). Sales/refunds and fees have net/gross qualifications (`raw:92-134`); schema fields are at `raw:137-175`; record/subtype meanings, including failed disbursement, are at `raw:178-207`. A report row or expected match is reconciliation evidence, not proof of receipt.

## `articles-aib-af-idempotency-lr` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:20` `[[braintree-at-most-once-processing]]` → `wiki/concepts/braintree-at-most-once-processing.md:20` `[[source-braintree-articles-aib-af-idempotency-lr]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-idempotency-lr.md:47` → `raw/braintree/articles/aib-af/idempotency-LR-2026-09-16.md`. Pinned and actual SHA-256: `caa238f3ce0fd20691ddff7ee8d741ddc1ef10bb8a558e9f2f855a039574bac7`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted AIB AF route with slug label `idempotency-LR`, documenting At-Most-Once Processing for a restricted/select audience. The body does not define AIB/AF/LR, identify a processor or region, state a pricing model, or prove current merchant enablement, SDK support, or execution. The limited-audience/share warning is explicit (`raw:14-15`).
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Merchant-supplied `ApiRequestKey` gives logical-intent idempotency, is mutually exclusive with transaction duplicate checking, and treats identical keys within 30 days as duplicates (`raw:20-35`). Same-details duplicates return in-progress error `915233` or the completed action's current state; changed details return `915232` (`raw:37-42`, `raw:178-184`). Supported families are listed at `raw:45-57`; action-specific matrices and retry qualifications are at `raw:59-175`. A new key is not a blanket-safe retry: safety depends on record/state evidence and may require investigation or Braintree intervention (`raw:73-87`, `raw:104-106`, `raw:120-122`, `raw:139-141`).

## `articles-aib-bf-chargebacks-retrievals-prearbs` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:528` `[[disputes]]` → `wiki/concepts/disputes.md:334` `[[source-braintree-articles-aib-bf-chargebacks-retrievals-prearbs]]` → `wiki/sources/braintree/source-braintree-articles-aib-bf-chargebacks-retrievals-prearbs.md:51` → `raw/braintree/articles/aib-bf/chargebacks-retrievals-prearbs-2026-09-16.md`. Pinned and actual SHA-256: `dbb0061f982e60f8740bd5aa2210cb2e6b500045800695ecbbff82a3a722f9ca`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted AIB BF article for **credit-card** chargebacks, retrievals, and pre-arbitrations; PayPal disputes are routed elsewhere (`raw:17-18`). It does not define AIB/BF, establish a region or pricing model, give fee amounts, provide independent current bank/card-network authority, or authorize transfer of AF/Wells terms.
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Notification recipients and Open/Won/Lost webhooks are at `raw:25-46`; current/legacy Control Panel actions, the API route, and the 12am account-time-zone reply-by cutoff are at `raw:49-85`. Expiry sends Accept and ends the evidence opportunity (`raw:77-79`). Chargeback payout debit, evidence decision, and outcome-independent fee are at `raw:90-113`; retrieval no-debit/no-processing-fee and fraud guidance at `raw:116-122`; pre-arb evidence/acceptance and fee at `raw:125-131`; statuses at `raw:134-143`; reports at `raw:146-163`. The BF Financial Impact Report is specifically used with statements for reconciliation (`raw:161-163`).

## `articles-aib-af-chargebacks-retrievals-prearbs` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:528` `[[disputes]]` → `wiki/concepts/disputes.md:332` `[[source-braintree-articles-aib-af-chargebacks-retrievals-prearbs]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-chargebacks-retrievals-prearbs.md:50` → `raw/braintree/articles/aib-af/chargebacks-retrievals-prearbs-2026-09-16.md`. Pinned and actual SHA-256: `4580b2fb2ff53a6d53ec9cf55e604539cbadc3a460ce4514da2cf7bdd0beabc9`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted AIB AF article for **credit-card** chargebacks, retrievals, and pre-arbitrations; PayPal disputes are routed elsewhere (`raw:17-18`). It identifies no region or pricing plan and states no numeric fee. It is not AIB BF behavior, independent current bank/card-network policy, a merchant-specific agreement, or a universal Braintree price schedule.
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Notification permissions and webhooks are at `raw:23-44`; rolling/legacy Control Panel actions, stated API route, and the reply-by cutoff are at `raw:47-83`. At 12am in the account time zone, the evidence window closes; expiry sends Accept and forfeits the dispute right (`raw:75-77`). Chargeback debit/outcome/fee and evidence are at `raw:88-111`; retrieval distinctions and fraud guidance at `raw:114-120`; pre-arb evidence/acceptance and fee at `raw:123-129`; statuses, including qualified 2–3-business-day return wording, at `raw:132-140`; the Dispute Report at `raw:143-152`. Unlike BF's Financial Impact Report, AF's Dispute Report is expressly **not** for reconciliation (`raw:152`).

## Shared gap sweep / extra reads

- Read in full: root index, Braintree index, the three routed concepts, all four selected source pages, and all four selected raw pages.
- Focused raw filename sweep found ordinary AIB AF/BF reconciliation, the general At-Most-Once guide, and processor/region-specific dispute variants. None was needed as factual authority for these page-local questions; importing them would blur the pinned LR/AF/BF scope. Selected sources contain no `## Related raw API references` requiring an additional read.
- Linked guides/API/support pages in the selected raws remain navigation only because no broader cross-page assertion was needed. No historical-version full read was performed.
- Material distinction preserved once: AF's Dispute Report is non-reconciliation (`AF raw:152`), while BF's Financial Impact Report is a statement-reconciliation input (`BF raw:161-163`).

- Handoff UTC: `2026-10-04T07:06:05Z`
