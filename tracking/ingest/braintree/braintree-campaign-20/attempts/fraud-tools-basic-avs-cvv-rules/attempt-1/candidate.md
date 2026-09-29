---
title: "Braintree AVS and CVV Rules"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules"
raw_files:
  - "braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16.md"
tags: [braintree, fraud-tools, avs, cvv, gateway-rejections]
---

## Overview

This collected Braintree guide documents customizable Address Verification System (AVS) and Card Verification Value (CVV) rules within Basic Fraud Tools for credit-card transaction and verification requests. It explains how issuing-bank match results feed merchant-configured gateway rules; those rule checks and their gateway-rejection outcomes are distinct from the processor authorization that precedes them.

## Key takeaways

- The page limits AVS and CVV rules to credit cards. AVS checks numeric address values, while CVV checks the submitted security value against the issuer's records.
- For a new card transaction or verification, Braintree sends the submitted address and CVV data to the card-issuing bank. If that bank approves, its response includes match codes; an enabled AVS or CVV rule can then cause Braintree to reject the request and send a void request. Some banks do not recognize void requests immediately, so the rule outcome is not the same thing as processor authorization or immediate removal of an authorization.
- Rule criteria are selected in the Control Panel under **Fraud Management**. Any enabled-rule violation can reject a transaction; AVS may instead require both postal-code and street-address violations, and rules can be scoped to all transactions or selected card types, amounts, or merchant accounts.
- By default, these rules apply only to first-time transactions, not recurring payments or transactions using cards stored in the Vault. Verifying a card before vaulting requires Control Panel card verification, and CVV must be collected again because Braintree says it never stores CVVs.
- Default AVS geographic scope is limited to requests with a US billing address or no stated country of origin. Global AVS can increase declines where issuers do not consistently support AVS; the page names three rejection reasons it recommends leaving unselected for that setup.

## Rule and outcome boundaries

The raw guide contains the exact enablement procedure, recommended setup guidance, Drop-in field behavior, Vault re-verification behavior, international postal-code limitations, Maestro/CVV warning, and per-request API skip routes. Use the locators below for those details rather than treating AVS/CVV matching as a general authorization, identity, fraud-prevention, chargeback-protection, liability-shift, settlement, or funding guarantee.

## Detail locators

- Credit-card-only availability and stated Basic Fraud Tools purpose: `# AVS and CVV Rules`, lines 17-22.
- Issuer approval, response-code meaning, rule-triggered gateway rejection, void request and delayed bank recognition: `## How AVS and CVV rules work`, lines 25-29.
- Control Panel configuration, combined-AVS option, transaction scoping and Drop-in field behavior: `## Enabling AVS and CVV rules`, lines 32-51.
- CVV collection and false-rejection guidance: `## Recommended setup options`, lines 56-60.
- First-time/Vault defaults, re-verification and CVV non-retention: `### AVS and CVV rules in the Vault`, lines 63-71.
- Country Scope, issuer-support warning, skip route and alphanumeric-postal-code limitation: `#### International AVS` through `#### International postal codes`, lines 76-102.
- Maestro/CVV consequence: `## Maestro cards and CVV rules`, lines 105-107.
- Selective API skip routes: `## Overriding rejections`, lines 110-112.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Supporting concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/docs/reference/general/processor-responses/avs-cvv-responses-2026-09-16|Braintree AVS and CVV Response Codes]] - navigation-only reference linked by this guide for the individual response-code categories; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|Braintree AVS and CVV Rules guide]] - complete collected page covering credit-card availability, issuer checks, merchant rule configuration, gateway-rejection outcomes, Vault and international boundaries, and override routes
