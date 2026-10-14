---
title: "Adyen autonomous store Terminal API flow"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/autonomous-stores"
raw_files:
  - "adyen/docs/point-of-sale/autonomous-stores/2026-09-15.md"
tags: [adyen, point-of-sale, autonomous-stores, card-acquisition, pre-authorization, capture]
---

## Overview

Adyen's dated autonomous-store guide describes a merchant-operated, staffless store using an unattended payment terminal and a Terminal API integration. The shopper presents a card before entry; the merchant's backend recognizes the card, pre-authorizes an entry amount, controls access, calculates the later basket amount, optionally adjusts the authorization, and manually captures the final charge to its merchant account. Adyen supplies payment interfaces and processing; the merchant implements door and basket logic. The page does not name a separate seller or merchant-of-record arrangement. See [[adyen]], [[adyen-autonomous-stores]], [[adyen-terminal-api]] and [[adyen-authorization-adjustment]].

## Key takeaways

- Prerequisites in this snapshot include a Terminal API integration, an unattended-suitable terminal such as P400 Plus/S1U2/UX300, an API key with Merchant PAL and Checkout webservice roles, Standard webhooks for `AUTHORISATION_ADJUSTMENT`, `CAPTURE` and `CAPTURE_FAILED`, and manual capture. Cloud Terminal API users may use their existing Terminal API API key. Adyen Support configures payment methods and, if desired, synchronous authorization adjustment. Adjustment availability depends on payment method, MCC and issuer; authorizations expire on card-scheme schedules. These are eligibility gates, not account-specific approvals.
- The merchant backend first triggers a Terminal API card-acquisition request. `Operation.Variant=PreAuthToEnterShop` hides the prospective pre-authorization amount on the initial terminal screen so it is not mistaken for an entry fee. `CardAcquisitionTransaction.TotalAmount` must equal the follow-up pre-authorization `RequestedAmount`. Save the acquisition response's `POIData.POITransactionID` timestamp/ID for `PaymentData.CardAcquisitionReference`. The card alias can recognize a returning card, but **cannot make payments**. Card acquisition itself is not authorization or entry approval.
- The guide optionally asks a first-time shopper for contact details or consent to tokenize. It suggests confirmation/signature input and phone/text input, and warns that `shopperReference` must not contain PII such as name or email. For tokenization, configure shopper identifiers with Adyen, then include `recurringProcessingModel=UnscheduledCardOnFile` in both card acquisition and pre-authorization as described. This creates a conditional recovery route; a card alias is never a recurring payment token.
- Send a Terminal API payment request with `authorisationType=PreAuth` and the acquisition reference. On successful pre-authorization, the merchant's own system decides whether to open the door. The guide recommends tokenization for possible later recovery; cardholder authentication is enforced through the specified recurring model **if configured by Adyen Support**, and SCA relevance is business-dependent. The examples use EUR 10 and test references, which do not establish a live outcome.
- After the shopper leaves, the merchant computes the purchase amount. If it differs, send an **Adyen backend API** authorization adjustment, not a Terminal API request to the terminal or terminal Cloud endpoint. The page calls for at least five seconds between pre-authorization and adjustment when building/testing. The new amount is the **total** authorized amount in minor units, including the original and all later additions. The asynchronous Checkout `/payments/{paymentPspReference}/amountUpdates` response `received` is only acknowledgment; use the `AUTHORISATION_ADJUSTMENT` webhook for outcome. The synchronous `/adjustAuthorisation` route requires Support enablement and the latest decoded `adjustAuthorisationData` blob, updating that blob after each authorized adjustment.
- Manually capture against the **original payment authorization PSP reference** for the final authorized amount in minor units. A capture response `received` is not proof of collection: use the `CAPTURE` webhook and handle `CAPTURE_FAILED`. The guide says a failed capture webhook should trigger review of its reason, correction, and a new capture request; it does not imply that blind retries are safe.
- If adjustment fails, the guide offers capture of the original pre-authorized amount and conditional recovery of a remainder via a recurring online payment **if a token was created**, or a payment link **if contact details were collected**. Auto Rescue is mentioned for refused shopper-not-present card transactions. A merchant-managed card-alias not-allowed list can prevent future entry after failed recovery; it does not itself collect a debt. The page gives no QR, split-sale, general cancellation/refund or terminal-timeout procedure and no PCI/privacy clearance for a merchant's store implementation.

## Detail locators

- `## Requirements`, `## How it works:`: Terminal API, roles, supported-device examples, webhook/manual-capture gates, eligibility/expiry and merchant-owned door/basket logic.
- `## 1. Get the card details`, `## 2. Optional: Get the shopper's details`: card-acquisition variant, response IDs/alias, shopper contact and consent inputs.
- `## 3. Pre-authorize an amount`: equal amounts, acquisition reference, conditional tokenization/authentication, original PSP reference and `adjustAuthorisationData`.
- `## 4. Adjust the pre-authorized amount`, `### Tab: Asynchronous authorization adjustment`, `### Tab: Synchronous authorization adjustment`: backend route, five-second test delay, total/minor-unit amount, webhook versus synchronous blob rules. The language SDK snippets and test API versions are examples, not version requirements.
- `## 5. Capture the amount`, `## Recover failed payments`: original authorization reference, manual capture and webhook outcome, token/link fallback and alias blocklist.

## Related

- [[adyen-autonomous-stores]] — proposed autonomous entry-to-capture topic route.
- [[adyen-terminal-api]] — POS-to-terminal messages and card acquisition.
- [[adyen-authorization-adjustment]] — eligibility and amount-update lifecycle.
- [[adyen-payment-capture]] — asynchronous manual-capture outcomes.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/autonomous-stores/2026-09-15|Adyen Autonomous stores, captured 2026-09-15]]
