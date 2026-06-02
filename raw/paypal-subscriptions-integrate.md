---
title: Integrate Subscriptions
slug: /docs/subscriptions/integrate/
createTime: "2024-07-10T05:36:26.494Z"
updateTime: "2025-05-09T15:36:10.578Z"
---

# Integrate Subscriptions

Integrate subscriptions to bill customers at regular intervals.

**info**
**Note:** You can also create and manage subscriptions directly in your [PayPal business account](https://www.paypal.com/billing/) .

## Know before you code

- Complete the steps in [Get Started](/api/rest/) to get the following sandbox account information from the Developer Dashboard: - Client ID
- Access token
- Business account credentials
- Personal account credentials

- This client-side and server-side integration uses the following: - [Catalog Products REST API](/docs/api/catalog-products/v1/) : Creates goods or services for customers to subscribe to
- [Subscriptions REST API](/docs/api/subscriptions/v1/) : Creates a recurring payment plan.
- [PayPal JavaScript SDK](/sdk/js/configuration/) : Creates a payment button.

- Use Postman to explore and test PayPal APIs.

To create a product for your subscription plan, copy and modify the following code:

### Sample request

**API endpoint used:** [Create product](/docs/api/catalog-products/v1/#products_create)

#### **`Sample request for create product `**

```curl

curl -v -X POST https://api-m.sandbox.paypal.com/v1/catalogs/products
  -H "Content-Type: application/json"   -H "Authorization: Bearer ACCESS-TOKEN"   -H "PayPal-Request-Id: REQUEST-ID"   -d '{
  "name": "Video Streaming Service",
  "description": "A video streaming service",
  "type": "SERVICE",
  "category": "SOFTWARE",
  "image_url": "https://example.com/streaming.jpg",
  "home_url": "https://example.com/home"
}'

```

### Modify the code

After you copy the code in the sample request, modify the following:

- Change ACCESS-TOKEN to your access token.
- Replace REQUEST-ID with a unique ID that you generate. This ID helps prevent duplicate requests if the API call is disrupted.

- Optional: Change parameters such as the name and description to represent your product.

### Step result

A successful request results in the following:

- The HTTP status code 201 Created .

- A JSON response body that contains an id for the product. Use this ID to complete other actions through the REST API, such as creating a subscription plan.

#### Sample response

#### **`Step result for create product`**

```javascript

{
    "id": "PROD-5FD60555F23244316",
    "name": "Video Streaming Service",
    "description": "A video streaming service",
    "create_time": "2023-01-21T16:04:39Z",
    "links": [
        {
            "href": "https://api-m.sandbox.paypal.com/v1/catalogs/products/PROD-5FD60555F23244316",
            "rel": "self",
            "method": "GET"
        },
        {
            "href": "https://api-m.sandbox.paypal.com/v1/catalogs/products/PROD-5FD60555F23244316",
            "rel": "edit",
            "method": "PATCH"
        }
    ]
}

```

The following sample request is an example of a subscription plan. Modify the code to fit your subscription model.

Review the following topics to help understand how to modify the code for your use case:

- [Customize subscriptions](/docs/subscriptions/customize/)
- [Create plan REST API endpoint](/docs/api/subscriptions/v1/#plans_create)

### Sample request

This sample request creates a subscription plan that:

- Has a 1-month free trial and continues as a 12-month, fixed-price subscription
- Includes a $10 USD setup fee
- Bills any outstanding balance at the next billing cycle
- Allows the subscription to continue if the initial payment for the setup fails
- Suspends the subscription after 3 consecutive payment failures
- Includes a 10% tax in the billing amount

**Important:** Only one currency_code is allowed per subscription plan. Make a new subscription plan to offer a subscription in another currency.

**API endpoint used:** [Create plan](/docs/api/subscriptions/v1/#plans_create)

#### **`Sample request for create subscription`**

```curl

curl -v -k -X POST https://api-m.sandbox.paypal.com/v1/billing/plans   -H "Accept: application/json"   -H "Authorization: Bearer ACCESS-TOKEN"   -H "Content-Type: application/json"   -H "PayPal-Request-Id: REQUEST-ID"   -d '{
      "product_id": "PROD-5FD60555F23244316",
      "name": "Basic Plan",
      "description": "Basic plan",
      "billing_cycles": [
        {
          "frequency": {
            "interval_unit": "MONTH",
            "interval_count": 1
          },
          "tenure_type": "TRIAL",
          "sequence": 1,
          "total_cycles": 1
        },
        {
          "frequency": {
            "interval_unit": "MONTH",
            "interval_count": 1
          },
          "tenure_type": "REGULAR",
          "sequence": 2,
          "total_cycles": 12,
          "pricing_scheme": {
            "fixed_price": {
              "value": "10",
              "currency_code": "USD"
            }
          }
        }
      ],
      "payment_preferences": {
        "auto_bill_outstanding": true,
        "setup_fee": {
          "value": "10",
          "currency_code": "USD"
        },
        "setup_fee_failure_action": "CONTINUE",
        "payment_failure_threshold": 3
      },
      "taxes": {
        "percentage": "10",
        "inclusive": false
      }
    }'

```

### Modify the code

After you copy the code in the sample request, modify the following:

- Change ACCESS-TOKEN to your access token.
- Replace REQUEST-ID with a unique ID that you generate. This ID helps prevent duplicate requests if the API call is disrupted.

- Change the value of the product_id parameter to the ID returned when you created the product.
- (Optional) Change or add parameters in the [Create plan request body](/docs/api/subscriptions/v1/#plans-create-request-body) to create a plan that meets your business needs. Some examples: - Fixed pricing plans
- User or seat-based pricing plans
- Free or discounted trials

### Step result

A successful request results in the following:

- The HTTP status code 201 Created .

- A JSON response body containing an id for the subscription plan. Use the subscription plan ID to complete other actions through the REST API, such as editing or deactivating the plan.
- A subscription plan in the seller's PayPal account in the On status.

#### Sample response

To see how this API call looks in the seller's account, use your sandbox business account credentials to log in to [https://www.sandbox.paypal.com/billing/plans](https://www.sandbox.paypal.com/billing/plans) . The subscription plan reflects the plan number from the REST API call you made.

#### **`The subscription plan reflects the plan number`**

```javascript

{
    "id": "P-17M15335A8501272JLXLLNKI",
    "product_id": "PROD-5FD60555F23244316",
    "name": "Basic Plan",
    "status": "ACTIVE",
    "description": "Basic plan",
    "create_time": "2023-01-21T16:09:13Z",
    "links": [
        {
            "href": "https://api-m.sandbox.paypal.com/v1/billing/plans/P-17M15335A8501272JLXLLNKI",
            "rel": "self",
            "method": "GET"
        },
        {
            "href": "https://api-m.sandbox.paypal.com/v1/billing/plans/P-17M15335A8501272JLXLLNKI",
            "rel": "edit",
            "method": "PATCH"
        },
        {
            "href": "https://api-m.sandbox.paypal.com/v1/billing/plans/P-17M15335A8501272JLXLLNKI/deactivate",
            "rel": "self",
            "method": "POST"
        }
    ]
}

```

To start a subscription from your website, add the PayPal JavaScript SDK code and modify it. This code adds buttons to your website so your buyers can use PayPal or a debit or credit card.

### Add and modify the code

- Copy and paste this code into webpage to create the buttons. When your buyer selects a button, they are directed to PayPal to complete subscription agreement and payment.

#### **`Add and modify the code `**

```html
<!DOCTYPE html>
<head>
   <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- Ensures optimal rendering on mobile devices. -->
</head>
<body>
  <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&vault=true&intent=subscription">
  </script> // Add your client_id
     <div id="paypal-button-container"></div>
      <script>
       paypal.Buttons({
        createSubscription: function(data, actions) {
          return actions.subscription.create({
           'plan_id': 'YOUR_PLAN_ID' // Creates the subscription
           });
         },
         onApprove: function(data, actions) {
           alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
         }
       }).render('#paypal-button-container'); // Renders the PayPal button
      </script>
  </body>
</html>
```

- Modify the code as follows: - Change YOUR_CLIENT_ID to your client ID.
- Change YOUR_PLAN_ID to the plan ID returned from the Create Plan API call.

- Load the webpage to see the payment buttons:

![subscription.png](assets/paypal-subscriptions-button.png)

**info**
**Tip:** To render more than one button on a single webpage, see [Multiple subscribe buttons for your website](/docs/subscriptions/customize/multiple-buttons-website/) .

## Test flow

Test a transaction to see the subscription created in the merchant account:

### Test the transaction as a buyer

- Select the PayPal button on the page.
- Use the sandbox personal login information from the Developer Dashboard to log in and simulate the buyer making a purchase.
- In the Checkout window, make a note of the purchase amount in the upper right corner. USD is the default currency. You can customize the JavaScript SDK by adding a different [currency code](/sdk/js/configuration/#currency) . **Availability:** The JavaScript SDK onShippingChange , onShippingAddressChange , and onShippingOptionsChange functions are not compatible with Subscriptions.

- Select the arrow next to the purchase amount to view the subscription details:

![subscription_details.png](assets/paypal-subscriptions-details.png)

- Select the test credit card as the payment method and select **Continue** .
- Select **Agree & Subscribe** to agree to the terms of the subscription.

### Confirm the movement of funds from the buyer account

- Use the sandbox personal account you used to complete the purchase to log in to [https://www.sandbox.paypal.com/myaccount/autopay/connect/](https://www.sandbox.paypal.com/myaccount/autopay/connect/) .
- Confirm the subscription appears in the active automatic payment list. Select the active automatic payment to see the details of the subscription.
- Log out of the account.

### Confirm the movement of funds to the merchant account

- Use the sandbox business account information from the Developer Dashboard to log in to [https://www.sandbox.paypal.com/billing/subscriptions](https://www.sandbox.paypal.com/billing/subscriptions) .
- Confirm the subscription made by the test buyer appears on the **Subscriptions** tab. Select the subscription to see the details of the subscription.
- Log out of the account.

## Next

- [Customize your subscription integration](/docs/subscriptions/customize)
- [Test and go live](/docs/subscriptions/test-subscriptions/) with your subscription integration.

## See also

- [Catalog Products REST API](/api/catalog-products/v1/) and [Subscriptions REST API](/api/subscriptions/v1) - Use these APIs to add actions to your integration, such as updating the product description, editing the plan or subscription, deactivating the plan or subscription, and more.
- [Subscriptions webhook events](/api/rest/webhooks/event-names/#subscriptions) - Use webhooks to handle tasks triggered by subscription actions.
