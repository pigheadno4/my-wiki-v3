<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/reference/faq/ -->

## <!-- Fetched: 2026-04-16 -->

title: Payouts frequently asked questions
slug: /docs/payouts/standard/reference/faq/
createTime: '2024-08-15T07:31:41.826Z'
updateTime: '2025-05-12T09:15:36.485Z'

---

# Payouts frequently asked questions

- [Is there a fee to send Payouts?](#is-there-a-fee-to-send-payouts)
- [How much money can I send?](#how-much-money-can-i-send)
- [Which countries can receive Payouts?](#which-countries-can-receive-payouts)
- [Can I send money in different currencies?](#can-i-send-money-in-different-currencies)
- [How do I confirm the receipt of payments?](#how-do-i-confirm-the-receipt-of-payments)
- [How do I cancel an individual payment?](#how-do-i-cancel-an-individual-payment)
- [A recipient told me that payment was not received. What could be the problem?](#a-recipient-told-me-that-payment-was-not-received-what-could-be-the-problem)

## Is there a fee to send Payouts?

PayPal charges the sender a percentage of each payment with the fee capped at a set amount in your primary currency. Payout recipients pay no fee regardless of the type of PayPal account they have. For detailed information about payout fees, see thePayPal [Merchant Fees](https://www.paypal.com/us/webapps/mpp/merchant-fees/) page.

## How much money can I send?

There is no limit on the total amount of the payout. Each individual payment can be no more than $20,000.00 USD or its equivalent in local currency by default. If you need to send higher value payments, please contact your account representative or [Customer Service](https://www.paypal.com/smarthelp/contact-us) .

## Which countries can receive Payouts?

Payouts are supported in over 156 countries in over 23 currencies. Note that currency restrictions do not allow conversion of Argentine Pesos, Brazilian Real, or Malaysian Ringgit. PayPal currency conversion rates apply should the sender or the recipient choose to convert the payments. For more information, see the [International coverage](/docs/payouts/standard/reference/country-feature/) .

## Can I send money in different currencies?

Yes, but you must make separate payment files for each currency.

If you choose to send one currency to a number of different countries, your recipients will have the option to convert the money into their selected currency.

Argentina, Brazil, and Malaysia have restrictions on how their currency can be used or exchanged. PayPal account holders in these countries should make sure that their payment file entries comply with these restrictions. For more information about currency restrictions, see countries with [currency restrictions](/docs/payouts/standard/reference/currency-conversion/#restrictions) .

## How do I confirm the receipt of payments?

PayPal sends you a notification email after each Payouts request completes. You can also log in to your PayPal account to check the status and review the details of each transaction using these logs:

- [Transaction activities](/docs/payouts/standard/reports/view-transaction-activities) — View a complete summary of one payout.
- [History log](/docs/payouts/standard/reports/search-transactions/) — Download and view individual payments by date range.

For more information on reports, see [Reporting](/docs/payouts/standard/reports/) .

For more information on notification subscriptions, see [Webhooks](/docs/integration/direct/webhooks/) .

## How do I cancel an individual payment?

You can only cancel payments that have an unclaimed status. Unclaimed payments will automatically expire in 30 days, and PayPal will return the money to your PayPal account.

To cancel an unclaimed payment:

- Log in to your PayPal business account at [www.paypal.com](https://www.paypal.com) and view your recent activity by clicking **Activity** at the top of the page, then scroll down to the **Activity** list.
- Directly above the list, enter the email address of your recipient and make sure that **Email Address** is selected in the **Search for transaction** dropdown menu.
- Adjust the date range and click **Search** . Your recipient's payment appears in the list.
- From the list, click on the title of the payment you want to cancel. The Details page for the specified item opens.
- Select **Cancel** and follow the instructions.

To cancel an unclaimed payment using the Payouts REST API, see [Cancel unclaimed payout item](/docs/api/payments.payouts-batch/v1/#payouts-item_cancel) .

## A recipient told me that payment was not received. What could be the problem?

Possible explanations include:

- **Incorrect email address** : Verify your recipient's email address. If the email address is incorrect, you can cancel an unclaimed payment and resend the payment.
- **Recipient has an unconfirmed email address** : Your recipient cannot receive a payment with an unconfirmed email address. Ask your recipient to confirm the email address with PayPal. Once that's done, the payment should appear in the recipient's PayPal account within a few minutes.
- **Recipient did not receive the payment email** : Sometimes PayPal emails get redirected to a recipient's spam folder. If this is the case, the recipient can simply log in to PayPal to view the payment. Also, double-check the email address in your Payouts file. There could be a misspelling or a formatting problem.
