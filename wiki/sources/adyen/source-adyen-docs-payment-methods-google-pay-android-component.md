---
title: "Adyen Google Pay Android Component setup"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/android-component"
raw_files:
  - "adyen/docs/payment-methods/google-pay/android-component/2026-09-15.md"
tags: [adyen, google-pay, android, component, wallets]
---

## Overview

This [[adyen]] guide adds **Google Pay** to an existing Android Components integration, with separate **Sessions** and **Advanced** server-side flows and Compose/non-Compose client examples. It links a migration guide for **5.9.x** but does not make that version a universal minimum in this page. It covers component configuration and test/live preparation, not token decryption, recurring consent, final payment webhooks, capture, or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** An existing Sessions Android Components integration, Checkout API **v69+**, and Google Pay added in Customer Area are stated prerequisites. The page says no extra Google-Pay-specific `/sessions` parameters are needed. It imports the `googlepay` module, plus `components-compose` for Compose, then gets the Google Pay payment method from `checkoutSession` and creates/attaches `GooglePayComponent`. A unique component key is shown for new screens or sessions. See raw lines 25–64 and 122–175.
- **Advanced:** An existing Advanced Android Components integration and Google Pay setup in Customer Area are stated prerequisites. The client selects the Google Pay method from the `/paymentMethods` response and creates/attaches the Component. The page says no extra Google-Pay-specific `/payments` parameters are needed. The Advanced section does **not** restate Sessions' Checkout API v69+ version as its own prerequisite; neither “no extra parameters” statement replaces the main integration's request requirements. See raw lines 216–246 and 304–365.
- Both flows list **optional** Google Pay configuration: allowed auth methods default to `PAN_ONLY` and `CRYPTOGRAM_3DS`, allowed networks derive from account settings but can be overridden, prepaid/billing/shipping/email and button visibility have stated defaults, and `setGooglePayEnvironment` can select Google's TEST or PRODUCTION environment, defaulting to the Adyen environment. These are configuration values, not proof of network eligibility, 3DS outcome, Google token processing, or payment authorization. The snippets include placeholders and an extra brace, so validate them against the applicable SDK before use. See raw lines 66–120 and 248–302.
- In TEST, the page offers Google's test-card suite (FPAN, Android/Chrome-on-Android DPAN, 3DS2 scenarios) or a wallet with real cards mapped to Adyen test cards of the same brand; it says the real card is not charged in that test route. For 3DS2 **without** the test suite, it names American Express or Discover only. These are test-fixture claims, not evidence of a completed payment. See raw lines 177–201 and 367–391.
- Before LIVE, the guide calls for an API credential with **API Clientside Encryption Payments role**, a configured **Google Merchant ID** in live Customer Area, and completion of Google's Android production-deployment steps; testing live scenarios is recommended. It says Google Pay is available in LIVE only when the shopper is logged in and has a valid method in their Google Pay account. These are necessary conditions in this snapshot, not sufficient merchant approval or actual processing proof. See raw lines 203–214 and 393–404.

## Detail locators

- 5.9.x migration-guide link and flow split: raw lines 17–25.
- Sessions dependency, optional configuration and component examples: raw lines 29–175.
- Advanced dependency, optional configuration and component examples: raw lines 216–365.
- TEST scenarios and LIVE checklist repeated by flow: raw lines 177–214 and 367–404.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/android-component/2026-09-15|Adyen Google Pay Android Component snapshot]]
