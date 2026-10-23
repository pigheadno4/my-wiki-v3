---
title: "Decrypt Apple Pay tokens"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/api-only/apple-pay-token-decryption"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/api-only/apple-pay-token-decryption/2026-09-15.md"
tags: [adyen, apple-pay, api-only, token-decryption, pci, card-data]
---

## Overview

This 2024-modified, 2026-09-15-captured [[adyen]] guide contrasts Adyen-decrypted Apple Pay tokens with **merchant-side decryption in an advanced API-only integration**. It belongs with [[adyen-online-payments]]. Its token and request examples explain data handoff; they do not evidence Apple Pay merchant eligibility, completed authentication, authorization, capture or settlement.

## Key takeaways

- The guide says a PCI-compliant merchant can choose whether Adyen or the merchant decrypts; a merchant **not PCI compliant must let Adyen handle decryption**. It advises merchant decryption only for advanced setups such as submitting MPI data. Self-decryption further requires an eligible Apple Developer account, the merchant's own Apple Pay certificate, PCI compliance for unencrypted card details, and API-only integration. PCI status is a prerequisite claimed by the guide, not established by this source.
- For **Adyen decryption**, in-app PassKit supplies `payment.token.paymentData` in the `PKPayment` callback; the code base64-encodes that data. Web receives token data in `onpaymentauthorized`; the example JSON-stringifies `event.payment.token.paymentData` and base64-encodes it. The merchant passes the encoded data through its server as `paymentMethod.type: applepay` and `applePayToken` in Checkout `/payments`. In-app and web encoding examples are distinct. The sample API endpoint is **test v72**, with illustrative amounts/currencies and library versions; submitting a token is not a payment outcome.
- For **merchant decryption**, the guide says verify the Apple Pay certificate before decrypting, select the matching merchant certificate/private key using `publicKeyHash`, recover/decrypt the symmetric data, check `transactionId` against already processed payments to avoid duplicate credit, and verify original transaction details. These are stated responsibilities, not a complete independently validated cryptographic procedure; the detailed method is delegated to Apple's token-format reference.
- The decrypted **customer-initiated** mapping includes card expiry/name/PAN from token fields and MPI authentication/CAVV/directory/ECI values. The table marks `mpiData.eci` with a required icon **but its description explicitly allows omission when `eciIndicator` is absent**; preserve that condition. The **merchant-initiated** table lists the card-data mapping without the customer-initiated MPI fields; its example adds `Subscription`, `ContAuth`, `networkTxReference`, shopper IP and billing address, which should not be promoted to universal table requirements.
- The decrypted-payment curl examples show masked `number` values and dated expiry placeholders, despite the table directing use of the token's `applicationPrimaryAccountNumber`. They are redacted illustrations, not copy-ready live payloads or permission to handle raw PAN outside the stated PCI/API-only conditions.

## Detail locators

- [[raw/adyen/docs/payment-methods/apple-pay/api-only/apple-pay-token-decryption/2026-09-15|Pinned raw]], lines 15–29: token purpose, PCI branching and advanced-use limit.
- Same raw, lines 31–72 and 363–402: Adyen-decryption in-app and web encoding/handoff, with test `/payments` examples; lines 74–691 contain language-specific request samples.
- Same raw, lines 693–717: merchant-side prerequisites, certificate/key/decryption, duplicate transaction ID and original-payment checks.
- Same raw, lines 719–767: customer-initiated field table and sample, including `eciIndicator` exception and redacted PAN; lines 769–813: merchant-initiated table and sample.

## Related

- [[adyen-pci-dss-compliance]] — compliance context for raw card data handling.
- [[adyen-card-encryption]] — distinct card-data encryption context.
- [[source-adyen-docs-payment-methods-apple-pay]] — Apple Pay channel/certificate overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/api-only/apple-pay-token-decryption/2026-09-15|Decrypt Apple Pay tokens]]
