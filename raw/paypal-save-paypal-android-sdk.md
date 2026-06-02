---
title: Save PayPal with the Android SDK
slug: /docs/checkout/save-payment-methods/during-purchase/android-sdk/paypal/
createTime: "2024-12-18T10:16:00.181Z"
updateTime: "2025-03-06T16:07:57.584Z"
---

# Save PayPal with the Android SDK

Allow customers to save their PayPal Wallet in order to eliminate the need to
re-enter payment details on subsequent purchases - leading to a faster
checkout experience.

**Important:**Don’t save PayPal as a payment method during purchase. For more information about securely saving payment methods and optimizing the buyer experience, see our[Best practices guide](/docs/checkout/standard/best-practices/).Customers with a PayPal Wallet can:

- Review PayPal transactions and transaction history
- Review, add, or remove funding sources
- Review and cancel recurring payments
- Hold a balance in their PayPal account
- Use PayPal to send and receive money
- Withdraw money to a linked bank account
- Use PayPal to transact with merchants

## Use cases

Businesses save payment methods if they want customers to:

- Check out without re-entering a payment method
- Pay after use, for example, ride-sharing and food delivery

## Availability

### See supported countries

- Australia
- Austria
- Belgium
- Bulgaria
- Canada
- China
- Cyprus
- Czech Republic
- Denmark
- Estonia
- Finland
- France
- Germany
- Hong Kong
- Hungary
- Ireland
- Italy
- Japan
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malta
- Netherlands
- Norway
- Poland
- Portugal
- Romania
- Singapore
- Slovakia
- Slovenia
- Spain
- Sweden
- United Kingdom
- United States

## Check eligibility

- Go to [paypal.com](https://www.paypal.com) and sign in with your
  business account.
- Go to **Account Settings** &gt; **Payment Preferences** &gt; **Save PayPal and Venmo payment methods** .
- In the Save PayPal and Venmo payment methods section, select **Get Started** .
- When you submit profile details, PayPal reviews your eligibility to save
  PayPal Wallets.
- After PayPal reviews your eligibility, you'll see a status of **Success** , **Need more information** , or **Denied** .

## How it works

PayPal encrypts payment method information and stores it in a digital vault
for that customer.

- Create an order with a PayPal payment source.
- Present PayPal Web Checkout to the payer using the PayPal SDK.
- After the payer completes PayPal Web Checkout, capture or authorize the
  order.
- On success, store the PayPal-generated customer ID and payment token found
  in the capture or authorize response in your server-side database for future
  reference.
- When a customer returns to your app and is ready to check out, use the
  PayPal-generated payment token as a payment source when creating an order.

The checkout process for returning payers can now be made shorter by using
saved payment information.

## Know before you code

- This integration requires a PayPal Developer account.
- This procedure modifies an existing [standard payments](https:/docs/checkout/standard/) or [advanced credit and debit card payments](https:/docs/checkout/advanced/) integration.
- Your payments integration must have a [server-side capture call](https:/docs/api/orders/v2/#orders_capture) or a [server-side authorization and capture call](https:/docs/api/orders/v2/#orders_capture) .
- To save payment methods, you must be able to uniquely identify payers. For
  example, payers create an account and log in to your site.
- Complete the steps in [Get started](https:/api/rest/) to get the
  following sandbox account information from the Developer Dashboard: - Your sandbox account login information
- Your access token

## 1. Set up sandbox to save payment methods

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps** , select your app name.
- Under **Sandbox App Settings** &gt; **App Feature Options** , check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

To go live, you'll need to be vetted for PayPal Wallet. You can start the
vetting process from the Merchant Servicing Dashboard.

- Only your sandbox business account is enabled for vaulting payment methods.
  Your developer account remains unaffected.
- You'll complete production onboarding when you're ready to go live.

  **Tip:** When prompted for data such as a phone number for the
  sandbox business request, enter any number that fits the required format.
  Since this is a sandbox request, the data doesn't have to be factual.

## 2. Add a button to initiate a transaction

Add a button to your app's UI to complete a purchase with PayPal:

1AndroidView(2factory={context-&gt;3PayPalButton(context).apply{4setOnClickListener{5// Create order server-side (see next step)6}7}8}9)## 3. Create an order
Set up your server to call the Orders API. Set the payment_source to paypal and request vaulting of the
payment source when the transaction completes successfully.

### Create order request

Modify the following request to create an order and initiate a vault for a
PayPal payment source:

1curl-v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-H"PayPal-Request-Id: REQUEST-ID"\\5-d'{6"intent": "CAPTURE",7"purchase_units": [{8"amount": {9"currency_code": "USD",10"value": "100.00"11}12}],13"payment_source": {14"paypal": {15"attributes": {16"vault": {17"store_in_vault": "ON_SUCCESS",18"usage_type": "MERCHANT",19"customer_type": "CONSUMER"20}21},22}23}24}'### Create order response
Return the id to your client to call the payer approval flow if
the payment_source needs payer approval.

**Note:** The request to save a PayPal payment source is made
when an order is created with the payment_source.attributes.vault.store_in_vault property set to true . Vault details are available only after an order is
authorized or captured.

1{2"id":"5O190127TN364715T",3"status":"PAYER_ACTION_REQUIRED",4"payment_source":{5"paypal":{}6},7"links":[{8"href":"https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",9"rel":"self",10"method":"GET"11},12{13"href":"https://www.paypal.com/checkoutnow?token=5O190127TN364715T",14"rel":"payer-action",15"method":"GET"16}17]18}## 4. Start PayPal Web Checkout
Locate the id property in the Orders API response JSON. This is
the Order ID.

Send orderId to the Android SDK to allow it to start PayPal Web
Checkout:

1funstartPayPalWebCheckout(){23// Set up PayPalWebClient4valcoreConfig=CoreConfig("CLIENT_ID")5valdeepLinkUrlScheme="com.myapplication.android"6valpayPalWebClient=PayPalWebClient(activity,coreConfig,deepLinkUrlScheme)78// Set up PayPalWebCheckoutListener9payPalWebCheckoutClient.listener=object:PayPalWebCheckoutListener{1011funonPayPalWebSuccess(result:PayPalWebCheckoutResult){12// After the payer approves, authorize or capture the transaction on your server (see next step)13}1415funonPayPalWebFailure(error:PayPalSDKError){16// Notify user of failure17}1819funonPayPalWebCanceled(){20// Allow user to retry21}22}2324valrequest=PayPalWebRequest(orderId="ORDER_ID")25payPalWebCheckoutClient.start(request)26}## 5. Authorize or capture order
After the payer approves, do one of the following on your server:

- Capture the order using the Orders API if the intent passed to
  create the order was CAPTURE
- Authorize the order using the Orders API if the intent passed
  to create the order was AUTHORIZE

When capture or authorization succeeds, a vault.id is created.

### Authorize order request

1curl-v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-d'{}'### Capture order request
1curl-v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture\\2-H"Content-Type: application/json"\\3-H"Authorization: Bearer ACCESS-TOKEN"\\4-d'{}'### Capture order response

The HTTP response codes HTTP 2xx or HTTP 200 are
returned for a successful request.

The capture is successful if the purchase_units[0].payments.captures.status is COMPLETED . You can confirm with the payer that the payment has
been captured.

In the response from the authorize or capture request, the Orders v2 API
interacts with the Payment Method Tokens v3 API. The Payment Method Tokens v3
API allows a PayPal Wallet to be saved. The response from the Orders v2 API
contains the:

- vault.id
- customer.id
- vault.status
- links for the payment token of a recently saved PayPal Wallet.

#### Capture order

1{2"id":"5O190127TN364715T",3"status":"COMPLETED",4"payment_source":{5"paypal":{6"attribute":{7"vault":{8"id":"3nqvjt3n",9"customer":{10"id":"208743798"11},12"status":"VAULTED",13"links":[{14"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/3nqvjt3n",15"rel":"self",16"method":"GET"17},18{19"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/3nqvjt3n",20"rel":"delete",21"method":"DELETE"22},23{24"href":"https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",25"rel":"up",26"method":"GET"27}28]29}30},31"name":{32"given_name":"Firstname",33"surname":"Lastname"34},35"email_address":"customer@example.com",36"phone_number":{37"national_number":"2025212022"38},39"account_id":"QYR5Z8XDVJNXQ",40"address":{41"country_code":"US"42},43}44},45"payer":{46"name":{47"given_name":"Firstname",48"surname":"Lastname"49},50"email_address":"customer@example.com",51"phone_number":{52"national_number":"2025212022"53},54"payer_id":"QYR5Z8XDVJNXQ",55"address":{56"country_code":"US"57}58}59"purchase_units":[{60"reference_id":"d9f80740-38f0-11e8-b467-0ed5f89f718b",61"payments":{62"captures":[{63"id":"3C679366HH908993F",64"status":"COMPLETED",65"amount":{66"currency_code":"USD",67"value":"100.00"68},69"seller_protection":{70"status":"ELIGIBLE",71"dispute_categories":[72"ITEM_NOT_RECEIVED",73"UNAUTHORIZED_TRANSACTION"74]75},76"final_capture":true,77"seller_receivable_breakdown":{78"gross_amount":{79"currency_code":"USD",80"value":"100.00"81},82"paypal_fee":{83"currency_code":"USD",84"value":"3.00"85},86"net_amount":{87"currency_code":"USD",88"value":"97.00"89}90},91"create_time":"2022-01-01T21:20:49Z",92"update_time":"2022-01-01T21:20:49Z",93"links":[{94"href":"https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F",95"rel":"self",96"method":"GET"97},98{99"href":"https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F/refund",100"rel":"refund",101"method":"POST"102}103]104}]105}106}],107"links":[{108"href":"https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",109"rel":"self",110"method":"GET"111}]112}#### Save approved payment source

If the payment has been authorized or captured, the payer does not need to be
present to save a payment_source . To keep checkout times as short
as possible, the Orders API responds as soon as payment is captured.

If the attributes.vault.status returned after payment is APPROVED , you won't have a vault.id yet. An example
of the attributes object from this scenario is in the following
sample:

1"attributes":{2"vault":{3"status":"APPROVED",4"links":[5{6"href":"https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",7"rel":"up",8"method":"GET"9}10]11}12}

The Payment Method Tokens API still saves the payment source even after the
Orders API returns its response and sends a webhook after the payment source
is saved.

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED [webhook](/api/rest/webhooks/) .

The Payment Method Tokens API sends a webhook after the payment source is
saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook
payload is shown in the following sample:

1{2"id":"WH-72S4353495632143A-68K769747M133873M",3"event_version":"1.0",4"create_time":"2022-08-27T01:25:57.462Z",5"resource_type":"payment_token",6"resource_version":"3.0",7"event_type":"VAULT.PAYMENT-TOKEN.CREATED",8"summary":"A payment token has been created.",9"resource":{10"time_created":"2022-08-26T18:25:57.449PDT",11"links":[12{13"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/7vrxmrw",14"rel":"self",15"method":"GET",16"encType":"application/json"17},18{19"href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/7vrxmrw",20"rel":"delete",21"method":"DELETE",22"encType":"application/json"23}24],25"id":"3nqvjt3n",26"payment_source":{27"paypal":{28"permit_multiple_payment_tokens":false,29"usage_type":"MERCHANT",30"customer_type":"CONSUMER",31"email_address":"email@example.com",32"payer_id":"VTR4JYK7STE7J"33}34},35"customer":{36"id":"208743798"37}38},39"links":[40{41"href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-72S4353495632143A-68K769747M133873M",42"rel":"self",43"method":"GET"44},45{46"href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-72S4353495632143A-68K769747M133873M/resend",47"rel":"resend",48"method":"POST"49}50]51}

In the previous example, the resource.id field is the vault ID.
The resource.customer.id is the PayPal-generated customer ID.

## 6. Test your integration

Run the following tests in the PayPal sandbox to ensure you can save PayPal
Wallets.

### Save payment method

- In your app, initiate a transaction by selecting the PayPal button.
- Log in to the payer account and complete PayPal Web Checkout.
- Capture the transaction.
- Store the PayPal-generated customer ID in your system.
- Log in to [sandbox](https://www.sandbox.paypal.com/) with your
  merchant account and verify the transaction.
- Return to your app and initiate another transaction. Use the
  PayPal-generated payment token as a payment source.
- Verify that the transaction captures successfully without having to complete
  PayPal Web Checkout again.

## Next steps

- [Test and go live](/reference/production/) with this integration.
- Change the credentials and API URLs from api-m.sandbox.paypal.com to api-m.paypal.com when
  going live with your integration.
- You can [create orders](/docs/api/orders/v2/#orders_create) without the payment_source.paypal.attributes.vault for subsequent or
  recurring transactions.
- You can [get a payment token](/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.
