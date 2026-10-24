---
title: "Adyen UPI Autopay Web signup integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/upi-autopay/web"
raw_files:
  - "adyen/docs/payment-methods/upi/upi-autopay/web/2026-09-15.md"
tags: [adyen, upi, autopay, india, web, mandate, recurring]
---

## Overview

This [[adyen]] page covers **Web SDK configuration for UPI Autopay signup**, where Indian shoppers review and authorize a recurring mandate in a UPI app through Collect, QR or Intent. It supports existing Web Drop-in or Components integrations with Sessions or Advanced flows. The page explicitly sends full backend requirements—including pre-debit notices, later recurring payments and billing-plan cancellation—to its API-only guide. Rendering mandate information, obtaining a shopper PIN, sending a request or receiving a client result does not alone prove mandate registration, first-payment success, token creation or later charge/refund completion. [[adyen-tokenization]]

## Key takeaways

- **Prerequisite and version scope:** The requirements list existing Web Components or Drop-in under Sessions or Advanced, plus a backend implementing all UPI Autopay recurring flows. The page names **Adyen Web SDK v6.22.0** for mandate information displayed in checkout, phrased as integrating to the “latest web version”; this dated snapshot does not establish a current latest version. The Web page is scoped to signup UI, while the linked API-only guide owns full backend requirements. See raw lines 19–28.
- **Shopper paths and display:** Collect apps show the **mandate amount**; QR/Intent apps show both mandate and first-transaction amounts. The described flow has the shopper review mandate details in the UPI app and authorize with a UPI PIN; the page describes mandate creation and the first payment as the intended result. From Web SDK v6.22.0, a checkout information box can show mandate details. Its text varies with transaction `amount`, known `mandate.amount` limit, `frequency` and `amountRule` (`exact` or `max`); examples cover monthly, weekly and ad hoc amounts. No client display alone proves provider acceptance or first-payment outcome. See raw lines 30–52 and 63–100.
- **Mandate-only/free-trial example:** The page describes a no-upfront-payment path in which a small minimum amount is authorized and automatically refunded, instructing a minimum **2 INR** in `additionalAmount` and information about authorization/refund shown **outside** the Component. This is page advice for that example, not evidence a particular authorization/refund has happened or a universal no-charge mandate. See raw lines 54–61.
- **Sessions signup fields:** Prose instructs passing the complete `mandate` object, `recurringProcessingModel`, `shopperReference` and `storePaymentMethod` in `/sessions`, then passing the **same mandate object** to the UPI Component configuration and mounting it. The adjacent `createSession` snippet shows `mandate` but does not spell out the other three fields, despite a generic “other session configuration” comment; do not treat it as a complete request. See raw lines 103–141.
- **Advanced signup fields:** Prose instructs the `mandate` object in UPI Component configuration and the complete mandate plus `recurringProcessingModel`, `shopperReference` and `storePaymentMethod` in `/payments` initiated within `onSubmit`. The example passes `{ ...state.data, mandate }` to `makePayment` without explicitly showing those three other named fields, so its server request cannot be verified from the snippet alone. `actions.resolve({ resultCode, action })` is a client callback handoff, not final payment proof. See raw lines 143–187.
- **TEST and LIVE:** The page says to contact Adyen to set up a UPI Autopay test environment and lists **scenario-specific magic amounts** for signup, pre-debit notice, recurring charge, mandate revoke and refund outcomes; one amount can label different outcomes in different scenarios. It separately says to contact Adyen to begin **live onboarding** before accepting live UPI Autopay payments. Those fixtures and contacts do not show actual notifications, cancellation, refund or live enablement. See raw lines 189–206.

## Detail locators

- Requirements, provider/app roles and Web-only scope: raw lines 19–28.
- Collect versus QR/Intent shopper journey and mandate display: raw lines 30–100.
- Sessions and Advanced prose versus snippets: raw lines 103–187.
- Scenario-specific TEST fixtures and LIVE onboarding: raw lines 189–206.

## Related

- [[adyen-tokenization]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-upi-upi-autopay]]
- [[source-adyen-docs-payment-methods-upi-upi-autopay-api-only]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/upi-autopay/web/2026-09-15|Adyen UPI Autopay Web signup guide]]
