<!-- Source URL: https://docs.stripe.com/billing/subscriptions/trials/compliance -->
<!-- Fetched: 2026-05-12 -->

# Manage compliance requirements for trials and promotions

Learn how to comply with card network requirements for trial offers.

You must comply with [card network requirements](https://stripe.com/payment-method/visa) when you use trial offers. This includes scenarios such as free trials and temporarily discounted rates that convert to a normal rate. Use this guide to help you stay compliant when you use trials.

## Notify customers with trial end reminder emails

Send your customers Stripe-hosted trial-end reminder emails, or opt to send your own hosted emails.

### Stripe-hosted reminder emails

You can enable [messaging settings](https://dashboard.stripe.com/settings/billing/automatic) in the Stripe Dashboard to help you meet the requirements. To send a reminder email prior to the end of the trial, select the **Link to a Stripe-hosted page** option in the [Subscriptions and emails setting](https://dashboard.stripe.com/settings/billing/automatic). The reminder email contains a link for the customer to add or update their payment details. We don’t send trial reminder emails in a [sandbox](https://docs.stripe.com/sandboxes.md). Learn more about how to [set up free trial reminders](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md#trial-ending-reminders).

### Self-hosted reminder emails

You can also use the [trial_will_end](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.trial_will_end) event to send your own hosted emails to customers. When you see the event in your Dashboard, it means your email was sent. If you notify users of [successful payments](https://dashboard.stripe.com/settings/emails), Stripe automatically displays information about the trial and the cancellation URL in those notifications. If you don’t use these settings, you’re still responsible for complying with the requirements.

### Reminder timing and default behavior

When customer emails are enabled, we send a reminder 7 days before a trial ends. If a trial is less than 7 days, we send the reminder email as soon as the trial begins. If trials renew, we send another reminder email.

If both trial reminders and subscription renewal reminders are enabled during a trial, customers only receive the trial ending reminder. We send renewal emails for subsequent billing periods.

## Cancel a trial

The cancellation policy link is a URL displays on customer receipts, along with other trial information. All card payments include this information. We also include the cancellation URL in the reminder email that we send to customers 7 days before their trial ends. Customers can also view, manage, and cancel a trial in the [customer portal](https://dashboard.stripe.com/test/settings/billing/portal).

When you use trial offers, your subscriptions might include trial offers such as discounted or free items, along with regular price items. You can remove a trial offer from a subscription to update the subscription rather than canceling the entire subscription.

## Manage trial text in statement descriptors

You can manage statement descriptors for the following scenarios:

- **Manual statement descriptors**: If you manually set the [statement descriptor](https://docs.stripe.com/api/invoices/object.md#invoice_object-statement_descriptor) on an invoice, you need to add the trial text as well.
- **Product statement descriptors**: If you use [product statement descriptors](https://docs.stripe.com/api/products/object.md#product_object-statement_descriptor), the trial text is appended automatically.
- **Account statement descriptors**: If you don’t manually set the statement descriptor or use product statement descriptors, the trial text is appended to your account’s statement descriptor. If needed, you can set up a shortened descriptor to make sure the trial text displays correctly.

> If your statement descriptor is greater than 10 characters, make sure it still makes sense to your customers with the trial text appended. Statement descriptors have a 22 character limit, so anything after the 10th character is overwritten with `* TRIAL OVER`.

## Meet requirements without using Stripe features

If you offer trials or promotions without using trials features, you still need to comply with the [requirements](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide). You can listen for the [invoice.upcoming event](https://docs.stripe.com/api/events/types.md#event_types-invoice.upcoming) to determine when to send email notifications. To add text to your statement descriptor that indicates the promotion is over:

- Listen for the [customer.subscription.updated](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.updated) event
- Check to see if a trial or promotion has ended
- Update the statement descriptor on the subscription’s latest_invoice

You need to update the latest invoice within an hour of its creation while it’s still in `draft` status.
