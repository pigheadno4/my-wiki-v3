<!-- Source URL: https://docs.stripe.com/payments/a-b-testing -->
<!-- Fetched: 2026-05-08 -->

# A/B testing a payment method

Launch an A/B test for a new payment method in the Dashboard.

A/B testing allows you to measure the impact of offering new payment methods to a percentage of buyers before offering them to all of your customers. You can run A/B tests without writing any code.

Use A/B testing to:

- Test Buy Now, Pay Later payment methods like Klarna, Affirm, and Afterpay with a subset of customers before you introduce them to all of your customers.
- Measure the impact of targeting rules, such as setting a minimum purchase price for certain payment methods.
- Gradually offer a new payment method to an increasing percentage of customers.

## Before you begin

To run an A/B test, your integration must use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md?payment-ui=payment-element#customization-features). A/B testing is available if you use either [Payment Element Web](https://docs.stripe.com/payments/payment-element.md) with the Payment Intents API or [Checkout](https://docs.stripe.com/payments/checkout.md) in payment mode. See [Supported payment methods](https://docs.stripe.com/payments/a-b-testing.md#supportability) for the list of payment methods you can test.

## Begin your A/B experiment

![A custom configuration page with the Create an experiment button](assets/stripe-ab-test-create-experiment.png)

1. In the Stripe Dashboard, open the [Payment method settings](https://dashboard.stripe.com/settings/payment_methods), then click **Create an experiment**.
   - You can only start, stop, and manage an experiment using the Stripe Dashboard (there’s no API option).
   - If you have more than one payment method configuration, select the configuration you want to run an experiment on before you click **Create an experiment**. You can only run one experiment at a time per configuration.
1. Select which payment methods you want to include in the experiment.
1. (Optional) Add custom [payment method rules](https://docs.stripe.com/payments/payment-method-rules.md), such as transaction amount or presentment currency, as additional filters to control when a payment method is eligible. You can also create custom rules using the standalone feature.
1. Name your experiment and choose the percentage of traffic to include in your treatment group.
   - **Traffic allocation**: Our default recommendation is 50% to balance receiving results quickly (statistically significant results take longer with a lower percentage) and risk management of poor experiment performance. You can opt for a smaller or larger percentage based on your risk tolerance and experiment goals. With an even 50/50 treatment/control split, a sample size of 80,000 offers enough power to detect a 100 BPS change in the conversion rate at a 5% significance level.
   - **Experiment randomization**: Stripe randomizes buyer sessions based on a unique identifier, which includes the [UserAgent](https://en.wikipedia.org/wiki/User-Agent_header), IP address, and date. As a result, an individual buyer sees the same set of treatment or control payment method options for a particular day. To avoid instances of double counting, such as page refreshes, we aggregate sessions for each unique user on a daily basis.
1. Review and start your experiment. (You can save an experiment as a draft if you’re not ready to start it.)
   > When you begin an experiment, you can change the treatment group traffic allocation percentage but you can’t turn payment methods on or off for your control or treatment groups. To make any payment method settings changes after an experiment has started, you must end the experiment first.
1. (Recommended) If you’re testing Buy Now, Pay Later (BNPL) payment methods, we recommend that you install the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md). This embeddable UI component allows your customers to see the available payment options directly from your product, cart, or payment pages.

## Manage and end an A/B experiment

![A settings page to manage your experiment](assets/stripe-ab-test-manage-experiment.png)

1. To view all active and past experiments from your payment method settings, click the overflow menu (⋯), then select **Manage experiments**.
1. There are four actions you can take while an experiment is active. If you have a Connect integration and select **treatment configuration**, any new payment method in treatment turns on for all users.
   - **Adjust traffic allocation**: Adjust the percentage of traffic allocated to your treatment group, which ranges from 1% to 99%.
   - **View experiment report**.
   - **Pause or resume an experiment**: When paused, only your control payment methods are available to buyers and experiment data isn’t captured in your report.
   - **End experiment**: When the experiment ends, you can either adopt your treatment settings, or revert to your previous (control) settings. If your experiment runs longer than 180 days, we end it on your behalf and enable your control settings.

## Understand your experiment results

After your experiment begins, view its progress in the Stripe Dashboard.
![A page with experiment results](assets/stripe-ab-test-experiment-report.png)

A/B testing considers an experiment complete when two conditions have been met:

- Average revenue per session is [statistically significant](https://en.wikipedia.org/wiki/Statistical_significance). We consider results to be statistically significant when there’s less than a 5% probability that the result is due to a random chance. See [Experiment methodology](https://docs.stripe.com/payments/a-b-testing.md#experiment-methodology).
- The experiment has accrued enough sessions. This is a dynamic number based on the treatment versus control percentage you set during experiment creation.

Experiment result metrics include:

| Result metric                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Average revenue per session** | Average revenue per session is the total revenue divided by the total number of sessions. It shows the difference in revenue per session between your treatment and control groups, and is a summary of the overall results of your experiment. The total number of sessions includes both sessions that resulted in a purchase and sessions that didn’t result in a purchase. Due to the significant variations in conversion rates and average order values by payment method, we recommend using the Average revenue per session metric as a guiding metric when determining the overall success of the experiment. |
| **Revenue at 100% of sessions** | Projected total revenue if the treatment group payment methods were offered to 100% of traffic across treatment and control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Gross revenue**               | Actual revenue (full purchase amount). This amount is influenced mainly by your treatment/control percentage selection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Conversion rate**             | Conversion rate is the number of sessions with a purchase divided by the total number of eligible sessions. Eligible sessions is defined as:                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

- One or more treatment payment methods was eligible (for example, the buyer was in a country where the payment method is accepted)
- The payment interface (Payment Element or Checkout) was rendered to the buyer |
  | **Average order value** | Average order value is the average purchase amount for sessions where the buyer made a purchase. |

### Statistical significance

Use the indicators on the overview tables to understand statistical significance. The metrics display a green or yellow difference when the experiment has reached at least 80% of estimated required sessions.

There are three types of indicators:

- Gray indicators mean your experiment hasn’t accrued enough sessions to reliably determine statistical significance.
- Green indicators demonstrate a statistically significant increase between the treatment and control groups.
- Yellow indicators demonstrate a statistically significant decrease between the treatment and control groups.
  ![A gray badge indicating there isn't statistical significance.](assets/stripe-ab-test-gray-indicator.png)

Before reaching statistical significance
![A green badge indicating statistical significance.](assets/stripe-ab-test-green-indicator.png)

After reaching statistical significance

### Conduct additional analysis

You can download raw data from the reporting page to further analyze your experiment results.

We recommend grouping by `experiment_session_id` to avoid double counting sessions for instances such as a page refresh. This is consistent with how the A/B test report calculates average revenue per session, conversion rate, and average order value.

| Dimension                        | Description                                                                                                                                                                                                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `occurred_at_day`                | The day (‘yyyyMMdd’) of the session.                                                                                                                                                                                                                                                     |
| `experiment_session_id`          | A unique, Stripe-generated ID for each experiment session. A session is based on the UserAgent, IP address, and date.                                                                                                                                                                    |
| `is_treatment`                   | A Boolean indicating whether outcome was assigned as treatment (1) or control (0).                                                                                                                                                                                                       |
| `converted`                      | A Boolean indicating whether this session converted (1) or not (0).                                                                                                                                                                                                                      |
| `payment_method`                 | The actual payment method used for the purchase.                                                                                                                                                                                                                                         |
| `converted_transaction_count`    | The number of individual transaction-level conversions in the user session. Usually this value is either 1 or 0, however, multiple conversions can occur within the same session if the same buyer makes multiple purchases within the same day.                                         |
| `rendered_transaction_count`     | The number of individual transaction-level renders in the user session. This can be a number >1 if a buyer visits the purchase page multiple times (for example, reloads or comes back later in the day).                                                                                |
| `amount_capturable`              | The total transaction amount.                                                                                                                                                                                                                                                            |
| `currency`                       | The currency type used in this transaction (for example, USD, GBP, EUR).                                                                                                                                                                                                                 |
| `is_eligible_session`            | A Boolean indicating whether this session was eligible (1) or ineligible (0) for A/B testing. If this field returns a 0 (for example, no treatment payment methods were eligible), then this session isn’t included in any reported metrics like Average Order Value or Conversion Rate. |
| `buyer_countries`                | The country/countries associated with the user session. In most cases this is a single country, but there could be multiple if the buyer is traveling or changes their browser’s location settings.                                                                                      |
| `control_payment_method_types`   | The list of control payment methods that were eligible to be shown in this session.                                                                                                                                                                                                      |
| `treatment_payment_method_types` | The list of treatment payment methods that were eligible to be shown in this session.                                                                                                                                                                                                    |
| `rendered_payment_methods`       | The list of payment methods that were available in the user session, including those hidden behind an overflow ‘show more’ selector.                                                                                                                                                     |
| `visible_payment_methods`        | The list of payment methods that were visible in the user session (not hidden behind an overflow, such as ‘show more’).                                                                                                                                                                  |
| `connected_account_id`           | The connected account ID associated with the session.                                                                                                                                                                                                                                    |

### Experiment methodology

A/B testing measures the [average treatment effect](https://en.wikipedia.org/wiki/Average_treatment_effect) (ATE) by comparing treatment and control outcomes. We consider an experiment statistically significant when there’s less than a 5% probability that the result is due to a random chance. In statistical terms, we use a [z-test](https://en.wikipedia.org/wiki/Z-test) to calculate differences between the treatment and control group at the 5% level, which is mechanically the same as checking whether the 95% confidence interval for the difference includes 0. To determine how many sessions are required to detect an impact, we run a power calculation based on your selected treatment and control percentage split. This power calculation returns the number of sessions required to have 80% power to detect a 1% difference between treatment and control at a 5% significance level.

> To provide you with this A/B testing service we need to derive analytics regarding your customers’ activities from your transaction data. We use your customers’ IP address and User Agent information to identify when a user who was shown a payment method on one page of the checkout flow went on to complete the flow. Depending on the law applicable to you and your customers, instructing us to undertake this activity on your behalf might require you to take steps such as providing disclosures and collecting customers’ consent to this activity. Consult with your legal counsel to make sure that you’re complying with all of your obligations under applicable data protection laws.

## Supported payment methods

### Integration options

To use A/B testing, your integration must use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md?payment-ui=payment-element#customization-features).

You can then access A/B testing if you use either of the following:

- [Payment Element Web](https://docs.stripe.com/payments/payment-element.md) with the Payment Intents API
- [Checkout](https://docs.stripe.com/payments/checkout.md) in payment mode

### Supported payment methods

| |
| |
| **Payment method** | **Payment Element** | (Connect)**Payment Element** 1 |
| [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md) | ✓ Supported | - Unsupported |
| [ACSS Debit](https://docs.stripe.com/payments/acss-debit.md) | ✓ Supported | - Unsupported |
| [Affirm](https://docs.stripe.com/payments/affirm.md) | ✓ Supported | ✓ Supported |
| [Afterpay (Clearpay)](https://docs.stripe.com/payments/afterpay-clearpay.md) | ✓ Supported | ✓ Supported |
| [Alipay](https://docs.stripe.com/payments/alipay.md) | ✓ Supported | - Unsupported |
| [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) | ✓ Supported | ✓ Supported |
| [Apple Pay](https://docs.stripe.com/apple-pay.md) | ✓ Supported | ✓ Supported |
| [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) | ✓ Supported | - Unsupported |
| [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md) | ✓ Supported | - Unsupported |
| [Bancontact](https://docs.stripe.com/payments/bancontact.md) | ✓ Supported | ✓ Supported |
| [BLIK](https://docs.stripe.com/payments/blik.md) | ✓ Supported | ✓ Supported |
| [Boleto](https://docs.stripe.com/payments/boleto.md) | ✓ Supported | ✓ Supported |
| [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) | ✓ Supported | ✓ Supported |
| [Crypto](https://docs.stripe.com/crypto.md) | ✓ Supported | ✓ Supported |
| [EPS](https://docs.stripe.com/payments/eps.md) | ✓ Supported | ✓ Supported |
| [FPX](https://docs.stripe.com/payments/fpx.md) | ✓ Supported | - Unsupported |
| [Giropay](https://docs.stripe.com/payments/giropay.md) | ✓ Supported | ✓ Supported |
| [Google Pay](https://docs.stripe.com/google-pay.md) | ✓ Supported | ✓ Supported |
| [GrabPay](https://docs.stripe.com/payments/grabpay.md) | ✓ Supported | ✓ Supported |
| [iDEAL](https://docs.stripe.com/payments/ideal.md) | ✓ Supported | ✓ Supported |
| [Klarna](https://docs.stripe.com/payments/klarna.md) | ✓ Supported | ✓ Supported |
| [Konbini](https://docs.stripe.com/payments/konbini.md) | ✓ Supported | - Unsupported |
| [MobilePay](https://docs.stripe.com/payments/mobilepay.md) | ✓ Supported | ✓ Supported |
| [OXXO](https://docs.stripe.com/payments/oxxo.md) | ✓ Supported | ✓ Supported |
| [P24](https://docs.stripe.com/payments/p24.md) | ✓ Supported | ✓ Supported |
| [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank.md) | ✓ Supported | ✓ Supported |
| [PayNow](https://docs.stripe.com/payments/paynow.md) | ✓ Supported | ✓ Supported |
| [PromptPay](https://docs.stripe.com/payments/promptpay.md) | ✓ Supported | ✓ Supported |
| [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md) | ✓ Supported | ✓ Supported |
| [SEPA Debit](https://docs.stripe.com/payments/sepa-debit.md) | ✓ Supported | - Unsupported |
| [Swish](https://docs.stripe.com/payments/swish.md) | ✓ Supported | ✓ Supported |
| [TWINT](https://docs.stripe.com/payments/twint.md) | ✓ Supported | ✓ Supported |
| [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) | ✓ Supported | - Unsupported |
| [Zip](https://docs.stripe.com/payments/zip.md) | ✓ Supported | ✓ Supported |

1 Certain payment methods require users to take additional off-Stripe action (such as identity verification, acceptance of terms of service, and so on) before they’re eligible to use that payment method. Because direct users can take these actions directly, we support A/B testing on these payment methods. However, because Connect users aren’t able to take action on behalf of their connected accounts, which means few or no connected accounts are eligible to use that payment method, we don’t support A/B testing on these payment methods.

### Split testing for Connect (Connect)

A/B testing is available for Connect platforms, but not for individual connected accounts. When setting up an A/B test, the payment methods selected for control and treatment apply to all eligible connected accounts. To opt out specific connected accounts, you can specify a list of account IDs during the experiment creation process.

Platforms can allow connected accounts to customize their payment method settings to turn on or off specific payment methods. If a connected account turns on or off any payment method that’s in a treatment or control group, the connected account’s preference applies to both treatment and control sessions. For example, if a platform runs an experiment with Klarna on, and a connected account has turned off Klarna, Klarna is never shown as an available payment method for the connected account’s users.
