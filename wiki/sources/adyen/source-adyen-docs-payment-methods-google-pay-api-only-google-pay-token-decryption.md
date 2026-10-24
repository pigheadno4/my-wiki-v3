---
title: "Adyen Google Pay merchant token decryption (historical API-only guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/api-only/google-pay-token-decryption"
raw_files:
  - "adyen/docs/payment-methods/google-pay/api-only/google-pay-token-decryption/2026-09-15.md"
tags: [adyen, google-pay, api-only, token-decryption, pci, online-payments, historical]
---

## Overview

This [[adyen]] guide, last modified and captured **2026-09-15**, describes an **API-only merchant-decryption** path for encrypted Google Pay tokens, after which the merchant passes **raw card details** to Adyen. It says this path is for PCI-compliant merchants and should be handled by the merchant only in advanced setups, such as a need to submit Merchant Plug-In (MPI) data (raw lines 15–35). It belongs under [[adyen-online-payments]]; it is distinct from the [[adyen-card-encryption|Adyen JWE card-encryption route]]. This page does not prove merchant PCI status, key custody, successful decryption or payment authorization.

## Key takeaways

- The stated merchant prerequisites are a **Google Pay merchant ID**, **PCI compliance to handle unencrypted card details**, and an **API-only integration** (raw lines 29–35). This child says “PCI-compliant” without a level, while the separately read [[source-adyen-docs-payment-methods-google-pay|Google Pay overview]] states **PCI DSS Level 1** for merchant-side token decryption (overview raw line 75). Preserve the narrower overview condition when assessing the two historical pages together; neither establishes a merchant's actual compliance or current permission.
- The page delegates cryptographic implementation to **Google's developer instructions**. Its overview sequence fetches Google root signing keys, verifies the intermediate key's signature with a nonexpired root signing key, checks intermediate-key expiry, verifies the payload signature, decrypts **only after signature verification**, then checks `messageExpiration` before using payment details (raw lines 37–49). This is a documented validation sequence, not a demonstrated key operation or complete production security review.
- It distinguishes **FPAN/`PAN_ONLY`** decrypted output (PAN and expiry) from **DPAN/`CRYPTOGRAM_3DS`** output (PAN/expiry plus cryptogram and ECI indicator) (raw lines 51–79). The two `/payments` field tables differ: FPAN marks scheme/card fields, `paymentMethod.brand: googlepay`, source type/tokenized **false** and Ecommerce interaction; DPAN additionally marks MPI `directoryResponse`, `authenticationResponse`, `cavv` from the exact cryptogram and `eci` from the exact indicator, and tokenized **true** (raw lines 81–100, 121–136). FPAN **may** trigger 3D Secure 2 and need extra fields; the page routes that handling to a separate 3DS guide (raw lines 83–87). These field mappings do not establish authentication, authorization or liability shift.
- **Example conflict:** both JSON-like request examples use capitalized `PaymentMethod` whereas the tables name `paymentMethod`; the FPAN example omits a comma and the colon after `shopperInteraction`, and the DPAN example has an omitted comma plus `Shopperinteraction` casing/colon mismatch (raw lines 91–119, 123–161). Placeholder `<PAN>` values and a JavaScript-style comment in the DPAN fenced JSON are further signs that these are illustrations, not runnable validated payloads. Use the exact request schema as separate authority before any implementation.
- The page gives no TEST/LIVE credential or key-rotation steps, response/result code, capture, settlement or recurring-token procedure. Its scope ends at decrypted-field request guidance (raw lines 15–161); no real card data or token operation is evidenced here.

## Detail locators

- Token purpose, PCI and advanced-use qualification: raw lines 15–35.
- Google verification/decryption/message-expiry sequence: raw lines 37–49.
- FPAN versus DPAN example decrypted fields: raw lines 51–79.
- FPAN request fields, possible 3DS2 and flawed example: raw lines 81–119.
- DPAN MPI/cryptogram/ECI fields and flawed example: raw lines 121–161.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-google-pay]]
- [[source-adyen-docs-payment-methods-google-pay-api-only]]
- [[adyen-card-encryption]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/api-only/google-pay-token-decryption/2026-09-15|Full pinned Google Pay token-decryption guide]]
