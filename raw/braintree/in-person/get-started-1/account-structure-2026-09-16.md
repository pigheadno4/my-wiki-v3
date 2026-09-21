<!-- Source URL: https://developer.paypal.com/braintree/in-person/get-started-1/account-structure -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Account Structure
slug: /in-person/get-started-1/account-structure/
createTime: '2024-11-20T19:02:45.122Z'
updateTime: '2025-01-24T00:52:25.150Z'
---



# Account Structure

This section discusses the various possibilities of account structure and the Braintree account hierarchy.


## Braintree Account Hierarchy

**NOTE**
Click on the expandable boxes below to learn more about what functions are available at each tier of the account structure!


### Gateway Account

The Braintree platform has primarily two account tiers. At the highest level is the [Braintree Gateway Account](/braintree/articles/control-panel/important-gateway-credentials#merchant-id) or sometimes referred to as a "Merchant ID" or "Public ID" or "Production ID". The Braintree Gateway Account can house multiple merchant accounts.

Braintree Gateway Account
- Umbrella account that encompasses multiple merchant accounts, a shared token vault, aggregated reporting, etc...




### Merchant Account ID

The Braintree [Merchant Account ID](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id) or sometimes referred to as the "Merchant Account ID" or "MAID" is an account tier that can be used to represent different channels of your business. This could be for an E-commerce site, a B2B wholesale channel, a Mobile app, or an in-store Retail channel. Within the Retail channel, there may be multiple brands or physical store locations. The Braintree Merchant Account has a great amount of flexibility in what it can represent, please take a look at some of the [considerations](#account-structure-considerations) to make while determining your account structure.

Braintree Merchant Account
- Bank account for disbursements are configured at the merchant account level


- Settlement reporting is generated at this account level


- Some configurations can be managed at this account level


- User access and permissions can be managed at this account level


- AMEX Service Establishment numbers are configured at this level


- Invoicing occurs at the merchant account level


- MCC code configured at merchant account level



**NOTE**
 [Click here](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id-versus-merchant-id) for more information on the difference between a "Merchant ID" and a "Merchant Account ID"


### Location ID

The [Location ID](/braintree/in-person/guides/setup-reader#create-location-id) is a layer in the account structure that is really a flexible "virtual-only" account layer. This is the layer in which the readers are paired to and where certain functionality is enabled, such as PayPal and Venmo in-person [QR code payments](/braintree/in-person/guides/paypal-and-venmo-qrc/). Typically, the location ID should represent a single store location where the readers are physically located.

Location ID
- Card readers are paired at the location ID level


- PayPal and Venmo [QRC](/braintree/in-person/guides/paypal-and-venmo-qrc) are enabled at this level


- Multiple card readers can be paired to the same location ID


- A card reader can only be paired to a single location ID at a time


- The location ID does NOT appear in any Braintree reporting. For location-level reporting in a single MAID see our [reporting docs](/braintree/in-person/guides/reporting-and-reconciliation/#using-the-order-id-field-to-reconcile-with-braintree-settlement-reports)


- Card reader screensaver/idle screen images can be configured at the location ID level




#### Take a look at the below diagram of the Braintree Account Structure variations:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Get-started:Account:Location_ID.png)The diagram on the left represents the "one MAID per store" structure. The diagram on the right depicts the "one MAID for all stores" structure.
## One MAID per store VS One MAID for all stores

The table below illustrates the various implications of having either the one MAID per store account structure or using one MAID for all (or multiple stores).

|  | **Merchant account for each store** | **Merchant account for each brand** |
| **Funds Disbursement** | One bank transfer for each (physical) store. | One bank transfer for each brand. |
| **Transaction fees** | Booked and visible for each store. | Booked and visible as total for each brand. |
| **Scheme Fees, Interchange, Markup** | Transaction-level information, one report file for each settlement. Store identified in summary reports by account name. | Transaction-level information, one report file for each settlement. Store indicated as data field for each transaction. |
| **Invoice** | Invoice possible for each store. | Invoice possible for each country, no separate invoice for each store. |
| **Implications** | Settlement of funds separated for each store which allows for granular reporting. However, in the case of many stores, large number of separate report files and bank transfers to be processed. | Simplifies terminal and configuration management and reduces effort in managing user credentials. Reduces number of bank transfers to be reconciled. |
|  | Higher complexity in managing configurations, readers and user credentials. | Requires some additional financial processes, for example to book specific transaction costs (separate scheme fees or balance transfers, etc.) which are only reported on a country or brand level to the individual stores, if merchant wants to allocate these costs for each store. |
| **Suggested use case** | Recommended for businesses where there is a need more granular reporting at the store level. | Recommended where a business has many stores. |


## Account Structure Considerations

There are many ways to structure your accounts with Braintree, however, it is important to get this right upon initial setup. Please take a look at some of the questions below while designing this account structure.

**NOTE**
 **Always discuss this with your PayPal Solutions Engineer or Integration Engineer before making a final decision**


- Would you like to receive settlement deposits individually per store location? Or would you prefer a single bulk deposit for multiple store locations?


- Do you currently have a direct contract with AMEX? If so, how many AMEX SE #s do you have?


- Would you prefer aggregated settlement reporting? Or separate reports per store location?


- What level of control do you require over user access permissions to the Braintree Control Panel?


- How often do you open new store locations?


- Typically, each separate legal entity within the business would have a separate merchant account.




## Preparing for Go Live!

Designing your account structure is a key activity to complete before go live, but it is important to remember that setting up your production environment takes time and can be done in parallel to integration development.

[Configure Sandbox](/braintree/in-person/get-started-1/configure-sandbox/)[API Authentication](/braintree/in-person/guides/api-authentication/)