# Fixed queries — api-explorer-webhooks-latest-post-cancellation

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-cancellation.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/CANCELLATION
Pinned evidence: `raw/adyen/api-explorer/Webhooks/latest/post/CANCELLATION/2026-09-15.md`, SHA-256 `6ea4dd72603a24157d0058e49b60d7cfe648680f04607de5bb42f7baa035f547`.

## Q1

This is the captured API Explorer `Webhooks/latest` incoming `POST /CANCELLATION` reference. It reports the result of a request to cancel a payment, rather than defining a merchant cancellation operation (raw lines 5–7). The example carries `eventCode: "CANCELLATION"`, an event date, merchant account and payment reference, optional original payment reference, and Adyen PSP reference (raw lines 18–27, 31–55). The request-body table marks `live` and `notificationItems` optional at the top level, while marking `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required inside `NotificationRequestItem` (raw lines 11–27). `originalReference` is optional and connects a modification to the original payment request; `pspReference` identifies the transaction or request (raw lines 23–25). `success` is a string indicating whether the event executed successfully, and `reason` is an optional refusal explanation when it is false (raw lines 26–27). The page uses the `latest` snapshot label and gives no numbered API version.

## Q2

`success` reports the `eventCode` outcome; `true` and `false` have the meanings stated in the table, while the sample shows only a `true` cancellation event (raw lines 26–27, 31–55). The response section labels HTTP `200` Success and says webhook events are accepted based on HTTP status code (raw lines 56–59). Thus receiver acceptance is distinct from cancellation-event success. The page gives no response-body contract, delivery/order/retry/deduplication/signature rule, capture/settlement conclusion, deprecation rule, or further cancellation finality beyond the event outcome. Consult the canonical route and its raw locators for this bounded contract.
