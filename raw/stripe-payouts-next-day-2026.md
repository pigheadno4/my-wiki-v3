<!-- Source URL: https://docs.stripe.com/payouts/next-day-settlement -->
<!-- Fetched: 2026-05-11 -->

# Next-day settlement

Access your funds in 1 business day.

With next-day settlement, funds from your domestic transactions (except [ACH direct debits](https://docs.stripe.com/payments/ach-direct-debit.md)) are available in your Stripe balance on the next business day. If you’re on an automatic daily payout schedule, Stripe sends eligible funds to your bank account the next business day. For example, your transactions from Monday typically settle in your bank account on Tuesday, but might be delayed, depending on your bank.

## Payout Schedule

Next-day settlement is available across all payout schedules (automatic or manual). You can view the fund settlement timeline based on your settlement speed and payout schedule below.

#### Daily automatic payouts

#### Standard settlement

When will my payout land on standard speed and daily payouts? (See full diagram at https://docs.stripe.com/payouts/next-day-settlement)

#### Next-day settlement

When will my payout land on standard speed and daily payouts? (See full diagram at https://docs.stripe.com/payouts/next-day-settlement)

#### Manual, weekly, monthly payouts

#### Standard settlement

When will my payout land on standard speed and non-daily payouts? (See full diagram at https://docs.stripe.com/payouts/next-day-settlement)

#### Next-day settlement

When will my payout land on standard speed and non-daily payouts? (See full diagram at https://docs.stripe.com/payouts/next-day-settlement)

## Availability

Next-day settlement is currently only available for Stripe Dashboard users in the US. If you’re a platform and want access to next-day settlement for your connected accounts, reach out to your account team for more details.

## Payout Limit

If your automatic payout amount to your bank account exceeds 1 million USD, funds take an additional day to settle in your bank account due to banking limitations in the US.

## Switch to other settlement speeds

You can switch from next-day settlement to your default standard settlement speed at any time. Use your [payout settings](https://dashboard.stripe.com/settings/payouts) in the Dashboard and select the standard option. You can also switch back to next-day settlement from the same settings panel.

## Eligibility

New Stripe users aren’t immediately eligible for next-day settlement. Check your eligibility in your [payout settings](https://dashboard.stripe.com/settings/payouts) to see if you have next-day settlement available.

## Fee schedule

Stripe calculates the monthly fee (0.6%) for next-day settlement as a percentage of the prior month’s accelerated charges. At the beginning of each month, we automatically debit the fee from your available balance.

## Next-day settlement or Instant Payouts

Both next-day settlement and [Instant Payouts](https://docs.stripe.com/payouts/instant-payouts.md) accelerate access to your earnings. You can use one or both options depending on your needs.

|                                 | Next-day settlement                                                                                                                     | Instant Payouts                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Best for**                    | Continuous, automatic liquidity management                                                                                              | As-needed, manual liquidity management                                                   |
| **Eligible funds**              | Settled USD earnings excluding ACH direct debits                                                                                        | All pending earnings (up to your Instant Payouts limit) after a card charge is completed |
| **When funds become available** | Next business day                                                                                                                       | Within 30 minutes                                                                        |
| **How to activate**             | Choose on or off in your [payout settings](https://dashboard.stripe.com/settings/payouts) to automatically apply to all eligible funds. | Manually request for each payout in your Balances Dashboard                              |
| **Fee**                         | 0.6%                                                                                                                                    | [See pricing](https://docs.stripe.com/payouts/instant-payouts.md#pricing)                |
