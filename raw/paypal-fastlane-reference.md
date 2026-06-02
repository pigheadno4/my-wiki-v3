<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/reference/ -->
<!-- Fetched: 2026-04-13 -->

# Fastlane Reference

Troubleshoot, read FAQs, follow best practices, and customize your integration.

## Troubleshooting

**Authorization error while initializing Fastlane**
Merchant account and client credentials may not be fully provisioned for Fastlane. Contact account team.

**Fastlane member doesn't have cards or addresses**
Add a new card or address to the member's Fastlane profile and complete the order.

**No payment token returned**
If `FastlaneCardComponent.getPaymentToken()` doesn't return a token, ensure all required parameters are passed in the correct format.

**Undefined methods returned**
If `identity.triggerAuthenticationFlow()`, `profile.showShippingAddressSelector()`, or `profile.showCardSelector()` return `undefined`, Fastlane has been disabled in the PayPal dashboard. The Fastlane SDK falls back to the guest experience without the option to create a Fastlane profile — no interruption to buyers.

## FAQs

**Will Fastlane work if I save a payer's payment methods to the PayPal vault?**
Yes. The `paymentToken` returned on the client can be saved to the vault before or after transacting. PayPal only supports vaulting using the `store_in_vault` attribute of the create order request. Fastlane does not support a flow where a customer or payment method is created prior to a transaction.

**How long is a payment token valid?**
A `paymentToken` is valid for **3 hours** from the time of issuance.

**What if the payer's shipping address is in a location that my site does not ship to?**
Pass a list of allowed locations using the `addressOptions` object when calling `window.paypal.fastlane.create()`.

**How should I handle when a payer leaves the checkout page?**
Call `triggerAuthenticationFlow()` when the page reloads. The SDK determines whether the payer must authenticate via OTP again or if the session should be restored. The method returns `authenticatedCustomerResult` including a new `paymentToken`.

**I am located outside the US. How can I test Fastlane?**
Fastlane is only available to payers in the US. Use a VPN to test payer flows from outside the US.

**Does a Fastlane member have to authenticate with an OTP for every transaction?**
A Fastlane member who has authenticated on their device won't receive an OTP for additional transactions with the same merchant during the same session. After the session expires, re-authentication is required.

**Does Fastlane support MOTO or manual entry?**
No. Fastlane does not support mail order/telephone order (MOTO) or manual entry transactions.

## Best Practices

### Buyer Experience

- **Present the branded PayPal button upstream**: show PayPal button on cart page or alongside the Fastlane email field
- **Make email entry the first step**: Fastlane accounts are looked up by email — email field must come first in checkout
- **Render the Fastlane watermark**: display below merchant-rendered fields; includes link to Fastlane terms of service
- **Streamline the process**: after Fastlane member authenticates, hide other payment methods under a single link; maintain minimalistic UI

### Member Flow

After a Fastlane member authenticates:
- Direct users to the order review page or equivalent
- Pre-select the least expensive shipping option
- Provide a "change" button for shipping address → calls `showAddressSelector()`
- Provide a "change" button for payment method → calls `showCardSelector()`
- For specific use cases (e.g. gift message), direct returning users to the relevant page

### Integration

- **Load Fastlane SDK on checkout page load**: always load during `onload` event — delayed loading causes conversion issues
- **Send shipping and billing addresses server-side**: pass via `/v2/checkout/orders` — especially important when users add new addresses or payment methods
- **Call authentication flow on checkout page refresh**: invoke `triggerAuthenticationFlow()` each time the checkout page reloads; returns new single-use token
- **Ensure Fastlane members can update stored credentials**: use `profile.showShippingAddressSelector()` or `profile.showCardSelector()` for editing

## Configuration Parameters

```javascript
window.paypal.Fastlane(options);
```

```typescript
interface FastlaneOptions {
  shippingAddressOptions: AddressOptions;
  cardOptions: CardOptions;
  styles: StyleOptions;
}

interface AddressOptions {
  // default: empty array = all locations allowed
  allowedLocations: AddressLocationEnum[];
  // Format: "US" = all regions; "US:CA" = specific region; "US:CA,US:AZ,FR" = multiple
}

enum CardBrandEnum {
  VISA, MASTERCARD, AMEX, DINERS, DISCOVER, JCB,
  CHINA_UNION_PAY, MAESTRO, ELO, MIR, HIPER, HIPERCARD
}

interface CardOptions {
  // default: empty array = all brands allowed
  allowedBrands: CardBrandEnum[];
}
```

## Fastlane Namespace

```typescript
interface Fastlane {
  identity: {
    lookupCustomerByEmail: (email: string) => LookupCustomerResult;
    triggerAuthenticationFlow: (customerContextId: string, options: AuthenticationFlowOptions) => AuthenticatedCustomerResult;
  };
  profile: {
    showShippingAddressSelector: () => ShowShippingAddressSelectorResult;
    showCardSelector: () => ShowCardSelectorResult;
  };
  setLocale: (locale: string) => void; // options: en_us, es_us, fr_us, zh_us
  FastlaneCardComponent: (options: FastlaneCardComponentOptions) => FastlaneCardComponent;
  FastlanePaymentComponent: (options: FastlanePaymentComponentOptions) => FastlanePaymentComponent;
  FastlaneWatermarkComponent: (options: FastlaneWatermarkOptions) => FastlaneWatermarkComponent;
}
```

## Type Definitions

### LookupCustomerResult
```typescript
interface LookupCustomerResult {
  customerContextId: string;
}
```

### AuthenticatedCustomerResult
```typescript
interface AuthenticatedCustomerResult {
  authenticationState: 'succeeded' | 'failed' | 'canceled' | 'not_found';
  profileData: ProfileData;
}

interface ProfileData {
  name: Name;
  shippingAddress: Shipping;
  card: PaymentToken;
}

interface Name {
  firstName: string;
  lastName: string;
  fullName: string;
}

interface Phone {
  nationalNumber: string;
  countryCode: string;
}

interface Address {
  addressLine1: string;
  addressLine2: string;
  adminArea1: string;
  adminArea2: string;
  postalCode: string;
  countryCode: string;
  phone: Phone;
}

interface Shipping {
  name: Name;
  address: Address;
  companyName: string;
}

interface PaymentToken {
  id: string; // the payment token
  paymentSource: PaymentSource;
}

interface PaymentSource {
  card: CardPaymentSource;
}

interface CardPaymentSource {
  brand: string;
  expiry: string;      // "YYYY-MM"
  lastDigits: string;  // "1111"
  name: string;
  billingAddress: Address;
}
```

### Profile method result types
```typescript
interface ShowShippingAddressSelectorResult {
  selectionChanged: boolean;
  selectedAddress: Address;
}

interface ShowCardSelectorResult {
  selectionChanged: boolean;
  selectedCard: PaymentToken;
}
```

### FastlaneCardComponent
```typescript
interface FastlaneCardComponent {
  render: (container) => FastlaneCardComponent;
  getPaymentToken: async (options: PaymentTokenOptions) => PaymentToken;
}

interface FastlaneCardComponentOptions {
  styles: StyleOptions;
  fields: { [fieldName: string]: Field };
}

interface Field {
  placeholder: string;
  prefill: string;
  enabled: boolean;
}

interface PaymentTokenOptions {
  billingAddress: Address;
  cardholderName: Name;
}
```

## Card Field Configurations

Available fields for `FastlaneCardComponent` and `FastlanePaymentComponent`:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `number` | field (optional) | Card number |
| `expirationDate` | field (optional) | Expiration in MM/YYYY or MM/YY. Don't use with expirationMonth/Year. |
| `expirationMonth` | field (optional) | Expiration month MM. Use with expirationYear. |
| `expirationYear` | field (optional) | Expiration year YYYY or YY. Use with expirationMonth. |
| `cvv` | field (optional) | 3 or 4-digit CVV/CID. For CVV-only vaulted token, omit all other fields. |
| `postalCode` | field (optional) | Postal or region code |
| `cardholderName` | field (optional) | Cardholder name |
| `phoneNumber` | field (optional) | Payer's phone number |

```javascript
fastlane.FastlaneCardComponent({
  styles,
  fields: {
    number: { placeholder: "Number" },
    phoneNumber: { prefill: "555-555-5555" }
  }
}).render(elem);
```

## Style Options

```typescript
interface StyleOptions {
  root: {
    backgroundColor: string;  // Default: #ffffff
    errorColor: string;        // Default: #D9360B
    fontFamily: string;        // Default: PayPal-Open; allowed: Arial, Verdana, Tahoma, Trebuchet MS, Times New Roman, Georgia, Garamond, Courier New, Brush Script MT
    textColorBase: string;     // Default: #01080D
    fontSizeBase: string;      // Default: 16px (min 13px, max 24px)
    padding: string;
    primaryColor: string;
  };
  input: {
    backgroundColor: string;
    borderRadius: string;      // Default: 0.25em (min 0px, max 32px)
    borderColor: string;       // Default: #DADDDD
    borderWidth: string;       // Default: 1px (max 5px)
    textColorBase: string;     // Default: #01080D
    focusBorderColor: string;  // Default: #0057FF
  };
}
```

### Design Guidance

- **backgroundColor vs textColor**: contrast ratio must be ≥ 4.5:1 — PayPal auto-corrects if not met
- **borderColor vs backgroundColor**: adequate contrast for consent toggle
- **WCAG AA compliance required**: all Fastlane integrations must conform to WCAG levels A and AA; if legal text and toggle button colors are indistinguishable, component reverts to defaults
- Colors: any valid CSS value (hex, RGB, RGBA, color names) — **no transparency allowed** for most fields

## FastlaneWatermarkComponent

```typescript
interface FastlaneWatermarkOptions {
  includeAdditionalInfo: boolean; // true = show tooltip; false = logo only
}

interface FastlaneWatermarkComponent {
  render: (container) => null;
}
```

Preload watermark asset in `<head>`:
```html
<link rel="preload"
  href="https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg"
  as="image" type="image/avif" />
```
