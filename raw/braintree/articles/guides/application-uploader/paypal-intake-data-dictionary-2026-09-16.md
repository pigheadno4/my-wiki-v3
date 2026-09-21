<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/application-uploader/paypal-intake-data-dictionary -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PayPal Intake Data Dictionary
slug: /articles/guides/application-uploader/paypal-intake-data-dictionary/
createTime: '2025-04-02T01:33:44.005Z'
updateTime: '2025-04-02T01:33:44.114Z'
---



# PayPal Intake Data Dictionary


**AVAILABILITY**
 The Application Uploader is only available for select merchants at this time.

 

The PayPal Intake Data Dictionary is your guide to creating applications. It specifies the type and format of data required in order to create many applications at once using the Intake API or the [Application Uploader](/braintree/articles/guides/application-uploader/overview).

Each row in the data dictionary includes a definition of expected information, and important details (like acceptable values and formatting information). There are two acceptable input schemas for the PayPal Intake Data Dictionary:

[](/braintree/files/the-paypal-intake-data-dictionary-v1.csv)

[](/braintree/files/the-paypal-intake-data-dictionary-v1.csv)[Download the PayPal Intake Data Dictionary (v1)](/braintree/files/the-paypal-intake-data-dictionary-v1.csv)

[](/braintree/files/paypal-intake-example-file-v1.csv)

[](/braintree/files/paypal-intake-example-file-v1.csv)[Download Sample (v1)](/braintree/files/paypal-intake-example-file-v1.csv)

[](/braintree/files/the-paypal-intake-data-dictionary-v2.csv)

[](/braintree/files/the-paypal-intake-data-dictionary-v2.csv)[Download the PayPal Intake Data Dictionary (v2)](/braintree/files/the-paypal-intake-data-dictionary-v2.csv)

[](/braintree/files/paypal-intake-example-file-v2.csv)

[](/braintree/files/paypal-intake-example-file-v2.csv)[Download Sample (v2)](/braintree/files/paypal-intake-example-file-v2.csv)

If you have a branded solution, you need to submit a slightly different set of application data. The PayPal Branded Solution Data Dictionary specifies the type and format of data that you should use.

[](/braintree/files/paypal-branded-solution-data-dictionary.csv)

[](/braintree/files/paypal-branded-solution-data-dictionary.csv)[Download the PayPal Branded Solution Data Dictionary](/braintree/files/paypal-branded-solution-data-dictionary.csv)  [](/braintree/files/paypal-branded-solution-example-file.csv)

[](/braintree/files/paypal-branded-solution-example-file.csv)[Download Sample (Branded Solution)](/braintree/files/paypal-branded-solution-example-file.csv)

The Data Dictionary is broken out into 7 unique sections:


- Identifier
- Business information
- Owner information
- Funding information
- ACH information (not required for branded solutions)
- Discount program registration information (not required for branded solutions)
- American Express information (not required for branded solutions)


## Identifier

This section consists of a single field: the unique identifier. You should provide a unique identifier per row / MID request. This will help prevent duplicate entries.


## Business information

This section contains information on your billers’ business (like DBA, legal name, address, and processing volume). This information is used both during the Underwriting process, and during the setup of features like PayPal, Venmo, and Hyperwallet.


## Owner information

This contains information on your billers’ owners and authorized signers.

Much like Business Information, Owner Information is used both during the Underwriting process, and during the setup of features like PayPal, Venmo, and Hyperwallet.

The first owner will be the individual listed as the primary contact on the account. Please see the additional documentation from your PayPal Account Management team for detailed guidance on ownership requirements.


## Funding information

Information in this section is used to set up a biller’s Funding profile and Hyperwallet account.


## ACH information

This section is not required for branded solutions.

Information in this section is used to set up a biller’s ACH payment method.


## Discount program registration information

This section is not required for branded solutions.

Information in this section is used to register the biller with a Discount Program (such as MVV, VPP, loan, etc.). Only include information in this section if the biller should be registered in a discount program.


**NOTE**
 If you’re using the API, there’s no need to provide the discountProgramRegistration.registered field; a ‘yes’ is implied by the presence of a value in the discountProgramRegistration.registrationIdentifier field.

 


## American Express information

This section is not required for branded solutions.

Information in this section is used to set the biller up with American Express via their Service Establishment number.


## Resources

[Sample File](/braintree/articles/guides/application-uploader/sample-file)

