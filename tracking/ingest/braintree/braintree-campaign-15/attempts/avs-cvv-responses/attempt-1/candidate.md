---
title: "Braintree AVS and CVV Response Codes"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/processor-responses/avs-cvv-responses"
raw_files:
  - "braintree/docs/reference/general/processor-responses/avs-cvv-responses-2026-09-16.md"
tags: [braintree, avs, cvv, card-verification, processor-responses]
---

## Overview

This Braintree reference defines the documented Address Verification System (AVS) and Card Verification Value (CVV) response categories. It distinguishes matches and mismatches from not-verified, not-provided, unsupported or nonparticipating, not-applicable, skipped and AVS system-error outcomes, while preserving an evidence gap in the damaged introduction that should have named the response objects.

## Key takeaways

- AVS reports postal-code and street-address results separately. For each, `M` means the supplied value matches the cardholder bank's information, `N` means it does not match, `U` means the issuing bank received the value but did not verify it, and `I` means the value was not provided.
- An AVS `U` is not a mismatch: the page says it typically occurs when the processor declines an authorization before the bank evaluates the postal code or street address.
- The remaining AVS categories are issuing-bank non-support (`S`), system error preventing verification (`E`), transaction type not supporting address verification (`A`), and a skipped AVS check (`B`). The page says `S` typically indicates an issuing bank outside the US, Canada and the UK.
- CVV uses match (`M`), mismatch (`N`), not verified (`U`), not provided (`I`), issuer nonparticipation (`S`), not applicable (`A`) and skipped (`B`) categories. For `U`, the page again qualifies that the bank may have declined authorization before evaluating the CVV; `I` also occurs for a transaction made with a vaulted payment method.
- The collected introduction reads only `Available on theandresponse objects.` Because the object names are missing, this page cannot establish which response objects or SDK fields expose these values. It also does not state that an AVS/CVV match guarantees transaction approval or that a mismatch alone determines a decline, fraud decision or retry action.

> [!warning] Damaged response-object scope
> Do not reconstruct the missing response-object names or field placement from the tables. Use this page for result-category semantics only; consult a complete operation or SDK authority before attributing the categories to a specific object, field or transaction outcome.

## Detail locators

- Damaged response-object introduction: `# AVS and CVV Response Codes`, line 16.
- AVS postal-code match, mismatch, not-verified and not-provided categories: `## AVS`, lines 19-24.
- AVS street-address categories plus unsupported, system-error, not-applicable and skipped results: `## AVS`, lines 25-32.
- CVV match, mismatch, not-verified, not-provided/vaulted, issuer-nonparticipation, not-applicable and skipped results: `## CVV`, lines 35-45.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related stored-payment-method update route: [[source-braintree-payment-method-update-node]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|Braintree AVS and CVV rules]] - navigation-only route linked for Vault-specific rules; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/general/processor-responses/avs-cvv-responses-2026-09-16|Braintree AVS and CVV Response Codes]] - complete collected page defining AVS postal/street and CVV result categories with a damaged response-object introduction
