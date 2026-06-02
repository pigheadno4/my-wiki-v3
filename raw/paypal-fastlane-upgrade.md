<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/upgrade/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Upgrade to Fastlane
slug: /docs/checkout/fastlane/upgrade/
createTime: '2025-02-25T08:29:55.054Z'
updateTime: '2025-02-27T08:46:05.005Z'
---

# Upgrade to Fastlane

Upgrade guide for existing PayPal or card field integrations (Orders v2 API) to add Fastlane.

## Know before you code

- Sandbox business account required with Fastlane and Vault enabled (Developer Dashboard → Apps & Credentials → app → Features → Accept payments → Fastlane and Vault checkboxes)
- If you have a PayPal or cards integration with the Orders v2 API, you can upgrade to Fastlane

## Upgrade PayPal (buttons integration → Fastlane)

### Script tag changes

Before:
```html
<script src="https://www.paypal.com/sdk/js?components=buttons&client-id=CLIENT_ID"></script>
```

After — add `fastlane` to components, add `data-sdk-client-token` and `data-client-metadata-id`:
```html
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,fastlane"
  data-sdk-client-token="SDK_CLIENT_TOKEN"
  data-client-metadata-id="CM_ID">
</script>
```

### Add email field + Fastlane lookup

Display a field to collect the payer's email address. After collecting:

```javascript
const { customerContextId } = await identity.lookupCustomerByEmail(
  document.getElementById("email").value
);
```

### Full authentication flow

```javascript
var renderFastlaneMemberExperience = false;

if (customerContextId) {
  const { authenticationState, profileData } =
    await identity.triggerAuthenticationFlow(customerContextId);

  if (authenticationState === "succeeded") {
    renderFastlaneMemberExperience = true;
    const name = profileData.name;
    const shippingAddress = profileData.shippingAddress;
    const card = profileData.card;
  } else {
    renderFastlaneMemberExperience = false; // treat as guest
  }
} else {
  renderFastlaneMemberExperience = false; // no profile found
}
```

### Shipping address for Fastlane members

```javascript
if (renderFastlaneMemberExperience) {
  if (profileData.shippingAddress) {
    const changeAddressButton = document.getElementById("your-change-address-button");
    changeAddressButton.addEventListener("click", async () => {
      const { selectedAddress, selectionChanged } =
        await profile.showShippingAddressSelector();
      if (selectionChanged) {
        // selectedAddress contains new address
      }
    });
  } else {
    // render your shipping address form
  }
} else {
  // render your shipping address form
}
```

### FastlanePaymentComponent — member or guest

```javascript
const shippingAddress = {
  name: { firstName: "Jen", lastName: "Smith" },
  address: {
    addressLine1: "1 E 1st St",
    addressLine2: "5th Floor",
    adminArea1: "Bartlett",
    adminarea2: "IL",
    postalCode: "60103",
    countryCode: "US",
    phone: "16503551233"
  }
};

const options = {
  fields: {
    phoneNumber: { prefill: "4026607986" }  // example prefill
  },
  styles: {
    root: { backgroundColorPrimary: "#ffffff" }
  }
};

const fastlanePaymentComponent = await fastlane.FastlanePaymentComponent({ options, shippingAddress });
fastlanePaymentComponent.render("#payment-container");

document.getElementById("submit-button").addEventListener("click", async () => {
  const { id } = await fastlanePaymentComponent.getPaymentToken();
  // Send paymentToken to server
});
```

HTML container:
```html
<div id="payment-container"></div>
<button id="submit-button">Submit Order</button>
```

### Server-side capture (same as standard Fastlane)

```bash
curl -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
 -H 'PayPal-Request-Id: UNIQUE_ID' \
 -H 'Authorization: Bearer PAYPAL_ACCESS_TOKEN' \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Client-Metadata-Id: CM_ID' \
 -d '{
  "intent": "CAPTURE",
  "payment_source": {
    "card": { "single_use_token": "1h371660pr490622k" }
  },
  "purchase_units": [{
    "amount": { "currency_code": "USD", "value": "50.00" },
    "shipping": {
      "type": "SHIPPING",
      "address": {
        "address_line_1": "585 Moreno Ave",
        "admin_area_2": "Los Angeles",
        "admin_area_1": "CA",
        "postal_code": "90049",
        "country_code": "US"
      }
    }
  }]
}'
```

## Upgrade Card (card-fields integration → Fastlane)

### Script tag changes

Before:
```html
<script src="https://www.paypal.com/sdk/js?components=buttons,card-fields&client-id=CLIENT_ID"></script>
```

After — replace `card-fields` with `fastlane`, add client token and metadata ID:
```html
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,fastlane"
  data-sdk-client-token="SDK_CLIENT_TOKEN"
  data-client-metadata-id="CM_ID">
</script>
```

The email lookup, authentication, shipping address, and FastlanePaymentComponent code is identical to the PayPal upgrade path above.

The existing server-side Orders API capture request (using `single_use_token`) remains unchanged.

## Testing and Go Live

- Test in sandbox using the [Fastlane integration testing guide](https://developer.paypal.com/docs/checkout/fastlane/integrate/#link-testintegration)
- Go live: [Move your app to production](https://developer.paypal.com/api/rest/production/)
