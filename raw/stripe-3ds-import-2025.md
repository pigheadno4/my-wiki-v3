<!-- Source URL: https://docs.stripe.com/payments/payment-intents/three-d-secure-import -->
<!-- Fetched: 2026-05-08 -->

# Import 3D Secure results

Process payments when 3D Secure runs outside of Stripe.

Importing 3DS results is an advanced payment flow that allows you to incorporate your external 3DS authentication into your Stripe payment by importing the authentication result. You need to import 3DS results if you:

- Are in the travel industry and receive card numbers and cryptograms from a travel aggregator, such as Expedia or Sabre
- Use a third-party provider to perform 3DS

In these situations, you can pass the card details and cryptogram directly to the Payment Intents API instead of using Stripe Elements to collect payment details and run 3DS.

Importing 3DS results is available in the following countries:

- AU
- CA
- CH
- EU
- GB
- HK
- MX
- NZ
- SG
- US

(Beta) All other countries in which Stripe supports card payments.

Importing 3DS results isn’t available in the following countries:

- IN
- MY
- TH

> In all the following code samples, the parameters set in the `three_d_secure` object must identically match the values returned by your 3DS provider.

## Process a payment with card details

If you handle card details on your server:

1. Create and _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent with the card details and 3DS details in one API call.
1. When creating the PaymentIntent, set [confirm](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-confirm) to `true`.
1. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when you confirm the PaymentIntent to prevent Stripe from performing a 3DS request during a soft decline.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "eur",
  payment_method_types: ["card"],
  payment_method_data: {
    type: "card",
    card: {
      number: 4000002760003184,
      exp_month: 12,
      exp_year: 23,
      cvc: 123,
    },
  },
  payment_method_options: {
    card: {
      three_d_secure: {
        version: "2.1.0",
        electronic_commerce_indicator: "05",
        cryptogram: "CJSJbzXT6TRQlvZDX+ZdOG4QriE=",
        transaction_id: "aaa65c7b-b0fc-4e71-bd6c-29c87acad489",
      },
    },
  },
  confirm: true,
  error_on_requires_action: true,
});
```

## Process a payment with a PaymentMethod

If you tokenize card details with the [Payment Methods API](https://docs.stripe.com/api/payment_methods.md):

1. Create and confirm a PaymentIntent with the PaymentMethod ID and 3DS details in one API call.
1. When creating the PaymentIntent, set [confirm](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-confirm) to `true`.
1. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` when you confirm the PaymentIntent to prevent Stripe from performing a 3DS request during a soft decline.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "eur",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_options: {
    card: {
      three_d_secure: {
        version: "2.2.0",
        electronic_commerce_indicator: "02",
        cryptogram: "M6+990I6FLD8Y6rZz9d5QbfrMNY=",
        transaction_id: "f879ea1c-aa2c-4441-806d-e30406466d79",
      },
    },
  },
  confirm: true,
  error_on_requires_action: true,
});
```

> If you intend to process a payment with a PaymentMethod shortly after tokenizing the card details, use raw card data instead.

## Set up future payments

The 3DS protocol supports two message categories:

- **Payment Authentication**: used for authenticating cardholders during transactions.
- **Non-Payment Authentication**: used for identity verification and account confirmation.

If you want to onboard customers for future payments, include the non-payment authentication cryptogram and either the card details or PaymentMethod ID when creating and confirming a [SetupIntent](https://docs.stripe.com/api/setup_intents.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_options: {
    card: {
      three_d_secure: {
        version: "2.2.0",
        electronic_commerce_indicator: "05",
        cryptogram: "4BQwsg4yuKt0S1LI1nDZTcO9vUM=",
        transaction_id: "f879ea1c-aa2c-4441-806d-e30406466d79",
      },
    },
  },
  confirm: true,
  expand: ["latest_attempt"],
});
```

## Import 3DS exempted outcomes

If you obtain a 3DS result outside of Stripe that contains a ‘low-risk’ _SCA_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) exemption, you can flag the exemption-based nature of the 3DS result to Stripe by using the [exemption_indicator](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-exemption_indicator) parameter.

If Stripe’s real-time transaction risk analysis determines that it’s appropriate, Stripe requests the [low-risk exemption](https://stripe.com/guides/strong-customer-authentication#low-risk-transactions) from the issuer and communicates this action to you by returning [exemption_indicator_applied](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure-exemption_indicator_applied) in to the authorization request response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "eur",
  payment_method_types: ["card"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_options: {
    card: {
      three_d_secure: {
        version: "2.2.0",
        electronic_commerce_indicator: "07",
        cryptogram: "CJSJbzXT6TRQlvZDX+ZdOG4QriE=",
        transaction_id: "aaa65c7b-b0fc-4e71-bd6c-29c87acad489",
        exemption_indicator: "low_risk",
      },
    },
  },
  confirm: true,
  error_on_requires_action: true,
  expand: ["latest_charge"],
});
```

To see whether Stripe requested the low-risk exemption, [expand](https://docs.stripe.com/api/expanding_objects.md) the `latest_charge` and inspect the [three_d_secure](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure) attribute.

```json
{
  "id": "pi_3aTnU0Aif3fLhNTb0le1BSXI",
  "object": "payment_intent",
  // ...
  "latest_charge": {
    "id": "ch_3aTnU1AifffLhNTb0tUoEZcd",
    "object": "charge",
    // ...
    "payment_method_details": {
      "card": {
        // ...
        "three_d_secure": {
          "authentication_flow": "frictionless",
          "electronic_commerce_indicator": "07",
          "exemption_indicator": "low_risk",
          "exemption_indicator_applied": true,
          "result": "exempted",
          "result_reason": null,
          "transaction_id": "aaa65c7b-b0fc-4e71-bd6c-29c87acad489",
          "version": "2.2.0"
        }
        // ...
      }
      // ...
    }
    // ...
  }
  // ...
}
```

## Importing Cartes Bancaires outcomes

To use 3DS import for transactions that process on the Cartes Bancaires network, you need to explicitly pass the authenticated network in your request using the [network](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-network) parameter.

To import Cartes Bancaires cryptograms, you also need additional data from your external 3DS server. The table below specifies the details of these additional required and recommended fields. These recommendations apply when you import 3DS outcomes using both PaymentIntents and SetupIntents.

| Field                                                                                                                                                                                 | Description                                                                                                                                 | Optionality                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [electronic_commerce_indicator](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-electronic_commerce_indicator) | The Electronic Commerce Indicator (ECI) is returned by your 3DS provider and indicates what degree of authentication was performed.         | Optional. Include this if it’s available. |
| [cb_avalgo](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-network_options-cartes_bancaires-cb_avalgo)        | The cryptogram calculation algorithm used by the card Issuer’s ACS to calculate the Authentication cryptogram. Also known as cavvAlgorithm. |

ARes/RReq messageExtension: `CB-AVALGO` | Required. |
| [cb_exemption](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-network_options-cartes_bancaires-cb_exemption) | The exemption indicator returned from Cartes Bancaires in the ARes. This is a 3 byte bitmap (lowest significant byte first and most significant bit first) that has been Base64 encoded. String (4 characters).

ARes message extension: `CB-EXEMPTION` | Optional. Include this if it’s available. |
| [cb_score](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-network_options-cartes_bancaires-cb_score) | The risk score returned from Cartes Bancaires in the ARes. Numeric value 0-99.

ARes/RReq message extension: `CB-SCORE` | Optional. Include this if it’s available. |
| [ares_trans_status](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-ares_trans_status) | The `transStatus` returned from the card Issuer’s ACS in the ARes. | Optional. Include this if it’s available. |
| [requestor_challenge_indicator](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure-requestor_challenge_indicator) | The challenge indicator (`threeDSRequestorChallengeInd`) which was requested in the AReq sent to the card Issuer’s ACS. A string containing 2 digits from 01-99. | Optional. Include this if it’s available. |

Provide as many of these additional fields as possible to increase the chances of a successful authorization.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "eur",
  payment_method_types: ["card"],
  payment_method: "{{PAYMENTMETHOD_ID}}",
  payment_method_options: {
    card: {
      network: "cartes_bancaires",
      three_d_secure: {
        version: "2.2.0",
        electronic_commerce_indicator: "05",
        cryptogram: "CJSJbzXT6TRQlvZDX+ZdOG4QriE=",
        transaction_id: "aaa65c7b-b0fc-4e71-bd6c-29c87acad489",
        requestor_challenge_indicator: "02",
        ares_trans_status: "Y",
        network_options: {
          cartes_bancaires: {
            cb_avalgo: "1",
            cb_score: 9,
            cb_exemption: "BAAA",
          },
        },
      },
    },
  },
  confirm: true,
  error_on_requires_action: true,
});
```

### Exemptions with Cartes Bancaires

If you’ve been granted an _SCA_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) exemption over 3DS, you must submit either the `cb_exemption` parameter, the `exemption_indicator` parameter, or both. If either of these parameters indicates that the exemption is low risk due to acquirer transaction risk analysis, Stripe reassesses the transaction, as described in [Import 3DS exempted outcomes](https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md#import-exempted-outcomes).

- If you have access to `cb_exemption`, pass that value and don’t populate `exemption_indicator`. Stripe infers the appropriate exemption indicator based on `cb_exemption`.
- If you pass both the `cb_exemption` parameter and `exemption_indicator` parameter, make sure that they both correctly indicate the exempted status.
- If there’s a mismatch where `exemption_indicator=none` and the bitmap in `cb_exemption` indicates that the applied exemption is a low risk exemption, Stripe rejects the request.

## Testing

You can validate your integration in a sandbox using either the authentication required test card: `4000 0027 6000 3184` or `pm_card_authenticationRequired`.

The simulation accepts any correctly-formatted 3DS result. For example:

- Version: `2.1.0`
- Electronic Commerce Indicator: `02`
- Cryptogram: `M6+990I6FLD8Y6rZz9d5QbfrMNY=`
- Transaction ID: `5f5d08f2-8c36-4f72-99d1-57b4fb70b7d5`

Or:

- Version: `2.2.0`
- Electronic Commerce Indicator: `05`
- Cryptogram: `4BQwsg4yuKt0S1LI1nDZTcO9vUM=`
- Transaction ID: `f879ea1c-aa2c-4441-806d-e30406466d79`

### Exemptions granted through 3DS

In a testing environment, all cards that include `exemption_indicator` return `exemption_indicator_applied` as true. To test a PaymentIntent creation that doesn’t pass the internal TRA check, and that returns false, use card number `4000 0000 0001 6123` and set `exemption_indicator=low_risk`.

### Cartes Bancaires

You can use the following co-badged cards to test importing Cartes Bancaires outcomes:

#### Card numbers

| Number              | Brand                         | CVC          | Date            |
| ------------------- | ----------------------------- | ------------ | --------------- |
| 4000 0025 0000 1001 | Cartes Bancaires / Visa       | Any 3 digits | Any future date |
| 5555 5525 0000 1001 | Cartes Bancaires / Mastercard | Any 3 digits | Any future date |
| 4000 0000 0001 6123 | Cartes Bancaires / Visa       | Any 3 digits | Any future date |

#### Tokens

| Token                                                | Brand                         |
| ---------------------------------------------------- | ----------------------------- |
| `tok_visa_cartesBancaires`                           | Cartes Bancaires / Visa       |
| `tok_mastercard_cartesBancaires`                     | Cartes Bancaires / Mastercard |
| `tok_threeDSecureImportExemptionIndicatorNotApplied` | Cartes Bancaires / Visa       |

#### PaymentMethods

| Payment Method                                           | Brand                         |
| -------------------------------------------------------- | ----------------------------- |
| `pm_card_visa_credit_fr_cartesBancaires`                 | Cartes Bancaires / Visa       |
| `pm_card_mastercard_credit_fr_cartesBancaires`           | Cartes Bancaires / Mastercard |
| `pm_card_threeDSecureImportExemptionIndicatorNotApplied` | Cartes Bancaires / Visa       |

You can use any valid `cb_exemption` value in your tests. For example:

- `AAAA` - No exemption granted
- `BAAA` - Low risk exemption granted

Like [the standard exemptions flow](https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md#exemptions-granted-through-3ds), when the value of `cb_exemption` corresponds to low risk, only the test card `4000 0000 0001 6123` returns false for [exemption_indicator_applied](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure-exemption_indicator_applied).

## Raw PAN usage

Stripe requires users to validate that cardholder data is handled securely and in compliance with the Payment Card Industry Data Security Standard (PCI DSS) before granting access to raw card data APIs.

For businesses that require this functionality, Stripe imposes strict requirements, including:

- Validation of PCI DSS compliance
- Submission to the Stripe review process
- Agreement to maintain additional controls on top of Stripe’s default security settings

See [Enabling access to raw card data APIs](https://support.stripe.com/questions/enabling-access-to-raw-card-data-apis) support article for enablement details.

> For accounts with custom pricing, if you specify Stripe as your acquirer in the 3D Secure request, Stripe passes network costs applicable to 3DS through, per your agreement with Stripe.

## See also

- [3D Secure options on PaymentIntents](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-three_d_secure)
