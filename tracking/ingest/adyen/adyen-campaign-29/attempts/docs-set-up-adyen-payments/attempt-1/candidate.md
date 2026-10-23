---
title: "Set up for Adyen payments"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/set-up-adyen-payments"
raw_files:
  - "adyen/docs/set-up-adyen-payments/2026-09-15.md"
tags: [adyen, payments, account-setup, test-account, go-live]
---

## Overview

This 2024-modified, 2026-09-15-captured [[adyen]] setup overview gives an ordered route from a **test account**, through selecting and building an integration, to a reviewed **live-account application**, contract and live configuration. It spans online, in-person, Adyen for Platforms and plugin paths rather than prescribing one implementation. See [[adyen-payments]] for the payment-family route. This navigation page does not prove account approval, live activation or a successful payment. [Raw: lines 15–17, 19–108]

## Key takeaways

- The guide starts with a free test account and access to the **test Customer Area** for test payments, team invitations, a live application and integration work. It expressly says a test account does **not guarantee** the ability to process live payments. For live payments, the page directs a business to the prohibited/restricted-products list and Sales contact if eligible; those are dated provider steps, not a current eligibility decision. [Raw: lines 19–36]
- Build against the test account while the live application can also begin. The guide notes that a business **may want to wait for application approval** before building the whole integration. Its integration choices are online web/mobile, in-person POS, Adyen for Platforms, and plugins for existing commerce systems. These links are routes to child documentation; they do not certify any chosen channel's setup or availability. [Raw: lines 38–66]
- For a live application, the page says Adyen as payment provider/acquirer performs detailed checks. It directs the applicant to review restricted products/services, contact Sales if eligible, review live-account requirements, and work through an Adyen contact. Approval is conditional; if approved, Adyen sends a contract and, **if the integration uses card payments**, a data-security attestation form. The page then says live Customer Area access follows receipt of the signed contract and completed form. This is not proof of PCI compliance for a merchant. [Raw: lines 68–84]
- Before accepting live payments, the live account must be configured: **test-account settings are not copied to live**. Separate online and in-person go-live checklists are linked, with a Platforms route. Access to live Customer Area or a checklist link alone is not evidence that payment methods, credentials, risk rules, terminals or webhooks were configured or that any live authorization, capture or settlement occurred. [Raw: lines 86–108]

## Detail locators

- Test account and explicit live-payment caveat: raw lines 19–36.
- Concurrent build/application choice and channel routes: raw lines 38–66.
- Live eligibility checks, Adyen contact, approval, contract and card attestation: raw lines 68–84.
- Separate live configuration and checklist routes: raw lines 86–108.

## Related

- [[adyen-payments]] — top-level payment-family concept
- [[adyen-account-structure]] — account structure context
- [[adyen-online-payments]] — online integration route
- [[adyen-platforms]] — platform route
- [[source-adyen-docs-payments]] — top-level payment directory

## Raw Sources

- [[raw/adyen/docs/set-up-adyen-payments/2026-09-15|Pinned Adyen payment setup overview]]
