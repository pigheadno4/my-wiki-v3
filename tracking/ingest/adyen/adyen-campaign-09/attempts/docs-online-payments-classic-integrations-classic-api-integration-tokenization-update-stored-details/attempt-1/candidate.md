---
title: "Update stored details with Classic API | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md"
tags: [adyen, classic-api, tokenization, recurring-payments, stored-card]
---

## Overview

This 2026-09-15 Adyen Docs snapshot explains how an existing Classic API integration can update previously stored **credit-card** details during a new recurring payment. Adyen marks the endpoint inactive and unsupported for new integrations, directing new integrations to Checkout API and existing integrations to migration. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- The merchant sends new card details in a Classic `/authorise` request with `selectedRecurringDetailReference` identifying the stored detail to update. The documented update is conditional on a successful recurring authorization; this is a payment authorization request with a linked stored-detail change, not a standalone credential-update endpoint.
- On successful recurring authorization, the old `recurringDetailReference` becomes invalid and Adyen creates a new one. The new reference is **not** returned in the authorization response; the page links to the Classic retrieve-stored-details guide for obtaining it. An unsuccessful authorization does not update the stored details according to this page.
- The JSON, SOAP, curl, and library examples illustrate expiry-month/year replacement, `RECURRING` contract, `Subscription` processing model, `ContAuth` shopper interaction, shopper reference, and a test API-key request. The examples do not establish that every shown field or value is a universal requirement. The sample expiry year is 2018 and the curl URL uses Payment API v46, so these examples are historical and do not define modern Checkout API behavior.
- This page does not document how shopper consent was obtained. The broader [[adyen-tokenization]] concept retains the consent and shopper-reference scope for stored credentials. Successful authorization and the stored-detail update described here do not establish capture or settlement.

## Detail locators

- Inactive Classic endpoint and migration routes: lines 16–21.
- Credit-card scope and examples of changed details: line 23.
- Update during new recurring `/authorise`, selected detail reference, and success condition: `Request`, lines 25–33.
- Example request shapes and dated API/library versions: JSON lines 35–59, SOAP lines 61–92, curl lines 94–121, library examples lines 123–474.
- Old-reference invalidation, new-reference retrieval route, and conditional `Authorised` response: `Response`, lines 476–494.

## Related

- [[adyen-tokenization]] — stored-credential consent and shopper-reference context.
- [[adyen-online-payments]] — Classic and Checkout integration routes.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15|Update stored details (2026-09-15)]]
