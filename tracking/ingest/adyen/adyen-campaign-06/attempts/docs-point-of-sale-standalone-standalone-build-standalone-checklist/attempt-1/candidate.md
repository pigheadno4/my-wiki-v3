---
title: "Adyen standalone terminal integration checklist"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/standalone/standalone-build/standalone-checklist"
raw_files:
  - "adyen/docs/point-of-sale/standalone/standalone-build/standalone-checklist/2026-09-15.md"
tags: [adyen, point-of-sale, standalone-terminals, test-checklist, go-live]
---

## Overview

Adyen's standalone checklist organizes a test-environment build for in-person payments initiated on an Adyen terminal without a POS app. It moves from test account/merchant/store structure to printer-equipped test devices, standalone configuration, physical boarding, test transactions and reconciliation, then a separate live-account application and signed contract. The source was fetched 2026-09-15 with raw last-modified metadata 2020-09-25; it is a workflow checklist, not evidence that any merchant has completed setup, payment, refund, reconciliation or live acceptance. [[adyen]] · [[adyen-standalone-terminals]]

## Key takeaways

- **Test-account scope:** Begin with a test account and test Customer Area; choose company/merchant/store structure for business needs. The checklist says to set up the structure again when going live, while the test structure should reflect the intended live one. Stores are conditional on the chosen structure and requested after merchant-account confirmation.
- **Device gate:** Select and order a test card and one or more test terminals with a built-in printer, which the checklist calls mandatory for standalone compliance. Its at-least-four-business-day arrival estimate is from this dated page, not a current delivery promise. Configure standalone mode and needed terminal/payment settings through Customer Area or API; test-terminal pre-assignment to a store is optional.
- **Board and test:** On receipt, follow the model-specific manual for tamper inspection, receipt paper, power, network, boarding and an Adyen-platform connection check. The checklist then asks operators to try test-card payments, manually entered test-card details, in-progress cancellation and refunds; look up transactions in the test Customer Area and check settlement-detail reporting/reconciliation. These are requested test activities, not observed outcomes. The linked standalone-use and configuration guides own exact MKE/MOTO, tipping, refund, passcode and payment-method enablement conditions; this checklist does not make all variants automatic.
- **Live gate:** Completing tests is followed by applying for a live account and signing the contract before taking the standalone solution live. Test account configuration, terminals and simulated transactions do not constitute live activation; live terminals need their separate setup described in the linked standalone setup guide.

## Detail locators

- **Purpose and test/live boundary:** raw lines 15–25; `## Going live` at 145–151.
- **Test structure and conditional store request:** raw lines 27–49, `## 1. Set up your Adyen test account`.
- **Printer requirement, test card/terminal order and dated delivery estimate:** raw lines 51–67, `## 2. Order test payment terminals`.
- **Standalone configuration, inheritance and optional store pre-assignment:** raw lines 69–89, `## 3. Prepare your terminals`. Detailed modes and passcodes belong to the linked setup guide.
- **Physical setup and connection check:** raw lines 91–106, `## 4. Get your terminals up and running`. Use the linked model manual for actual procedure.
- **Test transaction and reconciliation tasks:** raw lines 108–143, `## 5. Test your Standalone solution`; linked use/reporting pages own exact execution and reporting rules.

## Related

- [[adyen-standalone-terminals]] — direct-terminal solution and conditions
- [[source-adyen-docs-point-of-sale-standalone-standalone-build-set-up-standalone]] — separate test-device configuration and live-terminal boundary
- [[source-adyen-docs-point-of-sale-standalone-standalone-use]] — conditional payment, MKE/MOTO, tipping, cancellation and refund operation
- [[adyen-payment-terminals]] — device-manual route for physical setup

## Related raw API references

The checklist's linked account-structure, ordering, model-manual, reporting and go-live pages were not read for this entry. Use their raw sources for procedures and current conditions.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/standalone/standalone-build/standalone-checklist/2026-09-15|Standalone integration checklist, fetched 2026-09-15]]
