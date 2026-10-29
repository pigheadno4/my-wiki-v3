---
title: "Adyen ANCV payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ancv"
raw_files:
  - "adyen/docs/payment-methods/ancv/2026-09-15.md"
tags: [adyen, ancv, france, holiday-vouchers, partial-payments, online-payments]
---

## Overview

This captured [[adyen]] overview describes ANCV (National Agency for Holiday Vouchers) as a French online payment method for holiday vouchers. Adyen says it acts as a gateway; a merchant must contract directly with ANCV, which handles settlement and reporting. The page gives a capability matrix, a partial-authorization rule, and Web/API-only integration routes. It does not establish a particular merchant's enablement or an executed payment. [[adyen-online-payments]]

## Key takeaways

- **Provider roles and scope:** ANCV is described as a prepaid/gift-card method for France and EUR, with an `await` payment flow. Merchants must approach ANCV directly for a contract because Adyen plays the gateway role, while ANCV handles settlement and reporting. Do not infer Adyen settlement or merchant eligibility from this overview (raw lines 23–29).
- **Capabilities and matrix tension:** The table marks recurring, partial refunds, multiple partial refunds and chargebacks unavailable. It marks refunds available with “See note,” but this captured page gives no clear refund note; inspect method-specific guidance before relying on refund behavior. It marks separate captures, partial captures and multiple partial captures available, yet the immediately following prose says **only one partial capture is allowed per payment**. Preserve that conflict rather than treating the multiple-partial-captures checkmark as unconditional support (raw lines 27–31).
- **Partial payments:** ANCV supports partial authorization, where the shopper-authorized amount can be less than the merchant request. The page says merchants **must** use Adyen's partial-payments feature to handle this and **always** use `orderData` from a `/payments/details` response, not `/payments`, for ANCV partial payments (raw lines 33–39). This is an order continuation rule, not a guarantee of full authorization.
- **Integration routes:** Web links to prebuilt UI solutions for a website; API-only links to merchant-built UI for a website, iOS or Android app. These are route choices, not complete implementation instructions (raw lines 41–53).

## Detail locators

- Identity, gateway/contract/settlement roles and capability matrix: pinned raw lines 15–31.
- Partial authorization and `orderData` response-source requirement: pinned raw lines 33–39.
- Web and API-only integration choices: pinned raw lines 41–53.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-online-payments-partial-payments]] — provider partial-payment context; use this ANCV source for the method-specific `orderData` rule.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ancv/2026-09-15|ANCV overview, captured 2026-09-15]]
