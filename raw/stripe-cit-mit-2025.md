<!-- Source URL: https://docs.stripe.com/payments/cit-mit -->
<!-- Fetched: 2026-05-01 -->

# Customer-Initiated Transactions (CIT) and Merchant-Initiated Transactions (MIT)

Learn about card network rules based on who initiates a transaction.

The card networks divide card payments into two types, depending on whether the customer is participating in the payment flow: Customer-Initiated Transactions (CIT) and Merchant-Initiated Transactions (MIT).

> Card networks assign different characteristics and requirements to transactions, depending on whether they’re customer-initiated or merchant-initiated. For example, a Visa transaction’s authorization validity period varies depending on its type. If you’re using the API, the [payment_method_details.card.capture_before](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) attribute on the charge is the most reliable and accurate way to determine your charge’s authorization window.

## Merchant-Initiated Transactions (MIT)

An MIT is a transaction that you initiate without direct participation of your customer, based on a prior agreement with that customer authorizing you to store and use their credentials. For example, you operate a subscription-based business and your customer has consented to you collecting their future monthly payments using their credit card that you have on file.

### Compliance

When you save a customer’s payment information, regardless of the reason, you’re responsible for compliance with all applicable laws, regulations, and network rules. Include terms on your website or app that state how you save payment method details, and require customers to opt in before you save their payment information.

When you save a payment method, you can only use it for the specific purposes included in your terms. For example, if you want to automatically charge a saved payment method for future subscription renewals, you must first get explicit consent for that from the customer. You can collect that consent by including a “Save my payment method for automatic renewals” checkbox on the initial payment page.

To charge customers when they’re offline, include the following in your terms:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions
- The anticipated timing and frequency of payments; for example, whether the charges are for scheduled installments, subscription payments, or unscheduled top-ups
- How you determine the payment amount
- Your cancellation policy for any subscription services

Keep a record of each customer’s agreement to your terms.

### Card brand changes

Stripe’s Card Account Updater automatically updates saved cards when necessary, such as when a card expires or is re-issued. In some cases, an automatic update changes a card’s brand (for example, from Visa to Mastercard). When a card’s brand changes, you must prompt the cardholder to update their payment method.

Identify card brand changes by listening for the `payment_method.automatically_updated` event and comparing the `brand` in `previous_attributes` with the `brand` in the associated `card` object.

> #### Re-authorization requirement
>
> When a card’s brand changes, you can’t charge it for any MITs until you get a new cardholder agreement.

## Customer-Initiated Transactions (CIT)

CITs normally include all other transaction types, including any transaction where the cardholder is available to participate in the payment flow. For example, a customer manually places an order on your website.
