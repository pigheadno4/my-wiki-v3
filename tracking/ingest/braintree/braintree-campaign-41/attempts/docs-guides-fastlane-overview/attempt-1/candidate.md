---
title: "Braintree Fastlane Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/overview"
raw_files:
  - "braintree/docs/guides/fastlane/overview-2026-09-16.md"
tags: [braintree, paypal, fastlane, guest-checkout, authentication]
---

## Overview

This collected, unversioned [[braintree]] website overview describes [[paypal-fastlane]] as an autofill checkout solution for consumers manually entering payment information on a merchant website. It says Fastlane saves and retrieves card details and shipping addresses and can provide payment and billing information for customers with an existing profile. The page distinguishes a non-accelerated guest from an accelerated user identified and authenticated through an existing PayPal or Fastlane account, while separately stating that a Fastlane profile is distinct from a PayPal account.

This is a 2026-09-16 snapshot of an unversioned website page. It is not proof of current country availability, merchant or buyer eligibility, account enablement, successful authentication, profile retrieval, card acceptance, PCI compliance, payment execution, Vault behavior, authorization, settlement or funding. The linked sample applications are navigation only and do not provide exact-version GitHub or executed-payment evidence for this entry.

## Key takeaways

- The captured availability section lists Canada and the United States; China, Hong Kong, Malaysia and Singapore; a set of European countries and territories; and Australia and New Zealand. Treat that matrix as snapshot documentation and inspect the raw list for exact country codes rather than inferring current regional eligibility.
- The page limits this Braintree integration to responsive desktop and mobile web and says native apps are not currently supported. It also lists compatibility with an existing server SDK integration and requires card processing through Braintree. These are page-stated integration conditions, not proof that a particular merchant is enabled.
- Other listed merchant conditions are showing PayPal in the cart or beside the Fastlane email field, collecting a billing address, and including the merchant domain when generating the Braintree client token. The page says Fastlane uses the domain to authenticate and recognize returning customers and warns that omission prevents full functionality.
- A guest without a recognized profile receives the standard, non-accelerated flow. The accelerated path is described for a user identified and authenticated through an existing PayPal or Fastlane account; profile recognition alone must not be treated as successful authentication or payment.
- The profile-access section says Fastlane profiles are separate from PayPal accounts and provides Production and Sandbox profile-site links. Its fixed `111111` passcode and Braintree-testing-card restriction are expressly Sandbox fixtures, not Production authentication or card-support evidence.
- The developer-feature list claims customizable components, several named card brands, one-click checkout and cross-merchant profile recognition. Those are unversioned product-summary statements; they do not establish current SDK behavior, merchant configuration, buyer eligibility, successful tokenization or payment outcomes.

## Detail locators

- Autofill purpose, saved card and shipping data, and existing-profile payment/billing retrieval: `# Overview`, raw line 16.
- Captured country and territory matrix with exact codes: `### Availability`, raw lines 17-69.
- Responsive-web-only scope, server-SDK compatibility, Braintree card processing, PayPal visibility, billing-address collection and client-token domain conditions: `### Integration Requirements`, raw lines 72-82.
- Guest/non-accelerated versus identified-and-authenticated accelerated user descriptions: `### Fastlane User Profiles`, raw lines 85-91.
- Separate-profile statement, Production/Sandbox profile routes, Sandbox passcode and testing-card restriction: `### Accessing Fastlane Profiles`, raw lines 94-102.
- Braintree SDK and GraphQL sample-application links: `### Sample Applications`, raw lines 105-111; linked repositories were not read as evidence for this entry.
- Product-summary feature claims, named card brands, one-click language and cross-merchant portability: `### Key Features for Developers`, raw lines 114-124.

## Related

- [[braintree]] - provider and gateway context
- [[paypal-fastlane]] - Fastlane guest-checkout acceleration, identity/profile and tokenization concept; use integration-specific and versioned sources for runtime behavior

## Related raw API references

- [[raw/braintree/docs/guides/fastlane/setup-integration-2026-09-16|Braintree Fastlane setup and integration]] - next-step navigation only; not read as behavioral, eligibility, SDK-version or payment evidence for this entry
- [[raw/braintree/docs/guides/credit-cards/testing-go-live/node-2026-09-16|Braintree credit-card testing and go-live]] - linked testing-card navigation only; not read as evidence for this entry

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/overview-2026-09-16|Braintree Fastlane overview (collected 2026-09-16)]] - fully read pinned website snapshot
