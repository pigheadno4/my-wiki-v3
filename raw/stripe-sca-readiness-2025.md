<!-- Source URL: https://docs.stripe.com/strong-customer-authentication -->
<!-- Fetched: 2026-05-08 -->

# Strong Customer Authentication readiness

Learn how the Strong Customer Authentication regulation affects your business and how to update your integration to support it.

- [SCA video](https://stripe.com/payments/strong-customer-authentication)
- [SCA payment scenarios](https://stripe.com/guides/sca-payment-flows)
- [Webinar](https://go.stripe.global/sca-webinar.html)

[Strong Customer Authentication (SCA)](https://stripe.com/guides/strong-customer-authentication), a rule in effect as of September 14, 2019, as part of PSD2 regulation in Europe, requires changes to how your European customers authenticate online payments. Card payments require you to use _3D Secure_ (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) to meet SCA requirements. Your customers’ banks might decline transactions that don’t follow the new authentication guidelines.

To support SCA:

1. Determine if SCA impacts your business.
1. Decide which SCA-ready product is right for your business.
1. Make changes now to avoid declined payments.

If you use a third-party plugin, platform, or [extension partner](https://stripe.partners), contact your Stripe partner to see if changes are required to support SCA. [Contact support](https://support.stripe.com/contact) if you have any questions.

## Impacted businesses and payments

Update your Stripe integration to support SCA, if all of the following apply:

- Your business is based in the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) or you [create payments on behalf of connected accounts based in the EEA](https://docs.stripe.com/strong-customer-authentication/connect-platforms.md).
- You serve customers in the EEA.
- You accept cards (credit or debit).

While some low-risk transactions (based on the volume of fraud rates associated with the payment provider or bank) don’t require authentication, banks can still request that the customer complete authentication. Even if you’re primarily processing low-risk transactions, update your integration so your customers can complete authentication when requested by the bank. Learn about _SCA exemptions_ (Some transactions that are deemed low risk, based on the volume of fraud rates associated with the payment provider or bank, may be exempt from Europe's Strong Customer Authentication requirements).

## SCA-ready products and APIs

Whether you collect one-time payments or save cards for later reuse, Stripe provides prebuilt and customizable products to help you meet SCA requirements.

Integrations that aren’t SCA-ready, like those using the legacy [Charges API](https://docs.stripe.com/payments/charges-api.md), might see high rates of declines from banks that enforce SCA.

### One-time payments

Accept card payments with the _Payment Intents API_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) and [Checkout](https://docs.stripe.com/payments/checkout.md), a prebuilt, Stripe-hosted checkout flow that automatically handles SCA requirements for you. Checkout is customizable and lets you accept payments for one-time purchases and _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) on your website.

- [Migrate to the Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration.md)
- [Use a prebuilt checkout page](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout)
- [Build a custom payment flow](https://docs.stripe.com/payments/accept-a-payment.md?integration=elements)

### Re-using cards

Save a card for later reuse with the Payment Intents API and the _Setup Intents API_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method). You can also use Checkout to automatically handle SCA requirements, or use [Billing](https://docs.stripe.com/billing.md) to handle SCA for [subscriptions](https://docs.stripe.com/subscriptions.md).

- [Use a prebuilt checkout page](https://docs.stripe.com/payments/save-and-reuse.md?platform=checkout)
- [Build a custom flow to save card details](https://docs.stripe.com/payments/save-and-reuse.md)

## SCA migration

You might need to update your integration to support SCA. For details about the changes to make, including for specific product recommendations based on use case, see the following guides:

- [Migrate to the Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration.md)
- [SCA payment flows](https://stripe.com/guides/sca-payment-flows)

## Update plugins and developer libraries

You might need to update your Stripe plugin or developer library to support SCA. If you’re looking for an SCA-ready plugin, visit [Stripe Partners](https://stripe.com/partners/sca-ready).

### Identify your plugin on our platform

Include identifying information in your plugins and third-party libraries so we can contact you about future changes or critical updates to the API. Use the [setAppInfo function](https://docs.stripe.com/building-plugins.md#setappinfo) to provide those details in your Stripe integration.

We encourage you to join the [Stripe Partner Program](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide), which includes [free registration](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide&utm_medium=join#stripe-partner-program) and more resources for developers building plugins. Learn more about [suggested best practices](https://docs.stripe.com/building-plugins.md).

### Determine your integration path

Consider the following:

- Use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to collect payments using a customizable form. You can embed the payment form on your website or host it on Stripe.
- For more control over your checkout flow, use the Payment Intents API and Setup Intents API with [Elements](https://docs.stripe.com/payments/elements.md), _PaymentMethods_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs), _Customers_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments), and _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients). These APIs display authentication flows like 3DS 2, save cards to use later, and support SCA.
- For recurring payments, use Stripe Billing to manage [subscriptions](https://docs.stripe.com/subscriptions.md) and [invoicing](https://docs.stripe.com/invoicing.md).
- [Register a webhook endpoint](https://docs.stripe.com/webhooks.md#register-webhook) for your account or connected accounts, and manage them with the Webhooks API.

If none of these options work for your integration, [let us know](mailto:plugins+sca@stripe.com).

### Test dynamic authentication

After you implement your integration path, configure your [Dynamic 3D Secure Radar rules](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar) to test your integration using [3D Secure test cards](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-cards). Make sure to test both successful and unsuccessful authentication cases.

### Notify your customers and Stripe

As soon as you finish updating, provide an SCA-ready update to your customers. You can share the [Strong Customer Authentication guide](https://stripe.com/guides/strong-customer-authentication) with your customers to help them understand these regulatory changes. When you release an SCA-ready update, [notify Stripe](mailto:plugins+sca@stripe.com) as well. We direct users to SCA-ready solutions on the [Stripe Partners](https://stripe.com/partners/sca-ready) page.

## Use previous authorization agreements

If you collect payments when your customer isn’t actively using your application, SCA might require your customer to re-authenticate, even if they authenticated in the past. For these _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) payments, you can use the Stripe APIs to authenticate your customer once while _on-session_ (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method), and then reuse the card repeatedly while off-session.

Alternatively, you can use previous authorization agreements (sometimes referred to as grandfathering) for off-session payments that meet the following eligibility period, regardless of payment amount and frequency:

- Cards from EU customers saved before December 31, 2020
- Cards from UK customers saved before September 14, 2021

Stripe automatically looks for transactions made with cards prior to the dates listed above. If found, Stripe uses the previous authorization agreement for the current transaction. If the bank accepts the previous authorization agreement, the transaction is categorized as out-of-scope for SCA and can proceed without additional authentication.

If the bank declines the previous authorization agreement, the PaymentIntent status changes to _requires_payment_method_ (This status appears as "requires_source" in API versions before 2019-02-11), and you must notify your customer to [complete the payment](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements#charge-saved-payment-method).

### Save cards after the eligibility period

After SCA takes effect, you can use the Payment Intents API to [save and reuse cards](https://docs.stripe.com/payments/save-and-reuse.md), and the Setup Intents API to qualify for off-session exemptions. You can also save cards using [Stripe Checkout](https://docs.stripe.com/payments/save-and-reuse.md?platform=checkout).

### Prepare your saved cards for SCA

For Stripe to reuse previous authorization agreements, you must use the Payment Intents API and tell Stripe the payment is off-session.

| Before the eligibility period                                                                                                                                                                                                                        | After the eligibility period                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You saved the card by passing a token, [source](https://docs.stripe.com/sources.md), or [payment method](https://docs.stripe.com/payments/save-during-payment.md) to the `Customer` object.                                                          | Create a PaymentIntent with an [off-session flag](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements#charge-saved-payment-method). |
| You saved the card by creating a [SetupIntent](https://docs.stripe.com/payments/save-and-reuse.md) or using [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) in a PaymentIntent. | Create a PaymentIntent with an [off-session flag](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements#charge-saved-payment-method). |

## SCA enforcement

Prepare your payment flows for SCA-readiness as soon as possible, if SCA regulations impact you. This can help prevent an increase in declines from European cards, and prepare you in case of early enforcement by banks. Learn how [enforcement varies by country](https://support.stripe.com/questions/strong-customer-authentication-sca-enforcement-date).

### Make sure your integration is SCA-ready

Your integration is SCA-ready when you process all of your payments using SCA-ready products, such as Checkout, Billing, the Payment Intents API, or an SCA-ready partner solution.

Additionally, do the following:

- Test 3DS authentication with our [regulatory test cards](https://docs.stripe.com/testing.md#regulatory-cards) to make sure your integration can handle 3DS.
- For off-session payments, set up and authenticate the card when saving the payment method, and use the API to [flag off-session payments](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements#charge-saved-payment-method).
- If you use the Billing API for subscriptions or invoices, make sure your integration can handle [incomplete statuses](https://docs.stripe.com/billing/subscriptions/overview.md#payment-behavior).

### Understand incomplete, declined, or failed payments

Payments might not succeed for reasons including incomplete, declined, or failed payments. For payments stuck in an `incomplete` (Dashboard) or `requires_action` (API) status, do the following:

- Make sure your customer isn’t actively authenticating an on-session payment. Your customer might also have abandoned the checkout flow.
- Verify that you’re [handling next actions](https://docs.stripe.com/payments/payment-intents/verifying-status.md#next-actions), such as authentication.
- Set [off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-off_session) to `true` when creating an off-session payment.

Banks can decline payments that require 3DS authentication but don’t have 3DS enabled.

If an off-session payment fails, but you think it’s exempt from SCA requirements, do the following:

- Make sure you authenticate the card when saving payment method details, either during a payment or without a payment.
- When saving cards during a payment, set `setup_future_usage` to `off_session`.
- When saving cards without a payment, use the Setup Intents API and set `usage` to `off_session`.

Exemptions aren’t guaranteed, and off-session payments might still require authentication by the bank.

#### View declined payments

1. In the Dashboard, go to **Transactions** > [Payments](https://dashboard.stripe.com/payments).

1. From the **Filter by: status** dropdown, do one of the following:
   - Select **Failed** to view declined off-session payments.
   - Select **Incomplete** to view declined on-session payments.

1. Click **Apply**.

1. Hover over the status badge for the reason.

### Monitor disputes

When monitoring disputes, be aware that payments successfully authenticated through 3DS fall under the _liability shift_ rule. If a cardholder [disputes a 3DS payment](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments) as fraudulent, the liability typically shifts from you to the card issuer. If the card issuer applies exemptions, the payment isn’t authenticated through 3D Secure, and liability shift doesn’t apply.

### Collect permission to reuse cards

When you set up your payment flow to save a card using the Payment Intents API or Setup Intents API, Stripe marks subsequent off-session payments as a _merchant-initiated transaction_ (A payment made off-session with a properly authenticated saved card, can qualify as merchant-initiated transaction and be exempt from SCA) (MIT). These transactions require an agreement (also known as a _mandate_) between you and your customer.

On your website or application, minimally cover the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf
- The anticipated frequency of payments (one-time or recurring)
- How you determine the payment amount

In your checkout flow, reference the terms of the payment:

I authorize to send instructions to the financial institution that issued my card to take payments from my card account in accordance with the terms of my agreement with you.
