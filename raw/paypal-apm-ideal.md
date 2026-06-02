---
title: Accept iDEAL payments
slug: /docs/checkout/apm/ideal/
createTime: "2024-10-25T11:47:59.161Z"
updateTime: "2025-05-09T11:00:11.436Z"
---

# Accept iDEAL payments

iDEAL is a payment method in the Netherlands, enabling buyers to select their issuing bank from a provided list. The buyer experience varies depending on the bank they choose once they are redirected to the issuing bank's platform.

| Countries        | Payment type  | Payment flow | Currencies | Minimum amount | Refunds         |
| ---------------- | ------------- | ------------ | ---------- | -------------- | --------------- |
| Netherlands (NL) | bank redirect | redirect     | EUR        | 0.01EUR        | Within 180 days |

## How it works

![Alternative,payment,methods,diagram](assets/paypal-apm-unbranded-flow.svg)

- Your checkout page offers alternative payment methods.
- The buyer enters their personal details and selects an alternative payment method from your checkout page.
- The buyer is redirected to their selected issuing bank to confirm the purchase.
- The buyer authorizes and completes the payment.
- The buyer returns to your website to see the confirmation of the purchase.
- The merchant completes the payment process. PayPal transfers the funds to the merchant, and the transaction shows up in your PayPal account with the buyer's chosen payment method.

## Eligibility

- Available to merchants globally (excluding Russia, Japan, and Brazil).
- Billing agreements, multiple seller payments, and shipping callbacks are not supported.
- Only supports order capture (order authorization is not supported). See [authorised and captured payments](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/authcapture/) for details.
- Chargebacks are not supported.
- Transactions must be online purchases (buy online, pay in-store is not supported).

## Onboard a merchant for iDEAL payments

For merchants operating incountries such as: AT , AU , BE , BG , CA , CY , CZ , C2 , DE , DK , EE , ES , FI , FR , GR , HU , IE , IT , LI , LT , LU , LV , MT , NL , NO , PL , PT , RO , SE , SI , SK , UK , and US follow these steps to onboard them for iDEAL payments:

- **Step 1:** The merchant must complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=iDEAL&capabilities=IDEAL) to process iDEAL payments with their PayPal account. For more details, refer [here](https://paypal.com/businessmanage/account/payments) .
- **Step 2:** Merchants can check their onboarding status directly in their [PayPal account.](https://paypal.com/businessmanage/account/payments)

**info**
**Note:** Partners can streamline merchant onboarding using the Integrated Sign-Up (ISU) flow by following these steps:

- Send an API call to the [Partner Referral API](https://developer.paypal.com/docs/api/partner-referrals/v2/.) .
- Pass iDEAL in the products array and skip the capabilities array to ensure the request works perfectly.

For merchants outside the listed countries, offline onboarding is required.

- **Step 1:** The merchant must complete the [Critical Infrastructure Protection (CIP)](https://developer.paypal.com/api/rest/reference/info-security-guidelines/) process using their PayPal account.
- **Step 2:** Enable iDEAL for the merchant by coordinating with your Customer Success Manager or Sales team representative.

**error**
**Important:** Ensure that the merchant includes their website URL in their PayPal account during this process.

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API for a fully customised checkout experience.
