---
title: "Adyen GCash online payments overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash"
raw_files:
  - "adyen/docs/payment-methods/gcash/2026-09-15.md"
tags: [adyen, gcash, philippines, wallet, redirect]
---

## Overview

This [[adyen]] GCash overview describes a **Philippines (PH), Philippine peso (PHP)** wallet **redirect** method for online payments, with separate shopper sketches for a one-time purchase and a recurring transaction. It provides a capability matrix and links to channel-specific integration guides. These are a 2026-09-15 website snapshot of documented support, not proof of current merchant eligibility, consented recurring setup, completed authorization, capture, settlement or refund. [[adyen-online-payments]]

## Key takeaways

- **One-time shopper path:** After GCash selection on a website or mobile app, the described shopper is redirected to GCash, logs in with a mobile number, authenticates using an SMS one-time password and four-digit MPIN, confirms, returns to the merchant site/app and receives an SMS. The return and SMS are described shopper steps, not a final payment-status contract. See raw lines 25–37.
- **Recurring shopper paths:** The page says GCash can be used for recurring transactions. For a website selection it describes a QR-code scan with the GCash app followed by return/SMS; for a mobile-app selection it describes a GCash website login, SMS OTP and MPIN, confirmation, return/SMS. It does not state the token, mandate, consent, server-request or webhook mechanics; those require the relevant child guide. See raw lines 27 and 39–54.
- **Expiry and capability scope:** The GCash redirect page is valid for **30 minutes by default** and then times out; changing the link expiry is a Support request. The PH/PHP matrix marks recurring, refunds, partial refunds and multiple partial refunds available, while marking separate/partial/multiple-partial captures and chargebacks unavailable. Matrix marks are method-level snapshot claims, not a promise that a particular merchant or transaction qualifies. See raw lines 56–60.
- **Integration navigation:** The page routes to Web, iOS, Android, React Native, Flutter, API-only and Pay by Link guides. The API-only label describes building one's own UI for website/iOS/Android, but this overview supplies no endpoint fields or SDK/API versions. See raw lines 62–104.

## Detail locators

- GCash background and one-time/recurring shopper steps: raw lines 21–54.
- Redirect lifetime and PH/PHP capability matrix: raw lines 56–60.
- Channel and API-only child links: raw lines 62–104.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/2026-09-15|Adyen GCash overview snapshot]]
