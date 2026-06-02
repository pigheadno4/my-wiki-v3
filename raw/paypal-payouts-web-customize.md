---
title: Customize your payouts integration
slug: /docs/payouts/standard/payouts-web/customize/
createTime: "2024-12-10T13:26:30.239Z"
updateTime: "2025-11-25T03:29:50.278Z"
---

# Customize your payouts integration

## Send payments in a different currency

Send payments in [certain currencies](/docs/payouts/standard/reference/currency-conversion/#automatic) even if you don’t maintain a balance in that currency. It’s easy to view funding balances, see currency exchange rates, and monitor your payments.

**Note** : Before using Payouts Web to send payments in another currency, make sure you [enable Payouts Web](/docs/payouts/standard/payouts-web/#1-enable-payouts-web) .

[Prepare and upload a recipient data file](/docs/payouts/standard/payouts-web/#2-create-a-payment-file) as you would normally. A payout can be sent in a single currency, so if you need to make payments in multiple currencies, set up a separate payout for each currency. Payouts will automatically convert your funding currency to the supported currency.

If you need to make payments in multiple currencies, set up a separate payout for each currency. Payouts will automatically convert your funding currency to the supported currency.

Before sending, you'll see a preview of the payout, including fees and currency exchange calculation. You can view details for any individual payment, too. [See how currency exchange rates are calculated](https://www.paypal.com/uk/cshelp/article/where-can-i-find-paypals-currency-calculator-and-exchange-rates-HELP109) .

When you’re ready, send the payout.

## Track the payout status

Log in to your PayPal account and go to **Activities** to see the status of your payout and each payment. Click on the payout to see details of individual payments. The downloadable CSV and TXT files include the exchange rate, fee, and total amount in both currencies.

**Note** : See a list of country [exclusions](/docs/payouts/standard/reference/currency-conversion/#exclusions) and [restrictions](/docs/payouts/standard/reference/currency-conversion/#restrictions) for payouts currency conversion.

## Set payouts approvals

Once you've enabled Payouts Web, merchants can enable users to approve payouts.

In the PayPal business account dashboard, go to **Account Settings** and take these steps to set users to approve payouts:

- Select **Account access** , then **update** Manage users.
- On the **Manage users** page, select **Manage Approvals** .
- Select users to review and approve payouts.

One user can't start and approve a payout.

## See also

- Get [troubleshooting](/docs/payouts/standard/reference/troubleshooting/) information.
- See the payouts [FAQ](/docs/payouts/standard/reference/faq/) .
