---
title: "Adyen Issuing validation types and refusal reasons"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/validation-checks"
raw_files:
  - "adyen/docs/issuing/validation-checks/2026-09-15.md"
tags: [adyen, issuing, authorisation, validation, refusals]
---

## Overview

This Adyen Issuing guide, last modified 2021-11-15 and captured 2026-09-15, catalogs checks Adyen runs before authorising an issued-card transaction and reasons that may appear when one is refused. It is a diagnostic reference for [[adyen-issuing]], not evidence that a particular card payment was authorised or settled.

## Key takeaways

- For a `balancePlatform.transfer.created` webhook whose `status` is `refused`, inspect its `validationFacts` array for validation type and result, especially `invalid` results. The guide also directs users to Customer Area **Balances > Transfers** for validation results and refusal reasons (raw lines 19–34).
- Result meanings differ: `valid` passed; `invalid` failed; `notValidated` means the check could not run because services were unreachable or required information was unavailable; `notApplicable` means Adyen judged the check inapplicable to the transaction state. A transaction-rule failure can make relayed authorisation `notApplicable` (raw lines 36–45).
- The type catalog covers resource/card existence and status, balance and limits, cardholder or card authentication, AVS/CVC/PIN/3DS checks, sanctions or screening, scheme rules, transaction rules and relayed authorisation. The specific conditions and meanings are at raw lines 47–197; not every check necessarily runs for every transaction.
- `relayedAuthorisation` applies only when enabled. Refusing the payment fails that validation. If Adyen receives no response within **1500 milliseconds**, `relayedAuthorisationStip` stand-in processing is triggered; its `valid` or `invalid` result depends on the configured default fallback. A prior transaction-rule failure can instead make relayed authorisation inapplicable (raw lines 158–168).
- `partialApproval` is described only for supported acquirers and certain MCCs, such as automatic fuel dispensers. The guide says its validation result is always `valid` when performed under those conditions; a separate “Partially approved” refusal-reason entry describes approval only up to available balance. Preserve those as separate fields/context, rather than interpreting `valid` as full-amount approval (raw lines 130–132, 295–297).

## Detail locators

- `mitAllowedMerchant`: recurring transactions require an authenticated initial transaction; for nonrecurring transactions the merchant or acquirer ID must be allowed, with failed checks described at raw lines 123–128.
- `transactionRules` failures: the `transactionRulesResult` webhook object and Customer Area view provide more detail (raw lines 182–189).
- Full validation-type catalog, including card authentication, balance, limits and screening: raw lines 47–197. Full Customer Area refusal-reason catalog, including expired or blocked card, insufficient balance, failed 3DS/CVC/PIN, SCA, contactless limit and issuer timeout: raw lines 199–337. These are diagnostic descriptions, not proof of a live outcome.
- The refusal-reason list includes generic “Declined”, “Error”, “Refused” and “Transaction not permitted” entries that direct the reader back to failed validation types (raw lines 239–253, 311–313, 327–329).

## Related

- [[adyen-issuing]] — Issuing concept.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/validation-checks/2026-09-15|Adyen Issuing validation checks, captured 2026-09-15]]
