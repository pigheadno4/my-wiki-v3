<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/account-updater -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Account Updater
slug: /articles/guides/account-updater/
createTime: '2025-04-01T23:54:54.764Z'
updateTime: '2025-04-01T23:54:54.789Z'
---



# Account Updater

Account Updater is a feature that automatically requests updates for vaulted payment methods in the event that a customer's vaulted card expires or is replaced – helping you avoid failed transactions or gaps in services provided to your customers.


## Fees

Pricing for Account Updater varies depending on your pricing model. [Contact us](/braintree/help/feeHelp) for more information on fees.


## Compatibility

Account Updater is available to merchants who use Braintree Direct and are either based in the US or transact primarily with US customers. [Contact us](/braintree/help) to see if Account Updater is a good fit for your business.


### Customer compatibility

Whether a card can be updated using Account Updater is dependent on the customer’s issuing bank and that bank's participation in this feature. As a result, even if a customer's card type is compatible, it may not be eligible for automatic updates if the issuing bank does not participate. Supported card types are:


- Visa
- Mastercard
- Discover


**NOTE**
 Prepaid cards and cards processed through Apple Pay or Google Pay are not supported.

 


## Setup

Account Updater is not enabled on your account by default. We’ll work with you directly to make sure this feature is configured in a way that works best for your business. [Contact us to get started.](/braintree/help)


## How it works

When Account Updater is first enabled, we automatically send all vaulted Visa, Mastercard, and Discover credit card information to the card-issuing banks to request updates in batches of 600,000. If the issuing bank has opted to participate, they will respond with the new card number and/or expiration date – allowing us to update the vaulted card.


**NOTE**
 If you have more than 2 million payment methods saved in your Vault when you enable Account Updater, we will only request updates for cards that have expired within the last 13 months.

 

After the initial batch, we request updates for cards on a rolling basis when they meet any of the following criteria:


- Card is expired
- Card is set to expire in the current month
- [Recurring billing](/braintree/articles/guides/recurring-billing/overview)payment is due within 2 weeks
- Card has been flagged for[Next Day Card Refresh](#next-day-card-refresh)
- Relevant transaction activity suggests an update may be needed;[learn more](#transaction-activity-criteria)


### Transaction activity criteria

Account Updater will request an update for a vaulted card that meets the following criteria:


- Has been declined by the processor in the last 30 days
- Has been processed successfully within the last 13 months, but has not had any successful transactions in the last 30 days

In other words, if a card has been successfully processed within the last 13 months and within the last 30 days, one decline is not enough to trigger Account Updater. This is important to keep in mind with cards vaulted for recurring billing. A card associated with a monthly subscription will not be automatically added to an Account Updater batch the first time it is declined, since it was successfully processed exactly 30 days prior in the previous billing cycle. If you [retry the subscription](/braintree/articles/guides/recurring-billing/subscriptions#retrying-a-past-due-subscription) and it is declined a second time, we will then request an update for the card in question.


### Next Day Card Refresh

Next Day Card Refresh attempts to update vaulted cards if an authorization is declined with certain decline codes. This feature will only work if you have retry logic set up to re-attempt failed transactions – whether it’s through our [recurring billing feature](/braintree/articles/guides/recurring-billing/recurring-advanced-settings#automatic-retries) or logic you’ve built yourself. These are the decline codes that will trigger Next Day Card Refresh before being retried:

| Decline Code | Reason |
| --- | --- |
| 2000 | Do Not Honor |
| 2004 | Expired Card |
| 2005 | Invalid Credit Card Number |
| 2006 | Invalid Expiration Date |
| 2012 | Processor Declined - Possible Lost Card |
| 2013 | Processor Declined - Possible Stolen Card |
| 2022 | Declined - Updated Cardholder Available |
| 2043 | Error - Do Not Retry, Call Issuer |
| 2044 | Declined - Call Issuer |
| 2047 | Call Issuer. Pick Up Card |
| 2053 | Card reported as lost or stolen |

[Learn more about decline codes and their meanings.](/braintree/articles/control-panel/transactions/declines#authorization-decline-codes)


## Reporting

Our Account Updater reporting shows you how many cards were updated, the reason for and date of each update, and whether the updates were successful or not. If you display the last four digits or expiration dates for customer's cards in your UI, you can also leverage these reports to ensure that you keep their displayed information up to date.

You can find reporting for Account Updater in three ways:


- In the activity history for an[individual payment method](#individual-payment-methods)
- By generating an[Account Updater report](#account-updater-report)
- By using a[webhook](#account-updater-webhook)


### Individual payment methods

If you want to see the Account Updater activity for a specific payment method, you can find it in the payment method's transaction history:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Vault**in the navigation bar
- Scroll to the**Customer Search**section
- Define your desired parameters and click the**Search**button
- Click on the link in theTokencolumn located to the right of the payment method you'd like to check
- Scroll down to the**History**section

Any history events that have the prefix **AU** in the Source Description field are events triggered by Account Updater. This box will also include the [event description](#event-descriptions) that was returned when the update was attempted.


### Account Updater report

The Account Updater report shows all Account Updater activity within a specified date range. To generate an Account Updater report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Scroll to the**Vault**section
- Next to**Account Updater**, click the**Export**button
- Select your desired date range
- Click the**Filter and Download**button


**NOTE**
 Account Updater reports are limited to 40,000 rows.

 


### Account Updater webhook

If you'd like to review a daily report of Account Updater activity, you can use the [Account Updater webhook](/braintree/docs/reference/general/webhooks/account-updater). This webhook links to a CSV file containing information on all vaulted payment methods that have been updated within 24 hours.


**NOTE**
 The column names in the daily report sent via webhook are slightly different from the ones in the Account Updater report generated in the Control Panel. In the webhook report, event descriptions are listed in the _update_type_ column.

 


### Event descriptions

Event descriptions let you know why a payment method was sent by Account Updater, and whether it was successfully updated. These descriptions can be found in the activity history for a given payment method, the Account Updater report generated in the Control Panel, or the Daily Report generated via webhook. Here are the possible event descriptions:


- New account number
- New expiry date
- Call customer - account closed
- Call customer for updates
- Match found - card is current
- Call issuer for updates
- Do not retry
- Error

We will not attempt to resend any cards for updates that return the Call customer - account closed, Call customer for updates, Call issuer for updates, or Do not retry event descriptions until the payment method has been manually updated by a user in the Control Panel or via the API.

