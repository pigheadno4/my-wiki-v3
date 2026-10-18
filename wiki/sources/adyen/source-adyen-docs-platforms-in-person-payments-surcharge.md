---
title: "In-person surcharge | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/surcharge"
raw_files:
  - "adyen/docs/platforms/in-person-payments/surcharge/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, surcharge, split-payments, compliance]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms guide, captured 2026-09-15, describes passing payment-acceptance costs to a customer as a surcharge on an in-person payment. The platform must agree with its users on how payment-acceptance fees are charged. Surcharge booking is separate: by default the surcharge amount books to the platform's liable balance account, while split instructions can direct it to a user's balance account. The guide does not identify the legal seller, merchant of record, final payee or completed bank receipt. [[adyen-platforms]]

## Methods, restrictions and disclosure

- The guide adds method-specific solution and hardware conditions to the general Adyen for Platforms in-person requirements. Its dated availability list is Australia, Canada, Europe, Great Britain, New Zealand and the US; this list is not proof of current account, store, device or payment-method eligibility. Configuration-based rules calculate and apply surcharges automatically from settings such as card brand, funding source, issuing country and currency at company/merchant account, store or terminal scope. Dynamic surcharge uses the platform's own or a third party's calculation, optionally informed by card acquisition, and puts the calculated fee in the payment request. Standalone terminals support configuration-based surcharge only. Both methods can coexist; a surcharge amount passed in the payment request overrides the configured amount, including for an intended zero-surcharge transaction. See raw lines 23–75 for method-selection details.
- Surcharges must satisfy legal, regulatory and card-scheme rules; the feature does not automatically enforce global compliance. The page gives EEA-issued consumer cards in the EEA and US debit-card payments as examples where surcharge is disallowed, and directs the platform to the compliance guide, scheme rules and its own legal advisor. A surcharge cannot be applied to an authorization adjustment or overcapture because it cannot exceed what the customer saw at the point of sale. These dated examples are not an exhaustive or current legal determination. See raw lines 31–50.
- A terminal can display a surcharge confirmation screen showing the total, surcharge and payment method, with confirm/cancel choices; the Mobile solution has no such screen in this snapshot. Customer disclosure is still required. The page permits hiding the Adyen screen for other disclosure forms and names the Management API setting `surcharge.askConfirmation`; customized receipts must satisfy scheme disclosure requirements, while Adyen-generated Terminal API receipt data includes the amount. See raw lines 46–52 and 77–97.
- DCC and surcharge cannot apply to the same transaction. For terminal software earlier than v1.112, the guide recommends avoiding both configurations on the same terminals; at v1.112 or later, it says DCC is automatically skipped when the surcharge is greater than zero. Zero-surcharge cases can therefore differ. See raw lines 99–105.

## Booking and evidence

- The page strongly recommends enabling surcharge additional data in `AUTHORISATION` webhooks; when enabled, `additionalData.extraCostsCurrency` and `extraCostsValueSurcharge` provide currency and surcharge minor units. Its `live: false` payload is illustrative authorization evidence, not proof of capture, balance credit or payout. See raw lines 107–159.
- For the illustrated user-balance-account route, `balancePlatform.transfer.created` and `.updated` show the incoming surcharge split moving through `received`, `authorised` and `captured`, followed by `balancePlatform.transaction.created` with a booked transaction. The page says these webhooks are sent for every split item; `platformPaymentType: Surcharge` helps identify this one. A received/authorised transfer is not booked credit, and these test balance-account examples do not prove customer payment completion or bank receipt. See raw lines 161–186 and 189–489.
- For reconciliation, the guide recommends adding `Surcharge Amount` to the Payment Accounting and Settlement Detail reports. When `Surcharge` is specified in the payment request or split configuration, it says a separate incoming transfer is generated; the Balance Platform Accounting and Balance Platform Statement reports then contain surcharge lines. Use actual per-split events and reports to reconcile amounts and destinations, not sample IDs or dates. See raw lines 491–501.

## Detail locators

- **Purpose, split booking default and requirement boundaries:** raw lines 15–36.
- **Compliance, receipts, method choice and request-over-configuration precedence:** raw lines 38–75.
- **Confirmation screen, Mobile caveat and DCC/version interaction:** raw lines 77–105.
- **AUTHORISATION surcharge fields and illustrative test event:** raw lines 107–159.
- **Per-split transfer/transaction lifecycle and booked user-account example:** raw lines 161–489.
- **PAR/SDR column recommendation and BPAR/BPSR surcharge records:** raw lines 491–501.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-online-payments-surcharge]] — separate online card-payment pilot and API-only route

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/surcharge/2026-09-15|Adyen Platforms in-person surcharge guide — collected 2026-09-15]]
