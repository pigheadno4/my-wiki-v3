---
title: Pay upon Invoice with Ratepay
slug: /docs/checkout/apm/pay-upon-invoice/
createTime: "2024-08-15T05:57:43.669Z"
updateTime: "2025-05-12T15:54:21.055Z"
---

# Pay upon Invoice with Ratepay

Pay upon Invoice is an invoice payment method in Germany. It's a local buy now, pay later payment method thatallows the buyer to place an order, receive the goods, try them, verify they are in good order, and then pay the invoice within 30 days. No PayPal account is needed for the buyer to use Pay upon Invoice.

PayPal has partnered with Ratepay to provide this service. This payment method is also called Rechnungskauf mit Ratepay in German.

## Eligibility

**Important:** When adding Pay upon Invoice with Ratepay/Rechnungskauf mit Ratepay as a payment option to your checkout integration, you must [acknowledge and accept these Terms](https://www.paypal.com/de/webapps/mpp/ua/rechnungskauf-mit-ratepay?locale.x=eng_DE) and understand they are part of the PayPal User Agreement.

| Buyer relevant countries | Merchant relevant countries | Payment method type | Minimum amount | Maximum amount | Refunds         |
| ------------------------ | --------------------------- | ------------------- | -------------- | -------------- | --------------- |
| Germany (DE)             | Germany (DE)                | deferred payment    | 5EUR           | 2500EUR        | Within 180 days |

- This integration is available only in Germany to eligible merchants.
- You must sell goods in the B2C model only.
- You must ship orders within seven days after the transaction.
- You must be approved to accept transactions using this payment method. PayPal will ask you to enter a valid VAT ID Number as per EU regulations. Without a valid VAT ID for your business, PayPal is required to collect additional VAT as applicable on PayPal fees. Request approval to enable Pay upon Invoice by visiting these Sandbox and Live links: - Sandbox - [https://www.sandbox.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE](https://www.sandbox.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE)
- Live - [https://www.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE](https://www.paypal.com/bizsignup/entry?country.x=DE&product=payment_methods&capabilities=PAY_UPON_INVOICE)

- Paying for digital or virtual goods, including, but not limited to any form of vouchers, such as gift vouchers, gift cards, and cash codes, and any transactions outside of PayPal's Acceptable Use Policy is not allowed with Pay upon Invoice.

## How it works

PayPal facilitates the interaction between you and Ratepay:

- PayPal sends the buyer information to Ratepay for risk assessment. Depending on the result, Ratepay will send the buyer payment instructions or a rejection notice.
- You are funded immediately when the buyer successfully completes the checkout process with the Pay upon Invoice method. The buyer pays Ratepay instead of you. Ratepay is responsible for following up with the buyer to ensure the payment is made.
- You must inform the buyer that they have 30 days to pay Ratepay via bank transfer.
- PayPal may contact you in case a buyer has opened a dispute with Ratepay. You are required to respond to these inquiries.

### Buyer experience

- Buyer selects the Pay upon Invoice payment option. At the time of payment method selection, display the benefits of deferred payments and the due date for the payment. ![Pay,upon,Invoice,selected](assets/paypal-pui-selected.png)
- The buyer provides their information to process the Pay upon Invoice payment: full name, email, delivery and billing address, date of birth, and phone number. ![Pay,upon,Invoice,form](assets/paypal-pui-form.png)
- Near the **Buy Now** button, show legal text provided in the integration instructions so that the buyer is aware of the terms before you send any information to PayPal. ![PUI,transaction,details](assets/paypal-pui-transaction-details.png)
- On a successful transaction, Ratepay emails payment instructions to the buyer. On the Order Success page, you can provide transaction details and notify the buyer to wait for payment instructions from Ratepay. If Ratepay declines the transaction due to buyer risk reasons, you must display the error message as shown in the [Error handling section](/docs/checkout/apm/pay-upon-invoice/integrate-pui-merchant/#error-codes-and-error-messages) . ![PUI,email,notifications](assets/paypal-pui-email-notifications.png)
- Buyer receives an invoice with cart details and Ratepay’s payment instruction details, including the payment reference number, that are returned in the API response. Always use the payment instructions details provided on a per-transaction basis to ensure accuracy. In the invoice, instruct the buyer to pay only with Ratepay. Here's a sample invoice: ![Sample,invoice,image](assets/paypal-pui-sample-invoice.svg) Here's a sample payment instructions email from Ratepay: ![Sample,payment,instructions,email](assets/paypal-pui-payment-instructions-email.svg)
- Buyer pays Ratepay by logging into their bank account and making a bank transfer. If you have a simplified integration, you are obliged to ship the order within 7 calendar days.
- If the buyer does not pay within the due date, the buyer is subject to dunning fees charged by Ratepay. There is no action required from you during the follow-up and dunning process.

### Dispute handling

Buyers can open a dispute with Ratepay. You must respond within 10 business days with evidence, either through the PayPal Resolution Center or with the Disputes API. If you don't respond within the timeframe, you're subject to an automatic reversal of the disputed funds.

When responding to disputes, you must, depending on the dispute type:

- Provide the carrier name and shipping tracking number. You need these to respond to an "Item Not Received" dispute.
- Provide the invoice you sent to the buyer as part of the evidence.
- In certain cases, additional written explanation might be required. For example, if a buyer has returned the item and claims no refund was received.
- Retain the proof of shipment and delivery for at least 180 days from the time of order placement. There might be instances when you're asked for this evidence after 90 days of order placement for Ratepay to legally defend a buyer-defaulted transaction. If you don't provide this evidence, you're subject to an automatic reversal of the disputed funds.

Carrier companies delete tracking information after 90 days, so make sure you have an image or PDF copy to respond to the dispute and avoid the reversal of funds.

### Provide shipment information

As soon as a shipment is made, send tracking information to PayPal. Include the tracking ID and carrier name through either the:

- [Add Tracking API](/docs/tracking/tracking-api/integrate/) . Send shipment tracking numbers for all Rechnungskauf mit Ratepay transactions. Set notify_buyer to false for all Pay upon Invoice transactions.
- Transaction details page in your PayPal account.

Providing this information to PayPal can help you respond to dispute cases later. Especially in older cases where you can't get tracking information from your carrier.

### VAT statements

You can access monthly VAT Statements through your PayPal account. These statements reflect a summary of VAT collected by PayPal for any fees charged by PayPal. You can use these statements to claim your tax credits or self-assessment of VAT charges.

## Next step

- [Integrate Pay upon Invoice](/docs/checkout/apm/pay-upon-invoice/integrate-pui-merchant/)
