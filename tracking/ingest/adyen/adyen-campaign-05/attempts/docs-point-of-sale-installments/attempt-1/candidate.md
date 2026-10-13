---
title: "Adyen POS installments regional overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/installments"
raw_files:
  - "adyen/docs/point-of-sale/installments/2026-09-15.md"
tags: [adyen, point-of-sale, installments, credit-card-payments, brazil, japan, mexico]
---

## Overview

This Adyen Docs page is a short navigation overview for credit-card installment payments on payment terminals. It describes shoppers receiving goods or services immediately while spreading card charges over monthly payments, notes regional flow differences, and routes to Brazil, Japan, and Mexico guides. See [[adyen]] and [[adyen-terminal-api]] for provider and POS context. The overview does not establish current program eligibility, a Terminal API request contract, issuer/merchant debt ownership, merchant payout timing, interest, fees, liability, settlement, or a completed payment.

## Key takeaways

- The page's general description says installment charges reach the shopper's credit card every 30 days until the purchase is paid. It is a high-level description, not the binding schedule or terms for every issuer, card, country, or merchant.
- Regional flows differ. The page uses Brazil and Mexico as examples where a dual debit/credit card can require a choice of debit versus credit before an installment purchase. For Japan it mentions installment-type selection, with revolving payment as an example involving an initial partial payment and later installments. These are examples, not a universal checkout or finance model.
- The Brazil, Japan, and Mexico links are country-specific next steps; the overview itself supplies no detailed setup, available terms, rates, authorization/capture behavior, customer disclosure, or current legal requirements. Read each linked guide before adopting a country-specific claim or implementation.

## Detail locators

- Credit-card installment purpose and general monthly-card-charge description: `# Installments`, raw lines 15–19.
- Brazil/Mexico debit-credit choice and Japan revolving example: `# Installments`, raw line 21.
- Country-specific guide links and descriptions: `## Select your country/region of business`, raw lines 23–35.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person terminal payment concept; versioned GitHub payment examples are separate evidence.

## Related raw API references

- The raw page links to Brazil, Japan, and Mexico installment guides. They are navigation until independently read; see raw lines 23–35.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/installments/2026-09-15|Adyen Docs: Installments (2026-09-15 snapshot)]]
