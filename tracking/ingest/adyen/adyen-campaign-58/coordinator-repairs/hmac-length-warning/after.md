---
title: "Adyen Classic Platforms HMAC-signed notifications"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/configure-notifications/signing-notifications-with-hmac"
raw_files:
  - "adyen/docs/classic-platforms/configure-notifications/signing-notifications-with-hmac/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, hmac, security]
---

## Overview

This 2023-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes optional HMAC signing for notifications from Notifications v5 onward. Basic authentication is the stated default; HMAC adds an integrity check using a shared secret. The page points integrations built after 2022-08-01 to a separate new-integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Supply an HMAC signature key while subscribing with `/createNotificationConfiguration` to receive signed notifications at the configured URL; the example is a test Notification API v6 call with endpoint credentials (raw lines 19–25, 27–35, 37–82). The source says a payment-notification key may be reused. If a new key is generated, previous notifications remain signed with the previous key, so verification of older deliveries needs the appropriate previous key (raw lines 29–31).
- For each incoming notification, take `HmacSignature` and `Protocol` from HTTP headers. The page says only SHA256 is supported; compute HMAC over the whole, original HTTP request body with the shared key and compare with the header signature before deserializing. JSON element reordering after deserialization may otherwise make a valid signature fail (raw lines 84–90). Its Java sample uses `HmacSHA256`, UTF-8 payload bytes and Base64 output (raw lines 109–157).
- The page calls the key a **32bit hexadecimal** HMAC key, but its subscription and Java examples show a 64-hex-character key. This is a material size/terminology mismatch; do not derive a key-length rule from the wording alone (raw lines 29, 54, 114–115).
- The subscribe prose says the example activates `ACCOUNT_HOLDER_VERIFICATION`, whereas the request and response `eventConfigs` specify `ACCOUNT_CREATED`. Treat the sample as an illustration of configuration fields, not proof that the verification event is included by that request (raw lines 35, 48–53, 71–76). The example key and credentials are illustrative, not values to reuse.

> [!warning] Contradiction
> This guide's **32bit** wording differs from the separately captured Notification Configuration API v6 [[source-adyen-api-explorer-notificationconfiguration-latest-post-createnotificationconfiguration]] and [[source-adyen-api-explorer-notificationconfiguration-latest-post-getnotificationconfiguration]], which specify a **32-byte hex-encoded string**, explicitly 64 hexadecimal characters. Keep that API requirement distinct from this guide's wording and examples; the mismatch is retained rather than silently normalized.

## Detail locators

- Notifications v5+ and post-2022 integration boundary; default basic authentication and optional HMAC: raw lines 19–25. Key wording, reuse and rotation caveat: raw lines 27–31.
- Subscription description, test v6 request, example event config and response: raw lines 33–82. Header fields, SHA256, whole-body comparison before deserialization: raw lines 84–90. Java and sample-header mechanics: raw lines 92–174.

## Related

- [[adyen-classic-platforms]] — older platform model.
- [[adyen-webhooks]] — general webhook context; do not assume its signature format applies to this Classic notification route.
- [[source-adyen-docs-classic-platforms-verification-process]] — account-holder verification events and status.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/configure-notifications/signing-notifications-with-hmac/2026-09-15|Classic HMAC notification signing, captured 2026-09-15]]
