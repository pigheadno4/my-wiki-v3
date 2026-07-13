<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/subscription/manage-subscription-lifecycle.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage subscription lifecycle

Use the Metronome API to manage your customer's subscription lifecycle including pricing changes, free trials, upgrades, and downgrades.

## Update pricing​

A core benefit of using Metronome subscriptions is centralized management of pricing via the rate card. To change the price of a subscription, change the price of the associated subscription rate on the rate card. All contracts inherit the new pricing and customers are billed at the new rate at the start of the next billing period.

<Info>
  **INFO**

  If you apply an overwrite override to the price of the subscription on the contract, the contract won't inherit changes made on the rate card. It keeps the price assigned on the overwrite.
</Info>

## Configure a free trial​

Creating a free trial in Metronome follows the general pattern for discounts: apply a rate override on the customer’s contract. If you want to offer a free trial for a subscription you have two options, depending on the desired behavior:

* **If the trial period is less than a full billing cycle.**
  * Create one subscription on the contract that starts on the start date of the contract and ends after the free trial period. Add an override to the subscription rate to change the price to \$0.
  * Create a second subscription on the contract that starts after the first one ends.
* **If the trial period is a full billing cycle.**
  * Create one subscription on the contract that starts when the contract starts.
  * Add an override for the trial period to change the rate to \$0 for that period. Once that period ends, the customer is automatically billed at the list rate on the rate card at the start of the next period.

<INFO>
  **RATE CHANGES**

  In Metronome, subscriptions can only have one rate per billing period. This enables you to schedule price changes on the rate card without interrupting mid-cycle customers.
</INFO>

## Add a subscription to an existing contract​

Add a new subscription to an existing contract using the `add_subscription` action on the [edit contract end point](/api-reference/contracts/edit-a-contract). Make sure the `entitlement` for the relevant subscription rate is set to `true`. This is most often used to model subscription add-ons.

## Upgrade or downgrade a subscription​

Facilitate a contract transition by using the [create contract endpoint](/api-reference/contracts/edit-a-contract) and specifying the `transition` object `type` to`renewal`.

Metronome recommends facilitating upgrade and downgrade motions using contract transitions for a few reasons:

* End your first subscription and start the second one with a single API call - automatically handling proration.
* Oftentimes different subscription packages might have different rates. Ending one contract and starting a new one provides a clean separation and audit of the original and new rates.
* If using credit based subscription models, contract transitions will automatically handle roll-over logic.

<INFO>
  **DOWNGRADES**

  Metronome only supports prorating for upgrade motions, such as increasing quantity or adding a new subscription mid-period. For downgrade motions, such as decreasing quantity, the change takes effect at the start of the next billing period.
</INFO>

## Cancel a subscription​

End a subscription in Metronome by either:

* Ending the contract by moving the contract end date to the time of cancellation using the [edit contract endpoint](/api-reference/contracts/edit-a-contract).
* Ending the subscription on the contract by moving the subscription end date to the time of cancellation using the [edit contract endpoint](/api-reference/contracts/edit-a-contract). If using this method to cancel a hybrid subscription, you must also end the recurring credit separately.

For most cancellations, Metronome recommends ending the contract. If the same customer restarts the subscription in the future, create a new contract at that point in time. This enables the Metronome contract to be the source of truth for whether a customer has an active plan for your product.

<Warning>
  **WARNING**

  Extending or removing a contract's end date does **not** automatically update the subscription end date if the most recent service period has already been finalized. For in-advance subscriptions, create a new subscription using the [EditContract](/api-reference/contracts/edit-a-contract) endpoint when extending the contract to ensure that the customer will have an active subscription in future service periods.
</Warning>
