---
title: "Braintree Android Drop-in Customization (v5)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/drop-in/customization/android/v5"
raw_files:
  - "braintree/docs/guides/drop-in/customization/android/v5-2026-09-16.md"
tags: [braintree, android, drop-in, customization, vault-manager, fraud-tools]
---

## Overview

This historical Braintree Android v5-routed guide describes customization of the prebuilt Drop-in UI: customer-scoped saved-method display and vaulting, saved-method deletion through Vault Manager, cardholder-name collection, and Premium Fraud Management Tools coordination. It is configuration guidance from a website snapshot, not proof of the Android Drop-in package version, compatibility with the modular Android v5 SDK, current support, merchant enablement, buyer eligibility, successful tokenization, or payment processing.

## Key takeaways

- A client token generated with `customer_id` makes Drop-in display that customer's saved payment methods and automatically add newly entered methods to the customer's Vault record. Google Pay is explicitly excluded from automatic client-side vaulting.
- Customer-scoped client tokens can also enable removal of saved methods through Vault Manager. Braintree warns against enabling Vault Manager with recurring billing because customers could delete payment methods associated with subscriptions.
- The credit-card form can collect cardholder name and mark the field optional or required. The retained body establishes the option but does not retain a rendered configuration example.
- Premium Fraud Management Tools require three coordinated changes: enablement in the Control Panel, client-side device-data collection, and server-side device-data submission on transaction and verification requests. The page says delaying the code changes after enablement makes the integration malfunction.
- When a new payment method is automatically vaulted, its verification is evaluated without device data by Premium Fraud Management Tools; later transactions can still pass device data. This qualification does not establish whether a fraud product is enabled for a particular merchant.

> [!warning] Source-specific Drop-in lifecycle
> The snapshot says the Drop-in SDK becomes deprecated on October 1, 2026, after which it receives no new features, improvements, or bug fixes; payment processing remains supported until October 1, 2027. It says unsupported status begins October 1, 2027, after which Braintree support ends and payment processing may be suspended at any time, and it directs migration to the Braintree Android SDK. Treat this as the page's dated schedule and recheck current official status before operational planning.

> [!warning] Package-version, rendering, and certificate boundaries
> The `/android/v5` URL and retained body do not identify the Android Drop-in artifact version or prove compatibility with the independently retained modular `braintree-android@5.30.0` baseline. The separate exact-version [[source-github-braintree-android-drop-in]] retains `drop-in@6.17.0` pinned to Braintree Android `4.50.0`. The missing rendered configuration after the Vault Manager label does not show that a separate API or supported integration route is absent. Separately, [[source-braintree-client-sdk-setup-android-v5]] preserves a historical March 30, 2026 mobile-certificate notice with Android SDK `4.45.0+` or `5.0.0+` upgrade targets; that notice is not present in this raw and must not be projected onto an unidentified Drop-in dependency or treated as observed current traffic failure.

## Detail locators

- Drop-in deprecation, unsupported date, processing qualification, and Braintree Android SDK migration direction: `# Customization > IMPORTANT`, raw lines 17–22.
- Customer-scoped saved-method display, automatic vaulting, and the Google Pay exception: `## Display a saved payment method`, raw lines 27–31.
- Vault Manager enablement, missing rendered configuration boundary, and recurring-billing deletion warning: `## Delete a saved payment method`, raw lines 36–46.
- Optional or required cardholder-name field: `## Collect cardholder name`, raw lines 51–53.
- Coordinated Control Panel, client-side, and server-side Premium Fraud Management Tools steps plus the delay warning: `## Premium Fraud Management Tools`, raw lines 56–65.
- Automatic-vault verification device-data exclusion and subsequent-transaction alternative: `## Premium Fraud Management Tools > NOTE`, raw lines 68–69.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]
- [[source-braintree-drop-in-setup-and-integration-android-v5]] - separate Android v5-routed Drop-in setup and integration snapshot; not package-version or current-support evidence
- [[source-github-braintree-android-drop-in]] - independently versioned Android Drop-in implementation evidence
- [[source-braintree-client-sdk-setup-android-v5]] - separate modular Android v5 setup snapshot preserving the dated mobile-certificate qualification

## Raw Sources

- [[raw/braintree/docs/guides/drop-in/customization/android/v5-2026-09-16|Braintree Android Drop-in Customization (v5)]] - complete collected website snapshot for saved methods, Vault Manager, cardholder-name collection, fraud-tool coordination, and the source-specific lifecycle notice
