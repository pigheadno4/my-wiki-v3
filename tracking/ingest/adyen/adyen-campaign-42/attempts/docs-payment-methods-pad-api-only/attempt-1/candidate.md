---
title: "Adyen Pre-Authorized Debit Canada API-only guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pad/api-only"
raw_files:
  - "adyen/docs/payment-methods/pad/api-only/2026-09-15.md"
tags: [adyen, pad, canada, direct-debit, api-only, mandate, tokenization]
---

## Overview

This captured Adyen guide adds Pre-Authorized Debit Canada (PAD) to an existing API-only online-payments integration. It covers a merchant-built bank-detail form, mandate collection, CA/CAD payment-method discovery, `/payments`, tokenized recurring charges, asynchronous result interpretation, test returns and go-live setup. It is not proof of current merchant/bank eligibility or a completed bank debit. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-pad]] for the method-level mandate and chargeback boundaries.

## Key takeaways

- The guide requires an existing API-only integration, Checkout API v69 or later, Direct Debit Notice of Change Notification webhook subscription, Support-assisted Customer Area setup and a way to obtain shopper PAD consent. The merchant builds a form for Canadian account number, five-digit branch `bankLocationId`, three-digit `bankCode` and owner name; `/paymentMethods` uses `countryCode: CA` and `amount.currency: CAD` to request the method. The method overview additionally says the accepting merchant needs a Canadian account at a Canadian financial institution.
- `/payments` lists `eft_directdebit_CA`, bank account number, branch ID, bank code and owner name as required; billing address is listed without a required mark. A PAD agreement must be obtained for a single debit or recurring series, and the overview says the merchant must save that agreement. One-off PAD is supported but not recommended because of chargeback risk.
- The example initial `/payments` request includes optional recurring-token fields `recurringProcessingModel`, `shopperInteraction`, `shopperReference` and `storePaymentMethod`; its `amount.value` and `storePaymentMethod` are JSON strings (`"1000"`, `"true"`), while the prose describes the latter as a true tokenization flag and its response uses numeric amount. Treat the example as illustrative, not type-validation proof. Both primary `/paymentMethods` and `/payments` curl examples omit a shell continuation after `-X POST`, detaching their `-d` lines as printed.
- The response's `additionalData` can carry generated PAD mandate ID, date of signature, token and shopper reference. Tokenization response fields appear only when creation parameters were supplied **and** Recurring details is enabled in Customer Area. For later recurring payments, the guide routes to general tokenization instructions, requires a shopper mandate, Recurring tokens lifecycle webhook and token reuse; it says the mandate ID need not be included again in a recurring request. Do not infer that the response's generated mandate ID replaces collecting and retaining shopper consent.
- The immediate `Authorised` result means Adyen received the payment; the page says bank authorization may remain unknown for up to five business days. A successful debit appears in the Settlement Detail Report; failure produces `NOTIFICATION_OF_CHARGEBACK`. Its result table nevertheless tells merchants to inform the shopper that payment succeeded, creating a tension with the stated bank delay. Preserve the delay when presenting status. `Refused` is a separate immediate result. The overview says PAD lacks real-time authorization and chargebacks are not defendable.
- The test section gives bank details and a `chargeback:<reason>` owner-name trigger; in test, a return goes directly to Chargeback. Its return-code table permits **one** retry within 30 days only for 01 NSF and 08 Funds Not Cleared, while other listed codes are marked no-retry; stopped/revoked/no-agreement cases call for resolving or suspending recurrence and sometimes a new PAD agreement. These are reason-specific instructions, not a general retry permission. Live setup requires Support to add PAD in the live Customer Area.

## Detail locators

- API v69+, Notice of Change webhook, Support and mandate prerequisites; shopper steps: pinned raw lines 23–51. CA/CAD `/paymentMethods` and broken curl sample: lines 53–92.
- `/payments` required bank fields, optional billing address, mandate condition, tokenization fields and sample type/continuation cautions: pinned raw lines 94–146.
- Conditional `additionalData`, generated mandate ID/date/token and immediate result examples: pinned raw lines 148–192. Recurring mandate and lifecycle route: lines 194–205.
- Test bank/return setup, reason-specific retry and no-retry table, live Support gate: pinned raw lines 207–257. Merchant bank account, mandate preservation and non-real-time/nondefendable chargeback boundary: [[source-adyen-docs-payment-methods-pad]].

## Related

- [[adyen-online-payments]] — main integration concept
- [[adyen-tokenization]] — recurring-token concept
- [[source-adyen-docs-payment-methods-pad]] — method-level mandate, merchant eligibility and chargeback authority

## Raw Sources

- [[raw/adyen/docs/payment-methods/pad/api-only/2026-09-15|PAD Canada API-only, 2026-09-15]]
