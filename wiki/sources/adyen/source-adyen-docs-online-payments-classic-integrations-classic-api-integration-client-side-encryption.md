---
title: "Adyen Classic Client-Side Encryption (CSE)"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/2026-09-15.md"
tags: [adyen, classic-api, client-side-encryption, cse, card-payments, pci-dss]
---

## Overview

This Adyen Classic API guide describes a merchant-served card form that uses the CSE JavaScript library to encrypt card data in the shopper's browser before the merchant server sends a legacy Payment API `/authorise` request. Adyen says **CSE Web integrations are being phased out**: it is no longer developing or accepting new CSE integrations and directs website builds to newer Web integrations. The page expressly says mobile integrations are unaffected by that Web phaseout; it does not describe mobile implementation details here. See [[adyen]], [[adyen-online-payments]] and [[adyen-pci-dss-compliance]].

## Key takeaways

- The merchant first needs a test account, API key or basic-authentication credentials for server API calls, and the unique CSE library location from Customer Area. Adyen can host the JavaScript library and key, or the merchant can host the library/use the JavaScript in its page. The merchant creates the card form and uses the Adyen library to encrypt fields marked `data-encrypted-name`; the guide says **not** to put the ordinary `name` attribute on those card input fields so unencrypted card data is not posted to the server.
- For this legacy CSE Web integration, the page says Subresource Integrity must be implemented for PCI DSS v4.0.1, with a stated deadline of 2025-03-31. It directs the merchant to copy an integrity hash from the web-service user's Customer Area credentials and include it when loading the library. This dated requirement is not proof that any deployed payment page is secure or PCI compliant. The merchant-served form and optional merchant-hosted library remain within PCI control scope; [[adyen-pci-dss-compliance]] routes the separate SAQ A eligibility and merchant-responsibility guidance.
- The encrypted form includes a **server-generated** `generationtime` timestamp; the page says Adyen refuses transactions sent more than 24 hours after that timestamp, and warns that an unsynchronized client clock can cause failures. Its `onsubmit`/AJAX example is an optional no-reload form pattern, not required for all integrations.
- On the merchant server, the guide sends `merchantAccount`, `reference`, minor-unit `amount`, and encrypted card payload in `additionalData.card.encrypted.json` to the **Classic Payment API** `/authorise` endpoint. The example's `Authorised` result is illustrative: the page says validation precedes risk analysis, and authorization is attempted depending on the outcome. The returned PSP reference can support later capture, cancel or refund; capture and authorization/failure webhooks are separate next-step routes.
- The page says the default encrypted data container is `adyen-encrypted-data` (line 110), but later instructs setting `card.encrypted.json` to an `adyen.encrypted.data` value (line 138). It does not reconcile the two names. Verify the actual field mapping in a retained implementation or authoritative API reference before using the example. The final SAQ A/CSE-role go-live link is a navigation claim, subject to the separate PCI guide's SAQ A eligibility and risk qualifications.

## Detail locators

- Lines 16–32: Web phaseout, mobile exception, purpose, and library/key hosting choices.
- `## Requirements` (lines 34–44): test account, server credentials, unique Customer Area library URL.
- `## Client side` (lines 54–124): SRI requirement and hash location, form attributes, server timestamp and 24-hour refusal condition, optional `onsubmit` behavior.
- `## Server side` (lines 126–205): Classic `/authorise` request/response, encrypted payload field, minor units, conditional risk/authorization outcome and PSP reference; JSON/SOAP values are examples.
- `## Next steps` (lines 207–225): capture, webhooks, PCI/SAQ A and CSE-role navigation.

## Related

- [[adyen-online-payments]] — provider concept and reciprocal source route.
- [[adyen-pci-dss-compliance]] — eligibility, merchant security controls and SAQ boundaries.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]] — sibling raw-card Classic `/authorise` guide.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/2026-09-15|Classic CSE guide, captured 2026-09-15]]
