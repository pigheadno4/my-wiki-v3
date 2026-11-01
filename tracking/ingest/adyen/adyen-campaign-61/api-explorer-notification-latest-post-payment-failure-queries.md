# PAYMENT_FAILURE retrieval checks

## Q1 — What failed, and which account receives the affected funds?

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-classic-platforms.md` → `[[source-adyen-api-explorer-notification-latest-post-payment-failure]]` ([canonical URL](https://docs.adyen.com/api-explorer/Notification/latest/post/PAYMENT_FAILURE)). The pinned raw says this incoming notification concerns failure to book a split capture or refund (lines 5–7). For invalid account status or unknown `accountCode`, funds are credited or debited to or from the platform liable account instead of the specified split account (line 7). It does not itself prove the final outcome of a particular payment or refund.

## Q2 — Can the JSON sample be used as the PAYMENT_FAILURE contract, and how is receipt acknowledged?

Route: `[[source-adyen-api-explorer-notification-latest-post-payment-failure]]` ([canonical URL](https://docs.adyen.com/api-explorer/Notification/latest/post/PAYMENT_FAILURE)) → pinned raw lines 9–33 and 35–87. The table requires top-level `eventDate`, `eventType`, `executingUserKey`, `live`, `pspReference` and marks `content`/`error` optional (lines 11–33). The example has `eventType: TRANSFER_FUNDS` and a `content` shape that differs from this table (lines 37–78), so it should not establish the PAYMENT_FAILURE event payload. The response section shows `200 Success` and says optional `notificationResponse` may be set to `[accepted]` to acknowledge receipt (lines 79–87); this is not a claim that the booking succeeded.
