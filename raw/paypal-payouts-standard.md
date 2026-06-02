---
title: Standard Payouts
slug: /docs/payouts/standard/
createTime: "2024-08-15T07:19:30.665Z"
updateTime: "2025-11-25T21:42:42.535Z"
---

# Standard Payouts

Send money immediately to multiple recipients in 96 countries and 24 currencies using only their email, phone number, or PayPal ID.

**Important:** To use PayPal Payouts, you'll need to [request access](https://www.paypal.com/payoutsweb/landing) .

## How it works

Payouts make it easy for recipients to claim their money using either PayPal or Venmo:

- If they already have a PayPal or Venmo account, an email or mobile notification will prompt them to log in to their account to get payment details.
- If they don't have a PayPal or Venmo account, an email or mobile notification will prompt them to open a PayPal or Venmo account to claim their money.

**Note:** Venmo notifications require a U.S. mobile number and are mobile only.

### PayPal recipient flow

![PayPal,flow,for,new,and,existing,users](assets/paypal-payouts-paypal-flow.svg)

### Venmo recipient flow

![Venmo,flow,for,new,and,existing,users](assets/paypal-payouts-venmo-flow.svg)

## Eligibility

- Venmo can be used for payouts in the US using USD only.
- Some countries have limited or restricted payout features. See the full list of [Country and feature support](/docs/payouts/standard/reference/country-feature/) .

## Payouts prerequisites

For all payout options, you'll need the following:

- A PayPal business account
- Access to PayPal Payouts
- A confirmed identity, email, and bank account linked to your PayPal business account
- Sufficient funds in your PayPal business account

### Get a PayPal business account

If you don't have one, [sign up for a PayPal business account](https://www.paypal.com/bizsignup/) . You'll be asked for information about you and your business to secure your account. The PayPal business account serves as the digital wallet for your business.

After you sign up for an account, complete the following steps to enable the account to send payouts.

### Get access to PayPal Payouts

[Request access to PayPal Payouts](https://www.paypal.com/payoutsweb/landing) . You’ll be asked for information about your business needs to ensure the solution is a good fit for you. After you apply, PayPal will email you the decision. In the meantime, you can set up and test your integration in your sandbox accounts.

### Complete your account setup

These links take you to your merchant profile page to complete each step.

- [Confirm your identity](https://www.paypal.com/policy/flow/verifyCip) . PayPal verifies your identity to secure your account and comply with rules and regulations in your country.
- [Confirm your email](https://www.paypal.com/in/cshelp/article/how-do-i-confirm-my-email-address-help138) . Enable email communication between PayPal and your business.
- [Link to your bank account](https://www.paypal.com/businessexp/money/addbank) . Transfer money from your PayPal account to your bank.

### Add funds to your PayPal balance

Payouts are funded using your PayPal balance, so be sure to add enough to cover your payout total, including [fees](https://www.paypal.com/us/webapps/mpp/merchant-fees#paypal-payouts) . You can send payments in [certain currencies](/docs/payouts/standard/reference/currency-conversion/#automatic) even if you don't maintain a balance in that currency. To make payments in other currencies, you can [transfer your balance to another currency](https://paypal.com/us/smarthelp/article/how-do-i-transfer-my-balance-to-another-currency-faq1025) .

## How do you want to make payouts?

Choose how you want to make payouts from the following options.

- [API integration](/docs/payouts/standard/integrate-api) : Initiate payout requests using the Payouts API
- [Large Batch](/docs/payouts/standard/large-batch) : Create and upload payouts files to a secure FTP server
- [Payouts Web](/docs/payouts/standard/payouts-web) : Create and upload payout files using Payouts Web
