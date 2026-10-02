---
title: "Braintree Android Drop-in Setup and Integration (v5)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/drop-in/setup-and-integration/android/v5"
raw_files:
  - "braintree/docs/guides/drop-in/setup-and-integration/android/v5-2026-09-16.md"
tags: [braintree, android, drop-in, setup, client-authorization, browser-switch]
---

## Overview

This historical Braintree Android Drop-in setup snapshot describes client authorization, payment-method-specific setup routes, saved-method lookup, and browser-switch handling for the prebuilt Drop-in UI. It is a setup and navigation source, not proof of current SDK support, exact package compatibility, merchant or buyer eligibility, or a successful payment flow.

The collected body retains `Setup` and `Starting Drop-in` headings but not their rendered dependency or launch examples. Use the raw only for the text and examples actually present; the missing rendered fragments do not establish that separate setup requirements or implementation authority are absent.

## Key takeaways

- The page says the Drop-in UI needs either a Control Panel tokenization key or a client token generated on the merchant server. It does not turn either credential route into proof that a merchant is configured or eligible.
- Non-card payment methods require additional method-specific setup. The retained body routes Google Pay to its Android manifest metadata requirement, Venmo to browser-switch setup and a `VenmoRequest`, and 3D Secure to a `ThreeDSecureRequest` carrying an amount. These are setup instructions, not evidence that a method was displayed, vaulted, verified, or charged.
- `DropInClient#fetchMostRecentPaymentMethod` can avoid showing Drop-in when an existing method is returned, but the page says a result is returned only with a client token created with a `customer_id`. Its examples also distinguish Google Pay by requiring the buyer to perform the Google Pay flow again at checkout.
- Drop-in handles browser switching internally in most cases. A custom URL scheme is still required in some scenarios, including the page's uppercase-`applicationId` example; the manifest override and `DropInRequest` value must use the aligned scheme.

> [!warning] Source-specific lifecycle notice
> The snapshot says Drop-in becomes deprecated on October 1, 2026, with no later features, improvements, or bug fixes; payment processing remains supported until October 1, 2027. It says the SDK becomes unsupported on October 1, 2027, after which support ends and processing may be suspended at any time, and it directs migration to the Braintree Android SDK. Treat these as this website snapshot's schedule and recheck current support before operational planning.

> [!warning] Package-version and certificate boundaries
> The `/android/v5` documentation route does not identify the Drop-in package version or prove compatibility with the retained modular `braintree-android@5.30.0` baseline. The independently retained `drop-in@6.17.0` source pins Braintree Android `4.50.0`. Separately, [[source-braintree-client-sdk-setup-android-v5]] preserves a historical March 30, 2026 mobile-certificate notice with qualified Android SDK upgrade targets; that notice is not present in this Drop-in raw and must not be projected onto an unidentified Drop-in dependency or treated as observed current traffic failure.

## Detail locators

- Drop-in deprecation, unsupported date, processing qualification, and migration direction: `# Setup and Integration > IMPORTANT`, raw lines 17–22.
- Tokenization-key or server-generated-client-token authorization choice: `## Configuration`, raw lines 27–29.
- Missing rendered setup and launch-example boundary: `## Setup`, `### Gradle`, `## Client-side implementation`, and `### Starting Drop-in`, raw lines 32–45.
- Additional non-card setup condition and Google Pay qualifications: `### Configuring payment methods` and `#### Google Pay`, raw lines 48–57.
- Venmo browser-switch route and retained Java/Kotlin request examples: `#### Venmo`, raw lines 60–77.
- 3D Secure request-with-amount instruction: `### 3D Secure`, raw lines 79–81.
- Customer-scoped most-recent-method condition and Google Pay repeat-flow examples: `### Displaying the most recently added payment method`, raw lines 84–145.
- Default browser-switch handling, custom-scheme exception, manifest override, and matching request value: `## Browser Switch`, raw lines 147–180.
- Server nonce handoff, customization, and payment-method navigation: `## Next steps`, raw lines 183–190.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]
- [[source-braintree-client-sdk-setup-android-v5]] - separate modular Android v5 setup snapshot with environment, authorization, return-routing, and historical certificate qualifications; not Drop-in package-version evidence
- [[source-github-braintree-android-drop-in]] - independently versioned Android Drop-in implementation evidence
- [[source-github-braintree-android]] - independently versioned modular Android SDK implementation evidence and migration target

## Raw Sources

- [[raw/braintree/docs/guides/drop-in/setup-and-integration/android/v5-2026-09-16|Braintree Android Drop-in Setup and Integration (v5)]] - complete collected website snapshot for Drop-in authorization, method setup routes, saved-method lookup, browser switching, and the source-specific lifecycle notice
