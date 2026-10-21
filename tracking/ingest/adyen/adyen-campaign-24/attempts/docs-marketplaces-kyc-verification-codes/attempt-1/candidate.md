---
title: "Adyen Marketplace-path verification codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/kyc-verification-codes"
raw_files:
  - "adyen/docs/marketplaces/kyc-verification-codes/2026-09-15.md"
tags: [adyen, marketplaces, platforms, issuing, kyc, verification-codes]
---

## Overview

This 2021-modified, 2026-09-15-captured Marketplace-path guide explains verification errors and remediating codes found in account-holder capability `problems` in API responses or webhooks. Its stated integration scope is Adyen for Platforms or Adyen Issuing; the Marketplace URL alone does not make it a Classic Platforms API guide. It describes how to inspect codes and routes to three separate catalogs, not proof that a legal entity is verified or that a suggested action succeeded. See [[adyen]] and [[adyen-platforms]] for provider and current-platform context.

## Key takeaways

- Three distinct layers serve different purposes: a general error code broadly describes the failed check; a linked suberror identifies a more specific cause; a remediating-action code offers a possible solution. Adyen says it sends an action for every error whenever possible, not invariably. Use the suberror codes to design verification-error handling or test scenarios.
- To view codes by API request, the page requires a Configuration API web-service credential; to view them in Customer Area, it requires the **Manage account holder capabilities** role. The Customer Area account-holder **Capabilities** tab shows enabled, allowed and verification-status information. API inspection uses GET `/accountHolders/{id}`; `balancePlatform.accountHolder.created` and `.updated` webhooks are another route. Account-holder ID/reference and linked legal-entity ID are search keys, not the same object.
- For API-only onboarding, the guide recommends choosing error flows that fit the use case and development resources and building for all possible verification codes to provide accurate user feedback. This is a design recommendation, not a guarantee that every error has a remediating action or that remediation approves a capability.
- In the `problems` array, `entity.id` identifies the legal entity with the error. Each `verificationErrors` entry has type (`invalidInput` or `dataMissing`), general code/message, possibly common `remediatingActions`, and `subErrors` with their own type/code/message/actions. The prose calls common `remediatingActions` an object, but the sample shows an array; this snapshot does not settle the field's runtime shape. Check the applicable API schema or observed payload before parsing.
- The sample's general `1_30`, suberrors `1_3001` and `1_3000`, nested actions `1_300` and `1_301`, and `verificationStatus: invalid` illustrate distinct code roles and one outcome. The linked remediating-action, general-error and suberror catalogs own the full code lookups. The sample does not show approval after remediation.

## Detail locators

- Purpose, three code layers, possible-action qualifier and prerequisites: raw lines 15–35. Customer Area and Configuration API/webhook inspection routes: lines 37–61.
- API-only recommendation and problems-array field description: lines 63–81. Example payload, including common-action prose/example shape mismatch and `verificationStatus`: lines 83–144. Detailed catalog and test routes: lines 146–164.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — Platforms and Marketplace integration context.
- [[source-adyen-docs-marketplaces-kyc-verification-codes-remediating-actions]] — Marketplace-path action-code lookup.
- [[source-adyen-docs-marketplaces-kyc-verification-codes-general-verification-errors]] — Marketplace-path general error-code lookup.
- [[source-adyen-docs-marketplaces-kyc-verification-codes-sub-errors]] — Marketplace-path specific suberror lookup.
- [[source-adyen-docs-platforms-kyc-verification-codes]] — separately pinned Platforms-path overview.

## Related raw API references

- The raw page links to Configuration API account-holder responses, account-holder webhooks and verification testing; their live schema and behavior require separate authority.

## Raw Sources

- [[raw/adyen/docs/marketplaces/kyc-verification-codes/2026-09-15|Adyen Docs: Verification codes (2026-09-15 snapshot; page last modified 2021-01-19)]]
