---
title: "Adyen Issuing integration and go-live checklist"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/integration-checklist"
raw_files:
  - "adyen/docs/issuing/integration-checklist/2026-09-15.md"
tags: [adyen, issuing, integration, cards, go-live]
---

## Overview

This Adyen Issuing checklist, captured 2026-09-15, guides an integration from test credentials and account-holder onboarding through cards, funding, authorization decisions, test payments, webhooks, reports, and a separate live-account transition. It is a procedure and test example, not evidence that an account or card is currently eligible or that a payment has completed. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Before development, Adyen says to design the implementation and obtain an Issuing test account and API credential from an Adyen contact. The Balance Platform credential is used for Configuration and Transfers APIs; a distinct Scope.Company credential is used for Legal Entity Management. An online payments API credential is separately requested for simulated test payments. See raw lines 25-37 and 668-674.
- Before issuing cards, account holders undergo verification against their legal entities; the required information depends on where the account holder operates. Create and link legal entities, account holders, and balance accounts. Transfer instruments matter for use cases moving funds between balance and bank accounts, and additional documents may be required. See raw lines 583-603.
- The checklist covers virtual or physical cards. Successful *test* virtual-card creation yields card details for a test payment. It describes suspending a used single-use card as temporary, while closing a card is permanent and irreversible. A balance account needs funds for test payments; an Adyen contact helps fund the liable balance account in test, then the platform may transfer funds to other balance accounts according to its account structure. See raw lines 614-640.
- For authorization decisions, relayed authorisation can return allow/decline through a separate webhook endpoint within 2000 ms; configurable fallback applies when Adyen receives no valid response. Transaction rules can apply to a card, group, or balance platform; if combined with relayed authorisation, rules run first. The sample Checkout `/payments` call uses a distinct online payments credential in test, and its response depends on the approval/decline decision. See raw lines 642-674 and 1007.
- Regular asynchronous webhooks cover payments, captures, refunds and fund transfers, and use a separate endpoint from relayed authorisation. Programmatic report download needs a report credential and the `balancePlatform.report.created` notification before authenticated GET. See raw lines 1009-1031.
- Live issuing requires applying for a live account. Test account configuration does not replicate automatically: account holders, balance accounts, transaction rules and payment instrument groups must be recreated where applicable. Switch to live credentials/endpoints and run the listed end-to-end checks, including both approved and declined payment paths, webhooks, verification errors and reports. These are prescribed checks, not evidence they passed. See raw lines 1033-1077.

## Detail locators

- Credential verification requests, sample responses, and language-specific SDK examples: raw lines 30-582.
- Test Checkout v68 request body and SDK examples: raw lines 668-1007.
- Live Balance Platform endpoint example and checklist: raw lines 1046-1077.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[source-adyen-docs-issuing-get-started]] — design, test account and live application context.

## Raw Sources

- [[raw/adyen/docs/issuing/integration-checklist/2026-09-15|Adyen integration and go-live checklist, captured 2026-09-15]]
