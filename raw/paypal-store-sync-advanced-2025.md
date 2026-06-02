<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/advanced-use-cases -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced use cases

To extend your API beyond basic product sales, you can enable specialized shopping experiences. This guide shows you how to:

- Handle gift cards with recipient information and delivery scheduling.
- Use geographic coordinates for location-aware services, such as local-inventory checking and delivery-radius validation.

> **Note:** You can view the complete protocol reference for the [Cart API](/reference/api/rest/cart-operations/create-cart/) and the [Complete Checkout API](/reference/api/rest/checkout-operations/complete-checkout/).

## Gift cards

Create a cart containing a gift card with recipient details and scheduled delivery.

```bash lines expandable theme={null}
POST /api/paypal/v1/merchant-cart
Content-Type: application/json
Authorization: Bearer <paypal-jwt-token>

{
  "items": [
    {
      "variant_id": "GIFTCARD-100",
      "quantity": 1,
      "gift_options": {
        "is_gift": true,
        "recipient": {
          "name": "Mary Johnson",
          "email": "mary@example.com"
        },
        "delivery_date": "2024-12-25T09:00:00Z",
        "sender_name": "John Smith",
        "gift_message": "Merry Christmas! Enjoy your shopping."
      }
    }
  ],
  "payment_method": {
    "type": "paypal"
  }
}
```

## Geographic coordinates

Some merchants offer location-based services that require precise geographic positioning beyond standard postal addresses. The Cart API supports optional latitude/longitude coordinates to enable features like local inventory checking, distance-based pricing, delivery radius validation, and enhanced shipping calculations. This geographic data operates independently from shipping addresses, allowing you to provide location-aware commerce experiences while maintaining clean separation between postal and coordinate data.

### Latitude and longitude support strategy

Geographic coordinates are optional. This feature is for merchants who can provide enhanced location services.
Geographic coordinates are provided in a separate `geo_coordinates` field, distinct from the `shipping_address` object. This clean separation allows:

- Postal addresses to remain focused on standard shipping data
- Geographic coordinates to provide precise location enhancement
- Independent handling of address and coordinate data
- Graceful degradation when coordinates aren't supported

Here's how to structure address and coordinate data separately:

```json lines expandable theme={null}
{
  "shipping_address": {
    "address_line_1": "123 Main Street",
    "admin_area_2": "San Jose",
    "admin_area_1": "CA",
    "postal_code": "95131",
    "country_code": "US"
  },
  "geo_coordinates": {
    "latitude": "37.3349",
    "longitude": "-122.0090",
    "subdivision": "CA",
    "country_code": "US"
  }
}
```

### Geographic fields

The `geo_coordinates` object contains precise location data that enhances address information for location-aware services.

| Field                      | Description                                                               | Example                                       |
| -------------------------- | ------------------------------------------------------------------------- | --------------------------------------------- |
| `latitude` and `longitude` | Precise WGS84 coordinates in decimal degrees                              | `latitude: "37.3349", longitude: "-122.0090"` |
| `subdivision`              | Administrative division (state, province, region) using ISO 3166-2 format | `subdivision: "CA"` (California)              |
| `country_code`             | ISO 3166-1 alpha-2 country code for the coordinate location               | `country_code: "US"`                          |
