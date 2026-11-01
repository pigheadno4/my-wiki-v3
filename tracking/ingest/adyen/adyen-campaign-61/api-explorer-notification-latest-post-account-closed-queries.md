# C61 fixed-query answers — api-explorer-notification-latest-post-account-closed

Pinned raw: `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CLOSED/2026-09-15.md`. Canonical retrieval route: [[source-adyen-api-explorer-notification-latest-post-account-closed]]; URL: https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CLOSED

## Q1

Adyen sends an incoming `POST /ACCOUNT_CLOSED` webhook when an account is closed, linking to the separate Account API close operation (raw lines 5–7). Required body properties are `eventDate`, `eventType`, `executingUserKey`, `live` and top-level request `pspReference` (26–30). `content` is optional, as are its closed `accountCode`, nested request `pspReference`, `resultCode`, and new `status`; the permitted status values are Active, Inactive, Suspended, Closed (14–22). Optional `invalidFields` and `error` describe validation/failed-request information (16–25). The example contains `eventType: ACCOUNT_CLOSED`, `resultCode: Success`, `status: Closed`, and also an `error` object, so the example does not establish an unconditional outcome rule (34–62).

## Q2

The response section states HTTP 200 success and optional `notificationResponse` set to `[accepted]` to acknowledge receipt (raw lines 64–72). This is a receiver acknowledgment, not proof of execution of `POST /closeAccount` or a specific account state. The raw page states no delivery timing, ordering, retry, deduplication, signature, or broader financial finality rule (full raw lines 1–72). Read the separate closing-operation source for operation consequences: [[source-adyen-api-explorer-account-latest-post-closeaccount]]. Retrieval route: [[source-adyen-api-explorer-notification-latest-post-account-closed]]; https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CLOSED
