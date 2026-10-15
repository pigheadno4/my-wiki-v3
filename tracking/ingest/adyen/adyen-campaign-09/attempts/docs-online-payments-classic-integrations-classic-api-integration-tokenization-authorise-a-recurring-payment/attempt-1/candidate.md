---
title: "Adyen Classic API: authorise a payment with stored details"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-a-recurring-payment"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-a-recurring-payment/2026-09-15.md"
tags: [adyen, classic-api, tokenization, one-click, recurring-payments, stored-details]
---

## Overview

This dated Classic Payment API guide describes subsequent `/authorise` requests after payment details were successfully stored during an initial `/authorise` call. It distinguishes the one-click `ONECLICK`/`CardOnFile` request from the recurring `RECURRING`/`Subscription` request. The page marks this endpoint inactive and unsupported for new integrations, directs new builds to Checkout API, and tells existing users to contact Adyen about migration. It is a request guide, not evidence that storage, shopper consent, or a later authorization succeeded. [[adyen-tokenization]] [[adyen]]

## Key takeaways

- Both illustrated subsequent-payment routes identify the previously stored details using the original `shopperReference` and either a `recurringDetailReference` selected from stored details or `LATEST` for the most recent detail. Both list `shopperInteraction: ContAuth`; their `recurring.contract` and `recurringProcessingModel` values differ.
- The **one-click** section lists `recurring.contract: ONECLICK` and `recurringProcessingModel: CardOnFile`, plus `card.cvc` collected from the shopper. If hosting the Classic CSE library, the page places the encrypted card CVC in `additionalData.card.encrypted.json`. Keep that CVC handling scoped to this one-click route; the recurring section does not list a CVC field.
- The **recurring** section lists `recurring.contract: RECURRING` and `recurringProcessingModel: Subscription`. Its JSON, SOAP, curl and library examples show request shape, not a payment result or capture outcome. The linked next-step page covers capture separately.
- This page starts after successful storage; it does not define the shopper-consent or first-token creation flow. Use [[adyen-tokenization]] and its source routes for that boundary. Do not read these Classic examples as current eligibility for a new integration.

## Detail locators

- Opening notice and paragraph before `One-click payments` — inactive endpoint, migration direction, and prior successful storage prerequisite.
- `One-click payments` — CVC, `ONECLICK`/`CardOnFile`, common stored-detail selectors, JSON/SOAP/form examples, and CSE-hosted encrypted CVC variant.
- `Recurring payments` — `RECURRING`/`Subscription`, common stored-detail selectors and request examples.
- `Next steps` — linked capture, retrieve, and update stored-details pages; navigation only.

## Related

- [[adyen-tokenization]] — provider tokenization concept, consent and stored-detail scope.
- [[adyen]] — provider overview.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-a-recurring-payment/2026-09-15|Adyen authorise a recurring payment, fetched 2026-09-15]]
