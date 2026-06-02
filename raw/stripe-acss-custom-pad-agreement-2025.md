<!-- Source URL: https://docs.stripe.com/payments/acss-debit/custom-pad-agreement -->
<!-- Fetched: 2026-05-02 -->

# Custom Canadian pre-authorized debit mandate agreements

> It’s unlikely your business needs to create a custom mandate agreement. By default, the Stripe.js library provides an all-in-one solution for your customers to provide and verify their bank account and accept a valid mandate.

## When to use a custom mandate agreement

You can create a custom mandate agreement for the following scenarios:

- You want to obtain authorization from your customer to not send debit notification emails
- You want to provide different or additional cancellation or recourse terms that satisfy [Payments Canada rules](https://www.payments.ca/sites/default/files/h1eng.pdf)

The mandate agreement provided by default is specifically written to serve the needs of almost all businesses on Stripe. It uses the most flexible timelines for confirmation and cancellation allowed by Canadian banks and satisfies all requirements given by the [Payments Canada Rules for pre-authorized debits](https://www.payments.ca/sites/default/files/h1eng.pdf). Though there are very few reasons to create a custom agreement, not all businesses are the same. This page will help your business create a valid mandate agreement that will protect both you and your customers.

## When not to use a custom mandate agreement

You *don’t* need to create a custom mandate agreement for the following:

- Sending customized emails: You can send customized emails using the same mandate agreement text in the customer payment details collection solution. Match the same text that Stripe provides in your own emails.
- Specifying custom payment schedule terms: If you want to specify a custom payment schedule, you can use the Stripe API. The mandate agreement automatically displayed to your customers will use the payment schedule terms you provide.

## Background

In addition to collecting a customer’s name and bank account information, you must collect a specific debit mandate (often called a pre-authorized debit agreement). This mandate gives your business authorization to debit the customer’s bank account on a specified schedule. Your business must present and collect a mandate agreement with clear and specific terms for one-time or recurring debits that meets the requirements given by the [Payments Canada rules](https://www.payments.ca/sites/default/files/h1eng.pdf).

Parts of the agreement will be pre-defined based on the mandate you create [with the Stripe API](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md#web-create-payment-intent) (for example the `interval_description` defining your payment timeline or triggers) and existing information about your customers. This page will guide you through the remaining required parts of a mandate agreement, but your business will ultimately be responsible for any disputes arising from its contents.

After your customer accepts the mandate agreement, you can immediately debit the first payment due from your customer’s account. You must send your customer confirmation of the accepted mandate agreement, including collected payment details. The mandate agreement must include terms that allow you to immediately debit the bank account and send the confirmation within 5 days after your customer has accepted the mandate agreement. By default, Stripe sends a [customizable agreement confirmation email](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails) matching the [sample below](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement.md#sample-pre-authorized-debit-agreement).

Pre-debit notification emails informing your customer that a charge is being made and the amount of the charge is a requirement, as well. However, the time limit for these can be modified or they can be waived entirely in the agreement.

## Mandate agreement requirements

A properly formatted PAD mandate agreement must include the following information in order to meet regulatory requirements:

| Requirement                  | Description                                                                                                                                                         | Example Text |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Business Contact Information | The mandate agreement must contain accurate contact information that the customer can use to contact your business by a method of communication your customer uses. | Rocket Rides |

Attn: Billing Department

123 First Avenue

Toronto, ON

M2J 3R7

Email: billing@rocket-rides.com |
| Date of Agreement Acceptance | Somewhere in the agreement presented to customer, the date of the agreement acceptance must be shown. | Accepted on: April 8, 2024 |
| Pre-authorized debit Type | This value is determined by the type of transaction for which you are collecting this mandate agreement. It must be based on the mandate object `transaction_type` value. | - Personal

- Business |
  | Authority to Debit Account with Variable Amounts | A clear statement outlining your customer’s agreement that your business is authorized to debit the account given. | By clicking [“submit application”, “submit” or “I accept”], you accept this agreement and authorize *Rocket Rides* to debit the specified bank account for any amount owed for charges resulting from the use of services or purchase of products. |
  | Payment Schedule or Triggers | Required only if [Mandate](https://docs.stripe.com/api/mandates.md) `payment_schedule` is `interval` or `combined`.

The mandate agreement must display the [Mandate](https://docs.stripe.com/api/mandates.md) `interval_description` value, which should contain an explicit schedule of payments or triggering events for debits. | - On the 5th of every month or the next business day.

- On April 30, 2020.
- When issued invoices become due.
- When your RocketBucks balance goes below $20. |
  | Sporadic Authorization | Required only if [Mandate](https://docs.stripe.com/api/mandates.md) `payment_schedule` is `sporadic` or `combined`.

The mandate agreement must state that your business will obtain authorization (such as providing a username and password) from your customer for each sporadic payment you process. | *Rocket Rides* may debit the specified account for sporadic payments only after obtaining your authorization. |
| Modification of PAD Confirmation Period | In order to improve the speed with which you can do business, Stripe performs verification on customer bank accounts that allows your business to begin debiting after a PAD is accepted so long as the Customer has agreed to this in the mandate agreement. | You agree that any payment due will be debited from your account immediately upon acceptance of this PAD agreement and that confirmation of this PAD agreement will be sent within five calendar days after acceptance. |
| Modification of Pre-Notification Period | Stripe supports the ability to send required pre-debit notification emails to your customer (or provide webhooks that notify you to send them) when debits are initiated. Your customer must agree to waive the pre-notification period. This text must be bolded, highlighted or underlined in the mandate agreement text.

Pre-notifications are required if not expressly waived. If you opt out of sending these emails, the text for waiving the pre-notification must be included instead, also bolded, highlighted or underlined. | - **You waive the right to receive pre-notification and prior confirmation of the amount or timing of any PAD.**

- **You additionally agree that you don’t require advance notice of the amount or timing of any PAD before Rocket Rides processes the debit.** |
  | Recourse / Reimbursement Statement | The mandate agreement must contain this exact text in its entirety. | You have certain recourse rights if any debit doesn’t comply with this PAD agreement. For example, you have the right to receive reimbursement for any debit that isn’t authorized or isn’t consistent with this PAD Agreement. To obtain more information on your recourse rights, contact your financial institution or visit [www.payments.ca](https://www.payments.ca/). |
  | Cancellation of Agreement | A statement outlining a customer’s ability to revoke their authorization at any time, specifying an amount of notice required by your business. | You can amend or cancel this authorization at any time by providing the business with thirty days’ prior notice at *billing@rocket-rides.com*. To obtain a sample cancellation form, or further information on canceling a PAD agreement, contact your financial institution or visit [www.payments.ca](https://www.payments.ca/). |
  | Notice of Use of a Payment Service Provider | The mandate agreement must disclose Stripe as the payment service provider. | *Rocket Rides* partners with [Stripe](http://stripe.com) to provide payment processing. |

## Sample pre-authorized debit mandate agreement

This sample document illustrates what a complete mandate agreement might look like, both in your payment flow and in the confirmation email sent to your customers.
