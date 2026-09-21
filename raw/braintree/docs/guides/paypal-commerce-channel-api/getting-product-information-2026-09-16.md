<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/getting-product-information -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Getting Product Information
slug: /docs/guides/paypal-commerce-channel-api/getting-product-information/
createTime: '2025-04-02T00:15:07.014Z'
updateTime: '2025-04-02T00:15:07.040Z'
---



# Getting Product Information

Once you've obtained a retailer-specific access token, you can get information about that retailer's
products. Each product will have its own features – different colors, sizes, textures, etc. A
product variant represents one combination of the available features, and each variant has its own
SKU, or unique identifier. You can search products by SKU, URL, name, and description.
- ?sku=ABC123: Queries for the product containing a specific SKU
- ?url=https%3A%2F%2Fexample.com%2F/product: Queries for the products of a specific URL
- ?q=boots: Queries for the name and description fields of products
- ?name=shoes: Queries for the name field only

Our sample retailer (YOUR_BRAINTREE_MERCHANT_ID.retailer.com) sells four kinds of
footwear: black running shoes, blue hiking boots, red cowboy boots, and red sneakers. The following
search will return all of the black running shoe variants:
### bash
```bash
curl https://commerce.sandbox.braintreegateway.com/channel/products?q=black \
-H "Authorization: Bearer $ACCESS_TOKEN" \
-H "Content-Type: application/json"
```
The response is a list of products, each of which has a list of variants. Each variant has a unique
SKU. Choose one when you're ready to[initiate a purchase](/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product#initiating-the-purchase).
### http
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "data": [
        {
            "category_slugs": [],
            "description": "The best shoes you can buy",
            "features": {
                "Color": ["Black"],
                "Size": ["10", "11", "9"]
            },
            "high_price": "99.00",
            "high_suggested_price": "17.50",
            "in_stock": true,
            "low_price": "99.00",
            "low_suggested_price": "17.50",
            "name": "Shoes",
            "product_type_name": null,
            "requires_shipping": true,
            "web_buy_link": "https://www.paypal-commerce.com/retailer/product/RN-FA-MSQiWs_25Txl20Pw",
            "variants": [
                {
                    "current_price": "99.00",
                    "description": "Black Running Shoes really increase your speed.",
                    "features": {
                        "Color": "Black",
                        "Size": "9"
                    },
                    "inventory_quantity": 999999,
                    "name": "Black Running Shoes",
                    "photos": [
                        {
                            "image_url": null,
                            "images": [
                                {
                                    "height": 1440,
                                    "mime_type": "image/jpeg",
                                    "source": "http://i.imgur.com/5hZVUWy.jpg",
                                    "width": 1920
                                }
                            ]
                        }
                    ],
                    "sku": "BLACK-RUNNING-SHOES-9",
                    "upc": "U\u1e54C-4",
                    "url": null
                },
                {
                    "current_price": "99.00",
                    "description": "Black Running Shoes really increase your speed.",
                    "features": {
                        "Color": "Black",
                        "Size": "10"
                    },
                    "inventory_quantity": 999999,
                    "name": "Black Running Shoes",
                    "photos": [
                        {
                            "image_url": null,
                            "images": [
                                {
                                    "height": 1440,
                                    "mime_type": "image/jpeg",
                                    "source": "http://i.imgur.com/5hZVUWy.jpg",
                                    "width": 1920
                                }
                            ]
                        }
                    ],
                    "sku": "BLACK-RUNNING-SHOES-10",
                    "upc": "U\u1e54C-5",
                    "url": null
                },
                {
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
                            "image_url": null,
                            "images": [
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
                }
            ]
        }
    ],
    "meta": {
        "count": 1
    }
}
```
If there are no matching products, the endpoint will return an empty collection. There are two
critical properties to keep track of here:
- thein_stockproperty
- theskufor each variant

If a user decides to place an order, you will need to pass along the SKU for the specific variant
they selected. You can cache these results for up to a few minutes. If you move on to[ordering a product](/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product), you'll get up-to-date product information when obtaining the full cost. You will also see aweb_buy_linkon each product. This is a URL for purchasing the product through PayPal
Commerce's web client. You can provide these links directly to customers as an alternative to
constructing your own purchasing experience.