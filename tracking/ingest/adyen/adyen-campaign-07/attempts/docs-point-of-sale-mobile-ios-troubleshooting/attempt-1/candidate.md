---
title: "Adyen iOS Mobile POS error handling"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/troubleshooting"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/troubleshooting/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, troubleshooting, pos-mobile-sdk]
---

## Overview

Adyen's iOS Mobile POS error-handling guide, captured 2026-09-15, maps on-device security-attestation messages and public Swift `AdyenPOSError` cases to specific remedies. The enum can be thrown by payment, warm-up, diagnosis or firmware-update SDK calls and applies to both Tap to Pay on iPhone and paired NYC1 card-reader integrations. It is a dated troubleshooting reference for the in-person **iOS Mobile SDK**, separate from the native online-checkout [[adyen-ios-sdk]] and from Android Payments app/App Link flows. It does not establish current device eligibility, merchant entitlement, an actual payment outcome, or whether a failed operation is safe to replay. See [[adyen]], [[adyen-mobile-pos]], and [[adyen-mobile-card-readers]].

## Key takeaways

- A device security message must be resolved before the device is used again. The table distinguishes errors needing a network/security check (`NO_TOKEN`, `OFFLINE_DATA_TAMPERING`, expired offline token, local-time issue) from debugger, recording, screen-capture or overlay conditions to remove locally. `NON_SELF_RESOLVABLE` directs the user to Adyen Support. Its `SYSTEM_CHANGE` row has a crossed-out **Internet needed** indicator but instructs the user to connect to a network after a restart or date/time change; follow the stated action and verify current behavior instead of treating that indicator as definitive.
- `PASSCODE_NOT_ENABLED` says removal of the iOS device passcode cancels the transaction and **all earlier offline Store and Forward transactions performed with the original passcode are lost and cannot be recovered**. The SDK enum's `passcodeDisabled` wording is weaker: saved offline data **may** be lost. Restore a device passcode to resolve the security condition, but do not describe restoration as recovery of those transactions or as a payment result.
- For `AdyenPOSError`, `print(error)` or `error.localizedDescription` may only show an unreadable value such as `AdyenPOSError 6`; `String(describing: error)` yields the localized table message. The table's English text is reference text; actual language can follow card, configured primary/secondary, or device-language precedence.
- Transaction-stage cases are distinct: `malformedTransactionRequest` calls for checking Terminal API request structure; `transactionInProgress` says to wait for the current transaction to finish before starting another. `tooManyRequests` concerns **session-related** request rate and calls for waiting, backoff and review of session establishment. These remedies do not confirm the current transaction's financial status or authorize blind payment retries.
- Reader-only cases cover connection, pairing, battery information and invalid NYC1 firmware; firmware reasons distinguish no reader, no dock, missing delegate, no update available and update/retrieval failures. Tap-to-Pay-only cases distinguish unsupported device/iOS from an app that is not allowed, most likely because the Apple entitlement is missing. SDK lifecycle cases require foreground `warmUp()`, network/passcode checks for installation ID, and a `successScreenTimeout` from 0.5 to 4 seconds. See exact codes and actions in the raw tables before applying a remedy.

## Detail locators

- Security-attestation context, on-device codes, internet indicator and offline-data loss: [[raw/adyen/docs/point-of-sale/mobile-ios/troubleshooting/2026-09-15#Device error messages|Device error messages]] (raw lines 19–41).
- Public Swift enum scope, localized-message behavior and transaction cases: [[raw/adyen/docs/point-of-sale/mobile-ios/troubleshooting/2026-09-15#AdyenPOSError cases|AdyenPOSError cases]] and [[raw/adyen/docs/point-of-sale/mobile-ios/troubleshooting/2026-09-15#Transaction errors|Transaction errors]] (raw lines 43–58).
- NYC1 connection and passcode state, Tap to Pay model/entitlement, SDK lifecycle, and session rate limit: raw lines 60–98 under the corresponding headings. `tapToPayPaymentInterfaceFailure` directs retry and then Support if persistent, without proving payment state.
- Tap-to-Pay education cases and card-reader/dock firmware reasons: raw lines 100–123. Firmware-update retry guidance is about firmware operations, not replaying a payment.

## Related

- [[adyen-mobile-pos]] — primary merchant-device in-person solution hub.
- [[adyen-mobile-card-readers]] — NYC1 reader and dock hardware route.
- [[adyen-terminal-api]] — payment request/response context, separate from this error table.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/troubleshooting/2026-09-15|Adyen iOS Mobile POS error handling, captured 2026-09-15]]
