---
title: "In-person payment-facilitator user data | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/payment-facilitators"
raw_files:
  - "adyen/docs/platforms/in-person-payments/payment-facilitators/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, payment-facilitator, sub-merchant, terminal-api, management-api]
---

## Overview

This dated [[adyen]] for Platforms guide explains the **additional user (sub-merchant) data** a payment facilitator supplies with facilitated **in-person** transactions. It says that, for a transaction facilitated by the platform, the user is considered Merchant of Record under card-scheme requirements; Adyen adds some user data automatically and the facilitator supplies the rest. That statement is scoped to these facilitated transactions. It does not establish a universal platform/seller arrangement, account eligibility, contractual liability, payee, split booking, payout, or bank receipt. See [[adyen-pos-payment-facilitators]] and [[adyen-platforms]].

## Key takeaways

- **Channel and route.** The guide covers Terminal API with payment terminals or a Mobile solution, and standalone terminals. A standalone solution can supply the remaining user data **only through store configuration**. Integrated terminals can use store configuration, Terminal API request fields, or both. When both are used, the request fields override store data. This is data precedence, not payment authorization or financial split precedence. [Raw: Requirements and Methods to add user data, lines 23–44]
- **Store configuration.** For a user's store, the facilitator can create or update `subMerchantData` through the Management API; update requires a credential with **Management API—Stores read and write**. The store field table marks `email`, `id`, `mcc` and `name` required. Its `id` is the facilitator's unique identifier for the user, alphanumeric with a **15-character** maximum, distinct from the store ID used in `/stores/{storeId}`. The user name can overwrite part of the shopper's bank-statement transaction description under scheme rules. Store-configured data is added before requests go for authorization. The test-environment and language SDK snippets have stated library versions; several generated snippets are incomplete, so use the field table and versioned API contract when implementing. [Raw: lines 27–31, 46–66, 68–276]
- **Per-request data and lifecycle.** For integrated Terminal API requests, the `additionalData` JSON object can contain the user identifier, city, ISO alpha-3 country, name, postal code, street, tax ID and MCC. The table gives field descriptions but does **not** mark requiredness. Request `subMerchantId` is alphanumeric with a **19-character** maximum, different from store `subMerchantData.id`. Base64-encode the JSON and put it in `SaleData.SaleToAcquirerData`. Request fields are needed for Terminal API **payments** and **referenced or unreferenced refunds**; non-Terminal-API modifications such as manual capture and authorization adjustment use the initial payment's sub-merchant data. The payment response does not echo the submitted user data. [Raw: lines 42–44, 278–355]
- **User data together with splits.** If a Terminal API request carries both user data and split instructions, put **all** of that data in one `additionalData` JSON object and pass its Base64-encoded string in `SaleData.SaleToAcquirerData`; the guide says concatenated key-value pairs cannot pass on user data. Its combined example is illustrative and internally inconsistent on currency: the displayed JSON has `split.currencyCode` `USD`, while the Base64 example decodes to `EUR`; a separate payment-only example uses `BRL`. Do not treat those examples as a verified single transaction or completed booking. [Raw: Combining user data and split instructions, lines 357–409]

## Detail locators

- Raw `Requirements` and `Methods to add user data` (lines 23–44): integration types, Management API role, standalone limit, request-over-store precedence and modifications.
- Raw `Add to the store configuration` (lines 46–276): create/update routes, required store fields, ID/name constraints and versioned test snippets.
- Raw `Add to the Terminal API request` (lines 278–355): request fields, encoding, payment example and non-echo response caveat.
- Raw `Combining user data and split instructions` (lines 357–409): same-JSON/Base64 requirement and illustrative split example.

## Related

- [[adyen-pos-payment-facilitators]] — provider POS facilitator model and scoped Merchant-of-Record statement
- [[adyen-platforms]] — platform/user account context
- [[adyen-terminal-api]] — message transport
- [[source-adyen-docs-point-of-sale-payment-facilitators]] — separate general POS guide

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/payment-facilitators/2026-09-15|Adyen Platforms in-person payment facilitators — collected 2026-09-15]]
