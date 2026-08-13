# PayPal Messages Braintree Policy Boundary Design

**Date:** 2026-08-13
**Status:** Approved design, pending written-spec review
**Repositories:** `paypal/paypal-messages-ios`, `paypal/paypal-messages-android`

## Goal

Preserve and ingest the point at which PayPal's mobile Messages repository documentation changed from PayPal/PPCP-oriented integration guidance to an explicit Braintree-only merchant requirement.

The result must answer both questions without conflating them:

1. Which tagged package releases have been collected and what did their READMEs say?
2. When did the default-branch documentation first state that a Braintree account and Braintree SDK are required?

## Confirmed Boundary

The restriction is not attached to a semantic package release.

| Platform | Released before evidence | First default-branch commit with disclaimer | Commit date | Tagged release containing disclaimer |
| --- | --- | --- | --- | --- |
| iOS | `paypal-messages-ios@1.2.0`, SHA `432d6b832714b2615106c3f2a748ac61654d8bbd` | `fdd18681f486a3b2f1c60e3c47f8669f55a73a96` | 2026-06-01 | None |
| Android | `paypal-messages-android@1.3.0`, SHA `f1aa138cc6822cc11d68ac4bfdee3cf183aedbc2` | merge commit `0424354a5fa0ab697275186fe101d105838ac03e` | 2026-05-29 | None |

The iOS disclaimer commit is directly based on the retained `1.2.0` SHA. The Android disclaimer was merged onto `develop` after untagged commit `1d2238c9e5ec3564ad5d8060c474e008ab7bf779`; Android `v1.3.0` is on a separate release branch. The comparison must therefore distinguish immediate default-branch ancestry from latest tagged-release context.

The new README wording says the component is intended only for the Braintree SDK, requires a Braintree account and Braintree SDK integration, and does not support PPCP SDK integrations.

## Interpretation Boundary

This is a documentation-policy and merchant-eligibility change, not a proven SDK-code compatibility change.

- Do not attribute the Braintree requirement to iOS `1.2.0` or Android `1.3.0`.
- Do not create synthetic package versions for the untagged commits.
- Do not claim that code at the tagged releases technically stopped accepting a PayPal client ID.
- Treat the newer repository guidance as the current integration-policy signal for merchant recommendations.
- Keep the statement version-qualified and identify the untagged exact SHA whenever answering historical questions.

## Approaches Considered

### Exact-ref boundary collection

Reuse each repository's retained tagged snapshot as released context, collect the first untagged disclaimer commit with the existing repository capsule, and create an exact-ref comparison. This is selected because it preserves enough source to investigate whether the documentation change corresponds to code changes while avoiding unnecessary historical releases.

### Full release ladder

Collect every stable release from `1.0.0` forward. This would preserve broader history but would not locate the Braintree boundary because no tagged release contains the disclaimer. It is disproportionate to this query.

### README-only manual collection

Store the two README versions without repository snapshot metadata. This is smaller but bypasses the managed GitHub evidence lifecycle and weakens exact-SHA provenance. It is rejected.

## Collection Design

Add a narrow exact-ref boundary mode for release-tracked repositories. It must reuse the reviewed `tagged-tree-v1` capsule but produce commit-qualified evidence rather than a package release.

Conceptual command shape:

```bash
python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-ios \
  --from 432d6b832714b2615106c3f2a748ac61654d8bbd \
  --to fdd18681f486a3b2f1c60e3c47f8669f55a73a96

python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-android \
  --from 1d2238c9e5ec3564ad5d8060c474e008ab7bf779 \
  --to 0424354a5fa0ab697275186fe101d105838ac03e
```

The exact command name is implementation detail, but the behavior is fixed:

1. Resolve both supplied full SHAs and verify that `from` is an ancestor of `to`.
2. Reuse an accepted snapshot when a SHA is already retained.
3. Publish immutable snapshots for unretained SHAs using the repository's existing capsule and safety budgets.
4. Write a commit-qualified comparison and review packet with `ref_changes`, not `package_changes`.
5. Create no release manifest or release notes for either untagged commit.
6. Stop each repository work item at `awaiting_approval`.
7. Preserve normal monthly `semver-tags` discovery and `future = "all-stable"` behavior.

For iOS, `from` reuses the retained `1.2.0` snapshot. For Android, collect the immediate pre-disclaimer `1d2238c` snapshot as the direct comparison base. Keep retained `1.3.0` as separate released context and explicitly report that its README also lacks the disclaimer.

## Evidence Scope

Use the existing full public-source capsules for both exact refs. Do not weaken the collection to README-only evidence.

The packet must highlight:

- `README.md` as the selected policy change;
- `CHANGELOG.md` to establish that no package release records the change;
- exact commit metadata and ancestry;
- all other retained file differences between the selected SHAs;
- whether any implementation file changed together with the disclaimer.

If files other than README changed in the Android direct boundary, every retained change must receive a disposition before approval. The presence of unrelated changes does not permit the packet to label them as part of the Braintree requirement.

## Serial Ingest Design

Collection may prepare both repositories, but ingest remains one work item at a time.

Recommended order:

1. iOS boundary delta, because its direct base is the accepted `1.2.0` snapshot and the change is a single README commit.
2. Android boundary delta, after reviewing its direct untagged base and merge topology.
3. Update the paired analysis only after both repository histories have been ingested.

For each repository:

- read the cumulative source page and changelog first;
- read the packet, manifests, comparison, and every required path in full;
- append an **Unreleased documentation-policy change** entry to the repository changelog;
- update the cumulative source page without erasing tagged-version behavior;
- preserve the difference between merchant-policy guidance and technical source behavior.

After both serial ingests, update `analysis-paypal-messages-ios-vs-android.md` with a shared policy timeline. It must state that the Braintree-only requirement first appears in untagged default-branch documentation and is not yet tied to a collected package release.

## Query Behavior

Questions such as "Can a PayPal-only merchant use PayPal Messages mobile?" must search:

1. the cumulative source page;
2. the repository changelog, including unreleased entries;
3. the exact untagged README snapshot; and
4. the paired mobile analysis when cross-platform guidance is requested.

The answer should recommend the Braintree path based on current repository policy while explaining that the latest tagged READMEs predate that policy change.

## Failure and Approval Boundaries

- A non-ancestor `from`/`to` pair is rejected rather than compared as a direct boundary.
- Missing refs, unsafe paths, secret findings, hash failures, budget overflow, or unclassified retained changes block approval.
- Existing accepted snapshots and release records remain immutable.
- Exact-ref collection does not alter latest-release status or monthly release scheduling.
- Collection never edits wiki pages or begins ingest automatically.

## Validation

Add focused tests proving:

- exact-ref collection is permitted for a release-tracked repository without changing its release strategy;
- full SHA and ancestry validation are mandatory;
- an accepted `from` snapshot is reused;
- an unretained `from` snapshot can be published for direct-boundary evidence;
- work items use `ref_changes` only and create no release records;
- status and collection indexes preserve the repository's latest package release;
- collection stops at `awaiting_approval`.

Run focused tests, the full unittest suite, `scripts/validate_github_collection.py`, and `git diff --check` before committing implementation.

## Success Criteria

- The iOS exact boundary `432d6b8 -> fdd1868` is preserved with immutable before/after evidence.
- The Android direct boundary `1d2238c -> 0424354` is preserved, with `v1.3.0` retained as separate released context.
- Neither untagged commit is represented as a package release.
- Both packets identify the README policy change and classify every other retained change.
- Each work item stops at `awaiting_approval` before serial ingest.
- Final wiki guidance clearly says the Braintree restriction is an unreleased documentation-policy change, not a versioned SDK feature.
