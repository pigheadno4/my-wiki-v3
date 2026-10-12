---
title: "Adyen Tokenization"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/tokenization"
raw_files:
  - "adyen/docs/online-payments/tokenization/2026-09-15.md"
tags: [adyen, tokenization, recurring-payments, stored-payment-methods, pci-dss]
---

## Overview

This Adyen guide introduces tokenization for recurring payments. The 2026-09-15 snapshot calls Tokenize an Adyen Uplift module. With shopper consent, Adyen stores payment details in the Adyen Vault and the merchant later pays with a token representing those details. The page presents tokenization as a way to reduce exposure to sensitive payment data and PCI DSS scope; it does not establish current product packaging, merchant eligibility, enablement, or successful payment execution.

## Key takeaways

- Adyen documents two server-side implementation routes. Sessions creates a secure session for client-side components and is described as qualifying for SAQ A; Advanced gives the merchant more checkout control but requires the merchant to manage data flow and state.
- The documented recurring types are shopper-present one-click payments, regular merchant-initiated subscriptions, and automatic top-ups or other non-fixed schedule contracts. With Sessions, shopper-not-present token payments such as subscriptions still require a separate `/payments` call.
- Every stored token must be associated with a shopper reference that is unique to that shopper. Shopper references and tokens are merchant-account-scoped by default; sharing them across merchant accounts requires the separately enabled Token Groups feature.
- The guide says collecting raw card data requires full PCI DSS compliance. Using tokens can reduce PCI scope, but the snapshot is not a substitute for a merchant's current compliance assessment.
- The page routes readers to payment-method-specific recurring support and to separate guides for network tokens, Account Updater, forwarding stored details, creating tokens, and making token payments. Those linked pages were not read for this entry and provide navigation rather than evidence for their detailed behavior.

## Material qualifications

- Shopper consent is a condition for saving payment details.
- Creating a token and making a later payment are distinct actions; Sessions alone is not documented as executing shopper-not-present subscription or unscheduled payments.
- Token Groups is not the default scope and requires Support to enable it.
- This is a 2026-09-15 documentation snapshot. Product packaging, supported payment methods, account eligibility, compliance status, and runtime outcomes require current, merchant-specific verification.

## Detail locators

- Definition, shopper consent, Vault storage, token use, the snapshot's Adyen Uplift module classification, and PCI-scope purpose: opening paragraphs, raw lines 26-35.
- Sessions and Advanced server-side flow boundaries: `## Implementation options`, raw lines 37-43.
- One-click, subscription, and non-fixed schedule types plus the Sessions `/payments` qualification: `## Recurring payment types`, raw lines 45-60.
- Payment-method support navigation: `## Supported payment methods`, raw lines 62-66.
- Unique shopper reference, default merchant-account scope, and Token Groups enablement: `## Shopper reference management`, raw lines 68-72.
- Encryption and raw-card PCI DSS boundary: `## Security and compliance`, raw lines 74-80.
- Network tokenization, Account Updater, and Forward navigation: `## Enhance your tokenization implementation`, raw lines 82-106.
- Create-token and make-token-payment navigation: `## Next steps`, raw lines 108-120.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]
- Cross-cutting concept: [[recurring-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/tokenization/2026-09-15|Adyen Tokenization documentation snapshot]] - complete collected guide covering definition, implementation routes, recurring types, shopper-reference scope, security boundaries, enhancement navigation, and next steps
