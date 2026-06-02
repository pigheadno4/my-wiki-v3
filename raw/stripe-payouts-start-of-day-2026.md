<!-- Source URL: https://docs.stripe.com/payouts/customized-start-of-day -->
<!-- Fetched: 2026-05-11 -->

# Customized start of day

Set your start of day to help you track your automatic payouts reconciliation.

Express and Custom accounts can’t change their start of day directly. The platform chooses a common start of day for all of its connected accounts.

Stripe supports customized start of day for automatic _payouts_ (A payout is the transfer of funds to an external account, usually a bank account, in the form of a deposit) to group and send payments in your local timezone with a “customized day” starting time. This allows you to track payout reconciliation because payouts contain payments processed in a day of your timezone, versus payments processed in a UTC day.

For example, if a user in Singapore starts their customized day at midnight SGT (Singapore Time), the payments they process from midnight SGT to the following midnight SGT belong to the same day. If they start their day at 06:00 SGT, payments collected between 06:00 SGT on a given day and 06:00 SGT the next day are attributed to the given day.

Your default start of day is UTC midnight [except for some users in Asia-Pacific (APAC) markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts). You can change your start of day to a time in the allowed range (usually between midnight and morning) in your local timezone.

## Feature availability

Customized start of day is available in the following countries:

- AU
- HK
- ID
- IN
- JP
- MY
- NZ
- PH
- SG
- TH

## Change start of day

To change the start of day:

1. In the Dashboard, go to **Settings** > **Business** > [**Bank accounts and currencies**](https://dashboard.stripe.com/settings/payouts).
1. In the **Start of day** section, change the default setting to your preferred start of day.
   ![Start of day settings in the Dashboard](assets/stripe-payouts-start-of-day-1.png)

After you set the start of day, it doesn’t take effect immediately. The new start of day only takes effect at the new time. For example, if your current time is equivalent to 07:00 Asia/Singapore, and you set the start of day to 00:00 Asia/Singapore, this new start of day takes effect in 17 hours.
![Dashboard callout notifying when the new start of day takes effect](assets/stripe-payouts-start-of-day-2.png)

The settings at the time of the original transaction also apply to the payout. For example, if the settings at the time of the original transaction indicate a 7-day payout timing, this rule applies to the payout regardless of any later changes in time zones. For example, say a business has a balance of 1000 USD. 500 USD is attributed to UTC Monday and 500 USD is attributed to UTC Tuesday. If their start of the day changes to Singapore Time (SGT) on Wednesday, the 1000 USD balance is still assigned to UTC Monday and Tuesday, and the payout processes on the next Monday and Tuesday under UTC, not SGT. Only the payments created after the change to SGT follow the new time zone in terms of payout timing.

## Example

For example, say a business operates their business from New York. All transactions made before their start of day count towards the previous day because they set midnight ET as their start of day. Assuming this business is on a daily automatic payout plan and a 4 business day schedule, all transactions made between midnight ET Monday and midnight ET Tuesday are grouped into Monday’s sales and arrive in their bank before the end of Friday in one payout.

## See also

- [Receiving payouts](https://docs.stripe.com/payouts.md)
