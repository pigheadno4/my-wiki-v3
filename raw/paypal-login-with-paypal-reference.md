<!-- Source URL: https://developer.paypal.com/docs/log-in-with-paypal/integrate/reference/ -->

## <!-- Fetched: 2026-04-16 -->

title: Log in with PayPal reference
slug: /docs/log-in-with-paypal/integrate/reference/
createTime: '2024-08-15T06:17:56.878Z'
updateTime: '2025-08-04T17:27:59.236Z'

---

# Log in with PayPal reference

## Scope attributes

The following shows how user attributes map to OpenID Connect protocols:

| User attribute               | Category             | Scope value                                                                                                                       |
| ---------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| None                         | Basic Authentication | openid                                                                                                                            |
| Full name                    | Personal Information | profile                                                                                                                           |
| Email address                | Address Information  | email                                                                                                                             |
| Street address               | Address Information  | address                                                                                                                           |
| City                         | Address Information  | address                                                                                                                           |
| State                        | Address Information  | address                                                                                                                           |
| Country                      | Address Information  | address                                                                                                                           |
| Zip code                     | Address Information  | address                                                                                                                           |
| Account verification status  | Account Information  | https://uri.paypal.com/services/paypalattributes Shows if the customer has a verified PayPal account.                             |
| PayPal account ID (payer ID) | Account Information  | https://uri.paypal.com/services/paypalattributes The user's unique PayPal account ID used in PayPal APIs such as the Payouts API. |
