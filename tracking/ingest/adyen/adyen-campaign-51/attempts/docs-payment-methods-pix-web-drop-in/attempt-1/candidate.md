---
title: "Adyen Pix Web Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pix/web-drop-in/2026-09-15.md"
tags: [adyen, pix, web, drop-in, qr-code, asynchronous-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Pix to an existing Web Drop-in integration. It separates Sessions and Advanced server-side flows, method-specific fields, QR configuration, an Advanced `qrCode` action, refund window, and test/live steps. It supplements [[adyen-online-payments]] and does not establish current merchant enablement, a paid QR code, or a complete final-status integration. [[adyen]]

## Key takeaways

- **Sessions prerequisites and fields:** Start with an existing Web Drop-in Sessions integration, Checkout API **v68 or later**, and Pix added in Customer Area. The method-specific `/sessions` table marks `amount` (final purchase price) required. It lists `shopperName`, CPF/CNPJ `socialSecurityNumber`, `shopperStatement` (maximum **140 characters**), and `lineItems.id`/`amountIncludingTax` without required marks. The table gives line-item limits; the BR/BRL and `pix` values in samples are examples, not a blanket guarantee of eligibility. Its `sessionValidity` sample date is in 2021 and is not a usable current expiration. [Raw: lines 25–92]
- **Sessions UI configuration:** Individually importing `Pix` for tree shaking is optional. The page lists `countdownTime`, a shopper payment countdown starting when the QR loads, default **15 minutes**, and `personalDetailsRequired`, default **false**; setting the latter true requires shopper personal details. The shown `Pix.Configuration()` fragment is fenced as bash while using JavaScript-like assignment and labels `countdownTime` “Required” despite the table showing a default. Treat it as illustrative, not a validated copy-ready Web SDK constructor. [Raw: lines 508–535]
- **Advanced prerequisites and fields:** Start with an existing Web Drop-in Advanced integration that handles `action.type: qrCode` and has Pix added in Customer Area. The `/payments` table marks both `paymentMethod` (from frontend `onSubmit` `state.data.paymentMethod`) and `amount` required. It lists shopper name, CPF/CNPJ, shopper statement, `sessionValidity`, and line-item fields as unmarked; the page advises sending both name and CPF/CNPJ so the shopper can identify the payment. A custom **Advanced** `shopperStatement` must be under **60 characters**, unlike the Sessions table's 140-character maximum. [Raw: lines 563–621]
- **Distinct QR countdown and payment expiry:** Advanced UI configuration again lists a default **15-minute** `countdownTime` after QR display. Separately, its optional `sessionValidity` describes Pix payment expiry default **1 hour for Checkout API v71 or earlier** and **24 hours for v72 or later**. These clocks have different triggers and cannot be treated as one identical expiration. The Advanced code fragment repeats the same “Required”/default and bash/JS ambiguity as Sessions. The Advanced requirement table states no separate API minimum; do not transfer the Sessions v68 statement to it. [Raw: lines 563–601, 612–618]
- **QR response and asynchronous state:** The shown Advanced `/payments` response contains `resultCode: Pending` and `action.type: qrCode` with `qrCodeData`, `paymentData`, `pspReference`, and `pix.expirationDate`. It is a QR-presentation/pending step, not paid or authorized status. The page calls Pix asynchronous but does not give a final webhook/result protocol here; the base integration must supply final-state handling. [Raw: lines 1109–1128, 1139–1152]
- **Refund and environment gates:** The guide says a Pix payment can be refunded within **90 days** through Customer Area or API. In test Customer Area, a pending Pix offer can be manually promoted to a sale for reconciliation testing; paid or promoted test payments appear in Payment list. Before live acceptance, submit a request for Pix in live Customer Area. Manual test promotion is not a live shopper payment. [Raw: lines 538–559, 1131–1152]
- **Example limits:** The Sessions and Advanced request samples include past `sessionValidity` timestamps (2021 and 2025 respectively) and app-scheme `returnUrl` placeholders on this Web page; do not copy them as current expiry or a universal Web return URL. Node examples reference `Config`/`EnvironmentEnum` without shown imports. The Advanced requirement link contains an unresolved encoded `platform` template, while its action-handling link points to a generic redirect anchor despite `qrCode` action text. [Raw: lines 55–92, 264–301, 565–570, 631–668, 858–900]

> [!WARNING] Keep QR presentation and payment finality separate
> The Advanced example is `Pending` with a `qrCode` action, not a completed Pix payment (raw lines 1109–1128). A 15-minute UI countdown is not the same as the version-dependent payment-expiry default (raw lines 593–617), and test offer promotion is not live payment evidence (raw lines 1139–1152).

## Detail locators

- Sessions setup, required/optional fields and request examples: pinned raw lines 25–505.
- Sessions import, UI configuration, refund and test/live instructions: pinned raw lines 508–559.
- Advanced setup, configuration and required/optional fields: pinned raw lines 563–621.
- Advanced request examples and Pending QR action: pinned raw lines 623–1128.
- Advanced refund and test/live instructions: pinned raw lines 1131–1152.

## Related

- [[adyen-online-payments]] — provider integration and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/web-drop-in/2026-09-15|Pix Web Drop-in guide, captured 2026-09-15]]
