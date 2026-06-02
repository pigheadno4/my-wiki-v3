<!-- Source URL: https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions -->
<!-- Fetched: 2026-05-08 -->

# Strong Customer Authentication (SCA) exemptions

Use SCA exemptions and Data Only to reduce cardholder friction on eligible transactions.

**Applicability:** EEA, Switzerland, and UK

Stripe requests applicable [SCA exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication) on your behalf to reduce cardholder friction, while meeting [SCA requirements](https://docs.stripe.com/strong-customer-authentication.md). Users of [Adaptive Acceptance](https://docs.stripe.com/payments/analytics/optimization.md) get access to Data Only flows and AI tools that can improve performance.

> When the customer’s bank approves an exemption request, liability shift for fraudulent transactions doesn’t apply.

Stripe currently supports the following SCA exemptions:

| SCA Exemption | Description                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Low Value     | Applies to transaction amounts less than 30 EUR (25 GBP). However, SCA might still be required by the issuer for low value transactions when either of the following scenarios are met: |

- The cumulative amount for transactions initiated by the cardholder since SCA was last performed exceeds 100 EUR (85 GBP).
- The cardholder has initiated five transactions since SCA was last performed. |
  | Transaction Risk Analysis (TRA) or Low Risk Exemption | A payment provider (such as Stripe) can perform real-time risk analysis to determine whether a transaction warrants SCA. This permission is subject to the payment provider’s overall fraud rates for card payments in relevant markets staying below the following thresholds:

- 0.13% to exempt transactions up to 100 EUR (85 GBP)
- 0.06% to exempt transactions up to 250 EUR (220 GBP)
- 0.01% to exempt transactions up to 500 EUR (440 GBP)

Local equivalent amounts for these thresholds apply where relevant. See [Stripe’s current threshold limits for TRA](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions.md#stripe-tra-limits) for more on Stripe’s current TRA exemption availability. |
| Merchant-initiated transactions (including variable subscriptions) | Payments made with saved cards when the customer isn’t present in the checkout flow (sometimes called “off-session”) might qualify as merchant-initiated transactions (MITs). These payments technically fall outside the scope of SCA. In practice, marking a payment as MIT is similar to requesting an exemption; neither a customer challenge nor a liability shift occurs. To use merchant-initiated transactions, you authenticate the card when it’s being saved. You must also secure agreement from the customer (through a _mandate_ (A written notice of authorization to debit a bank account, agreed to by the customer before the first debit)) to charge their card at a later point. The [Stripe API](https://docs.stripe.com/payments/more-payment-scenarios.md) lets you authenticate a card when it’s being saved for later use and mark subsequent payments as MITs. |

## Stripe’s transaction risk analysis (TRA) limits

Stripe uses risk assessments that allow us to support this exemption for our users. The exemption limit available for you depends on the Stripe overall fraud rates and your access to the Stripe authentication offerings, including [Adaptive Acceptance](https://docs.stripe.com/payments/analytics/optimization.md). Currently:

- UK and Swiss merchants have access to TRA exemptions for qualifying low risk transactions up to 220 GBP.
- EEA merchants have access to TRA exemptions for qualifying low risk transactions up to 250 EUR.

## Data Only

Data Only is a form of authentication supported by some card schemes that leverages 3D Secure (3DS) data. The Data Only flow sends the authentication request to the card network, who includes its own risk data in the authorization message, before sending it to the issuer. Successful Data Only requests offer a frictionless experience that improve approval rates for payments that aren’t subject to SCA.

> Because we don’t send an authentication request to the issuer in a Data Only flow, no liability shift occurs for the business.

The standard Data Only flow requires 3DS version 2.2 or later. Mastercard has its own Data Only product, Mastercard Identity Check Insights, which Stripe currently offers to Adaptive Acceptance and [Authorisation Boost](https://stripe.com/payments/authorization) users in the EEA and UK only. Instead of sending a transaction straight to authorization, the Stripe AI optimizations use the Data Only flow to help with conversion or lower costs for certain transactions. Handling these requests requires no further action from businesses.
