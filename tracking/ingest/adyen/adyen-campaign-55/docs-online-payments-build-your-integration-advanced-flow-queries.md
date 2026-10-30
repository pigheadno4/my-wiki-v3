# C55 Advanced flow reviewer queries

Pinned source: `raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15.md`, SHA-256 `dbfc4c515cc40764229b30f52cfb42cab28bed5c7674e7fd7c78bcb165bab196`; canonical URL: `https://docs.adyen.com/online-payments/build-your-integration/advanced-flow`. Full raw lines 1-24629 read independently.

## Q1. In Advanced flow, who makes the payment requests and what does the client handle?

The merchant payment server requests `/paymentMethods`, `/payments`, and `/payments/details` as needed. Drop-in or Components collect details and handle client-side actions through variant-specific callbacks/delegates; API-only requires a merchant-built UI and client-side action logic. The webhook server receives the outcome. Web Drop-in raw lines 70-78, 881-882, 1175-1193; Web API-only 4087-4132; React Native callbacks 16235-16243; Flutter callbacks 20774-20787. The embedded Sessions amount-update blocks at 1074-1173 and 3074-3173 do not make `/sessions` a universal Advanced step.

## Q2. What happens after redirect and which response establishes the final payment outcome?

A returning client can provide redirect details for `/payments/details`; if the shopper never returns, the additional details may be unavailable, so wait for the webhook. The API-only redirect sections expressly URL-decode `redirectResult` and `MD`/`PaRes` (raw 5195, 5273, 19389, 19467, 24058, 24136), while Web Drop-in/Components handle the redirect through their own callback flow (1658-1675, 3657-3674). `resultCode` is current shopper-facing status; the asynchronous `AUTHORISATION` webhook supplies the final order outcome using `merchantReference` (1941-1953, 24504-24511). The API-only 3DS examples have `PaReq` in `action.data` and the POST example but adjacent tables name `PaRes` (5209-5254, 24064-24138); retain the conflict.

## Review-specific platform check

Under **Flutter API only**, the source table specifies `channel` **Web** and curl sends `"channel": "Web"` (23364-23400), while its `returnUrl` requirements demand an `http://` or `https://` URL (23623-23643). This is unlike the React Native API-only iOS/Android channel and native return URL guidance (19043-19077, 19240-19261). A reader selecting Flutter API-only could mistakenly apply the Web-shaped values to a native Flutter app; the source summary needs an explicit qualification.

Canonical retrieval entry: [[source-adyen-docs-online-payments-build-your-integration-advanced-flow]].
