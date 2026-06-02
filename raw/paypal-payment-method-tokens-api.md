<!-- Source URL: https://docs.paypal.ai/payments/methods/save-payment-tokens/integrate -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save payment methods directly with the Payment Method Tokens API

No transaction is required when payment methods are saved with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/). You can save payment methods and charge payers after a set amount of time. Payers don't need to be present when charged. Common use cases include offering free trials, subscription billing, and storing payment methods for faster checkout.

The Payment Method Tokens API supports saving credit and debit cards, and PayPal Wallets. When you save a payer's card or wallet, the API provides a setup token associated with the payment method. You'll exchange this setup token for a permanent token from the API.

You can choose to save cards, PayPal, or both.

## Key differences between PayPal and cards integrations

- Saving a card requires no payer interaction.
- Saving a PayPal Wallet requires payers to approve a billing agreement once.
- Calls to save PayPal or cards require different fields in the request body.
- Cards integrations support cards with the following verification methods:
  - no verification
  - smart authorization
  - 3D Secure

## Country availability

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

Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get the following information:

- Your business sandbox account login and password.
- Your app's client ID and client secret. Exchange these for an OAuth access token.

To save credit and debit cards, you'll need:

- A [PayPal Expanded Checkout integration](https://developer.paypal.com/studio/checkout/advanced)
- [SAQ D PCI Compliance](https://listings.pcisecuritystandards.org/documents/SAQ_D_v3_Merchant.pdf)

### Enable your business account

> **Tip:** You can continue to test this integration in the sandbox while waiting for PayPal to approve your eligibility.

1. Go to [paypal.com](https://www.paypal.com) and sign in with your business account.
2. Go to **Account Settings** > **Payment Preferences** > **Save PayPal and Venmo payment methods**.
3. In the Save PayPal and Venmo payment methods section, select **Get Started**.
4. When you submit business profile details, PayPal reviews your eligibility to save PayPal and Venmo accounts.
5. After PayPal reviews your eligibility, you'll see one of the following statuses:

- **Success**
- **Need more information**
- **Denied**

### Enable your developer dashboard

Enable your sandbox and live business accounts to save payment methods:

1. Log in to the Developer Dashboard.
2. Under **Apps & Credentials** > **REST API apps**, select your app name.
3. Scroll down to **Features** and ensure **Vault** is selected.

> **Important:** If you're already using the [Billing Agreements API](https://developer.paypal.com/docs/api/payments.billing-agreements/v1/), contact [PayPal customer support](https://www.paypal.com/us/cshelp/contact-us) to save payment methods with the [Payment Method Tokens API](https://developer.paypal.com/docs/api/payment-tokens/v3/).

## Create setup token for PayPal

Before you create a setup token, a payer must:

- Log in to their PayPal account
- Approve a billing agreement

Make a `POST` call on the `setup-tokens` endpoint to complete the following actions:

- Receive a `PAYER_ACTION_REQUIRED` status
- Create a temporary setup token
- Redirect the payer after they approve or deny the billing agreement

### Get setup token request

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a timestamp.
3. Set the `payment_source` to `paypal`. Complete the rest of the source object for your use case and business.
4. Update the `return_url` value with the URL where the payer is redirected if they approve the flow.
5. Update the `cancel_url` value with the URL where the payer is redirected if they cancel the flow.
6. Optional: For existing customers, pass the `customer.id` to link additional information such as `payment_source` to the customer. For new customers, the customer ID is returned in the setup token response.

Copy and modify the following code sample to create a setup token for PayPal that triggers a flow to approve a billing agreement:

Endpoint: [Create a setup token](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens_create)

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -d '{
        "payment_source": {
          "paypal": {
            "description": "Description for PayPal to be shown to PayPal payer",
            "shipping": {
              "name": {
                "full_name": "Firstname Lastname"
              },
              "address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "Building 17",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US"
              }
            },
            "permit_multiple_payment_tokens": false,
            "usage_pattern": "IMMEDIATE",
            "usage_type": "MERCHANT",
            "customer_type": "CONSUMER",
            "experience_context": {
              "shipping_preference": "SET_PROVIDED_ADDRESS",
              "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
              "brand_name": "EXAMPLE INC",
              "locale": "en-US",
              "return_url": "https://example.com/returnUrl",
              "cancel_url": "https://example.com/cancelUrl"
            }
          }
        },
        "customer": {
          "id": "CUSTOMER-ID-TO-LINK-ADDITIONAL-PAYMENT-SOURCE"
        }
      }'
```

### PayPal setup token response

A successful request returns the following:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request.
- When saving a payer's PayPal Wallet for first time, the response to the `setup-token` request returns the PayPal-generated `customer.id` and the `setup_token_id`.
- A status of `PAYER_ACTION_REQUIRED`.
- The following HATEOAS links:

| Rel       | Method | Description                                                                         |
| --------- | ------ | ----------------------------------------------------------------------------------- |
| `approve` | `GET`  | Take your payer through a PayPal-hosted approval flow.                              |
| `confirm` | `POST` | Use an approved setup token to save the PayPal Wallet and generate a payment token. |
| `self`    | `GET`  | View the state of your setup token and payment method details.                      |

The setup token expires after 3 days. After the payer completes the approval flow, you can [swap the setup token for a payment token](#swap-setup-token-for-payment-token).

## Create setup token for card

The Payment Method Tokens API can create a setup token for cards that have:

- No verification - checks that card data is formatted correctly when passed to the API.
- Smart authorization - runs a zero-value or minimal-value authorization to validate the card is real and active.
- 3D Secure verification - requires two-factor authentication where the cardholder must authenticate before the transaction.

The card verification method depends on the card, issuing bank, and geographic locale.

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
3. Use the card as the payment source and complete the rest of the source object for your use case and business.
4. Pass the `verification_method` parameter with `SCA_WHEN_REQUIRED` for PayPal to automatically trigger the appropriate verification method for the card.
5. Update the `return_url` value with the URL where the payer is redirected after they approve the flow.
6. Update the `cancel_url` value with the URL where the payer is redirected after they cancel the flow.
7. Optional: For existing customers, pass the `customer.id` to link additional information such as `payment_source` to the customer. For new customers, the customer ID is returned in the setup token response.

Copy and modify the following code sample to create a setup token associated with a credit or debit card.

Endpoint: [Create a setup token](https://developer.paypal.com/docs/api/payment-tokens/v3/#setup-tokens_create)

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/setup-tokens' \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -H "Content-Type: application/json" \
  -d '{
        "payment_source": {
          "card": {
            "number": "4111111111111111",
            "expiry": "2027-02",
            "name": "Firstname Lastname",
            "billing_address": {
              "address_line_1": "2211 N First Street",
              "address_line_2": "17.3.160",
              "admin_area_1": "CA",
              "admin_area_2": "San Jose",
              "postal_code": "95131",
              "country_code": "US"
            },
            "verification_method": "SCA_WHEN_REQUIRED",
            "experience_context": {
              "brand_name": "YourBrandName",
              "locale": "en-US",
              "return_url": "https://example.com/returnUrl",
              "cancel_url": "https://example.com/cancelUrl"
            }
          }
        },
        "customer": {
          "id": "CUSTOMER-ID-TO-LINK-ADDITIONAL-PAYMENT-SOURCE"
        }
      }'
```

### Cards setup token response

A successful request returns the following:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request.
- When saving a card for the first time for a payer, the response to the setup token request returns the `customer.id` and the `setup_token_id`.
- A status of `PAYER_ACTION_REQUIRED`.
- The following HATEOAS links:

| Rel       | Method | Description                                                                | Verification methods |
| --------- | ------ | -------------------------------------------------------------------------- | -------------------- |
| `approve` | `GET`  | Take the payer through the card approval flow.                             | 3D secure only       |
| `confirm` | `POST` | Use an approved setup token to save the card and generate a payment token. | All methods          |
| `self`    | `GET`  | View the state of your setup token and payment source data.                | All methods          |

## Swap setup token for payment token

Exchange a temporary setup token for a permanent payment token.

### Swap setup token call

Copy and modify the following code:

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a unique alphanumeric set of characters such as a time stamp.
3. Use `token` as the `payment_source` and complete the rest of the source object for your use case and business.
4. Pass the ID of the setup token you obtained from the previous step in the `payment_source` parameter. Set the type as `SETUP_TOKEN`.

Endpoint: [Create payment token for a given payment source](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_create)

```bash theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -d '{
        "payment_source": {
          "token": {
            "id": "YOUR-SETUP-TOKEN-ID-GOES-HERE",
            "type": "SETUP_TOKEN"
          }
        }
      }'
```

### Swap setup token response

A successful request returns:

- An HTTP response code of `200` or `201`. Returns `200` for an idempotent request
- `id` of the payment token and associated payment method information.
- The following HATEOAS links:

| Rel      | Method   | Description                                  |
| -------- | -------- | -------------------------------------------- |
| `self`   | `GET`    | Retrieve data about the saved payment method |
| `delete` | `DELETE` | Delete the payment token                     |

## Use saved payment token for purchase

After you create a payment method token, use the token instead of the payment method to create a purchase and capture the payment with the Orders API.

You can use the payment method token to create an order on behalf of the payer when the payer isn't present.

You can store a merchant customer ID to help match your customer information across your system and PayPal. This is an optional field that returns the value shared in the response.

### Call the Orders v2 API with saved payment token

Copy and modify the following code:

1. Change `ACCESS-TOKEN` to your sandbox access token.
2. Change `REQUEST-ID` to a set of unique alphanumeric characters such as a time stamp.
3. Set the `payment_source` to `card` or `paypal`.
4. For `vault_id`, enter the ID of the payment method token you received in the previous step.

The following request creates an order with a payment token associated with a card.

Endpoint: [Create order](https://developer.paypal.com/docs/api/orders/v2/#orders_create)

```curl theme={null}
curl -v -k -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
  -H "PayPal-Request-Id: REQUEST-ID" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "intent": "CAPTURE",
        "purchase_units": [
          {
            "amount": {
              "currency_code": "USD",
              "value": "100.00"
            }
          }
        ],
        "payment_source": {
          "card": {
            "vault_id": "ID-FROM-PREVIOUS-STEP"
          }
        }
      }'
```

### Optional: Retrieve saved payment token

If you stored the payment token the payer created on your site, skip this step.

To make a payment on behalf of the payer, retrieve the payment token they created. You'll need the customer ID that you assigned to this payer when saving the payment method.

Copy and modify the following code:

- Change `ACCESS-TOKEN` to your sandbox access token
- Pass the PayPal-generated `customer_id` to retrieve the payment token details associated with the payer.

Endpoint: [Retrieve a payment token](https://developer.paypal.com/docs/api/payment-tokens/v3/#payment-tokens_get)

```bash theme={null}
curl -v -k -X GET 'https://api-m.sandbox.paypal.com/v3/vault/payment-tokens?customer_id=customer_YOUR-CUSTOMER-ID' \
 -H 'Authorization: Bearer ACCESS-TOKEN' \
 -H 'Content-Type: application/json'
```

After you retrieve the `payment_tokens.id`, you can use the payment method token with checkout to create an order.
