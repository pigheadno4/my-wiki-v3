<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/integrate/ -->
<!-- Fetched: 2026-04-13 -->

# Integrate Fastlane by PayPal

Before beginning your integration, you need to set up your development environment.

Start your integration by grabbing the sample code from PayPal's GitHub repo, or visiting the PayPal GitHub Codespace.

## 1. Integrate front end (CLIENT)

### Step 1: Generate client token

Client token generation for Fastlane uses special parameters different from a regular access token:

```javascript
// POST /v1/oauth2/token
const searchParams = new URLSearchParams();
searchParams.append("grant_type", "client_credentials");
searchParams.append("response_type", "client_token");
searchParams.append("intent", "sdk_init");
searchParams.append("domains[]", DOMAINS);  // comma-separated domains
```

Returns `data.access_token` — used as `data-sdk-client-token` in the script tag.

### Step 2: Initialize PayPal JS SDK and Fastlane

Script tag (components must include `fastlane`):
```html
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=buttons,fastlane"
  data-sdk-client-token="CLIENT_TOKEN"
  defer
></script>
```

Initialize Fastlane in JavaScript:
```javascript
const {
    identity,
    profile,
    FastlanePaymentComponent,
    FastlaneWatermarkComponent,
} = await window.paypal.Fastlane({
    metadata: { geoLocOverride: "undefined" },
    // shippingAddressOptions: { allowedLocations: [] },
    // cardOptions: { allowedBrands: [] },
    styles: {
        root: {
            backgroundColor: "#faf8f5",
            // errorColor, fontFamily, textColorBase, fontSizeBase, padding, primaryColor
        },
        // input: { backgroundColor, borderRadius, borderColor, borderWidth, textColorBase, focusBorderColor }
    },
});
```

Supported locales: `en_us` (default), `es_us`, `fr_us`, `zh_us`.

### Step 3: Capture user email address

Render your own email input field. Display the Fastlane watermark below it:
```javascript
(await FastlaneWatermarkComponent({ includeAdditionalInfo: true }))
    .render("#watermark-container");
```

**Privacy note**: You are sharing consumer email addresses with PayPal (a data controller). The "Powered by Fastlane" logo and tooltip are required by PayPal.

Look up email:
```javascript
const { customerContextId } = await identity.lookupCustomerByEmail(email);
```

Authenticate if member:
```javascript
if (customerContextId) {
    const authResponse = await identity.triggerAuthenticationFlow(customerContextId);

    if (authResponse?.authenticationState === "succeeded") {
        memberAuthenticatedSuccessfully = true;
        shippingAddress = authResponse.profileData.shippingAddress;
        paymentToken = authResponse.profileData.card;
    }
}
```

`triggerAuthenticationFlow()` returns `AuthenticatedCustomerResult` with `authenticationState` property.
If authentication fails or is declined → treat as guest.

### Step 4: Render shipping address

Only required for Fastlane members with a shipping address in a supported region.

Not required for:
- Fastlane members without a shipping address
- Fastlane members with address in unsupported region
- Guest payers

For members: show returned address + Fastlane watermark + Fastlane logo + Change address button.

Change address calls:
```javascript
const { selectionChanged, selectedAddress } = await profile.showShippingAddressSelector();
```

Note: Fastlane is US-customers only, but merchants control shipping destinations via `allowedShippingLocations` parameter.

### Step 5: Accept payments (Quick Start)

```javascript
const paymentComponent = await FastlanePaymentComponent();
paymentComponent.render("#payment-component");

// on checkout button click:
paymentToken = await paymentComponent.getPaymentToken();
```

Quick start payment component auto-renders:
- Selected card for Fastlane member + "Change card" link
- Card fields for guests / members without a saved card
- Billing address fields

To update shipping address on the component:
```javascript
paymentComponent.setShippingAddress(shippingAddress);
```

Watermark preload (add to `<head>`):
```html
<link rel="preload"
  href="https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg"
  as="image" type="image/avif" />
```

### Step 6: Style the Fastlane component (optional)

Accessibility requirements:
- backgroundColor vs textColor contrast ratio: must be ≥ 4.5:1 (PayPal auto-corrects if not met)
- borderColor vs backgroundColor: adequate contrast for consent toggle

Use `StyleOptions` object inside the Fastlane init call.


## 2. Integrate back end (SERVER)

### Create order

Payment source uses `single_use_token` from Fastlane's `paymentToken.id`:

```javascript
const payload = {
    intent: "CAPTURE",
    payment_source: {
        card: {
            single_use_token: paymentToken.id,
        },
    },
    purchase_units: [{
        amount: { currency_code: "USD", value: "100" },
        shipping: {
            type: "SHIPPING",
            name: { full_name: fullName },
            address: { /* address fields */ },
        },
    }],
};

// POST /v2/checkout/orders
```

### Special use cases

**Store pickup**: set `shipping.type = "PICKUP_IN_STORE"` to prevent store address being saved to buyer's Fastlane profile.

**Vault with transaction**: include `store_in_vault` attribute in the `/v2/orders` request — returns a vault ID for future captures.

**Vault without transaction**: payment token is generated but Fastlane profile is NOT created. Fastlane profile is only created if the customer completes a transaction.

### Client token vs access token generation

Client token (for Fastlane SDK init) — extra params:
```javascript
searchParams.append("response_type", "client_token");
searchParams.append("intent", "sdk_init");
searchParams.append("domains[]", DOMAINS);
```

Access token (for Orders API calls) — standard:
```javascript
searchParams.append("grant_type", "client_credentials");
```

SDK URL construction:
```javascript
const sdkParams = new URLSearchParams({
    "client-id": PAYPAL_CLIENT_ID,
    components: "buttons,fastlane",
});
```

Server routes:
- `GET /` → render checkout page with SDK script tag + client token injected
- `POST /transaction` → create order with paymentToken + shippingAddress
- `GET /sdk/client-token` → return client token for client-side injection

## 3. Test integration

### Test cards
| Brand | Test number |
| ----- | ----------- |
| Visa | 4005 5192 0000 0004 |
| Visa | 4012 0000 3333 0026 |
| Visa | 4012 0000 7777 7777 |
| Mastercard | 5555 5555 5555 4444 |
| American Express | 3782 822463 10005 |

### Test OTP (one-time password)
- `111111` → successful authentication
- Any other 6-digit number → failed authentication

### Test guest payers
- Use a new email not associated with any Fastlane account
- Opt-in toggle must be ON to create a Fastlane profile
- Phone number must be valid (e.g. not 111-111-1111) — invalid number prevents profile creation
- No SMS sent in sandbox

### Test Fastlane members
- First create a profile via the guest flow
- Use the registered email + OTP `111111` for successful auth
- Test adding/changing address and card
- Test failed OTP scenarios

### Test PayPal members
PayPal members are handled automatically by the SDK:
- `lookupCustomerByEmail()` returns a `customerContextId` as if a Fastlane member
- `triggerAuthenticationFlow()` shows a CTA to create a Fastlane profile from PayPal account with one click
- If accepted → returns `profileData` like a Fastlane member
- If dismissed → returns empty `profileData` → treat as guest

## 4. Go live
- Request **Advanced Credit and Debit Card Payments** for your business account — Fastlane is enabled alongside it
- Change `PAYPAL_API_BASE_URL` from `api-m.sandbox.paypal.com` to `api-m.paypal.com`
- Change `PAYPAL_SDK_BASE_URL` from `www.sandbox.paypal.com` to `www.paypal.com`
