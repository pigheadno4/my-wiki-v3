---
title: "Braintree Fastlane Testing Guide"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/testing-go-live"
raw_files:
  - "braintree/docs/guides/fastlane/testing-go-live-2026-09-16.md"
tags: [braintree, fastlane, testing, sandbox]
---

## Overview

This collected, unversioned [[braintree]] website guide is a test checklist for [[paypal-fastlane]] guest and member scenarios. It covers Sandbox identity and authentication fixtures, consent/profile creation cases, saved-address and saved-card changes, fallback card entry, and a table of test-card values. The captured page does not identify a Braintree Web SDK or PayPal Fastlane runtime version.

Despite the page URL's `testing-go-live` label, the captured content contains no production credentials, enablement, eligibility, domain approval, or launch procedure. Its scenario tables state intended integration results; completing a fixture or seeing an expected-looking result is not evidence of current production eligibility, token validity, authorization, capture, settlement, funding, or a successful live payment.

## Key takeaways

- The guest-payer checklist starts with a new email address not associated with a Sandbox Fastlane account. In Sandbox, it says any valid phone number may be entered and no SMS is sent; after the prescribed transaction completes, the page expects a Fastlane profile to exist for later member testing.
- Member testing depends on first creating a Fastlane profile through the guest path. The page supplies a Sandbox-only OTP success/failure fixture and asks the integrator to exercise updates to cards and shipping addresses. These are test inputs and expected cases, not reusable production authentication behavior.
- The member table covers successful authentication and prefill, failed or cancelled OTP fallback, adding or changing addresses and cards, and profiles with no supported card or address. Statements that an order or payment "should" complete are checklist expectations, not observed execution evidence.
- The page says PayPal members without a Fastlane profile do not need a distinct Fastlane integration test and routes readers to a separate advanced-options page. That statement is scoped to this collected checklist and does not establish current product parity or live support.
- The test-card table is snapshot data rather than proof of network, processor, or account behavior. It assigns one repeated number to two different brand rows, so retain its labels exactly when inspecting the raw and do not treat the table as independently validated.

> [!WARNING]
> This page does not document client-token creation, payment-method nonce or single-use-token handling, server transaction submission, or authorization/capture/settlement transitions. Use the applicable integration and transaction authorities for those lifecycle questions. The checklist's stated outcomes do not prove that a payment actually succeeded.

## Detail locators

- Guest-payer email, consent, phone and profile-creation checklist: `#### Testing Guest Payers`, lines 19-25.
- Guest consent-off and consent-on scenario table with stated profile and payment results: lines 27-37.
- Member-profile prerequisite, Sandbox OTP fixture and update-test instruction: `#### Testing Fastlane Members`, lines 40-47.
- Member happy path, failed/cancelled OTP fallback, new/change address and card cases, and unsupported-card/region cases: lines 49-96.
- PayPal-member-without-Fastlane handling and advanced-options navigation: `#### PayPal members without a Fastlane Profile`, lines 99-103.
- Test-card values and as-captured brand labels: `#### Test Cards`, lines 106-114.

## Related

- [[braintree]] - company and gateway context
- [[paypal-fastlane]] - Fastlane identity, profile and checkout-acceleration concept; consult version- and integration-specific sources for token and payment lifecycle behavior
- [[braintree-web-sdk]] - exact-version Braintree browser-adapter evidence, kept separate from this unversioned website checklist

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/testing-go-live-2026-09-16|Braintree Fastlane testing checklist (collected 2026-09-16)]]
