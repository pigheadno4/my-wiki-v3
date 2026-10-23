---
title: "Apple Pay certificate"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/apple-pay-certificate"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/apple-pay-certificate/2026-09-15.md"
tags: [adyen, apple-pay, certificates, web, ios]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Apple Pay certificate overview identifies which certificate choice the documented web and native mobile integrations allow. It routes through [[adyen-online-payments]]. It is a channel-selection and setup overview, not a certificate-provisioning procedure or evidence of merchant enablement or payment success.

## Key takeaways

- For **Web Drop-in/Components**, the page allows either the merchant's own Apple Pay certificate or Adyen's certificate. For **iOS Drop-in/Components**, it requires the merchant's own certificate. Its **API-only** comparison likewise allows either certificate on web and requires the merchant's own certificate for a mobile integration; it expressly allows merchant-owned native plus Adyen-certificate web.
- Adyen's certificate option is described for **web** integrations. Its setup path calls for secure Apple Pay server communication, HTTPS on pages containing Apple Pay, a valid domain SSL certificate, and adding Apple Pay in Customer Area with the merchant name/account and shop website URLs. The page says `http://localhost` cannot be used to test this path. After that setup, it points to the separate Web Drop-in or Web Component guides.
- Merchant-owned certificates are necessary for native mobile and optional for web. The page links to separate own-certificate **Web** and **iOS** setup guides; it does not provide their certificate creation, upload or renewal steps here. Adobe Commerce and Salesforce Commerce Cloud plugin users are routed to plugin-specific Apple Pay instructions.

## Detail locators

- [[raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/2026-09-15|Pinned raw]], lines 15–32: purpose, channel-by-channel certificate choice, mixed web/native choice and plugin links.
- Same raw, lines 34–55: Adyen-certificate web option, server/HTTPS/SSL and Customer Area/domain setup, localhost limit and Web Drop-in/Component continuation.
- Same raw, lines 57–73: own-certificate mobile/web scope and navigation to the separate Web and iOS guides.

## Related

- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-web]] — own-certificate Web setup.
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]] — own-certificate iOS setup.
- [[source-adyen-docs-payment-methods-apple-pay-api-only]] — API-only integration guide.
- [[source-adyen-docs-payment-methods-apple-pay]] — Apple Pay overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/2026-09-15|Apple Pay certificate]]
