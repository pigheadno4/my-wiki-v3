# C21 worker queries — relayed authorisation

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation-relayed-authorisation]] → [[raw/adyen/docs/issuing/authorisation/relayed-authorisation/2026-09-15]]. Related contrast: [[source-adyen-docs-issuing-validation-checks]] → [[raw/adyen/docs/issuing/validation-checks/2026-09-15]].

## Q1. What decision does the platform make, and what setup is required?

When Adyen receives a payment authorisation request, it sends the configured platform endpoint a relayed-authorisation webhook with transaction, rule and validation data; the platform replies with approval or refusal (primary raw lines 19–23, 80–89). Its HTTPS endpoint must accept JSON and basic authentication on port 443, 8443 or 8843 (primary raw lines 34–40). Customer Area configuration requires the **Manage relayed authorisation configuration** role and includes URL, basic auth, HMAC, and decision-on-error settings (primary raw lines 42–78). The sample incoming `authorisationDecision.status: Authorised` is example data, not a final-payment guarantee (primary raw lines 97–115, 226–255).

## Q2. What are the time, fallback and response-contract boundaries?

The dedicated guide says reply within 2000 ms and configure default approval/refusal if no response arrives; separate error settings cover timeout/connection and invalid response, while 4xx/5xx trigger fallback (primary raw lines 23–26, 73–76, 80–95, 258–263). The validation-checks guide says stand-in triggers after 1500 ms with no response (related raw lines 162, 168); these snapshots leave the timing relationship unresolved. The dedicated guide's prose describes a response-body `status` field, whereas its examples nest `status` under `authorisationDecision` (primary raw lines 86–89, 226–255). Verify the contract before implementation; a webhook setup or sample does not prove authorization, capture, or settlement.
