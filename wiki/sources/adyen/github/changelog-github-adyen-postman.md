---
title: "GitHub changelog: adyen/adyen-postman"
type: source
date_ingested: 2026-08-12
original_format: github-repo
raw_files:
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
