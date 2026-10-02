---
title: "Braintree Auth Branding for JavaScript v3"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/branding/javascript/v3"
raw_files:
  - "braintree/docs/guides/braintree-auth/branding/javascript/v3-2026-09-16.md"
tags: [braintree, braintree-auth, branding, javascript-v3, connected-merchants]
---

## Overview

This collected JavaScript v3 branding guide defines how a platform should present the closed-beta [[braintree-auth]] Connect experience to merchants. It identifies the merchant-facing brand as **PayPal powered by Braintree** and provides logo, payment-method image, explanatory-copy and **Connect with Braintree** button variants; these assets are presentation guidance, not evidence that a payment method is currently enabled or accepted for a particular platform or merchant.

## Key takeaways

- The snapshot labels Braintree Auth as closed beta and directs interested platforms to contact Braintree. It describes Braintree Auth and Connect with Braintree as a unified PayPal and Braintree merchant experience whose merchant-facing brand is **PayPal powered by Braintree**.
- For platform dashboards, the page provides horizontal and vertical **PayPal powered by Braintree** logos. It separately provides one payment-method image that names major credit/debit cards plus PayPal and a cards-only image; these are display variants, not a current capability or eligibility matrix.
- The recommended explanatory copy depends on the platform's intended relationship: the transaction-creating variant tells merchants that connecting starts acceptance of credit/debit cards and PayPal, while the non-transaction variant asks merchants only to link their account. Both examples include the generic learn-more link.
- The page says to display a **Connect with Braintree** button. It prefers the `braintree-oauth-connect.js` library, while also allowing the button image to be added manually.
- After a button click, the guide requires redirecting the merchant to the unified signup form with the server-generated `connect_url`. After the merchant authorizes the application and returns to the platform dashboard, it says not to initialize `braintree-oauth-connect.js` or display the connect button.

> [!warning] Snapshot and capability boundary
> This is branding and merchant-connection guidance from a 2026-09-16 snapshot. The closed-beta label, logos, badge wording and example copy do not establish current Braintree Auth availability, account eligibility, successful connection, OAuth permissions, or live card/PayPal acceptance.

## Detail locators

- Closed-beta notice and contact route: `# Branding > AVAILABILITY`, lines 17-18.
- Unified merchant experience and required merchant-facing brand: `# Branding`, line 20.
- Horizontal and vertical dashboard logos with HTML examples: `## Logo`, lines 23-40.
- Combined card-and-PayPal image and cards-only variant: `## Payment methods`, lines 44-60.
- Transaction-creating explanatory copy and learn-more link: `## Description and FAQ`, lines 65-75.
- Non-transaction account-linking copy and learn-more link: `## Description and FAQ`, lines 76-82.
- Connect button, preferred library and manual-image alternative: `## Button`, lines 84-92.
- Required server-generated Connect URL redirect and post-authorization button/library state: `## Button`, lines 93-95.
- Downloadable partner-assets archive or provided-code route: `## Resources`, lines 100-102.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Merchant-facing hosted flow: [[source-braintree-auth-connect]]

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/branding/javascript/v3-2026-09-16|Braintree Auth Branding for JavaScript v3]] - complete collected branding guide for merchant-facing logos, copy variants, Connect button presentation and its post-authorization display condition
