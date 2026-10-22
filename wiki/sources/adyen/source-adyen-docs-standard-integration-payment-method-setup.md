---
title: "Adyen Standard integration payment-method setup"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/payment-method-setup"
raw_files:
  - "adyen/docs/standard/integration/payment-method-setup/2026-09-15.md"
tags: [adyen, standard-integration, online-payments, payment-methods, setup]
---

## Overview

This Standard integration page (modified and captured 2026-09-15) lists payment-method families and **extra setup for selected methods**. It says most Adyen methods can be used without additional setup but identifies exceptions. Its list and steps are a dated documentation snapshot, not evidence that a method is enabled for a merchant, store, shopper, country, session or live account. The page does not define Sessions filtering or method-return rules. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Apple Pay has two certificate paths:** The guide requires allowing Apple Pay IP addresses and either Adyen's certificate or the merchant's own. The Adyen-certificate path requires secure HTTPS pages, valid SSL and Customer Area merchant name and shop websites; `http://localhost` is excluded for the listed website test setup. The own-certificate path adds an Apple Developer account, merchant identifier, payment-processing certificate and merchant-domain registration; its merchant-identity certificate is used to request an Apple Pay payment session and its CSR must be created separately from Adyen's payment-processing CSR. These are setup instructions, not proof of merchant validation or payment success.
- **PayPal permission and other activation gates:** PayPal setup uses developer and sandbox business/personal accounts, Customer Area addition and an emailed activation link to permit Adyen to process the sandbox business account's PayPal transactions. Fastlane by PayPal has a separate sandbox business-account activation route. Bizum needs a local supported acquirer contract plus MID/Terminal ID and acquirer connection to Adyen. Several named methods (DuitNow, Open Banking, both Pay by Bank regions, PayPay, PromptPay, Touch 'n Go and Walley) route through Support for Customer Area addition. Google Pay directs to Google's setup documentation. These conditions are method-specific; a family listed at the top is not a blanket availability promise.
- **Other product and commercial qualifications:** Bancontact mobile asks for **3DS2 Additional Fields** in Customer Area. The page labels its MobilePay steps as **payouts** with Support approval and recurring-token lifecycle webhooks; do not silently recast those steps as an ordinary shopper-payment method. Riverty and Scalapay warn that activation defaults to standard pricing and point to an account manager to check Enterprise pricing eligibility. Titres Restaurant needs an authorization/CONECS MID and separate issuer contracts. The exact list and setup conditions are at the raw locators below.
- **Scope boundary:** This page specifies some payment-method setup requirements, not merchant/store-level entitlement, method selection in a particular `/sessions` response, or a guaranteed authorization/capture/settlement result. Those questions require the relevant method and integration guides plus actual configured account evidence.

## Detail locators

- Supported method families, “most” statement and setup-exception list: pinned raw lines 15-49.
- Apple Pay certificate, domain, HTTPS and merchant-session setup paths: pinned raw lines 50-143.
- Bancontact mobile, Bizum, DuitNow, Fastlane, Google Pay, MobilePay, Open Banking and Pay by Bank: pinned raw lines 145-193.
- PayPal, PayPay, PromptPay, Riverty, Scalapay, Titres Restaurant, Touch 'n Go and Walley: pinned raw lines 195-233.

## Related

- [[adyen-online-payments]] — main online-payment concept and reciprocal source route.
- [[source-adyen-docs-standard]] — Standard integration checklist.

## Raw Sources

- [[raw/adyen/docs/standard/integration/payment-method-setup/2026-09-15|Standard integration payment-method setup, captured 2026-09-15]]
