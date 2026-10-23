---
title: "Adyen Apple Pay web with your own certificate (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/apple-pay-certificate/web"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/apple-pay-certificate/web/2026-09-15.md"
tags: [adyen, apple-pay, web, certificates, historical]
---

## Overview

This [[adyen]] page, last modified **2023-11-24** and captured 2026-09-15, describes enabling Apple Pay on a website **with the merchant's own Apple Pay certificates**. Its stated integration prerequisite is Web Drop-in/Components using the Advanced or Sessions flow, plus a Customer Area user with Merchant admin or Manage API Credentials role and an Apple Developer Program or Enterprise Program account (raw lines 21–31). It is a historical setup guide under [[adyen-online-payments]], not evidence of current eligibility, a deployed certificate or an authorized payment.

## Key takeaways

- The guide calls for separate Apple merchant identifiers for **test** and **live** transactions, although the same identifier may serve multiple websites and iOS apps (raw lines 35–49). It selects the web service user that will execute Apple Pay transactions in Adyen Customer Area and uses its CSR to create a payment processing certificate for each identifier. The processing certificate encrypts payment information for Adyen to decrypt and process; the resulting certificate is uploaded against the corresponding identifier/user (raw lines 35–38, 58–84).
- For ordinary web setup, the merchant also registers and validates its domain with Apple, creates a distinct **merchant identity certificate**, converts it to PEM and places it on the merchant server. That certificate authenticates communication when requesting an Apple Pay payment session for each transaction; the **Adyen-issued CSR for processing cannot be reused** for this identity certificate (raw lines 39–43, 158–194). Both the domain-registration and merchant-identity-certificate steps explicitly **do not apply to the Salesforce Commerce Cloud plugin**; the page routes plugin users to separate documentation (raw lines 158–170).
- The processing-certificate renewal creates an overlap: Apple may still use the old certificate during activation and for about **four hours afterward** (raw lines 86–112). The page describes matching the decoded `paymentMethod.applePayToken.header.publicKeyHash` to the Customer Area `KeyID` to identify the certificate used for a payment; an old `KeyID` during rollout alone does not mean setup failed. A new `KeyID` on an **authorized** payment is its verification signal (raw lines 114–154). The page then gives an old-certificate removal control (raw line 156); this is a source procedure, not a completed rotation or authorization claim.
- Adding Apple Pay in Customer Area is a separate step using merchant name/account and the created merchant identifier (raw lines 196–201). Its example token and certificate command are illustrative; this page does not establish current account activation, safe handling of private keys, or payment capture/settlement.

## Detail locators

- Requirements and setup role/account prerequisites: raw lines 21–31.
- Merchant identifiers, TEST/LIVE split, Adyen web-service-user CSR and payment processing certificate: raw lines 33–84.
- Certificate renewal, overlap, token-header `KeyID` check and removal: raw lines 86–156.
- Domain registration and Salesforce exception: raw lines 158–166.
- Merchant identity certificate, distinct CSR, PEM/server path and Salesforce exception: raw lines 168–194.
- Customer Area payment-method addition: raw lines 196–201.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/web/2026-09-15|Full pinned Apple Pay web certificate guide]]
