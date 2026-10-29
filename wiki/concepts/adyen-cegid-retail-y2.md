---
title: "Adyen Cegid Retail Y2 Integration"
type: concept
category: technology
tags: [adyen, cegid-retail-y2, point-of-sale, terminal-api, retail]
---

## Definition

Adyen's Cegid Retail Y2 CPOS plugin connects the Retail Y2 POS system with Adyen payment terminals through Terminal API for in-person payments. The 2024-modified overview captured 2026-09-15 states compatibility with Retail Y2 v11.05 and later, recommends local POS-to-terminal communication, and allows a cloud route after contacting Support. [[source-adyen-docs-plugins-cegid-retail-y2]]

## Scope and prerequisites

The overview lists in-store payment features and routes separately to setup, gift cards, optional Tap to Pay and Pay by Link for Cegid Retail Mobile POS on iOS or Retail Live Store on Android. It starts from Adyen onboarding and a test account while live credentials are pending. Child guides own merchant/terminal configuration, feature eligibility, supported market/method details and actual test/go-live procedure.

## Evidence boundary

The host-version floor is not an exact CPOS package release or current device/method matrix. A linked all-terminals or all-terminal-methods statement is not universal merchant, country, terminal-software or feature enablement. Feature descriptions and setup navigation do not establish authorization, capture, settlement or bank receipt for a particular payment. This Cegid product route is separate from generic Terminal API implementations.

## Sources

- [[source-adyen-docs-plugins-release-notes]] — 2019–2026 captured Cegid Retail Y2 CPOS release history, including version-qualified installation and the v2.1.12 receipt/reconciliation issue marked fixed in v2.1.13.


- [[source-adyen-docs-plugins-cegid-retail-y2-pay-by-link]] — 2026-09-15 Cegid Retail Y2 Mobile POS/Live Store Pay by Link guide for versioned prerequisites, Cegid activation, hosted-page terms, QR/text link access and in-app result; link presentation is not payment proof.


- [[source-adyen-docs-plugins-cegid-retail-y2-giftcards]] — 2023-modified, 2026-09-15-captured CPOS guide to Cegid gift-card operations, keypad buttons, payment-method mapping and EPT provider/entry-mode configuration.


- [[source-adyen-docs-plugins-cegid-retail-y2-tap-to-pay]] — 2026-09-15 Cegid mobile Tap to Pay guide separating iPhone iOS Mobile SDK/InStoreHub/v18+ from Android Payments app credentials, merchant/store IDs, Support enablement and device-security gates; setup is not payment proof.


- [[source-adyen-docs-plugins-cegid-retail-y2-troubleshooting]] — 2023-modified, 2026-09-15-captured CPOS/MPOS diagnostics for references, refund setting, DRV/DCPP logs, version/TLS, local URL and Tap to Pay 403/903/store-session routing; conditional remedies are not payment proof.


- [[source-adyen-docs-plugins-cegid-retail-y2-set-up-the-plugin]] — Cegid Retail Y2 CPOS plugin v2.1.33 setup guide: installation, local/cloud Terminal API configuration, mapping, refund settings, and test-to-live checklist.


- [[source-adyen-docs-plugins-cegid-retail-y2]] — Cegid Retail Y2 CPOS plugin overview, v11.05+ host scope, communications choices, feature list and test/live setup navigation (2026-09-15 snapshot).

## Related

- [[adyen]]
- [[adyen-terminal-api]]
