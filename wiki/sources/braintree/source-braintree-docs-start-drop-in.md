---
title: "Braintree Drop-in UI Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/drop-in"
raw_files:
  - "braintree/docs/start/drop-in-2026-09-16.md"
tags: [braintree, drop-in, checkout-ui, client-sdk, server-sdk, deprecation]
---

## Overview

This [[braintree]] website landing-page snapshot describes Drop-in as a ready-made payment UI for adding a customizable checkout to an app or website. Its retrieval value is the high-level product purpose, the complementary client/server SDK responsibility split, and the page's dated Drop-in lifecycle notice; it is not exact-package implementation evidence or proof of current availability, merchant eligibility, payment-method enablement, runtime compatibility, or successful payment processing.

## Key takeaways

- The page presents Drop-in as a quick integration path with a customizable UI and routes readers toward cards, PayPal, and other payment-method types. These are product and navigation statements, not evidence that a method is available or enabled for a particular merchant, buyer, platform, region, or environment.
- Client SDKs collect payment-method details, while server SDKs manage merchant-server requests to the Braintree gateway. This landing page does not specify the complete authorization, sale, settlement, funding, error-handling, or fulfillment lifecycle.
- The integration checklist routes readers to separate server setup and client Drop-in setup, then suggests considering PayPal, Venmo, or Apple Pay. Those linked routes require their own version-, platform-, eligibility-, and configuration-specific evidence.
- If Drop-in does not fit, the page points to Hosted Fields or a custom client-SDK integration; this is selection guidance, not a compatibility or migration guarantee.

> [!warning] Source-qualified lifecycle notice
> This 2026-09-16 website snapshot says the Drop-in SDK becomes deprecated on October 1, 2026, with no new features, improvements, or bug fixes after that date; payment processing remains supported until October 1, 2027. It says the SDK becomes unsupported on October 1, 2027, Braintree support assistance ends, and payment processing may then be suspended at any time. The page directs migration specifically to the Braintree iOS SDK. These statements are snapshot evidence, not current status or proof of the reader's support, eligibility, or migration path. They also conflict with the September lifecycle schedule in retained exact-version repository evidence; preserve each schedule as source-specific and verify current official guidance before planning a migration. [[source-github-braintree-web-drop-in]]

## Detail locators

- Deprecation, processing-support, unsupported-status, suspension, and iOS-migration statements: `# Drop-in UI > **IMPORTANT**`, raw lines 17-22.
- Ready-made UI purpose, app-or-website positioning, customization, and payment-method expansion claims: `# Drop-in UI`, raw lines 26-41.
- JavaScript CodePen and tutorial navigation: `## Try it out`, raw lines 44-56.
- Client SDK collection role and server SDK gateway-request role: `## Drop-in and your server`, raw lines 57-65.
- Server setup, client Drop-in setup, optional PayPal/Venmo/Apple Pay routes, and Hosted Fields/custom-integration alternatives: `## Integrate Drop-in`, raw lines 66-76.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-drop-in]]
- Broader Direct integration flow: [[source-braintree-get-started]]
- Browser-and-server tutorial: [[source-braintree-docs-start-tutorial-drop-in-node]]
- Exact-version repository evidence: [[source-github-braintree-web-drop-in]]

## Raw Sources

- [[raw/braintree/docs/start/drop-in-2026-09-16|Braintree Drop-in UI landing page]] - fully read pinned website snapshot covering product positioning, client/server roles, integration navigation, alternatives, and the dated lifecycle notice
