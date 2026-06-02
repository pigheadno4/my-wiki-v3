<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Fraud protection
slug: /docs/checkout/advanced/customize/fraud-protection/
createTime: '2024-08-15T07:54:27.701Z'
updateTime: '2025-05-13T10:23:10.365Z'
---


# Fraud protection
Fraud protection is a robust risk management toolkit for PayPal merchants who have integrated advanced credit and debit card payments.

Fraud causes many problems for digital business, such as chargebacks and penalty fees. Fraud protection automatically accepts good transactions and rejects fraudulent ones, helping to reduce chargebacks and false positives.

The adaptive machine learning engine monitors card transactions on your website or mobile app to learn new fraud patterns and improve the machine learning models' performance.

Fraud protection provides insight and control through:

- Out-of-the-box filters tuned for your business
- Simulated filter impact before you activate the service
- Real-time actionable filter recommendations
- Dashboard and visualization

Important: Fraud protection is available through your PayPal business account and requires no additional onboarding or integration.

## Enable fraud protection tool
- Log into your [PayPal business account](https://www.paypal.com) .
- In the App Center, go to Manage Risk &gt; Fraud Protection &gt; Get Started .
- Select Enable Fraud Protection to launch the Fraud Protection tool.

## Ensure optimal performance
Send the following fields in the transaction payload:

- [Buyer's phone number](/docs/api/orders/v2/#definition-payer) .
- [Buyer's email](/docs/api/orders/v2/#definition-payer) .

## Next steps
[](/tools/sandbox/)[.css-32eus9-badge_base-text_caption-neutral{color:#001435;font-family:PayPalOpen-Regular,"Helvetica Neue",Arial,sans-serif;font-size:0.875rem;line-height:1.25rem;font-weight:400;max-width:18rem;overflow:hidden;word-break:break-word;text-transform:none;-webkit-line-clamp:2;display:-webkit-inline-box;-webkit-box-orient:vertical;height:auto;padding:0.125rem 0.5rem;border-radius:0.5rem;color:#001435;background-color:#e6e0d9;}@media screen and (max-width: 752px){.css-32eus9-badge_base-text_caption-neutral{font-size:min(0.875rem, 28px);line-height:min(1.25rem, 40px);}}[dir='rtl'] .css-32eus9-badge_base-text_caption-neutral{text-align:right;}Optional](/tools/sandbox/)[](/tools/sandbox/)[Test in PayPal Sandbox](/tools/sandbox/)A self-contained, virtual testing environment.

[](/api/rest/production/)[.css-32eus9-badge_base-text_caption-neutral{color:#001435;font-family:PayPalOpen-Regular,"Helvetica Neue",Arial,sans-serif;font-size:0.875rem;line-height:1.25rem;font-weight:400;max-width:18rem;overflow:hidden;word-break:break-word;text-transform:none;-webkit-line-clamp:2;display:-webkit-inline-box;-webkit-box-orient:vertical;height:auto;padding:0.125rem 0.5rem;border-radius:0.5rem;color:#001435;background-color:#e6e0d9;}@media screen and (max-width: 752px){.css-32eus9-badge_base-text_caption-neutral{font-size:min(0.875rem, 28px);line-height:min(1.25rem, 40px);}}[dir='rtl'] .css-32eus9-badge_base-text_caption-neutral{text-align:right;}Optional](/api/rest/production/)[](/api/rest/production/)[Go Live](/api/rest/production/)Move from PayPal's production environment to go live.
