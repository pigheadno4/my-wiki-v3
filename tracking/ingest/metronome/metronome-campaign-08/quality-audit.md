# Metronome Campaign 08 — Fixed Three-Page Query-Quality Audit

## Verdict

**PASS — 3/3 pages and 9/9 future-query tests passed.** No material partial, factual conflict, missing deep-dive route, or reciprocal-citation defect was found. The audit therefore stops at the immutable three-page sample; campaign-wide expansion is not required.

## Immutable scope

The approved Campaign 08 manifest fixes these audit jobs:

| Audit role | Job | Approved attempt | Raw SHA-256 |
| --- | --- | ---: | --- |
| Standard page | `manage-product-access` | 1 | `42bee2588c3e27fc0e984e047bb87578da11180a3cc9eeaf3b9dcf49907ce1a1` |
| Long/schema-heavy page | `get-remaining-balance` | 1 | `2f427835858daeeb9f71ff4ce25b53a08d0b62ea9d2dc3edba5cf6f182351bae` |
| Ordinary sample | `spend-trackers` | 1 | `8327257a20bcb8b0989cd2024d03e5a9bc1e47136d10416b44c9f38a553d47eb` |

Each raw page and canonical source page was read in full. For each job, the canonical source is byte-identical to the approved candidate, the candidate is byte-identical to the receipt's `source_page`, the raw file path and SHA-256 match the campaign record and disk, and the canonical URL and path-qualified Raw Sources link are exact.

## Mechanical and catalog checks

| Check | Result |
| --- | --- |
| Approved candidate → canonical source byte equality | PASS, 3/3 |
| Candidate → receipt `source_page` equality | PASS, 3/3 |
| Raw path and SHA-256 | PASS, 3/3 |
| Canonical URL and path-qualified raw backlink | PASS, 3/3 |
| Metronome company source catalog | PASS, 3/3 source entries present |
| Metronome provider source catalog | PASS, 3/3 source entries present |
| Required fact-bearing reciprocal concept citations | PASS, 5/5 present |
| Navigation-only reciprocal citation decision | PASS; `manage-product-access` adds no durable concept fact and correctly requires none |
| Catalog/count reconciliation | PASS; 60 source files, company `source_count: 60`, 60 company catalog entries, 60 provider catalog entries, and provider coverage 60 ingested / 165 pending |
| Targeted wiki validation | PASS, 9 relevant source/concept/company/log files |
| Metronome capsule validation | PASS, 225 raw / 60 sources / 165 pending |

The required reciprocal citations are:

- `get-remaining-balance` → `metronome-credits-and-commits`, `metronome-customers-and-contracts`, and `metronome-invoicing`.
- `spend-trackers` → `metronome-spend-trackers` and `metronome-credits-and-commits`.

Non-material validator note: invoking the generic wiki validator directly on `wiki/metronome-index.md` reports that the provider index has no YAML frontmatter. This is the existing plain-index format also used by other provider indexes, not a Campaign 08 catalog/link regression; the catalog counts and links reconcile and the provider-aware capsule validator passes. It does not change any query verdict or trigger audit expansion.

## Query tests

### 1. `manage-product-access` — standard page

| Test | Future query | Audit result | Verdict |
| --- | --- | --- | --- |
| Core retrieval | What does Metronome's Manage Product Access guide actually cover? | The source quickly returns the contract-defined-access framing and routes to provisioning, lifecycle transitions, trials, and notifications. It correctly identifies the page as navigation, not an implementation specification. | PASS |
| Boundary / unknown | Does this page prove a specific entitlement API, real-time SLA, notification-delivery mechanism, or that Metronome enforces access in the merchant product? | No. The Documentation boundaries section explicitly leaves entitlement fields, evaluation timing/mechanics, notification delivery, transition semantics, temporary-access configuration, and enforcement ownership unspecified. This prevents the raw page's marketing wording from becoming an unsupported guarantee. | PASS |
| Cross-link / deep-dive | Where should a future query go for implementation details? | The source links the Metronome company, four relevant concepts, two dedicated source summaries, and the exact raw snapshot. Company and provider catalogs both route back to this source. Because this navigation page contributes no durable implementation fact, the approved absence of reciprocal concept citations is correct. | PASS |

### 2. `get-remaining-balance` — long/schema-heavy page

| Test | Future query | Audit result | Verdict |
| --- | --- | --- | --- |
| Core retrieval | Which API gives a customer aggregate versus individual balances, and how should amounts and ledgers be interpreted? | The source distinguishes `/getNetBalance` from `listBalances`, explains signed per-ledger arithmetic, preserves fractional USD-cent semantics (`0.8` cents = `$0.008`), describes manual adjustments, and retains the complete credit, prepaid-commit, and postpaid-commit entry families. | PASS |
| Boundary / unknown | Does “real-time” guarantee freshness, can currencies be freely combined, and is an invoice-deduction timestamp the invoice or payment timestamp? | No. The source explicitly rejects an inferred SLA, cross-currency addition, undocumented cross-contract/hierarchy scope, and any mapping from the service-period-end effective timestamp to invoice creation, finalization, delivery, collection, or payment. It also records the unresolved duplicate descriptions for the two prepaid expiration types. | PASS |
| Cross-link / deep-dive | Can a future query trace balance, customer-scope, or invoice-timing claims back to evidence? | Yes. The source links the exact raw snapshot and the credits/commits, customers/contracts, and invoicing concepts. Each concept contains the relevant durable fact and a reciprocal citation to this source; company and provider catalogs also contain it. Exact schemas and table rows can be deep-dived through the raw backlink. | PASS |

### 3. `spend-trackers` — ordinary sample

| Test | Future query | Audit result | Verdict |
| --- | --- | --- | --- |
| Core retrieval | What does a spend tracker count, how can it affect discounts, and what can be retrieved? | The source returns Public Beta status, current `COMMIT_PURCHASE` scope, manual/threshold-recharge and discounted filters, reset-period accumulation, threshold-discount cap behavior, and `accumulated_spend` amount plus period boundaries. It separates contract-integrated behavior from merchant-owned checks. | PASS |
| Boundary / unknown | Is this a general usage or invoice metric, is it GA, and does Metronome automatically enforce a payment-gated manual-commit cap? | No. The source preserves Public Beta/access warnings, excludes usage-event, rated-usage, invoice-total, balance, alert, and payment-state interpretations, and says manual payment-gated enforcement is merchant-owned. It also leaves lifecycle inclusion, freshness, cap concurrency, units, reset timing, and the response-shaped curl request unresolved. | PASS |
| Cross-link / deep-dive | Can a future query reach feature-specific and credits/commit context plus raw evidence? | Yes. The source links the dedicated `metronome-spend-trackers` concept, credits/commits context, related sources, and the exact raw snapshot. Both fact-bearing concepts cite the source reciprocally, and the company/provider catalogs plus provider concept catalog are complete. | PASS |

## Expansion decision

No audit item is partial or failed. The fixed sample remains sufficient, and no all-page Campaign 08 quality-audit expansion is triggered.
