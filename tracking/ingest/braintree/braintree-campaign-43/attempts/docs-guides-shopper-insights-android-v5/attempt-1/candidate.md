---
title: "Braintree Shopper Insights (Beta) — Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/shopper-insights/android/v5"
raw_files:
  - "braintree/docs/guides/shopper-insights/android/v5-2026-09-16.md"
tags: [braintree, shopper-insights, android, mobile-sdk, paypal, venmo, beta]
---

## Overview

This 2026-09-16 snapshot of the Braintree Android v5-routed Shopper Insights beta guide describes client-side customer-session creation or update, PayPal-or-Venmo recommendation retrieval, recommendation presentment, and presented/selected event calls. It is evidence for the captured guide, not current availability, customer eligibility, a recommendation for any particular customer, event acceptance, or payment execution. See [[braintree]] and [[braintree-android-sdk]].

## Key takeaways

- The page says `generateCustomerRecommendations` returns PayPal or Venmo as a recommended payment using the customer's email. Before using the method, the merchant must obtain the customer's consent to share that information with PayPal services. The guide does not establish that either method will be recommended for a given customer.
- A Client Token is required to initialize the SDK; the feature is not supported with Tokenization Keys.
- Under its PayPal Checkout presentment terms, the page says to confirm the customer's PayPal network payment eligibility before any other payment method. If eligibility is confirmed, the recommended method or methods should receive preferential placement on pages offering payment options and, if available, should be preselected. If eligibility cannot be confirmed, PayPal should be positioned at least at parity with other payment methods.
- The examples create or update a customer session, generate recommendations from a session ID, call `sendPresentedEvent` after presenting recommendations, and call `sendSelectedEvent` after the user selects an option. These snippets illustrate client calls and inputs; they do not prove customer eligibility, recommendation accuracy, event receipt, authorization, or payment success.

> [!warning] Captured mobile-certificate notice
> The captured page says the SSL certificates for Braintree Mobile iOS and Android SDKs were set to expire on March 30, 2026, would affect existing SDK versions in published apps, and directs Android integrations to upgrade to version 4.45.0+ or 5.0.0+ for new SSL certifications. It further says that failing to decommission app versions containing older SDKs or force-upgrade them by the expiration date would cause 100% of customer traffic to fail. This preserves the page's dated wording and version thresholds; the snapshot does not establish current certificate or SDK-support status.

## Detail locators

- Beta title and captured availability statement: title and **AVAILABILITY**, lines 14–18.
- Mobile SSL-certificate expiration, Android upgrade versions, and traffic-failure warning: **IMPORTANT**, lines 21–26.
- Recommendation purpose and consent condition: **Integration**, lines 34–38.
- PayPal Checkout eligibility, preferential-placement, preselection, and parity language: **IMPORTANT**, lines 41–42.
- Client Token requirement and Tokenization Key exclusion: **NOTE**, lines 45–46.
- Captured `shopper-insights:5.8.0` dependency example: lines 50–65.
- Customer-session create and update examples, including hashed email/phone inputs and session ID: lines 67–108.
- Recommendation-generation example: lines 110–126.
- Presented and selected event examples: lines 128–139.

## Related

- [[braintree]]
- [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/shopper-insights/android/v5-2026-09-16|Braintree Shopper Insights (Beta) — Android v5 (fetched 2026-09-16)]]
