---
title: "Adyen India recurring-card mandate guide (historical)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/cards-recurring-india"
raw_files:
  - "adyen/docs/payment-methods/cards/cards-recurring-india/2026-09-15.md"
tags: [adyen, cards, india, recurring-payments, tokenization, mandates, historical]
---

## Overview

This [[adyen]] guide, last modified **2021-05-04** and captured 2026-09-15, describes **locally acquired recurring card payments in India** for regular **Subscription** charges and non-fixed **UnscheduledCardOnFile** automatic top-ups. It explicitly says local acquiring is needed and tells the merchant to contact an Account Manager or Support to evaluate whether and how it can process locally (raw lines 14–21). The flow is a shopper/issuer **mandate**, a pre-debit notification, then a recurring **/payments** request. Route this through [[adyen-tokenization]] and [[adyen-online-payments]]. It does not establish current India eligibility, mandate approval, legal compliance or a completed payment.

## Key takeaways

- The illustrated initial flow sends encrypted card details and billing-plan **mandate** fields in **/payments**, redirects the shopper to issuer **3D Secure 2**, and sends **/payments/details** on return (raw lines 23–48, 64–91). The prose says the request/response instructions describe **Checkout API v66 or earlier**, with unspecified 3DS differences on v67+, yet its examples use **v72** endpoints (raw lines 31–39, 95–96, 424–425). Do not treat those mixed versions as proven equivalent. A successful initial response is presented as creating the mandate; the issuer's **mandateId** is explicitly an empty placeholder in this snapshot (raw lines 190–203).
- The mandate is unique per billing plan. Its amount must be at least the initial transaction amount; **max** (default) and **exact** set different permitted recurring-charge ranges, with monthly/adhoc frequency and an end date in the table (raw lines 58–89). The page states a recurring charge **at or below INR 15,000** does not need 3DS authentication (raw line 76). This is a **2021 provider statement**, not a current regulatory threshold or merchant approval.
- Before each later charge, the merchant initiates **/notifyShopper** with token, merchant, shopper, amount, billing date and reference, then uses the returned **shopperNotificationReference** in the later **/payments** request (raw lines 316–360, 403–420). A **Success** response means the notification request was processed in its example; it is not proof that the shopper received an email/SMS or that a payment was authorized. The guide recommends initiation **at least 72 hours** before charging and says issuer delivery is **at least 24 hours** before the recurring charge (raw lines 50–54, 323–325). The later [[source-adyen-docs-industries-markets-india|India overview]] and [[source-adyen-docs-online-payments-payments-india-compliance-guide|compliance guide]] state a **48-hour cooling period** (their raw lines 39 and 79 respectively). The 24-hour delivery statement here must not replace that separately stated cooling period; the page does not reconcile their timing origins.
- **/notifyShopper** can return **Refused** or an errorCode/message, and subsequent **/payments** can be **Refused**; the guide routes the final payment status through an **AUTHORISATION** webhook (raw lines 376–400, 449–497). Example **Authorised** data is illustrative. Authentication, authorization, capture and settlement are distinct; no sample response or notification reference proves funds moved.
- Mandate cancellation may arrive via **DISABLE_RECURRING** for BillDesk acquiring or, with enabled Tokenization webhooks, **recurring.token.disabled** for local acquiring (raw lines 499–505). A cancellation between authorization and scheme clearing can yield **CAPTURE_FAILED**. The page's opening local-acquiring prerequisite and its BillDesk-specific branch coexist without explaining how a merchant qualifies for each; do not generalize one webhook route to all. The **/disable** request's **recurringDetailReference** is optional in the table, but **omitting it disables the whole recurring contract for that shopper, including all recurring details** (raw lines 507–529). Treat that selector as consequential; the example includes a specific reference.
- The final checklist points to the **live India Customer Area** (raw lines 539–541), but this snapshot does not demonstrate a live account, local-acquiring approval, issuer mandate status or a processed recurring charge.

## Detail locators

- India/local-acquiring scope, recurring models and initial flow: raw lines 14–62.
- Initial encrypted-card/mandate request fields, example and redirect: raw lines 64–188.
- Conditional mandate result, token and placeholder issuer ID; result codes/webhook: raw lines 190–314.
- Pre-debit timing, **/notifyShopper** fields and Success/Refused/error examples: raw lines 316–401.
- Later recurring **/payments** request and final AUTHORISATION webhook: raw lines 403–497.
- Cancellation webhook branches, **CAPTURE_FAILED**, broad **/disable** omission effect: raw lines 499–537.
- Live India Customer Area pointer: raw lines 539–541.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[adyen-online-payments]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-industries-markets-india]]
- [[source-adyen-docs-online-payments-payments-india-compliance-guide]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/cards-recurring-india/2026-09-15|Full pinned India recurring-card guide]]
