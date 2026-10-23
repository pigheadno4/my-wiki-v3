---
title: "Adyen Apple Pay error handling"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/handle-apple-pay-errors"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/handle-apple-pay-errors/2026-09-15.md"
tags: [adyen, apple-pay, errors, online-payments]
---

## Overview

Adyen troubleshooting guide for selected Apple Pay API, web merchant-validation, Adobe Commerce and `/applePay/sessions` errors. Its metadata says last modified 2023-07-05; this raw was captured 2026-09-15. Each remedy is tied to a named symptom and integration path. It does not establish present provider configuration, a valid live certificate, successful authentication or payment outcome.

## Key takeaways

- API error `5_001` says the Apple Pay-authorized amount and Adyen-authorized amount differ; verify transaction amounts. The page notes Discover and American Express **test** cards support only USD. Error `5_002` says the API-submitted token does not conform to specification; the `/payments` custom-integration example says to stringify and base64-encode `payment.token.paymentData` as `applePayToken`. These are error-specific checks, not universal instructions for all Apple Pay integrations (raw lines 21–44).
- Error `5_004` says the Apple Pay encryption key is correct but the decrypting private key is not configured for the Adyen API credential. Check that the payment processing certificate used the same API credential, the app/site uses the linked merchant identifier, and the latest certificate was activated in Apple Developer Portal after Adyen confirmation. Also check test-to-live merchant identifier and avoid a test card in live. This concerns Adyen credential/certificate mapping, not a prompt to expose or handle private keys (raw lines 46–71).
- `CSR algorithm/size incorrect. Expected: RSA(2048)` appears while creating a **web merchant identity** in Apple Developer Portal. The page says not to use Adyen’s CSR for that merchant identity certificate; generate the separate CSR using its web merchant-identity route. Do not conflate it with the payment processing certificate checks above (raw lines 73–81).
- For web “Payment Not Processed,” check validated domain, its link to the merchant identity certificate, `onValidateMerchant`/`validationUrl`, matching verified-domain `initiativeContext`, Apple server requirements and Safari Web Inspector errors. The Adobe Commerce case separately points to `adyen_exception.log`, PEM location, merchant identifier/domain and network status (raw lines 83–112). These are diagnostics, not proof of repair.
- The `422 Unauthorized to process transactions on behalf of merchantId` case concerns `/applePay/sessions` merchant-session retrieval. The page says SDK 3.18.0+ and API v65+, a `merchantId` in `/paymentMethods` configuration, and then distinguishes Drop-in/Components (pass the full `/paymentMethods` response and add all shop domains in Customer Area) from API-only (include required session parameters). If 422 remains, it directs each route to Support with its full `/applePay/sessions` request for URL enrollment and merchantIdentifier review (raw lines 114–141).

## Detail locators

- API errors `5_001`, `5_002`, `5_004`: raw lines 21–71.
- Separate web merchant-identity CSR error: raw lines 73–81.
- Web payment-sheet and Adobe Commerce troubleshooting: raw lines 83–112.
- Versioned 422 merchant-session troubleshooting by Drop-in/Components versus API-only: raw lines 114–141.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/handle-apple-pay-errors/2026-09-15|Adyen Apple Pay error guide snapshot]]
