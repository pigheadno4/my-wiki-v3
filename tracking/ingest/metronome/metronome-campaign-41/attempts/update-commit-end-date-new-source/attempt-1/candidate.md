---
title: "Metronome API Reference: Update the Commit End Date"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/update-the-commit-end-date"
raw_files:
  - "metronome/api-reference/credits-and-commits/update-the-commit-end-date-2026-07-13.md"
tags: [metronome, credits-and-commits, prepaid-commits, api]
---

## Overview

This OpenAPI page documents Metronome's bearer-authenticated `POST /v1/contracts/customerCommits/updateEndDate` operation for shortening an existing prepaid commit. It is the targeted evidence for ending that commit's access or invoicing earlier than originally scheduled, not for extending a commit or changing a credit.

## Key takeaways

- The operation only supports prepaid commits and moves an end boundary earlier; it cannot extend the commit.
- It can shorten the exclusive access cutoff, after which the commit can no longer be drawn down, and/or the exclusive invoicing cutoff. An omitted cutoff is not updated.
- Metronome directs extensions and other broader changes to the separate edit-commit endpoint.

## Important boundaries

> [!warning] Shortening only, on a prepaid commit
> Do not use this operation to extend a commit, mutate a credit, or update the enclosing contract's end date. For an extension or other comprehensive commit edit, follow the separate [[source-metronome-api-reference-credits-and-commits-edit-a-commit|edit-commit authority]].

## Verified raw locators

- Use `paths./v1/contracts/customerCommits/updateEndDate.post` together with the root `security` declaration for the method, path, bearer authentication, purpose, and request-body route.
- Use `components.schemas.UpdateCommitEndDatePayload` for the customer and commit identifiers and the independent access and invoice cutoff semantics.
- Use `paths./v1/contracts/customerCommits/updateEndDate.post.responses`, `components.schemas.Id`, `components.schemas.Error`, and `components.responses.NotFound` for the success and error response inventory.

## Related

- Company: [[metronome]]
- Concept: [[metronome-credits-and-commits]]
- Related operation: [[source-metronome-api-reference-credits-and-commits-edit-a-commit]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/update-the-commit-end-date-2026-07-13|Update the commit end date]] — complete collected OpenAPI page for prepaid-commit end-date shortening
