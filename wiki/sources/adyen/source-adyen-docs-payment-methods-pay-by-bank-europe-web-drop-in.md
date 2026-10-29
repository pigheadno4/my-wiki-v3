---
title: "Adyen Pay by Bank (Europe) Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-europe/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-europe/web-drop-in/2026-09-15.md"
tags: [adyen, pay-by-bank-europe, web, drop-in, open-banking, tink, sepa-direct-debit]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds Pay by Bank (Europe) to an existing **Web Drop-in** integration for Sessions or Advanced flow. It covers a country-code request field, optional issuer presentation, Tink redirects, a separate SEPA Direct Debit route for future tokenized payments, and test/live setup. It does not prove current market or merchant eligibility, a completed bank transfer, or settled funds. See [[adyen-online-payments]] and the related Pay by Bank (Europe) method overview.

## Key takeaways

- **Prerequisites and request field:** Both Sessions and Advanced tabs require Web Drop-in **v5.70.0 or later** and Support assistance to add the method in Customer Area. The related method overview also says onboarding requires approval through an Adyen contact. Both /sessions and /payments tables mark **countryCode** required to filter shopper methods; **QZ** is an exception to the usual two-letter country-code format, not a claim that Pay by Bank (Europe) is available in Kosovo. Web Drop-in v6 imports **PayByBank** when importing its resources. A separate live Customer Area addition is required before accepting live payments. [Pinned raw: lines 21–65, 1502; related overview raw: raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md, line 23]
- **Bank choice and Tink:** Issuer selection in the merchant form is optional only where supported. The guide says markets with too many banks, such as Germany, redirect shoppers to Tink to choose a bank; in the UK the merchant may show a bank list first or let Tink handle selection. Optional configuration includes logo visibility, a preselected issuer ID, highlighted issuers and placeholder text under **paymentMethodsConfiguration.paybybank**. The UK test and live issuer tables are examples that may change, not guaranteed current bank availability. [Pinned raw: lines 67–156]
- **Recurring is a different method:** The page says future recurring transactions are supported **through SEPA Direct Debit**, not by reusing the Pay by Bank one-time method type. It strongly recommends explicit shopper permission for future charges. It describes creating a shopper token, receiving a **recurring.token.created** webhook with **storedPaymentMethodId**, and using that ID for later off-session **Subscription** or **UnscheduledCardOnFile** payments with **paymentMethod.type=sepadirectdebit** and **shopperInteraction=ContAuth**. The normal SEPA tokenization parameters apply. [Pinned raw: lines 158–173, 523–531, 533–555, 872–899]
- **Payment outcome:** A **Received** resultCode and pspReference mean the payment request was received; use webhooks to track whether it succeeded. The related overview warns that even a successful AUTHORISATION webhook can precede a failed bank transfer and that funds are not guaranteed; it documents SentForSettle, a possible CHARGEBACK after eight weekdays without funds, and a later CHARGEBACK_REVERSED if funds arrive. Do not treat Received or AUTHORISATION as settled funds. [Pinned raw: line 1496; related overview raw: raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md, lines 45–60]
- **Test scope:** The guide recommends approved, authentication-error and shopper-cancelled test scenarios, includes UK/DE/FR/FI Tink demo credentials, and gives a UK approved-scenario account choice for amounts above or below GBP 150. These are test instructions, not current live coverage or live credentials. [Pinned raw: lines 1498–1556]

> [!WARNING] Market scope differs between overview prose, matrix and tests
> The related overview prose says currently available in Germany, France and the UK, while its matrix also lists Finland; this child page includes Finland test credentials. The captured sources do not resolve whether Finland was live-supported at capture time, and none of these historical statements establishes present eligibility. [Related overview raw: raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md, lines 23–43; pinned raw: lines 1548–1556]

> [!WARNING] Token-creation examples already use a stored ID
> Under “Create a token,” the examples already pass **paymentMethod.type=sepadirectdebit** and **storedPaymentMethodId**, while the prose says this step creates a shopper token whose ID arrives in a recurring.token.created webhook. The examples therefore do not demonstrate obtaining a new ID from a first Pay by Bank payment; use the linked standard SEPA tokenization guidance to establish the initial token. A later legacy example under “UnscheduledCardOnFile” uses **Subscription** instead, so preserve the prose/model distinction rather than copying that block blindly. [Pinned raw: lines 169–198, 523–531, 872–899, 1215–1235]

## Detail locators

- Identity, both flow prerequisites, v6 import, and countryCode tables: pinned raw lines 15–65.
- Optional issuer display/configuration and UK issuer lists: pinned raw lines 67–156.
- SEPA recurring prose, token-creation examples and token webhook: pinned raw lines 158–523.
- Off-session Subscription and UnscheduledCardOnFile examples and conflicting legacy block: pinned raw lines 525–1494.
- Received status, test scenarios, live addition, and regional demo credentials: pinned raw lines 1496–1556.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pay-by-bank-europe]] — method overview for onboarding, market and settlement qualifications.
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — SEPA Direct Debit tokenization context, if available.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/web-drop-in/2026-09-15|Pay by Bank (Europe) Web Drop-in guide, captured 2026-09-15]]
