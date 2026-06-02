<!-- Source URL: https://docs.stripe.com/payments/vault-and-forward -->
<!-- Fetched: 2026-05-11 -->

# Forward card details to third-party API endpoints

Use the Vault and Forward API to securely share card details across multiple processors.

The Vault and Forward API allows you to tokenize and store card details in Stripe’s PCI-compliant vault and route that data to supported processors or endpoints. Leverage the API to:

- Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) [across multiple processors](https://docs.stripe.com/payments/forwarding-third-party-processors.md).
- Use Stripe as your primary vault for card details across processors.
- Route card details to your own [PCI compliant token vault](https://docs.stripe.com/payments/forwarding-token-vault.md).

> #### Request access
>
> To gain access to use Stripe’s forwarding service, contact [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

## Forward requests to destination endpoints and populate card details from Stripe’s vault

API flows for forwarding card details (See full diagram at https://docs.stripe.com/payments/vault-and-forward)

## Collect card details and create a PaymentMethod

To collect card details, use the Payment Element to create [a PaymentMethod](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy.md?type=payment#create-pm). After you create a PaymentMethod, we automatically store card details in Stripe’s PCI compliant vault. If you have your own frontend, you can still use the Vault and Forward API by [creating a PaymentMethod directly](https://docs.stripe.com/api/payment_methods/create.md).

Typically, you can only reuse PaymentMethods by attaching them to a Customer. However, the Vault and Forward API accepts all PaymentMethod objects, including those not attached to a customer.

Similarly, the Vault and Forward API doesn’t [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) or [capture](https://docs.stripe.com/api/payment_intents/capture.md) PaymentIntents. As a result, you might unintentionally use them to capture a payment on Stripe that was already captured on another processor.

> #### Link transactions
>
> The consumer payment credentials saved with Link transactions can’t be transferred between payment processors. Any credentials saved through Link are excluded from forwarding.

CVCs expire automatically after a certain time period and also expire when used with the Vault and Forward API. If you require a CVC after either of these conditions are met, you must re-collect the card details.

### Preserve CVC with SetupIntents

If you use [SetupIntents](https://docs.stripe.com/api/setup_intents.md) to collect card details before forwarding, card validation during SetupIntent confirmation can consume the CVC. When this happens, subsequent Forwarding API calls won’t include the CVC, which can cause failures with processors that require it.

To access options for preserving CVC availability when using SetupIntents with the Forwarding API, contact [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DPreserve%2520CVC%2520with%2520SetupIntents%2520and%2520Forwarding%2520API).

## Create a ForwardingRequest

To send card details from Stripe’s vault, you must [Create a ForwardingRequest](https://docs.stripe.com/api/forwarding/forwarding_requests/create.md) and include the following parameters:

- `payment_method`: Object that enables Stripe to identify your customer’s card details within Stripe’s vault and insert that data into the request body.
- `url`: The exact destination endpoint of your request.
- `request.body`: The API request body that you want to send to the destination endpoint (for example, the payments request you send to another processor). Leave any field where you normally input your customer’s card details blank.
- `replacements`: Fields that you want Stripe to substitute in the `request.body`. The [available fields](https://docs.stripe.com/api/forwarding/forwarding_requests/create.md#forwarding_request_create-replacements) that we recommend always setting are `card_number`, `card_expiry`, `card_cvc`, and `cardholder_name`. For example, including `card_number` in the `replacements` array replaces the appropriate card number field for your destination endpoint in the `request.body`.

> The placeholder value for each card field in `request.body` must match the JSON type that the destination endpoint expects. Use `""` for string fields and `0` for numeric fields. For example, if your destination endpoint requires `expiryMonth` and `expiryYear` as integers, set them to `0` instead of `""`:
>
> ```json
> "paymentMethod": {"number": "", "expiryMonth": 0, "expiryYear": 0, "cvc": "", "holderName": ""}
> ```

````

> Stripe might be more lenient than other processors in validating the cardholder name field. If you use the `cardholder_name` replacements field, you’re responsible for making sure that the names you use pass any validation enforced by the destination endpoint. For example, if the destination endpoint expects all names to only contain the letters A-Z with no accent marks or other writing systems, you must make sure the card details you forward meet this requirement. An alternative is to not use the `cardholder_name` replacements field and specify the cardholder name in your request body directly in your request.

You must format your request based on the data that the destination endpoint expects. In the example below, the destination endpoint expects an `Idempotency-Key` header and accepts a JSON body with the payment details.

We require you to pass API keys for the destination endpoint on each API request. Stripe forwards the request using the API keys you provide, and only retains hashed and encrypted versions of destination endpoint API keys.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const request = await stripe.forwarding.requests.create(
  {
    payment_method: '{{PAYMENTMETHOD_ID}}',
    url: 'https://endpoint-url/v1/payments',
    request: {
      headers: [
        {
          name: 'Destination-API-Key',
          value: '{{DESTINATION_API_KEY}}',
        },
        {
          name: 'Destination-Idempotency-Key',
          value: '{{DESTINATION_IDEMPOTENCY_KEY}}',
        },
      ],
      body: '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    },
    replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
  },
  {
    idempotencyKey: '{{IDEMPOTENCYKEY_ID}}',
  }
);
````

> You can provide an `Idempotency-Key` to make sure that requests with the same key result in only one outbound request. Use a different and unique key for Stripe and any idempotency keys you provide on the underlying third-party request.
>
> Use a new `Idempotency-Key` every time you make updates to `request.body` or `request.header` fields. Passing in the older idempotency key results in the API replaying older responses, including any previous validation errors or destination endpoint errors. We recommend that you use a new idempotency key when retrying requests that encountered an error reaching the destination endpoint to make sure the request is retried at the destination.

## Forward wallet payment methods

Use the Vault and Forward API to forward Apple Pay and Google Pay payment methods. Depending on the wallet and tokenization type, use different replacement fields so the wallet credentials forward correctly.

### Supported wallets

Stripe supports the following wallets:

- **Apple Pay**: Device Primary Account Numbers (DPANs) only. Apple Pay Merchant Primary Account Numbers (MPANs) aren’t supported.
- **Google Pay**: Both Funding Primary Account Numbers (FPANs) and Device Primary Account Numbers (DPANs).

To access wallet forwarding, contact [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520wallet%2520forwarding%2520for%2520Vault%2520and%2520Forward%3F).

> Link Payments currently unsupported for the Vault and Forward API. Link card transactions have a [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object.md) with a [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type) of `card` and a [wallet type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-wallet-type) of `link`. Don’t include PaymentMethods in forwarding requests.
>
> If your integration uses Link, route Link card transactions to Stripe for processing rather than forwarding them to a third-party endpoint.

### Detect wallet payment methods

To determine which replacement fields to use, fetch the `PaymentMethod` and check the wallet type and tokenization method:

#### Google Pay

The `tokenization_type` field indicates whether the payment method uses an FPAN or DPAN:

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "type": "card",
  "card": {
    "wallet": {
      "type": "google_pay",
      "google_pay": {
        "tokenization_type": "dpan_or_ecommerce_token" // or "fpan"
      }
    }
  }
}
```

#### Apple Pay

Apple Pay payment methods always use DPANs, indicated by the `tokenization_type` field:

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "type": "card",
  "card": {
    "wallet": {
      "type": "apple_pay",
      "apple_pay": {
        "tokenization_type": "dpan",
        "cryptogram_type": "emv"
      }
    }
  }
}
```

### Replacement fields for wallets

The replacement fields you use depend on the wallet type:

- **Google Pay FPANs**: Use standard card replacement fields (`card_number`, `card_expiry`, `card_cvc`, `cardholder_name`)
- **Google Pay DPANs**: Use network token replacement fields (`network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator`)
- **Apple Pay DPANs**: Use network token replacement fields (`network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator`)

### Forward Google Pay FPAN

For Google Pay FPANs, use the same replacement fields as regular card payments:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const request = await stripe.forwarding.requests.create(
  {
    payment_method: "{{PAYMENTMETHOD_ID}}",
    url: "https://endpoint-url/v1/payments",
    request: {
      headers: [
        {
          name: "Destination-API-Key",
          value: "{{DESTINATION_API_KEY}}",
        },
        {
          name: "Destination-Idempotency-Key",
          value: "{{DESTINATION_IDEMPOTENCY_KEY}}",
        },
      ],
      body: '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    },
    replacements: ["card_number", "card_expiry", "card_cvc", "cardholder_name"],
  },
  {
    idempotencyKey: "{{IDEMPOTENCYKEY_ID}}",
  },
);
```

### Forward wallet DPANs

For both Google Pay and Apple Pay DPANs, use network token replacement fields:

#### Google Pay

```bash
curl https://api.stripe.com/v1/forwarding/requests \
  -u "sk_test_4eC39HqLyjWDarjtT1zdp7dc:" \
  -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
  -d payment_method="{{PAYMENT_METHOD}}" \
  --data-urlencode url="https://endpoint-url/v1/payments" \
  -d "replacements[0]"=network_token_number \
  -d "replacements[1]"=network_token_cryptogram \
  -d "replacements[2]"=network_token_expiry \
  -d "replacements[3]"=network_token_electronic_commerce_indicator \
  --data-urlencode 'request[body]={"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"networkToken":{"number":"","cryptogram":"","expiryMonth":"","expiryYear":"","electronicCommerceIndicator":""}},"reference":"{{REFERENCE_ID}}"}' \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"="{{DESTINATION_API_KEY}}" \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"="{{DESTINATION_IDEMPOTENCY_KEY}}"
```

#### Apple Pay

```bash
curl https://api.stripe.com/v1/forwarding/requests \
  -u "sk_test_4eC39HqLyjWDarjtT1zdp7dc:" \
  -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
  -d payment_method="{{PAYMENT_METHOD}}" \
  --data-urlencode url="https://endpoint-url/v1/payments" \
  -d "replacements[0]"=network_token_number \
  -d "replacements[1]"=network_token_cryptogram \
  -d "replacements[2]"=network_token_expiry \
  -d "replacements[3]"=network_token_electronic_commerce_indicator \
  --data-urlencode 'request[body]={"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"networkToken":{"number":"","cryptogram":"","expiryMonth":"","expiryYear":"","electronicCommerceIndicator":""}},"reference":"{{REFERENCE_ID}}"}' \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"="{{DESTINATION_API_KEY}}" \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"="{{DESTINATION_IDEMPOTENCY_KEY}}"
```

## Forward the request with card details

Stripe makes a request to the destination endpoint on your behalf by inserting the card details from the PaymentMethod into the `request.body`. Where enabled and available, the Card Account Updater (CAU) automatically attempts to update and provide the latest available card details for requests.

Stripe then forwards the request to the destination endpoint. For example:

1. Stripe makes a POST request to the endpoint:

   ```
   POST /v1/payments HTTP/1.1
   User-Agent: Stripe
   Accept: */*
   Host: endpoint-url
   Content-Type: application/json
   Content-Length: 321
   ```

1. Stripe includes the following headers:

   ```
   Destination-API-Key: {{DESTINATION_API_KEY}}
   Destination-Idempotency-Key: {{DESTINATION_IDEMPOTENCY_KEY}}
   ```

1. Stripe includes the following JSON body in the request:

   ```
   {
     amount: {
       value: 1000,
       currency: 'usd'
     },
     paymentMethod: {number: '4242424242424242',
       expiryMonth: '03',
       expiryYear: '2030',
       cvc: '123',
       holderName: 'First Last',
     },
     reference: '{{REFERENCE_ID}}'
   }
   ```

> If you’re using the Vault and the Forward API to make an authorization request, you must handle any post-transaction actions, such as refunds or disputes, directly with the third-party processor. Contact Stripe support if you require 3DS authentication across your multiprocessor setup.

## Handle the response from the destination endpoint

When you use the Vault and Forward API to forward card details to a third-party processor, Stripe synchronously waits for a response from the destination endpoint. The timeout period for this response is less than a minute. Stripe redacts identified PCI-sensitive data, stores the redacted response from the destination endpoint, and returns a [ForwardingRequest](https://docs.stripe.com/api/forwarding/request/object.md) object, which contains data about the request and response.

> When you use the Vault and Forward API to forward card details to a third-party processor, Stripe can’t guarantee that the processor will provide any particular response to your forwarded API requests. If the third-party processor is unresponsive, you must reach out directly to that processor to resolve the issue.

```json
{
  id: "fwdreq_123",
  object: "forwarding.request",
  payment_method: "{{PAYMENT_METHOD}}",
  request_details: {
    body: '{
      "amount": {
        "value": 1000,
        "currency": "usd"
      },
      "paymentMethod": {
        "number": "424242******4242",
        "expiryMonth": "03",
        "expiryYear": "2030",
        "cvc": "***",
        "holderName": "First Last",
      },
      "reference": "{{REFERENCE_ID}}"
    }',
    headers: [
      {
        name: "Content-Type",
        value: "application/json",
      },
      {
        name: "Destination-API-Key",
        value: "{{DESTINATION_API_KEY}}",
      },
      {
        name: "Destination-Idempotency-Key",
        value: "{{DESTINATION_IDEMPOTENCY_KEY}}",
      },
      ...
    ]
  },
  request_context: {
      "destination_duration": 234,
      "destination_ip_address": "35.190.113.80"
  },
  response_details: {
    body: '{
      // Response from the third-party endpoint goes here
      ...
    }',
    headers: [
      ...
    ],
    status: 200,
  },
  replacements: [
    "card_number",
    "card_expiry",
    "card_cvc",
    "cardholder_name"
  ]
  ...
}
```

## Configure your Vault and Forward API endpoint

To set up your Vault and Forward API endpoint, you must:

- [Confirm that we support the destination endpoint](https://docs.stripe.com/payments/vault-and-forward.md#confirm-endpoint).
- Provide a test and production account with [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).
- [Share the production details](https://docs.stripe.com/payments/vault-and-forward.md#share-production-details) for the destination endpoint with [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

### Confirm that we support the destination endpoint

Stripe supports forwarding API requests to the following endpoints:

- **Accertify**:
  - `icnow01.accertify.net/icNowImport/[path]`
- **Adyen**:
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v68/payments`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v68/storedPaymentMethods`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v69/payments`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v69/storedPaymentMethods`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v70/payments`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v70/storedPaymentMethods`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v71/payments`
  - `[prefix]-checkout-live.adyenpayments.com/checkout/v71/storedPaymentMethods`
- **Basis Theory**:
  - `api.basistheory.com/connections/stripe-forward/tokenize`
- **Braintree**:
  - `payments.braintree-api.com/graphql`
- **CardPointe**:
  - `[prefix].cardconnect.com/cardconnect/rest/auth`
- **Checkout**:
  - `api.checkout.com/tokens`
  - `api.checkout.com/payments`
- **Evervault**:
  - `[prefix].relay.evervault.app`
- **Expedia**:
  - `api.ean.com/v3/itineraries`
- **Fat Zebra**:
  - `gateway.pmnts.io/v1.0/credit_cards`
- **Fiserv**:
  - `prod.api.firstdata.com/gateway/v2/payments`
- **FlexPay**:
  - `api.flexpay.io/v1/gateways/charge`
- **GMO Payment Gateway**:
  - `p01.mul-pay.jp/payment/ExecTran.json`
- **PaymentsOS**:
  - `api.paymentsos.com/tokens`
- **PCI Vault**:
  - `api.pcivault.io/v1/capture/stripe`
- **ProcessOut**:
  - `api.processout.com/cards`
- **Rewards Network**:
  - `api.rewardsnetwork.com/v2/members/enroll`
  - `api.rewardsnetwork.com/v2/members/*/cards`
- **Shift4**:
  - `api.shift4.com/charges`
- **SoftBank**:
  - `stbfep.sps-system.com/api/xmlapi.do`
- **Spreedly**:
  - `core.spreedly.com/v1/payment_methods.json`
- **TabaPay**:
  - `[prefix]/v1/clients/[ClientID]/accounts`
- **TokenEx**:
  - `tgapi.tokenex.com/Tokenize/Proxy/[ProfileID]`
- **VGS (Very Good Security)**:
  - `[prefix].live.verygoodproxy.com/cards`
- **Worldpay**:
  - `access.worldpay.com/api/payments`
  - `access.worldpay.com/cardPayments/customerInitiatedTransactions`
  - `access.worldpay.com/tokens`
  - `secure.worldpay.com/jsp/merchant/xml/paymentService`
- **Xsolla**:
  - `ps.xsolla.com/forwarding/payments/card`
- [Your own PCI-compliant token vault](https://docs.stripe.com/payments/forwarding-token-vault.md)

Stripe supports HTTPS-based APIs that accept JSON/XML requests and return JSON/XML responses. If your destination endpoint isn’t supported or you require a different API format, share the endpoint details with [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520Access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F) to get support for your specific needs.

### Supported countries

The Vault and Forward API can only forward requests to the following countries:

### Countries eligible for request forwarding

- AE
- AG
- AL
- AM
- AO
- AR
- AT
- AU
- AZ
- BA
- BD
- BE
- BG
- BH
- BJ
- BN
- BO
- BS
- BT
- BW
- CA
- CH
- CI
- CL
- CO
- CR
- CY
- CZ
- DE
- DK
- DO
- DZ
- EC
- EE
- EG
- ES
- ET
- FI
- FR
- GA
- GB
- GH
- GI
- GM
- GR
- GT
- GY
- HK
- HR
- HU
- ID
- IE
- IL
- IN
- IS
- IT
- JM
- JO
- JP
- KE
- KH
- KR
- KW
- KZ
- LA
- LC
- LI
- LK
- LT
- LU
- LV
- MA
- MC
- MD
- MG
- MK
- MN
- MO
- MT
- MU
- MX
- MY
- MZ
- NA
- NE
- NG
- NL
- NO
- NZ
- OM
- PA
- PE
- PH
- PK
- PL
- PT
- PY
- QA
- RO
- RS
- RW
- SA
- SE
- SG
- SI
- SK
- SM
- SN
- SV
- TH
- TN
- TR
- TT
- TW
- TZ
- US
- UY
- UZ
- VN
- ZA

Additionally, ensure that your Stripe account is registered in one of these countries:

### Countries eligible for the Vault and Forward API

- AE
- AT
- AU
- BE
- BG
- BR
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GI
- GR
- HK
- HR
- HU
- ID
- IE
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MX
- MY
- NL
- NO
- NZ
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- US

### Provide test accounts to Stripe support

To access the Vault and Forward API, share the [account IDs](https://dashboard.stripe.com/settings/account) (`acct_xxxx`) for your test accounts with [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

### Share production details

Share the production details for destination endpoint with [Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F). These include the following for destination endpoint: URL, HTTP method, documentation, fields, request headers, and encryption keys. Stripe then sets up destination endpoint for use with the Vault and Forward API in live mode.

To share third-party API keys, you must encrypt them by using the Stripe public key that’s specific to the Vault and Forward API. Start by [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84) using [the GNU Privacy Guard (PGP)](http://gnupg.org). After you familiarize yourself with the basics of PGP, use the following PGP key to encrypt your third-party API keys:

### Vault and Forward API PGP key

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
UraCYX03loNHRxLCyeHR4GA=
=bbos
-----END PGP PUBLIC KEY BLOCK-----
```

To encrypt your third-party API keys with the Vault and Forward API PGP key:

1. Create a file named `hash_encrypt_key.sh` with the content below. The script generates a `SHA256` hash of your API key, encrypts it with Stripe’s public key, and then `Base64` encodes it.

   > #### Required utilities
   >
   > To run the script, you must first install the `sha256sum`, `gpg`, and `base64` utilities.

   ```bash
   #!/bin/sh
   set -euo pipefail
   fail () { printf "Error: $1\n" >&2 && exit 1; }

   STRIPE_PUBLIC_KEY=AE863ADA1603150856C0A853A7B203177D034588
   API_KEY=$(printf "$1" | tr -d '\n' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')

   [ -x "$(command -v sha256sum)" ]                    || fail "sha256sum is not installed."
   [ -x "$(command -v gpg)" ]                          || fail "gpg is not installed."
   [ -x "$(command -v base64)" ]                       || fail "base64 is not installed."
   [ ! -z "$API_KEY" ]                                 || fail "Please pass in an API key."
   grep -iqv "Basic \|Bearer " <<< "$API_KEY"          || fail "Please omit the Basic/Bearer prefix."
   gpg --list-keys $STRIPE_PUBLIC_KEY > /dev/null 2>&1 || fail "Stripe public key not imported."

   printf "$API_KEY" | sha256sum | cut -d " " -f 1 | tr -d '\n' | gpg -e -r $STRIPE_PUBLIC_KEY --always-trust | base64 > encrypted_hashed_key.txt
   printf "Successfully generated encrypted_hashed_key.txt\n"
   ```

1. Run the script by passing your third-party API key in single quotes, omitting any `Bearer` or `Basic` prefix. The key must be the exact key that you use for actual requests to the destination endpoint, not including any prefix.

   The script produces a file named `encrypted_hashed_key.txt`.

   ```bash
   sh hash_encrypt_key.sh '<THIRD_PARTY_API_KEY>'
   ```

### Use Stripe restricted API keys with Vault and Forward

Use a [restricted API key (RAK)](https://docs.stripe.com/keys-best-practices.md#limit-access) to allow server-side access to only the Vault and Forward endpoints.

- Enable the minimal permissions for your restricted key:
  - `forwarding_request_write`: Required to [create](https://docs.stripe.com/api/forwarding/forwarding_requests/create.md) ForwardingRequests.
  - `forwarding_request_read`: (Optional) to [retrieve](https://docs.stripe.com/api/forwarding/forwarding_requests/retrieve.md) or [list](https://docs.stripe.com/api/forwarding/forwarding_requests/list.md) ForwardingRequests.
- Use the restricted API key as your `Authorization: Bearer <rk_...>` credential when calling `/v1/forwarding/requests` from your server.
- If your integration also calls other APIs, add only the minimal additional permissions those calls require.

Learn more about how to [create a restricted API key](https://docs.stripe.com/keys.md#create-restricted-api-secret-key).

## Test your integration

To confirm that your integration works correctly with destination endpoint, initiate a ForwardingRequest using the PaymentMethod you created. This example uses `pm_card_visa` as a payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const request = await stripe.forwarding.requests.create(
  {
    payment_method: "pm_card_visa",
    url: "{{DESTINATION ENDPOINT}}",
    request: {
      headers: [
        {
          name: "Destination-API-Key",
          value: "{{DESTINATION_API_KEY}}",
        },
        {
          name: "Destination-Idempotency-Key",
          value: "{{DESTINATION_IDEMPOTENCY_KEY}}",
        },
      ],
      body: '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    },
    replacements: ["card_number", "card_expiry", "card_cvc", "cardholder_name"],
  },
  {
    idempotencyKey: "{{IDEMPOTENCYKEY_ID}}",
  },
);
```

> The Vault and Forward API treats any response from the destination endpoint as a `success` and returns a `200`, along with the destination endpoint’s response code in the `response.body`. For example, when the destination endpoint returns a status code of `400` to Stripe, the Vault and Forward API responds with a status code of `200`. The `response.body` includes the destination endpoint’s `400` response and error message. Separately test the API request that you send to your destination endpoint to make sure that you don’t have any errors.

### View your request logs in the Dashboard

You can view request logs and errors related to the Vault and Forward API in [Workbench](https://docs.stripe.com/workbench/overview.md#request-logs). Additionally, you can use the [List API](https://docs.stripe.com/api/forwarding/forwarding_requests/list.md) to fetch the logs from Stripe.

> The `request.headers` and `request.body` in the incoming request are encrypted and appear as `encrypted_request` in the Dashboard.
