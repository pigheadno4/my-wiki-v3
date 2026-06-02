<!-- Source URL: https://developer.paypal.com/docs/checkout/fastlane/integrate/ (Flexible tab) -->
<!-- Fetched: 2026-04-13 -->

# Integrate Fastlane by PayPal — Flexible Integration

This is the Flexible tab variant of the Fastlane integration page. The Flexible pattern enables custom UI and renders your own form fields to collect address and payment. The backend is identical to the Quick Start integration.

## Flexible Integration Requirements

For **Fastlane members with a stored card**, render:
- The selected card from the `profile` object
- Fastlane watermark
- Change card button that invokes `profile.showCardSelector()`

For **Fastlane members with no card, unsupported card, and guest payers**, render:
- `FastlaneCardComponent` to accept new card information
- A form to capture the payer's billing address
- Pass billing address and cardholder name in `getPaymentToken()` method

Note: Even if the `cardholderName` field is disabled in your checkout process, it must still be sent in the `getPaymentToken()` request.

## Key difference from Quick Start

| Aspect | Quick Start | Flexible |
| ------ | ----------- | -------- |
| Payment component | `FastlanePaymentComponent()` — pre-built UI | `FastlaneCardComponent()` — custom card fields only |
| Billing address | Handled inside payment component | Merchant renders separate billing address form |
| Card selector | Built into payment component | Merchant invokes `profile.showCardSelector()` |
| Card display for member | Auto-rendered | Merchant renders selected card from `profileData` |
| `getPaymentToken()` call | Via `paymentComponent.getPaymentToken()` | Via `cardComponent.getPaymentToken({ billingAddress })` |
| Member state tracking | Not needed | `memberHasSavedPaymentMethods` state required |

## Flexible Frontend (HTML)

Adds a separate `<section id="billing">` for billing address (not present in Quick Start):

```html
<section id="billing">
  <fieldset>
    <input name="billing-address-line1" placeholder="Street address" autocomplete="address-line1" />
    <input name="billing-address-line2" placeholder="Apt., ste., bldg. (optional)" autocomplete="address-line2" />
    <input name="billing-address-level2" placeholder="City" autocomplete="address-level2" />
    <input name="billing-address-level1" placeholder="State" autocomplete="address-level1" />
    <input name="billing-postal-code" placeholder="ZIP code" autocomplete="postal-code" />
    <input name="billing-country" placeholder="Country" autocomplete="country" />
  </fieldset>
</section>

<section id="payment">
  <div id="selected-card"></div>      <!-- member's saved card display -->
  <div id="payment-watermark"></div>  <!-- Fastlane watermark -->
  <div id="card-component"></div>     <!-- FastlaneCardComponent for new card input -->
</section>
```

## Flexible Frontend (JavaScript)

### Initialization

```javascript
const {
    identity,
    profile,
    FastlaneCardComponent,
    FastlaneWatermarkComponent,
} = await window.paypal.Fastlane({
    metadata: { geoLocOverride: "US" },
    // shippingAddressOptions: { allowedLocations: [] },
    // cardOptions: { allowedBrands: [] },
});

const cardComponent = await FastlaneCardComponent();
const paymentWatermark = await FastlaneWatermarkComponent({ includeAdditionalInfo: false });
```

Note: No `styles` object in this example (unlike Quick Start which included `styles`).

### Additional state

```javascript
let memberHasSavedPaymentMethods;  // NEW — not in Quick Start
let billingAddress;                // NEW — not in Quick Start
```

### Payment section — member vs guest rendering

For members with saved card (`memberHasSavedPaymentMethods = true`):
- Display saved card: `💳 •••• ${paymentToken.paymentSource.card.lastDigits}`
- Show watermark
- "Edit" button calls `profile.showCardSelector()`

```javascript
paymentEditButton.addEventListener("click", async () => {
    if (memberHasSavedPaymentMethods) {
        const { selectionChanged, selectedCard } = await profile.showCardSelector();
        if (selectionChanged) {
            paymentToken = selectedCard;
            setPaymentSummary(paymentToken);
        }
    } else {
        setActiveSection(paymentSection);
    }
});
```

For guests / members without saved card:
- Render `cardComponent` in `#card-component`
- Collect billing address from separate billing form section
- Proceed: shipping → billing → payment

### Checkout — getPaymentToken with billingAddress

```javascript
// Flexible: pass billingAddress to cardComponent
if (!memberHasSavedPaymentMethods) {
    paymentToken = await cardComponent.getPaymentToken({ billingAddress });
}
```

vs Quick Start:
```javascript
// Quick Start: payment component handles billing internally
paymentToken = await paymentComponent.getPaymentToken();
```

### Shipping → next section logic

In Flexible, after shipping the next section depends on member status:
```javascript
setActiveSection(memberHasSavedPaymentMethods ? paymentSection : billingSection);
```

In Quick Start, it always goes directly to payment.

## Backend (Node.js)

Identical to the Quick Start backend — same `getClientToken()`, `getAccessToken()`, `createOrder()`, and server routes. Only title and `initScriptPath` differ:

```javascript
const locals = {
    title: "Fastlane - PayPal Integration (Flexible)",
    initScriptPath: "init-fastlane-flexible.js",  // vs "init-fastlane.js" in Quick Start
};
```
