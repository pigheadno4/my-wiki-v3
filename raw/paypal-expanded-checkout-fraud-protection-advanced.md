<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Fraud Protection Advanced
slug: /docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/
createTime: '2025-01-28T18:22:09.740Z'
updateTime: '2025-08-28T00:32:47.384Z'
---


# Fraud Protection Advanced


## Fraud Protection Advanced  
Fraud Protection Advanced (FPA) is a robust fraud protection tool integrated into PayPal's core processing services. It enables your fraud teams to conduct in-depth risk analysis and investigations to help identify and mitigate fraud.

Fraud Protection Advanced combines decades of intelligence from the PayPal network with advanced machine learning (ML) and analytics to continuously adapt to changes in both a merchant's business and evolving fraud tactics. It is integrated with PayPal Complete Payments (PPCP) for merchants who are on the Advanced Checkout integration.


**info**
**Notes:**

- FPA is now available in the US and multiple global regions. For a complete list of supported countries,see [Targeted users, eligible markets, and pricing details](#targeted-users-eligible-markets-and-pricing-details) .
- Fraud Protection Advanced is available through your merchant's PayPal business account and can be enabled easily. For more information on how your merchants can set up FPA, see [Getting started with FPA](/docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/getting-started/) .



## Why is FPA essential? 
FPA provides a range of powerful capabilities:

- Fraud profile identification: Initial fraud strategies are customized based on historical risk patterns. The effectiveness of these profiles is monitored post-onboarding and adjusted as needed to enhance performance.
- Fraud detection and risk scoring: Mitigate fraud by declining high-risk transactions using advanced features, including: - Custom filters: Tailor rules to identify and block fraudulent activities.
- Manual review: Assess and review flagged transactions manually for further validation.
- Blocklists, allowlists, and reviewlists: Enhance filters with supplementary lists to manage trusted and suspicious entities.
- Activity tracking and audit trail: Track changes and user actions and maintain a detailed audit trail.

 
- ML-based AI model: Utilize machine learning techniques to analyze data points such as card details, buyer information, purchasing patterns, and device intelligence to generate a risk score.

Hence, we strongly recommend that you choose FPA as your fraud protection tool.

 

### What are the benefits?
FPA provides the following benefits on top of [Fraud Protection](https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/) (FP) for merchants enrolling in PPCP capabilities:

- It is a self-serve tool that you can customize to meet your specific business requirements. It is not pre-configured to fit any business needs by default.
- PayPal can view both merchant and consumer activities across 25 billion transactions annually. This rich data fuels PayPal's machine learning models, which adapt to new transactions as they occur and historical fraud trends seen across the network, leading to more accurate fraud detection.
- Due to enhanced fraud decision-making by merchants, consumers will experience fewer declines, less friction, and faster order processing.

Additionally, PayPal enhances the onboarding experience for fraud protection tools by offering:

- The right product recommendation for fraud prevention tools, better discoverability, and comprehension of products.
- A streamlined, guided setup and activation experience.
- A better description of the advanced capabilities and flexibility of the fraud tools.



## Essential prerequisites for optimal FPA performance 
To enhance risk and fraud management, we strongly recommend that youprovide additional data. This data is incorporated into PayPal's machine learning models, allowing them to analyze historical transactions and to improve the model's efficiency in detecting fraud. This approach optimizes the performance of your risk and fraud management processes. To include this data, you must pass the following fields to all requests sent to the Orders v2 API for processing.

 

### Create order
The following table shows the required parameters for optimal FPA performance when making a POST call to the Create order endpoint of the Orders v2 API.

**Device ID**

- If you are integrated through PayPal JS SDK, the device ID will be passed by default.
- If you are integrated through APIs, you would need to do the following so that the device ID is passed in the request: - Integrate Fraudnet if you are on a browser. The device ID is sent as PAYPAL-CLIENT-METADATA-ID in the request data.
- Integrate Magnes if you are on an app.
- If you do not want to use Fraudnet or Magnes, you can pass the device ID information directly through the Orders API requests in the PAYPAL-CLIENT-METADATA-ID field. For more information, see the Client-Metadata-Id in the Create order endpoint of the Orders v2 API.

 


### Header
| **Field name** | **Description** | **Type** | **Notes** |
| PayPal-Client-Metadata-Id | The device ID for this purchase. See the[parameter definition](/docs/api/orders/v2/#orders_create!in=header&path=PayPal-Client-Metadata-Id&t=request)for more information. | String | - Minimum characters: 1
- Maximum characters: 36 |

 

### Body
| **Field name** | **Description** | **Type** | **Notes** |
| payment_source.card.attributes.customer.email_address | Email address of the buyer as provided to the merchant or on file with the merchant. Email Address is required if you are processing the transaction using PayPal Guest Processing, which is offered to select partners and merchants. For all other use cases, we do not expect partners or merchant to sendemail_addressof their customer. See the[parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/email_address&t=request)for more information. | string | - Minimum characters: 3
- Maximum characters: 254
- Pattern: (?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) |
| payment_source.card.attribues.customer.phone | The phone number of the buyer as provided to the merchant or on file with the merchant. Thephone.phone_numbersupports onlynational_number. See the[parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/phone&t=request)for more information. | object |  |
| payment_source.card.billing_address | The billing address for this card. Supports only theaddress_line_1,address_line_2,admin_area_1,admin_area_2,postal_code, andcountry_codeproperties. See the[parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/billing_address&t=request)for more information. | object |  |
| purchase_units.shipping.address | The address of the person to whom to ship the items. Supports only theaddress_line_1,address_line_2,admin_area_1,admin_area_2,postal_code, andcountry_codeproperties. See the[parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/attributes/customer/phone&t=request)for more information. | object |  |
| purchase_units.items | An array of line items that the customer purchases from the merchant. See the[parameter definition](/docs/api/orders/v2/#orders_create!path=payment_source/card/billing_address&t=request)for more information. | array of objects |  |
| purchase_units[].supplementary_data.risk.customer.ip_address | An Internet Protocol address (IP address). This address assigns a numerical label to each device that is connected to a computer network through the Internet Protocol. Supports IPv4 and IPv6 addresses.

- If your merchant is integrated through PayPal JS SDK, the Customer IP will be passed by default.
- If your merchant is integrated through APIs, they can send in the Customer IP through [Orders v2 API](/docs/api/orders/v2/) requests. In the request object for Orders v2 API, the Customer IP is structured as follows:

"supplementary_data": { "risk": { "customer": { "ip_address": "192.158.1.38" } } } | string | Minimum characters: 7

Maximum characters: 39

Pattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$ |

 

### Capture payment for order
| **Field name** | **Description** | **Type** | **Notes** |
| payment_source.card.name | The cardholder's name as it shows up on the card. See the[parameter definition](/docs/api/orders/v2/#orders_capture!path=payment_source/card/name&t=request)for more information. | string | - Minimum characters: 1
- Maximum characters: 300 |
| payment_source.card.number | The primary account number (PAN) for the payment card. See the[parameter definition](/docs/api/orders/v2/#orders_capture!path=payment_source/card/number&t=request)for more information. | string | - Minimum characters: 13
- Maximum characters: 19 |



## Targeted users, eligible markets, and pricing details 
FPA is available for both direct merchants and through marketplaces, which are payment platforms that host merchants. The following table outlines the pricing details for each FPA-screened transaction across the available markets:

| **Country code** | **Country** | **Headline price** |
| US | United States | 0.07USD |
| CA | Canada | 0.09CAD |
| AU | Australia | 0.1AUD |
| AT | Austria | 0.06EUR |
| DE | Germany | 0.06EUR |
| GB | United Kingdom | 0.06GBP |
| FR | France | 0.06EUR |
| ES | Spain | 0.06EUR |
| IT | Italy | 0.06EUR |
| PL | Poland | 0.3PLN |
| PT | Portugal | 0.06EUR |
| IE | Ireland | 0.06EUR |
| BG | Bulgaria | 0.06EUR |
| CY | Cyprus | 0.06EUR |
| CZ | Czech Republic | 1.6CZK |
| DK | Denmark | 0.5DKK |
| EE | Estonia | 0.06EUR |
| FI | Finland | 0.06EUR |
| GR | Greece | 0.06EUR |
| HU | Hungary | 25HUF |
| LT | Lithuania | 0.06EUR |
| LV | Latvia | 0.06EUR |
| MT | Malta | 0.06EUR |
| RO | Romania | 0.35RON |
| SE | Sweden | 0.7SEK |
| SI | Slovenia | 0.06EUR |
| SK | Slovakia (Slovak Republic) | 0.06EUR |
| BE | Belgium | 0.06EUR |
| LU | Luxembourg | 0.06EUR |
| NL | Netherlands | 0.75EUR |
| LI | Lichtenstein | 0.06EUR |
| NO | Norway | 0.75NOK |
| SM | San Marino | 0.06EUR |
| SG | Singapore | 0.1SGD |
| HK | Hong Kong | 0.6HKD |

 



## Discovery and access 
You can find FPA using either of the following options:

- In **Business Tools** , navigate to the **Manage Risk** section. Select the **Fraud Tools** tile.
![FPA discovery via Business Tools](https://www.paypalobjects.com/devdoc/FPA_Home_Discovery_BusinessTools.png)

- Alternatively, go to your **Account Settings** , and select **Payment preferences** . Next to the **Manage fraud** section, select **Choose a fraud tool.**
![FPA discovery via Account Settings](https://www.paypalobjects.com/devdoc/Activate_dirmerch_acct_settingSS.png)


### Enable FPA
You can enable FPA using the following steps:

- Select **Do it yourself using PayPal's fraud tool** and select **Next** .
![FPA DIY selection screen](https://www.paypalobjects.com/devdoc/FPA_Home_DIY_FPA_Recommended.png)

- You will see a recommended solution based on your business metrics. However, you can modify the selection if you want. Choose **Fraud Protection Advanced Tool** and select **Next** .
![Select FPA tool screen](https://www.paypalobjects.com/devdoc/Activate_Dir_Mer_Select_FPA.png)

- Confirm your details to set up automatic bank payments for your fraud tool, and select **Next** .
![Set up auto debit screen](https://www.paypalobjects.com/devdoc/Activate_Dir_Mer_Set_Up_auto_debit.png)

- Select **Let's Go** to go to the Fraud Protection Advanced tool and begin customizing your fraud tool.
![FPA activation end screen](https://www.paypalobjects.com/devdoc/Activate_DirMer_EndOfFlow_.png)


### View the FPA Dashboard
Once activated, Fraud Protection Advanced will open in a new tab that will display the **Dashboard** , which presents fraud metrics related to your business. The dashboard displays fraud metrics over the past 180 days.

Now, you're ready to begin customizing the tool to suit your business needs.

![FPA Dashboard](https://www.paypalobjects.com/devdoc/FPA_Home_Dashboard.png)

 



### Features
FPA offers a range of powerful features designed to help you reduce fraud:

- Fraud profile identification: Provides automated filter recommendations based on onboarding data and historical transaction data. Use these to make informed decisions and strengthen your overall fraud prevention strategy.
- Risk score calculation: PayPal's machine learning model analyzes various data points, including card details, buyer information, purchasing patterns, and device intelligence, among others, to calculate a Risk Score. The risk score ranges from 0 to 100, where 0 indicates no risk, and 100 represents a highly risky transaction.
- Fraud detection: Mitigates fraud by declining risky transactions through advanced features such as: - **Filters** : Rules that determine whether FPA approves, rejects, or flags a transaction for review. Youcan enable, adjust, or create your own filters.
![FPA Filters screen](https://www.paypalobjects.com/devdoc/FPA_Home_Filters.png)

- **Lists** :Collections used to apply actions to a group of attributes. You can use **Allowlists** to ensure your trusted customers can check out smoothly and **Blocklists** to prevent known bad actors. **Reviewlists** enable you to automatically queue transactions with specific attributes for manual review, allowing your team to decide whether to approve or reject them. You can create lists, view the number of items on each list, and check if an active filter is associated with each attribute list.
![FPA Lists screen](https://www.paypalobjects.com/devdoc/FPA_Home_Lists.png)

- **Review** : Transactions flagged for review are placed in a single queue, where you can view the filters that triggered the review, the time the transaction occurred, and the associated risk score. You can manually review transactions and determine whether to approve or reject them.
- **Activity** :History of all actions associated with the FPA tool, including changes to filters, fields, lists, and case reviews. It helps you also track who made changes and when they occurred.
![FPA Activity screen](https://www.paypalobjects.com/devdoc/FPA_Home_Activity.png)


 



## Next steps 


A comprehensive overview of onboarding with Fraud Protection Advanced (FPA).
