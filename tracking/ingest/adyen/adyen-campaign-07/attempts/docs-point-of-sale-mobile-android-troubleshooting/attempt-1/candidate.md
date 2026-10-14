---
title: "Adyen Android Mobile solution error handling"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/troubleshooting"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/troubleshooting/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, troubleshooting, security]
---

## Overview

Adyen's Android Mobile error-handling page, captured 2026-09-15, maps two distinct error surfaces: security-attestation/device errors for a merchant integration with the **Android Mobile SDK**, and UI/App Link errors for the separate **Android Payments app** route. It belongs to [[adyen-mobile-pos]], not apps installed on Adyen payment terminals or the [[adyen-android-sdk]] for online checkout. The page gives possible causes and corrective actions for listed codes, not a payment-outcome ledger or proof that a retry is safe.

## Key takeaways

- In the Android Mobile SDK route, Adyen performs regular mobile-device security checks. An attestation issue appears on the device and must be resolved before the device is used again. The device-error table distinguishes whether internet is marked as needed and identifies codes for developer/debug settings, local time change, security token and network checks, SDK update, offline store-and-forward limits, and `INVALID_NYC1_FIRMWARE_VERSION` for the **NYC1 card reader**. `NON_SELF_RESOLVABLE` directs the operator to Adyen Support. Preserve the table's exact code-to-action mapping; an Android device error is not automatically a card-reader error.
- The Android Payments app section is a separate UI/App Link table. Prefixes and descriptions identify onboarding check (`01_...`), boarding (`02_...`), before-payment (`03_...`) and after-payment (`05_...`) contexts for many codes. It covers return URL and encoding, boarding/request tokens, device-bound installation ID (`02_010`), Payments app role or encryption passphrase (`02_003`), Terminal API request encoding/shape/encryption, NFC availability (`03_018`), and response decoding/encryption or transaction-ID extraction after payment. `02_010` specifically requires a new boarding request token for the current device, rather than reuse of one issued to a different device.
- The page recommends restarting onboarding for particular boarding/token/security-credential errors, checking network or request configuration for others, and contacting Support where specified. Those actions are **code-specific**. An after-payment `05_...` response, App Link failure or generic error does not establish whether the financial transaction succeeded; inspect the actual payment state before initiating another payment. The raw's `Try again` wording for `05_004` and `05_009` does not by itself establish an idempotent payment retry.
- The snapshot has internal table inconsistencies that should not be silently corrected: the row labeled `01_105` describes `01_005`; the `SYSTEM_CHANGE` row marks internet as not needed but its action instructs a network connection; `03_020` and `03_021` descriptions refer to boarding; and `05_007`/`05_008` descriptions refer to both before and after payment. Use exact code and observed stage when diagnosing.

## Detail locators

- Raw opening and `## Device error messages` (lines 19–47): Android Mobile SDK attestation identity, device/NYC1 codes, internet-needed column and actions. `ANDROID_NOT_UPDATED` and `SECURITY_PATCH_LEVEL_OUTDATED` say to update the **SDK** in this table; do not silently rewrite that as an OS-update instruction.
- Raw `## Error messages for the Android Payments app` (lines 49–89): Payments app UI/App Link identity and exact error-code table. Rows 55–59 cover return URLs and installation ID; 60–71 cover role/passphrase, boarding tokens, network and device mismatch; 72–85 cover Terminal API request and security-credential failures; 86–89 cover after-payment response/URL failures. The table's possible causes are not guaranteed diagnoses.
- Raw `## See also` (lines 91–93): navigation to Android Mobile solution maintenance; this link alone does not establish maintenance behavior.

## Related

- [[adyen-mobile-pos]] — merchant-device Mobile POS routes and sibling Android build guides.
- [[adyen-terminal-api]] — request and response model referenced by the Payments app error table.
- [[adyen-mobile-card-readers]] — NYC1 reader context, distinct from handset security errors.
- [[adyen-android-terminals]] — separate Adyen payment-terminal app path.
- [[adyen-android-sdk]] — separate native online-checkout SDK.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/troubleshooting/2026-09-15|Android Mobile error handling, fetched 2026-09-15]]
