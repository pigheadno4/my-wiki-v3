---
title: "Adyen Android Payments app build guide"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/build/payments-app"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/build/payments-app/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, payments-app, tap-to-pay, terminal-api]
---

## Overview

This dated Adyen guide builds the **Android Payments app** route for Tap to Pay on an Android mobile device without integrating the POS Mobile SDK. A merchant POS app, installed on the device or browser-based, uses Terminal API messages and Android App Links to a separate Adyen Payments app. This is distinct from the POS Mobile SDK Tap to Pay route, a paired card-reader route, apps deployed to Adyen Android payment terminals, and online Android Checkout SDK flows. See [[adyen-mobile-pos]] for the mobile solution map and [[adyen-terminal-api]] for the message family.

## Key takeaways

- The POS app must integrate Terminal API. The guide requires an Adyen Payments app API key with client key and app role, Support enablement, and an Android COTS device with NFC that is **not** a payment terminal. It sends country/region, method and feature limits to the separate support catalog and hardware/software details to Android system requirements; this snapshot does not establish present eligibility. For a web POS app, the guide also calls for Support-enabled short browser responses and an HTTPS server with TLS 1.2 or higher. See raw § Requirements (lines 23–36).
- Each installed device's Payments app must be boarded. The POS app checks boarding through an App Link; its back end exchanges a `boardingRequestToken` for a one-time `boardingToken` (one-hour validity), bound to the app instance and device; the POS app finishes via an App Link and retains the resulting `installationId`. The merchant-account or store boarding-token endpoint determines where its transactions route; `storeId` differs from a store reference. See raw § 1, especially lines 50–61, 127–173 and 184–239.
- For a transaction, set Terminal API `MessageHeader.POIID` to that `installationId`, encrypt the request with a shared key as for local Terminal API communication, Base64URL-encode it, and send it through the Payments app `/nexo` App Link. The guide says **never call a transaction endpoint directly** for this app route. A device POS app receives an encrypted full Terminal API response and decrypts it; a browser POS app receives an encrypted short result and optional full-result URL. The 30-second shopper-presentation timeout requires a new request. See raw § 2 (lines 247–264, 376–437, 459–518).
- Starting reboarding immediately breaks the prior merchant/store association; that app-device combination cannot take payments until reboarding completes, and a reboarding error requires restarting the flow. Revoke the `installationId` by API when a device is defective, stolen or retired; the guide also describes **Settings → Unregister**. A failed app-instance verification automatically revokes it and requires boarding again. See raw §§ Reboard, Revoke app instance, Verify app instance (lines 520–535, 605–633, 669–681).
- Test and live are separate Payments app packages, API credentials, Management API hosts and App Link bases. The guide's go-live steps require a live account/Customer Area access, a live key with the app role, the live app, enablement and URL changes. Its test-card instructions are test-environment guidance, not evidence of successful execution. See raw §§ Test your solution and Go live (lines 635–667).

## Detail locators

- Raw § 1.1–1.3: status, authentication and finish-boarding App Links, token/ID fields, test URLs and Kotlin examples (lines 63–245).
- Raw § 2: request types, local-protection reference, encryption sample, App Link shape, full and short response decryption examples (lines 247–518).
- Raw §§ Reboard, Revoke app instance and Verify app instance: destructive association change, API/UI revocation and failed-verification consequence (lines 520–633, 669–681).

## Related

- [[adyen-mobile-pos]] — Android mobile solution map and sibling SDK or reader routes.
- [[adyen-terminal-api]] — in-person message structure and encryption context.
- [[adyen-mobile-card-readers]] — separate paired-reader route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/build/payments-app/2026-09-15|Android Payments app guide, fetched 2026-09-15]]
