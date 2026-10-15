---
title: "Adyen Classic API store payment details"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/store-payment-details"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/store-payment-details/2026-09-15.md"
tags: [adyen, classic-api, tokenization, recurring-payments, stored-payment-methods]
---

## Overview

This dated [[adyen]] Classic API page describes creating a stored recurring detail as part of an `/authorise` payment request or HPP payment-session form. It says successful payment causes the details to be stored and a `recurringDetailReference` to be created for later use. The page labels this endpoint inactive and unsupported for new integrations, directing new builds to Checkout API and existing users to contact Adyen about migration. Use [[adyen-tokenization]] for the broader current tokenization concept.

## Key takeaways

- The page maps `recurringProcessingModel` to three named cases: `Subscription` for a fixed schedule, `CardOnFile` for payments without a fixed schedule, and `UnscheduledCardOnFile` for non-fixed-schedule use of stored card details such as automatic top-ups. It does not further resolve the overlap between the latter two descriptions.
- Each shopper needs a unique `shopperReference`; the page states a maximum of 100 stored card details per reference. The page ties retrieval of a stored recurring detail to the `shopperReference` used for that recurring contract.
- Illustrative `/authorise` JSON, SOAP, cURL, and library requests include card data, shopper reference, `recurring.contract` with `RECURRING` and `ONECLICK`, and `recurringProcessingModel=Subscription`. This combined example is not a rule that `ONECLICK` and `Subscription` are interchangeable or that every subsequent payment has the same initiation pattern.
- For a later payment, the page says `selectedRecurringDetailReference` can name a `recurringDetailReference` obtained from stored details for the original `shopperReference`, or use `LATEST` for a recent detail. It also states an `AUTHORISATION` webhook with `success=true`; neither the example requests nor that sentence proves an actual merchant payment or token creation in this snapshot.
- This Classic page does not describe a shopper-consent step. Consult [[source-adyen-docs-online-payments-tokenization-create-tokens]] for the separate token-creation guidance on consent; do not use this omission to infer that consent is unnecessary.

## Detail locators

- **Inactive Classic scope and migration:** raw lines 14–21.
- **Storage condition, processing models, and shopper-reference limit:** raw lines 23–31.
- **Illustrative `/authorise` request formats and contract/model fields:** raw lines 33–487; these are examples rather than confirmed execution results.
- **Later `selectedRecurringDetailReference` and webhook note:** raw lines 489–495.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[recurring-payments]]
- [[source-adyen-docs-online-payments-tokenization-create-tokens]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/store-payment-details/2026-09-15|Adyen Classic API store payment details — collected 2026-09-15]]
