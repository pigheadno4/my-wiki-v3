# Fixed queries — api-explorer-webhooks-latest-post-refunded-reversed

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-post-refunded-reversed.md` — https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED
Pinned evidence: `raw/adyen/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED/2026-09-15.md`, SHA-256 `0b618c575eac92107db16af263ab147ed5c9371ac9ac3ff050ddd184805a335d`.

## Q1

The captured `Webhooks/latest` `POST /REFUNDED_REVERSED` page describes an incoming notification that a refunded amount was reversed and, in this page's wording, returned to “your bank account” (raw lines 5–7). The `latest` label gives no numbered version. The body table marks outer `live`, `notificationItems`, and wrapper optional; inside an item, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required (raw lines 11–27). Optional `originalReference` links modifications to the original payment request; `pspReference` identifies Adyen's transaction or request (raw lines 23–25). The example carries `eventCode: "REFUNDED_REVERSED"`, an original reference, and `success: "true"` (raw lines 42–50). The table says HTTP POST currency/value are URL parameters, but the example places them in a nested JSON `amount` object; this snapshot does not reconcile them (raw lines 18, 38–41).

## Q2

`success` is event-scoped, and the optional `reason` is described for `success: false` (raw lines 26–27). The example nevertheless has a nonempty `reason` with `success: "true"`; it does not establish a new reason rule (raw lines 49–50). HTTP `200` and status-code acceptance describe receiver acknowledgement, separate from the reversal event outcome (raw lines 56–59). The endpoint's “your bank account” statement differs from the existing Adyen refund guide's “returned to Adyen” and merchant-account wording; the sources do not reconcile destination or independently prove bank receipt (raw line 7; [[source-adyen-docs-online-payments-refund]]). This page gives no delivery/order/retry/deduplication/signature, response-body or numbered-version guarantee. Consult the canonical route and raw locators for the bounded contract.
