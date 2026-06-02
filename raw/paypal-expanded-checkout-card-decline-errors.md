<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/card-decline-errors/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Card decline errors
slug: /docs/checkout/advanced/card-decline-errors/
createTime: '2024-10-30T13:59:00.317Z'
updateTime: '2025-05-14T09:22:36.923Z'
---


# Card decline errors

To understand why a card payment was declined, the Orders v2 API processor_response object includes values returned for card transactions.

The following tables list possible AVS and CVV error response decline values and descriptions.



## Error response codes 
Visa, Mastercard, Discover, and American Express use the same alphabetical AVS and CVV error codes. Maestro uses numeric AVS and CVV error codes.


### Visa, Mastercard, Discover, American Express

#### AVS Error

| AVS Code | Meaning | Matched details |
| --- | --- | --- |
| A | Address | Address only (no ZIP code) |
| B | International "A" | Address only (no ZIP code) |
| C | International "N" | None. The transaction is declined. |
| D | International "X" | Address and Postal Code |
| E | Not allowed for MOTO (Internet/Phone) transactions | Not applicable. The transaction is declined. |
| F | UK-specific "X" | Address and Postal Code |
| G | Global Unavailable | Not applicable |
| I | International Unavailable | Not applicable |
| M | Address | Address and Postal Code |
| N | No | None. The transaction is declined. |
| P | Postal (International "Z") | Postal Code only (no Address) |
| R | Retry | Not applicable |
| S | Service not Supported | Not applicable |
| U | Unavailable | Not applicable |
| W | Whole ZIP | Nine-digit ZIP code (no Address) |
| X | Exact match | Address and nine-digit ZIP code |
| Y | Yes | Address and five-digit ZIP |
| Z | ZIP | Five-digit ZIP code (no Address) |
| All others | Error | Not applicable |


#### CVV Error

| CVV2 Code | Meaning | Matched details |
| --- | --- | --- |
| E | Error - Unrecognized or Unknown response | Not applicable |
| I | Invalid or Null | Not applicable |
| M | Match | CVV or CSC |
| N | No match | None |
| P | Not processed | Not applicable |
| S | Service not supported | Not applicable |
| U | Unknown - Issuer is not certified | Not applicable |
| X | No response | Not applicable |
| All others | Error | Not applicable |


### Maestro

#### AVS Error

| AVS Code | Meaning | Matched details |
| --- | --- | --- |
| 0 | All the address information matched. | All information matched |
| 1 | None of the address information matched. | None. The transaction is declined. |
| 2 | Part of the address information matched. | Partial |
| 3 | The merchant did not provide AVS information. Not processed. | Not applicable |
| 4 / U (either a number or a letter is returned) | Address not checked, or acquirer had no response. Service not available. | Not applicable |
| Null | No AVS response was obtained. Default value of field. | Not applicable |


#### CVV Error

| CVV2 Code | Meaning | Matched details |
| --- | --- | --- |
| 0 | Matched | CVV2 |
| 1 | No match | None |
| 2 | The merchant has not implemented CVV2 code handling | Not applicable |
| 3 | Merchant has indicated that CVV2 is not present on card | Not applicable |
| 4 / X (either a number or a letter is returned) | Service not available | Not applicable |
| All others | Error | Not applicable |


## See Also 

- Orders response object: Processor response object for the Orders v2 API — /docs/api/orders/v2/#definition-processor_response
- Orders errors: Details about errors for the Orders v2 API — /api/rest/reference/orders/v2/errors/
