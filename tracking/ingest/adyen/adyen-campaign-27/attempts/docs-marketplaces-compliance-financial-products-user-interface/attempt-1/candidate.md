---
title: "Marketplace financial-products user application and interface"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/compliance-financial-products/user-interface"
raw_files:
  - "adyen/docs/marketplaces/compliance-financial-products/user-interface/2026-09-15.md"
tags: [adyen, marketplaces, financial-products, compliance, user-interface]
---

## Overview

This Marketplace financial-products UI page, last modified 2023-12-12 and captured 2026-09-15, states Adyen's interface and customer-disclosure guidelines. It expressly says it is **not legal advice**. These dated guidelines do not establish current law, product availability, Adyen approval, collected consent, or completed financial operations. See [[adyen]] and [[adyen-financial-products]] (raw lines 5–19).

## Key takeaways

- The platform UI is to let users request financial services that the marketplace has agreed with Adyen to offer, provide required KYC data, present agreements, bank disclosures, fees and terms, obtain user acceptance, and preserve access to accepted agreements. Hosted onboarding places KYC fields, agreements and terms on Adyen's hosted flow; Adyen components may embed some requirements. The UI should give free ongoing access to applicable Balance/Bank Account, Capital or Issuing account and transaction information supplied through Adyen APIs (raw lines 21–35).
- The UI must not preselect acknowledgement options or present the marketplace as a bank; it should identify Adyen as financial-services provider. The page specifies Ireland-only provider wording for all products. Exact consent/provider text belongs to the raw source (raw lines 29–43).
- Product-specific terms and displays differ: payment processing is **UK only** in these tables; Business accounts, Issuing and Capital have separate terms and account/transaction or financing information. EU Business accounts require a Depositor Information Sheet before offering and annually thereafter, plus confirmation of acceptance. For payments using an Adyen bank account, the EU/UK payee verification/confirmation section describes distinct match, partial-match, no-match and unsupported notices with user choices (raw lines 45–82).
- Conditional country/product UI details include UK Business Accounts enabled for BACS Direct Debits (mandate visibility, notification, immediate cancellation/amendment, transaction overview and refund request/claim routing), US Business accounts (FDIC wording and internet-gambling certification), US Capital/Charge Card disclosures and declined-request notification, Canada Capital fee display, and Ireland Capital precontract disclosures and affirmative consent. The UI path to request a refund or manage a mandate is not proof that the underlying operation completed (raw lines 84–150).
- The attached customer-disclosure and consent procedure distinguishes mandatory disclosure from freely given, informed and specific consent; it says only an Authorized Signatory natural person can consent to Adyen, requirements depend on service line, and evidence of remote consent through onboarding forms or APIs must be retained. It does not prove that a given signatory was verified or consented (raw lines 152–186).

## Detail locators

- General UI, hosted onboarding/components, acceptance, account access and provider disclosure: raw lines 19–43.
- Product terms and UI matrix, including EU/UK/US Business accounts and UK BACS details: raw lines 45–122.
- Issuing and Capital requirements by product and country: raw lines 123–150.
- Disclosure/consent procedure, authorized signatory and evidence retention: raw lines 152–186.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-marketplaces-compliance-financial-products]]
- [[source-adyen-docs-platforms-compliance-financial-products-user-interface]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/compliance-financial-products/user-interface/2026-09-15|Pinned Marketplace UI guidelines]]
