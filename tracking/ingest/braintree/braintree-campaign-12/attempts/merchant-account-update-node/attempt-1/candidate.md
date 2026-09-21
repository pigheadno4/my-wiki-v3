---
title: "Braintree Merchant Account Update (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/merchant-account/update/node"
raw_files:
  - "braintree/docs/reference/request/merchant-account/update/node-2026-09-16.md"
tags: [braintree, node-js, merchant-accounts, marketplace, updates]
---

## Overview

This Braintree Node.js reference demonstrates `gateway.merchantAccount.update()` with a merchant-account identifier and an update parameter object. The worked example changes one individual identity field and checks `result.success` in the callback.

## Key takeaways

- The example identifies the merchant account with the string `blue_ladder_store` and supplies `individual.firstName` as the displayed change. It does not establish the identifier's general format or a complete list of updateable fields.
- The callback exposes `err` and `result`, then reads `result.success`; the example comment shows `true`. The page does not show how errors or an unsuccessful result are handled.
- If the merchant account cannot be found, the page routes that case to Braintree's Node.js `notFoundError` reference. Exact exception details remain in the linked raw reference.
- This worked example does not establish universal update eligibility or wider effects on approval, verification, funding, settlement, existing transactions, agreements, or account activation. The linked Marketplace and sub-merchant guides are navigation only here.

> [!warning] Worked-example and side-effect boundary
> Treat the displayed account ID, first-name change, and successful result check as one Node.js example. Do not generalize them into universal eligibility, supported-field, validation, propagation, or downstream-effect rules.

## Detail locators

- Merchant Account response-object route: `# Merchant Account: Update`, line 15.
- Displayed update parameter object: `# Merchant Account: Update > ### Node`, lines 21-25.
- Merchant-account identifier, update invocation, callback arguments and `result.success` check: `# Merchant Account: Update > ### Node`, lines 27-30.
- Missing-account error route: line 33.
- Marketplace and sub-merchant update navigation: `## See also`, lines 36-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/merchant-account/node-2026-09-16|Braintree Node.js Merchant Account response reference]] - navigation-only response-object route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation-only destination for the linked `notFoundError`; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-marketplace/overview-2026-09-16|Braintree Marketplace overview]] - navigation-only Marketplace route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-marketplace/update/node-2026-09-16|Braintree Node.js sub-merchant update guide]] - navigation-only sub-merchant update route linked by this page; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/merchant-account/update/node-2026-09-16|Braintree Node.js merchant-account update reference]] - complete collected page covering the displayed account identifier, first-name update, callback result check, missing-account route, and related navigation
