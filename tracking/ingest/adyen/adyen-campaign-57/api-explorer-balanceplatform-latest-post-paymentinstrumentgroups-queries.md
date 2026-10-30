# Fixed retrieval answers: api-explorer-balanceplatform-latest-post-paymentinstrumentgroups

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-paymentinstrumentgroups.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstrumentGroups

## Q1: For `balanceplatform/latest/post/paymentInstrumentGroups`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API v2 `POST /paymentInstrumentGroups` creates a payment instrument group for associating payment instruments; a transaction rule can be applied to a group. The group belongs to the specified `balancePlatform`. The request-body schema marks `balancePlatform` and `txVariant` required properties, with optional `description`, `properties`, and `reference`; it does not separately state body requiredness or `txVariant` values. Authentication and permission errors are documented without a named role. [Raw lines 5–21, 68–89.]

## Q2: What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 schema marks `balancePlatform` and `txVariant` required; `id` is marked optional although the success example includes one. Errors listed are 400, 401, 403, 422 and 500. Generic 422/500 examples describe payment-instrument operations, so they do not prove group-specific errors. This is a test-server `/bcl/v2` reference captured 2026-09-15 despite a `latest` URL. A group-creation response does not establish card association, rule application, a completed authorization, verification/approval, payment or funds movement, propagation timing, or live availability. [Raw lines 9–10, 32–45, 48–145, 147–225.]
