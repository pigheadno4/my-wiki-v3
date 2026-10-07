---
title: "Braintree Shopper Insights (Beta) for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/shopper-insights/ios/v7"
raw_files:
  - "braintree/docs/guides/shopper-insights/ios/v7-2026-09-16.md"
tags: [braintree, ios, shopper-insights, paypal, venmo, checkout, beta]
---

## Overview

This 2026-09-16 website snapshot documents Braintree Shopper Insights (Beta) on the iOS v7 route. It describes using customer information to request PayPal or Venmo payment recommendations and then adjusting checkout presentation; it is documentation evidence, not proof of current availability, merchant eligibility, recommendation results, or successful payment execution.

## Key takeaways

- The captured availability notice says Shopper Insights is available only to merchants using iOS SDK v6+ or Android SDK v4+, and not to merchants using the JavaScript or Drop-in SDK. The iOS v7 route itself does not establish enablement for a particular merchant or customer.
- Before calling `generateCustomerRecommendations`, the guide says to obtain customer consent to share the information with PayPal services. Its Swift examples create or update a customer session from a `BTCustomerSessionRequest`, then request recommendations that may identify PayPal or Venmo.
- The guide requires a client token to initialize the SDK and says tokenization keys are unsupported for this feature.
- Its presentment terms say PayPal-network eligibility is checked before other payment methods; when confirmed, recommended methods receive preferential placement and, if available, preselection. When eligibility cannot be confirmed, PayPal is positioned at least at parity with other methods.
- The analytics section directs the integration to report when a PayPal or Venmo button is displayed and when it is selected or tapped. The prose calls the first method `sendPresentedEvents`, while the Swift example calls `sendPresentedEvent`; consult the captured lines rather than treating this page as an exact callable-signature guarantee.
- The snapshot carries a dated mobile-SDK certificate warning: certificates were stated to expire on March 30, 2026; it directs iOS merchants to upgrade to 6.17.0+ and warns that retaining app versions with older SDK certificates without a forced upgrade would cause all customer traffic to fail. This is a preserved historical warning, not evidence of current certificate or traffic status.

## Detail locators

- Availability scope: raw lines 17–18.
- Certificate-expiry warning, upgrade floor, and decommission/forced-upgrade consequence: raw lines 23–26.
- Recommendation purpose, customer-consent condition, presentment terms, client-token requirement, and UI-adjustment direction: raw lines 31–52.
- Swift create-session example (`BTShopperInsightsClientV2`, `BTCustomerSessionRequest`, and `createCustomerSession`): raw lines 53–71.
- Swift update-session example (`BTShopperInsightsClient`, session ID, and `updateCustomerSession`): raw lines 73–98.
- Swift recommendation example and PayPal/Venmo result checks: raw lines 100–131.
- Analytics direction and the prose/code method-name mismatch: raw lines 133–153.

## Related

- [[braintree]]
- [[braintree-ios-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/shopper-insights/ios/v7-2026-09-16|Braintree Shopper Insights (Beta), iOS v7 — 2026-09-16 snapshot]]
