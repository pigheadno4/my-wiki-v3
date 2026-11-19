<!-- Source URL: https://docs.stripe.com/payments/customer-balance/reconciliation -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Reconciliation

Learn about how Stripe reconciles the customer balance to payments and invoices.

Stripe offers the `automatic` or `manual` reconciliation behavior for funds in the cash balance.

By default, Stripe applies the automatic reconciliation mode to the cash balance of all of your customers. You can use the Bank Transfers [reconciliation settings](https://dashboard.stripe.com/settings/bank_transfers) to change the reconciliation behavior for everyone.
![Bank Transfer reconciliation settings](https://b.stripecdn.com/docs-statics-srv/assets/bank-transfer-reconciliation-settings.930a07d8937809fddf187138649fc419.png)

Bank Transfer reconciliation settings

## Automatic cash balance reconciliation 

By default, Stripe automatically applies any available cash balance to PaymentIntents and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s `open` and either hasn’t passed its due date or became overdue within the last 365 days.

Automatic reconciliation considers the customer’s entire available cash balance in the payment currency, including unreconciled funds from earlier bank transfers. For reference matching, Stripe applies no more than the amount of the bank transfer that triggered reconciliation. If reference matching doesn’t use all available funds, the remaining reconciliation steps consider the rest of the available cash balance.

#### USD, EUR, and other currencies

This applies to bank transfers in the US, UK, EU, and MX.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching [invoice number](https://docs.stripe.com/api/invoices/object.md#invoice_object-number).
2. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s [display_bank_transfer_instructions](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference) field.
3. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount available in the cash balance. For multiple valid combinations, Stripe prioritizes as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
4. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest due ones first.
5. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

#### JPY

Stripe applies funds in the following order:

1. We try to find a group of between one and five invoices and PaymentIntents that are waiting for the exact amount available in the cash balance. If there are multiple valid combinations, we prioritize as follows:
   - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
   - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
   - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.
2. If we’re unsuccessful in finding a group that sums to the exact funding available, we fund as many invoices that can be fully funded in order of finalization time, oldest first.
3. If any funding remains, Stripe applies funds to incomplete PaymentIntents in order of confirmation time, oldest first.

### Partial payments and invoice finalization

When funds arrive, Stripe can partially fund an incomplete PaymentIntent. For invoices, Stripe only applies an incoming bank transfer as a partial payment when you enable automatic partial reconciliation and your customer includes the invoice number in the transfer memo.

When you finalize an invoice, Stripe also checks the customer’s existing cash balance. Stripe applies the balance if it can fully pay the invoice after accounting for your configured underpayment threshold. If the available balance is less than that amount, Stripe leaves the funds in the cash balance instead of partially applying them to the newly finalized invoice.

## Override reconciliation behavior  

You can use the Dashboard or API to override the Bank Transfers reconciliation settings for a specific customer.

To override a customer’s reconciliation behavior in the Dashboard:

1. Select the customer, then find **Cash Balance** in the **Payment methods** section.
2. Expand the overflow menu (⋯) next to the cash balance details.
3. From the expanded options, select **Change reconciliation mode**. This displays a modal that allows you to change the reconciliation behavior for the customer.
![Cash Balance section on the Customer page](https://b.stripecdn.com/docs-statics-srv/assets/cash-balance-settings.fbc9cb0a50beaf42ab1ff6baab7dc09f.png)

The Cash Balance section on the Customer page

To override a customer’s reconciliation behavior using the API, set the customer’s [reconciliation mode](https://docs.stripe.com/api/customers/object.md#customer_object-balance_settings-reconciliation_mode) to `manual`.

> #### Accounts v2 considerations
> 
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the [Accounts v2 preview](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md), you need to [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
> 
> To manage the cash balance settings, including reconciliation mode, for a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer), use the Customers API endpoint with the `Account` ID as the path parameter, for example `v1/customers/acct_xxxxx`.

```curl
curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "cash_balance[settings][reconciliation_mode]=manual"
```

To point the reconciliation mode for an overridden customer back to the user’s default, you can do so in the Dashboard. You can also use the API to set the [reconciliation mode](https://docs.stripe.com/api/customers/object.md#customer_object-balance_settings-reconciliation_mode) on the customer to `merchant_default`.

## Manual cash balance reconciliation 

When manual reconciliation is enabled on a customer, Stripe doesn’t automatically apply any funds from the customer balance.

You can apply funds from the customer balance manually using either the API or the Dashboard.

For both the API and the Dashboard, you can apply funds to an incomplete or partially funded PaymentIntent, or an open Invoice. You can also fund Invoices that are still open but marked overdue with this method.

#### Dashboard

In the Dashboard, you can apply funds to a PaymentIntent on the Payments page or on the page for the individual payment.

To fund a PaymentIntent from the Payments page, find the payment you want to fund, select the overflow menu (⋯), then click **Fund from cash balance**.
![The overflow menu for a single Payment on the Stripe Dashboard Payments page](https://b.stripecdn.com/docs-statics-srv/assets/fund-from-cash-balance-payments-list.16be7818811602d966d2ce4f1aadbc0f.png)

To fund a PaymentIntent from the page for the individual payment, click the **Fund from cash balance** button.

In both cases, selecting the **Fund from cash balance** button prompts you to confirm the payment. This button doesn’t appear on either page if the customer doesn’t have any funds available on their cash balance.

To apply funds to an invoice, go to the **Invoice** page, click the **Charge customer** button, and then select **Cash Balance** as the payment method.

You can partially or fully fund an invoice using the Dashboard. This option allows you to pay a portion of the invoice, if the customer doesn’t have sufficient funds on their cash balance to fully pay the invoice.

#### API

To apply funds using the API:

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}}/apply_customer_balance \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1500 \
  -d currency=usd
```

The amount is optional. When omitted, the amount defaults to the remaining amount requested on the PaymentIntent.

### Example

The following code is an example of a full pass of manual reconciliation. You receive the `customer_cash_balance_transaction.created` webhook, check whether the transaction represents new funds (type `funded`), find PaymentIntents that are awaiting funding, and use the funds available to reconcile the open PaymentIntents.

The `customer_cash_balance_transaction.created` event contains a single [CustomerCashBalanceTransaction](https://docs.stripe.com/api/cash_balance_transactions/object.md) object with transaction-level detail, including the `currency` and `customer` for each funding event.

> #### Accounts v2 considerations
> 
> To retrieve the cash balance for a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer), pass the `Account` ID instead of the `Customer` ID. Expand the `Customer` object returned in the event to get the associated `Account` ID from its [customer_account](https://docs.stripe.com/api/customers/object.md#customer_object-customer_account) property.

#### Ruby

```ruby
require 'stripe'
require 'sinatra'

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

post '/webhook' do
  sig_header = request.env['HTTP_STRIPE_SIGNATURE']
  endpoint_secret = ENV['ENDPOINT_SECRET']
  payload = request.body.read

  begin
    event = Stripe::Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  rescue JSON::ParserError => e
    status 400
    return
  rescue Stripe::SignatureVerificationError => e
    status 400
    return
  end

  case event['type']
    when 'customer_cash_balance_transaction.created'
    # The event contains a CustomerCashBalanceTransaction object with details
    # about the specific transaction, including currency and customer.
    transaction = event['data']['object']
    customer_id = transaction['customer']
    currency = transaction['currency']

    # Only process funded transactions (bank transfers adding funds).
    if transaction['type'] != 'funded'
      status 200
      return
    end

    # Getting all PaymentIntents for a customer.
    customer_payment_intents = client.v1.payment_intents.list({customer: customer_id})['data']

    # We can order the funding of PaymentIntents in whichever order we like - here we'd
    # like to pay the oldest first.
    customer_payment_intents = customer_payment_intents.sort_by { |payment_intent| payment_intent['created'] }

    # Filter for fundable PaymentIntents in the same currency as the transaction.
    fundable_intents = customer_payment_intents.select do |payment_intent|
      allowed_payment_methods = payment_intent['payment_method_types']
      awaiting_further_payment = ['requires_payment_method', 'requires_action'].include? payment_intent['status']
      payment_intent['currency'] == currency and awaiting_further_payment and allowed_payment_methods.include? 'customer_balance'
    end

    # Attempt to fund every fundable PaymentIntent. Each time we fund a PaymentIntent,
    # we re-check the cash balance to make sure funds remain for the next one.
    cash_balance = client.v1.customers.retrieve_cash_balance(customer_id)
    fundable_intents.each do |payment_intent|
      if cash_balance['available'][currency] == 0
        break
      end
      client.v1.payment_intents.apply_customer_balance(payment_intent['id'])
      cash_balance = client.v1.customers.retrieve_cash_balance(customer_id)
    end
  end
end
```

## Unreconciled cash balance funds 

Sometimes funds in the customer balance remain unreconciled—for example, when a customer sends too much money and you haven’t created any more PaymentIntents or Invoices for that customer.

To reconcile outstanding funds in the customer cash balance, you can either create a new PaymentIntent or invoice to accept a payment, or return the funds to the customer.

> You’re responsible for making sure that you reconcile customer cash balances promptly and accurately. Reconcile outstanding customer balances quickly, rather than leaving them in your account for an extended period.

Stripe periodically sends a reminder email when you have unreconciled balances in your account to make sure that you can review these unreconciled funds. If funds remain unreconciled for 75 days, Stripe automatically attempts to return the aged portion to the customer’s bank account. A return can fail if the customer’s bank can’t process it (for example the bank account is closed).

Newer funds remain in the cash balance and follow their own 75-day timeline. When Stripe doesn’t have the customer’s account information, Stripe might reach out to the customer directly to initiate the return. If the aged funds remain at the 90-day mark, we transfer that portion to your Stripe account balance. The 90-day action isn’t another return attempt. Coordinate directly with the customer to make sure they receive the returned funds.

You can see the full list of customers who have unreconciled cash balances and the date that we’ll return them to the customer in your [Dashboard](https://dashboard.stripe.com/test/customers?tab=remaining_balance).
![Remaining customer balances filter](https://b.stripecdn.com/docs-statics-srv/assets/remaining-customer-balances-filter.cf053bcd3a49b97efaf8bf11537e4b65.png)

Remaining customer balances filter

## Credit balance 

*Credit balance* is handled differently from cash balance. Customer credit balance is an *Invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice)-only feature which represents liability between you and the customer. When an invoice is finalized, the customer’s credit balance is applied to the invoice, decreasing the amount due.

For more information on credit balances, see [Customer Credit Balance](https://docs.stripe.com/invoicing/customer/balance.md).
