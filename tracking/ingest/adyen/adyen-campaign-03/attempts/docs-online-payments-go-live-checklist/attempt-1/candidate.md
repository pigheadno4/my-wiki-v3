---
title: "Adyen Online Payments Go-Live Checklist"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/go-live-checklist"
raw_files:
  - "adyen/docs/online-payments/go-live-checklist/2026-09-15.md"
tags: [adyen, online-payments, go-live, live-environment, testing, webhooks]
---

## Overview

This Adyen checklist guides an online-payments merchant through live Customer Area setup and end-to-end checks before accepting live shopper payments. Test Customer Area configuration is not copied to live; account, finance, risk/compliance, API communication, and webhooks each need live configuration. The related [[source-adyen-docs-online-payments-integration-checklist|integration checklist]] places approval of the live-account application before this go-live stage.

## Key takeaways

- Configure live account structure, user access, offered payment methods, and shopper statement details. For finance, provide bank-account details for payouts **from Adyen to the merchant**, review payout settings, and set up reconciliation reporting. A Reserve is presented as optional.
- Review the live risk profile and risk-related notifications, protect against card testing, confirm PCI DSS work, and support 3D Secure where SCA or local rules require it. The page cautions that Mastercard 3D Secure enrollment may take up to 12 hours after live Customer Area activation, so immediate 3DS availability should not be assumed.
- Before live API calls, generate a live API key, check the live credential's permissions, use live endpoints, and reconfigure optional response `additionalData`. Set up live webhooks and any webhook `additionalData`; acknowledge events with a successful HTTP status and check that required event types arrive.
- The final testing section calls for real payment details across the supported lifecycle, including success, refusal, fraud-triggered refusal, refund and partial refund, and conditionally capture/cancel/partial-capture, redirects, 3D Secure, and tokenization. Real-detail payments incur fees. Test on physical iOS and Android devices for touch behavior and in a secure browser context; for custom domains the guide calls for HTTPS. A strict CSP can block native 3DS2 challenges unless needed URLs are allowed; the guide says Adyen does not maintain a complete URL list and suggests redirect 3DS if CSP is not adjusted.
- This page is a readiness checklist, not evidence that a merchant has live-account approval, configured settings, completed real-payment tests, or achieved an authorization, payout, or settlement result.

## Detail locators

- Opening and `## Account` (raw lines 15–49): separate live settings, account structure/users, payment methods, and statement text.
- `## Finance` (raw lines 51–67): merchant payout bank details, payout settings, reconciliation reports, and optional Reserve.
- `## Risk and compliance` (raw lines 69–94): risk profile, PCI DSS, card testing, SCA/3DS support, and Mastercard enrollment timing.
- `## API communication` and `## Webhooks` (raw lines 96–118): live key, permissions, endpoint and additional-data settings, webhook setup/acknowledgment, and event coverage.
- `## End-to-end testing` (raw lines 120–171): physical-device and secure-context conditions, fee warning, real payment cases, and conditional capture, redirect, 3DS/CSP, and tokenization scenarios.

## Related

- Company: [[adyen]]
- Concept: [[adyen-online-payments]]
- Prior approval route: [[source-adyen-docs-online-payments-integration-checklist]]

## Raw Sources

- [[raw/adyen/docs/online-payments/go-live-checklist/2026-09-15|2026-09-15 Adyen online-payments go-live checklist]]
