---
title: "Braintree Google Pay Configuration for JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/configuration/javascript/v3"
raw_files:
  - "braintree/docs/guides/google-pay/configuration/javascript/v3-2026-09-16.md"
tags: [braintree, google-pay, javascript-v3, configuration, control-panel]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] website guide documents Google Pay configuration on the JavaScript v3 route: enable Google Pay in the matching sandbox or production Control Panel, seek merchant-account-specific activation when needed, and separately work with Google for production; accepting PayPal through Google Pay requires both payment methods enabled. It is documentation-family evidence, not an exact `braintree-web` package contract or confirmation of current browser coverage, merchant or account enablement, Google production approval, client/server integration, or payment execution.

## Key takeaways

- The page says Google Pay in the JavaScript SDK is available across multiple browsers and routes the full browser list to Google documentation rather than enumerating it locally.
- For either sandbox or production, the documented action is to use that environment's Control Panel and turn on Google Pay under **Account Settings** → **Payment Methods**.
- General Control Panel activation may be insufficient for a particular merchant account; the page directs that case to Braintree support. Production also requires separate work with Google to go live.
- PayPal via Google Pay has a dual-enablement condition: both PayPal and Google Pay must be enabled in the Control Panel.

## Detail locators

- **JavaScript SDK browser-availability statement and external browser-list route:** `AVAILABILITY`, raw lines 16–17.
- **Sandbox/production Control Panel setup action:** `## Setup`, raw lines 20–29.
- **Merchant-account-specific activation route:** raw line 31.
- **Separate Google production requirement:** raw line 33.
- **PayPal via Google Pay dual-enablement condition:** `### PayPal via Google Pay`, raw lines 36–38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Google Pay orientation: [[source-braintree-docs-guides-google-pay-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/configuration/javascript/v3-2026-09-16|Braintree Google Pay configuration — JavaScript v3 (2026-09-16 snapshot)]]
