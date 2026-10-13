---
title: "Adyen Docs: MOTO payments on POS terminals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mail-and-telephone-order-moto"
raw_files:
  - "adyen/docs/point-of-sale/mail-and-telephone-order-moto/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, moto, card-not-present, avs]
---

## Overview

This Adyen Docs guide describes **Mail Order/Telephone Order (MOTO)** as a **card-not-present** transaction where a shopper gives order and card details by regular mail (not email), fax, or telephone. In its Terminal API path, a POS payment request carries the `MOTO` tender option and the payment terminal prompts **staff** to key in the card number and CVC. The page also covers a standalone-terminal path and mentions virtual JCB cards. A terminal used for manual entry does not make the shopper/card present, and this is not an ordinary online Checkout API flow. See [[adyen-terminal-api]], [[adyen-pci-dss-compliance]], and [[adyen]].

## Key takeaways

- **Enablement and compliance:** the stated integration types are Terminal API with payment terminals or standalone. The page requires completing PCI DSS **Self-Assessment Questionnaire B-IP** as part of the commercial contract. Selected merchants can enable `Allow MOTO payments` themselves in Customer Area; otherwise contact Support. A `MOTO max amount` can be configured. Adyen for Platforms must assign terminals to a store configured with the legal entity's business line. AVS and optional capture delay need separate configuration. These instructions do not prove a specific merchant has MOTO enabled or meets PCI scope. [Raw: Requirements; Configure MOTO, AVS, and capture delay]
- **Fraud and verification:** the guide calls MOTO insecure, says there is **no liability shift**, and assigns the merchant full liability for fraud chargebacks. Optional AVS prompts staff for the shopper's postal code and house number; the issuer may authorize despite incomplete address match. AVS support is listed for American Express, Discover, Mastercard, and Visa, and other issuers in the US, UK, and Canada; AVS checks are unavailable on Android and legacy payment terminals. A configured capture delay can allow cancellation after reviewing the AVS result. [Raw: Risk management; Address verification service; Requirements]
- **Terminal API request and response:** for an integrated POS, put `tenderOption=MOTO` in `SaleData.SaleToAcquirerData`, either as a key-value pair or Base64-encoded JSON. Staff then enter PAN and CVC on the terminal; if AVS is enabled, they enter address data there too. The `PaymentResponse` identifies keyed entry and `posEntryMode=MKE`; configured AVS data appears as `avsResult` and `avsResultRaw`. The sample request/response values and Java code illustrate the flow, not card-scheme, merchant, or environment eligibility. [Raw: Make a MOTO payment]
- **After authorization:** an inconclusive AVS check can coexist with issuer authorization. The merchant must decide whether to trust the transaction; the guide says to cancel the authorization if not, and that an uncancelled payment will be captured. It specifically warns that cancelling a MOTO authorization changes status to `SentForRefund`. For standalone MOTO with AVS, the terminal presents an Approve/Decline choice after an issuer non-decline; selecting Decline leads Adyen to cancel authorization or refund if already captured. [Raw: Address verification service; Make a MOTO payment]
- **Boundary:** this page does not specify a universal API role, cardholder verification method outcome, or global AVS availability beyond its stated issuer/terminal regions. Its online/point-of-sale AVS test-card link and related pages are navigation, not evidence of production behavior. [Raw: Requirements; Testing MOTO payments; See also]

## Detail locators

- Raw `Requirements`, `Risk management`, and `Address verification service` carry the PCI, liability, issuer/region, terminal-model, and Platforms setup qualifications.
- Raw `Configure MOTO, AVS, and capture delay` locates the Customer Area toggle, optional max amount, additional-data options, and capture-delay route.
- Raw `Make a MOTO payment` locates the two tender-option encodings, manual terminal entry, keyed response, AVS result, and cancellation behavior.
- Raw `Testing MOTO payments` and `See also` contain separate test-card/detail links, treated here as navigation only.

## Related

- [[adyen-terminal-api]] — existing in-person Terminal API concept hub
- [[adyen-pci-dss-compliance]] — provider PCI scope concept
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mail-and-telephone-order-moto/2026-09-15|MOTO — Adyen Docs snapshot, 2026-09-15]]
