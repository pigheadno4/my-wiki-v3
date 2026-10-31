# C59 Capital webhooks v1 overview fixed-query answers

## Q1

The 2026-09-15-captured API Explorer page explicitly labels the family **Capital webhooks v1**. Adyen says these notify a system when financing offers or grants are created or updated, and suggests using their data in a dashboard showing users business-financing details (raw lines 5–9). Its incoming POST catalog separates static offer creation (`balancePlatform.balanceAccountHolder.capitalOffer.created`), dynamic offer creation (`balancePlatform.capital.dynamicOffer.created`), grant creation (`balancePlatform.grants.created`) and grant update (`balancePlatform.grants.updated`) (lines 11–19). The page gives no event payload requirements, identity fields or transition schema. The `latest` route does not independently prove the current version. Canonical route: [[source-adyen-api-explorer-capital-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/capital-webhooks/latest/overview.

## Q2

This overview establishes four named notification routes, not an accepted offer, approved or funded grant, booked transfer, bank receipt or repayment (raw lines 5–19). The page does not give event payloads, grant statuses, amounts/currencies, failure or reversal conditions, delivery/order/retry/deduplication or signature rules. A grant-created/updated event name should not be read as disbursement; transfer and transaction evidence belongs to separate contracts. The captured family title says v1, while `latest` is only its documentation route. Canonical route: [[source-adyen-api-explorer-capital-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/capital-webhooks/latest/overview.
