# Fixed query check — POST /merchants

Canonical target: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-post-merchants.md`
Canonical URL: https://docs.adyen.com/api-explorer/Management/latest/post/merchants

## Q1

For `Management/latest/post/merchants`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Management API test `/v3` page creates a merchant account under the `companyId` company account. The endpoint is for integrations that require it, including Adyen for Platforms Manage, and says Adyen contact setup plus the Management API—Accounts read and write credential role are needed. `companyId` is required in the request-property table. For Platforms Manage, `businessLineId`, `legalEntityId`, and `pricingPlan` are described as required despite general `No` table flags; Adyen supplies the pricing-plan values. `reference` becomes required and company-unique only when Adyen has configured a company-account template; with that template, the merchant ID equals the reference, otherwise Adyen generates the ID. The page does not separately mark the body itself required. (Raw lines 5–29, 43–57.)

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

`200` says the create request succeeded and lists merchant-account fields, while `204` says it succeeded with no content. The example's matching `reference` and `id` does not prove every company has a template. The page lists `400` malformed/problem request, `401` authentication required, `403` insufficient permissions, `422` validation, and `500` server failure. It shows test `/v3` only, despite `latest` in the URL. It does not establish live merchant activation, payment-method enablement, legal-entity verification, payment or payout success, deletion, propagation timing, or current live access. (Raw lines 15–16, 43–61, 64–177.)
