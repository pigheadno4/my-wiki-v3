<!-- Source URL: https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts -->
<!-- Fetched: 2026-05-11 -->

# Minimum balances for automatic payouts

Set a minimum balance in your Stripe account to manage cash flow and cover potential refunds, disputes, and fees.

Automatic payouts default to paying out your entire available balance according to your set schedule. This can result in insufficient funds to manage your payments business on Stripe, preventing you from processing refunds or disputes.

Minimum balances for automatic payouts let you keep a specified amount in your Stripe account after an automatic payout. Automatic payouts only pay out funds exceeding this minimum balance to your bank account. This helps minimize the risk of a negative balance due to refunds, disputes, or fees after automatic payouts. You can use **Minimum Balances** to help:

- Improve your cash flow management by keeping a balance to cover refunds, disputes, and fees.
- Receive comprehensive reconciliation reports with automatic payouts, including the minimum balance you’ve set.

> Only use minimum balances to cover anticipated refunds, disputes, and fees. Not supported in Brazil, India, and Thailand.

## Set up minimum balances

Minimum balances work with all automatic payout schedules. If you dip below the set minimum balance, Stripe attempts to renew first by using your available balance. If you have no available balance, we use your incoming funds instead.

To set up a minimum balance:

1. Log in to the Dashboard. **Minimum Balances** are only available when you have access to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payouts).
1. Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts). Under the **Minimum Balance** section, toggle the option on, and set a fixed amount.
1. Specify the amount you want to keep as a minimum balance. This amount remains in your account to cover potential refunds, disputes, and fees.
1. Save your settings. Your automatic payouts will now retain the specified minimum balance.
   ![Minimum balance settings in the Dashboard](assets/stripe-payouts-minimum-balance.png)

## Manage minimum balances

You can update the minimum balance as needed:

1. Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts).
1. Under the **Minimum Balance** section, change the amount. If you choose a lower amount to keep as a minimum balance, we include the released funds on your next scheduled payout. If you choose a higher minimum balance, we accumulate from new incoming payments. Regularly check your balance to verify it aligns with your business needs.

You can also disable your **Minimum Balance** in the Dashboard:

1. Navigate to [Payout Settings](https://dashboard.stripe.com/settings/payouts).
1. Under the **Minimum Balance** section, set the amount to 0 or toggle the option off. When you turn off minimum balances, Stripe no longer retains the specified minimum balance during automatic payouts. Your entire available balance will be disbursed according to your payout schedule.

> #### Note
>
> Consider setting a minimum balance that covers your typical refund, dispute, and fee amounts. We generally recommend four to five times your average daily processing volumes, as this has proven effective in maintaining healthy cash flow.

## Negative balances

With a **Minimum Balance** in place, the likelihood of a [negative balance](https://support.stripe.com/embedded-connect/questions/handling-negative-balances) is significantly reduced. However, if you process refund amounts greater than your minimum balance amount at any given time, your balance becomes negative. To learn more about handling negative balances, see [Fix a negative balance](https://support.stripe.com/questions/fix-the-negative-balance-on-your-account).

## Reconciliation reports

When you enable **Minimum Balance**, your [Payout Reconciliation Report](https://docs.stripe.com/reports/payout-reconciliation.md) displays the amount retained due to the minimum balance. This helps you see how the minimum balance affects your payouts and transactions. The timing of your reconciliation reports remains unchanged. The reports shows the total payout and the amount retained based on the minimum balance.

The following sections illustrate how Stripe pays out and reconciles an account with a set minimum balance using USD as example currency, workings for other currencies will be the same:

- Total Balance: 30,000 USD
- Minimum Balance: 10,000 USD
- Payout Amount: 20,000 USD (30,000 USD Total Balance - 10,000 USD Minimum Balance)

Stripe initiates an automatic payout of 20,000 USD to your linked bank account. The minimum balance of 10,000 USD remains in your Stripe account. You can see the [Balance Transaction API](https://docs.stripe.com/api/balance_transactions.md) for more details on the hold made for the minimum balance.

Your reconciliation report shows the following details:

- All transactions leading up to the total balance of 30,000 USD
- A transaction for the retained amount of -10,000 USD (your selected Minimum Balance)
- Results in a total payout amount of 20,000 USD

## Minimum balances for platforms

As a platform, you can follow the same steps to [set your minimum balance](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md#set-up-minimum-balances) in the Dashboard. Set a platform minimum balance that covers negative balances and refunds for your connected accounts.

You can also programmatically configure minimum balances **per connected account** with the [Balance Settings API](https://docs.stripe.com/api/balance-settings/update.md).

> After you set a minimum balance for your connected accounts, their payouts differ from the amounts shown on their balance. We recommend you reach out to your customers before setting a minimum balance to explain the purpose and effects.

### Set and update minimum balances

You can set new minimum balances, add currencies to existing configurations, update amounts, and modify settings for your connected accounts.

#### Set minimum balances

To configure minimum balances for your connected accounts, provide the currency codes and amounts in the _minor currency unit_ (The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency)).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const balanceSettings = await stripe.balanceSettings.update(
  {
    payments: {
      payouts: {
        minimum_balance_by_currency: {
          usd: 1500,
          cad: 8000,
        },
      },
    },
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

#### Add a minimum balance for a new currency

To add a minimum balance for a new currency to a connected account that already has other currencies configured, provide the new currency code and amount:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const balanceSettings = await stripe.balanceSettings.update(
  {
    payments: {
      payouts: {
        minimum_balance_by_currency: {
          eur: 5000,
        },
      },
    },
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

This parameter uses a merge mechanism, which allows you to add a new currency without affecting existing minimum balance settings. For example, if a connected account has minimum balances for USD and CAD, when you add EUR, the updated configuration contains all three currencies.

### Before

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

### After

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000,
        "eur": 5000
      },
      ...
    },
    ...
  }
}
```

#### Update an existing minimum balance amount

To change the amount for an existing currency’s minimum balance, pass the new value using the same currency code. For example, you can update a connected account with an existing minimum balance of 15 USD to 30 USD:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const balanceSettings = await stripe.balanceSettings.update(
  {
    payments: {
      payouts: {
        minimum_balance_by_currency: {
          usd: 3000,
        },
      },
    },
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

### Before

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

### After

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 3000,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

### Delete minimum balances

You can delete a single currency’s minimum balance or clear all minimum balance settings at once.

#### Delete a single currency’s minimum balance

To remove the minimum balance for a specific currency, pass the currency code with an empty string as its value:

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][minimum_balance_by_currency][usd]="
```

### Before

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

### After

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

#### Delete all minimum balances

To delete all minimum balance settings at once, pass an empty string as the value for the entire `minimum_balance_by_currency` parameter:

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][minimum_balance_by_currency]="
```

### Before

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

### After

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": null,
      ...
    },
    ...
  }
}
```

### Retrieve minimum balances

To view the current minimum balance configuration for a connected account:

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const balanceSettings = await stripe.balanceSettings.retrieve({
  stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
});
```

```json
{
  "object": "balance_settings",
  ...
  "payments": {
    "payouts": {"minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      ...
    },
    ...
  }
}
```

## See also

- [Receiving payouts](https://docs.stripe.com/payouts.md)
