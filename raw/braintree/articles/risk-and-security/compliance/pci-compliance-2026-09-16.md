<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/pci-compliance -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PCI Compliance
slug: /articles/risk-and-security/compliance/pci-compliance/
createTime: '2025-04-01T22:44:45.237Z'
updateTime: '2025-04-01T22:44:45.255Z'
---



# PCI Compliance


**IMPORTANT**
 Starting from March 31, 2024, all PCI DSS assessments will be mandated to adhere to the PCI DSS 4.0 compliance standard

 

The Payment Card Industry Data Security Standard (PCI DSS) is a set of industry-mandated requirements for any business that handles, processes, or stores credit cards – regardless of the business's size or location. The PCI Security Standards Council was founded by 5 of the major card brands, and they each share equal responsibilities in the council's work. [Read more about PCI compliance on the PCI Security Standards Council's website.](https://www.pcisecuritystandards.org/)


## PCI Self-Assessment Questionnaires

You must fill out a Self-Assessment Questionnaire (SAQ) annually to help you determine if your payment processing setup is PCI compliant. The SAQ includes a series of yes-or-no questions for each applicable PCI DSS requirement.

Your PCI compliance level and how you integrate with Braintree will determine which SAQ you should complete. [Read more about the different SAQs.](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment)


## PCI compliance levels

There are four levels of PCI compliance that indicate your level of risk and exposure. In their role as part of the PCI Security Standards Council, Visa determines how to classify your business by looking at your Visa transaction volume over a 12-month period. This transaction volume is based on the aggregate number of Visa transactions (inclusive of credit, debit, and prepaid cards) from your registered Doing Business As (DBA) name. Merchants with the highest transaction volumes are classified as level 1, while those with the lowest transaction volumes are level 4. You can find more information about PCI levels on [Visa's website](https://usa.visa.com/support/small-business/security-compliance.html#2).


## Your requirements

Although we securely store and process card data for you, integrating with us does not automatically fulfill your PCI compliance requirements. You are still **required** to complete an annual SAQ in order to be PCI compliant.


**IMPORTANT**
 Failing to complete your annual SAQ for PCI compliance could result in substantial fines and the suspension of your ability to accept credit card payments.

 


## How we can help

PCI compliance may seem overwhelming, but there are resources to help. Qualified Security Assessors (QSAs) are independent security individuals and organizations that have been qualified by the PCI Security Standards Council to validate an entity’s adherence to the PCI DSS. A QSA can help you choose the right SAQ for your business and support you through the process.

We’ve partnered with SecurityMetrics, a QSA company, to offer PCI compliance assistance to our merchants. Once your application with Braintree has been approved, you'll receive an email explaining how to create your account with SecurityMetrics, if you choose to use them for PCI assistance.

If you are using Braintree Direct and your business falls into level 3 or 4 of PCI compliance, we’ll set you up with SecurityMetrics at no cost to you. Due to the increased scope of compliance, level 1 and 2 merchants who choose to partner with SecurityMetrics will be subject to any enterprise-level account fees assessed by SecurityMetrics.


**NOTE**
 While we are always willing to help in any way we can, SecurityMetrics is best equipped to answer specific questions about your scope of compliance. For the best way to contact SecurityMetrics, [visit their website](https://www.securitymetrics.com/contact).

 


### Enrolling with SecurityMetrics

To take advantage of SecurityMetrics’ services, you’ll need to wait to enroll until we email you with your Merchant Account Number. The Merchant Account Number needed to enroll with SecurityMetrics is different from your [merchant account ID and merchant ID](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id-versus-merchant-id). This value is not displayed in the Control Panel, so if you no longer have the email with this information, you’ll need to [email us](/braintree/help?issue=ComplianceQuestion).


**NOTE**
 Due to security reasons, we can't provide your Merchant Account Number over the phone – the authorized signer on your account must email us with the request.

 

Part of the enrollment process includes answering a brief set of questions that will help them determine which SAQ you need to complete.

To enroll:


- Navigate to the[SecurityMetrics Braintree page](https://www.securitymetrics.com/pcidss/braintree)
- Click**Sign Up**and enter the email address associated with your Braintree account
- Verify your email address
- Accept the Terms of Use
- Continue through the wizard and complete the questionnaire about your credit card processing


**IMPORTANT**
 Data security is incredibly important to us. If you believe the security of your Braintree integration may have been compromised, [contact us](/braintree/help) and we'll assist you from there.

 

