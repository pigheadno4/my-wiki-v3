<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/recurring-billing/recurring-advanced-settings -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Advanced Settings
slug: /articles/guides/recurring-billing/recurring-advanced-settings/
createTime: '2025-04-01T23:53:12.438Z'
updateTime: '2025-04-01T23:53:12.478Z'
---



# Advanced Settings

Under **Settings** &gt; **Account Settings** &gt; **Recurring Billing** &gt; **Options**, you can determine whether you would like to automatically retry failed transactions and whether [proration](#proration) will apply to subscription price changes.


## Automatic retries

When a transaction fails (transaction status = FAILED), there are three built-in automated retries before we mark the subscription as Past Due. You may have to wait up to two days before all three retries have finished executing and the subscription shows as Past Due. If the transaction has been PROCESSOR*DECLINED or GATEWAY_REJECTED, the subscription status will change to Past Due immediately. After a subscription is marked Past Due, we will try billing the subscription at least two more times. These two retries would occur whenever recurring billing runs but you can choose to specify the interval after which to retry in the control panel. The default plan after these two retries fail is retrying the subscription once per billing cycle. This default backup plan can be changed in the control panel to one of [these options](/braintree/articles/guides/recurring-billing/recurring-advanced-settings#if-above-retry-fails--try-again-after).


### Setting up retry logic

To find the options for automatic retries:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Account Settings**from the drop-down menu
- Scroll to the**Recurring Billing**section
- Next to**Recurring Billing**, click the**Options**link
- Check the box next toAutomatically retry failed transactions
- Make your selections;[learn more](#retry-logic-options)
- Click the**Save Recurring Billing Options**button


#### Retry logic options


##### After a subscription is past due, retry the subscription after…

Here’s where you can specify how long you want to wait to retry the charge after it initially fails or is declined. You must choose a value between 1 and 10 days.


##### If above retry fails, try again after…

Same idea as above. Again, you must choose a value between 1 and 10 days.


##### If above retries have failed…

This is where you have the most flexibility. You can choose to:


- Cancel the subscription
- Continue retrying the subscription
- Leave the subscription past due


**IMPORTANT**
 If Leave the subscription past due is selected, the past due balance will continue to accrue each billing cycle without any additional retries or transaction attempts. You will need to contact your customer to update their payment information and to collect the past due amount.

 

The first and second retries above will only apply during the billing cycle in which the subscription becomes Past Due. If you choose to continue retrying the subscription, we will only retry it once per billing cycle, on the subscription’s usual billing date.

The balance on Past Due subscriptions will continue to increase every billing cycle—either indefinitely or until the number of cycles in the subscription is reached. If a subscription remains Past Due for multiple cycles and you don’t want to bill the customer for the full amount owed, you can manually retry the subscription for any amount. If the retry is successful, regardless of the amount of the transaction, it will reduce that subscription’s balance to $0.


**NOTE**
 Any time you manually retry a subscription charge via the API or in the Control Panel and the transaction fails, it will not count as an automatic retry attempt. This means that your automatic retry logic will still run as scheduled.

 

Retry logic example



Your customer has a $50 monthly subscription that bills on the first of each month, and you’ve set up your retry logic with the following parameters:



After a subscription is past due, retry the subscription after: 10 days   If above retry fails, try again after: 10 days   If above retries have failed: Continue retrying the subscription



Prior to August 1, the customer had an Active subscription with a balance of $0. On August 1, the transaction for $50 fails, the customer’s subscription becomes Past Due, and its balance increases to $50. Based on your retry logic, here’s how it might turn out:





August 11    We retry the transaction for $50, but it fails again. The customer’s balance remains $50 and the status remains Past Due.





August 21    We retry the transaction for $50 a second time, but again, it fails. The customer’s balance remains $50 and the status remains Past Due.





September 1    It’s the beginning of a new billing cycle, so in addition to the $50 Past Due balance, the customer has a new $50 monthly charge. We attempt a transaction for $100, but this also fails, increasing the subscription balance to $100. We won’t try to charge the customer again until the beginning of the next billing cycle.





October 1    It’s another new billing cycle, so on top of the $100 Past Due balance, the customer has a new $50 monthly charge. We attempt a transaction for $150, which is successful this time. Now the subscription’s status returns to Active, and the subscription balance returns to $0.{" "}





Now that the subscription is Active, if it goes back to Past Due on a future billing date, the retry logic will be applied again and the subscription will be retried in 10 days.




### Handling declines

It is important to note that our retry logic will not automatically retry every transaction that is declined by the processor. Some [decline codes](/braintree/docs/reference/general/processor-responses/authorization-responses#decline-codes) are not retried because they suggest that it's unlikely the transaction will ever be successful.

Decline codes that are not retried

| Code | Text | Type |
| --- | --- | --- |
| 2004 | Expired Card | Hard |
| 2005 | Invalid Credit Card Number | Hard |
| 2006 | Invalid Expiration Date | Hard |
| 2007 | No Account | Hard |
| 2008 | Card Account Length Error | Hard |
| 2009 | No Such Issuer | Hard |
| 2010 | Card Issuer Declined CVV | Hard |
| 2011 | Voice Authorization Required | Hard |
| 2012 | Processor Declined – Possible Lost Card | Hard |
| 2013 | Processor Declined – Possible Stolen Card | Hard |
| 2014 | Processor Declined – Fraud Suspected | Hard |
| 2015 | Transaction Not Allowed | Hard |
| 2017 | Cardholder Stopped Billing | Hard |
| 2018 | Cardholder Stopped All Billing | Hard |
| 2019 | Invalid Transaction | Hard |
| 2020 | Violation | Hard |
| 2021 | Security Violation | Hard |
| 2022 | Declined – Updated Cardholder Available | Hard |
| 2023 | Processor Does Not Support This Feature | Hard |
| 2024 | Card Type Not Enabled | Hard |
| 2027 | Set Up Error – Amount | Hard |
| 2028 | Set Up Error – Hierarchy | Hard |
| 2029 | Set Up Error – Card | Hard |
| 2030 | Set Up Error – Terminal | Hard |
| 2031 | Encryption Error | Hard |
| 2032 | Surcharge Not Permitted | Hard |
| 2033 | Inconsistent Data | Hard |
| 2034 | No Action Taken | Soft |
| 2036 | Authorization could not be found | Hard |
| 2037 | Already Reversed | Hard |
| 2039 | Invalid Authorization Code | Hard |
| 2041 | Declined – Call For Approval | Hard |
| 2043 | Error – Do Not Retry, Call Issuer | Hard |
| 2044 | Declined – Call Issuer | Hard |
| 2045 | Invalid Merchant Number | Hard |
| 2047 | Call Issuer. Pick Up Card | Hard |
| 2049 | Invalid SKU Number | Hard |
| 2050 | Invalid Credit Plan | Hard |
| 2051 | Credit Card Number does not match method of payment | Hard |
| 2053 | Card reported as lost or stolen | Hard |
| 2054 | Reversal amount does not match authorization amount | Hard |
| 2055 | Invalid Transaction Division Number | Hard |
| 2056 | Transaction amount exceeds the transaction division limit | Hard |
| 2058 | Merchant not Mastercard SecureCode enabled | Hard |
| 2059 | Address Verification Failed | Hard |
| 2060 | Address Verification and Card Security Code Failed | Hard |
| 2061 | Invalid Transaction Data | Hard |
| 2062 | Invalid Tax Amount | Soft |
| 2063 | PayPal Business Account preference resulted in the transaction failing | Hard |
| 2064 | Invalid Currency Code | Hard |
| 2065 | Refund Time Limit Exceeded | Hard |
| 2066 | PayPal Business Account Restricted | Hard |
| 2067 | Authorization Expired | Hard |
| 2068 | PayPal Business Account Locked or Closed | Hard |
| 2069 | PayPal Blocking Duplicate Order IDs | Hard |
| 2070 | PayPal Buyer Revoked Pre-Approved Payment Authorization | Hard |
| 2071 | PayPal Payee Account Invalid Or Does Not Have a Confirmed Email | Hard |
| 2072 | PayPal Payee Email Incorrectly Formatted | Hard |
| 2073 | PayPal Validation Error | Hard |
| 2074 | Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | Hard |
| 2075 | Payer Account Is Locked Or Closed | Hard |
| 2076 | Payer Cannot Pay For This Transaction With PayPal | Hard |
| 2077 | Transaction Refused Due To PayPal Risk Model | Hard |
| 2079 | PayPal Merchant Account Configuration Error | Hard |
| 2081 | PayPal pending payments are not supported | Hard |
| 2082 | PayPal Domestic Transaction Required | Hard |
| 2083 | PayPal Phone Number Required | Hard |
| 2084 | PayPal Tax Info Required | Hard |
| 2085 | PayPal Payee Blocked Transaction | Hard |
| 2086 | PayPal Transaction Limit Exceeded | Hard |
| 2087 | PayPal reference transactions not enabled for your account | Hard |
| 2088 | Currency not enabled for your PayPal seller account | Hard |
| 2089 | PayPal payee email permission denied for this request | Hard |
| 2090 | PayPal or Venmo account not configured to refund more than settled amount | Hard |
| 2091 | Currency of this transaction must match currency of your PayPal account | Hard |
| 2093 | PayPal payment method is invalid | Hard |
| 2094 | PayPal payment has already been completed | Hard |
| 2095 | PayPal refund is not allowed after partial refund | Hard |
| 2096 | PayPal buyer account can't be the same as the seller account | Hard |
| 2097 | PayPal authorization amount limit exceeded | Hard |
| 2098 | PayPal authorization count limit exceeded | Hard |


## Proration

You can use proration to charge or credit a customer if a change is made to the subscription price in the middle of a billing cycle. Enabling proration adjusts the price based on how many days are left in the billing cycle, and charges the customer the newly-calculated rate immediately. Without proration enabled, any changes made to a customer’s subscription mid-cycle will go into effect at the beginning of the next cycle.


**NOTE**
 The number of days that have passed in a billing cycle is updated each day at 12am in the time zone specified in your Control Panel. The time zone for your account was established during the application process; to see your current time zone settings, navigate to **Account** &gt; **Merchant Account Info** &gt; **Time Zone**.

 

When you make a change to a subscription’s price, it is either considered an upgrade or a downgrade. An upgrade includes editing the subscription price to a higher dollar amount or applying an add-on. A downgrade includes editing the subscription price to a lower dollar amount or applying a discount.


### Proration with add-ons and discounts

In order to adjust a subscription’s price, you can either use [add-ons/discounts](/braintree/articles/guides/recurring-billing/add-ons-discounts), or directly [update the subscription](/braintree/articles/guides/recurring-billing/subscriptions#updating-a-subscription) and change the price. When you make an update to the subscription, the price change will be reflected for the remainder of its billing cycles or until another change is made. Alternatively, when you use add-ons/discounts, you must define how many billing cycles should be adjusted.

If you have proration enabled, use caution when applying add-ons or discounts mid-billing cycle to an existing subscription. Doing so will not only adjust the price for the specified number of subsequent billing cycles, but will also charge (or discount) your customer for the prorated amount left on the current billing cycle.

The best way to avoid this scenario is to do one of the following:


- disable proration on the specific subscription update
- [create a separate transaction](/braintree/articles/control-panel/transactions/create)outside of the subscription
- disable proration for your entire gateway
- only apply add-ons/discounts on the first day of a new billing cycle


**NOTE**
 When creating or updating a subscription via the Control Panel you will see an option to Prorate subscription amount (subscription price, add-ons and discounts). This option will override any proration settings you have established in your general Recurring Billing settings.

 


### Enable proration on upgrades

If you edit the subscription price to a higher dollar amount or apply an add-on, it is defined as an upgrade. To enable proration on upgrades:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Navigate to**Settings**&gt;**Account Settings**&gt;**Recurring Billing**
- Click**Options**
- Check the box next toEnable proration on upgrades

If the price of a subscription increases in the middle of the billing cycle and you have enabled proration on upgrades, then the gateway will immediately charge the customer a prorated amount to cover the remainder of the billing cycle. We’ll do this each time the subscription price increases.

Proration on upgrades example



Your customer has a $30 monthly subscription that bills on the first of each month. He decides to upgrade to a $50 monthly subscription on September 3. Because he already paid his $30 monthly bill on September 1, he’ll be charged a prorated amount immediately to cover the charge for the rest of the month.



 

Based on this example, here’s how we’ll calculate the prorated charge:





Original monthly subscription price = $30





New monthly subscription price = $50





Number of days left in the billing cycle = 27





Total number of days in the billing cycle = 30



($50 – $30) x (27 / 30) = $18



Here are the charges your customer will see on his statement:





September 1: $30





September 3: $18





October 1: $50




### If the charge for a prorated amount fails

Once you enable proration on upgrades, you can choose how to handle failed charges for prorated amounts by checking or unchecking this field in the **Options** under **Settings** &gt; **Account Settings** &gt; **Recurring Billing** :

If the transaction for a prorated amount fails, don't update the subscription or the balance.

If this is checked and the charge fails, we will not add the prorated amount to the subscription balance and the subscription itself will remain unchanged. Using the example above, if the $18 prorated charge were to fail, the subscription price wouldn’t change; the customer would be billed the usual $30 on October 1.

If this field is left unchecked, we’ll add the prorated amount to the customer’s subscription balance, and on the next billing date, we’ll charge them this amount plus the next cycle’s full price. In this case, if the $18 prorated charge were to fail, the subscription price would increase to $50, and we would bill the customer $68 on October 1.


### Enable proration on downgrades

If you edit the subscription price to a lower dollar amount or apply a discount, it is defined as a **downgrade**. To enable proration on downgrades:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Navigate to**Settings**&gt;**Account Settings**&gt;**Recurring Billing**
- Click**Options**
- Check the box next toEnable proration on downgrades

If the price of a subscription decreases in the middle of the billing cycle and you have enabled proration on downgrades, then we will subtract the prorated amount from the customer’s subscription balance. A customer’s balance should be $0 if they pay their bill on time, so you should see a negative balance for them in the gateway.

On the next billing date, the customer will be charged for any positive balance on their subscription. If the downgrade gave them a negative balance, their payment method won’t be charged until their balance exceeds $0.


**NOTE**
 Prorations on downgrades will always be applied to the subscription balance in the gateway—we will not issue a refund to the customer’s payment method. If you would like to issue a refund instead of applying a credit, you will need to create a separate transaction outside of the subscription.

 

Proration on downgrades example



Say your customer has a $75 monthly subscription that bills on the fifth of each month. She decides to downgrade to a $25 monthly subscription on September 6. She had already paid her $75 monthly bill on September 5, so we’ll subtract a prorated amount from her subscription balance to credit her for what she’s already paid. This credit will be applied to her balance in the gateway, so it will not affect her bank statement at all.



 

First, we need to calculate how much she overpaid. **Here’s what we already know** :





Original monthly subscription price = $75





New monthly subscription price = $25





Number of days left in the billing cycle = 28





Total number of days in the billing cycle = 30





To calculate the amount we’ll credit her, we find the difference between the new subscription price and the old subscription price, then multiply it by the portion of the billing cycle that remains (number of days left in the billing cycle divided by the total number of days in a billing cycle).



($25 – $75) x (28 / 30) = -$46.66



Based on this calculation, we’ll apply a credit of -$46.66 to her subscription balance.



 

How you see her balance in the gateway will differ from the charges she’ll see on her monthly bank statements. **Here are the charges your customer will see on her bank statements** :





September 5: $75





October 5: $0





November 5: $3.34





She’ll see the full $75 that she paid on September 5, because the transaction had already posted, and we do not issue refunds when downgrading subscriptions. On October 5, we apply the new monthly subscription amount ($25) to her balance in the gateway (-$46.66 + $25 = -$21.66)—because her balance is still negative, she is not charged anything for October. On November 5, we apply the monthly subscription amount to the remaining balance on her subscription and find that she only owes the remaining $3.34 (-$21.66 + $25 = $3.34)—which is automatically debited and then reflected on her November bank statement.



 

**Here’s what her subscription balance will show for you in the gateway** :





September 5: $0





September 6: -$46.66





October 5: -$21.66





November 5: $0





Because she paid her full $75 balance on September 5, her balance shows as $0 in the gateway. On September 6, we’ll apply the calculated credit, which results in a negative balance. On the next billing cycle (October 5), we add the new subscription price ($25) to her balance, leaving -$21.66 on her subscription. With the next billing cycle (November 5) we add the new subscription price ($25) to her balance, making her new balance $3.34. Because her balance is now positive, she will be automatically be charged the $3.34—if the charge is successful her balance will be shown as $0 in the gateway.



 

At this point, she is officially trued up on her subscription! From here forward, the customer will see a $25 charge on the fifth of each month.



