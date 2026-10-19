---
title: "Adyen Issuing: troubleshoot 3D Secure failures"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/troubleshooting"
raw_files:
  - "adyen/docs/issuing/3d-secure/troubleshooting/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, troubleshooting]
---

## Overview

This Issuing troubleshooting page (last modified 2024-07-04; captured 2026-09-15) describes failed 3D Secure authentication for online payments made with Adyen-issued cards. It separates an authentication failure before authorisation, a temporary card block after repeated failures, and an issuer soft decline when a processing merchant skips required SCA. The processing merchant controls whether to retry a soft-declined payment with 3D Secure. This is issuer-side troubleshooting, not an acquiring checkout flow or proof of a live payment outcome. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The guide requires an Issuing integration. Viewing Customer Area **Payments** and **Transfers** lists requires the **Balance platform base role**. It instructs subscribing to `balancePlatform.transfer.created` and `balancePlatform.transfer.updated` for soft-decline updates.
- For failed 3D Secure authentication, this page says the authorisation is not sent to Adyen, so no relayed authorisation or Payments-list entry appears; it also broadly says “no webhook.” Its remedy is to check 3D Secure enrollment before retrying and contact Adyen Support if the issue persists. **Cross-source warning:** [[source-adyen-docs-issuing-3d-secure-password-otp]] says `balancePlatform.authentication.created` is sent regardless of authentication outcome, including a rejected example. The troubleshooting page's broad no-webhook statement therefore must not be used to rule out that authentication-specific event; distinguish it from transfer/authorisation events.
- The snapshot says Adyen temporarily blocks 3D Secure authentication after **five consecutive failed attempts** and automatically lifts the block after **one hour**. For earlier unblocking, contact Support, which may ask for cardholder ownership information. These are dated operational claims; the page attributes the policy to PSD2 but does not establish current legal requirements.
- If the **processing merchant** skips 3D Secure for a payment requiring SCA, the page says Adyen declines by default. Issuing programs may request soft declines through an Adyen contact. When enabled, Adyen sends a soft decline asking the processing merchant to retry with 3D Secure; merchant retry is its own decision. For this failed authorisation, `balancePlatform.transfer.created` includes a `validationFacts` entry with `type: psd2SoftDeclineCheck` and `result: invalid`; `balancePlatform.transfer.updated` follows status changes, and the attempt can appear in **Transfers**.

## Detail locators

- Raw lines 19–29 identify scope, Customer Area role and transfer-webhook subscriptions.
- Raw lines 31–35 give the pre-authorisation failure description and enrollment/Support remedy.
- Raw lines 37–44 give repeated-failure block threshold, one-hour release and faster Support path.
- Raw lines 46–56 cover skipped SCA, optional soft declines, merchant retry ownership, validation fact, transfer webhooks and Transfers-list visibility.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[source-adyen-docs-issuing-3d-secure-password-otp]] — authentication outcome webhook evidence and conflict.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/troubleshooting/2026-09-15|Adyen Issuing 3D Secure troubleshooting, captured 2026-09-15]]
