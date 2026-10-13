---
title: "Adyen Docs: Point-of-sale risk management"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/risk-management-pos"
raw_files:
  - "adyen/docs/point-of-sale/risk-management-pos/2026-09-15.md"
tags: [adyen, point-of-sale, risk-management, moto, manual-key-entry]
---

## Overview

This Adyen POS risk-management guide, fetched 2026-09-15 and marked last modified 2022-12-26 in its raw metadata, describes Customer Area risk rules for riskier in-person-channel MOTO and Manual Key Entry (MKE) transactions. It calls the system “RevenueProtect”; the broader [[adyen-risk-management]] hub uses the newer Protect name. The guide says most ordinary POS transactions have lower fraud risk than ecommerce and most risk rules do not apply. It does not establish current feature availability, account configuration, a fraud outcome, or a rule for every terminal payment. [[adyen]] · [[adyen-risk-management]] · [[adyen-terminal-api]]

## Key takeaways

- For MOTO and MKE, the guide says POS risk rules can be enabled in Customer Area. Under the described settings, transactions receive a 0–100 risk score; at 100, the transaction is declined and the terminal shows **Card blocked**. This is the guide's configured POS risk path, not a claim that every POS payment is scored or declined.
- The guide describes MOTO and MKE payments as insecure, with no liability shift, and places fraud-chargeback liability on the accepting merchant. Its MKE signature description is specific to this entry mode; it does not define cardholder verification or liability for other POS methods.
- POS risk checks may be enabled at company-account scope for all merchant accounts by default or for one merchant account, where the guide requires **Override company setting** first. General Protect enablement and POS checking are distinct toggles in this dated Customer Area walkthrough.
- When enabled, the company default risk profile applies. For a merchant account processing only POS, Adyen recommends a dedicated profile, assigned to the relevant merchant accounts, because ecommerce-oriented defaults can wrongly decline POS traffic. The guide directs disabling three shared-IP/shopper-reference rules; further rule tuning and optional custom rules are in the raw.
- The sample risk refusal has Terminal API `PaymentResponse` `Result=Failure`, `ErrorCondition=Refusal`, and `AdditionalResponse` with `refusalReason=199 Card blocked` and `message=BLOCK_CARD`. Its test-amount example ends in 125, and the guide explicitly says the integration must not retry that refused transaction.

## Detail locators

- **Purpose, risk score and liability:** raw lines 24–28, with MOTO/MKE scope and the guide's dated RevenueProtect name.
- **Enable POS checks:** “Step 1” (lines 30–47), including company versus merchant account scope, POS toggle, and merchant override. These are snapshot UI paths, not proof of present-day account eligibility.
- **Risk profile:** “Step 2” and “Step 3” (lines 49–87). The dedicated POS profile is a recommendation conditioned on POS-only processing; the three listed IP/shopper-reference rules are the guide's required disablements in that profile. Other rules are optional to disable, while Velocity and Consistency remain candidates for POS tuning.
- **Optional rules and data conditions:** “Step 4” (lines 89–103). AVS-based rules are conditional on sending shopper street address and ZIP/postal code; CVC mismatch and velocity rules, plus optional custom rules using additional data such as `shopperEmail`, are described here. Do not treat example data as mandatory for every POS request.
- **Test refusal:** “Testing” (lines 105–143) gives the response shape, the amount-ending-in-125 simulation, and no-retry instruction. The linked simulation page was not read here; the sample does not prove live behavior.

## Related

- [[adyen-risk-management]] — provider risk settings, profiles, and Protect boundary
- [[adyen-terminal-api]] — Terminal API payment response context
- [[source-adyen-docs-point-of-sale-cardholder-verification-methods]] — separate POS cardholder-verification guide

## Related raw API references

Linked MOTO, MKE, POS payment-method/chargeback, risk-rule, AVS, Terminal API response, and test-card pages are navigation only; their contents were not used to expand this source.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/risk-management-pos/2026-09-15|Adyen POS risk-management guide, fetched 2026-09-15]]
