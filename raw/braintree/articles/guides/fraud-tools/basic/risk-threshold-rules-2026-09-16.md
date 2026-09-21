<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Risk Threshold Rules
slug: /articles/guides/fraud-tools/basic/risk-threshold-rules/
createTime: '2025-04-02T01:09:15.884Z'
updateTime: '2025-04-02T01:09:15.902Z'
---



# Risk Threshold Rules


**AVAILABILITY**
 Risk threshold rules only apply to credit card and [certain Google Pay](/braintree/articles/guides/payment-methods/google-pay#fraud-tools) transactions.

 

Risk threshold rules – often referred to as velocity checks – are designed to detect and prevent carding attacks. The rules trigger different actions when specified customer information passes through the gateway multiple times within a designated time period. The gateway can either send you an email or automatically reject the verifications or transactions that trigger your risk threshold rules.

The easiest way to understand risk threshold rules is to start with a basic example of a rule:

**Gateway reject**when**7**or more**Verifications**with the same**Customer Email**occur within**15**minutes of each other.

When a customer is adding a lot of new cards to their account, this can be an indicator of a carding attack. With the above rule enabled, Braintree will start rejecting verifications from the same customer email when 7 or more have been attempted in a 15 minute window.


## Creating custom rules

To create and enable your own custom risk threshold rules:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Fraud Management**from the drop-down menu
- Next to**Risk Thresholds**, click the**Options**link
- Click**+ New Rule**in the**Custom Rules**section
- Fill in the fields with your desired criteria
- Click the**Create**button

You can always view your risk threshold rules by returning to the Risk Threshold Rules **Options** page. To create additional rules, click the **+ New Rule** button located on the right of the page. If a rule is not working as expected, you can delete it altogether by clicking the **Delete** link to the right of the rule in question. Learn more about all available rule criteria [below](#rule-criteria).


### Example

Let's say you want to be notified when a customer is performing a lot of transactions over a short period of time, as this can be an indicator of fraud. Here’s how you might set up this rule:

**Action** : Email    **Alert Email Address** : [cardattackalerts@yourcompanyname.com](mailto:/cardattackalerts@yourcompanyname.com)     **Alert Period (minutes)** : 20   **Threshold** : 5   **Operation** : Transactions   **Fields** : Customer ID   **Window (minutes)** : 5

Based on the criteria chosen above, this would be your rule:

**Email**me at [cardattackalerts@yourcompanyname.com](mailto:/cardattackalerts@yourcompanyname.com) every **20** minutes when **5** or more **Transactions** with the same **Customer Id** occur within **5** minutes of each other.


## Enabling existing risk threshold rules

To enable or disable existing risk threshold rules:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Fraud Management**from the drop-down menu
- Next to**Risk Thresholds**, click the**Options**link
- Click**Enable**or**Disable**as desired


### Recommended setup options

When reviewing the recommendations below, keep in mind that a business offering subscription-based services has different needs than one that ships physical products, so they’ll likely need different risk threshold rules to help mitigate attacks. If you have questions as you set up your own rules, feel free to [contact us](/braintree/help/FraudProtectionQuestion).


#### Test your rules

Before rejecting transactions based on your rules, we recommend you start off by setting your rule’s [Action](#action) to **Email**. This will allow you to monitor activity on your account without impacting your customers, as the Braintree gateway won't take action on the risk threshold rule's response.

When you receive an email notification, we encourage you to look up the details of the transaction or verification in the Control Panel. If you believe that it might be fraudulent, you can then [void or refund](/braintree/articles/control-panel/transactions/refunds-voids-credits) the request. It's usually best to follow your instincts in these cases.

Once you have verified that the rule works as intended, you can change the Action to **Gateway Reject**, blocking any transactions that trigger your rule.


#### Choose your alert frequency

The Alert Period determines how often you'll be notified that your rule has been triggered. You will get one email per Alert Period, so if you'd like to receive more emails, set the Alert Period to a low value. To limit the number of emails received, set the Alert Period to a higher value.


#### Consider purchase frequency

If your customers usually make repeat purchases in a small window of time, set your rule’s Window and Threshold to higher values. This will ensure that legitimate purchases don’t trigger your rule unnecessarily.

However, if your customers are more likely to make infrequent purchases, you could set your Window and Threshold at lower values to detect any transactions that don’t follow the normal pattern.


### Rule criteria

You must define the following rule criteria for each risk threshold rule:


- Action
- Threshold
- Operation
- Field
- Window


#### Action

The Action of a risk threshold rule is the event triggered when a transaction or verification violates that rule.


- **Email**: Each email notification will include a list of all verifications and transactions that have triggered the rule in the current Alert Period
- **Alert Email Address**: The email address that we will send alerts to
- **Alert Period (minutes)**: This will determine how often email notifications will be sent to you; the lower you set this number, the more emails you will receive if your rule is being triggered (maximum 120 minutes)


- **Gateway Reject**: Each rejected verification or transaction will have a status ofGateway Rejectedand a Gateway Rejection Reason ofFraud


#### Threshold

The Threshold defines the total number of times the Field must be duplicated within your designated Window before the rule is triggered. The request that causes your Threshold value to be met, along with any subsequent requests, will trigger your designated Action. The maximum Threshold value is 2147483647.


#### Operation

Your risk threshold rule's Operation indicates whether the rule should monitor [transactions](/braintree/articles/control-panel/transactions/create) or [verifications](/braintree/articles/control-panel/vault/card-verification).


#### Window (minutes)

The Window sets the number of minutes during which your rule will be triggered if the Threshold is reached. The higher the number of minutes, the more likely your rule will be triggered. Once the designated window passes, the rule resets and the Field returns to 0. The maximum Window is 178 minutes.


#### Fields

The Field you choose determines what your rule will monitor. If the Field is duplicated enough times to reach your Threshold within your designated Window, the rule will be triggered. Only one Field can be specified per rule, but you can create as many rules as you need.


- **Billing Postal Code**: Counts the number of transactions or verifications that have used the same billing postal code
- **Unique Credit Card Numbers per Billing Postal Code**: Counts the number of transactions or verifications that have unique credit card numbers with the same billing postal code
- **Credit Card Number**: Counts the number of transactions or verifications that have the same credit card number
- **Unique Customer ID per Credit Card Number**: Counts the number of transactions or verifications that have unique customer IDs and the same credit card number
- **Unique Order ID per Credit Card Number**: Counts the number of transactions that have unique order IDs and the same credit card number
- **Customer Email**: Counts the number of transactions or verifications that have the same customer email address
- **Customer ID**: Counts the number of transactions or verifications that have the same customer ID
- **Unique Credit Card Numbers per Customer ID**: Counts the number of transactions or verifications that have unique credit card numbers and the same customer ID
- **Order ID**: Counts the number of transactions that have the same order ID
- **Unique Credit Card Numbers per Order ID**: Counts the number of transactions that have unique credit card numbers and the same order ID
- **Payment Method Token**: Counts the number of transactions or verifications that have the same payment method token
- **Unique Credit Card Numbers per Payment Method Token**: Counts the number of transactions or verifications that have unique credit card numbers with the same payment method token


**NOTE**
 Many of the Fields above are not required in the Braintree gateway. To make sure your risk threshold rules work properly, be sure your transactions include all the Fields your rules rely on.

 


## Overriding rejections

The only way to override your risk threshold rules is to temporarily disable them in the Control Panel. We typically don’t recommend doing this, but it is possible if you believe an exception should be made for a customer.

