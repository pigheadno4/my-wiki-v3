---
title: "Adyen Pay by Link in Cegid Retail Y2 Mobile POS and Live Store"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2/pay-by-link"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/pay-by-link/2026-09-15.md"
tags: [adyen, cegid-retail-y2, pay-by-link, mobile-pos, live-store]
---

## Overview

This Cegid Retail Y2 guide covers using Adyen **Pay by Link** from **Cegid Retail Mobile POS** or **Cegid Retail Live Store** for an in-store shopper. A store employee selects Pay by Link; the shopper opens the link by QR scan on a personal device or via a received text message, completes checkout on an Adyen-hosted payment page, and the employee receives a payment result in the Cegid app. The link offers a route to methods unavailable on the payment terminal, with method support governed by the separate Pay by Link documentation. Link creation, presentation or result display is not itself proof of authorization, capture, settlement or funds receipt for a particular order.

## Key takeaways

- The listed shared prerequisites are **Cegid Retail Y2 InStoreHub** on Windows with the CPOS plugin, **Retail Y2 v18 or later**, and an Adyen payment terminal. For **Retail Mobile POS**, the page additionally requires **Mobile POS 5.1.607 or later** and an **iOS mobile device**. For **Retail Live Store**, it lists an Android or iOS mobile device or any browser-capable device. These are separate app/device conditions, not a universal method or market eligibility statement.
- The user flow is the same in both Cegid apps, but setup differs. Mobile POS activation requires contacting a Cegid representative, following Cegid extension documentation, and adding purchase terms and conditions to the Adyen-hosted payment page under the linked Pay by Link requirements. For Live Store enablement, contact a Cegid representative. This guide does not specify API credentials, permissions, SMS sender/delivery guarantees or account-level method configuration.
- The QR and text-message branches describe ways the shopper reaches a link; the page does not establish which method is offered to a particular shopper or prove text delivery. The secure hosted page is where the shopper completes a payment attempt; the app receives a result, whose status and later financial lifecycle must be checked in the applicable payment records.

## Detail locators

- Raw lines 15–27: Cegid app scope, in-store link purpose and separate method-support route.
- Raw lines 29–37, `Requirements`: InStoreHub/CPOS, Retail Y2, terminal, Mobile POS iOS/version and Live Store device conditions.
- Raw lines 39–50, `How it works`: employee selection, shopper QR/text navigation, hosted checkout and app result.
- Raw lines 52–65, `Set up Pay by Link`: distinct Mobile POS extension/terms and Live Store representative steps.

## Related

- [[adyen]] — provider context.
- [[adyen-cegid-retail-y2]] — CPOS integration and Cegid feature routing.

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/pay-by-link/2026-09-15|Cegid Retail Y2 Pay by Link, fetched 2026-09-15]]
