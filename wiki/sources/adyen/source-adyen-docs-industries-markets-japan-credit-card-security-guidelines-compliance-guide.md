---
title: "Adyen Japan Credit Card Security Guidelines 5.0 guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/markets/japan/credit-card-security-guidelines-compliance-guide"
raw_files:
  - "adyen/docs/industries/markets/japan/credit-card-security-guidelines-compliance-guide/2026-09-15.md"
tags: [adyen, japan, credit-card-security, 3d-secure, sca]
---

## Overview

This 2023-02-21-last-modified, 2026-09-15-captured Adyen guide interprets **Japan Credit Card Security Guidelines 5.0** for online credit cards processed over **Japan acquiring connections**, citing an **April 1, 2025** effective date. It describes 3D Secure 2 routing, out-of-scope and recurring-transaction conditions, and separate in-person cardholder-verification changes. The page explicitly says it is not legal advice and supplements domestic authority, scheme and EMVCo material. Treat all scope and compliance statements as dated provider guidance; see [[adyen-3d-secure]] and [[adyen]].

## Key takeaways

- **Scope and actor:** The guide frames in-scope online credit-card transactions over Japan acquiring connections as requiring 3D Secure 2, including cards issued outside Japan. Its broad “all online” language is qualified by the page's out-of-scope list and risk-based CardOnFile conditions. This is not a universal requirement for every card type, market or payment channel, nor evidence that a particular merchant or transaction complied.
- **In-person path differs:** It says PIN bypass and signature cease to be valid verification routes for applicable in-person integrations, while asserting Adyen in-person integrations need no merchant action. That assertion belongs to this historical provider snapshot; it does not certify a merchant's terminal configuration or current compliance.
- **Recurring and out-of-scope distinctions:** The guide distinguishes initial Ecommerce CardOnFile/Subscription/UnscheduledCardOnFile use from later ContAuth transactions. Later Subscription/UnscheduledCardOnFile SCA is shown as required on changed shopper-agreement terms; CardOnFile risk decisions depend on zero-value versus nonzero, prior authenticated token, Adyen tokenization, token date and risk. Its out-of-scope list includes prepaid/debit, MOTO, certain recurring, separate B2B/employee environments, unsupported-3DS devices and Google Pay/Apple Pay. These classifications are source claims requiring current and transaction-specific verification, not blanket exemptions.
- **Routing controls and responsibility:** With Adyen 3DS2 integration, the guide says the Authentication Engine applies 3DS2 to in-scope transactions. For default handling it asks for Dynamic 3D Secure **Prefer Not** and avoidance of request flags that block 3DS: `authenticationData.attemptAuthentication: never` on Checkout API v69+ or `executeThreeD: false` on v68 or earlier. It also permits Dynamic rules or per-request preferences but warns that the latter override default routing and may cause non-compliance. When Adyen 3DS2 is not implemented, this dated guide makes the merchant responsible for ensuring the relevant in-scope online credit-card payments over Japan acquiring connections are authenticated with 3DS2 and for sending third-party authentication data in the payment request; its out-of-scope qualifications still apply. Authentication routing alone does not establish successful authentication, financial authorization, liability shift, PCI DSS status or legal compliance.

## Detail locators

- Lines 15–25: Japan-acquiring effective date, provider non-legal-advice boundary and supplemental authorities.
- `## Credit Card Security Guidelines 5.0`, lines 27–44: online credit-card/3DS2 framing and in-person PIN/signature claims.
- `## In-scope transactions`, lines 46–95: Authentication Engine and initial/later recurring/risk-based conditions.
- `## Out-of-scope transactions`, lines 97–108: enumerated exclusions and Adyen routing claim.
- `## Implement 3D Secure 2 with Adyen`, lines 110–141: Adyen versus third-party authentication responsibility, integration routes, default/Dynamic/API preference controls and versioned flags.

## Related

- [[adyen-3d-secure]] — 3DS2 integration and regional regulation route.
- [[adyen-psd2-sca-and-3d-secure]] — separate PSD2 regulatory scope.
- [[adyen-pci-dss-compliance]] — separate PCI DSS obligations; this guide does not establish PCI compliance.
- [[source-adyen-docs-online-payments-3d-secure-for-regulation-compliance]] — regional rule overview.

## Raw Sources

- [[raw/adyen/docs/industries/markets/japan/credit-card-security-guidelines-compliance-guide/2026-09-15|Japan Credit Card Security Guidelines guide, captured 2026-09-15]]
