---
title: "Braintree Brazil 3D Secure Processing Requirements"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/transactions/three-d-secure-processing-requirements"
raw_files:
  - "braintree/articles/br/transactions/three-d-secure-processing-requirements-2026-09-16.md"
tags: [braintree, brazil, 3d-secure, visa, mastercard, debit-cards]
---

## Overview

This collected Braintree Brazil article snapshot identifies Visa and Mastercard as the card types to which its processing discussion applies. It separately describes a Brazil-specific Visa debit approval-rate tendency, a Mastercard debit processing requirement, and Braintree's recommendation for debit-card 3D Secure authentication.

Treat this as a 2026-09-16 snapshot of the article (whose metadata records a 2025-04-02 update), not proof of current policy, merchant-account eligibility, payment authorization or approval, liability shift, or requirements for another Braintree account, processor, region, card type or sibling article.

## Key takeaways

- Under `Applicable card types`, the article names Visa and Mastercard. It does not extend the stated processing discussion to other card brands or payment methods.
- For Visa debit cards in Brazil, the article says issuers tend to approve transactions at higher rates when the cards are authenticated with 3D Secure. This is a qualified approval-rate tendency, not a stated Visa mandate or an approval guarantee.
- For Mastercard debit cards, the article says Mastercard has issued a requirement that they be processed using either standard 3D Secure authentication or data-only 3D Secure authentication. The subject is Mastercard debit cards, and the permitted action is one of those two authentication paths.
- Based on the issuer and card-brand statements, Braintree recommends authenticating debit cards with 3D Secure to achieve the highest approval rates. The page frames this as a recommendation; it does not promise approval or state that every Brazil card transaction must use 3D Secure.

> [!warning] Snapshot and outcome boundaries
> Do not generalize the Mastercard debit-card requirement to Visa, credit cards, all Brazil transactions, or another account/processor/region. The page does not establish current merchant eligibility, a liability shift, authorization, settlement, or successful payment execution.

## Detail locators

- Card-type scope: `## Applicable card types`, raw lines 17-23.
- Brazil issuer approval-rate tendency for Visa debit cards: `### Visa debit cards`, raw lines 26-28.
- Mastercard debit-card requirement and the standard-or-data-only authentication alternatives: `### Mastercard debit cards`, raw lines 31-33.
- Braintree recommendation and stated approval-rate purpose: final paragraph under `### Mastercard debit cards`, raw line 35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]

## Raw Sources

- [[raw/braintree/articles/br/transactions/three-d-secure-processing-requirements-2026-09-16|Braintree Brazil 3D Secure Processing Requirements]] - fully read 2026-09-16 snapshot covering Visa and Mastercard debit-card 3D Secure processing guidance
