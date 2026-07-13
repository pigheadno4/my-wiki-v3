<!-- Source URL: https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/india-e-mandates.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# India e-mandate support for Stripe invoices

> Invoice Indian credit cards using RBI-compliant Stripe mandates.

In accordance with RBI pre-authorization requirements, this feature users to charge customers with Indian credit cards using Stripe mandates. After a mandate is active, Metronome will use it for eligible off-session charges.

## Setup

### 1. Collect the customer's payment method and create the mandate via SetupIntent

When collecting the user's card on-session, create a mandate using a Stripe `SetupIntent`. The user completes authentication during confirmation, and Stripe creates the mandate for that payment method.

```bash theme={null}
curl https://api.stripe.com/v1/setup_intents \
  -u sk_test_...: \
  -d customer=cus_123 \
  -d payment_method=pm_123 \
  -d confirm=true \
  -d "payment_method_options[card][mandate_options][amount_type]"=maximum \
  -d "payment_method_options[card][mandate_options][amount]"=500000 \
  -d "payment_method_options[card][mandate_options][currency]"=inr \
  -d "payment_method_options[card][mandate_options][interval]"=sporadic \
  -d "payment_method_options[card][mandate_options][reference]"=AUTO_RECHARGE_123 \
  -d "payment_method_options[card][mandate_options][start_date]"=1735689600
```

**For threshold billing customers:**

* Set `interval` to `sporadic` — recharges are triggered by a balance threshold, not a fixed cadence.
* Set `amount_type` to `maximum` - support varying charge amounts.
* Set `amount` to a sufficiently high value - account for variance in recharge amounts over time.

**For subscriptions and recurring fees (e.g. monthly PayGo):**

* Set `interval` to the corresponding recurrence (e.g. `month`).
* Set `amount_type` to `fixed` if the recurring fee is known, or `maximum` if it is variable.
* Set `amount` to the known recurring fee or a sufficiently high maximum.

### 2. Wait for the mandate to become active

A mandate may remain in `pending` for up to 30 minutes after creation. You can check readiness in two ways:

* Listen to the `mandate.updated` webhook from Stripe and wait until `status` becomes `active`.
* Retrieve the mandate by ID from the `SetupIntent` and poll until it is `active`.

If the mandate transitions to `inactive`, it cannot be used. The customer will need to authorize a new mandate.

### 3. Create and map the mandate custom field

On the Metronome contract, create a custom field (e.g. `stripe_mandate_id`). Via the entity mapping UI, map this contract custom field to the Stripe `invoice.payment_settings` → `default_mandate` field.

### 4. Provision the customer in Metronome

Create the Metronome contract. Populate the `stripe_mandate_id` custom field with the mandate ID created in step 1. All invoices sent to Stripe will attempt to attach this mandate.

### 5. Listen for the `action_required` webhook

After the invoice is created with the associated mandate, the `paymentIntent` may transition to an `action_required` state. Stripe will issue a [`invoice.payment_action_required` webhook](https://docs.stripe.com/api/events/types#event_types-invoice.payment_action_required).

### 6. Confirm payment

* If the customer approves the charge, the payment succeeds and the balance is released.
* If the customer does not respond or the mandate becomes inactive, the payment fails and enters the normal failure workflow. A new mandate must be collected and activated before future recharge attempts can succeed.

## Limitations

* Mandates must be created and managed entirely in Stripe. Metronome does not expose an API for interacting with mandates other than returning the set custom field value.
* Mandates must be set up via a `SetupIntent` since all charges, including the first one, are off-session.
* Metronome does not manage mandate lifecycle events. Payment failures are surfaced through the normal webhook and failure path. It is your responsibility to update the mandate in Stripe and take appropriate action before retrying.

## Relevant documentation

* [Stripe guide for RBI e-mandates](https://docs.stripe.com/india-recurring-payments)
