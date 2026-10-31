# Fixed queries — api-explorer-webhooks-latest-post-offer-closed

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-offer-closed.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/OFFER_CLOSED
Pinned evidence: `raw/adyen/api-explorer/Webhooks/latest/post/OFFER_CLOSED/2026-09-15.md`, SHA-256 `10de8bc74098ef49d8bfaeab1eba37c4215a9f016e28e8323ebd91ebcbec2f21`.

## Q1

The captured API Explorer `Webhooks/latest` page is an incoming `POST /OFFER_CLOSED` offer-expiry notification reference; shopper session abandonment is an example cause, and **cards** expire after 12 hours by default (raw lines 5–7). The example has `eventCode: "OFFER_CLOSED"`, `paymentMethod: "ideal"`, a merchant account/reference, PSP reference, amount, event date, and `success: "true"` (raw lines 31–58). The body table marks `live` and `notificationItems` optional at top level; inside `NotificationRequestItem`, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required (raw lines 11–27). `originalReference` is optional and described for modifications, while `pspReference` identifies Adyen's transaction or request (raw lines 23–25). The table says HTTP POST notification currency and value are URL parameters (raw line 18), while the example puts them in a nested JSON `amount` object (raw lines 42–45); this snapshot does not reconcile the two representations. The `latest` label is not a numbered version. The iDEAL sample does not extend the card expiry rule to iDEAL.

## Q2

`success` is a string about the `eventCode` outcome, so the sample's `true` denotes execution of the offer-closed event, not successful payment (raw lines 26–27, 46–53). HTTP `200`/status-code acceptance is receiver acknowledgement of the webhook, distinct from that event outcome (raw lines 59–62). The example's `additionalData.hmacSignature` is not a universal signature requirement (raw lines 38–40); the page gives no general signature, response-body, delivery/order/retry/deduplication, or payment finality rules. Consult the canonical route and its raw locators for the bounded contract.
