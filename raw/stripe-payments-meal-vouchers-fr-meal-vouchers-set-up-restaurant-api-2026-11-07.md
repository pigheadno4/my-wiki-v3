<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set up a restaurant for titres-restaurant payments with the API

Use the Stripe API to onboard a restaurant to accept Bimpli, Pluxee, and Up Déjeuner French meal vouchers payments.

This guide shows how to onboard a restaurant to accept [French meal vouchers payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md) using the Stripe API. If you prefer to use the Stripe Dashboard, see [Set up a restaurant for titres-restaurant payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md).

Before you begin, you must obtain a license from [Commission Nationale des Titres-Restaurant](https://www.cntr.fr/) (CNTR) and contract with each of the French meal vouchers issuers you want to support.

> API features are only available in [private preview SDKs](https://docs.stripe.com/sdks/versioning.md#private-preview-release-channel).

Stripe supports the following French meal vouchers issuers:

- Bimpli
- Pluxee
- Up Déjeuner

> #### Want to accept France titres-restaurant payments?
> 
> France titres-restaurant is in private preview. Enter your email address to [join the waitlist](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md#fr_meal_voucher_preview). Stripe will contact you when we can onboard additional users.

### Want to accept France titres-restaurant payments?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api" \
  -d '{"email": "EMAIL", "preview": "fr_meal_voucher_preview"}'
```

## Update the Stripe SDK

This feature requires preview [Stripe version](https://docs.stripe.com/sdks/set-version.md) `2026-05-27.preview` or later.

If you must use an SDK version that doesn’t support this feature, you can still access [SDK private parameters](https://docs.stripe.com/sdks/server-side.md#undocumented-params-and-fields). You can also use custom requests in any of the following SDKs to call private endpoints related to this feature:

- [Ruby](https://github.com/stripe/stripe-ruby/blob/master/README.md#custom-requests)
- [Python](https://github.com/stripe/stripe-python/blob/master/README.md#custom-requests)
- [PHP](https://github.com/stripe/stripe-php/blob/master/README.md#custom-requests)
- [Node](https://github.com/stripe/stripe-node/blob/master/README.md#custom-requests)
- [Java](https://github.com/stripe/stripe-java/blob/master/README.md#custom-requests)
- [.NET](https://github.com/stripe/stripe-dotnet/blob/master/README.md#custom-requests)
- [Go](https://github.com/stripe/stripe-go/blob/master/README.md#custom-requests)

## Create a payment location

A [PaymentLocation](https://docs.stripe.com/api/payment-location.md?api-version=2026-05-27.preview) represents the physical restaurant or store where you accept meal vouchers payments. Each location maps to a single SIRET, the French 14-digit establishment identifier. If you operate multiple branches, create a separate payment location for each one.

```curl
curl https://api.stripe.com/v1/payment_locations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d "display_name=Pasta Paradise Paris" \
  -d "address[line1]=999 Rue de Rivoli" \
  -d "address[city]=Paris" \
  -d "address[postal_code]=75001" \
  -d "address[country]=FR" \
  -d "business_registration[siret]=29009360804163"
```

The API returns a `PaymentLocation` object:

```json
{
  "id": "loc_12345",
  "object": "payment_location",
  "display_name": "Pasta Paradise Paris",
  "address": {
    "line1": "999 Rue de Rivoli",
    "city": "Paris",
    "postal_code": "75001",
    "country": "FR"
  },
  "business_registration": {
    "siret": "29009360804163"
  },
  "capability_settings": {
    "fr_meal_vouchers_conecs_payments": {
      "supported_issuers": {
        "card": [],
        ...
      }
    },
    ...
  },
  ...
}
```

Save the `id` (for example, `loc_12345`). You need it to request onboarding and to create PaymentIntents.

> The SIRET and postal code must match the restaurant’s registration with the CNTR. You can’t change the `country` field after you create the location.

## Request the meal vouchers capability

To onboard the location for French meal vouchers payments, request the `fr_meal_vouchers_conecs_payments` [PaymentLocationCapability](https://docs.stripe.com/api/payment-location-capability.md?api-version=2026-05-27.preview) on your payment location. You don’t need to complete account-level onboarding steps for French meal vouchers—each physical location onboards individually.

```curl
curl https://api.stripe.com/v1/payment_location_capabilities/fr_meal_vouchers_conecs_payments \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d location=loc_12345 \
  -d requested=true
```

The API returns a `PaymentLocationCapability` object with `status: "pending"` and `requirements[disabled_reason]: "pending.onboarding"` while Stripe processes the onboarding request with Conecs. This process takes 1–2 business days.

```json
{
  "capability": "fr_meal_vouchers_conecs_payments",
  "object": "payment_location_capability",
  "account": "acct_12345",
  "location": "loc_12345",
  "requested": true,
  "requirements": {
    "currently_due": [],
    "disabled_reason": "pending.onboarding",
    "errors": []
  },
  "status": "pending"
  ...
}
```

## Monitor onboarding status

Monitor the onboarding status to know when the location is ready to accept payments or when issues need your attention. You can either poll the API or listen to webhook events.

### Poll the API

Retrieve the capability to check whether onboarding has completed:

```curl
curl -G https://api.stripe.com/v1/payment_location_capabilities/fr_meal_vouchers_conecs_payments \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d location=loc_12345
```

When onboarding succeeds, the `status` changes to `active`:

```json
{
  "capability": "fr_meal_vouchers_conecs_payments",
  "object": "payment_location_capability",
  "account": "acct_12345",
  "location": "loc_12345",
  "requested": true,
  "requirements": {
    "currently_due": [],
    "disabled_reason": null,
    "errors": []
  },
  "status": "active"
  ...
}
```

### Listen to webhooks

Listen to webhook events to receive notifications when the onboarding status changes:

- `payment_location_capability.updated`: Sent when the capability’s `status` or `requirements` change.
- `payment_location.updated`: Sent when the list of supported issuers for the PaymentLocation changes.

These events can arrive independently. Conecs can provide the list of supported issuers before onboarding is fully complete, so you might receive a `payment_location.updated` event before the capability becomes `active`. The `supported_issuers` arrays reflect which issuers are available for the location:

```json
{
  "id": "evt_12345",
  "object": "event",
  "type": "payment_location.updated",
  "data": {
    "object": {
      "id": "loc_12345",
      "object": "payment_location",
      "capability_settings": {
        "fr_meal_vouchers_conecs_payments": {
          "supported_issuers": {
            "card": ["up", "bimpli", "pluxee"],
            ...
          }
        }
      }
      ...
    }
  }
  ...
}
```

You can [accept French meal vouchers payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md) for a location as soon as the capability status is `active`.

## Optional: Resolve outstanding requirements

If monitoring reveals that the capability has outstanding requirements, resolve them to continue the onboarding process. Stripe validates the location data before sending the onboarding request to Conecs, and Conecs can also return errors after submission. In both cases, the capability’s `requirements.currently_due` array lists what needs to be fixed and `requirements.errors` explains why.

For example, if the SIRET is missing, you receive:

```json
{
  "capability": "fr_meal_vouchers_conecs_payments",
  "object": "payment_location_capability",
  "requirements": {
    "currently_due": ["business_registration.siret"],
    "disabled_reason": "requirements.fields_needed",
    "errors": [
      {
        "requirement": "business_registration.siret",
        "code": "information_missing",
        "reason": "SIRET number is missing in the location."
      }
    ]
  },
  "status": "pending",
  ...
}
```

To resolve this, update the payment location with the correct value:

```curl
curl https://api.stripe.com/v1/payment_locations/loc_12345 \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d "business_registration[siret]=29009360804163"
```

After you provide the required data, Stripe automatically resumes the onboarding process.

If the postal code doesn’t match the SIRET registered with the CNTR, you receive:

```json
{
  "capability": "fr_meal_vouchers_conecs_payments",
  "object": "payment_location_capability",
  "requirements": {
    "currently_due": ["address.postal_code"],
    "disabled_reason": "requirements.fields_needed",
    "errors": [
      {
        "requirement": "address.postal_code",
        "code": "invalid_value_other",
        "reason": "The postal_code provided doesn't match the siret provided. Update the postal_code on this Location."
      }
    ]
  },
  "status": "pending",
  ...
}
```

To resolve this, update the location with the correct postal code.

If the SIRET doesn’t exist or the restaurant doesn’t have CNTR approval, you receive:

```json
{
  "capability": "fr_meal_vouchers_conecs_payments",
  "object": "payment_location_capability",
  "requirements": {
    "currently_due": ["business_registration.siret"],
    "disabled_reason": "requirements.fields_needed",
    "errors": [
      {
        "requirement": "business_registration.siret",
        "code": "invalid_value_other",
        "reason": "The siret provided either doesn't exist or the restaurant hasn't obtained approval from the CNTR to accept meal vouchers in France. Refer to https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers#requirements for more information."
      }
    ]
  },
  "status": "pending",
  ...
}
```

To resolve this, confirm the SIRET is correct. If the SIRET is wrong, update the location with the correct value. If the restaurant hasn’t completed CNTR registration yet, no location update is required—Stripe automatically resumes onboarding after Conecs processes the registration.

## Optional: Update location data after onboarding

After a location onboards, certain field changes (such as updating the SIRET or address) trigger a new onboarding review and temporarily suspend the capability. Stripe blocks these updates by default to prevent accidental disruptions.

If you attempt to update an onboarding-relevant field without acknowledging this, you receive an error:

```json
{
  "error": {
    "type": "invalid_request_error",
    "message": "Unable to update business_registration[siret] as it might affect Location Capabilities for this Location."
  }
}
```

To confirm the update and accept that it will trigger a new onboarding review, include `onboarding_data_update_acknowledged=true`:

```curl
curl https://api.stripe.com/v1/payment_locations/loc_12345 \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d "business_registration[siret]=42424242424242" \
  -d onboarding_data_update_acknowledged=true
```

During re-onboarding, the location’s capability status reverts to `pending` and you can’t accept meal vouchers payments until the new onboarding completes.

## Optional: Set up a restaurant with Connect

For Connect platforms where the connected account is the merchant of record (for example, direct charges or destination charges with `on_behalf_of`), create the payment location and request the capability on behalf of the connected account using the `Stripe-Account` header.

```curl
curl https://api.stripe.com/v1/payment_locations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "display_name=Pasta Paradise Lyon" \
  -d "address[line1]=5 Place Bellecour" \
  -d "address[city]=Lyon" \
  -d "address[postal_code]=69002" \
  -d "address[country]=FR" \
  -d "business_registration[siret]=29009360804163"
```

Then request the capability for that connected account:

```curl
curl https://api.stripe.com/v1/payment_location_capabilities/fr_meal_vouchers_conecs_payments \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d location=loc_67890 \
  -d requested=true
```

Learn more about [making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md) and the [Connect guide for French meal vouchers](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect.md).

## Test your integration 

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), Stripe simulates the Conecs onboarding process without making a real network call. A capability moves to `active` as soon as all required location fields are valid.

Use the following SIRET and postal code combinations to test different onboarding scenarios:

| SIRET | Postal code | Resulting status | Notes |
| --- | --- | --- | --- |
| `42424242842427` | `75009` | `active` | Valid onboarded restaurant |
| `42424242842427` | Any valid postal code other than `75009` | `pending` (`requirements.fields_needed`) | Postal code doesn’t match the SIRET |
| Any other valid SIRET | Any valid postal code | `pending` (`requirements.fields_needed`) | SIRET either doesn’t exist or the restaurant doesn’t have CNTR approval |

The test SIRET and postal code combinations above simulate the errors described in [Resolve outstanding requirements](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md#resolve-requirements).

## Next steps 

After onboarding your restaurant, you can:

- [Accept French meal vouchers payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md) for the location.
- [Accept French meal vouchers payments with Connect](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect.md) if you’re using a Connect platform.
