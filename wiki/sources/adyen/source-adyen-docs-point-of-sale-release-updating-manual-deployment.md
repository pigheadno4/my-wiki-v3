---
title: "Adyen Docs: Manually schedule terminal software updates"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/release-updating/manual-deployment"
raw_files:
  - "adyen/docs/point-of-sale/release-updating/manual-deployment/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, terminal-software, release-updates]
---

## Overview

Adyen's 2026-09-15 documentation snapshot explains how to schedule a terminal-software rollout in Customer Area when the terminals use the manual update strategy. The flow selects terminal ranges and models, an LTS release, an optional pilot, batches, and dates; Adyen reviews the submitted plan before the scheduled update. This is a fleet software procedure, not Android-app deployment or proof that any device has installed a release. [[adyen]] · [[adyen-terminal-management]]

## Key takeaways

- Customer Area roles differ by action: Merchant POS Terminal Management, Support, or View is listed for viewing earlier schedules; Merchant POS Terminal Management Admin is listed for scheduling a new update. Only Long Term Support (LTS) software versions can be manually scheduled. The guide says to read release notes first and recommends the latest LTS; that latest-version choice is advice, not an eligibility rule.
- In **Devices > Terminal software > Schedule update**, select range, LTS software version, and models. All terminal ranges are selected by default, so check the target before submitting. An optional pilot can test up to 20 terminals before fleet rollout. Optimized batching creates three batches, up to 10%, up to 30%, then the remainder, based on criteria such as activity, model, or country/region; alternatively create batches manually. Manual list upload allows up to 1,000 comma-separated terminal IDs per selection. Download CSV to review batch contents.
- Select a date for each batch. Adyen recommends at least seven days between batches for monitoring, says it needs two business days to approve schedule requests, and says updates occur at the restart hour (6:00 AM by default). A submitted plan awaits Adyen review and may require changes; the selected day is not proof of an approved plan or completed device updates.
- The **Default versions** tab changes the software version installed when a newly boarded terminal of a chosen model boards. It does not schedule an update for already boarded terminals, and it does not override software-version settings at lower merchant or store levels.
- The **Updates** view separates plan validation from terminal execution. Validation includes To be reviewed, Approved, Cancelled, and Rejected; hover on Rejected for a reason. Per-terminal deployment status includes Successful, Pending, Failed, and Cancelled. Pending means scheduled but not started, most likely because the device is offline or off; Failed means it could not complete. The UI offers cancel update, cancel pending updates, and reschedule failed updates. Do not equate plan approval with an installed update.

## Detail locators

- **Eligibility and sequence:** raw `Requirements` (lines 21–29) contains Customer Area roles, LTS restriction, and release-note advice. `How it works` (31–42) has the selection, submission, Adyen review, and rollout sequence. The guide links to a test Customer Area URL but does not establish production eligibility or the currently offered versions.
- **Targets and batches:** `1. Select the software version` (44–58), `2. Select the update strategy` (60–76), and `3. Select batches` (78–98) give range/model selection, optional 20-terminal pilot, optimized percentages, manual terminal-ID selection, and CSV review.
- **Timing:** `4. Select the date` (100–111) distinguishes seven-day spacing advice, two-business-day approval lead time, restart-hour timing, and Submit.
- **New versus existing terminals:** `Change the default software version` (113–129) limits default-version changes to newly boarded terminals and preserves lower-level overrides.
- **Validation and recovery:** `Monitor the status of your update plan` (131–163) lists separate validation and per-terminal execution statuses. `Update your plan` (165–175) identifies cancellation and failed-update rescheduling controls.

## Related

- [[adyen-terminal-management]] — terminal fleet software and administration route
- [[adyen-android-terminals]] — neighboring on-terminal Android app deployment, a separate workflow
- [[adyen-terminal-api]] — in-person payment messages, separate from software scheduling

## Related raw API references

The linked release-strategy, LTS, release-note, restart-hour, role, assignment, and troubleshooting pages were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/release-updating/manual-deployment/2026-09-15|Adyen manual terminal software deployment guide, fetched 2026-09-15]]
