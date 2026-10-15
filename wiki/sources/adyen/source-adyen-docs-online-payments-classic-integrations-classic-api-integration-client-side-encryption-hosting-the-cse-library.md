---
title: "Adyen Classic CSE library self-hosting"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library/2026-09-15.md"
tags: [adyen, classic-api, client-side-encryption, cse, web, card-data]
---

## Overview

This dated Classic Web CSE guide explains how a merchant can host Adyen's legacy Client-Side Encryption JavaScript library, or embed it in a payment form, so card details are encrypted in the browser before submission to the merchant server. Adyen says it strongly recommends its own hosting from a unique URL. The page says CSE Web integrations are being phased out, are no longer developed, and are not accepted for new integrations; it separately states mobile integrations are unaffected. The raw page reports `last_modified: 2019-04-22` and was captured 2026-09-15. This route is distinct from Adyen's newer Web JWE card-encryption guide.

## Key takeaways

- The page requires the CSE public key from Customer Area to encrypt payment details client-side. Self-hosting uses `adyen.encrypt.min.js` for HTML form binding or JavaScript-only use; `adyen.encrypt.nodom.min.js` supports JavaScript-only use. The raw page does not specify library release numbers or establish current availability. See **Requirements**, **Merchant hosted**, and **JavaScript only**.
- In the HTML form variant, the merchant supplies the form markup and JavaScript binding. Card inputs use `data-encrypted-name` without a `name` attribute so the raw card values are not posted as ordinary form fields; the library adds a hidden encrypted-card input on submission. The page links this design to PCI concerns, but it does not prove PCI DSS compliance or a particular scope reduction. See **Merchant hosted** and **Form template**.
- The form includes a hidden `generationtime` value created server-side. The page says transactions submitted more than 24 hours after that timestamp are refused and warns that the browser clock might be unsynchronized. See **Form template**.
- The HTML form route shows either a plain global `adyen.encrypt` script or an AMD/Require.js module to call `createEncryptedForm`. The Require.js version in its sample URL is an example, not a declared CSE library version. See **Plain JavaScript** and **Require.js**.
- The HTML-independent route calls `createEncryption` and encrypts a card-data object before sending `adyen-encrypted-data` to the merchant server. Its snippets are illustrations; the page does not establish payment authorization or runtime security of a particular merchant implementation. See **JavaScript only**.

## Detail locators

- **Requirements** — Customer Area CSE public-key location.
- **Merchant hosted** — DOM-capable versus no-DOM library file and form-binding scope.
- **Form template** — field annotations, server handler, encrypted hidden input, generation-time validity and clock qualification, and PCI-related rationale.
- **Plain JavaScript** and **Require.js** — global versus AMD loading and form-binding examples.
- **JavaScript only** — no-DOM library, `createEncryption`, and encrypted-data submission example.

## Related

- [[adyen]]
- [[adyen-card-encryption]] — provider card-encryption concept; its JWE route is separate from this legacy CSE guide.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library/2026-09-15|Classic CSE library hosting (2026-09-15 snapshot)]]
