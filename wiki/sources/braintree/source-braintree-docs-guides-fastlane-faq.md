---
title: "Braintree Fastlane Troubleshooting and FAQs"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/faq"
raw_files:
  - "braintree/docs/guides/fastlane/faq-2026-09-16.md"
tags: [braintree, fastlane, troubleshooting, payment-token, vaulting]
---

## Overview

This collected, unversioned [[braintree]] website FAQ is a troubleshooting and implementation-retrieval page for merchants integrating [[paypal-fastlane]] through Braintree. It covers merchant provisioning and disablement signals, buyer/member fallback behavior, payment-token lifetime and refresh, delivery-location controls, pickup handling, CSP guidance, vaulting answers and the division of work between the prebuilt Payment Integration and Flexible Integration. The captured page does not identify a Braintree Web SDK or hosted Fastlane runtime version.

The page is snapshot documentation, not proof of current availability, merchant or buyer eligibility, successful authentication, token consumption, payment or Vault execution, security or privacy compliance, or country support. Its `addressOptions` answer concerns merchant-allowed shipping locations; it does not state a Fastlane country-availability matrix.

## Key takeaways

- An initialization authorization error may mean the merchant account and client credentials are not provisioned for Fastlane; the page directs the merchant to its account team. This diagnostic does not establish enablement or eligibility.
- When a merchant disables Fastlane, the FAQ says the client SDK reverts buyers to a guest experience without Fastlane-profile opt-in. When disabled in the Braintree Control Panel, the authentication and saved-address/card selector methods listed in the raw return `undefined`.
- The FAQ gives a three-hour lifetime for a `paymentToken`. On checkout-page reload it recommends calling `triggerAuthenticationFlow()` again; the SDK may request OTP authentication or restore the session, and the returned authentication result includes a new token. These statements do not prove downstream transaction or Vault success.
- Store-pickup integrations are told to set the shipping method to `pickupInStore` or `shipToStore` so the store address is not saved as the buyer's shipping address. Merchants can pass allowed locations through `addressOptions`; the page does not enumerate supported Fastlane countries or make every delivery destination eligible.
- The CSP section recommends `frame-src *.paypal.com` for Sandbox and Production and labels the instruction as skippable for Hosted Card Fields. This is page-specific integration guidance, not a complete security policy or a security, privacy or regulatory compliance guarantee.
- The vaulting answers conflict inside this snapshot. One answer says a token may be vaulted first through customer-create or payment-method-create and transacted later; a later answer says pre-transaction customer/payment-method creation is unsupported and only `store_in_vault_on_success` vaulting is supported. Do not select either route as authoritative without resolving the conflict against the applicable current Braintree contract.
- The comparison table frames Payment Integration as a lighter, PayPal-prebuilt form and Flexible Integration as merchant-customized UI that additionally owns billing-address fields and conditional card-field display. This is a selection aid, not a runtime, conversion or compatibility guarantee.

## Detail locators

- Initialization authorization, missing member cards/addresses, token-call formatting and disabled-method troubleshooting: `# Troubleshooting and FAQs`, raw lines 16-23.
- Merchant-disablement guest fallback and the three methods that return `undefined` after Braintree Control Panel disablement: `**Disablement Flow**`, raw lines 25-40.
- Store-pickup shipping-method values and the profile-address safeguard: `#### FAQs` / `**How do I integrate Fastlane if I have store pick-up?**`, raw lines 47-53.
- Transact-and-vault and vault-then-transact answers: `**How do I vault transactions with Fastlane?**`, raw lines 57-67.
- CSP rationale, Hosted Card Fields exception and the Sandbox/Production `frame-src` value: `**Is there any directive I need to include in my Content Security Policy (CSP)?**`, raw lines 69-79.
- Conflicting vault-support limitation: `**Will Fastlane work if I vault payer's payment methods?**`, raw lines 81-85.
- Token lifetime, merchant-allowed shipping locations and reload authentication/session restoration: raw lines 87-97.
- Prebuilt Payment Integration versus Flexible Integration responsibilities: `**When should I use quick-start Payment integration vs. Flexible integration?**`, raw lines 103-120.

## Related

- [[braintree]] - provider and gateway context
- [[paypal-fastlane]] - Fastlane guest-checkout acceleration, identity/profile and tokenization concept; consult integration- and version-specific sources for runtime behavior

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/faq-2026-09-16|Braintree Fastlane Troubleshooting and FAQs (collected 2026-09-16)]] - fully read pinned snapshot
