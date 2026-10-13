---
title: "Adyen POS Cardholder Verification Methods"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/cardholder-verification-methods"
raw_files:
  - "adyen/docs/point-of-sale/cardholder-verification-methods/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, cardholder-verification, pin, signature, contactless]
---

## Overview

This Adyen POS guide describes cardholder verification methods (CVMs) for credit and debit cards used on Adyen payment terminals in a Terminal API integration. It covers online/offline PIN, PIN bypass, signature handling, the card-encoded CVM list and response result, and contactless limits. The pinned webpage was captured 2026-09-15 and records `last_modified` 2025-11-21; it is not a current limit table or a general PSD2/SCA, wallet device-CVM, or CDCVM specification.

## Key takeaways

- The terminal can verify a shopper's PIN offline with the EMV chip or online with the issuer. Online PIN is enciphered; offline PIN may be enciphered or plaintext. The card's CVM list supplies methods, failure behavior and applicability conditions, and the terminal selects a supported applicable method. The live Mastercard and test-card CVM lists in this guide are examples, not universal card or region rules.
- PIN bypass must be enabled with Adyen Support and applies only to cards that allow it; the guide warns of lost/stolen-card fraud and possible issuer-to-merchant chargeback liability shift. Support is also the route for regional card eligibility and optional on-terminal bypass instructions.
- Major schemes named in the snapshot treat signature as optional for card-present transactions. Terminal prompting depends on configuration and card support; some cards will not prompt even when the setting is enabled. The merchant checks a signature against the card or other identification. In a Terminal API flow, authorization already exists when the signature prompt appears and the terminal approves even if the shopper cancels that screen. A merchant-owned manual check must inspect `CapturedSignature` in `PaymentResponse`; if staff declines, refund is needed unless the merchant has set a capture delay that permits cancellation of the authorization instead. The source recommends that delay, rather than requiring it.
- The POS receives the resulting CVM in hexadecimal `cardHolderVerificationMethodResults`; the second character identifies the CVM using the source's lookup table. Contactless CVM, reader and floor limits are distinct settings. The current CVM limit must be read in Customer Area at **Devices > Device settings > Payment features > Contactless cards**; limits can change and a changed limit arrives at the terminal on a maintenance call. The contactless currency is the country/region currency of the store.
- **Source conflict:** the early PIN section says an above-limit contactless payment always needs online PIN, but the detailed NFC section says the card indicates whether signature or PIN is required after the terminal requests CVM; if PIN is selected, it is Online PIN and that transaction cannot be processed offline. Preserve the detailed condition rather than assuming every above-limit NFC transaction uses PIN. The guide does not explain device-based CVM/CDCVM or translate these terminal CVMs into PSD2 SCA outcomes.

## Detail locators

- `## Requirements`, `## Personal Identification Number (PIN)`, `### PIN bypass` — Terminal API scope, offline/online PIN, changing CVM limit lookup, eftpos magnetic-stripe PIN condition, bypass eligibility and risk.
- `## Signature`, `### Implementing a manual signature check` — optional scheme signature, card support, Customer Area toggle, already-authorized prompt, `CapturedSignature`, staff check, refund and advised capture-delay path.
- `## CVM lists`, `### CVM list live example`, `### CVM list test example` — card-encoded code/type/condition, live Mastercard illustration, test-card amounts in minor units, currency/DCC-dependent selection.
- `## CVM results` — `cardHolderVerificationMethodResults` second-character mapping.
- `## Contactless (NFC) transactions and CVM` — current Customer Area limit, reader/currency/floor settings and the more conditional description of card-selected signature versus online PIN above the CVM limit.

## Related

- Company: [[adyen]]
- POS interface and PaymentResponse context: [[adyen-terminal-api]]
- Separate online-payments SCA/3DS domain: [[adyen-psd2-sca-and-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/cardholder-verification-methods/2026-09-15|2026-09-15 Adyen POS cardholder-verification guide snapshot]]
