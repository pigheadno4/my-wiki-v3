# Fixed query answers — api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccount-recurringtopup-created

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccount-recurringtopup-created]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created). Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.recurringTopUp.created/2026-09-15.md`.

## Q1

The captured `latest` POST page is an **incoming webhook** with example type `balancePlatform.balanceAccount.recurringTopUp.created`; Adyen says it sends it when a recurring top-up is successfully created for a balance account (raw lines 5–7, 68–70). The table requires `data.accountId` for the balance account and `data.webhookTopUpConfiguration.id` for the configuration, plus the configuration's `counterparty`, `description`, `status`, `topUpAmount`, and `trigger` (raw lines 14–27). `status` can be active or inactive, amount can be fixed or target, and trigger can be a schedule or minimum-balance threshold (raw lines 25–27). `data.id`, platform ID, event creation date, queued timestamp, mandate, and beneficiary reference are optional in this table (raw lines 16–24, 29). The EUR amounts, weekly schedule, transfer-instrument ID, and mandate in the JSON are example values only (raw lines 32–72).

## Q2

The event reports successful **configuration creation**; it does not report a triggered top-up, transfer, booked credit, or bank receipt (raw lines 5–7, 14–27). A receiver accepts the webhook with any `2xx`; the `200`/`[accepted]` body is an acknowledgement example (raw lines 73–92). This page does not specify delivery order, retry or deduplication, signature verification, transfer failure or reversal outcomes. Its `latest` URL and one captured example do not establish a numbered version, current availability, or financial finality (raw lines 1–7, 32–92). Follow the source route and its raw locators for exact fields rather than importing behavior from another webhook family.
