---
title: "Adyen Issuing: reference for additional capabilities"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-requirements/reference-additional-products"
raw_files:
  - "adyen/docs/issuing/verification-requirements/reference-additional-products/2026-09-15.md"
tags: [adyen, issuing, verification, source-of-funds]
---

## Overview

This 2026-09-15 Adyen Issuing-path reference covers industry-code values and source-of-funds information for business lines, including onboarding v4. Its “Requirements” section says an Issuing integration has no additional requirements, limitations or preparations, yet its source-of-funds section explicitly says source-of-funds verification applies to card issuing as well as Business Accounts. Treat that as a source-internal scope tension; the page is not proof that a particular program or user is currently eligible or verified. [[adyen]] [[adyen-issuing]]

## Key takeaways

- For **business-account requests**, the page says industry codes representing a user's line of business are required; some industries need Adyen approval before onboarding. It directs a `POST /businessLines` with the most representative code and links separate general and brand-specific code lists. The page does not state this industry-code requirement as a universal Issuing prerequisite.
- The source-of-funds section expressly applies to **card issuing and Business Accounts**. It says to submit a `POST /businessLines` with `service: issuing` for card issuing or `service: banking` for Business Accounts. Adyen may ask for supporting documents depending on fund type; the table's document and date requirements apply **if requested**.
- The prose says set `sourceOfFunds.adyenProcessedFunds` true when funds were processed through Adyen, otherwise false and provide `sourceOfFunds.type` and `sourceOfFunds.description` stating the origin. A table row instead labels the Adyen-processed flag `businessLines.adyenProcessedFunds`. This path difference is unresolved in the snapshot; check the applicable API schema before implementing the request.
- The table lists business earnings, employment, cryptocurrency, dividends, loans, grants, third-party funding, asset sales, rent, gifts, royalties, gambling winnings, inheritance, pension and insurance/settlement, with category-specific required information, example documents and recency conditions. Its Adyen-processed business-earnings row says no supporting document is required; do not generalize that to other sources or bypass separate verification.

## Detail locators

- Raw lines 19–23 contain the onboarding-v4 pointer and the Issuing “no additional requirements” statement.
- Raw lines 25–38 describe industry-code collection for business-account requests, approval caveat, list links and `POST /businessLines`.
- Raw lines 40–55 state the card-issuing/Business Accounts source-of-funds scope, service values, processed-funds field prose and conditional document rule.
- Raw lines 57–146 contain source-of-funds categories, API values, information and conditional supporting-document examples; line 59 has the conflicting field path and no-document row.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-requirements/reference-additional-products/2026-09-15|Adyen additional-capabilities reference, captured 2026-09-15]]
