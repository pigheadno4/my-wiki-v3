---
title: "Braintree Google Pay Testing and Go Live for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/testing-go-live/android/v5"
raw_files:
  - "braintree/docs/guides/google-pay/testing-go-live/android/v5-2026-09-16.md"
tags: [braintree, google-pay, android, testing, sandbox, production]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] Android v5 guide describes Google Pay sandbox testing and the separate steps for enabling a production Braintree account and obtaining Google Payment API production access. It is not evidence of current SDK support, merchant or device eligibility, account enablement, Google review approval, runtime behavior, or successful payment execution. See [[braintree-android-sdk]].

## Key takeaways

- To test the entire Android user flow, the page says the user must have at least one card or PayPal account stored in Google Pay or the Google account, while also allowing a payment method to be added during checkout if none is present.
- In the Braintree sandbox, Google Pay returns testing nonces representing a test virtual account number or PayPal account. The page routes simulated server outcomes to separate test-amount and test-nonce references. It says completed Google Pay transactions appear immediately in the Braintree gateway, while PayPal-through-Google-Pay transactions appear as PayPal transactions; the sandbox `payer_email` differs from the PayPal account email, whereas the page says production matches it.
- Going live requires enabling Google Pay in the production Braintree Control Panel, then following Google's separate production-access and app-review process. If Google Pay is already active but must be enabled for a particular merchant account, the page directs the merchant to contact Braintree. These instructions do not prove either enablement or review completion.

> [!warning] Historical certificate notice
> The captured page states that Braintree Mobile iOS and Android SDK certificates expire on March 30, 2026, directs Android upgrades to `4.45.0+` or `5.0.0+`, and warns that all customer traffic will fail if affected older app versions are neither decommissioned nor force-upgraded by that date. The notice predates the 2026-09-16 fetch and is retained as historical page wording, not current certificate status, exact package compatibility, runtime behavior, or traffic evidence.

## Detail locators

- Mobile SDK certificate warning and Android version thresholds: raw lines 17–18.
- Android full-flow user payment-method condition: raw line 22.
- Sandbox testing nonces, test-amount/test-nonce navigation, gateway classification, and `payer_email` difference: raw line 24.
- Production Control Panel enablement procedure: `## Go live`, raw lines 27–36.
- Separate Google production-access/app-review route and merchant-account-specific enablement route: raw lines 38–40.

## Related

- [[braintree-android-sdk]]
- [[braintree]]

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/testing-go-live/android/v5-2026-09-16|Braintree Google Pay Testing and Go Live — Android v5 (2026-09-16 snapshot)]]
