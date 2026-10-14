---
title: "Adyen Docs: QR code wallet payments at point of sale"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/qr-code-wallets"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/qr-code-wallets/2026-09-15.md"
tags: [adyen, point-of-sale, qr-code-wallets, terminal-api, referenced-refunds]
---

## Overview

This Adyen POS guide describes QR code wallet payments through a payment terminal or standalone solution. A merchant-presented QR code can be selected on the terminal or launched by the POS app; alternatively, the POS can scan a code shown in the shopper's wallet app. These routes differ in request data, hardware, supported wallets, and shopper experience. The page was last modified in 2021 and captured on 2026-09-15; its wallet list and examples do not establish current wallet, region, merchant-account, or device availability or a successful live payment. [[adyen]] [[adyen-pos-alternative-payment-methods]] [[adyen-terminal-api]]

## Key takeaways

- The guide lists a Terminal API integration with payment terminals or a standalone solution, requires adding the QR method to the Adyen account, and calls for Greek-bank onboarding for IRIS. The supported-wallet listing is a separate linked overview, so this page's `AllowedPaymentBrand` values should be treated as a dated request reference, not a live eligibility matrix. See **Supported wallets** and **Requirements**, pinned raw lines 19–33.
- **Initiate from terminal:** send a standard payment request; staff or shopper selects the terminal's QR icon and a wallet from the displayed menu, then the shopper scans and verifies the terminal's QR code. The page says this flow requires no extra integration work beyond a card-payment-capable integration and is also used for standalone terminals. That statement is specific to this path, not all QR wallets or account setup. See **QR code payment flows** and **Initiate from terminal**, pinned raw lines 39–47 and 63–85.
- **Initiate from POS app:** the POS specifies the shopper's wallet in `PaymentRequest.PaymentTransaction.TransactionConditions.AllowedPaymentBrand` to launch that wallet's QR code directly on the terminal. The shopper scans and verifies; the payment then goes to Adyen for processing and the POS receives a payment result. The listed brand strings and EUR Alipay request are examples from this dated page. See **Initiate from POS app**, pinned raw lines 87–170.
- **Initiate from barcode scanner:** the shopper presents a code from the wallet app; the POS must have a QR-capable scanner/camera, translate the code to a numeric value, and send it as `StoredValueID` with `StoredValue`, `Other`, `Scanned`, and `BarCode` instrument fields. AlipayHK additionally uses `AllowedPaymentBrand: alipay_hk`. The page excludes Affirm, Atome, IRIS, PayMe, PayNow, PayPay, PIX, Rakuten Pay, TWINT, and Zip from this path. The guide says the shopper need not have active internet for this scanner path; it does not claim the POS or terminal can process offline. See **QR code payment flows** and **Initiate from barcode scanner**, pinned raw lines 53–59 and 172–305.
- The terminal- and POS-generated QR test flow is automatically `Approved` after 15 seconds in the described test integration, with IRIS test result depending on amount; the scanned-code test flow is described as immediately `Approved`. These are test fixtures, while the live flow requires reading the returned payment result. This page does not specify QR expiry, cancellation, asynchronous notification, or a universal final-status timer. See pinned raw lines 77–83, 162–168 and 305–319.
- QR code wallets in this guide support only referenced refunds: send a `ReversalRequest` against the original payment. Full and partial referenced refunds are allowed. The page does not describe an unreferenced refund path. See **Refunds**, pinned raw lines 311–315.

## Detail locators

- **Supported wallets** (pinned raw lines 19–23) — route to a separate payment-method overview.
- **Requirements** (pinned raw lines 25–33) — Terminal API or standalone, account setup, IRIS onboarding.
- **QR code payment flows** (pinned raw lines 35–61) — terminal menu, POS app direct launch, shopper-code scanner, excluded scanner wallets, and shopper connection qualification.
- **Initiate from terminal** (pinned raw lines 63–85) — terminal selection, shopper verification, test-only result, and normal response route.
- **Initiate from POS app** (pinned raw lines 87–170) — `AllowedPaymentBrand` values, illustrative request and test-only result.
- **Initiate from barcode scanner** (pinned raw lines 172–309) — scanner/numeric-code prerequisite, `PaymentInstrumentData`, AlipayHK exception, example payloads, and result.
- **Refunds / Testing** (pinned raw lines 311–319) — referenced full/partial `ReversalRequest` and simulator route.

## Related

- [[adyen-pos-alternative-payment-methods]] — POS alternative-method families.
- [[adyen-terminal-api]] — message structure and terminal result handling.

## Related raw API references

These links are navigation in the pinned guide, not independently reviewed evidence for this entry:

- Supported QR code wallets — https://docs.adyen.com/point-of-sale/what-we-support/payment-methods#qr-code-wallets
- Standard Terminal API payment/result — https://docs.adyen.com/point-of-sale/basic-tapi-integration/make-a-payment
- Referenced refunds — https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/referenced
- Testing QR code wallets — https://docs.adyen.com/point-of-sale/testing-pos-payments#testing-qr-code-wallets

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/qr-code-wallets/2026-09-15|Adyen POS QR code wallet guide, fetched 2026-09-15]]
