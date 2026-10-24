---
title: "Set up PayPal for direct merchants"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/setup-paypal-direct-merchants"
raw_files:
  - "adyen/docs/payment-methods/paypal/setup-paypal-direct-merchants/2026-09-15.md"
tags: [adyen, paypal, direct-merchants, setup, permissions]
---

## Overview

This 2026-09-15-modified and captured [[adyen]] guide describes **direct-merchant** PayPal setup in separate test and live environments, routed through [[adyen-online-payments]]. It explicitly sends **marketplaces** to a different setup guide. Its activation-link and Customer Area status steps are account configuration, not evidence that a shopper consented to a billing agreement, that a recurring token exists, or that any payment was authorized, captured or settled.

## Key takeaways

- To enable **test** PayPal payments, the guide calls for a PayPal developer account with both business and personal sandbox accounts, adding PayPal in Adyen's **test Customer Area**, then using an activation link to permit Adyen to process transactions on the **business sandbox** account. The business account simulates the merchant receiving a payment; the personal account simulates a shopper. It says to create sandbox accounts under the developer account so test payments can be seen later.
- For **live**, it separately calls for a live PayPal **business** account, PayPal in the **live Customer Area**, and an activation link granting Adyen permissions on that live account. The activation-link delivery email supplied in Customer Area may differ from the PayPal account email. Adyen says it retrieves PayPal Merchant ID after link completion; the setup form does not require entering it.
- Both test and live Customer Area instructions say payments are **captured immediately after authorisation by default**; choose **Enable authorisation & capture** for later capture. Both tabs also say recurring transactions are enabled by default. That configuration wording does not establish a shopper billing agreement or recurring consent. The separately read [[source-adyen-docs-payment-methods-paypal-web-component]] states Vault permissions as a condition for direct merchants without indirect settlement and strongly recommends explicit shopper permission for future recurring charges; retain these route-specific qualifications rather than treating the default setting as complete recurring readiness.
- Adding PayPal initially leaves an **inactive reason** of “Activation link sent to your inbox.” The emailed link is valid for **seven days after receipt** in test and live; the page also describes retrieving it from the Customer Area PayPal details/MID field or contacting Support if needed. The user follows the link, logs into the corresponding sandbox/live PayPal business account and accepts Adyen's requested permissions. The page says Customer Area status will change to **Active within the same business day**, with a Support escalation if it does not. This is a historical stated expectation, not observed activation or current service-level proof.
- For live PayPal business signup, the page advises a generic company email rather than a personal one because that address appears on shopper PayPal receipts and may outlast an employee. It also calls for activating the PayPal business account and then completing live Customer Area and Adyen-permission steps. No payment request, provider response, billing-agreement state or shopper approval is shown on this setup page.

## Detail locators

- [[raw/adyen/docs/payment-methods/paypal/setup-paypal-direct-merchants/2026-09-15|Pinned raw]], lines 15–33: purpose, marketplace exclusion and distinct test/live sequences.
- Same raw, lines 35–51: developer, merchant and shopper sandbox account roles; lines 53–75: test/live Customer Area options, Merchant ID retrieval, capture/recurring defaults and inactive reason.
- Same raw, lines 77–95: seven-day activation link, corresponding PayPal business login, Adyen permission acceptance and same-business-day Active status/escalation.
- Same raw, lines 97–112: live PayPal business account/email guidance and repeated live setup steps.
- [[source-adyen-docs-payment-methods-paypal-web-component]] — separately read recurring setup and shopper-permission wording, raw lines 1414–1426.

## Related

- [[source-adyen-docs-payment-methods-paypal]] — PayPal overview.
- [[source-adyen-docs-payment-methods-add-payment-methods]] — Customer Area payment-method management.
- [[adyen-tokenization]] — recurring-token context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/setup-paypal-direct-merchants/2026-09-15|Set up PayPal]]
