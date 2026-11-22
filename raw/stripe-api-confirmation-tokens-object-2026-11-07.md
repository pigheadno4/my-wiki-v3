<!-- Source URL: https://docs.stripe.com/api/confirmation_tokens/object -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# The Confirmation Token object

### The Confirmation Token object

```json
{
  "id": "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
  "object": "confirmation_token",
  "created": 1694025025,
  "expires_at": 1694068225,
  "livemode": true,
  "mandate_data": null,
  "payment_intent": null,
  "payment_method": null,
  "payment_method_preview": {
    "billing_details": {
      "address": {
        "city": "Hyde Park",
        "country": "US",
        "line1": "50 Sprague St",
        "line2": "",
        "postal_code": "02136",
        "state": "MA"
      },
      "email": "jennyrosen@stripe.com",
      "name": "Jenny Rosen",
      "phone": null
    },
    "card": {
      "brand": "visa",
      "checks": {
        "address_line1_check": null,
        "address_postal_code_check": null,
        "cvc_check": null
      },
      "country": "US",
      "display_brand": "visa",
      "exp_month": 8,
      "exp_year": 2026,
      "funding": "credit",
      "generated_from": null,
      "last4": "4242",
      "networks": {
        "available": [
          "visa"
        ],
        "preferred": null
      },
      "three_d_secure_usage": {
        "supported": true
      },
      "wallet": null
    },
    "type": "card"
  },
  "return_url": "https://example.com/return",
  "setup_future_usage": "off_session",
  "setup_intent": null,
  "shipping": {
    "address": {
      "city": "Hyde Park",
      "country": "US",
      "line1": "50 Sprague St",
      "line2": "",
      "postal_code": "02136",
      "state": "MA"
    },
    "name": "Jenny Rosen",
    "phone": null
  }
}
```

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string, value is "confirmation_token")
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `expires_at` (timestamp, nullable)
  Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- [`mandate_data`](https://docs.stripe.com/api/confirmation_tokens/object.md?query=mandate_data) (object, nullable)
  Data used for generating a Mandate.

- `metadata` (map, nullable)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payment_intent` (string, nullable)
  ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

- [`payment_method_options`](https://docs.stripe.com/api/confirmation_tokens/object.md?query=payment_method_options) (object, nullable)
  Payment-method-specific configuration for this ConfirmationToken.

- [`payment_method_preview`](https://docs.stripe.com/api/confirmation_tokens/object.md?query=payment_method_preview) (object, nullable)
  Payment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken.

- `return_url` (string, nullable)
  Return URL used to confirm the Intent.

- `setup_future_usage` (enum, nullable)
  Indicates that you intend to make future payments with this ConfirmationToken’s payment method.

  The presence of this property will [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be present in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

- `setup_intent` (string, nullable)
  ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

- [`shipping`](https://docs.stripe.com/api/confirmation_tokens/object.md?query=shipping) (object, nullable)
  Shipping information collected on this ConfirmationToken.

- `use_stripe_sdk` (boolean)
  Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to `true` on ConfirmationToken.
