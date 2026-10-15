---
title: "Adyen Pay by Link iOS app"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/ios-app"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/ios-app/2026-09-15.md"
tags: [adyen, unified-commerce, pay-by-link, ios, payment-links]
---

## Overview

Adyen's 2026-09-15 guide describes the merchant-facing Pay by Link iOS app for creating and managing payment links on an iOS mobile device without development work. The app works with selected Customer Area credentials, merchant accounts and stores. Creating or sharing a link is an offer of an Adyen-hosted payment route; it is not evidence that a shopper paid, that an authorization succeeded, or that funds settled.

## Key takeaways

- The app guide says links created through iOS can offer most Pay by Link methods **except buy now, pay later**. This is an iOS-app claim, not a universal Pay by Link availability rule. Actual account-enabled methods and other eligibility conditions remain separate; see **Requirements** and [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]].
- Before use, the merchant must add terms and conditions to the payment page, add methods to the account, configure Pay by Link creation settings, and give the Customer Area user the **Pay by Link Interface** role. The raw starts from a test Customer Area account; it does not prove live enablement. See **Requirements**.
- At first login, staff select the **test or live** environment, enter Customer Area credentials and choose merchant accounts. The guide says credentials are then encrypted and stored on the device, with Face ID or device passcode for later login. The environment choice and local credential statement do not establish account permission or payment success. See **Log in to the app**.
- The **New payment link** form reflects Customer Area creation settings. The app's **Overview** lists links **created using the app** and filters by link status; staff can share a selected link, show its QR code, or expire it. Do not infer that it lists every link created through Customer Area or API. See **Create a payment link** and **Manage payment links**.
- Staff can change the selected merchant account or store from Settings. To use different Customer Area credentials, they log out and back in. The page also says payment webhook events can be sent by email but gives no delivery or status-contract details here. See **Change the merchant account or store**, **Change user credentials**, and the opening overview.

## Detail locators

- **Requirements** — terms, Pay by Link Interface role, added payment methods and creation settings.
- **Log in to the app** — test/live selection, Customer Area login, chosen merchant accounts, and stored-device-credential statement.
- **Create a payment link** — New payment link screen and settings-dependent form.
- **Manage payment links** — app-created link list, status filters, share/QR/expire operations.
- **Change the merchant account or store** and **Change user credentials** — selection and account-switch steps.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[source-adyen-docs-unified-commerce-pay-by-link]] — broader hosted Pay by Link overview.
- [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] — separate Customer Area/API method matrix.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/ios-app/2026-09-15|Pay by Link iOS app (2026-09-15 snapshot)]]
