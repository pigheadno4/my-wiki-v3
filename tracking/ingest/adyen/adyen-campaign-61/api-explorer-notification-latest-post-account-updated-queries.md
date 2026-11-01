# Fixed retrieval answers — api-explorer-notification-latest-post-account-updated

Pinned raw: `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_UPDATED/2026-09-15.md`
Canonical source: [[source-adyen-api-explorer-notification-latest-post-account-updated]]
Canonical URL: https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_UPDATED

## Q1 — purpose, identities, fields, limits and lifecycle

This captured `Notification/latest` page describes an **incoming Adyen webhook** sent when a Classic account is updated, pointing to Account API `/updateAccount` (raw lines 5–7). The optional `content` parent contains a nested required `accountCode` when present (lines 12–15); top-level `eventDate`, `eventType`, `executingUserKey`, `live` and `pspReference` are marked required (lines 33–37). Optional fields include holder-held bank-account UUID and card payout-method routing, payout schedule and speed, metadata, description, request `pspReference`, `resultCode`, `invalidFields`, and top-level `error` (lines 16–32). `HOLD` blocks scheduled payouts but allows manual initiation (line 26). See [[source-adyen-api-explorer-notification-latest-post-account-updated]] and https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_UPDATED.

## Q2 — acceptance and evidence boundaries

The response table says the receiver can set optional `notificationResponse` to `[accepted]` to acknowledge notification receipt (raw lines 79–87). That is not an account-update outcome, scheduled payout, or bank receipt. The example contains both `error` and `invalidFields` and `content.resultCode="Success"` (lines 43–76), so it cannot establish a single outcome interpretation. This page does not specify delivery order, retry, deduplication or signature mechanics. The separate Classic scheduled-payout guide says to wait for `ACCOUNT_UPDATED` to confirm a schedule update after the Account API response; that guidance is attributed to [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]], not this raw. See [[source-adyen-api-explorer-notification-latest-post-account-updated]] and https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_UPDATED.
