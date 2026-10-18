---
title: "Adyen for Platforms automatic split-configuration creation"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/automatic-split-configuration/create-split-configuration"
raw_files:
  - "adyen/docs/platforms/automatic-split-configuration/create-split-configuration/2026-09-15.md"
tags: [adyen, platforms, automatic-splits, balance-accounts, management-api]
---

## Overview

This Adyen for Platforms guide describes creating a **split-configuration profile**, defining at least one conditional rule for transaction funds and fees, then **linking the profile to a user's store** with a selected user balance account. The profile can be shared by multiple stores, each association naming that store's user balance account. Once the store is successfully created or updated, Adyen evaluates its transactions and applies the rule with the **highest-priority matching condition**; this page links to a separate rule-hierarchy explanation rather than specifying the full priority algorithm. Without split instructions in either a profile or the Checkout/Terminal API payment request, Adyen says funds and fees are booked to the **platform liable balance account**. The page is configuration guidance and examples, not proof of an authorized payment, actual split booking, merchant-of-record allocation, settlement or payout.

## Key takeaways

- **Enablement, roles and association:** the guide requires an Adyen for Platforms **platform-model** integration and Support enablement of split-configuration profiles. API creation/management requires Management API credential role `Management API—SplitConfiguration read and write`; Customer Area creation/management requires Support to enable `Manage new split configuration settings` for an admin who can grant it onward. Create a profile in Customer Area or Management API, but the general store-link step uses Management API `POST /stores` or `PATCH /stores/{storeId}` with `splitConfigurationId` and `balanceAccountId`. The introduction gives an **Onboarding on invite** exception for Customer Area store linking, while later requirements and linking instructions say Management API only; do not erase this source qualification.
- **Rule selection:** the first rule is created with the profile. Customer Area conditions include shopper interaction/channel, method or variant, card funding source and currency. The Management API `POST /merchants/{merchantId}/splitConfigurations` body contains `description` and `rules`; its table marks currency, payment method, funding source, shopper interaction, split logic and platform commission as required. Optional card usage/region conditions are listed, but **card region is pilot-only** and API-defined if available. `ANY` broadens a condition; the exact priority among matching rules belongs to the separately linked hierarchy page.
- **Funds, commission and fees:** a rule's platform commission goes to the liable balance account and can be fixed (minor units), variable (percentage), or both. An optional additional commission goes to its specified balance account. Fee booking can target liable or user balance accounts. The fee-type table allows **one aggregation level at a time**: `paymentFee` alone, paired `acquiringFees` and `adyenFees`, or the four detailed interchange/scheme/Adyen commission/markup fields. The raw prose misspells `acquiringFees` as `aquiringFees` in combination lines while examples use `acquiringFees`; use the current API schema for executable requests.
- **Later lifecycle and currency:** optional refund/chargeback amounts and their fees may be assigned to liable/user balance accounts or follow the original payment split ratio. **Do not use `deductAccordingToSplitRatio` for refunds if the store processes multiple partial captures.** A `remainder` instruction books leftover value after currency conversion for **online** payments. DCC markup splitting is **in-person and pilot-only**; after Adyen's share, `dcc.accountHolderPercentage` is in basis points for the user balance account, with the rest for the liable balance account. Tip/surcharge booking is in-person; the page says surcharge configuration is available for payments initiated in Australia/New Zealand, with Canada/Europe/US pilots.
- **Example and environment limits:** fixed amounts use minor units and percentage inputs use basis points in the composite example. The many curl/SDK snippets are **test-environment examples across differing library versions**, not a current SDK baseline or proof of a successful configuration. The composite example's narrative commission and curl values differ, and a fee response value differs from its request; use the verified Management API contract and returned configuration for implementation. No Checkout/Terminal request-versus-profile precedence beyond the stated no-instructions fallback is established here.

## Detail locators

- Raw lines 15–43: profile purpose, no-instruction liable fallback, create/link sequence, platform/role/Support prerequisites and invitation exception.
- Raw lines 45–107: Customer Area first-rule creation, channel/method/funding/currency conditions and commission/fee/chargeback/tip choices.
- Raw lines 109–157: Management API creation endpoint, required/optional rule fields, pilot card-region condition and optional booking categories.
- Raw lines 161–180 and 181–566: fee aggregation restrictions, test SDK examples and returned profile/rule/logic IDs; inspect request/response discrepancies before reuse.
- Raw lines 570–993: refund/chargeback allocations and multi-partial-capture restriction, with type-specific examples.
- Raw lines 997–1453: online conversion remainder and pilot in-person DCC markup.
- Raw lines 1457–1853: regional/pilot surcharge qualification and tip/surcharge booking.
- Raw lines 1855–2373: composite catch-all example, minor-unit/basis-point statement and versioned snippet inconsistencies.
- Raw lines 2375–2649: store create/update association, selected balance account, highest-priority-rule statement and illustrative test store response.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform/user balance-account and payment-flow context.

## Raw Sources

- [[raw/adyen/docs/platforms/automatic-split-configuration/create-split-configuration/2026-09-15|Automatic split configuration creation, fetched 2026-09-15]]
