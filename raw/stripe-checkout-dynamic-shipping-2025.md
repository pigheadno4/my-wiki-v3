<!-- Source URL: https://docs.stripe.com/payments/checkout/custom-shipping-options -->
<!-- Fetched: 2026-04-21 -->

# Dynamically customize shipping options

Learn how to create different shipping rates for your customers.

Learn how to dynamically update shipping options based on the address that your customer enters when you use Checkout.

### Use cases

- **Validate an address**: Confirm whether you can ship a product to a customer’s address using your own custom validation rules. You can also create a custom UI for customers to confirm their preferred address.
- **Show relevant shipping options**: Display only available shipping methods, based on the customer’s address. For example, show overnight shipping only for deliveries in your country.
- **Dynamically calculate shipping rates**: Calculate and display shipping fees based on a customer’s delivery address.
- **Update shipping rates based on order total**: Offer shipping rates based on the shipping address or order total, such as free shipping for orders over 100 USD. For checkouts allowing quantity changes or cross-sells, see [Dynamically updating line items](https://docs.stripe.com/payments/checkout/dynamically-update-line-items.md).

### Limitations

- Only supported in [payment mode](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-mode). [Shipping rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_options) aren’t available in subscription mode.

> #### Payment Intents API
>
> If you use the Payment Intents API, you must manually update shipping options and modify the payment amount based on a selected shipping option, or by creating a new PaymentIntent with adjusted amounts.

## Configure update permissions for the Checkout Session [Server-side]

Set the [shipping_address_collection.allowed_countries](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection-allowed_countries) to the list of countries you want to offer shipping to.

When you create the Checkout Session, pass the [permissions.update_shipping_details=server_only](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-permissions-update_shipping_details) option to disable the client-side [updateShippingAddress](https://docs.stripe.com/js/custom_checkout/update_shipping_address) method and to enable updating the shipping address and shipping options from your server.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  ui_mode: "elements",
  permissions: {
    update_shipping_details: "server_only",
  },
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  return_url: "https://example.com/return",
});
```

## Customize shipping options [Server-side]

Create an endpoint on your server to calculate the shipping options based on the customer’s shipping address.

1. [Retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve.md) the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md) using the `checkoutSessionId` from the request body.
1. Validate the customer’s shipping details from the request body.
1. Calculate the shipping options based on the customer’s shipping address and the line items in the Checkout Session.
1. [Update](https://docs.stripe.com/api/checkout/sessions/update.md) the Checkout Session with the customer’s [shipping_details](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-collected_information-shipping_details) and the [shipping_options](https://docs.stripe.com/api/checkout/sessions/update.md#update_checkout_session-shipping_options).

#### Ruby

```ruby
require 'sinatra'
require 'json'
require 'stripe'

set :port, 4242

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

# Return a boolean indicating whether the shipping details are valid
def validate_shipping_details(shipping_details)
  # TODO: Remove error and implement...
  raise NotImplementedError.new(<<~MSG)
    Validate the shipping details the customer has entered.
  MSG
end

# Return an array of the updated shipping options or the original options if no update is needed
def calculate_shipping_options(shipping_details, session)
  # TODO: Remove error and implement...
  raise NotImplementedError.new(<<~MSG)
    Calculate shipping options based on the customer's shipping details and the
    Checkout Session's line items.
  MSG
end

post '/calculate-shipping-options' do
  content_type :json
  request.body.rewind
  request_data = JSON.parse(request.body.read)

  checkout_session_id = request_data['checkout_session_id']
  shipping_details = request_data['shipping_details']

  # 1. Retrieve the Checkout Session
  session = client.v1.checkout.sessions.retrieve(checkout_session_id)

  # 2. Validate the shipping details
  if !validate_shipping_details(shipping_details)
    return { type: 'error', message: "We can't ship to your address. Please choose a different address." }.to_json
  end

  # 3. Calculate the shipping options
  shipping_options = calculate_shipping_options(shipping_details, session)

  # 4. Update the Checkout Session with the customer's shipping details and shipping options
  if shipping_options
    client.v1.checkout.sessions.update(checkout_session_id, {
      collected_information: { shipping_details: shipping_details },
      shipping_options: shipping_options
    })

    return { type: 'object', value: { succeeded: true } }.to_json
  else
    return { type: 'error', message: "We can't find shipping options. Please try again." }.to_json
  end
end
```

## Update the client SDK [Client-side]

#### HTML + JS

Initialize Stripe.js with the `custom_checkout_server_updates_1` beta header.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["custom_checkout_server_updates_1"],
});
```

#### React

Pass the `custom_checkout_server_updates_1` beta header when initializing the `stripe` instance.

```bash
npm install --save @stripe/react-stripe-js@^5.0.0 @stripe/stripe-js@^8.0.0
```

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["custom_checkout_server_updates_1"],
});
```

## Request server updates [Client-side]

#### HTML + JS

Create an asynchronous function that makes a request to your server to update the shipping options and wrap it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). A successful request updates the [Session](https://docs.stripe.com/js/custom_checkout/session_object) object with the new shipping options.

The following code example shows how to update the shipping options with the `AddressElement`.

```html
<div id="shipping-form">
  <!-- Shipping Address Element will be mounted here -->
  <div id="shipping-address-element"></div>
  <button id="save-button">Save</button>
  <div id="error-message"></div>
</div>

<div id="shipping-display" style="display: none">
  <div id="address-display"></div>
  <button id="edit-button">Edit</button>
</div>
```

```javascript
// mount the Shipping Address Element
const shippingAddressElement = checkout.createShippingAddressElement();
shippingAddressElement.mount("#shipping-address-element");

const toggleViews = (isEditing) => {
  document.getElementById("shipping-form").style.display =
    isEditing ? "block" : "none";
  document.getElementById("shipping-display").style.display =
    isEditing ? "none" : "block";
};

const displayAddress = (address) => {
  const displayDiv = document.getElementById("address-display");
  displayDiv.innerHTML = `
    <div>${address.name}</div>
    <div>${address.address.line1}</div>
    <div>${address.address.city}, ${address.address.state} ${address.address.postal_code}</div>
  `;
};

const updateShippingOptions = async (shippingDetails) => {
  const response = await fetch("/calculate-shipping-options", {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify({
      checkout_session_id: "session_id",
      shipping_details: shippingDetails,
    }),
  });

  const result = await response.json();

  if (result.type === "error") {
    document.getElementById("error-message").textContent = result.message;
    toggleViews(true);
  } else {
    document.getElementById("error-message").textContent = "";
    toggleViews(false);
    displayAddress(actions.getSession().shippingAddress);
  }

  return result;
};

const handleSave = async () => {
  const addressElement = await checkout.getShippingAddressElement();
  if (!addressElement) {
    return;
  }

  const result = await addressElement.getValue();
  if (!result.complete) {
    return;
  }

  try {
    await checkout.runServerUpdate(() => updateShippingOptions(result.value));
  } catch (error) {
    document.getElementById("error-message").textContent = error?.message;
    toggleViews(true);
  }
};

// Event Listeners
document.getElementById("save-button").addEventListener("click", handleSave);
document
  .getElementById("edit-button")
  .addEventListener("click", () => toggleViews(true));
```

#### React

Create an asynchronous function that makes a request to your server to update the shipping options and wrap it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). A successful request updates the [Session](https://docs.stripe.com/js/custom_checkout/session_object) object with the new shipping options.

The following code example shows how to update the shipping options with the `AddressElement`.

```jsx
import React from "react";
import {
  useCheckout,
  ShippingAddressElement,
} from "@stripe/react-stripe-js/checkout";

const Shipping = () => {
  const [editing, setEditing] = React.useState(true);
  const [error, setError] = React.useState(null);
  const checkoutState = useCheckout();
  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }
  const { runServerUpdate, id, shippingAddress, getShippingAddressElement } =
    checkoutState.checkout;

  const updateShippingOptions = async (shippingDetails) => {
    const response = await fetch("/calculate-shipping-options", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        checkout_session_id: id,
        shipping_details: shippingDetails,
      }),
    });

    if (response.type === "error") {
      setError(response.message);
      setEditing(true);
    } else {
      setError(null);
      setEditing(false);
    }

    return result;
  };

  const handleEdit = (event) => {
    event.preventDefault();
    setEditing(true);
  };

  const handleSave = async () => {
    const addressElement = getShippingAddressElement();
    if (!addressElement) {
      return;
    }
    const aeValue = await addressElement.getValue();
    if (!aeValue.complete) {
      return;
    }

    try {
      await runServerUpdate(() => updateShippingOptions(aeValue.value));
    } catch (e) {
      setError(e?.message);
      setEditing(true);
    }
  };

  if (!editing && shippingAddress) {
    const { line1, line2, city, postal_code, state, country } =
      shippingAddress.address;
    return (
      <div>
        <div>{shippingAddress.name}</div>
        <div>{line1}</div>
        <div>{line2}</div>
        <div>
          {city} {state} {postal_code} {country}
        </div>
        <button onClick={handleEdit}>Edit</button>
      </div>
    );
  }

  return (
    <div>
      <AddressElement options={{ mode: "shipping" }} />
      <button onClick={handleSave}>Save</button>
      {error && <div>{error}</div>}
    </div>
  );
};
```

## Test the integration

Follow these steps to test your integration, and ensure your custom shipping options work correctly.

1. Set up a sandbox environment that mirrors your production setup. Use your Stripe sandbox API keys for this environment.

1. Simulate various shipping addresses to verify that your `calculateShippingOptions` function handles different scenarios correctly.

1. Verify server-side logic by using logging or debugging tools to confirm that your server:
   - Retrieves the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md).
   - Validates shipping details.
   - Calculates shipping options.
   - Updates the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md) with new shipping details and options. Make sure the update response contains the new shipping details and options.

1. Verify client-side logic by completing the checkout process multiple times in your browser. Pay attention to how the UI updates after entering shipping details. Make sure that:
   - The `runServerUpdate` function is called when expected.
   - Shipping options update correctly based on the provided address.
   - Error messages display properly when shipping is unavailable.

1. Enter invalid shipping addresses or simulate server errors to test error handling, both server-side and client-side.
