<!-- Source URL: https://developer.paypal.com/braintree/articles/br/transactions/installments -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Installments
slug: /articles/br/transactions/installments/
createTime: '2025-04-02T01:46:08.610Z'
updateTime: '2025-04-02T01:46:08.845Z'
---



# Installments

In Brazil, it is common for transactions to be paid in installments. These installments are spaced 30 days apart and can occur in sets of 2-12. Installments can be subject to alteration due to refunds and disputes and have fees associated with them. Every installment transaction is associated with a set of installments, which will detail the installment amount, timing, and any adjustments created as the result of refunds or chargebacks. Read below to learn more about how to create and manage installment transactions.


## Card Types

By default, your account is set up to accept installments on the following card types:


- Visa
- Mastercard
- Amex
- Elo
- Hipercard


### Installment support on combo cards

In Brazil, installments are only supported for credit cards. If you are using a combo card, you can specify the card is a combo card by using the account_type field in the transaction sale call.


## Creating Installments


### Request

In order to create a transaction with installments, you'll need to specify the total transaction amount, and an integer between 2 and 12 that indicates the total number of installments over which the transaction should contain. To create a transaction with installments, include the following information in your [Transaction.sale()](/braintree/docs/reference/request/transaction/sale/ruby) request:


- installmentCount:String- Number of monthly installments (can be anywhere between 2 and 12)


### Ruby
```ruby
result = gateway.transaction.sale(
    :amount => "100.00",
    :installments => {
        :count => "4",
    },
    :order_id => "order id",
    :merchant_account_id => "a_merchant_account_id",
    :payment_method_nonce => nonce_from_the_client,
    :device_data => device_data_from_the_client,
    :customer => {
        :first_name => "Drew",
        :last_name => "Smith",
        :company => "Braintree",
        :phone => "312-555-1234",
        :fax => "312-555-1235",
        :website => "http://www.example.com",
        :email => "drew@example.com"
    },
    :billing => {
        :first_name => "Paul",
        :last_name => "Smith",
        :company => "Braintree",
        :street_address => "1 E Main St",
        :extended_address => "Suite 403",
        :locality => "Chicago",
        :region => "IL",
        :postal_code => "60622",
        :country_code_alpha2 => "US"
    },
    :shipping => {
        :first_name => "Jen",
        :last_name => "Smith",
        :company => "Braintree",
        :street_address => "1 E 1st St",
        :extended_address => "Suite 403",
        :locality => "Bartlett",
        :region => "IL",
        :postal_code => "60103",
        :country_code_alpha2 => "US"
    }
)
```

**NOTE**
The amount field should have the total installment amount in Brazilian Real. The total amount of the transaction is split equally into the desired installments. Each installment must have a calculated amount of at least 5 BRL.

  For example: If the requested amount is 50 BRL, and the installment count is 10, then each installment will have a calculated amount of 5 BRL.

 


### Response

The following fields will be returned as part of the response:


- installment_count:String- Number of monthly installments (Echoed back from the request)


## Settling Installment Transactions

Sale transactions can be submitted for settlement immediately or they can be settled separately later. Auth expiration timelines apply for transactions that are settled later.


### Request


#### Settling immediately

Transactions can be submitted for settlement immediately using [options().submitForSettlement()](/braintree/docs/reference/request/transaction/sale/ruby#options-submit_for_settlement) on the [Transaction.sale()](/braintree/docs/reference/request/transaction/sale/ruby) call. No extra information is needed if you choose to settle immediately.


#### Settling later

Sale transactions can be submitted for settlement later by calling [Transaction.submitForSettlement()](/braintree/docs/reference/request/transaction/submit-for-settlement/ruby). If chosen to settle later, the total amount can be adjusted during settlement.

To adjust the total amount during settlement, send in the following field:


- amount:String


**NOTE**
 The adjusted amount should be equal or lower than the authorized amount. The total amount of the transaction is split equally into the desired installments. Each installment must have a calculated amount of at least 5 BRL. For example: If the requested amount is 50 BRL, and the installment count is 10, then each installment will have a calculated amount of 5 BRL.

 


### Response

The following fields will be returned as part of [Transaction.submitForSettlement()](/braintree/docs/reference/request/transaction/submit-for-settlement/ruby) response. If settled as part of the [Transaction.sale()](/braintree/docs/reference/request/transaction/sale/ruby) call, the same fields will be returned in the response.


- installment_count:String- (echoed back from the request)
- amount:String- (echoed back from the request)
- An array of
- id:String- IDs of individual installments
- amount:String- Amount of individual installments




## Refunding Installments

Installments can be adjusted through refunds. Whether it is through a single refund or multiple refunds, [Transaction.refund()](/braintree/docs/reference/request/transaction/refund/ruby) response will contain the effect the refund has on individual installments.


### Request

No additional fields are needed for installment refunds. Simply call [Transaction.refund()](/braintree/docs/reference/request/transaction/refund/ruby) with the total amount to be refunded.


### Response

The following fields will be returned as part of the response:


- installment_count:String(echoed back from the request)
- amount:String(echoed back from the request)
- An array of installments:
- id:String
- amount:String


- An array of adjustments:
- amount:String
- kind:String




## Chargebacks

In addition to refunds, installments can also be adjusted by chargebacks. The adjustmentReason field will indicate the reason the adjustment was triggered.


## Getting Installment Details

Complete installment information can be retrieved using the **Search API** or through the **Control Panel** search. You will receive the following installment-specific information


- Total amount
- Installment Count
- An array of the following individual information (depending on the number of installments requested)
- Installment ID
- Installment Amount
- Projected Clearing Date
- Actual Clearing Date
- Adjustment Amount
- Adjustment Reason




### Searching for Installment Transactions via API

To get full installment information (including disbursement dates), simply search for the installment transaction using [Transaction.search()](/braintree/docs/reference/request/transaction/search/ruby). Here, you can search by transaction date, transaction ID, amount, customer ID, and more.


### Searching for Installment Transactions via the Control Panel

To retrieve installment transaction details in the Control Panel, follow the instructions below:


- Log into the**Control Panel**
- Click on**Transaction Search**in the navigation bar
- Search for the installment transaction (using the number of search options provided on the page)
- Click on the**Search**button
- If only a single transaction was matched, the page will be routed to the transaction detail page
- If you have several search results, click on the public id of the transaction that you would like to get more information on



