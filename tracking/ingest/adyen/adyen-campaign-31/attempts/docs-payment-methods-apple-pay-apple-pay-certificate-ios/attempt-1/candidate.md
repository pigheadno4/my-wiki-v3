---
title: "Adyen own Apple Pay payment processing certificate for iOS"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/apple-pay-certificate/ios"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/apple-pay-certificate/ios/2026-09-15.md"
tags: [adyen, apple-pay, ios, certificates, payments]
---

## Overview

This [[adyen]] guide, last modified 2023-11-24 and captured 2026-09-15, describes setting up a merchant-owned **Apple Pay payment processing certificate** for a native iOS mobile integration. It applies to an existing iOS Drop-in or Components integration using Advanced or Sessions. The merchant creates Apple merchant identifiers and the certificate through Apple, then supplies the certificate to Adyen for decryption and payment processing. It is a configuration and renewal guide, not evidence of current Apple Pay entitlement, live enablement or a successful payment. See [[adyen-online-payments]].

## Key takeaways

- **Access and prerequisites:** The guide requires a Customer Area user with **Merchant admin** or **Manage API Credentials** and an Apple Developer account in the Developer or Enterprise Program. It separately recommends an Apple **Account Holder** or **Admin** user with a group inbox/distribution-list email so expiry notifications reach the team; that notification setup is distinct from the required Customer Area role. The iOS Drop-in/Components Advanced-or-Sessions integration is a prerequisite. See pinned raw lines 21–31.
- **Identifiers, capability and certificate roles:** Create separate Apple merchant identifiers for **test** and **live** transactions, even though the page says one identifier can be reused across multiple websites and iOS apps within an environment. Enable Apple Pay capability for the app. For each merchant identifier, generate a CSR through the Adyen Customer Area record of the **web service user that executes Apple Pay transactions**, use that CSR in Apple Developer to create the payment processing certificate, and upload the resulting CER to the corresponding identifier for that web service user. Apple Pay encrypts payment information with this certificate; Adyen needs it to decrypt and process the payment. The page instructs answering **No** if Apple asks whether the Merchant ID's payments are processed exclusively in China; this is source-dated setup wording, not a current regional eligibility determination. Then add Apple Pay to the relevant merchant account in Customer Area. See pinned raw lines 33–87 and 161–166.
- **Renewal and overlap:** The source says certificates must be renewed at expiry. Its renewal path creates a new CSR under the relevant web service user, matches the `KeyID` with an **Input needed** certificate record, uploads the new CER and activates the certificate in Apple's Developer Portal. The old certificate remains in use until Apple activation, and can continue to be used for **about four hours** afterward during rollout; do not assume immediate cutover. See pinned raw lines 89–119.
- **Check the certificate in use:** The guide shows how to decode the Base64 JSON `paymentMethod.applePayToken` from a `/payments` request and compare the token header's `publicKeyHash` (containing `KeyID`) against the relevant web service user's certificate records. Seeing the old `KeyID` during rollout does not by itself indicate failed setup; the guide treats a new `KeyID` on an **authorized** payment as confirmation of its setup steps. This is certificate-use evidence, not proof of capture, settlement or payout. The page also gives the Customer Area route for removing the old certificate; treat removal as a separate lifecycle action after checking the rollover. See pinned raw lines 117–159. The token strings shown are placeholders, not credentials or a safe token-handling implementation.

## Detail locators

- Requirements and distinct Customer Area versus Apple Developer roles: pinned raw lines 21–31.
- Four setup phases, test/live merchant IDs, CSR and web service user route: pinned raw lines 33–64.
- iOS capability, Apple payment processing CER, China prompt and upload: pinned raw lines 66–87.
- Renewal, `KeyID` matching, Apple activation and approximately four-hour overlap: pinned raw lines 89–115.
- Token-header check, rollout interpretation and old-certificate removal path: pinned raw lines 117–159.
- Customer Area Apple Pay addition with merchant account and identifier: pinned raw lines 161–166.

## Related

- [[adyen-online-payments]] — main online-wallet integration route.
- [[adyen-ios-sdk]] — separately versioned iOS Apple Pay client runtime and server boundary.
- [[source-adyen-docs-payment-methods-apple-pay]] — Apple Pay overview and channel routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/ios/2026-09-15|Merchant-owned Apple Pay certificate for iOS, captured 2026-09-15]]
