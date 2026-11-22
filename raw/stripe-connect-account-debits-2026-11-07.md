<!-- Source URL: https://docs.stripe.com/connect/account-debits -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Debit connected accounts

Collect funds from a connected account by debiting its Stripe balance.

At times, your platform might need to collect funds from your connected accounts:

- To collect fees directly related to processing payments on your platform
- To recover funds for a previous refund
- To make other adjustments to connected [account balances](https://docs.stripe.com/connect/account-balances.md) (for example, to correct an error)

When [your platform is responsible for negative balances](https://docs.stripe.com/connect/risk-management.md#identify-negative-balance-responsibility) you can debit a connected account’s Stripe balance, transferring funds to your platform balance.

> To bill connected accounts where Stripe is responsible for negative balances, create a customer for each connected account and [charge them using Stripe Billing subscriptions](https://docs.stripe.com/connect/subscriptions.md#connected-account-platform).

This creates a `Transfer` on the connected account and a `Payment` on the platform account.

## Requirements

This functionality is only supported for connected accounts where [your platform is responsible for negative balances](https://docs.stripe.com/connect/risk-management.md#identify-negative-balance-responsibility). Additionally:

- Using Account Debits incurs an [additional cost](https://stripe.com/connect/pricing).
- Using Account Debits requires getting legally binding consent from your connected accounts.
- Both your platform and the connected account must be in the same region (for example, both are in Japan).
- The `currency` value must match the default currency of the connected account.
- Debiting an account can’t make the connected account balance become negative unless you have [reserves enabled](https://docs.stripe.com/connect/account-balances.md#understanding-connected-reserve-balances) (on by default for all new platforms created after January 31, 2017) and have a bank account in the same currency as the debit.
- If a connected account has a [negative balance](https://docs.stripe.com/connect/account-balances.md#accounting-for-negative-balances), Stripe might auto-debit the external account on file, depending on what country the connected account is in. If the external account hasn’t been verified, the debit can fail.
- The maximum `amount` is 100,000 USD (or equivalent in your currency).

## Availability

Account debits are available for platforms and connected accounts according to whether they’re in the same region (domestic) or cross-border regions (international).

### Domestic availability

You can use account debits when the platform and connected account are both in one of the following regions:

- Americas: US, CA
- Asia Pacific: JP, AU, HK, NZ
- Europe: SEPA countries (EU and UK)

### International availability

You can use cross-border account debits when the platform and connected account match the following corridors:

| Platform region | Connected account region |
| --- | --- |
| US | HK |
| UK | EU, CH, NO |
| EU | UK, CH, NO |
| AU | NZ |
| CH | EU, NO |
| NO | EU, CH |

If you’re interested in other regions, contact our [sales team](https://stripe.com/contact/sales).

## Charge a connected account 

#### Dashboard

To pull funds from a connected account:

1. Navigate to the **Account balances** page for the connected account.
2. Click **Pull funds**.
3. Select the amount to charge.
4. Click **Pull**.

#### API

The [create a charge](https://docs.stripe.com/api.md#create_charge) API call supports providing a connected account ID as the `source` value:

```curl
curl https://api.stripe.com/v1/charges \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1500 \
  -d currency=usd \
  -d "source={{CONNECTEDACCOUNT_ID}}"
```

The API call returns the `Payment` created on the platform account. It doesn’t return a `Charge`.

This approach is appropriate for platforms that charge their connected accounts for goods and services (that is, for using the platform). For example, a platform can charge its connected accounts for additional fees or services through their Stripe balance, minimizing any need to collect an additional payment method and allowing for nearly instant availability of the funds.

## See also

- [Creating Direct Charges](https://docs.stripe.com/connect/direct-charges.md)
- [Creating Destination Charges on Your Platform](https://docs.stripe.com/connect/destination-charges.md)
- [Creating Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)
