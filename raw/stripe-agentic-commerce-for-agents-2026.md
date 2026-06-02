<!-- Source URL: https://docs.stripe.com/agentic-commerce/for-agents -->
<!-- Fetched: 2026-05-12 -->

# Embed commerce into your AI interface

Browse products, collect payment information, and complete purchases on behalf of sellers.

> Agentic Commerce Suite is available in the US. It supports purchases of physical goods.

Use Agentic Commerce Suite (ACS) to embed commerce capabilities into your AI interface. ACS works across multiple commerce protocols, so your AI interface can discover products, collect payment information, and complete purchases on behalf of sellers. Use the embedded integration for an end-to-end agentic commerce flow.

# Embedded

> This is a Embedded for when agent-checkout-mode is full. View the full page at https://docs.stripe.com/agentic-commerce/for-agents?agent-checkout-mode=full.

Use the embedded integration to manage the full checkout lifecycle through Stripe, including product feed ingestion, cart management, fulfillment, and payment collection. Stripe handles routing, authentication, error retries, and shared payment token (SPT) creation so you don’t need to integrate directly with each seller.

Agents that enable both product discovery and purchase capabilities directly within their interface might be considered marketplace facilitators (MPFs) with tax collection and remittance obligations-consult a tax advisor to understand if this applies to you.
Checkout lifecycle (See full diagram at https://docs.stripe.com/agentic-commerce/for-agents)

## Get started

### Set up your Stripe account

[Create a Stripe account](https://stripe.com/register) if you don’t already have one. After you verify your email, activate payments by providing business and personal information, linking a bank account for payouts, and setting up two-step authentication.

### Begin agent configuration

Go to the [Agentic commerce](https://dashboard.stripe.com/agentic-commerce) page and select **Onboard as an agent** to configure your account as an agent. If you don’t already have a [Stripe profile](https://docs.stripe.com/get-started/account/profile.md), Stripe prompts you to create one.

### (Optional) Upload terms of service and privacy policy

You can require sellers to accept your terms of service and privacy policy before they proceed. During onboarding, upload a link for each document. Stripe shows these links to sellers when they initiate an agreement. This step is optional.

### Configure product feed acceptance

Set up SSH File Transfer Protocol (SFTP) to ingest seller product feeds from Stripe. You must provide the host name, port, and user name. Stripe generates a public and private key pair that you add to the server’s authorized keys. The public key is available as you complete agent onboarding in the Stripe Dashboard. Stripe rotates the public and private keys every 365 days and notifies the agent when it’s time to rotate.

During onboarding, Stripe also presents you with a unique challenge token. You must upload this token to your SFTP host in a file called `stripe-verification.txt`. Once Stripe verifies the presence of this file with the expected token, Stripe begins uploading product catalogs for your sellers to your SFTP server.

### Complete verification

After you complete all onboarding steps, your account might enter a pending state while Stripe completes final verification checks. Stripe might ask you to complete additional identity verification, which you can access in your [Account settings](https://dashboard.stripe.com/settings/account). Stripe sends you an email when your agent configuration becomes active.

## Manage seller relationships

### Set up an orchestrated commerce agreement

After you complete agent onboarding, all Agentic Commerce Suite (ACS) sellers can discover your account name and business profile in the Dashboard.

Before you can connect with a seller, you need an orchestrated commerce agreement (OCA). An OCA is a required connection between your agent and a seller that enables agentic commerce flows. Only a seller can initiate an OCA request.

After a seller requests an OCA, the seller appears on the Agentic commerce page in the Dashboard. You can approve or reject the OCA for that seller.

### Terminate an orchestrated commerce agreement

Either party can terminate an OCA at any time. After termination, only the party that terminated the OCA can request a new one. You can terminate an OCA on the Agentic commerce page in the Dashboard.

### Manage an OCA with webhooks

Configure your agent to listen for [v2 webhooks](https://docs.stripe.com/api/v2/core/event_destinations.md). Set up an event destination to receive these events:

- `v2.orchestrated_commerce.agreement.created`
- `v2.orchestrated_commerce.agreement.partially_confirmed`
- `v2.orchestrated_commerce.agreement.confirmed`
- `v2.orchestrated_commerce.agreement.terminated`

#### Establish an OCA

After a seller enables your agent in the Stripe Dashboard, Stripe sends two webhooks to your agent: `v2.orchestrated_commerce.agreement.created` and `v2.orchestrated_commerce.agreement.partially_confirmed`.

When you receive the `partially_confirmed` webhook, retrieve the OCA to verify the seller’s identity, then confirm your side of the OCA:

```json
// Webhook payload
{
  "id": "evt_123",
  "object": "v2.core.event",
  "type": "v2.orchestrated_commerce.agreement.partially_confirmed",
  "related_object": {
    "id": "orca_123",
    "type": "v2.orchestrated_commerce.agreement",
    "url": "/v2/orchestrated_commerce/agreements/orca_123"
  }
}
```

Retrieve the OCA to verify the seller:

```curl
curl https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

You can also retrieve the seller’s Stripe profile for additional details, such as display name and branding.

```curl
curl https://api.stripe.com/v2/network/profiles/{{SELLER_PROFILE_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Confirm the OCA:

```curl
curl -X POST https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}}/confirm \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Stripe sends a `v2.orchestrated_commerce.agreement.confirmed` webhook to the seller. After both parties confirm the OCA, it authorizes data access between your agent and the seller.

#### Terminate an OCA

Either party can terminate an OCA at any time:

```curl
curl -X POST https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}}/terminate \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Termination sends a `v2.orchestrated_commerce.agreement.terminated` webhook to the other party and revokes the OCA. After termination, only the party that terminated the OCA can initiate a new one.

## Ingest product feeds

Seller product feeds are sent to the SFTP server you set up during onboarding. For details on the SFTP directory layout, feed schemas, and manifest handling, see [SFTP catalog ingestion](https://docs.stripe.com/agentic-commerce/product-feed/sftp-catalog-ingestion.md).

### Disable checkout

Each product in the feed includes a `disable_checkout` field that indicates whether the product supports checkout:

- `false`: The product is available for checkout. You can create a `RequestedSession` to complete the purchase through Stripe.
- `true`: The product is for discovery only. Don’t include it in checkout flows. Instead, redirect your customer to the seller’s site to complete the purchase.

## Manage checkout flows

After you establish a valid OCA with the seller, use the Delegated Checkout API to:

- Route requests to the correct seller automatically by using Stripe profiles.
- Manage the checkout lifecycle with the `RequestedSession` object.
- Handle seller errors with Stripe-defined error codes and messages.
- Create and send shared payment tokens (SPTs) automatically.

### Create a requested session

After a customer selects items through your agent, create a `RequestedSession` with the seller’s Stripe profile and the products the customer wants to purchase:

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d "seller_details[network_profile]=profile_123" \
  -d currency=usd \
  -d "line_item_details[0][sku_id]={{PRODUCT_SKU}}" \
  -d "line_item_details[0][quantity]=1"
```

### Update requested session details

Update a `RequestedSession` as the customer provides more information during checkout.

#### Update quantity

When a customer changes an item quantity in your agent interface, update the `quantity` in `line_item_details`:

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d "line_item_details[0][key]={{LINE_ITEM_KEY}}" \
  -d "line_item_details[0][quantity]=2"
```

#### Add fulfillment information

When the customer provides a fulfillment address, update the `address` in `fulfillment_details` to receive a list of fulfillment options that the seller supports:

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d "fulfillment_details[name]=Jenny Rosen" \
  --data-urlencode "fulfillment_details[email]=jenny@example.com" \
  -d "fulfillment_details[phone]=5555551234" \
  -d "fulfillment_details[address][line1]=123 Main St" \
  -d "fulfillment_details[address][city]=San Francisco" \
  -d "fulfillment_details[address][state]=CA" \
  -d "fulfillment_details[address][postal_code]=94111" \
  -d "fulfillment_details[address][country]=US"
```

#### Select a fulfillment option

After you render the available fulfillment options in your agent interface and the customer selects one, update the `selected_fulfillment_option` in `fulfillment_details`:

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d "fulfillment_details[selected_fulfillment_option][type]=shipping" \
  -d "fulfillment_details[selected_fulfillment_option][shipping][shipping_option]={{SHIPPING_OPTION_KEY}}"
```

### Collect a payment method

Collect the customer’s payment method before you confirm the `RequestedSession`. Use Stripe Elements to securely collect payment details on web, or the [mobile SDK](https://docs.stripe.com/agentic-commerce/for-agents.md#mobile-integration) for native apps.

### Collect payment method with Elements

Use Stripe Elements to collect payment information and complete the checkout flow. You can use either integration independently or combine both to offer customers multiple payment options.

#### Supported payment methods

The Delegated Checkout API supports the following payment methods:

| Payment method                                                 | Availability    |
| -------------------------------------------------------------- | --------------- |
| [Cards](https://docs.stripe.com/payments/cards/overview.md)    | ✓ Supported 1   |
| [Link](https://docs.stripe.com/payments/wallets/link.md)       | ✓ Supported     |
| [Apple Pay](https://docs.stripe.com/apple-pay.md)              | ✓ Supported     |
| [Google Pay](https://docs.stripe.com/google-pay.md)            | ✓ Supported     |
| [Klarna](https://docs.stripe.com/payments/klarna.md)           | ✓ Supported     |
| [Affirm](https://docs.stripe.com/payments/affirm.md) (limited) | ✓ Supported 2,3 |

1 In collaboration with the card networks, Stripe might use tokens issued through network programs such as Mastercard’s Agent Pay and Visa’s Intelligent Commerce programs on your behalf. Stripe submits the requested data to the card networks to provision and process those tokens for related transactions. 2 An agent might not programmatically interact with the Affirm loan application UI inside the webview; the buyer must be the one navigating and confirming. It also might not render the Affirm checkout in a browser on the device over which the agent doesn’t have navigation control. 3 If an agent markets Affirm to customers, the agent must comply with Affirm’s [marketing compliance guides](https://docs.affirm.com/developers/docs/compliance_and_guidelines) and use the Affirm [guide](https://businesshub.affirm.com/hc/en-us/articles/10653174159636-Affirm-Marketing-Compliance-Guides) that relates to the Affirm payment options you display to your customers.

#### Express Checkout Element

Use the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md) to collect payment and shipping details through one-click payment buttons such as Apple Pay, Google Pay, and Link.

#### Create the Express Checkout Element

The Delegated Checkout API requires complete customer details. You can collect them through the Express Checkout Element, or collect some details separately in your own UI:

#### HTML + JS

```javascript
const expressCheckoutElement = elements.create("expressCheckout", {
  emailRequired: true,
  phoneNumberRequired: true,
  billingAddressRequired: true,
  shippingAddressRequired: true,
});

expressCheckoutElement.mount("#express-checkout-element");
```

#### React

```jsx
import { ExpressCheckoutElement } from "@stripe/react-stripe-js";

const options = {
  emailRequired: true,
  phoneNumberRequired: true,
  billingAddressRequired: true,
  shippingAddressRequired: true,
};
```

#### Handle shipping address changes

When the customer selects a shipping address, the `shippingaddresschange` event provides a partial address (city, state, postal code, country) without the street address. These details are sufficient to calculate shipping rates until the customer confirms payment. Update the `RequestedSession` with this address to retrieve available shipping rates:

#### HTML + JS

```javascript
expressCheckoutElement.on("shippingaddresschange", async (event) => {
  // event.address contains: city, state, postal_code, country (no line1)
  const { shippingRates, lineItems } =
    await updateRequestedSessionFulfillmentAddress(sessionId, event.address);

  event.resolve({ shippingRates, lineItems });
});
```

#### React

```jsx
<ExpressCheckoutElement
  options={options}
  onShippingAddressChange={async (event) => {
    const { shippingRates, lineItems } =
      await updateRequestedSessionFulfillmentAddress(sessionId, event.address);

    event.resolve({ shippingRates, lineItems });
  }}
/>
```

#### Handle shipping rate selection

When the customer selects a shipping option, update the `RequestedSession` with the selected option:

#### HTML + JS

```javascript
expressCheckoutElement.on("shippingratechange", async (event) => {
  const { lineItems } = await updateRequestedSessionShippingOption(
    sessionId,
    event.shippingRate.id,
  );

  event.resolve({ lineItems });
});
```

#### React

```jsx
<ExpressCheckoutElement
  options={options}
  onShippingRateChange={async (event) => {
    const { lineItems } = await updateRequestedSessionShippingOption(
      sessionId,
      event.shippingRate.id,
    );

    event.resolve({ lineItems });
  }}
/>
```

#### Confirm the checkout

When the customer confirms payment, update the `RequestedSession` with complete details, create a PaymentMethod, and confirm:

#### HTML + JS

```javascript
expressCheckoutElement.on("confirm", async (event) => {
  await updateFulfillmentDetails(sessionId, {
    name: event.shippingAddress.name,
    email: event.billingDetails.email,
    phone: event.billingDetails.phone,
    address: event.shippingAddress.address,
  });

  const { paymentMethod } = await stripe.preparePaymentMethod({ elements });

  await confirmRequestedSession(sessionId, paymentMethod.id);
});
```

#### React

```jsx
<ExpressCheckoutElement
  options={options}
  onConfirm={async (event) => {
    await updateFulfillmentDetails(sessionId, {
      name: event.shippingAddress.name,
      email: event.billingDetails.email,
      phone: event.billingDetails.phone,
      address: event.shippingAddress.address,
    });

    const { paymentMethod } = await stripe.preparePaymentMethod({ elements });

    await confirmRequestedSession(sessionId, paymentMethod.id);
  }}
/>
```

#### Payment Element

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) with [Address Element](https://docs.stripe.com/elements/address-element.md) for standard guest checkout flows with manual card entry.

#### Set up Elements

The Delegated Checkout API requires complete customer details. Configure your Elements to collect all required information:

| Configuration                                            | Reason                                                                                |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Custom email input                                       | The Delegated Checkout API requires email, but the Address Element doesn’t collect it |
| `fields: { phone: 'always' }`                            | The Delegated Checkout API requires phone number                                      |
| Separate Address Element with `mode: 'billing'`          | The Delegated Checkout API requires billing address                                   |
| `fields: { billingDetails: 'never' }` on Payment Element | Source billing details from the Address Element instead                               |

#### HTML + JS

```javascript
const elements = stripe.elements({
  mode: "payment",
});

const shippingAddressElement = elements.create("address", {
  mode: "shipping",
  fields: { phone: "always" },
  validation: { phone: { required: "always" } },
});

const billingAddressElement = elements.create("address", {
  mode: "billing",
});

const paymentElement = elements.create("payment", {
  fields: { billingDetails: "never" },
});

shippingAddressElement.mount("#shipping-address-element");
billingAddressElement.mount("#billing-address-element");
paymentElement.mount("#payment-element");
```

#### React

```jsx
import {
  Elements,
  AddressElement,
  PaymentElement,
} from "@stripe/react-stripe-js";

const options = {
  mode: "payment",
};

function CheckoutForm() {
  return (
    <Elements stripe={stripePromise} options={options}>
      <AddressElement
        options={{
          mode: "shipping",
          fields: { phone: "always" },
          validation: { phone: { required: "always" } },
        }}
      />
      <AddressElement options={{ mode: "billing" }} />
      <PaymentElement options={{ fields: { billingDetails: "never" } }} />
    </Elements>
  );
}
```

#### Collect shipping details

When the customer enters their shipping address, update the `RequestedSession` to retrieve available shipping rates:

#### HTML + JS

```javascript
shippingAddressElement.on("change", async (event) => {
  if (event.complete) {
    const { shippingRates } = await updateRequestedSessionFulfillmentAddress(
      sessionId,
      event.value.address,
    );

    renderShippingOptions(shippingRates);
  }
});
```

#### React

```jsx
<AddressElement
  options={{ mode: "shipping", fields: { phone: "always" } }}
  onChange={async (event) => {
    if (event.complete) {
      const { shippingRates } = await updateRequestedSessionFulfillmentAddress(
        sessionId,
        event.value.address,
      );

      setShippingRates(shippingRates);
    }
  }}
/>
```

#### Handle shipping rate selection

When the customer selects a shipping option, update the `RequestedSession`:

#### HTML + JS

```javascript
async function onShippingOptionSelected(shippingRateId) {
  const { lineItems } = await updateRequestedSessionShippingOption(
    sessionId,
    shippingRateId,
  );

  renderOrderSummary(lineItems);
}
```

#### React

```jsx
const handleShippingOptionChange = async (shippingRateId) => {
  const { lineItems } = await updateRequestedSessionShippingOption(
    sessionId,
    shippingRateId,
  );

  setLineItems(lineItems);
};
```

#### Confirm the checkout

When the customer submits payment, create a PaymentMethod and confirm the `RequestedSession`.

#### HTML + JS

```javascript
async function handleSubmit() {
  const billingAddress = await billingAddressElement.getValue();

  const { paymentMethod } = await stripe.preparePaymentMethod({
    elements,
    params: {
      billing_details: {
        name: billingAddress.value.name,
        address: billingAddress.value.address,
      },
    },
  });

  await confirmRequestedSession(sessionId, paymentMethod.id);
}
```

#### React

```jsx
const handleSubmit = async () => {
  const billingAddress = await billingAddressRef.current.getValue();

  const { paymentMethod } = await stripe.preparePaymentMethod({
    elements,
    params: {
      billing_details: {
        name: billingAddress.value.name,
        address: billingAddress.value.address,
      },
    },
  });

  await confirmRequestedSession(sessionId, paymentMethod.id);
};
```

### Mobile integration

For mobile integrations, follow the standard [Payment Sheet integration](https://docs.stripe.com/payments/mobile/accept-payment.md) guide. The Delegated Checkout API specific differences occur when you initialize the Payment Sheet:

#### Supported payment methods

Mobile integrations support the same payment methods listed above.

| Standard Payment Sheet                                                                                                 | Shared payment token (SPT) mode (The Delegated Checkout API)                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Specify the payment mode using `mode`.                                                                                 | Specify `payment` mode using `sharedPaymentTokenSessionWithMode`.                                                                                     |
| A callback fires when the customer confirms. You create a `PaymentIntent` on your server and return its client secret. | A callback fires when the customer confirms. You confirm the `RequestedSession` on your server with the `PaymentMethod` ID. No return value required. |
| Payment Sheet handles charge confirmation using the client secret.                                                     | Your server confirms the charge when it confirms the `RequestedSession`.                                                                              |

#### iOS (Swift)

#### SPT mode configuration

```swift
@_spi(SharedPaymentToken) import StripePaymentSheet

func didTapCheckoutButton() {
    let intentConfig = PaymentSheet.IntentConfiguration(
        sharedPaymentTokenSessionWithMode: .payment(amount: 1099, currency: "usd"),
        sellerDetails: nil,
        preparePaymentMethodHandler: { paymentMethod, shippingAddress in
            // Implement confirmRequestedSession to call the Confirm
            // Requested Session endpoint on your server
            confirmRequestedSession(paymentMethodId: paymentMethod.stripeId)
        }
    )

    var configuration = PaymentSheet.Configuration()
    configuration.merchantDisplayName = "Your App"
    configuration.returnURL = "your-app://stripe-redirect"
    let paymentSheet = PaymentSheet(intentConfiguration: intentConfig, configuration: configuration)
}
```

#### Android (Kotlin)

#### Configure SPT mode

```kotlin
@OptIn(SharedPaymentTokenSessionPreview::class)
fun onCheckoutButtonPressed() {
    val paymentSheet = PaymentSheet.Builder(::onPaymentSheetResult)
        .preparePaymentMethodHandler { paymentMethod, shippingAddress ->
            // Implement confirmRequestedSession to call the Confirm
            // RequestedSession endpoint on your server.
            val id = paymentMethod.id ?: error("Payment method ID must not be null")
            confirmRequestedSession(paymentMethodId = id)
        }
        .build(this)

    paymentSheet.presentWithIntentConfiguration(
        intentConfiguration = PaymentSheet.IntentConfiguration(
            sharedPaymentTokenSessionWithMode = PaymentSheet.IntentConfiguration.Mode.Payment(
                amount = 1099L,
                currency = "USD",
            ),
            sellerDetails = null
        ),
        configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Your App").build()
    )
}
```

### Confirm the requested session

After the customer provides the required information, confirm the `RequestedSession` with a `PaymentMethod`.

When you confirm a `RequestedSession`, Stripe creates an [SPT](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md) from the `PaymentMethod` and sets usage limits and seller details. Stripe routes the token to the seller for payment processing, so you don’t need to manage the token’s lifecycle.

You must provide risk details when you confirm a `RequestedSession`. You can use a [RadarSession](https://docs.stripe.com/radar/radar-session.md#create-radar-session) to capture these details automatically, or you can pass the risk signals directly in the API. Stripe uses risk signals for Radar models and scoring.

#### Radar session

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode "return_url=https://example.com/agent-checkout/return" \
  -d "risk_details[client_device_metadata_details][radar_session]={{RADAR_SESSION_ID}}"
```

#### Risk signals

```curl
curl https://api.stripe.com/v1/delegated_checkout/requested_sessions/{{SESSION_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode "return_url=https://example.com/agent-checkout/return" \
  --data-urlencode "risk_details[client_device_metadata_details][referrer]=https://example.com" \
  -d "risk_details[client_device_metadata_details][remote_ip]=1.2.3.4" \
  -d "risk_details[client_device_metadata_details][time_on_page_ms]=1000" \
  --data-urlencode "risk_details[client_device_metadata_details][user_agent]=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

### Handle next actions

When you confirm a `RequestedSession`, the seller might complete the payment immediately, or the underlying SPT might transition to `requires_action`. This usually happens for redirect payment methods such as Klarna and Affirm, and it might happen when card payments require 3D Secure authentication.

If the payment requires additional customer action (for example, because the payment method uses a redirect or the card issuer requires 3D Secure authentication), you must handle that action because the buyer is interacting with your interface, not the seller’s. Provide a `return_url` when you confirm the `RequestedSession` and listen for the `shared_payment.issued_token.requires_action` event. You can access the `next_action` on the expandable `shared_payment_issued_token` property of the `RequestedSession`. For more information about the SPT `next_action`, see [Handle the next action](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md?agent-seller=agent#handle-next-actions).

After the customer completes the required action, Stripe sends the `shared_payment.issued_token.active` event unless the SPT was deactivated first. Stripe then continues processing the checkout and sends `delegated_checkout.requested_session.completed` when the order is complete.

#### Get order information

If the payment doesn’t require additional customer action, or after the customer completes any required next action, the response includes order information:

```json
{
  "id": "{{SESSION_ID}}",
  "status": "completed",
  "payment_method": "{{PAYMENT_METHOD_ID}}",
  "shared_payment_issued_token": "{{SHARED_PAYMENT_TOKEN_ID}}",
  "order_details": {
    "order_status_url": "https://seller.com/orders/{{ORDER_ID}}"
  }
  // ...
}
```

Use `order_status_url` to provide customers with order tracking.

#### Retry failed payments

When configured, Stripe calls the seller’s API endpoints for real-time inventory checks or shipping quotes. Stripe returns a `424` status code if the seller’s API endpoint returns a non-`2xx` status code. You can retry payments that fail with a `424` status code if the error is transient (for example, a seller API timeout).

### Listen for webhooks

Listen for webhook events to track the `RequestedSession` lifecycle and any SPT next action that the buyer must complete to finish the payment:

| Event                                            | Description                                                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `delegated_checkout.requested_session.created`   | Stripe created a new `RequestedSession`.                                                               |
| `delegated_checkout.requested_session.updated`   | Stripe updated the `RequestedSession` details.                                                         |
| `delegated_checkout.requested_session.completed` | Stripe processed the payment successfully.                                                             |
| `delegated_checkout.requested_session.expired`   | The `RequestedSession` expired or was manually closed.                                                 |
| `shared_payment.issued_token.requires_action`    | The SPT requires buyer action in your interface before the seller can complete the payment.            |
| `shared_payment.issued_token.active`             | The buyer completed the required action and the SPT can proceed through the rest of the checkout flow. |

## Test integration

To test your integration, enable **Test Seller** in the Agentic commerce page in the Dashboard. The test seller simulates a real seller so you can verify your checkout flow end-to-end without a live seller connection.

After you enable the test seller:

1. Ingest the test product feed through SSH File Transfer Protocol (SFTP).
1. Use the items from the product feed as `line_item_details` when you create a `RequestedSession` with the test seller’s Stripe profile.
1. Complete the full checkout flow—update fulfillment details, collect a payment method, and confirm the `RequestedSession`—to verify your integration works as expected.

# Redirect

> This is a Redirect for when agent-checkout-mode is feed-only. View the full page at https://docs.stripe.com/agentic-commerce/for-agents?agent-checkout-mode=feed-only.

Use the redirect integration to ingest seller product catalogs through Stripe without using the Delegated Checkout API. This option is for agents that want access to seller product data but want to handle product display, checkout, and purchase flow independently.

## Get started

### Set up your Stripe account

[Create a Stripe account](https://stripe.com/register) if you don’t already have one. After you verify your email, activate payments by providing business and personal information, linking a bank account for payouts, and setting up two-step authentication.

### Begin agent configuration

Go to the [Agentic commerce](https://dashboard.stripe.com/agentic-commerce) page and select **Onboard as an agent** to configure your account as an agent. If you don’t already have a [Stripe profile](https://docs.stripe.com/get-started/account/profile.md), Stripe prompts you to create one.

### (Optional) Upload terms of service and privacy policy

You can require sellers to accept your terms of service and privacy policy before they proceed. During onboarding, upload a link for each document. Stripe shows these links to sellers when they initiate an agreement. This step is optional.

### Configure product feed acceptance

Set up SSH File Transfer Protocol (SFTP) to ingest seller product feeds from Stripe. You must provide the host name, port, and user name. Stripe generates a public and private key pair that you add to the server’s authorized keys. The public key is available as you complete agent onboarding in the Stripe Dashboard. Stripe rotates the public and private keys every 365 days and notifies the agent when it’s time to rotate.

During onboarding, Stripe also presents you with a unique challenge token. You must upload this token to your SFTP host in a file called `stripe-verification.txt`. Once Stripe verifies the presence of this file with the expected token, Stripe begins uploading product catalogs for your sellers to your SFTP server.

### Complete verification

After you complete all onboarding steps, your account might enter a pending state while Stripe completes final verification checks. Stripe might ask you to complete additional identity verification, which you can access in your [Account settings](https://dashboard.stripe.com/settings/account). Stripe sends you an email when your agent configuration becomes active.

## Manage seller relationships

### Set up an orchestrated commerce agreement

After you complete agent onboarding, all Agentic Commerce Suite (ACS) sellers can discover your account name and business profile in the Dashboard.

Before you can connect with a seller, you need an orchestrated commerce agreement (OCA). An OCA is a required connection between your agent and a seller that enables agentic commerce flows. Only a seller can initiate an OCA request.

After a seller requests an OCA, the seller appears on the Agentic commerce page in the Dashboard. You can approve or reject the OCA for that seller.

### Terminate an orchestrated commerce agreement

Either party can terminate an OCA at any time. After termination, only the party that terminated the OCA can request a new one. You can terminate an OCA on the Agentic commerce page in the Dashboard.

### Manage an OCA with webhooks

Configure your agent to listen for [v2 webhooks](https://docs.stripe.com/api/v2/core/event_destinations.md). Set up an event destination to receive these events:

- `v2.orchestrated_commerce.agreement.created`
- `v2.orchestrated_commerce.agreement.partially_confirmed`
- `v2.orchestrated_commerce.agreement.confirmed`
- `v2.orchestrated_commerce.agreement.terminated`

#### Establish an OCA

After a seller enables your agent in the Stripe Dashboard, Stripe sends two webhooks to your agent: `v2.orchestrated_commerce.agreement.created` and `v2.orchestrated_commerce.agreement.partially_confirmed`.

When you receive the `partially_confirmed` webhook, retrieve the OCA to verify the seller’s identity, then confirm your side of the OCA:

```json
// Webhook payload
{
  "id": "evt_123",
  "object": "v2.core.event",
  "type": "v2.orchestrated_commerce.agreement.partially_confirmed",
  "related_object": {
    "id": "orca_123",
    "type": "v2.orchestrated_commerce.agreement",
    "url": "/v2/orchestrated_commerce/agreements/orca_123"
  }
}
```

Retrieve the OCA to verify the seller:

```curl
curl https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

You can also retrieve the seller’s Stripe profile for additional details, such as display name and branding.

```curl
curl https://api.stripe.com/v2/network/profiles/{{SELLER_PROFILE_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Confirm the OCA:

```curl
curl -X POST https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}}/confirm \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Stripe sends a `v2.orchestrated_commerce.agreement.confirmed` webhook to the seller. After both parties confirm the OCA, it authorizes data access between your agent and the seller.

#### Terminate an OCA

Either party can terminate an OCA at any time:

```curl
curl -X POST https://api.stripe.com/v2/orchestrated_commerce/agreements/{{OCA_ID}}/terminate \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview"
```

Termination sends a `v2.orchestrated_commerce.agreement.terminated` webhook to the other party and revokes the OCA. After termination, only the party that terminated the OCA can initiate a new one.

## Ingest product feeds

Seller product feeds are sent to the SFTP server you set up during onboarding. For details on the SFTP directory layout, feed schemas, and manifest handling, see [SFTP catalog ingestion](https://docs.stripe.com/agentic-commerce/product-feed/sftp-catalog-ingestion.md).

## Test integration

To test your integration, enable **Test Seller** in the Agentic commerce page in the Dashboard. The test seller simulates a real seller so you can verify your feed ingestion without a live seller connection.

After you enable the test seller:

1. Ingest the test product feed through SSH File Transfer Protocol (SFTP).
1. Verify that the product data arrives on your SFTP server and matches the expected [product feed field reference](https://docs.stripe.com/agentic-commerce/product-feed.md#product-feed-field-reference) structure.
