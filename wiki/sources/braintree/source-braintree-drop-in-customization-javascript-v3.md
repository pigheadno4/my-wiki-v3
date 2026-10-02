---
title: "Braintree Drop-in Customization: JavaScript v3"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/drop-in/customization/javascript/v3"
raw_files:
  - "braintree/docs/guides/drop-in/customization/javascript/v3-2026-09-16.md"
tags: [braintree, drop-in, javascript-v3, vault-manager, events, customization]
---

## Overview

This Braintree JavaScript v3 guide is a customization reference for the prebuilt browser Drop-in UI. It covers customer-scoped saved-method presentation, selection clearing and deletion, card-form options, coordinated fraud-device-data setup, event-driven submission state, and CSS or field/button styling. These are client integration and presentation routes; the fraud section separately requires server-side device-data forwarding, and the snapshot does not prove current SDK support, merchant enablement, buyer eligibility, successful tokenization, or payment processing.

## Key takeaways

- A client token generated with `customer_id` makes Drop-in show that customer's saved payment methods and automatically add newly entered methods to the Vault record. The page says Venmo, Google Pay, and Apple Pay are not automatically vaulted on the client.
- `clearSelectedPaymentMethod` returns the customer to other saved methods or new entry after a failure; it does not delete the method from the Vault. Deletion is a separate, opt-in Vault Manager capability available when Drop-in is authorized with a customer-scoped client token. Braintree warns against enabling Vault Manager with recurring billing because customers could delete methods associated with subscriptions.
- Premium Fraud Management Tools require Control Panel enablement, client-side device-data collection, and server-side device-data submission to be completed together; the page warns that a delay between enablement and code changes makes the integration malfunction. Automatically vaulted new methods are verified without device data at vault time, although later transactions can still submit it.
- Drop-in events expose whether a payment method is requestable and support submit-button state. For cards, `paymentMethodRequestable` can fire after minimum client-side validation and before the buyer finishes entering a postal code; the page recommends checking `event.paymentMethodIsSelected` before automatic retrieval, while preserving manual submission otherwise. External payment flows fire the event after their flow completes.
- UI customization includes stable-looking `data-braintree-id` selectors, Hosted Fields-compatible card `overrides` for field options and styles, and a PayPal `buttonStyle` option. Braintree says to recheck custom CSS when upgrading and advises against Braintree class-name selectors because those names can change between versions; the field example also states that custom web fonts are unsupported.

> [!warning] Source-specific Drop-in lifecycle dates
> This snapshot says deprecation begins October 1, 2026, updates and fixes stop after that date, payment processing remains supported until October 1, 2027, and unsupported status begins October 1, 2027, after which support ends and processing may be suspended. The retained `braintree-web-drop-in@1.47.0` and `1.48.0` repository evidence instead gives September 1, 2026 and September 1, 2027 milestones. Treat both schedules as snapshot-specific, do not infer current support from either, and verify current official status before migration planning. [[source-github-braintree-web-drop-in]]

## Detail locators

- `Display a saved payment method`, `De-select a payment method`, and `Delete a saved payment method` cover customer-scoped client-token behavior, callback/Promise examples, Vault Manager, and the recurring-billing deletion warning.
- `Collect cardholder name` shows optional-versus-required configuration.
- `Premium Fraud Management Tools` lists the coordinated Control Panel, client, and server changes and the automatic-vault verification qualification.
- `Events` defines requestability, option-selection behavior, submit-button examples, and guarded automatic nonce retrieval. A nonce must still be sent to the merchant server; this page does not establish transaction completion.
- `Customize your UI` covers CSS selectors, card field overrides and styles, and PayPal button styling. Linked reference pages are navigation unless independently read.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-drop-in]]
- Related exact-version implementation evidence: [[source-github-braintree-web-drop-in]]

## Raw Sources

- [[raw/braintree/docs/guides/drop-in/customization/javascript/v3-2026-09-16|Braintree JavaScript v3 Drop-in customization guide]] - complete captured page, including lifecycle, Vault, fraud, events, and UI sections
