<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Ordering a Product
slug: /docs/guides/paypal-commerce-channel-api/ordering-a-product/
createTime: '2025-04-02T00:02:50.527Z'
updateTime: '2025-04-02T00:02:50.590Z'
---



# Ordering a Product

To order a product for a user, you'll go through the following flow:
- [Obtain and store payment information](#obtaining-and-storing-payment-information)
- [Obtain a shipping address](#obtaining-a-shipping-address)
- [Obtain the full cost](#obtaining-the-full-cost)
- [Create the order using a customer access token](#creating-an-order)
- [Initiate the purchase](#initiating-the-purchase)


## Obtaining and storing payment information

The Channel API leverages[Braintree SDKs](/braintree/docs/start/overview)to provide
safe, secure, and flexible payments. You'll need to provide a[payment_method_token](/braintree/docs/guides/payment-methods)when you[initiate the purchase](#initiating-the-purchase).
## Obtaining a shipping address

In order for a user to purchase a product, they must also supply a shipping address. This is
important both for the retailer to get the product to the user and for us to calculate the
appropriate taxes and shipping costs. A shipping address can have the following components:| Parameter | Status | Example |
| --- | --- | --- |
| first_name | optional | "Clinton" |
| last_name | optional | "Ecker" |
| street_address | required | "1234 Main Street" |
| extended_address | optional | "Unit 222" |
| locality | required | "Chicago" |
| region | required | "IL" |
| postal_code | required | "60654" |
| country_code_alpha2 | required | "US" |
| phone_number | optional | "+1-312-234-5678" |


## Obtaining the full cost

Up to this point, the user only knows about the "base cost" of the product variant – not the full
cost including any discounts, taxes, and shipping. Before creating an order, we strongly recommend
determining the full cost and presenting it to the user. Not performing this task can lead to
confusion, chargebacks, and generally a bad user experience. To obtain the full cost of purchasing a
given variant, make a request to the single variant endpoint and include the query string
parameters:
- postal_code,country_code_alpha2to indicate the destination (required)
- promo_codesto see if any discounts can be applied (optional)

These parameters allow the Channel API to determine:
- whether or not the retailer ships to the requested location
- what taxes and shipping costs would be assessed if the product were actually purchased
- whether the given promo codes are valid, and if so, what the total cost would be after the discount

If the product can be shipped to the requested location, the response will include cost information
under thecostsproperty. If the retailer doesn't ship to the requested location (e.g.
they don't ship internationally, or only ship to certain international destinations), theshippableproperty will befalse. Promo codes are optional when obtaining
the full cost of the product. If the given promo codes are valid, the response will includediscountinformation under thecostsproperty. If the retailer doesn't
support the promo codes, you'll receive a response with a 404 status code.
### bash
```bash
curl "https://commerce.sandbox.braintreegateway.com/channel/variants/BLACK-RUNNING-SHOES-11?postal_code=94301&country_code_alpha2=us&promo_codes="10OFF,FALL25"" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json"
```

### http
```http
HTTP/1.1 200 OK

{
    "data": {
        "current_price": "99.00",
        "description": "Black Running Shoes really increase your speed.",
        "features": {
            "Color": "Black",
            "Size": "11"
        },
        "inventory_quantity": 999999,
        "name": "Black Running Shoes",
        "photos": [
            {
                "image_url": "http://i.imgur.com/5hZVUWy.jpg",
                "images": [
                    {
                        "height": 1440,
                        "mime_type": "image/jpeg",
                        "source": "http://i.imgur.com/5hZVUWy.jpg",
                        "width": 1920
                    },
                    {
                        "height": 1440,
                        "mime_type": "image/jpeg",
                        "source": "http://i.imgur.com/5hZVUWy.jpg",
                        "width": 1920
                    },
                    {
                        "height": 1440,
                        "mime_type": "image/jpeg",
                        "source": "http://i.imgur.com/5hZVUWy.jpg",
                        "width": 1920
                    }
                ]
            }
        ],
        "sku": "BLACK-RUNNING-SHOES-11",
        "upc": "U\u1e54C-6",
        "url": null
    },
    "meta": {
        "costs": {
            "shipping": "5.95",
            "tax": "0.00",
            "total_cost": "102.95",
            "discount_total": "2.00",
            "variant_price": "99.00"
        },
        "shippable": true
    }
}
```
If theSKUdoesn't exist in our records, you'll receive a response with a 404 status
code.
### bash
```bash
curl "https://commerce.sandbox.braintreegateway.com/channel/variants/NOT-A-VALID-SKU?postal_code=94301&country_code_alpha2=us" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json"
```

### http
```http
HTTP/1.1 404 NOT FOUND

{
    "data": "A product with the given SKU does not exist in this store.",
    "errors": {
        "product_not_found": "A product with the given SKU does not exist in this store."
    }
}
```

## Creating an order

Once the customer has seen the full cost and decided to make the purchase, you'll need to obtain acustomer access tokenbefore initiating the purchase. These tokens are specific to your
channel and the retailer, and they work in the same way as the[access tokens you use for other calls](/braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token). The only major difference is that they allow you to operate in the context of a particular user.
### Obtaining a customer access token

To obtain a token for a user, first ensure you have a unique customer ID for each of your users.
Generally a username or numerical identifier works just fine. Next, send aPOSTto/tokenin the same way you did for the retailer-specific access token, but this time
include thecustomer_id:
### bash
```bash
curl -X POST https://commerce.sandbox.braintreegateway.com/channel/token \
    -H "Content-Type: application/json" \
    -d '{
        "client_id": "'"$PARTNER_CLIENT_ID"'",
        "client_secret": "'"$PARTNER_CLIENT_SECRET"'",
        "retailer_domain": "'"$RETAILER_DOMAIN"'",
        "customer_id": "clint.ecker"
    }'
```
The API will return a response containing a customer access token, as well as how long the token
will be valid (in seconds):
### http
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "access_token": "AAABBCCCDD...",
  "expires_in": 7200
}
```
As before, you can cache this token and refresh it upon expiration (or on a schedule ahead of
expiration that suits your needs).
## Initiating the purchase

Once you have a customer access token, you can initiate the purchase. Your request body must include
anorderobject containing the following properties:
- partner_order_id: An external identifier for the order
- variant: Askuproperty for the variant to be purchased, and an optionalquantityproperty
- shipping_address: The shipping destination
- payment_method: The token representing the vaulted payment method
- promo_codes: An optional comma-separated list of promo codes to be applied

Here's what a sample request looks like:
### bash
```bash
curl -X POST https://commerce.sandbox.braintreegateway.com/channel/orders \
-H "Authorization: Bearer $CUSTOMER_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "order": {
    "partner_order_id": "or_2293",
    "variant": {
      "sku": "'$SKU'",
      "quantity": 2
    },
    "shipping_address": {
      "first_name": "Clinton",
      "last_name": "Ecker",
      "street_address": "222 W Merchandise Mart Plaza",
      "extended_address": "Suite 800",
      "locality": "Chicago",
      "region": "IL",
      "postal_code": "60647",
      "country_code_alpha2": "US",
      "phone_number": "312-833-1946"
    },
    "payment_method": {
      "payment_method_token": "'$PAYMENT_METHOD_TOKEN'"
    },
    "promo_codes": ["10OFF", "FALL25"]
  }
}'
```
Upon success, the API will return a response that includes an HTTP status code of 201 and the full
cost information associated with the order:
### http
```http
HTTP/1.1 201 CREATED
Content-Type: application/json

{
  "data": {
    "partner_order_id": "or_2293",
    "variant_price": "31.98",
    "quantity": 2,
    "shipping_cost": "5.00",
    "tax_cost": "0.27",
    "discount_total": "2.00",
    "total_cost": "67.50"
  }
}
```

**NOTE**
If anything went wrong during the purchasing process, you will receive a 400-499 error code. See [Handling Error Responses](/braintree/docs/guides/paypal-commerce-channel-api/handling-error-responses) for more details.

From here, our system will transmit the order to the retailer's ecommerce system where it will be
marked as ready to fulfill.