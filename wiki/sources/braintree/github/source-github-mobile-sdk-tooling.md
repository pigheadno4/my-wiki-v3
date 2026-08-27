---
title: "GitHub: braintree/mobile-sdk-tooling"
type: source
date_ingested: 2026-08-27
original_format: github-repo
raw_files:
  - "github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/manifest.json"
tags: [braintree, mobile-sdk, developer-tooling, github-actions, code-review, slack, github-repository]
---

## Overview

`braintree/mobile-sdk-tooling` contains shared workflows and cross-platform operational tooling for Braintree mobile SDK repositories. The retained baseline is default branch `main` at exact commit `a3b0ffe7931cde179f8b0dfdd5162979adf81683`, committed on 2026-07-22. The immutable capsule contains the repository README and the `PR Review Digest` GitHub Actions workflow.

Repository: <https://github.com/braintree/mobile-sdk-tooling>

## Evidence Boundary

- This repository is engineering-operations evidence. It does not implement a mobile SDK, checkout flow, payment method, merchant eligibility rule, tokenization path, or payment-processing behavior.
- The workflow describes how selected pull requests are surfaced for review. A digest entry, approval count, or clean merge state is not proof that a change is correct, released, or deployed.
- The retained snapshot does not include the organization secrets, Actions variables, GitHub App installation, Slack workflow, or runtime logs. Their configured values and production behavior remain external evidence gaps.
- The history is commit-qualified because the repository has no retained package release identity.

## Grounding Excerpts

> "Workflows and cross-platform tooling for Braintree Mobile SDK repositories"
>
> `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/README.md:2`

> `REPOS: ${{ vars.REPOS }}`
>
> `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/.github/workflows/pr-review-digest.yml:38`

> `owner: ${{ github.repository_owner }}`
>
> `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/.github/workflows/pr-review-digest.yml:26`

> `echo "Done. Posted $TOTAL regular PR(s) and $INNER_SOURCE_TOTAL inner source PR(s) to Slack."`
>
> `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/.github/workflows/pr-review-digest.yml:296`

## Schedule and Execution

The `PR Review Digest` workflow runs on `ubuntu-latest`, has a 15-minute timeout, supports manual dispatch, and schedules two weekday runs intended for 09:00 and 15:00 US Central time. The cron expressions are fixed to daylight time; comments require a manual one-hour adjustment when Central Standard Time begins.

The job creates an organization-scoped GitHub App token with `actions/create-github-app-token@v1`, then checks out this repository so the script can inspect its `CODEOWNERS` file. It reads the GitHub App ID and private key plus the Slack webhook from Actions secrets. The comma-separated repository list and optional open threshold come from Actions variables; the threshold defaults to 12 hours.

## Repository and Pull Request Selection

The script scans each configured repository with `gh pr list`, requesting at most 100 open pull requests. It skips drafts. It treats the `inner source` and `tech lead review required` labels case-insensitively:

- Inner-source pull requests awaiting tech-lead review are always hidden.
- Other inner-source pull requests appear only on Tuesdays and Thursdays.
- Regular pull requests can appear on every scheduled weekday run.

The repository list is configuration, not source-controlled inventory. If `REPOS` is empty, the workflow logs guidance and exits successfully without posting a digest.

## Review-State Reduction

The script fetches the full paginated review history for each candidate pull request and reduces it to each reviewer's latest decisive state: `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`. `COMMENTED` and `PENDING` reviews do not replace a prior decisive review.

When a `CODEOWNERS` file is found, only individual `@username` entries count; organization/team references are intentionally skipped. Only those owners' approvals and change requests then affect the digest. Without a discovered `CODEOWNERS` file, all reviewers count.

A pull request with a relevant outstanding change request is excluded when its latest commit is not newer than the request. The commit lookup is lazy to avoid GitHub GraphQL node limits. If that lookup fails, the script keeps the pull request visible instead of hiding it.

## Digest Criteria and Slack Output

A candidate is included when at least one of these conditions applies:

- It has fewer than two counted approvals.
- GitHub reports `mergeStateStatus` as `CLEAN`.
- It has at least two counted approvals but no activity for the configured threshold.

The digest groups entries by repository and includes pull request number, sanitized title, bare URL, author, age, reasons, labels, and counted approvers. Inner-source entries use a separate section. When no entry qualifies, the workflow posts an all-clear message. The final Slack Workflow webhook payload contains a single `message` field and is sent with `curl -sf`.

## Operational Limitations

- Daylight-saving changes require manual cron edits; the schedule can drift by one hour if that maintenance is missed.
- `gh pr list --limit 100` does not paginate beyond 100 open pull requests per repository, so larger backlogs can be omitted.
- The script relies on Ubuntu/GNU behavior, including `date -d` and `grep -P`; portability to macOS or non-GNU runners is not established.
- GitHub App repository installation and read permissions must cover every configured repository. Missing access can stop the strict shell script before Slack delivery.
- The CODEOWNERS extraction matches individual usernames only and does not resolve team membership, so team-only ownership can fall back to counting all reviewers.
- A clean merge state and two approvals are routing signals, not a complete release gate. Branch protection, required checks, security review, release automation, and deployment remain outside this workflow's evidence.

## Related

- [[changelog-github-mobile-sdk-tooling]] - commit-qualified repository history
- [[braintree]] - company and knowledge-status page
- [[source-github-braintree-android]] - independently versioned Android SDK implementation
- [[source-github-braintree-ios]] - independently versioned iOS SDK implementation

## Raw Sources

- Snapshot manifest: `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/manifest.json`
- Workflow: `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/.github/workflows/pr-review-digest.yml`
- README: `raw/github/braintree/mobile-sdk-tooling/snapshots/2026-08-27-a3b0ffe/files/README.md`
