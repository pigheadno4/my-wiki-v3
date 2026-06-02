<!-- Source URL: https://docs.stripe.com/payments/orchestration/rules -->
<!-- Fetched: 2026-05-11 -->

# Manage rules

Learn how to create and manage rules for routing payments.

> #### Want access to Orchestration?
>
> Orchestration is in private preview.

Use Orchestration to route payments across all of your processors. In the Dashboard, go to **Payments** > [Orchestration](https://dashboard.stripe.com/orchestration) to create rules based on payment conditions, such as card country or currency. Stripe executes the conditions in order, from left to right, and applies the first action that matches a payment’s condition.

## Rule conditions and actions

When adding rules, you can specify a condition that a payment must meet for the rules to apply. For example, you can add a currency condition to route payments in EUR to one processor, and an action to route all other payments to Stripe. You can add multiple conditions.

| Condition                        | Description                                                                                                                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amount                           | The value of the payment. To route based on amount, you must also specify a currency.                                                                                                                                                                          |
| Bank Identification Number (BIN) | The first 6 or 8 numbers on the payment card, which identifies the card issuer.                                                                                                                                                                                |
| Card country                     | The issuing country for the card used for payment.                                                                                                                                                                                                             |
| Card issuer                      | The financial institution that issued the card used for payment.                                                                                                                                                                                               |
| Card type                        | The card type for the payment method. You can choose between `credit card`, `debit card`, and `prepaid card`.                                                                                                                                                  |
| Currency                         | The currency that a customer pays in. You can choose from the [presentment currencies](https://docs.stripe.com/currencies.md#presentment-currencies) that Stripe supports.                                                                                     |
| Metadata                         | The [information that you associate](https://docs.stripe.com/payments/payment-intents.md#storing-information-in-metadata) with common requests, such as processing payments. For example, you can attach a specific processor to a PaymentIntent for an order. |

After adding conditions to your rules, you add the actions. You can select the main and retry processors to use for payments that match the conditions, as well as the main and retry processors to use if no conditions are met.

## Set the order

Stripe executes your conditions in order, from left to right, and applies the first action that matches a payment’s condition. From the [Orchestration rules](https://dashboard.stripe.com/orchestration/rules) page, click the overflow menu (⋯) next to any condition to move it left or right. Make sure you set the order correctly, or your payments won’t process as expected.

## Save rules

If you want to continue modifying and testing your rules before activating, click **Save changes**. Draft rules don’t affect payments until you click **Activate rules**.

## Test rules

Before activating rules in live mode, we recommend activating and testing your rules in a [sandbox](https://docs.stripe.com/sandboxes.md). The rules you create in a sandbox don’t affect your live integration. If testing produces the results you expect, you can recreate the rules in live mode and activate.

## Activate rules

When you’re ready to start processing payments based on your rules, click **Activate rules**.

You can only have one set of active rules. When you activate a new set of rules, this action automatically deactivates the rules that are currently active. You can reactivate rules at any time.

If you don’t have active rules, payments route to Stripe.

## Duplicate rules

You can’t edit active rules. If you want to make changes to active rules, you must duplicate it and then edit the draft of your duplicated rules.

From the [Orchestration rules](https://dashboard.stripe.com/orchestration/rules) page, click the overflow menu (⋯) for the rules that you want to edit. In the dialog, click **Duplicate rules**, and make your desired changes to the duplicated rules.

## Deactivate rules

You can deactivate rules from the [Orchestration rules](https://dashboard.stripe.com/orchestration/rules) page. Click the overflow menu (⋯) for the active set of rules, and then click **Deactivate rules**.
