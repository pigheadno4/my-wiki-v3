<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/integrate/ -->
<!-- Fetched: 2026-04-13 -->

---
title: 'Integrate Chargeback Protection '
slug: /docs/checkout/advanced/customize/chargeback-protection/integrate/
createTime: '2025-06-03T12:55:08.204Z'
updateTime: '2025-06-11T13:28:48.482Z'
---


# Integrate Chargeback Protection 

PayPal's Chargeback Protection Tool provides security against fraudulent transactions by defending eligible disputes. The tool requires specific integration requirements and mandatory fields to effectively identify and mitigate fraud risk.



## Know before you code 


- Have a [PayPal business account](https://www.paypal.com/unifiedonboarding/entry?country.x=US&locale.x=en_US) .
- Activate the [Chargeback Protection Tool](https://www.paypal.com/manage-risk-hub/) .
- You will need to have an existing [Expanded Checkout](https://developer.paypal.com/studio/checkout/advanced) integration.



## Integration requirements 
Integrate with either [JavaScript SDK](https://developer.paypal.com/sdk/js/) or [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) integrations to create and capture orders.

 

## Field descriptions
The Chargeback Protection Tool requires a set of mandatory fields.

The following table shows the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) parameters to passto reduce fraudulent transactions using the Chargeback Protection Tool.

 

### Create order
Pass the following fields when you send a [Capture order](https://developer.paypal.com/docs/api/orders/v2/#orders_create) request.

| Field name | Description | Type | Notes | Priority |
| payer.name | The name of the payer. Supports only thegiven_nameand surname properties. See the[parameter defintion](https://developer.paypal.com/docs/api/orders/v2/#orders_create!ct=application/json&path=payer/name&t=request)for more information. | object |  | Recommended |
| purchase_units.shipping.address | The address of the person receiving the items. Supports only theaddress_line_1,address_line_2,admin_area_1,admin_area_2,postal_code, andcountry_codeproperties. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_create!ct=application/json&path=purchase_units/shipping/address&t=request)for more information. | object | Recommended for intangible goods | Mandatory |

 

### Capture order
Pass the following fields when you send a [Capture payment for order](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) request

| Field name | Description | Type | Notes | Priority |
| payment_source.card.number | The primary account number (PAN) for the payment card. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!ct=application/json&path=payment_source/card/number&t=request)for more information. | string | - Minimum characters: 13
- Maximum characters: 19 | Mandatory |
| payment_source.card.name | The cardholder's name as it shows up on the card. See the[parameter defintion](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!ct=application/json&path=payment_source/card/name&t=request)for more information. | string | - Minimum characters: 1
- Maximum characters: 300 | Mandatory |
| payment_source.card.attributes.customer.email_address | Email address of the merchant as provided to the merchant or on file with the merchant. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!ct=application/json&path=payment_source/card/attributes/customer/email_address&t=request)for more information. | string | - Minimum characters: 3
- Maximum characters: 254
- Pattern: (?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) | Mandatory |
| payment_source.card.attributes.customer.phone | The phone number of the customeras provided to the merchant or on file with the merchant. Thephone.phone_numbersupports onlynational_number. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!ct=application/json&path=payment_source/card/attributes/customer/phone&t=request)for more information. | object |  | Recommended |
| payment_source.card.billing_address | The billing address for the card. Supports only theaddress_line_1,address_line_2,admin_area_1,admin_area_2,postal_code, andcountry_codeproperties. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!ct=application/json&path=payment_source/card/billing_address&t=request)for more information. | object |  | Mandatory |
| PayPal-Client-Metadata-Id | A unique key that identifies risk data. See the[parameter definition](https://developer.paypal.com/docs/api/orders/v2/#orders_capture!in=header&path=PayPal-Client-Metadata-Id&t=request)for more information. | string | - Minimum characters: 1
- Maximum characters: 36 | Mandatory |



## Google Pay and Apple Pay fields 
For Google or Apple Pay transactions, fields should be passed through the JavaScript SDK instead of Orders V2 API request. See [GooglePay](https://developer.paypal.com/docs/checkout/apm/google-pay/) and [Apple Pay](https://developer.paypal.com/docs/checkout/apm/apple-pay/) integration guides for more details about setting up your integration. Pass the following fields through the SDK:

| Field name | Description | Priority |
| Buyer credit card | The card number that includes the Device Primary Account Number (DPAN)and the credit card hash. | Mandatory |
| Cardholder name | The cardholder's name. | Mandatory |
| Buyer name | The buyer's name. | Recommended |
| Buyer email | The buyer's email address. Ensure this entry is notnullor–999. | Mandatory |
| Buyer phone | The buyer's phone number. Ensure this entry is notnullor–999. | Recommended |
| Buyer billing address | Billing address for the transaction. Ensureaddress_line1andaddress_cityare not blank and contain a valid input. | Mandatory |
| Buyer shipping address | This is the buyer's shipping address. Ensureaddress_line1andaddress_cityare not blank and contain a valid input. You may lose dispute eligibility and Chargeback Protection coverage if you don't provide a valid shipping address. | Mandatory for tangible goods and recommended for intangible goods |
| RDA key | A unique key that identifies risk data. | Mandatory |
| Xclick item information | Contains information about the item purchased. | Recommended |
| Auto submit evidence for charegeback protection | Shipping ID, tracking ID, and additional evidence. See the[Proof of delivery](https://www.paypal.com/us/legalhub/paypal/seller-protection#proof-delivery)policy for more information. | Recommended |



## Submit evidence for protected disputes 
To submit shipping or tracking information and any additional evidence as required by policy, see the following steps:

- Subscribe to the CUSTOMER.DISPUTE.CREATED webhook to receive a notification when a dispute is created. The payload includes the dispute.id .
- Use the dispute.id to retrieve dispute details and determine the appropriate action.
- In the API response, check the following path to verify protection coverage: response.adjudications.reason.PROTECTION_POLICY_APPLIES . See [Get started with PayPal REST APIs](https://developer.paypal.com/api/rest/) for dispute details.
- If the dispute is protected under the Chargeback Protection Tool, submit the evidence by following the request.evidence-file path. See [Get started with PayPal REST APIs](https://developer.paypal.com/api/rest/) to learnto upload evidence.



## Resources 
- Be sure to onboard to the [Chargeback Protection Tool](https://www.paypal.com/manage-risk-hub/) , and integrate with [Advanced Credit and Debit Card](https://developer.paypal.com/studio/checkout/advanced/integrate) processing before testing this integration.
- Use the [Chargeback Protection Integration Health Dashboard](https://www.paypal.com/cbp-tool-dashboard/integration) to check your integration details.
- For more information on Chargeback Protection Tool options, see the [Chargeback Protection Tool overview](https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/) .
- For more information on items or transactions not eligible for PayPal's Chargeback Protection program, see [Ineligible Items and Transactions](https://www.paypal.com/us/legalhub/paypal/seller-protection?locale.x=en_US#ineligible-items) .
