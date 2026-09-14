---
title: "List commits"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/list-commits"
raw_files:
  - "metronome/api-reference/credits-and-commits/list-commits-2026-08-28.md"
tags: [metronome, api-reference, credits-and-commits, customer-commits]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contracts/customerCommits/list`, which retrieves a customer's prepaid and postpaid commit agreements. It is the evidence route for selecting commit records and locating optional ledger and current-balance views; exact request and returned Commit schemas remain in the immutable raw snapshot.

## Query-critical routes

- Within a supplied JSON object, `customer_id` is the only required property. The enclosing OpenAPI `requestBody` is not marked required. Use the raw request schema for the optional commit, access-type, date, contract/archive-scope, ledger, balance and pagination controls.
- `include_contract_commits` expands the result beyond customer-level commits, and `include_archived` includes archived commits and commits from archived contracts. Optional ledger and balance expansion is documented as potentially slower.
- The success response contains a `data` array of `Commit` objects plus a nullable `next_page` cursor. Use the raw `Commit` component for identity, type, schedules, applicability, ledger, balance and other returned details rather than treating this entry as a schema inventory.

## Interpretation warning

> [!warning] Balance and ledger views are not interchangeable
> The ledger is an ordered list of events that affect a commit's balance. The calculated balance represents value accessible at the current moment: expired and upcoming segments contribute zero, excessive negative manual entries cannot reduce the calculated balance below zero, and future-dated manual entries on active segments are included. Consult the exact raw components before reconciling ledger arithmetic with the returned balance.

## Raw-detail locators

- Operation identity, bearer security and request controls: OpenAPI `paths./v1/contracts/customerCommits/list.post`, especially `requestBody.content.application/json.schema`.
- Response envelope and cursor placement: `paths./v1/contracts/customerCommits/list.post.responses.200.content.application/json.schema`.
- Returned commit details: `components.schemas.Commit`, with schedules under `ScheduleDuration` and `SchedulePointInTime`.
- Optional ledger and current-balance interpretation: `components.schemas.CommitLedger`, its referenced entry schemas, and `BalanceForCommitsAndCredits`.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/list-commits-2026-08-28|2026-08-28 snapshot - customer commit-list purpose, request controls, response route, ledger events and current-balance semantics]]
