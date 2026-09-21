<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/managing-authorizations -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Managing Authorizations
slug: /articles/control-panel/transactions/managing-authorizations/
createTime: '2025-04-02T00:58:35.944Z'
updateTime: '2025-04-02T00:58:35.969Z'
---



# Managing Authorizations

All authorizations expire, though the timeframes differ [by payment method](/braintree/docs/reference/general/statuses#authorization-expired). This is a common challenge for businesses that wait to collect funds until they are ready to ship their products, provide their services, or need to adjust a transaction's amount post-authorization. Below are some options and limitations to be aware of when managing your authorization workflow.


**NOTE**
 
- For PayPal transactions, delaying settlement for shipped goods isn’t necessary thanks to[Seller Protection](https://www.paypal.com/webapps/mpp/security/seller-protection).
- Authorization and capture can incur merchant fees in some markets. For more information, see your[Braintree User Agreement](https://www.braintreepayments.com/legal).

 


## Authorization options

Merchants in some industries may want an authorization to stay active on a customer's account for longer than the timeframe established by the customer’s bank. There are two ways to do this in the Braintree gateway:


- [**Verify and store**](#verify-and-store)– recommended
- [**Multiple authorizations**](#multiple-authorizations)– not recommended

Eligible merchants that need to adjust the amount of a transaction after it has already been authorized (e.g. adding a tip post-authorization) can use the [authorization adjustment option](#authorization-adjustments).


### Verify and store

To use the verify and store method, follow these steps:


- If the customer's payment method is a credit or debit card, use[card verification](/braintree/docs/guides/credit-cards/server-side#card-verification)to ensure that the card is valid; otherwise, continue on to the next step
- Store the payment method in the[Vault](/braintree/docs/guides/customers#create)
- Store the customer ID and/or payment method token in your business’s database
- When you’re ready to collect funds,[create a transaction using the vaulted payment method](/braintree/docs/reference/request/transaction/sale/ruby#using-a-vaulted-payment-method)


#### Pros


- Little development work needed
- May save you money in processing fees, compared to the multiple authorizations method


#### Cons


- No guarantee that the customer will have sufficient funds at the time the transaction is created
- No guarantee that the customer’s account will be active at the time of the transaction


### Multiple authorizations


**NOTE**
 Because of the complications that this method can introduce to your customers and your developers, we don’t recommend it as a standard workflow.

 



If you decide that the multiple authorizations method is the best fit for your business, you will need to create logic on your end that identifies the payment method type from the [details returned in a results object](/braintree/docs/reference/response/transaction#payment_instrument_type) and then implement rules based on the payment method type’s [expiration timeframe](/braintree/docs/reference/general/statuses#authorization-expired). Here’s a suggestion of what this logic could look like:


- [Create a transaction](/braintree/docs/reference/request/transaction/sale)to authorize the amount you plan to charge; do not submit for settlement yet. Store the payment method in the vault using the "store in vault" option in the transaction request
- [Void the transaction](/braintree/docs/reference/request/transaction/void)within the appropriate expiration timeframe
- Create a new transaction to authorize the amount again using the vaulted token created in step 1. Do not submit for settlement yet
- Repeat steps 2 and 3 if you need to continue to extend the authorization
- When you’re ready to collect funds,[submit the latest transaction for settlement](/braintree/docs/reference/request/transaction/submit-for-settlement)


#### Pros


- Can guarantee that the customer has sufficient funds


#### Cons


- Considerable development work needed
- May cost more in processing fees
- The voids may result in[duplicate pending transactions](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids)on a customer’s account, causing confusion and preventing the customer from using those funds


### Authorization adjustments


**AVAILABILITY**
 Authorization adjustments are available for select merchants and processors. [See availability for details.](#availability)

 




#### Authorization adjustments without settlement

For some business models, there is a need to adjust an authorization for either more or less than the amount it was originally authorized for (e.g. incremental charges). This action is commonly referred to as an authorization (or auth) adjustment.

You can call our [Auth adjustment](/braintree/docs/reference/request/transaction/adjust-authorization) API to adjust an authorization as many times as you want by passing in a new authorization amount and the original authorization reference. If you adjust an authorization for less than the original authorized amount, we attempt a partial reversal in order to reverse the difference back to the cardholder. If you adjust for more than the original authorized amount, we attempt an incremental authorization to increase the authorized amount. In either case, if the cardholder’s issuing bank declines the adjustment, we will return a validation error. When an adjustment is declined in this way, the original transaction will remain in an Authorized status.


**AVAILABILITY**
 

  This is currently available only in US only for Visa and Mastercard.

 




#### Authorization adjustments during settlement

For some business models, there is a need to [submit a transaction for settlement](/braintree/docs/reference/request/transaction/submit-for-settlement#authorization-adjustments) for either more or less than the amount it was originally authorized for (e.g. tip adjustments).

If you submit for less than the original authorized amount, we attempt a partial reversal in order to reverse the difference back to the cardholder. If you submit for more than the original authorized amount, we attempt an incremental authorization to increase the authorized amount. In either case, if the cardholder’s issuing bank declines the adjustment, we will return a validation error. When an adjustment is declined in this way, the original transaction will remain in an Authorized status. If you had previously adjusted an authorization using the adjustment endpoint, you can still do one final adjustment while you [submit for settlement](/braintree/docs/reference/request/transaction/submit-for-settlement#authorization-adjustments).

If you qualify for and utilize auth adjustments, you will need to update your logic to listen for [validation errors](/braintree/docs/reference/general/validation-errors/overview) when submitting for higher or lower than the original authorized amount.


#### Availability

Authorization adjustments can only be made on Visa and Mastercard transactions, and are available for select processors in the following regions:


- US - Visa and Mastercard
- APAC - Visa and Mastercard
- EU - Visa and Mastercard
- Australia - Visa and Mastercard

All merchant categories are eligible to utilize Mastercard’s adjustment functionality; however, Visa limits adjustment usage to the following merchant categories:


- Lodging
- Vehicle rentals
- Cruise lines
- Restaurants and bars
- Amusement parks
- Taxicabs and rideshares
- General rental categories
- Electric vehicle charging
- Parking lots, parking meters, and garages
- Grocery stores and supermarkets


#### Benefits


- Real time decline responses for tip adjustments and partial captures
- Auth adjustment details allow merchants to track adjustment success rates

