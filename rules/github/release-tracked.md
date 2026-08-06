# Rule: Release-tracked GitHub repositories

> Read `rules/github-repos.md` first. This rule applies when `version_strategy` is `monorepo-packages`, `semver-tags`, or `github-release`.

## Identity and policy

Always use package-qualified release identities such as `@paypal/paypal-js@10.0.3`. Never interpret `v10` without identifying the package. One repository may publish independently versioned packages at the same SHA.

An enabled release repository requires package-qualified version tracks and exactly one supported release capsule. Use `npm-tracked-source-v1` for a release-valid NPM workspace. Use `tagged-tree-v1` when one semantic Git tag maps to one package release but the repository does not expose a release-valid NPM workspace.

The tagged adapter does not run package managers or builds and does not fabricate a package manifest. Missing implementation needed by a later approved query must use a supplement.

For `future = "all-stable"`, select every stable release newer than the highest retained version. Do not silently backfill older gaps; use an exact release request or reviewed backfill policy.

## Evidence and commands

Each package release links to one exact-SHA snapshot and has its own immutable record:

```text
raw/github/<company>/<repo>/releases/<package-slug>/<version>/<collection-date>/
+-- manifest.json
+-- release-notes.md
```

Package comparisons live at:

```text
tracking/github/repos/<company>/<repo>/comparisons/<package-slug>/<from>--<to>/
```

Use:

```bash
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --release <package@version>
python3 scripts/collect_github_repos.py compare --repo <owner/repo> --from <package@version> --to <package@version>
```

`compare` writes an ad hoc review packet beside the comparison. It does not create or advance a work item.

## Collection procedure

1. Discover configured releases and recheck retained tag SHAs and release-note hashes.
2. Group releases sharing one SHA into one work item with separate `package_changes`.
3. Fetch notes and resolve the bounded capsule before publishing.
4. Publish or reuse the exact-SHA snapshot and immutable release records.
5. Compare each release with its prior selected package release.
6. Build the review packet and stop at `awaiting_approval`.

Changed release notes create a dated immutable revision. Exact note matches reuse accepted evidence.

## Ingest output

Keep package sections and major-version subsections where evidence exists. The changelog maintains separate package timelines and groups releases sharing a SHA as one repository change set. Every entry uses package-qualified from/to identities and links the release record, comparison, snapshot, and exact raw files.
