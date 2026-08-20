# Metronome Campaign 17 query-quality audit

- Audit date: 2026-08-20
- Manifest: `tracking/ingest/metronome/metronome-campaign-17/manifest.json`
- Audited pages: fixed three-page sample
- `overall_decision`: **pass**
- `expansion_triggered`: **false**
- `expansion_completed`: **not applicable**
- `expansion_required`: **false**
- `closure_approved`: **true**
- Material open defects: **none**

The immutable sample covered the standard page `make-a-pricing-change`, the
longest and high-risk page `revenue-recognition-examples`, and the ordinary
page `edit-or-override-a-contract`. All nine fixed queries passed, so the
campaign-wide expansion rule was not triggered.

## Integrity, backlinks, and reciprocity

| Job | Raw SHA-256 | Exact raw backlink | Fact-bearing concept reciprocity |
| --- | --- | --- | --- |
| `make-a-pricing-change` | **pass** - `167df7747dca0372537d7885442ce30cb798396f367f58cf76f19362d7c284b0` equals the manifest | **pass** - exact nested raw at source line 57 | **pass** - products/rate cards, packages/aliases, and customers/contracts are bidirectional exactly once |
| `edit-or-override-a-contract` | **pass** - `ab6257a40cb9857cb21b26e7611b817d26bf95f5c71d04c936d45ec64ac20384` equals the manifest | **pass** - exact nested raw at source line 57 | **pass** - products/rate cards and customers/contracts are bidirectional exactly once |
| `data-export-cookbook` | **pass** - `ff238507fbef397ef328228d6ea56fca4ce04d7ee203743aa47556ee175963d8` equals the manifest | **pass** - exact nested raw at source line 87 | **pass** - reporting/analytics carries the approved durable facts and reciprocal source link |
| `edit-contract` | **pass** - `c15529eca1213a59666840f54d1648a2292360cdaf6ea6ec4428461b378b5786` equals the manifest | **pass** - exact nested raw at source line 93 | **pass** - customers/contracts, credits/commits, and invoicing are bidirectional exactly once |
| `revenue-recognition-examples` | **pass** - `c2861f1e4d056b07a1105b2ca5443826a9c968f77831f6d08831fb3481c022a2` equals the manifest | **pass** - exact nested raw at source line 97 | **pass** - reporting/analytics, credits/commits, invoicing, and payment reconciliation/reporting are bidirectional exactly once |

Other `Related` concept links remain navigational unless the campaign added a
durable fact to that concept. They do not create a false reciprocal-link
requirement.

## Query results

### `make-a-pricing-change`

1. **Retrieval - pass.** "How can a merchant launch pricing changes for all
   customers, a cohort of new customers, or one customer?" The source preserves
   the three scopes: rate-card `addRates`, package and alias provisioning, and
   contract re-provisioning or direct editing (lines 14-22 and 47).
2. **Boundary/contradiction - pass.** "Does the worked `addRates` payload really
   schedule a one-year price increase, and does an alias update migrate existing
   contracts?" The source flags the identical `starting_at` values and differing
   regions (line 29), then limits the later alias to future provisioning while
   existing customers retain their original package pricing (lines 39-43).
3. **Raw deep dive - pass.** The path-qualified backlink at line 57 opens the
   exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

### `revenue-recognition-examples`

1. **Retrieval - pass.** "What billing-export examples does CloudNet provide?"
   The source covers on-demand usage and free credits, prepaid purchase and
   drawdown, expiration and overage, and postpaid commitment true-up (lines
   14-18 and 38-74).
2. **Boundary/contradiction - pass.** "Can these tables be treated as executable
   schema or authoritative accounting outputs?" The source preserves the field
   name drift, reused IDs, customer/contract mismatch, CloudStorage amount
   conflict, prepaid arithmetic conflicts, month-11 amount conflicts, reversed
   postpaid invoice labels, double-count boundary, and non-accounting-policy
   limitation (lines 20-35, 42-80, and 83-87).
3. **Raw deep dive - pass.** The path-qualified backlink at line 97 opens the
   exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

### `edit-or-override-a-contract`

1. **Retrieval - pass.** "Which contract override types, selectors, and priority
   rules are documented?" The source preserves multiplier, overwrite, and
   tiered models; entitlement behavior; AND-within/OR-across specifiers;
   dimensional and presentation targeting; and non-stacking precedence (lines
   18-41).
2. **Boundary/contradiction - pass.** "Does this page explain editing an existing
   contract, and may dimensional selectors use only a subset of keys?" The
   source flags the all-`POST /v1/contracts/create` evidence boundary (lines 14
   and 45) and preserves the unresolved all-values-versus-subset wording (lines
   30-35).
3. **Raw deep dive - pass.** The path-qualified backlink at line 57 opens the
   exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

## Mechanical campaign-wide checks

Each of the five source wikilinks occurs exactly once in both
`wiki/companies/metronome.md` and `wiki/metronome-index.md`. The required
coverage values are consistent:

- Company frontmatter: `source_count: 107`.
- Company knowledge status: `107` ingested / `124` raw without summaries.
- Provider index coverage: `107` ingested / `124` raw without summaries.
- All five jobs are approved; no job remains queued, running, or reviewing.
- Coordinator repairs: **0**.

## Final totals and closure

- Audited pages: **3 / 3 fixed sample**
- Queries: **9 pass / 0 partial / 0 fail**
- Page outcomes: **3 pass / 0 partial / 0 fail**
- Campaign-wide raw hashes: **5 pass / 0 fail**
- Material open defects: **0**
- `overall_decision`: **pass**
- `expansion_required`: **false**
- `closure_approved`: **true**
