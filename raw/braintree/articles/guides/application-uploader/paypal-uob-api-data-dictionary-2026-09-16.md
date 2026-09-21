<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/application-uploader/paypal-uob-api-data-dictionary -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Account Onboarding API Data Dictionary
slug: /articles/guides/application-uploader/paypal-uob-api-data-dictionary/
createTime: '2025-04-01T23:10:44.192Z'
updateTime: '2025-04-01T23:10:44.211Z'
---



# Account Onboarding API Data Dictionary


**AVAILABILITY**
 The Account Onboarding API is only available for select merchants at this time.

 

The Account Onboarding API Data Dictionary is your guide to creating applications. It specifies the type and format of data required in order to create many applications at once using the onboarding API.

Each row in the data dictionary includes a definition of expected information, and important details (like acceptable values and formatting information).

[](/braintree/files/uob-api-data-dictionary.csv)

[](/braintree/files/uob-api-data-dictionary.csv)[Download the Account Onboarding Data Dictionary](/braintree/files/uob-api-data-dictionary.csv).

If you have the Branded solution, you would only need to submit a subset of the application data, since some information is not required. The PayPal Branded Solution Data Dictionary specifies the type and format of data that you should use.

[](/braintree/files/uob-api-branded-data-dictionary.csv)

[](/braintree/files/uob-api-branded-data-dictionary.csv)[Download the Account Onboarding Branded Solution Data Dictionary](/braintree/files/uob-api-branded-data-dictionary.csv).

The Data Dictionary is broken out into 7 unique sections:


- Create Account Input
- Business information
- Stakeholder information
- Funding information
- ACH information
- Discount program registration information
- American Express information


**NOTE**
 ACH information, Discount Program, and American Express are not needed if you are using the Branded Solution. See the download link for the Branded Solution Data Dictionary above.

 


## Create Account Input

This section consists of two fields that represent account level settings: external ID and Country Code. In addition, all other properties below are nested under the Create Account Input.


## Business information

This section contains information on your billers’ business (like DBA, legal name, address, and processing volume). This information is used both during the Underwriting process, and during the setup of features like PayPal, Venmo, and Hyperwallet.

If you have additional people at the company who should be involved in the vetting and review process other than the beneficial owners or authorized signers, then you must supply contact information for at least one Point of Contact. Our review team will reach out to them for additional questions in the onboarding process.


## Stakeholder information

This section contains information on your billers’ beneficial owners and authorized signers. Much like Business Information, Stakeholder Information is used both during the Underwriting process, and during the setup of features like PayPal, Venmo, and Hyperwallet.

The first stakeholder will be the individual listed as the primary contact on the account.


**NOTE**
 You must include stakeholders' information for any beneficial owner with &gt; 25% ownership.

 


## Funding information

Information in this section is used to set up a biller’s Funding profile and Hyperwallet account.


## ACH information

Information in this section is used to set up a biller’s ACH payment method.


## Discount program registration information

Information in this section is used to register the biller with a Discount Program (such as MVV, VPP, loan, etc.). Only include information in this section if the biller should be registered in a discount program.


## American Express information

Information in this section is used to set the biller up with American Express via their Service Establishment number.

