---
title: "Adyen Classic authorisation with details stored by a third party"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party/2026-09-15.md"
tags: [adyen, classic-api, recurring-payments, card-on-file, third-party-storage]
---

## Overview

This [[adyen]] page describes authorising a payment through an existing Classic integration when payment details are stored with a third party. Storage by that third party is the credential source; the page's requests are new payment authorisations using those details, not an Adyen Vault token-creation or stored-detail lookup procedure. The endpoint is marked inactive and unsupported for new integrations. New integrations are directed to Checkout API, while existing users are told to contact Adyen about migration. See [[adyen-tokenization]] for the wider Adyen-stored token routes and their separate scope.

## Key takeaways

- For the page's Card-on-File/Subscription requests, it lists `amount`, `shopperInteraction`, and `recurringProcessingModel` as fields to pass. It assigns `shopperInteraction=Ecommerce` to the initial payment and `ContAuth` to subsequent payments.
- It assigns `recurringProcessingModel=Subscription` to fixed-schedule payments and `Card On File` to payments without a fixed schedule. The latter spelling is the page's wording; use the current endpoint schema when implementing.
- Initial and subsequent JSON examples include a `card` object with number, expiry, CVC and holder name, plus amount, merchant account, reference and shopper email. These examples show the request shape, not proof that a particular credential is valid, an external vault is configured, or any authorization succeeded. The page does not explain how the third party stores or returns the details.
- This is a Classic endpoint lifecycle warning, not an endorsement for a new build. The raw page gives no payment response or webhook outcome, so it cannot establish a final payment state.

## Detail locators

- **Inactive Classic endpoint and Checkout migration routes:** raw lines 14–21.
- **Third-party-stored detail purpose and named request fields:** raw lines 23–31, under `## Initial Card on file/Subscription payments`.
- **Initial request example:** raw lines 33–52; `Ecommerce` appears at line 49.
- **Subsequent request example:** raw lines 54–75; `ContAuth` appears at line 72.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-authorise-a-recurring-payment]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party/2026-09-15|Classic third-party-stored details authorisation guide — collected 2026-09-15]]
