<!-- Source URL: https://docs.paypal.ai/payments/methods/save-cards/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save cards with purchase with the JavaScript SDK

After customers save their credit or debit card, they can select it for faster checkout. Customers won't have to enter payment details for future transactions.

Use the JavaScript SDK to save a payer's card if you aren't <a href="https://www.pcisecuritystandards.org/pci_security/completing_self_assessment">PCI Compliant - SAQ A</a> but want to save credit or debit cards during checkout.

## Availability

<Accordion title="Supported countries">
  * Australia
  * Austria
  * Belgium
  * Bulgaria
  * Canada
  * China
  * Cyprus
  * Czech Republic
  * Denmark
  * Estonia
  * Finland
  * France
  * Germany
  * Hong Kong
  * Hungary
  * Ireland
  * Italy
  * Japan
  * Latvia
  * Liechtenstein
  * Lithuania
  * Luxembourg
  * Malta
  * Netherlands
  * Norway
  * Poland
  * Portugal
  * Romania
  * Singapore
  * Slovakia
  * Slovenia
  * Spain
  * Sweden
  * United Kingdom
  * United States
</Accordion>

## Prerequisites

- This integration requires a PayPal Developer account.
- You'll need to have an existing [credit and debit card payments integration](https://developer.paypal.com/docs/checkout/advanced/). PayPal must approve your account to process advanced credit and debit card payments.
- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get the following sandbox account information from the Developer Dashboard:
  - The sandbox client ID and secret of your REST app.
  - An access token to use the PayPal REST API server.
- This client-side and server-side integration uses the following:
  - [PayPal JavaScript SDK](https://docs/paypal.ai/reference/sdk-v6-reference)
  - [Orders REST API](https://developer.paypal.com/docs/api/orders/v2/)

## How it works

PayPal encrypts payment method information and stores it in a digital vault for that customer.

1. The payer saves their payment method.
2. For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
3. When the customer returns to your website and is ready to check out, pass their PayPal-generated customer ID to the JavaScript SDK. The customer ID tells the JavaScript SDK to save or reuse a saved payment method.
4. The payer completes a billing agreement.
5. The JavaScript SDK populates the checkout page with each saved payment method. Each payment method appears as a one-click button next to other ways to pay.

The checkout process is now shorter because it uses saved payment information.

## Use cases

Businesses save payment methods if they want customers to:

- Check out without re-entering a payment method
- Pay after use, for example, ride-sharing and food delivery

You can charge now and save the card in a single flow. Keep your one-time payment session on the client and add a vault directive on your server when creating the order.

## 1. Set up sandbox to save payment methods

Set up your sandbox and live business accounts to save payment methods:

1. Log in to the Developer Dashboard.
2. Under **REST API apps**, select your app name.
3. Under **Sandbox App Settings** > **App Feature Options**, check **Accept payments**.
4. Expand **Advanced options**. Confirm that **Vault** is selected.

## 2. Add checkbox for payers to save card

Add a `checkbox` element grouped with your card collection fields to give payers the option to save their card.

```html theme={null}
  <input type="checkbox" id="save" name="save">
  <label for="save">Save your card</label>
</div>
```

## 3. Pass checkbox value

Pass `document.getElementById("save").checked` to your server with the following details in the `createOrder()` method:

- Value of the checkbox
- Optional: Card name
- Optional: Billing address

<Tabs>
  <Tab title="No verification">
    ```javascript theme={null}
    // Initialize the v6 SDK with card-fields component
    const sdk = await window.paypal.createInstance({ 
      clientId: "YOUR_CLIENT_ID",
      components: ["card-fields"] 
    });

    // Create a one-time payment session using v6 SDK
    const session = sdk.createCardFieldsOneTimePaymentSession();

    // Check eligibility and render card fields
    if (session.isEligible()) {
      session.NameField().render("#card-name-field-container");
      session.NumberField().render("#card-number-field-container");
      session.ExpiryField().render("#card-expiry-field-container");
      session.CVVField().render("#card-cvv-field-container");
    } else {
      // Handle the workflow when credit and debit cards are not available
    }

    // Submit button event handler
    const submitButton = document.getElementById("submit-button");
    submitButton.addEventListener("click", async () => {
      try {
        // Create order - server determines verification settings
        const saveCheckbox = document.getElementById("save");

        const orderResponse = await fetch("/api/paypal/order/create/", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            saveCard: saveCheckbox.checked,
          }),
        });

        const orderData = await orderResponse.json();
        const orderId = orderData.id;

        // Submit the session with billing address
        const { state, data } = await session.submit(orderId, {
          billingAddress: {
            postalCode: "95131"
          },
        });

        // Handle successful transaction
        if (state === "succeeded") {
          // Capture the order
          const captureResponse = await fetch(`/api/paypal/orders/${data.orderId}/capture/`, {
            method: "POST"
          });

          const captureData = await captureResponse.json();

          // Handle vault details if card was saved
          const vault = captureData?.paymentSource?.card?.attributes?.vault;
          if (vault) {
            // Save the vault.id and vault.customer.id for future use
            console.log('Vault ID:', vault.id);
            console.log('Customer ID:', vault.customer.id);
          }

          // Handle successful transaction completion
          console.log('Payment completed successfully');
        }

      } catch (error) {
        // Handle any error that may occur
        console.error('Payment error:', error);
      }
    });
    ```

  </Tab>

  <Tab title="3D Secure">
    To trigger the authentication, pass the required contingency with the verification method in the create orders payload. The verification method can be contingencies parameter with `SCA_ALWAYS` or `SCA_WHEN_REQUIRED`.

    `SCA_ALWAYS` triggers an authentication for every transaction, while `SCA_WHEN_REQUIRED` triggers an authentication only when a regional compliance mandate such as PSD2 is required. 3D Secure is supported only in countries with a <a href="https://www.paypal.com/uk/webapps/mpp/PSD2?_ga=1.51925228.43968804.1640649786PSD2">PSD2 compliance mandate</a>.

    ```javascript theme={null}
    // Initialize the v6 SDK with card-fields component
    const sdk = await window.paypal.createInstance({
      clientId: "YOUR_CLIENT_ID",
      components: ["card-fields"]
    });

    // Create a one-time payment session using v6 SDK
    const session = sdk.createCardFieldsOneTimePaymentSession();

    // Check eligibility and render card fields
    if (session.isEligible()) {
      session.NameField().render("#card-name-field-container");
      session.NumberField().render("#card-number-field-container");
      session.ExpiryField().render("#card-expiry-field-container");
      session.CVVField().render("#card-cvv-field-container");
    } else {
      // Handle the workflow when credit and debit cards are not available
    }

    // Submit button event handler
    const submitButton = document.getElementById("submit-button");
    submitButton.addEventListener("click", async () => {
      try {
        // Create order with 3DS verification directly in client payload
        const saveCheckbox = document.getElementById("save");

        const orderResponse = await fetch("/api/paypal/order/create/", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            saveCard: saveCheckbox.checked,
            // Direct 3DS configuration in client payload
            card: {
              attributes: {
                verification: {
                  method: "SCA_ALWAYS" // or "SCA_WHEN_REQUIRED"
                },
              },
              experience_context: {
                shipping_preference: "NO_SHIPPING",
                return_url: "https://example.com/returnUrl",
                cancel_url: "https://example.com/cancelUrl",
              },
            }
          }),
        });

        const orderData = await orderResponse.json();
        const orderId = orderData.id;

        // Submit the session with billing address
        const { state, data } = await session.submit(orderId, {
          billingAddress: {
            postalCode: "95131"
          },
        });

        // Handle successful transaction
        if (state === "succeeded") {
          // Capture the order
          const captureResponse = await fetch(`/api/paypal/orders/${data.orderId}/capture/`, {
            method: "POST"
          });

          const captureData = await captureResponse.json();

          // Handle vault details if card was saved
          const vault = captureData?.paymentSource?.card?.attributes?.vault;
          if (vault) {
            // Save the vault.id and vault.customer.id for future use
            console.log('Vault ID:', vault.id);
            console.log('Customer ID:', vault.customer.id);
          }

          // Handle successful transaction completion
          console.log('Payment completed successfully');
        }

      } catch (error) {
        // Handle any error that may occur
        console.error('Payment error:', error);
      }
    });
    ```

  </Tab>
</Tabs>

## 4. Create order and save card

### Server side

Set up your server to call the Orders API. The button that the payer selects determines the `payment_source` sent in the following sample.

This SDK uses the Orders v2 API to save payment methods in the background. Use the following request using the Orders API to add attributes needed to save a card.

<Tabs>
  <Tab title="First-time payer">
    #### Save payment method for first-time payers

    This request is for payers who:

    * Don't have a payment source saved into the vault.
    * Selected the save checkbox. The `document.getElementById("save").checked` value is `true`.

    To run 3D Secure on the card, set the  `payment_source.card.attributes.verification.method` to `SCA_ALWAYS` or `SCA_WHEN_REQUIRED`.

    `SCA_ALWAYS` triggers an authentication for every transaction, while `SCA_WHEN_REQUIRED` triggers an authentication only when a regional compliance mandate such as PSD2 is required. 3D Secure is supported only in countries with a <a href="https://www.paypal.com/uk/webapps/mpp/PSD2?_ga=1.51925228.43968804.1640649786PSD2">PSD2 compliance mandate</a>.

    > **Note:** In the following requests, the `payment_source.attributes.vault.store_in_vault` with the value `ON_SUCCESS` means the card is saved with a successful authorization or capture.

    ```bash theme={null}
    curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders
    -H "Content-Type: application/json"
    -H "Authorization: Bearer 'ACCESS-TOKEN'"
    -d '{
      "intent": "CAPTURE",
      "purchase_units": [{
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }],
      "payment_source": {
        "card": {
          "name": "Firstname Lastname",
          "billing_address": {
            "address_line_1": "123 Main St.",
            "address_line_2": "Unit B",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
          },
            "attributes": {
            "customer" : {
                "id": "'PayPal-generated customer id'"
            },
            "vault": {
              "store_in_vault": "ON_SUCCESS"
            },
          }
        }
      }
    }
    ```

  </Tab>

  <Tab title="Returning payer">
    #### Save payment method for returning payers

    This request is for payers who:

    * Already have a payment method saved in the vault.
    * Want to save another payment method to the vault.
    * Selected the save checkbox. The `document.getElementById("save").checked` value is `true`.

    Pass the PayPal-generated `customer.id` as part of this request. Link additional `payment_sources` to this customer through their `customer.id`. The `customer.id` is returned in the response from an `authorize` or `capture` request.

    ```bash theme={null}
    curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders
    -H "Content-Type: application/json"
    -H "Authorization: Bearer 'ACCESS-TOKEN'"
    -d '{
          "intent": "CAPTURE",
          "purchase_units": [{
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "amount": {
              "currency_code": "USD",
              "value": "100.00"
            }
          }],
          "payment_source": {
            "card": {
              "name": "Firstname Lastname",
              "billing_address": {
                "address_line_1": "123 Main St.",
                "address_line_2": "Unit B",
                "admin_area_2": "Anytown",
                "admin_area_1": "CA",
                "postal_code": "12345",
                "country_code": "US"
              },
              "attributes": {
                "customer" : {
                    "id": "'PayPal-generated customer id'"
                },
                "vault": {
                  "store_in_vault": "ON_SUCCESS"
                },
              }
            }
          }
        }
    ```

  </Tab>
</Tabs>

#### Response

Pass the order `id` to the JavaScript SDK. The SDK updates the order with the new card details. PayPal handles any PCI compliance issues.

After the SDK is updated, it triggers the `onApprove()` method, which receives an object containing the `orderID`. You can authorize or capture the order when you have the `orderID`.

> **Note:** The request to save the payment method is made when the order is created through `payment_source.attributes.vault.store_in_vault`. Vault details are available only after an order is authorized or captured.

```json theme={null}
{
  "id": "5O190127TN364715T",
  "status": "CREATED",
  "intent": "CAPTURE",
  "payment_source": {
    "card": {
      "brand": "VISA",
      "last-digits": "1881",
      "billing_address": {
        "address_line_1": "123 Main St.",
        "address_line_2": "Unit B",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    }
  },
  "purchase_units": [
    {
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      }
    }
  ],
  "create_time": "2021-10-28T21:18:49Z",
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=5O190127TN364715T",
      "rel": "approve",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "update",
      "method": "PATCH"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture",
      "rel": "capture",
      "method": "POST"
    }
  ]
}
```

## 5. Authorize or capture order and save card

### Server side

Set up your server to call the <a href="/reference/api/rest/orders/create-order" target="_blank" rel="noopener noreferrer">Orders v2 API</a>:

- Call the [authorize order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) if the `intent` passed was `AUTHORIZE`.
- Call the [capture order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) if the `intent` passed was `CAPTURE`.

### Request

Add a `payment_source.card` instruction for vault. Use your desired amounts, URLs, and business policy.

```bash theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/YOUR-ORDER-ID/{authorize or capture}
-H "Content-Type: application/json"
-H "Authorization: Bearer 'YOUR-ACCESS-TOKEN'"
-d
'{
  "intent": "CAPTURE",
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "100.00" }
  }],
  "payment_source": {
    "card": {
      // 3DS (optional): see 3DS guide for attributes.verification + experience_context
      "attributes": {
        // "verification": { "method": "SCA_WHEN_REQUIRED" },
        "vault": {
          "store_in_vault": "ON_SUCCESS" // or "ALWAYS" per your business policy
        }
      }
    }
  }'
```

### Response

```json theme={null}
  {
    "id": "5O190127TN364715T",
    "status": "COMPLETED",
    "payment_source": {
      "card": {
        "brand": "VISA",
        "last_digits": "4949"
        "attributes": {
          "vault": {
            "id": "nkq2y9g",
            "customer": {
                "id": "695922590"
            },
            "status": "VAULTED",
            "links": [{
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/nkq2y9g",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/nkq2y9g",
                "rel": "delete",
                "method": "DELETE"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              }
            ]
          }
        }
      }
    },
    "purchase_units": [{
      "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
      "payments": {
        "captures": [{
          "id": "3C679366HH908993F",
          "status": "COMPLETED",
          "amount": {
            "currency_code": "USD",
            "value": "100.00"
          },
          "seller_protection": {
            "status": "NOT_ELIGIBLE"
          },
          "final_capture": true,
          "seller_receivable_breakdown": {
            "gross_amount": {
              "currency_code": "USD",
              "value": "100.00"
            },
            "paypal_fee": {
              "currency_code": "USD",
              "value": "3.00"
            },
            "net_amount": {
              "currency_code": "USD",
              "value": "97.00"
            }
          },
          "create_time": "2022-01-01T21:20:49Z",
          "update_time": "2022-01-01T21:20:49Z",
          "processor_response": {
              "avs_code": "Y",
              "cvv_code": "M",
              "response_code": "0000"
          },
          "links": [{
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F",
              "rel": "self",
              "method": "GET"
            },
            {
              "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/3C679366HH908993F/refund",
              "rel": "refund",
              "method": "POST"
            }
          ]
        }]
      }
    }],
    "links": [{
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }]
}
```

In the response from the Authorize or Capture request, the Orders v2 API interacts with the Payment Method Tokens v3 API to save the card.

The `payment_source.card.attributes.vault` stores the card information as the `vault.id`, which can be used for future payments when the `vault.status` is `VAULTED`.

#### Save approved payment source

If the payment has been authorized or captured, the payer doesn't need to be present to save a `payment_source`. To keep checkout times as short as possible, the Orders API responds as soon as payment is captured.

If the `attributes.vault.status` returned after payment is `APPROVED`, you won't have a `vault.id` yet. An example of the `attributes` object from this scenario is in the following sample:

```json theme={null}
  "attributes": {
    "vault": {
      "status": "APPROVED",
      "links": [
        {
          "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T",
          "rel": "up",
          "method": "GET"
        }
      ]
    }
  }
```

The Payment Method Tokens API still saves the payment source even after the Orders API returns its response and sends a webhook after the payment source is saved.

In order to retrieve a `vault_id` when an `APPROVED` status is returned, you'll need to subscribe to the `VAULT.PAYMENT-TOKEN.CREATED` [webhook](https://developer.paypal.com/api/rest/webhooks/).

The Payment Method Tokens API sends a webhook after the payment source is saved. An example of the `VAULT.PAYMENT-TOKEN.CREATED` webhook payload is shown in the following sample:

```json theme={null}
{
  "id": "WH-1KN88282901968003-82E75604WM969463F",
  "event_version": "1.0",
  "create_time": "2022-08-15T14:13:48.978Z",
  "resource_type": "payment_token",
  "resource_version": "3.0",
  "event_type": "VAULT.PAYMENT-TOKEN.CREATED",
  "summary": "A payment token has been created.",
  "resource": {
    "time_created": "2022-08-15T07:13:48.964PDT",
    "links": [
      {
        "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
        "rel": "self",
        "method": "GET",
        "encType": "application/json"
      },
      {
        "href": "https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
        "rel": "delete",
        "method": "DELETE",
        "encType": "application/json"
      }
    ],
    "id": "nkq2y9g",
    "payment_source": {
      "card": {
        "last_digits": "1111",
        "brand": "VISA",
        "expiry": "2027-02",
        "billing_address": {
          "address_line_1": "123 Main St.",
          "address_line_2": "Unit B",
          "admin_area_2": "Anytown",
          "admin_area_1": "CA",
          "postal_code": "12345",
          "country_code": "US"
        }
      }
    },
    "customer": {
      "id": "695922590"
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F/resend",
      "rel": "resend",
      "method": "POST"
    }
  ]
}
```

In this example, the `resource.id` field is the vault ID, and `resource.customer.id` is the PayPal-generated customer ID.

You can now style your card fields and test a purchase.

#### Payment processor codes

Payment processors return the following codes when they receive a transaction request. For advanced card payments, the code displays in the authorization object under the `response_code` field.

The following sample shows the processor response codes returned in an authorization (`avs_code`) and capture call (`cvv_code`) response:

```json theme={null}
  "processor_response": {
    "avs_code": "Y",
    "cvv_code": "S",
    "response_code": "0000"
  }
```

See the Orders API `response_code` object to get the [processor response code for the non-PayPal payment processor errors](https://developer.paypal.com/docs/api/orders/v2/#definition-processor_response).

## 6. Pay with saved payment methods

When a payer returns to your site, you can show the payer's saved payment methods with the Payment Method Tokens API.

### List all saved payment methods

Make the server-side [list all payment tokens API call](https://developer.paypal.com/docs/api/payment-tokens/v3/#customer_payment-tokens_get) to retrieve payment methods saved to a payer's PayPal-generated customer ID. Based on this list, you can show all saved payment methods to a payer to select during checkout.

### Show saved card to payer

Display the saved card to the payer and use the Orders API to make another transaction. Use the vault ID the payer selects as an input to the Orders API.

Use [supported CSS properties](https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/) to style the card fields.

## 7. Test your integration

Test your vault integration in the PayPal sandbox.

1. Copy the sample request code.
2. Change `'ACCESS_TOKEN'` to your
   access token.

### Save payment method

1. On the checkout page, enter the card information and select the option to save the card. You can use [test card numbers](#test-cards) for testing.
2. Capture the transaction.
3. Log in to [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.

### Pay with a saved payment method

1. Use the [list all payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) API to retrieve all the payment methods saved for the payer.
2. Capture the payment by passing the payer-selected vault ID to the Orders API.
3. Log in to the [sandbox](https://www.sandbox.paypal.com/) with your merchant account and verify the transaction.

## 8. Integrate front end

The following sample shows how a full script to save cards might appear in HTML:

```html theme={null}
<head>
  <!-- Add meta tags for mobile and IE -->
  <meta charset="utf-8" />
</head>
<body>
  <script src="https://www.paypal.com/sdk/js?components=card-fields&client-id=YOUR-CLIENT-ID&currency=USD&intent=capture&merchant-id=YOUR-MERCHANT-ID"></script>
  <div align="center"> or </div>
  <!-- Advanced credit and debit card payments form -->
  <div class='card_container'>
    <div id='card-number'></div>
    <div id='expiration-date'></div>
    <div id='cvv'></div>
    <div id='card-holder-name'></div>
    <label>
<input type='checkbox' id='vault' name='vault' /> Vault
    </label>
    <br /><br />
    <button value='submit' id='submit' class='btn'>Pay</button>
  </div>
  <!-- Implementation -->
  <script>
    // Create the card fields component and define callbacks
    const cardFields = paypal.CardFields({
createOrder: async (data) => {
  const result = await fetch("https://api-m.sandbox.paypal.com/v2/checkout/orders", {
    method: "POST",
    body: JSON.stringify({
intent: "CAPTURE",
purchase_units: [{
  amount: {
    currency_code: "USD",
    value: "100.00"
  }
}],
payment_source: {
  card: {
    attributes: {
verification: {
  method: "SCA_ALWAYS"
},
vault: {
  store_in_vault: "ON_SUCCESS",
  usage_type: "PLATFORM",
  customer_type: "CONSUMER",
  permit_multiple_payment_tokens: true,
},
    }
  },
  experience_context: {
    shipping_preference: "NO_SHIPPING",
    return_url: "https://example.com/returnUrl",
    cancel_url: "https://example.com/cancelUrl",
  },
},
    }),
    headers: {
"Content-Type": "application/json",
"Authorization": "Bearer ACCESS_TOKEN",
"PayPal-Request-Id": "UNIQUE_ALPHANUMERIC_KEY"
    },
  })
  const {
    id
  } = await result.json();
  return id;
},
onApprove: async (data) => {
  const {
    orderID
  } = data;
  return fetch('https://api-m.sandbox.paypal.com/v2/checkout/orders/\${orderID}/capture/', {
    method: "POST",
    body: JSON.stringify({
payment_source: {
  attributes: {
    vault: {
store_in_vault: "ON_SUCCESS",
usage_type: "PLATFORM",
customer_type: "CONSUMER",
permit_multiple_payment_tokens: true,
    },
  },
  experience_context: {
    shipping_preference: "NO_SHIPPING",
    return_url: "https://example.com/returnUrl",
    cancel_url: "https://example.com/cancelUrl",
  },
},
    }),
    headers: {
"Content-Type": "application/json",
"Authorization": "Bearer ACCESS_TOKEN",
"PayPal-Request-Id": "UNIQUE_ALPHANUMERIC_KEY"
    },
  })
  // Retrieve vault details from the response and
  // save vault.id and customer.id for the buyer's return experience
  return await res.json();
},
onError: (error) => console.error('Something went wrong:', error)
    });
    // Render each field after checking for eligibility
    // Check eligibility and display advanced credit and debit card payments
    if (cardFields.isEligible()) {
cardFields.NameField().render("#card-holder-name");
cardFields.NumberField().render("#card-number");
cardFields.ExpiryField().render("#expiration-date");
cardFields.CVVField().render("#cvv");
    } else {
// Handle workflow when credit and debit cards are not available
    }
    const submitButton = document.getElementById("submit");
    submitButton.addEventListener("click", () => {
cardFields
  .submit()
  .then(() => {
    console.log("submit was successful");
  })
  .catch((error) => {
    console.error("submit erred:", error);
  });
    });
  </script>
  </html>
```

## Testing

Use the following card numbers to test transactions in the sandbox:

| Test number        | Card type        |
| ------------------ | ---------------- |
| `371449635398431`  | American Express |
| `376680816376961`  | American Express |
| `36259600000004`   | Diners Club      |
| `6304000000000000` | Maestro          |
| `5063516945005047` | Maestro          |
| `2223000048400011` | Mastercard       |
| `4005519200000004` | Visa             |
| `4012000033330026` | Visa             |
| `4012000077777777` | Visa             |
| `4012888888881881` | Visa             |
| `4217651111111119` | Visa             |
| `4500600000000061` | Visa             |
| `4772129056533503` | Visa             |
| `4915805038587737` | Visa             |

Test the following scenarios:

- Transaction succeeds and card is saved to the vault. Verify in the merchant dashboard.
- Transaction fails and the instrument is not saved with `ON_SUCCESS`.
- 3DS success, cancellations, and failures behave as expected

## Troubleshooting

- Make sure you've placed the vault directive under `payment_source.card.attributes` during order creation.
- Verify currency and amount consistency between session context and server payloads.
- Add missing `break;` statements in client `switch` handling of `state`.

## Next steps

- [Go live](https://developer.paypal.com/api/rest/production/) with this integration.
  - Complete [production onboarding](https://www.paypal.com/bizsignup/entry/product/ppcp) to be eligible to process cards with your live PayPal account.
  - Be sure to swap the credentials and API URL from sandbox to production when going live with your integration.
- Follow [Use payment method token with checkout](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/cards/#link-usesavedpaymenttoken) for subsequent or recurring transactions.
- You can [get a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_get), [list all payment tokens](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens), [delete a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_delete), and more with the Payment Method Tokens API.
- Keep saved cards up-to-date with the [real-time account updater](https://developer.paypal.com/docs/checkout/advanced/customize/rtau/).
