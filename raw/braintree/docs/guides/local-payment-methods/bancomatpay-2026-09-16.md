<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/local-payment-methods/bancomatpay -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: BANCOMAT Pay
slug: /docs/guides/local-payment-methods/bancomatpay/
createTime: '2025-04-01T23:29:19.176Z'
updateTime: '2025-04-01T23:29:19.217Z'
---



# BANCOMAT Pay


### Overview


**AVAILABILITY**
BANCOMAT Pay is currently in limited release and is available to pilot merchants in selected countries. If you want to participate in the pilot, [contact us](/braintree/help/acceptPaymentTypes) .

BANCOMAT Pay is a local payment method that a customer can use to place an order and then complete
the payment with their BANCOMAT Pay mobile digital wallet app.
- [Create, verify, and link](/braintree/articles/guides/payment-methods/paypal/setup-guide)your PayPal business account in the Braintree Control Panel. In order to process Local Payment Methods, you need to have a valid PayPal business account.
- Make sure you are using the latest version of the[Client SDK](https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/javascript/v3).

| Payment type | Buyer countries | Seller countries | Currency codes | Customer transaction limits |
| --- | --- | --- | --- | --- |
| `bancomatpay` | Italy | Global except Russia, Japan, Brazil | `EUR` | Min: 0.01 EUR |


### Loading the SDK

You will need to load the Client SDK and Local Payments SDK. One way is to load these from external
sources:
### HTML
```html
<script src="https://js.braintreegateway.com/web/3.111.0/js/client.min.js"></script>
<script src="https://js.braintreegateway.com/web/3.111.0/js/local-payment.min.js"></script>
```
Other methods of loading SDKs are discussed in[the documentation for the Client SDK](https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/javascript/v3).
### Capturing BANCOMAT Pay Transactions

BANCOMAT Pay works by circumventing the normal tokenization process. For this reason, merchants**must**be signed up to receive and process the[LPMs webhooks](/braintree/docs/reference/general/webhooks/local-payment-methods/ruby).
The merchant will receive the single-use token they must transact upon through thelocal_payment_completedwebhook.
### BANCOMAT Pay with GraphQL


**NOTE**
BANCOMAT Pay is currently available only through the Javascript Client SDK and various server-side SDKs.


### Example Requests

The client-side implementation of BANCOMAT Pay is the same as described for[other LPM types](/braintree/docs/guides/local-payment-methods/client-side-custom/javascript/v3)with these caveats:
- No pop-up will be launched, and the merchant will not receive a response with a nonce. The merchant will receive a response with a payment ID that they will need to keep track of in their system.


### Callback
```javascript
function createLocalPaymentClickListener(type) {
    return function (event) {
        event.preventDefault();
        localPaymentInstance.startPayment({
            paymentType: 'bancomatpay',
            amount: '10.00',
            currencyCode: 'EUR',
            phone: '0226830102',
            phoneCountryCode: '39',
            givenName: 'Joe',
            surname: 'Doe',
            address: {
                countryCode: 'IT'
            },
            onPaymentStart: function (data) {
                // NOTE: It is critical here to store data.paymentId on your server
                // so it can be mapped to a webhook sent by Braintree once the
                // buyer completes their payment. See Start the payment
                // section for details.
            }
        }, function (startPaymentError) {
            if (startPaymentError) {
                if (startPaymentError.code === 'LOCAL_PAYMENT_START_PAYMENT_FAILED') {
                    console.error('LocalPayment startPayment failed.');
                } else {
                    console.error('Error!', startPaymentError);
                }
            } else {
                // Success! Respond accordingly here.
            }
        });
    };
}
```

### Promise
```javascript
function createLocalPaymentClickListener(type) {
    return function (event) {
        event.preventDefault();
        localPaymentInstance.startPayment({
            paymentType: 'bancomatpay',
            amount: '10.00',
            currencyCode: 'EUR',
            phone: '0226830102',
            phoneCountryCode: '39',
            givenName: 'Joe',
            surname: 'Doe',
            address: {
                countryCode: 'IT'
            },
            onPaymentStart: function (data) {
                // NOTE: It is critical here to store data.paymentId on your server
                // so it can be mapped to a webhook sent by Braintree once the
                // buyer completes their payment. See Start the payment
                // section for details.
            }
        }).then(function() {
            // Success! Respond accordingly here.
        }).catch(function (err) {
            if (err.code === 'LOCAL_PAYMENT_START_PAYMENT_FAILED') {
                console.error('LocalPayment startPayment failed.');
            } else {
                console.error('Error!', err);
            }
        });
    };
}
```
[See the Local Payment Method guide](/braintree/docs/guides/local-payment-methods/overview)for an overview of other implementation details.