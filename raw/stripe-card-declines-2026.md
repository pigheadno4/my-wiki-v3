<!-- Source URL: https://docs.stripe.com/declines/card -->
<!-- Fetched: 2026-05-09 -->

# Card declines

Learn about card declines and how to lower your decline rate.

Card payments can fail for a variety of reasons. Some of the most common are:

- **Insufficient customer funds:** If a customer has insufficient customer funds or credit, the card issuer declines the transaction. To help minimize declines due to insufficient funds, consider adding a [Buy Now, Pay Later (BNPL)](https://docs.stripe.com/payments/buy-now-pay-later.md) option.

- **Incorrect card data:** If a customer enters an incorrect card number, CVV, or expiration date, the card issuer might decline the transaction. In these cases, request your customer to re-enter their card information.

- **Fraudulent activity:** If a card issuer suspects fraudulent activity, which can be triggered by large purchases or a large volume of transactions over a short period of time, they might decline payments. Your customer must resolve this issue by communicating with their issuing bank and confirming their identity.

> #### Stripe Sigma
>
> Use [Stripe Sigma](https://docs.stripe.com/stripe-data.md) to analyze your decline rate. Our interactive SQL reporting environment offers prebuilt queries for this purpose. To investigate declines outside Sigma, consider the `Card` object [fingerprints](https://docs.stripe.com/api/cards/object.md#card_object-fingerprint) instead of charge IDs to exclude repeat attempts.

## Card declines

When your customer’s card issuer receives a charge, their automated systems and models decide whether to authorize it. These tools analyze signals such as spending habits, account balance, and card data including expiration date, address information, and CVC.

If the card issuer declines a payment, Stripe shares some of the decline information we receive. This information is available in the Dashboard and through the API. Sometimes, issuers provide specific explanations, such as an incorrect card number or low funds. We show these as [decline codes](https://docs.stripe.com/declines/codes.md).

Card issuer’s categorize most declines as generic ([generic_decline](https://docs.stripe.com/declines/codes.md#generic_decline)), making the exact decline reason unclear. If the card information is correct, request your customer to contact their card issuer to understand why a transaction was declined. For privacy and security reasons, card issuers discuss the specifics of a decline only with their cardholders.

### Network codes

Whenever there’s a decline, the card issuer provides two types of network codes:

- **Network decline code:** The card’s issuing bank provides this 2-4 digit code. When Stripe doesn’t receive a response code from the card network for a declined charge, the `network_decline_code` field is null. The meaning of a code differs based on the card network. For this reason, take the card’s brand into consideration when interpreting the code.

- **Network advice code:** The card’s issuing bank provides this 2-4 digit code. The code offers guidance on managing a decline. When Stripe doesn’t receive a response code from the card network for a declined charge, the `network_advice_code` field is null. The meaning of a code differs based on the card network. For this reason, take the card’s brand into consideration when interpreting the code. Mastercard refers to network advice codes as Merchant Advice Codes (MAC).

## Reduce card declines

You can typically resolve card issuer declines resulting from inaccurate card details (such as an incorrect card number or expiration date) by asking your customers to correct the error or use a different card or payment method. For example, [Checkout](https://docs.stripe.com/payments/checkout.md) provides feedback to the customer when a card declines and allows them to try again.

To avoid declines that stem from suspected fraudulent activity, request your customers to provide their CVC and postal code during checkout. The impact of other data that you gather, such as the full billing address, might vary by card brand and country. If you continue to see elevated decline rates, Stripe recommends collecting extra customer information. You can also implement [3D Secure](https://docs.stripe.com/payments/3d-secure.md) to authenticate payment, which can lower decline rates in countries that support it.

For a clear insight into why the card issuer declined the card during generic or [do_not_honor](https://docs.stripe.com/declines/codes.md#do_not_honor) declines, examine the associated data. For example, if CVC or Address Verification Service (AVS) checks fail when your customer adds a card, request your customer to verify both of these details before initiating another charge.

If you notice that a customer is using a card issued in one country while operating from an IP address in another, it might be a legitimate decline due to possible unauthorized card use. However, exceptions can occur, particularly when customers are traveling internationally and use their cards from various locations.

### Card type restrictions

Some customers find that their card has restrictions on the types of purchasable items. _FSA or HSA_ (Flexible Spending Account or Health Savings Account debit cards use pre-tax funds to cover certain types of purchases, such as medical expenses. Their use is restricted only to businesses that directly provide eligible products and services) cards are often limited to certain types of businesses (for example, healthcare providers), so card issuer’s decline any other type of purchase. Additionally, some card issuers might not allow purchases from certain countries or outside of their own. In either case, your customer must contact their card issuer to inquire about potential restrictions.

### Geographic location impacts

If your customers use cards issued in a different country than where you registered your Stripe account, they might see an increased rate of declines. To resolve this, your customer must contact their issuing bank to authorize the charge. If you have a global customer base with concentrations in various locations, you might want to set up Stripe accounts in larger markets, or in regions that encounter higher decline rates. This allows you to process charges locally.

## Declined card retries

When a payment gets declined, Stripe offers a reason for the decline and briefly suggests a resolution path.
![Declined payment due to insufficient funds](assets/stripe-card-declined-payment-dashboard.png)

Declined payment due to insufficient funds

If you’re a [Stripe Billing](https://docs.stripe.com/billing.md) user, you can create a custom retry schedule for subscriptions. Use [Smart Retries](https://docs.stripe.com/invoicing/automatic-collection.md#smart-retries) to choose the best times to retry failed payment attempts. Be aware that card networks limit the number of times you can reattempt a single charge. We recommend a maximum of eight retries for charges that permit retries. Card issuers might see creating additional retries as potential fraud, which can result in increased declines for legitimate charges.

In the API, the [reason](https://docs.stripe.com/api.md#charge_object-outcome-reason) in the [outcome](https://docs.stripe.com/api.md#charge_object-outcome) uses [decline codes](https://docs.stripe.com/declines/codes.md) to tell you why the card issuer declined the authorization. The [advice_code](https://docs.stripe.com/api.md#charge_object-outcome-advice-code) in the `outcome` tells you what to do next.

| Advice code         | Description                                                                                                                          | Next steps                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `do_not_try_again`  | The card was declined and you shouldn’t use it again for the same transaction.                                                       | See the [decline code](https://docs.stripe.com/declines/codes.md) for the reason why the card issuer declined the authorization. Your customer might need to contact their card issuer for more information. |
| `try_again_later`   | The card issuer declined the transaction, but you can [retry it](https://docs.stripe.com/declines/card.md#retrying-issuer-declines). | Ask the customer to attempt the payment again. If subsequent payments are declined, the customer needs to contact their card issuer for more information.                                                    |
| `confirm_card_data` | The card issuer declined the transaction because some of the provided information is incorrect.                                      | See the [decline code](https://docs.stripe.com/declines/codes.md) for the reason why the card issuer declined authorization. The customer needs to validate the information on their card.                   |

## Manage declines programmatically

There are several ways to programmatically handle declines:

- Retrieve the [last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-decline_code) property from the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object to see why the card issuer declined the payment attempt.
- Iterate over the PaymentIntent’s [attempted charges](https://docs.stripe.com/payments/payment-intents/verifying-status.md#identifying-charges) and inspect the [failure message](https://docs.stripe.com/api/charges/object.md#charge_object-failure_message).
- Use [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to monitor PaymentIntent status updates. For example, the `payment_intent.payment_failed` event triggers when a payment attempt is unsuccessful.

You might also need to manage additional payment failure situations such as when your customer is present (on-session) or absent (off-session) during your checkout process. As you develop your integration, Stripe advises treating all possible API exceptions, including unexpected [errors](https://docs.stripe.com/error-codes.md).

> [Stripe Billing](https://docs.stripe.com/billing.md) handles many of these payment failure scenarios with features like [Automatic Collection](https://docs.stripe.com/invoicing/automatic-collection.md) and [Hosted Invoices](https://docs.stripe.com/invoicing/hosted-invoice-page.md).

### On-session declines

If your customer is present in your website or application’s checkout flow, prompt them to try their payment method again or ask for a new payment method.

### Off-session declines

If your customer isn’t available to make a payment or update a payment method, notify them (for example, send them an email or in-app notification) to visit your website or application. If your business is affected by regulations like [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md), payment attempts might also require authentication and fail with an [authentication_required](https://docs.stripe.com/declines/codes.md) decline code. For more information on handling these scenarios, see [off-session payments with saved cards](https://docs.stripe.com/payments/save-during-payment.md?platform=web#charge-saved-payment-method).

## See also

- [Decline codes](https://docs.stripe.com/declines/codes.md)
- [Disputes and fraud](https://docs.stripe.com/disputes.md)
