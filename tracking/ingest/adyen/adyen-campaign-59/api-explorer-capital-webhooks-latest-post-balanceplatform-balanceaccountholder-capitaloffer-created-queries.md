# api-explorer-capital-webhooks-latest-post-balanceplatform-balanceaccountholder-capitaloffer-created fixed query answers

Pinned raw: `raw/adyen/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created/2026-09-15.md` (SHA-256 `db698a337afb596564d5fb4b25ac8af4f2520abd555bed2d571544cb80517010`). Canonical source route: `wiki/sources/adyen/source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-balanceaccountholder-capitaloffer-created.md`. Canonical URL: https://docs.adyen.com/api-explorer/capital-webhooks/latest/post/balancePlatform.balanceAccountHolder.capitalOffer.created

## Q1

The captured incoming `balancePlatform.balanceAccountHolder.capitalOffer.created` Capital webhook provides details of a static offer created for an account holder (raw lines 5–7). The table requires `accountHolderId`, described as the account holder to whom a grant is offered; static-offer `id`, amount, `loan`/`cashAdvance` contract type, validity dates, fee and repayment configuration are optional (raw lines 11–33). If the amount, fee or repayment objects are supplied, their listed nested currency/minor-unit value, fee amount, repayment basis points, term estimated days and threshold amount have the table's conditional requiredness (raw lines 15–32). The page has no request example, explicit `type`/`environment` envelope fields or numbered webhook version; `latest` is the captured route label.

## Q2

The `amount` description is what would be paid out, not evidence of a payout (raw line 15). Creation of a static offer does not establish acceptance, signed terms, a grant request/outcome, disbursement, booked credit, bank receipt or repayment. The response table says any HTTP 2xx accepts the webhook and `notificationResponse` is optional (raw lines 35–43); acknowledgment is not a financing outcome. This page specifies no failure/reversal sequence or delivery ordering, retry, deduplication or signature rule (full raw lines 1–43).
