---
title: "Adyen Docs: Manual Key Entry on a POS terminal"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/enter-payment-manually"
raw_files:
  - "adyen/docs/point-of-sale/enter-payment-manually/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, manual-key-entry, signature]
---

## Overview

This Adyen Docs guide describes **Manual Key Entry (MKE)** as a fallback when a payment terminal cannot obtain details from a shopper's card chip or magnetic stripe. For its **Terminal API integration with payment terminals**, the merchant POS requests `ForceEntryMode=Keyed`; the terminal asks the **shopper** to enter card number and expiry date and then sign on its display. This differs from the separate MOTO card-not-present flow, where remote order/card details are keyed by staff. See [[adyen-terminal-api]], [[adyen-pci-dss-compliance]], and [[adyen]].

## Key takeaways

- **Risk and prerequisites:** MKE has **no liability shift**; the merchant is fully liable for fraud chargebacks. Contact Adyen Support to enable MKE and configure an **MKE max amount** in Customer Area because of increased chargeback risk. The page gives no universal numeric maximum or merchant-specific enabled state. The integrated instructions apply to Terminal API with terminals; standalone terminal instructions are only linked navigation. [Raw: introduction; Requirements; Set maximum MKE transaction amount]
- **Method boundary:** the page expressly excludes **virtual JCB credit cards** from MKE and directs those to MOTO. It does not provide a broader card-scheme, country, or software-version compatibility table. It does not state a general PCI questionnaire or API-role requirement for MKE; do not import the MOTO page's requirements into this flow. [Raw: Requirements]
- **Request and shopper interaction:** a Terminal API `PaymentRequest` uses `PaymentTransaction.TransactionConditions.ForceEntryMode` with value `Keyed`; the example includes currency and `RequestedAmount`. Once enabled and started from the POS, the terminal prompts the shopper for card number/expiry and then a signature. The example amount and terminal model are illustrative, not a guaranteed limit or eligibility. [Raw: How it works; Make an MKE payment]
- **Response:** the guide identifies `PaymentResult.AuthenticationMethod=SignatureCapture`, `CapturedSignature` coordinates, `CardData.EntryMode=Keyed`, and `AdditionalResponse.posEntryMode=MKE`. These fields describe the documented keyed/signature flow; a signature prompt or example `Result=Success` is not evidence of universal CVM behavior or a live payment outcome. [Raw: Make an MKE payment, response]
- **Risk rules:** the page also points to Adyen risk management and says its classic risk setting can decline at a score of 100. That is configuration-dependent, not a blanket MKE acceptance rule. [Raw: Risk management]

## Detail locators

- Raw `Requirements` locates the Terminal API scope, virtual-JCB exclusion, Support enablement, and max-amount setup.
- Raw `How it works` describes the failed-read fallback and shopper-operated entry/signature sequence.
- Raw `Set maximum MKE transaction amount` locates Customer Area configuration scope.
- Raw `Make an MKE payment` locates `ForceEntryMode`, amount example, and response signatures/entry-mode fields.
- Raw standalone, MOTO, chargeback and risk links are navigation only.

## Related

- [[adyen-terminal-api]] — existing in-person API concept hub
- [[adyen-pci-dss-compliance]] — separate provider PCI scope guidance
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/enter-payment-manually/2026-09-15|Manual Key Entry — Adyen Docs snapshot, 2026-09-15]]
