---
title: "Braintree Authorization Responses"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/processor-responses/authorization-responses"
raw_files:
  - "braintree/docs/reference/general/processor-responses/authorization-responses-2026-09-16.md"
tags: [braintree, authorization, processor-responses, declines, retries]
---

## Overview

This Braintree reference explains processor authorization response classes, including approvals, hard and soft declines, and network problems. It also documents retry restrictions that narrow when a declined transaction may be attempted again; the full response-code inventory and code-specific implications remain in the raw page.

## Key takeaways

- Braintree says 1000-class codes mean the processor successfully authorized the transaction and `success` is true. That processor approval does not rule out a separate gateway rejection under the merchant's processing settings.
- A 2000-class code means the processor declined the authorization and `success` is false, while a 3000-class code indicates a back-end processing-network problem. The page warns that an individual code's explanation can be ambiguous.
- Hard declines are non-temporary issues for which another attempt with the same payment method is unlikely to succeed. Soft declines are temporary and may succeed on a later attempt, but that category does not itself grant unrestricted retries.
- Mastercard prohibits retries for the listed hard-decline codes. Transactions originally carrying a recurring ecommerce indicator have additional card-association restrictions: soft declines are limited to 15 retries in 30 days, codes 2004 and 2015 must not be retried, and code 2005 must not be retried with the same payment information.
- Authorization and capture can incur merchant fees in some markets. The page routes the fee qualification to the Braintree User Agreement and does not state that every authorization or capture incurs a fee.

## Scope boundary

This page classifies processor authorization responses and retry handling. Processor approval is distinct from gateway acceptance, and neither an approval class nor `success` alone establishes capture or final settlement. Code-specific meanings, customer guidance, payment-method qualifications, and the complete decline table remain at the raw locators below.

## Detail locators

- Some-market merchant-fee qualification and Braintree User Agreement route: `# Authorization > **NOTE**`, lines 17-18.
- 1000-class processor approval, `success` value, and separate gateway-rejection possibility: `## Approvals`, lines 21-23.
- Approval-code inventory, including refund, credit, voice-authorization, partial-approval, risk and settlement-captured cases: `## Approvals`, lines 25-32.
- 2000-class declines, 3000-class network problems and ambiguity qualification: `## Declines`, lines 35-37.
- Hard-versus-soft decline definitions and general pending-order retry approach: `### Types of declines` through `#### Retrying declined transactions`, lines 38-52.
- Mastercard prohibited-retry codes and recurring-ECI retry restrictions: `#### Retrying declined transactions`, lines 54-74.
- Complete response-code meanings, implications and hard/soft labels: `### Decline codes`, lines 77-191.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Recurring-ECI retry context: [[recurring-payments]]

## Raw Sources

- [[raw/braintree/docs/reference/general/processor-responses/authorization-responses-2026-09-16|Braintree authorization-response reference]] - complete collected page covering approval and decline classes, retry restrictions, merchant-fee qualification, and the response-code table
