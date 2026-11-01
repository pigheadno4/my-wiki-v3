# Fixed-query check: ACCOUNT_CREATED

## Q1

The 2026-09-15 `Notification/latest` page specifies an incoming Adyen `ACCOUNT_CREATED` webhook after a Classic account creation, with `accountCode` and `accountHolderCode` optionally in `content`. Required envelope fields are `eventDate`, `eventType`, `executingUserKey`, `live`, and outer `pspReference`; the content can include payout-coupling and schedule fields, `resultCode`, `status`, `invalidFields`, and an outer processing `error`. The page does not state a numeric Notification API version. See [[source-adyen-api-explorer-notification-latest-post-account-created]], [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 5–39]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CREATED).

## Q2

The response section says HTTP 200 and optional `notificationResponse` set to **[accepted]** acknowledge receipt; they do not establish creation or financial state. The sample combines error/invalid fields with `Success` and `Active`, so it is not a reliable universal outcome rule. The separate Classic creation guide supplies the wait-for-`ACCOUNT_CREATED` business-logic gate. This pinned operation page does not specify delivery ordering, retries, deduplication, signatures, or a payout outcome. See [[source-adyen-api-explorer-notification-latest-post-account-created]], [[raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_CREATED/2026-09-15|raw lines 43–91]], and [Adyen API Explorer](https://docs.adyen.com/api-explorer/Notification/latest/post/ACCOUNT_CREATED).
