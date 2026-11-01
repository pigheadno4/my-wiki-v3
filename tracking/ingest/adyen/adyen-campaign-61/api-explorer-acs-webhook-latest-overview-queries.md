# C61 fixed-query answers — api-explorer-acs-webhook-latest-overview

Pinned raw: `raw/adyen/api-explorer/acs-webhook/latest/overview/2026-09-15.md`. Canonical retrieval route: [[source-adyen-api-explorer-acs-webhook-latest-overview]]; URL: https://docs.adyen.com/api-explorer/acs-webhook/latest/overview

## Q1

The captured **Authentication webhooks v1** overview says Adyen sends webhooks about cardholder-authentication events (raw lines 5–7). It catalogs POST `balancePlatform.authentication.created` (“Cardholder authenticated”) and POST `balancePlatform.authentication.relayed` (“Out-of-band authentication requested”) (9–15). It does not specify event payload fields, identifiers, conditionality, response fields, limits or challenge timing; those belong to endpoint references.

## Q2

The 15-line catalog states no receiver acceptance or decision response, delivery order, retry, deduplication, signature, authentication-outcome rule, payment authorization, or financial finality contract (raw lines 1–15). Its route summaries are labels, not proof that an individual cardholder completed authentication or that a payment was authorized. Retrieval route: [[source-adyen-api-explorer-acs-webhook-latest-overview]]; https://docs.adyen.com/api-explorer/acs-webhook/latest/overview
