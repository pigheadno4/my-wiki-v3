---
title: "Adyen UPI Autopay"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/upi-autopay"
raw_files:
  - "adyen/docs/payment-methods/upi/upi-autopay/2026-09-15.md"
tags: [adyen, upi, autopay, recurring-payments, mandates, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes **UPI Autopay recurring payments**, where a shopper uses a participating UPI app linked to a bank account to approve a mandate and an initial charge. It covers subscription and automatic-top-up models, initial approval, subsequent debits, failure and free-trial handling. It is distinct from one-off UPI checkout, and its historical description does not establish current app, bank, merchant or account eligibility. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The guide maps fixed-interval subscriptions to Adyen's **Subscription** recurring processing model and non-fixed automatic top-ups to **UnscheduledCardOnFile**. At signup it presents UPI Collect (VPA entry), QR (scan), and Intent (mobile/mobile web only) as options for approving Autopay in a UPI app. The shopper sees mandate details including frequency, amount and start/end dates, then uses a UPI PIN for approval. (raw lines 19–40)
- Mandate creation, first charge and later charges are **separate states**. The described successful path shows mandate creation followed by an initial payment, checkout status on return, and a pre-debit SMS/email/push notification from the UPI app at least **24 hours** before later charges. The page says a subsequent amount below **₹15,000** is debited, while **₹15,000 or above** prompts the shopper for a UPI PIN to authorize that charge. These steps describe the guide's flow, not evidence a specific mandate or debit succeeded. (raw lines 34–46)
- **First-payment failure:** A mandate can be created successfully while its first payment fails. In that case, the page says Adyen automatically **cancels** the mandate, the shopper sees cancellation in the UPI app, and the merchant may initiate a fresh transaction and signup. It explains that mandates without a successful first payment within five minutes require a later PIN re-entry, and says Adyen tokenizes details **only after a successful initial payment**. Do not treat mandate approval as stored-token or first-payment success. (raw lines 48–54)
- **Front end:** The guide recommends at least two methods per device: QR/Collect on desktop because Intent is unsupported there, and Intent/Collect on mobile. For Android it describes a generic intent app drawer; on iOS it calls for app-specific intent URLs. Its Adyen Web SDK **v6.22.0 or later** statement is specifically about automatic display of mandate information, not a general API minimum or proof of native-SDK support. Native app SDK inquiries go to an Implementation Manager. (raw lines 56–75)
- **Free-trial workaround:** UPI Autopay cannot create a mandate with a **0 INR initial charge**. The page directs a minimum **2 INR authorization** using `additionalAmount` in `/payments`, followed by an Adyen-initiated refund **after successful authorization**. If the automatic refund fails, a `REFUND_FAILED` webhook is sent and the merchant should retry via the standard refund flow. An authorization or refund initiation alone does not prove capture, settlement, or completed refund. (raw lines 77–87)
- This page does not give a mandate amendment API, a manual cancellation procedure, a general mandate expiry rule, an API-version minimum, or a TEST/LIVE execution result. The See also links are navigation to API-only integration, webhooks and API Explorer. (raw lines 1–93)

## Detail locators

- Recurring models and Collect/QR/Intent signup options: raw lines 19–32.
- Mandate approval, first payment, notice and ₹15,000 PIN threshold: raw lines 34–46.
- Failed first payment, automatic mandate cancellation and tokenization condition: raw lines 48–54.
- Device recommendations and Web SDK v6.22.0 mandate-information feature: raw lines 56–75.
- Zero-INR constraint, 2-INR authorization and automatic-refund failure handling: raw lines 77–87.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/upi-autopay/2026-09-15|Adyen UPI Autopay guide, 2026-09-15 snapshot]]
