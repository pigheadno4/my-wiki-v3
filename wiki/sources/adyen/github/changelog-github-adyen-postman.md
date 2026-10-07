---
title: "GitHub changelog: adyen/adyen-postman"
type: source
date_ingested: 2026-08-12
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/manifest.json"
  - "github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json"
tags: [adyen, postman, checkout-api, terminal-api, changelog, github-repository]
---

## Overview

Commit-qualified history for `adyen/adyen-postman`. Durable API-example knowledge belongs in [[source-github-adyen-postman]]; this page records when each immutable repository baseline entered the wiki.

## `default-branch@ecb2907` (2026-08-04)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `main` | Initial baseline | `default-branch@ecb2907` | `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7` | Full |

**Important findings:** The baseline contains generated Checkout v72, Recurring v68, BIN Lookup v54, and Test Card v1 collections plus an independently maintained, unversioned Terminal API collection. Checkout examples cover online payment, Sessions, modifications, stored methods, links, orders, utilities, and recurring models. Terminal examples cover 82 payment and terminal-interaction requests.

**Developer or merchant impact:** Treat examples as exact-commit payload guidance, not evidence of account enablement or current eligibility. Prefer Checkout recurring endpoints when possible because the retained Recurring API collection identifies itself as legacy. Keep Terminal API, Checkout API, and Management API responsibilities separate.

**Migration action:** Initial baseline; no prior retained snapshot exists. Configure variables in a private environment, use the correct test or live endpoints, and verify any production implementation against current Adyen API documentation and actual responses.

**Updated source sections:** collection generation and setup; Checkout API v72; tokenization and recurring operations; BIN lookup and test cards; Terminal API.

**Evidence boundary:** This commit is the first retained baseline, so no repository diff is available. The versioned collection filenames identify API versions, while the Terminal collection is qualified only by the repository commit.

**Evidence:**

- Packet: `tracking/github/repos/adyen/adyen-postman/ingest-packets/github-ab2d0a488d97d9590b4c/packet.md`
- Snapshot: `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json`
- Source synthesis: [[source-github-adyen-postman]]

## `default-branch@ecb2907` to `default-branch@78874d7` (2026-09-28)

- **Identity:** `main`, SHA `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7` to `78874d7b10d8cb438ed15eb01dd732c8d86540a7`; collected and ingested 2026-10-07. Commit-qualified evidence, not a semantic release.
- **Mode/read:** user-approved delta overriding the path-based full recommendation, with a one-time focused-reading exception. Complete stored-method/donation sections in both snapshots, full comparison and cumulative source/changelog read; inventories, unaffected request structures and ten unchanged files verified mechanically. Full historical knowledge preserved.
- **Changes:** Checkout v72 stored-method create/list/delete descriptions now name the `API tokenise payment details` credential role; no new enforcement date established. Two donation-account request examples removed, reducing Checkout requests 60 to 58. The existing campaign donation request remains unchanged; no endpoint deprecation inferred.
- **Unchanged:** Terminal API and all other retained files; existing request structures outside descriptions. No API-version upgrade or new payment flow established.
- **Impact:** verify stored-method credential roles; use commit-qualified donation evidence and do not interpret example removal as product withdrawal. No live API/payment test performed.
- **Updated sections:** additive source history, recurring-payments concept, company, provider index/log and root log. Historical count qualified, no factual contradiction or substantive cross-company comparison identified. Repository source count stays 14; package-release counts are unchanged.
- **Collection repair:** packet-file limit raised 30 to 40 with its old policy hash registered as historical. Scope and byte budgets unchanged; accepted raw evidence not rewritten.
- **Evidence:** [snapshot](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/manifest.json), [Checkout collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/files/postman/CheckoutService-v72.json), [prior Checkout collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json), [comparison record](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/comparison.json), [comparison](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/comparison.md), [patch](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/diff.patch), [packet](../../../../tracking/github/repos/adyen/adyen-postman/ingest-packets/github-1b49bd6b9d94ec92f190/packet.md).
