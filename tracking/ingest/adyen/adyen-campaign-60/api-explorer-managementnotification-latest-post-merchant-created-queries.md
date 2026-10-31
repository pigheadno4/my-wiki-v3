# Fixed queries — api-explorer-managementnotification-latest-post-merchant-created

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-managementnotification-latest-post-merchant-created.md` — https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.created
Pinned evidence: `raw/adyen/api-explorer/ManagementNotification/latest/post/merchant.created/2026-09-15.md`, SHA-256 `bec8a7b95fd2aa41add72a87f044d47f405334baea42dd0743f9470c924a3c47`.

## Q1

This captured `ManagementNotification/latest` page describes an incoming `merchant.created` notification that a merchant account was created; the `POST` heading is webhook delivery, not the creation operation (raw lines 5–7). The `latest` label gives no numbered version. The body table requires `createdAt`, `data`, `data.capabilities`, `data.companyId`, `data.merchantId`, `data.status`, `environment`, and `type`; `legalEntityId` is optional (raw lines 11–30). Capability entries require `requested` and `requestedLevel`, while allowance and verification fields are optional (raw lines 16–24). The test example has `type: "merchant.created"`, a company ID, merchant ID, requested `sendToTransferInstrument` capability, and `PreActive` status; it does not show allowance or completed verification (raw lines 32–52).

## Q2

Merchant creation is distinct from readiness. `PreActive` cannot access Customer Area or process payments; `Active` enables processing and payouts only if the company account is also Active; `InactiveWithModifications` permits modifications and payouts but no new payments; `Inactive` disables processing and payouts; `Closed` is irreversible and disables login, processing and payouts (raw line 28). `requested` does not mean `allowed`; Adyen sets `allowed: true` after successful verification, while the example only shows a requested capability (raw lines 16–24, 41–49). HTTP `200` is shown and any `2xx` accepts the webhook; this receiver response is separate from resource status or eligibility (raw lines 53–61). The page does not establish delivery/order/retry/deduplication, signature, future activation, or payment/payout execution guarantees. Consult the canonical source route and raw locators for this Management account contract.
