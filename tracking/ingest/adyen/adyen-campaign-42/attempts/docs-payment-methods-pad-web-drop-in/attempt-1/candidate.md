---
title: "Pre-Authorized Debit Canada Web Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pad/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pad/web-drop-in/2026-09-15.md"
tags: [adyen, pad, canada, web, drop-in, direct-debit, tokenization]
---

## Overview

This 2026-09-15 Adyen page gives PAD Canada additions to an existing **Web Drop-in** integration, separately for Sessions and Advanced server-side flows. It covers setup, consent, recurring tokens, delayed bank outcome, test returns and retry codes. It is an integration snapshot, not proof of enabled acceptance or a final bank debit. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Both flows** require an existing matching Web Drop-in integration, Checkout API **v69 or later**, the `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` webhook for outdated bank details, Support enablement in Customer Area, and a way to obtain the shopper's PAD mandate. Before live use, contact Support to add PAD Canada in the **live** Customer Area. See raw lines 25–37, 181–193 and 397–399. The overview [[source-adyen-docs-payment-methods-pad]] gives the separate merchant-held agreement requirements; this page's setup reference alone is not a complete mandate procedure.
- **Sessions:** `PreAuthorizedDebitCanada` is an optional individual import for tree shaking; no PAD-specific Drop-in configuration is needed. The `/sessions` table lists optional `billingAddress` and tokenization fields `recurringProcessingModel`, `shopperInteraction`, `shopperReference`, `storePaymentMethod`; the example uses CA/CAD. Shopper mandate consent is needed for the payment or recurring series. See raw lines 39–68 and 70–99.
- **Advanced:** the same optional import applies. `paymentMethodsConfiguration.eft_directdebit_CA.enableStoreDetails` is available from Web **v5.24.0**, defaults false and controls the save-details checkbox; it is not shown as required. The `/payments` table marks `paymentMethod.type=eft_directdebit_CA`, `bankAccountNumber`, five-digit `bankLocationId`, three-digit `bankCode`, and `ownerName` required; `billingAddress` and tokenization fields are listed separately. The example uses a **v72 test endpoint**, which does not replace the stated v69+ minimum. See raw lines 195–247 and 249–284.
- **Tokens and mandate:** the guide recommends against one-off PAD because of chargeback risk, supports recurring tokenization, and requires a mandate for future recurring debits. Create the token on the initial payment; Sessions receives `storedPaymentMethodId` via `recurring.token.created`, while Advanced may receive it in the API response and/or webhook. Advanced `additionalData` can include generated mandate ID and initial-request signature date; tokenization response fields require creation parameters plus Customer Area **Recurring details**. Store token with `shopperReference`; later recurring requests do not need mandate ID. The generated ID/date fields do **not** themselves prove shopper consent. See raw lines 65–68, 108, 114–125, 287–296 and 328–345. [[adyen-tokenization]]
- **Outcome is asynchronous:** both flow sections say bank authorization can take up to **five business days**. Success appears in the Settlement details report; a failed debit may produce `CHARGEBACK`. The Advanced example's `resultCode: Authorised` must not be treated as final bank authorization or settlement. See raw lines 104–110 and 298–330.
- **Testing and returns:** test payments can use a real Canadian bank account without debiting it or the listed test credentials. In TEST, `ownerName=chargeback:<reason>` triggers a return straight to Chargeback. The source's reason table permits **one** retry within **30 days** of original authorization for codes **01** and **08**; listed account, stop, mandate, revoked-agreement, notification and other return codes are marked no retry. Use the reason-specific table, not a blanket retry policy. See raw lines 127–175 and 349–395.

## Detail locators

- Sessions setup, optional import/configuration and `/sessions` fields: raw lines 25–99.
- Sessions token, delayed outcome and recurring instructions: raw lines 102–125.
- Advanced setup, Web version, required `/payments` bank fields and example: raw lines 181–284.
- Advanced additionalData, response example, delayed outcome and recurrence: raw lines 287–345.
- TEST credentials, return codes, retry limits and live Support step: raw lines 127–179 and 349–399.

## Related

- [[adyen-online-payments]] — Web Drop-in Sessions and Advanced routing.
- [[adyen-tokenization]] — recurring token creation and use.
- [[source-adyen-docs-payment-methods-pad]] — PAD overview and merchant agreement, return and dispute context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/pad/web-drop-in/2026-09-15|PAD Canada Web Drop-in, captured 2026-09-15]]
