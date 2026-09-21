<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/handling-error-responses -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Handling Error Responses
slug: /docs/guides/paypal-commerce-channel-api/handling-error-responses/
createTime: '2025-04-02T00:17:48.368Z'
updateTime: '2025-04-02T00:17:48.382Z'
---



# Handling Error Responses

An API response with an HTTP status code other than a 2XX indicates an error. In general, if you
receive a client error (4XX), you should update the request before retrying it. Client errors
include (but are not limited to):| Code | Error | Description |
| --- | --- | --- |
| 400 | product_quantity_not_available | Product is out of inventory |
| 400 | store_does_not_ship_to_destination | Product is not shippable to the requested destination |
| 400 | payment_method_authorization_failed | Payment method authorization failed |
| 400 | address_missing_required_fields | Shipping address is missing required fields |
| 400 | invalid_post_body | Request body is not formatted correctly |
| 403 | forbidden | Access token has expired or retailer has revoked access |
| 404 | product_not_found | Product with the given SKU does not exist in this store |

