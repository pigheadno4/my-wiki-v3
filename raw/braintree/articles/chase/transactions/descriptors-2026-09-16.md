<!-- Source URL: https://developer.paypal.com/braintree/articles/chase/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/chase/transactions/descriptors/
createTime: '2025-04-01T23:54:05.225Z'
updateTime: '2025-04-01T23:54:05.240Z'
---



# Descriptors


**NOTE**
 If you’d like to update your descriptor for PayPal transactions, you can do so from your PayPal console.

 

A descriptor is what your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME CHICAGO IL $100.00

Chase automatically configures your descriptor based on information you provided in the Transaction Division Information section of your application. Your descriptor consists of 3 separate fields:


- Merchant name (DBA)
- Merchant city
- Merchant state


**NOTE**
 When issuing a refund, the descriptor shown will default to the descriptor that was passed with the original transaction.

 


## Descriptor field requirements


### Merchant name (DBA) field


- Limit of 22 characters
- Must be all caps
- Can contain letters and numbers
- Can't contain special characters ^ [ ] ~ `


**NOTE**
 For Mastercard transactions, a question mark (?) will be reflected as a space in the descriptor.

 


#### Customizing the merchant name field

You can customize your merchant name field by adding a more specific descriptor – whether it be a product or store name. The more specific your descriptor, the less likely customers are to be confused by purchases they see on their statement – which can decrease the likelihood of [chargebacks](/braintree/articles/risk-and-security/chargebacks-retrievals/overview).

Your merchant name field still has a limit of 22 characters, and must also follow these guidelines:


- DBA can make up the first 3, 7, or 12 characters – we recommend abbreviating in a way that most clearly reflects your DBA
- DBA must be separated from the rest with an asterisk (*) – which can only occupy the 4th, 8th, or 13th space

For example, if your company name is Amazing Company, and you sell 3 different colors of the same hat, you can identify which one the customer purchased in your descriptor. Options for this could be:


- AMAZINGCOMPANY*RED HAT
- AMAZINGCO*REDHAT
- AMAZCO*REDHATOPTION


### Merchant city field

The merchant city field is not limited to identifying your location. If you prefer, you can use this field to provide your customer service phone number, URL, or customer service email address instead. This way customers can easily contact you if they have a question about a transaction on their bank statement.

While there are different requirements for using a phone number, email, or URL, the basic parameters of the merchant city field are as follows:


- Limit of 13 characters
- Can include special characters - @ . and space


#### Phone number

If you choose to list a phone number instead of your city, the phone number must follow these rules:


- First 3 characters must be numeric followed by a hyphen (-)
- Remaining characters can be alpha or numeric

Example: 617-SERVICE or 617-737-8423


#### URLs and email addresses

If you choose to list your URL or email address instead of your city, they must follow these rules:


- URL must include a period (.)
- Email address must include the at (@) symbol

Example: [US@COMPANY.CO](mailto:US@COMPANY.CO) or [URCOMPANY.COM](http://URCOMPANY.COM)


### Merchant state field

While the merchant city field can be used for a number of options, the merchant state field should always list the state in which your business is located.

