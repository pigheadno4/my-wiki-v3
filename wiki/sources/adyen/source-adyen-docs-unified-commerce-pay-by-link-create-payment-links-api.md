---
title: "Pay by Link through the API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/create-payment-links/api"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/create-payment-links/api/2026-09-15.md"
tags: [adyen, unified-commerce, pay-by-link, payment-links, checkout-api]
---

## Overview

This 2026-09-15-captured Adyen guide explains how a merchant creates a Pay by Link URL with Checkout API, sends or redirects a shopper to the Adyen-hosted page, and learns the payment result. It also covers reusable links, card tokenization, method-specific data, forced link expiry and page customization. It is a historical API guide with TEST examples, not evidence of a created link, enabled account, successful payment or current method eligibility. See [[adyen]], [[adyen-unified-commerce]], and [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links]] for the creation-channel overview and cross-channel expiry rules.

## Key takeaways

- **Prerequisites and creation:** after a test account, the guide calls for terms and conditions on the payment page, an API key, webhooks able to accept/process payment updates, and methods added to the merchant account (raw lines 42–84). A POST /paymentLinks request supplies merchantAccount, a transaction reference, and amount currency/value in minor units; shopperLocale, expiresAt and description are examples of optional additions. Without them, the page says browser-locale language, no description and **24-hour link expiry** (raw lines 93–103). The examples are TEST requests across named SDK/library versions, not a universal runtime/version requirement (raw lines 105–384).
- The creation response carries link ID, URL and expiresAt; send the **URL** to the shopper, who lands on Adyen's hosted payment page with methods available for the requested amount and countryCode (raw lines 386–418). The page says that **from 2025-11-01, payment links cannot be embedded in an iframe** (raw line 416). Creating or opening a link is not an AUTHORISATION result.
- **Outcome and status:** wait for the AUTHORISATION webhook, whose additionalData.paymentLinkId associates a payment with the link, pspReference identifies the payment, and success distinguishes completed from failed attempts. Manual capture remains a separate action **if enabled** (raw lines 420–447). GET /paymentLinks/{linkId} then returns link details/status: active if unexpired and unpaid, completed or expired otherwise, and paymentPending during an unfinished asynchronous shopper flow (raw lines 476–505). A link's paymentPending status is not a final successful payment. The page says Customer Area's Payment Links list currently shows only EU-created links, gives an ID-based details route for other regions, and retains link details for **three months** (raw lines 424–432); this is a retrieval limit, not the payment-link expiry period.
- A reusable link is requested by setting reusable=true on POST /paymentLinks, illustrated for fixed-amount donations (raw lines 509–535). The guide does not make ordinary links reusable by default; the related creation overview specifies the ordinary one-success and 70-day/five-failure limits. Treat reusable as a link property, not a promise that every shopper/payment attempt succeeds.
- **Tokenization is conditional:** the guide distinguishes CardOnFile for a future shopper-present one-off payment, Subscription for regular merchant-initiated payments, and UnscheduledCardOnFile for non-fixed merchant-initiated payments (raw lines 798–806). It says to seek shopper consent; use a unique non-PII shopperReference of at least three characters, storePaymentMethodMode askForConsent (or enabled when consent already exists), and the matching recurringProcessingModel (raw lines 808–824, 1426–1442, 1751–1767). It describes zero-value authorization for subscription/unscheduled token setup without a charge, and separate later /paymentMethods token retrieval and /payments charges after the shopper completes payment/preauthorization (raw lines 1426–1449, 1747–1749, 1751–1771, 2072–2074). This page is a recipe, not evidence of actual consent or token creation.
- Some BNPL methods need product lineItems and/or countryCode, shopper fields and addresses; the page gives a method-specific table rather than making all such fields globally required (raw lines 2076–2092). For shopper data, API v67+ can use requiredShopperFields to ask on the hosted page, or the merchant can include collected values in POST /paymentLinks (raw lines 2556–2565, 3048–3050). The table/examples are dated method guidance, not proof of a method being enabled; the related Pay by Link pages retain a BNPL channel-availability conflict.
- **Forced expiry and customization:** PATCH /paymentLinks/{linkId} with status=expired forces expiry and changes expiresAt to the current date/time; the returned details reflect both (raw lines 3644–3648, 3839–3858). This changes the link lifecycle and must not be confused with a refund or payment reversal. Customer Area country-based method ordering needs the Change payment methods user role, while API allowedPaymentMethods or blockedPaymentMethods use paymentMethodVariant identifiers for a particular link (raw lines 3868–3895). Themes require Merchant admin or Pay by Link Settings to create, then themeId can select one; shopperLocale controls language, otherwise browser locale applies (raw lines 4173–4200, 4476–4510).
- Testing uses test cards/methods and test Customer Area Payment list. Live preparation calls for a live account/configuration, live method request, live Checkout endpoint and live terms and conditions (raw lines 4511–4523). None of these instructions document a live operation in this snapshot.

> [!warning] Scope and linked-page qualifications
> The API page states a 24-hour default and optional expiresAt, but does not itself restate the related creation overview's 70-day maximum or five-failed-attempt expiry (raw line 101 versus [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links]]). The same related overview and method directory have a BNPL channel conflict; apply method/account-specific eligibility rather than assuming the API example permits a particular method. Link status, AUTHORISATION success, manual capture and three-month detail retention are distinct events/limits.

## Detail locators

- Requirements and POST /paymentLinks baseline, defaults, language examples: raw lines 42–103; multilingual TEST examples 105–384.
- Response URL/ID/expiry, send, iframe restriction and asynchronous webhook/status: raw lines 386–505.
- Reusable link prose and multilingual examples: raw lines 509–797.
- Tokenization models, consent, CardOnFile/subscription/unscheduled examples and subsequent-payment routes: raw lines 798–2074.
- BNPL method-specific data matrix, product examples and shopper collection alternatives: raw lines 2076–3642.
- Force-expiry PATCH and multilingual examples: raw lines 3644–3858.
- Method selection, roles, theme and localization examples: raw lines 3860–4510.
- Test and live checklist: raw lines 4511–4523.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links]]
- [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]]

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/api/2026-09-15|Pay by Link API guide, captured 2026-09-15]]
