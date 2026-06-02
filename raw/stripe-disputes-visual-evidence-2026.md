<!-- Source URL: https://docs.stripe.com/disputes/visual-evidence -->
<!-- Fetched: 2026-05-09 -->

# Dispute sample evidence packets

Use these visual examples to help you through a dispute.

You can manage disputes using the [Dashboard](https://docs.stripe.com/disputes/responding.md) or the [API](https://docs.stripe.com/disputes/api.md).

Learn how to navigate common network dispute categories by referring to the following sample evidence packets. To learn about the reason codes within these categories, see [Dispute reason codes](https://docs.stripe.com/disputes/reason-codes-defense-requirements.md).

> The images throughout this guide are for illustrative purposes only.

## Credit not processed

The following visual evidence captures when a _Credit Not Processed_ dispute is denied or approved. To effectively show proof or denial of a dispute in this category, adhere to this non-exhaustive list of best practices.

#### Approved

To provide official proof that you refunded a transaction, begin by showing the original transaction.
![Credit not processed approval example (1)](assets/stripe-disputes-evidence-credit-not-processed-approved-1.png)

With this, include refund details, the payment processor log, and merchant account statement.
![Credit not processed approval example (3)](assets/stripe-disputes-evidence-credit-not-processed-approved-3.png)

#### Denied

To effectively deny a refund, begin by showing your reason for denial.
![Credit not processed denial example (1)](assets/stripe-disputes-evidence-credit-not-processed-denied-1.png)

Attach your communication history, showing that you informed the customer of the policy before the chargeback.
![Credit not processed denial example (2)](assets/stripe-disputes-evidence-credit-not-processed-denied-2.png)

Add your contact information, and emphasize that you presented your terms of sale at checkout.
![Credit not processed denial example (3)](assets/stripe-disputes-evidence-credit-not-processed-denied-3.png)

## Duplicate

The following visual evidence captures when a _Duplicate_ dispute is denied or approved. To effectively show that a transaction was a duplicate or intentional, adhere to this non-exhaustive list of best practices.

#### Approved

To show proof that you refunded one of the transactions, begin by capturing your investigation summary.
![One duplicate refunded (1)](assets/stripe-disputes-evidence-duplicate-approved-1.png)

Show the valid and refunded transactions.
![One duplicate refunded (1)](assets/stripe-disputes-evidence-duplicate-approved-2.png)

Include the refund details and the payment processor log.
![One duplicate refunded (1)](assets/stripe-disputes-evidence-duplicate-approved-3.png)

Attach a bank statement record that shows that you successfully refunded one of the transactions.
![One duplicate refunded (1)](assets/stripe-disputes-evidence-duplicate-approved-4.png)

#### Denied

To show proof that each transaction was a separate intentional purchase, begin by capturing your investigation summary.
![Not duplicate transactions (1)](assets/stripe-disputes-evidence-duplicate-denied-1.png)

Carefully compare both transactions, highlighting any differences (for example, SES-785ab12c90d3 and SES-785ab12c91e4), which indicate separate purchase attempts.
![Not duplicate transactions (2)](assets/stripe-disputes-evidence-duplicate-denied-2.png)

Highlight the time gap between transactions, showing that this is inconsistent with an accidental duplicate charge by the system.
![Not duplicate transactions (3)](assets/stripe-disputes-evidence-duplicate-denied-3.png)

Emphasize that the customer explicitly clicked **Complete Purchase** for both transactions, confirming intent to make two separate purchases.
![Not duplicate transactions (3)](assets/stripe-disputes-evidence-duplicate-denied-4.png)

## Fraudulent

The following visual evidence shows you how to perform comprehensive fraud analysis, which includes transaction legitimacy and authorization verification. To effectively counter a dispute in this category, adhere to this non-exhaustive list of best practices.

To show proof that a transaction wasn’t fraudulent, begin by summarizing your investigation.
![Fraudulent dispute example (5)](assets/stripe-disputes-evidence-fraudulent-5.png)

Reference location data, confirming the transaction originated from an IP address consistent with past orders and the billing address.
![Fraudulent dispute example (2)](assets/stripe-disputes-evidence-fraudulent-2.png)

If you have one, provide the fraud risk score that you assigned to the transaction, emphasizing that it was low risk. With this, include your customer’s verification details.
![Fraudulent dispute example (3)](assets/stripe-disputes-evidence-fraudulent-3.png)

Show that your customer performed or completed Address Verification System (AVS), CVV verification, and 3D Secure (3DS).
![Fraudulent dispute example (4)](assets/stripe-disputes-evidence-fraudulent-4.png)

Summarize the conclusion from your investigation.
![Fraudulent dispute example (1)](assets/stripe-disputes-evidence-fraudulent-1.png)

## General

The following visual evidence shows transaction details, pricing transparency, and customer communications.

#### Order confirmation and receipts

Provide a summary of evidence.
![Dispute order confirmation and receipts (1)](assets/stripe-disputes-evidence-general-order-confirmation-1.png)

Provide a copy of the receipt email, showing the order details, total amount, payment method, and transaction ID.
![Dispute order confirmation and receipts (2)](assets/stripe-disputes-evidence-general-order-confirmation-2.png)

Provide a record of the order confirmation screen shown to the customer immediately after completing the purchase.
![Dispute order confirmation and receipts (3)](assets/stripe-disputes-evidence-general-order-confirmation-3.png)

Include a transaction and dispute summary.
![Dispute order confirmation and receipts (5)](assets/stripe-disputes-evidence-general-order-confirmation-5.png)

#### POS data and system logs

Provide a summary of evidence.
![Dispute POS data and system logs (2)](assets/stripe-disputes-evidence-general-pos-data-2.png)

Provide a breakdown of how you displayed the pricing and taxes throughout the purchasing process.
![Dispute POS data and system logs (3)](assets/stripe-disputes-evidence-general-pos-data-3.png)

Show that you clearly presented the total amount to the customer before proceeding to payment.
![Dispute POS data and system logs (4)](assets/stripe-disputes-evidence-general-pos-data-4.png)

Include transaction details such as the transaction ID, date, and authorization code for verification.
![Dispute POS data and system logs (5)](assets/stripe-disputes-evidence-general-pos-data-5.png)

#### Customer communications

Provide a summary of evidence.
![Dispute customer communcations (2)](assets/stripe-disputes-evidence-general-customer-comms-2.png)

Show that the customer didn’t contact support regarding their billing concerns before filing the dispute.
![Dispute customer communcations (3)](assets/stripe-disputes-evidence-general-customer-comms-3.png)

Provide a record of the welcome email sent to the customer, confirming the purchase or subscription activation and total amount charged.
![Dispute customer communcations (4)](assets/stripe-disputes-evidence-general-customer-comms-4.png)

Add pre-purchase customer communications that show that you informed the customer about the total price.
![Dispute customer communcations (5)](assets/stripe-disputes-evidence-general-customer-comms-5.png)

## Product not received

The following visual evidence guides you through what you need to provide when responding to a _Product not received_ reason code. To effectively counter a dispute in this category, adhere to this non-exhaustive list of best practices.

#### Physical product

Cite your terms of service, including sections that touch on delivery confirmation and disputes.
![Physical product not received (1)](assets/stripe-disputes-evidence-product-not-received-physical-1.png)

Reference email notifications that show that you or the carrier informed the recipient before, during, and after delivery.
![Physical product not received (2)](assets/stripe-disputes-evidence-product-not-received-physical-2.png)

Include a photo of the delivery and your customer’s signature verification.
![Physical product not received (3)](assets/stripe-disputes-evidence-product-not-received-physical-3.png)

In the tracking history, mark up the delivery date, highlighting that the customer raised the dispute after the carrier delivered the product.
![Physical product not received (4)](assets/stripe-disputes-evidence-product-not-received-physical-4.png)

Include only relevant shipping information, such as the carrier, ship date, delivery date, tracking number, and status.
![Physical product not received (5)](assets/stripe-disputes-evidence-product-not-received-physical-5.png)

#### Digital product

Cite your terms of service, including sections that touch on delivery confirmation and activation records.
![Digital product not received (1)](assets/stripe-disputes-evidence-product-not-received-digital-1.png)

Reference email notifications that show that you informed the recipient before, during, and after delivery.
![Digital product not received (2)](assets/stripe-disputes-evidence-product-not-received-digital-2.png)

Attach your customer’s account activity log that shows they downloaded, activated, and accessed the digital product.
![Digital product not received (3)](assets/stripe-disputes-evidence-product-not-received-digital-3.png)

Add usage information that includes the product’s activation date and login sessions.
![Digital product not received (4)](assets/stripe-disputes-evidence-product-not-received-digital-4.png)

#### Service

Cite your terms of service, including sections that touch on service delivery and disputes.
![Service not received (1)](assets/stripe-disputes-evidence-product-not-received-service-1.png)

Add your communications with the customer that show the service’s scheduling date and completion date.
![Service not received (2)](assets/stripe-disputes-evidence-product-not-received-service-2.png)

Show a confirmation receipt that your customer completed the service.
![Service not received (3)](assets/stripe-disputes-evidence-product-not-received-service-3.png)

Include a service session log that captures when you scheduled the session, any reminders sent, and notes you took throughout the session.
![Service not received (4)](assets/stripe-disputes-evidence-product-not-received-service-4.png)

Attach information about the service delivery and fulfillment.
![Service not received (5)](assets/stripe-disputes-evidence-product-not-received-service-5.png)

## Product unacceptable

The following visual evidence guides you through what you need to provide when responding to a _Product unacceptable_ reason code. To effectively counter a dispute in this category, adhere to this non-exhaustive list of best practices.

#### Quality and functionality

Provide a summary of evidence.
![Quality and functionality unacceptable (1)](assets/stripe-disputes-evidence-product-unacceptable-quality-1.png)

Include any evidence to demonstrate the product functioned as advertised.
![Quality and functionality unacceptable (2)](assets/stripe-disputes-evidence-product-unacceptable-quality-2.png)

Provide any documentation or results to show the product met specifications before shipment.
![Quality and functionality unacceptable (4)](assets/stripe-disputes-evidence-product-unacceptable-quality-4.png)

Provide the original transaction details and dispute context.
![Quality and functionality unacceptable (5)](assets/stripe-disputes-evidence-product-unacceptable-quality-5.png)

#### Marketing materials

Provide a summary of evidence.
![Marketing materials (1)](assets/stripe-disputes-evidence-product-unacceptable-marketing-1.png)

Attach a feature verification summary that shows that all of the advertised features were fully functional, and that your customer used most of them.
![Marketing materials (2)](assets/stripe-disputes-evidence-product-unacceptable-marketing-2.png)

Add the entirety of your product listing at the time your customer purchased the product.
![Marketing materials (3)](assets/stripe-disputes-evidence-product-unacceptable-marketing-3.png)

#### Support and resolution

Provide a summary of evidence.
![Support and resolution (1)](assets/stripe-disputes-evidence-product-unacceptable-support-1.png)

Attach the terms and refund policy that your customer accepted when they purchased your product or service.
![Support and resolution (3)](assets/stripe-disputes-evidence-product-unacceptable-support-3.png)

Provide support ticket logs showing the customer successfully used the product or didn’t report functionality issues.
![Support and resolution (4)](assets/stripe-disputes-evidence-product-unacceptable-support-4.png)

Add resolution notes that indicate that you resolved the issue to the customer’s satisfaction.
![Support and resolution (5)](assets/stripe-disputes-evidence-product-unacceptable-support-5.png)

## Subscription canceled

The following visual evidence shows subscription terms and policies, cancellation records, and continued usage after alleged cancellation. To effectively counter a dispute in this category, adhere to this non-exhaustive list of best practices.

#### Terms and policies

Include evidence that the customer received and agreed to your terms at the time of signup.
![Terms and policies (2)](assets/stripe-disputes-evidence-subscription-canceled-terms-2.png)

Provide the subscription terms the customer agreed to, including renewal, cancellation, and refund policies.
![Terms and policies (3)](assets/stripe-disputes-evidence-subscription-canceled-terms-3.png)

Summarize the evidence that supports your case.
![Terms and policies (1)](assets/stripe-disputes-evidence-subscription-canceled-terms-1.png)

#### Cancellation records

Highlight that you automatically send a confirmation email when a customer cancels their subscription.
![Cancellation records (2)](assets/stripe-disputes-evidence-subscription-canceled-records-2.png)

Outline the available cancellation methods, including self-service cancellation through customer account settings, and cancellation requests through customer support.
![Cancellation records (3)](assets/stripe-disputes-evidence-subscription-canceled-records-3.png)

Highlight that the subscription has been active and billed regularly without cancellation attempts.
![Cancellation records (4)](assets/stripe-disputes-evidence-subscription-canceled-records-4.png)

Summarize the evidence that supports your case.
![Terms and policies (1)](assets/stripe-disputes-evidence-subscription-canceled-terms-1.png)

#### Usage and communications

Provide a record of the renewal reminder email sent to the customer before the billing date.
![Usage and communcation (2)](assets/stripe-disputes-evidence-subscription-canceled-usage-2.png)

Provide a record of subscription-related emails sent to the customer, including renewal reminders and payment receipts.
![Usage and communcation (4)](assets/stripe-disputes-evidence-subscription-canceled-usage-4.png)

Provide service usage logs that show your customer made no cancellation requests within the disputed period.
![Usage and communcation (5)](assets/stripe-disputes-evidence-subscription-canceled-usage-5.png)

Summarize the evidence that supports your case.
![Terms and policies (1)](assets/stripe-disputes-evidence-subscription-canceled-terms-1.png)
