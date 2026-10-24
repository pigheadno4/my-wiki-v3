---
title: "Adyen UPI React Native Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/upi/react-native-drop-in/2026-09-15.md"
tags: [adyen, upi, react-native, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **UPI-specific additions** for an existing **React Native Drop-in** integration, split by Sessions and Advanced server-side flows. It points to the base guides for the wider payment integration. The page's simulator steps do not establish current UPI eligibility, a live app redirect, or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The stated prerequisites are an existing Sessions React Native Drop-in integration, **Checkout API v68 or later**, and UPI added in Customer Area. The guide says no UPI-specific extra `/sessions` fields or configuration are needed. Its **Integration type** link nevertheless points to an **Advanced-flow** React Native Drop-in URL, while its `/sessions` link points to Sessions; follow the named flow rather than silently accepting that mismatched base-guide link. (raw lines 25–47)
- **Advanced:** The stated prerequisites are existing Advanced React Native Drop-in, additional-action handling labelled **`action.type: await`**, and Customer Area setup. It says no extra UPI configuration, but its `/payments` table requires **`paymentMethod.appId` when `paymentMethod.type: upi_intent`** to identify the shopper's TPAP app. The TEST v72 INR/IN `gpay` request is an example, not an explicit API minimum or live eligibility proof. No separate Advanced minimum is stated. The action-handling link ends in `#handle-the-redirect` even though the row labels the action `await`; keep both exact contexts. (raw lines 71–119)
- **Simulator scope:** In both sections the page says UPI can be tested with Adyen's **Payment Simulator**. It describes UPI Intent redirect to a hosted simulator page, but its QR instruction is expressly **'UPI QR (on web)'**—do not generalize that line into a React Native in-app QR scan guarantee. The tester selects an outcome, checks integration handling, and confirms the corresponding webhook and Customer Area list item. This is a TEST procedure, not an observed outcome. The Advanced `await` row and simulator Intent redirect are different descriptions on the page; neither alone defines every UPI action path. (raw lines 49–69, 75–80, 121–141)
- **Webhook wording:** The simulator checklist spells `eventCode: AUTHORISED`; the separate UPI API-only guide's payment-outcome tables use `AUTHORISATION`. Retain the source-specific spelling mismatch rather than treating this checklist as proof of the actual final webhook schema. A chosen simulator outcome, redirected browser, or Customer Area entry is not itself live authorisation, capture, settlement or refund evidence. (raw lines 64–69, 136–141; [[source-adyen-docs-payment-methods-upi-api-only]])
- The page does not cover UPI Collect migration, recurring UPI AutoPay mandates, a live go-live requirement, or implementation of the base React Native bridge. The payment-modification test link is a recommendation after outcome tests. (raw lines 15–141)

## Detail locators

- Sessions version, Customer Area, base-link mismatch and no-extra-fields/configuration: raw lines 25–47.
- Sessions Intent simulator and Web-only QR wording plus webhook checklist: raw lines 49–69.
- Advanced `await` action/link, conditional `appId` and TEST v72 sample: raw lines 71–119.
- Advanced repeated simulator/outcome checklist: raw lines 121–141.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]
- [[source-adyen-docs-payment-methods-upi-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/react-native-drop-in/2026-09-15|Adyen UPI React Native Drop-in guide, 2026-09-15 snapshot]]
