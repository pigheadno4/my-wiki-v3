# Rule: GitHub evidence supplements

> Read `rules/github-repos.md` and the repository's strategy rule first. This rule applies before every supplement collection.

Use a supplement only when an approved query needs specific text source excluded from an accepted bounded snapshot. A supplement is tied to one existing repository SHA and never modifies or replaces its snapshot.

```bash
python3 scripts/collect_github_repos.py supplement --repo <owner/repo> --sha <full-sha> --path <repo-relative-path>
```

Before collection, confirm the repository, exact accepted SHA, requested paths, and query need. Collect only reviewed UTF-8 text paths. Apply the same path safety, size, secret, hash, and immutable-publication protections as snapshots. Do not use supplements to bypass a capsule budget or silently broaden future collection policy.

Supplements live under:

```text
raw/github/<company>/<repo>/supplements/
```

When a supplement changes required reading for an existing work item, publish one canonical evidence attachment under:

```text
tracking/github/repos/<company>/<repo>/evidence-attachments/<work-item-id>/
```

Link the attachment through `evidence_attachments`. Approval and ingest must revalidate every linked attachment and read its manifest and source files in full, one by one. A missing, unlinked, unsafe, or modified attachment blocks lifecycle progress.
