# React Stripe.js Collection Design

## Goal

Make `stripe/react-stripe-js` executable through the existing GitHub collection workflow, collect one current stable baseline, and stop at the review packet before wiki ingest.

## Registry Policy

- Keep the existing repository identity, company, weekly frequency, tier-1 priority, and release-driven strategy.
- Discover the current stable package major before editing the registry.
- Add one package-qualified version track for `@stripe/react-stripe-js`:
  - `backfill = "latest-stable"`
  - `future = "all-stable"`
  - `include_prerelease = false`
- Enable the row only after it has exactly one valid version track and one valid capsule.

## Source Capsule

Use the existing `npm-tracked-source-v1` adapter with:

- focus package `@stripe/react-stripe-js`;
- internal runtime dependency closure;
- bounded changed-path handling;
- required public roots for `src` and examples that exist in the selected release;
- normal repository context such as README, license, and package metadata;
- stories eligible for retention;
- tests and fixtures excluded; and
- conservative file-count and UTF-8 size budgets.

If a required root is absent or the capsule exceeds a budget, collection must stop for policy review. Do not silently broaden roots, exclusions, or budgets.

## Execution

1. Perform read-only release discovery and identify the latest stable package release and major.
2. Update only the `stripe/react-stripe-js` registry row.
3. Run focused registry tests and the offline GitHub collection validator.
4. Run backfill collection for `stripe/react-stripe-js`.
5. Review the generated snapshot, release record, comparison state, evidence gaps, unclassified paths, required-reading count, and recommendation.
6. Stop in `awaiting_approval`.

Collection must not approve the work item, call `next-ingest`, or edit wiki pages.

## Success Criteria

- Registry validation passes.
- Collection publishes an immutable exact-SHA snapshot and package-qualified release record.
- A canonical review packet is linked from one `awaiting_approval` work item.
- The packet has no unexplained identity or classification errors.
- Existing unrelated working-tree changes remain untouched.

