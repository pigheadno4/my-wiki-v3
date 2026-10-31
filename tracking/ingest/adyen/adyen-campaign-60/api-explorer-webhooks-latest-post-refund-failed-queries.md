# Fixed retrieval answers — Webhooks latest POST /REFUND_FAILED

## Q1

[[source-adyen-api-explorer-webhooks-latest-post-refund-failed]] routes to the 2026-09-15 Adyen Webhooks `latest` incoming event reference ([canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND_FAILED)). Its headline and description say the refund failed due to card-scheme rejection (API Explorer raw lines 5–7), while its single example names BLIK (lines 38–54); neither proves general BLIK eligibility nor a card-only method limit. The nested table marks amount, eventCode, eventDate, merchantAccountCode, merchantReference, pspReference and success required; originalReference and reason are optional (lines 18–27). Outer live and notificationItems are marked No (lines 14–16). The API Explorer table describes originalReference generically for modifications (line 23). The separate [[source-adyen-docs-online-payments-refund]] guide maps originalReference to original payment PSP reference and pspReference to refund request PSP reference for REFUND_FAILED (guide raw lines 673–681).

## Q2

[[source-adyen-api-explorer-webhooks-latest-post-refund-failed]] shows `200 Success` and HTTP-status-based webhook acceptance (API Explorer raw lines 60–63; [canonical source](https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND_FAILED)). Its example's `success: \"true\"` is success of the REFUND_FAILED event, not refund completion (lines 46, 54; field definition line 27). The table describes reason for false success, yet the example has `reason: \"Refund Failed\"` with true success (lines 26, 53–54). The page gives no delivery/order/retry/deduplication guarantee, signature rule, or settlement outcome. `latest` is the captured route label, not a numeric version pin.
