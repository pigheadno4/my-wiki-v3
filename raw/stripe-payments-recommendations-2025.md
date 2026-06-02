<!-- Source URL: https://docs.stripe.com/payments/analytics/recommendations -->
<!-- Fetched: 2026-05-08 -->

# Recommendations

Learn about the Stripe recommendations that can help increase revenue and improve fraud detection.

Payments recommendations are suggestions that Stripe makes that can help increase your revenue or improve fraud protection.

You can view recommendations on the [Acceptance](https://dashboard.stripe.com/acceptance) page in the Stripe Dashboard. Depending on availability, you might have no recommendations or up to three at any given time. To dismiss a particular recommendation, click the cancel icon (**X**).

To share feedback on recommendations, select **Feedback** in [Payments analytics](https://dashboard.stripe.com/acceptance), and click **Submit**.

> Carefully consider any recommendations. It’s up to your business to analyze and decide to act on a recommendation. Recommendations don’t constitute professional advice. Any estimated impacts, such as increases in revenue, are estimates and aren’t guaranteed. Stripe doesn’t have all the relevant information about your business to guarantee an outcome. Recommendations might require a tradeoff, such as an increase in costs, risk of fraud, or additional applicable legal terms.

### Recommendation availability

We offer recommendations in your account when they’re relevant to your business. We base recommendations on factors such as your account settings, how you integrate with Stripe, or thresholds. For example, if you share data on some of your payments, but not 80% or more, Stripe might recommend that you share that data on more of your payments. Not all businesses receive the same recommendations.

Stripe updates recommendations on a daily basis. Natural fluctuations in your payments could affect the availability of a recommendation as well as its estimated impact.

### Estimated impact

Each recommendation includes an estimated impact, such as a revenue (otherwise known as payment volume) increase or fraud model improvement. We show all of your revenue increases in your settlement currency.

Stripe estimates impact in one of the following ways:

| |
| |
| **Based on all payment volume** | - Stripe takes your most recent month of payment volume, multiplies it by an average increase figure, then multiplies it by 12 to provide an annual estimate.

- We base the average increase on the increase experienced by other businesses that took the action we recommend. Stripe regularly runs tests to evaluate this estimated impact. When annualizing the impact, we assume no changes to your payment volume over time. |
  | **Based on relevant payment volume** | - Stripe takes your most recent month of relevant payment volume, multiplies it by an average increase figure, then multiplies it by 12 to provide an annual estimate. Stripe excludes payments that aren’t relevant for the recommendation.
- For example, in the card account updater recommendation, we exclude payments using cards that don’t have an available update. |

## Provide network transactions IDs

You can increase your authorization rates in either of the following cases:

- You have transactions where Stripe didn’t previously authorize the underlying card.
- You create your payments with card numbers without using the Stripe `Customer` object.

If you process a merchant-initiated transaction (off-session), you can provide the network transaction ID (NTID) of a previous on-session transaction or validation from the same customer to the card network. This increases the authorization rates and decreases the possibility of the issuer requesting 3DS. If you process all payments through Stripe, we handle this automatically. If you use other payment processors and Stripe didn’t previously authorize your customer’s card, we might not have access to the appropriate NTID, unless you provided it when creating the Payment Intent.

Learn how to [provide a network transaction ID](https://docs.stripe.com/stored-credential-transaction-type.md#use-transaction-ids-on-subsequent-transactions) when using a stored credential type.

## Share postal codes for Visa credit cards

The Address Verification System (AVS) is a security measure that confirms a customer’s address against the one held by their card issuer. Mitigating the risk of fraud with AVS can contribute to more favorable interchange rates in the US and save costs. Learn how to [collect address information](https://docs.stripe.com/disputes/prevention/verification.md#avs-check).

## Remove AVS and CVC rules blocking low risk payments

To prevent blocking legitimate payments that have an incorrect postal code or CVC, we recommend disabling the following Radar rules:

- `Block if CVC verification fails`
- `Block if postal code verification fails`

Many legitimate payments might have an incorrect postal code or CVC, and enabling those rules would block these payments, even after they’ve been authorized by the cardholder’s bank. To improve your payment success rate, we recommend disabling those rules.

To block payments that fail a card issuer’s postal verification or CVC check, unless Stripe evaluates the payments as low risk, enable the following Radar rules:

- `Block if CVC verification fails based on risk score`
- `Block if postal code verification fails based on risk score`

Stripe automatically blocks truly high risk payments that are detected by our machine learning algorithm, through the rule `Block if :risk_level: = 'highest'`, regardless of your configured rules.

You can manage Radar rules on the [Rules tab](https://dashboard.stripe.com/radar/rules) in the Stripe Dashboard. Learn more about using [fraud prevention rules](https://docs.stripe.com/radar/rules.md#traditional-bank-checks).

## Reduce 3D Secure on low risk transactions

Requesting [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure.md) for low risk transactions outside of regions with authentication requirements might decrease your payment success rate while offering minimal or no effect on your fraud risk. We recommend requesting 3DS only if it’s required or as a way to reduce fraud.

Depending on how you request 3DS, you can change it as follows:

- If you request 3DS through the API, [manually stop requesting it through the API](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#manual-three-ds).
- If you request 3DS using a Radar rule, [disable the rule in your Dashboard](https://dashboard.stripe.com/radar/rules).

Disabling 3DS won’t affect payments that require 3DS by regulation, such as [Strong Customer Authentication (SCA)](https://docs.stripe.com/strong-customer-authentication.md) in Europe or the Credit Card Security Guidelines in Japan.

To allow Stripe to automatically request 3DS when we think it might reduce fraud, you can enable the [Radar Authentication control](https://docs.stripe.com/radar/risk-settings.md#adaptive-3ds).

## Check your 3D Secure integration

A large number of your 3D Secure (3DS) requests are abandoned, which means you might have an issue with your 3DS integration. Learn how to [process 3DS payments](https://docs.stripe.com/payments/3d-secure/authentication-flow.md).

## See also

- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance.md)
- [Authentication analytics](https://docs.stripe.com/payments/analytics/authentication.md)
- [Disputes analytics](https://docs.stripe.com/payments/analytics/disputes.md)
