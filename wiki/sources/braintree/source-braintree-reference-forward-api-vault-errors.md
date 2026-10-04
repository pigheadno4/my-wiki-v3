---
title: "Braintree Forward API Vault Errors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/vault-errors"
raw_files:
  - "braintree/docs/reference/forward-api/vault-errors-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, vault-errors, api-errors]
---

## Overview

This collected, unversioned Braintree [[braintree-forward-api|Forward API]] reference catalogs Vault-related failures returned in a response body to the caller's application. The page shows a JSON body resembling an example with top-level `error`, nested `message`, and `request-uuid` fields; because the page describes the body as resembling the example, the sample is not a guarantee of an exhaustive or fixed response schema. See [[braintree]].

This is Forward API Vault-error reference material, not [[braintree-orchestration]] documentation. It does not establish destination-side acceptance or processing, or any payment authorization, capture, settlement, reconciliation, or funding result.

## Key takeaways

- Production Forward API use is subject to eligibility. The snapshot directs readers to an Account Manager or Business Development; collection of the page and possession of credentials do not establish current merchant eligibility, production approval, or enablement.
- The Vault-status catalog maps `401` to invalid API credentials or an IP allowlist violation, and `403` to credentials lacking the Forward API right. For the latter, the page directs readers to contact Braintree to confirm that the user's API credentials have been allowlisted. These entries identify failure conditions, not credential-provisioning or automatic-retry procedures.
- The `404` entries distinguish an invalid `merchant_id`, `payment_method_nonce`, or `payment_method_token`; the nonce and token cases list corresponding not-found text in additional `message` content. Use the raw table for the exact field links and message text.
- The `422` entries cover a malformed or data-insufficient payment method, a payment method that cannot be used with Forward API, failures in one or more payment methods or `cse_data` bindings, and a PayPal-specific nonce condition. The bindings entry says to inspect the returned object for details and identifies `message` as a JSON object; it does not define the object's schema or guarantee a particular correction or outcome.
- For forwarding a PayPal account, the page says the supplied `payment_method_nonce` must come from the Vault flow and gives additional text stating that a Pre-Approved Payment enabled PayPal account is required for exporting. This is a subject-specific prerequisite in the Vault-error catalog, not a general statement about other payment methods or sibling APIs.

> [!warning] Eligibility and access boundary
> Production Forward API use remains eligibility-gated. A captured error catalog, allowlisted credential, or corrected request does not by itself prove current production enablement or destination authorization.

> [!warning] Error reference is not execution evidence
> The page describes Vault failures returned by Forward API. It supplies no general retry contract and does not establish that a destination accepted or processed a forwarded request or that any payment lifecycle step occurred.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `**AVAILABILITY**`, raw lines 17-20.
- Example response body and its `error`, nested `message`, `vault_error?`, `vault_status`, message text, and `request-uuid`: opening JSON example, raw lines 22-34.
- Vault-context lead-in and complete status table: raw lines 35-45.
- Invalid credentials or IP allowlist violation (`401`) and missing Forward API right (`403`): raw lines 37-38.
- Invalid merchant, nonce, and token cases (`404`): raw lines 39-41.
- Insufficient/malformed data, non-exportable method, and payment-method or `cse_data` binding cases (`422`): raw lines 42-44.
- PayPal-account nonce Vault-flow prerequisite and Pre-Approved Payment enabled account text (`422`): raw line 45.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Distinct processor-connection route: [[braintree-orchestration]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]]
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Forward API forwarding-request reference]]
- [[raw/braintree/docs/guides/payment-methods/node-2026-09-16|Braintree payment methods guide for Node.js]]
- [[raw/braintree/articles/risk-and-security/allowlisting-2026-09-16|Braintree IP allowlisting article]]

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/vault-errors-2026-09-16|Braintree Forward API Vault errors]] - fully read 2026-09-16 snapshot covering production eligibility, the illustrative response body, Vault status mappings, field-specific failures, binding-error context and the PayPal Vault-flow prerequisite
