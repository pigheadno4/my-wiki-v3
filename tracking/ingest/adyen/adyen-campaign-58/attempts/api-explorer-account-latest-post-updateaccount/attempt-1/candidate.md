---
title: "Adyen Account API v6: POST /updateAccount"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount"
raw_files:
  - "adyen/api-explorer/Account/latest/post/updateAccount/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, payout-schedule]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /updateAccount` on the Account API v6 TEST server. It updates an account's description or payout schedule; the request table also documents optional bank-account coupling, payout-method coupling, metadata, and payout speed. The required `accountCode` identifies the account being updated, distinct from the account holder that owns the referenced bank account or payout method. The page does not separately specify request-body requiredness.

## Key takeaways

- `bankAccountUUID` couples the account to a bank account held by its account holder. Scheduled payouts in that bank account's currency go there; other currencies go to a matching bank account of the holder. `payoutMethodCode` couples a holder-held payout method for scheduled card payouts. Neither field is marked required.
- On metadata update, omitting existing key-value pairs **deletes** those pairs. The optional description has a 256-character limit and stated character set.
- If `payoutSchedule` is supplied, its nested `schedule` is marked required. `HOLD` prevents scheduled payouts but still permits manual payouts; `reason` is required when the schedule is `HOLD`. The optional `action` controls already-scheduled payout batches: `CLOSE` closes the existing batch, `UPDATE` reschedules it, and `NOTHING` (default) lets it proceed. `payoutSpeed` permits `STANDARD` (default) or `SAME_DAY`; the page does not establish eligibility or timing for same-day execution.
- A 200 says the request succeeded, whereas a 202 says it was accepted but processing has not completed. The response includes required `accountCode` and optional updated fields, `invalidFields`, `pspReference`, and `resultCode`; `invalidFields` is described as fields causing the request to fail. Neither response proves an individual scheduled payout, transfer, or bank receipt.
- Listed errors are 400 (request reading/understanding), 401 (authentication), 403 (insufficient permissions), 422 (validation), and 500 (server processing). This TEST-server snapshot does not establish a live endpoint or current merchant eligibility.

## Detail locators

- Request fields, payout routing, metadata replacement, schedule enum/action/defaults and conditional reason: pinned raw, `## Parameters > ### Request body`, lines 12–26.
- Example weekly schedule with `CLOSE`: `## Request examples > ### basic`, lines 28–39; example is not a required combination.
- 200/202 status text and response fields: `## Responses`, lines 40–91; errors and illustrative JSON: lines 94–182.

## Related

- [[adyen-classic-platforms]] — Classic account-holder/account context and payout flow.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/updateAccount/2026-09-15|Account API v6 POST /updateAccount capture]]
