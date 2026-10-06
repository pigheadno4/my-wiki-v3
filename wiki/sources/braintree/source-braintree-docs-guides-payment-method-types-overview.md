---
title: "Braintree Payment Method Types Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/payment-method-types-overview"
raw_files:
  - "braintree/docs/guides/payment-method-types-overview-2026-09-16.md"
tags: [braintree, payment-methods, integration, client-sdk, server-sdk, account-compatibility]
---

## Overview

This unversioned [[braintree]] website-guide snapshot, collected 2026-09-16, is a provider-wide orientation to adding a payment method type to a Braintree integration. It frames selection and setup around production-account banking-partner compatibility, merchant and customer region, an existing client-and-server SDK integration, account/provider configuration, checkout UI, method-dependent server handling, and testing and go-live work.

## Key takeaways

- The page says payment-method acceptance can vary with the banking partner for the merchant's Braintree production account. It directs existing production merchants to their bank-specific Accepted Payment Methods page and says the production-account setup information identifies the types supported by that banking partner.
- Availability is also qualified by both business location and customer location. The linked support articles are the page's route to method-specific availability and compatibility; this overview itself does not establish eligibility for any named method, merchant or buyer.
- The guides assume existing client-side and server-side Braintree SDK integrations. They provide high-level SDK support while routing granular version support to SDK changelogs on GitHub, and the page recommends current client and server SDK versions for the broadest method range. A merchant without an integration is routed first to the basic-payments guide.
- The page organizes onboarding into four broad stages: configure and, where required, register the method; add customer-facing collection UI and client options; update server handling when applicable; then test end to end in sandbox and production and complete method-specific go-live steps. The list is an orientation, not a method support matrix or exact SDK procedure.
- Server treatment is method-dependent. The page says a common server path can handle payment-method nonces in simple cases, but some methods need additional server-call data, prohibit actions such as vaulting, or require a distinct server implementation.
- For a third-party integration or shopping cart, the page assigns client/server integration handling to that provider and directs merchants to the provider's documentation and support. This is distinct from a merchant-owned direct Braintree SDK integration.
- The page instructs merchants to inform payers that Braintree processes the payment, using either the specified checkout acknowledgment and PayPal privacy-notice link or the specified language in a privacy notice shown before payment. Preserve the exact supplied text from the raw locator rather than paraphrasing it for implementation.

## Evidence limitations

This website snapshot is not current availability, account enablement, merchant or buyer eligibility, exact SDK/version behavior, successful go-live, or payment, authorization, settlement or funding proof. References to bank-specific support articles, method guides, GitHub changelogs and third-party documentation are navigation unless separately retained and read. Testing in both sandbox and production is an instructed stage, not evidence that either environment has been tested successfully.

## Detail locators

- Purpose of the payment-method-type guide family: `# Overview`, line 18.
- Production-account banking-partner compatibility and bank-specific lookup: `### Compatible Braintree account`, lines 37-41.
- Merchant-region and customer-region availability qualifications: `### Availability in your region`, lines 44-48.
- Existing client/server SDK assumption, high-level versus changelog version routing, latest-version recommendation and basic-payments prerequisite: `### Braintree client and server SDK integration`, lines 51-57.
- Third-party integration or shopping-cart ownership boundary: note under `### Braintree client and server SDK integration`, lines 59-60.
- Four-stage configuration, client, server, testing and go-live sequence: `## Integration steps`, lines 63-75.
- Generic nonce handling versus method-specific extra data, prohibited vaulting and unique server implementation: `## Integration steps`, lines 70-72.
- Payer disclosure instruction and the two supplied text options: note under `## Integration steps`, lines 78-81.
- Support, reference, sales and enablement-help routes: `## How to get help`, lines 86-92.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Platform context: [[braintree-payment-platform]]
- Client SDK context: [[braintree-web-sdk]], [[braintree-ios-sdk]], [[braintree-android-sdk]]
- Server SDK context: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/payment-method-types-overview-2026-09-16|Braintree Payment Method Types overview]] - fully read pinned website snapshot covering account and regional qualifications, integration responsibilities, method-dependent limits, testing/go-live stages and payer disclosure
