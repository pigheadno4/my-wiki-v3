<!-- Source URL: https://docs.stripe.com/google-pay -->
<!-- Fetched: 2026-05-07 -->

# Google Pay

Learn how to accept payments using Google Pay.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods).

Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer’s Google account.

Google Pay is fully compatible with Stripe’s products and features (for example, recurring payments), allowing you to use it in place of a traditional payment form whenever possible. Use it to accept payments for physical goods, donations, *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis), and so on.

> #### Google Pay terms
>
> By integrating Google Pay, you agree to Google’s [terms of service](https://payments.developers.google.com/terms/sellertos).

#### Payment method properties

- **Customer locations**

  Worldwide except India

- **Presentment currency**

  See [supported presentment currencies](https://docs.stripe.com/currencies.md#presentment-currencies)

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  Yes

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/google-pay.md#disputed-payments)

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/google-pay.md#refunds)

#### Business locations

Stripe accounts worldwide except India can accept Google Pay payments with local currency settlement.

#### Product support

- Connect
- Checkout
- Payment Links
- Elements
- Subscriptions
- Invoicing

## Using Stripe and Google Pay versus the Google Play billing system

This guide explains how to configure your app to accept Google Pay for physical goods, services, and other eligible items. Stripe processes these payments, and you pay only Stripe’s [processing fees](https://stripe.com/pricing).

For digital products, content, and subscriptions sold in the US or the European Economic Area (EEA), your Android app can accept payments directly in-app through a third-party payment processor such as Stripe. You can use these payment UIs:

- [Mobile Payment Element](https://docs.stripe.com/payments/mobile.md) to accept payments directly in-app
- [Stripe Checkout](https://docs.stripe.com/mobile/digital-goods/checkout.md) to redirect customers to a Stripe-hosted payment page
- [Payment Links](https://docs.stripe.com/mobile/digital-goods/payment-links.md) for a limited number of products and prices

For more information about which purchases must use the Google Play billing system, see Google Play’s [developer terms](https://support.google.com/googleplay/android-developer/answer/10281818).

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/google-pay?platform=android.

## Accept a payment using Google Pay in your Android app

`GooglePayLauncher`, part of the Stripe Android SDK, is the fastest and easiest way to start accepting Google Pay in your Android apps.

## Prerequisites

To support Google Pay in Android, you need the following:

- A `minSdkVersion` of `19` or higher.
- A `compileSdkVersion` of `28` or higher.

Additionally, if you wish to test with your own device, you need to [add a payment method to your Google Account](https://support.google.com/wallet/answer/12058983?visit_id=637947092743186187-653786796&rd=1).

## Set up your integration

This guide assumes you’re using the latest version of the Stripe Android SDK.

#### Groovy

```groovy
dependencies {
    implementation 'com.stripe:stripe-android:23.7.0'
}
```

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

## Create a PaymentIntent

### Server-side

Create a `PaymentIntent` on your server with an [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) and [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-currency). Always decide how much to charge on the server side, a trusted environment, as opposed to the client side. This prevents malicious customers from choosing their own prices.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
});
const clientSecret = paymentIntent.client_secret;
// Pass the client secret to the client
```

### Client-side

A PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). You can use the client secret in your Android app to securely complete the payment process instead of passing the entire PaymentIntent object. In your app, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

  private lateinit var paymentIntentClientSecret: String

  override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      // ...
      startCheckout()
  }

  private fun startCheckout() {
      // Request a PaymentIntent from your server and store its client secret in paymentIntentClientSecret
      // Click View full sample to see a complete implementation
  }
}
```

## Add the Google Pay button

Add the Google Pay button to your app by following [Google’s tutorial](https://developers.google.com/pay/api/android/guides/tutorial#add-button). This ensures you’re using the correct assets.

## Instantiate GooglePayLauncher

Next, create an instance of [GooglePayLauncher](https://github.com/stripe/stripe-android/blob/master/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt) in your `Activity` or `Fragment`. This must be done in `Activity#onCreate()`.

`GooglePayLauncher.Config` exposes both required and optional properties that configure `GooglePayLauncher`. See `GooglePayLauncher.Config` for more details on the configuration options.

#### Kotlin

```kotlin
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
    // fetch client_secret from backend
    private lateinit var clientSecret: String

    private lateinit var googlePayButton: PayButton

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        PaymentConfiguration.init(this, PUBLISHABLE_KEY)

        googlePayButton = /* TODO: Initialize button by following Google's guide. */

        val googlePayLauncher = GooglePayLauncher(
            activity = this,
            config = GooglePayLauncher.Config(
                environment = GooglePayEnvironment.Test,
                merchantCountryCode = "US",
                merchantName = "Widget Store"
            ),
            readyCallback = ::onGooglePayReady,
            resultCallback = ::onGooglePayResult
        )

        googlePayButton.setOnClickListener {
            // launch `GooglePayLauncher` to confirm a Payment Intent
            googlePayLauncher.presentForPaymentIntent(clientSecret)
        }
    }

    private fun onGooglePayReady(isReady: Boolean) {
        // implemented below
    }

    private fun onGooglePayResult(result: GooglePayLauncher.Result) {
        // implemented below
    }
}
```

After instantiating `GooglePayLauncher`, the `GooglePayLauncher.ReadyCallback` instance is called with a flag indicating whether Google Pay is available and ready to use. This flag can be used to update your UI to indicate to your customer that Google Pay is ready to be used.

#### Kotlin

```kotlin
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
    // continued from above

    private lateinit var googlePayButton: PayButton

    private fun onGooglePayReady(isReady: Boolean) {
        googlePayButton.isEnabled = isReady
    }
}
```

## Launch GooglePayLauncher

After Google Pay is available and your app has obtained a `PaymentIntent` or `SetupIntent` client secret, launch `GooglePayLauncher` using the appropriate method. When confirming a `PaymentIntent`, use `GooglePayLauncher#presentForPaymentIntent(clientSecret)`. When confirming a `SetupIntent`, use `GooglePayLauncher#presentForSetupIntent(clientSecret)`.

#### Kotlin

```kotlin
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
    // fetch client_secret from backend
    private lateinit var clientSecret: String

    private lateinit var googlePayButton: PayButton

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // instantiate `googlePayLauncher`

        googlePayButton.setOnClickListener {
            // launch `GooglePayLauncher` to confirm a Payment Intent
            googlePayLauncher.presentForPaymentIntent(clientSecret)
        }
    }
}
```

## Handle the result

Finally, implement `GooglePayLauncher.ResultCallback` to handle the result of the `GooglePayLauncher` operation.

The result can be `GooglePayLauncher.Result.Completed`, `GooglePayLauncher.Result.Canceled`, or `GooglePayLauncher.Result.Failed`.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    // continued from above

    private fun onGooglePayResult(result: GooglePayLauncher.Result) {
        when (result) {
            GooglePayLauncher.Result.Completed -> {
                // Payment succeeded, show a receipt view
            }
            GooglePayLauncher.Result.Canceled -> {
                // User canceled the operation
            }
            is GooglePayLauncher.Result.Failed -> {
                // Operation failed; inspect `result.error` for the exception
            }
        }
    }
}
```

## Go live with Google Pay

Follow [Google’s instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to request production access for your app. Choose the integration type **Gateway** when prompted, and provide screenshots of your app for review.

After your app has been approved, test your integration in production by setting the environment to `GooglePayEnvironment.Production`, and launching Google Pay from a signed, release build of your app. Remember to use your *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments) [API keys](https://docs.stripe.com/keys.md). You can use a `PaymentIntent` with [`capture_method` = `manual`](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to process a transaction without capturing the payment.

### Test Google Pay

Google allows you to make test payments through their [Test card suite](https://developers.google.com/pay/api/android/guides/resources/test-card-suite). The test suite supports using Stripe [test cards](https://docs.stripe.com/testing.md).

You must test Google Pay using a physical Android device instead of a simulated device, in a country where Google Pay is supported. Log in to a Google account on your test device with a real card saved to Google Wallet.

## Creating a PaymentMethod

If you confirm your payment on your server, you can use `GooglePayPaymentMethodLauncher` to only collect a `PaymentMethod` instead of confirm payment.

#### Kotlin

```kotlin
import com.google.android.gms.wallet.button.PayButton

class CheckoutActivity : AppCompatActivity() {
    private lateinit var googlePayButton: PayButton

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        PaymentConfiguration.init(this, PUBLISHABLE_KEY)

        googlePayButton = /* TODO: Initialize button by following Google's guide. */

        val googlePayLauncher = GooglePayPaymentMethodLauncher(
            activity = this,
            config = GooglePayPaymentMethodLauncher.Config(
                environment = GooglePayEnvironment.Test,
                merchantCountryCode = "FR",
                merchantName = "Widget Store"
            ),
            readyCallback = ::onGooglePayReady,
            resultCallback = ::onGooglePayResult
        )

        googlePayButton.setOnClickListener {
            googlePayLauncher.present(
                currencyCode = "EUR",
                amount = 2500
            )
        }
    }

    private fun onGooglePayReady(isReady: Boolean) {
        googlePayButton.isEnabled = isReady
    }

    private fun onGooglePayResult(
        result: GooglePayPaymentMethodLauncher.Result
    ) {
        when (result) {
            is GooglePayPaymentMethodLauncher.Result.Completed -> {
                // Payment details successfully captured.
                // Send the paymentMethodId to your server to finalize payment.
                val paymentMethodId = result.paymentMethod.id
            }
            GooglePayPaymentMethodLauncher.Result.Canceled -> {
                // User canceled the operation
            }
            is GooglePayPaymentMethodLauncher.Result.Failed -> {
                // Operation failed; inspect `result.error` for the exception
            }
        }
    }
}
```

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/google-pay?platform=react-native.

Stripe’s React Native SDK is the fastest and easiest way to start accepting Google Pay in your React Native apps. The [PlatformPayButton](https://stripe.dev/stripe-react-native/api-reference/index.html#PlatformPayButton) component wraps Google’s required UI, and you can use the `confirmPlatformPayPayment` and `createPlatformPayPaymentMethod` methods to seamlessly collect or create payments in your app with minimal setup.

> If you use React Native and Expo, Expo Go doesn’t support Google Pay. To use Google Pay with Expo, you must create a [development build](https://docs.expo.dev/get-started/set-up-your-environment/?mode=development-build&platform=android). If you already have an Expo Go project, you can [migrate it to a development build](https://docs.expo.dev/develop/development-builds/expo-go-to-dev-build/).

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Enable Google Pay

To use Google Pay, first enable the Google Pay API by adding the following to the `<application>` tag of your **AndroidManifest.xml**:

```xml
<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>
```

For more details, see Google Pay’s [Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup) for Android.

## Create a PaymentIntent [Server-side]

First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `card` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent` (this is also the default payment method if none are provided):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["card"],
  amount: 1099,
  currency: "usd",
});
```

A PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). You can use the client secret in your React Native app to securely complete the payment process instead of passing back the entire PaymentIntent object. In your app, request a PaymentIntent from your server and store its client secret.

## Initialize Google Pay [Client-side]

First, check whether or not the device supports Google Pay by calling `isPlatformPaySupported`.

```javascript
import { usePlatformPay } from '@stripe/stripe-react-native';

function PaymentScreen() {
  const { isPlatformPaySupported } = usePlatformPay();

  React.useEffect(() => {
    (async function () {
      if (!(await isPlatformPaySupported({ googlePay: {testEnv: true} }))) {
        Alert.alert('Google Pay is not supported.');
        return;
      }
    })();
  }, []);

  ...

  return (
    <View >
      ...
    </View>
  );
}
```

## Present the Google Pay sheet [Client-side]

After you know Google Pay is available and your app has obtained a `PaymentIntent` or `SetupIntent` client secret, call `confirmPlatformPayPayment`. When confirming a `SetupIntent`, use `confirmPlatformPaySetupIntent` instead.

```javascript
import {PlatformPayButton, usePlatformPay} from '@stripe/stripe-react-native';

function PaymentScreen() {
  const {
    isPlatformPaySupported,
    confirmPlatformPayPayment,
  } = usePlatformPay();

  React.useEffect(() => {
    ... // see above
  }, []);

  const fetchPaymentIntentClientSecret = async () => {
    // Fetch payment intent created on the server, see above
    const response = await fetch(`${API_URL}/create-payment-intent`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        currency: 'usd',
      }),
    });
    const { clientSecret } = await response.json();

    return clientSecret;
  };

  const pay = async () => {
    const clientSecret = await fetchPaymentIntentClientSecret();

    const { error, paymentIntent } = await confirmPlatformPayPayment(
      clientSecret,
      {
        googlePay: {
          testEnv: true,
          merchantName: 'My merchant name',
          merchantCountryCode: 'US',
          currencyCode: 'USD',
          billingAddressConfig: {
            format: PlatformPay.BillingAddressFormat.Full,
            isPhoneNumberRequired: true,
            isRequired: true,
          },
        },
      }
    );

    if (error) {
      Alert.alert(error.code, error.message);
      // Update UI to prompt user to retry payment (and possibly another payment method)
      return;
    }
    Alert.alert('Success', 'The payment was confirmed successfully.');
    console.log(JSON.stringify(paymentIntent, null, 2));
  };

  return (
    <View >
      <PlatformPayButton
        type={PlatformPay.ButtonType.Pay}
        onPress={pay}
        style={{
          width: '100%',
          height: 50,
        }}
      />
    </View>
  );
}
```

## Optional: Create a PaymentMethod [Client-side]

If you confirm your payment on your server, you can use Google Pay to only collect a `PaymentMethod` instead of confirm a payment. To make that call, use the `createPlatformPayPaymentMethod` method:

```javascript
import {PlatformPayButton, usePlatformPay} from '@stripe/stripe-react-native';

function PaymentScreen() {
  const {
    isPlatformPaySupported,
    createPlatformPayPaymentMethod,
  } = usePlatformPay();

  React.useEffect(() => {
    ... // see above
  }, []);

  const createPaymentMethod = async () => {
    const { error, paymentMethod } = await createPlatformPayPaymentMethod({
      googlePay: {
        amount: 12,
        currencyCode: 'USD',
        testEnv: true,
        merchantName: 'Test',
        merchantCountryCode: 'US',
      },
    });

    if (error) {
      Alert.alert(error.code, error.message);
      return;
    } else if (paymentMethod) {
      Alert.alert(
        'Success',
        `The payment method was created successfully. paymentMethodId: ${paymentMethod.id}`
      );
    }
  };

  return (
    <View >
      <PlatformPayButton
        type={PlatformPay.ButtonType.GooglePayMark}
        onPress={createPaymentMethod}
        style={{
          width: '100%',
          height: 50,
        }}
      />
    </View>
  );
}
```

## Go live with Google Pay

Follow [Google’s instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) to request production access for your app. Choose the integration type **Gateway** when prompted, and provide screenshots of your app for review.

After your app has been approved, test your integration in production by using `testEnv: false`, and launching Google Pay from a signed, release build of your app. Remember to use your *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments) [API keys](https://docs.stripe.com/keys.md). You can use a `PaymentIntent` with [`capture_method` = `manual`](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to process a transaction without capturing the payment.

### Test Google Pay

Google allows you to make test payments through their [Test card suite](https://developers.google.com/pay/api/android/guides/resources/test-card-suite). The test suite supports using Stripe [test cards](https://docs.stripe.com/testing.md).

You must test Google Pay using a physical Android device instead of a simulated device, in a country where Google Pay is supported. Log in to a Google account on your test device with a real card saved to Google Wallet.

# Web

> This is a Web for when platform is web. View the full page at https://docs.stripe.com/google-pay?platform=web.

## Accept Google Pay on the web

You can accept Google Pay payments on the web using [Checkout](https://docs.stripe.com/payments/checkout.md) or [Elements](https://docs.stripe.com/payments/elements.md) by enabling Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). Using Google Pay in Checkout requires no additional code implementation. For Elements, refer to the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md) or [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=checkout) guides to learn how to add Google Pay to your site.

You need to serve from an HTTPS webpage with a TLS domain-validated certificate to accept Google Pay payments on the web.

### Register your domain with Google Pay

To use Google Pay, you must register all of your web domains that show a Google Pay button. That includes top-level domains (for example, **stripe.com**) and subdomains (for example, **shop.stripe.com**), in production and testing.

> #### Subdomains
>
> `www` is a subdomain (for example, **www.stripe.com**) that you must also register.

Register your domain on the [Payment methods domains page](https://dashboard.stripe.com/settings/payment_method_domains) in the Dashboard or use the API with your live secret key, as shown in the following example. Register your domain only once per account.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethodDomain = await stripe.paymentMethodDomains.create({
  domain_name: "example.com",
});
```

When using [direct charges](https://docs.stripe.com/connect/direct-charges.md) with *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you need to configure the domain for each connected account using the API. This isn’t a requirement for connected accounts using other charge types.

After registering your domains, you can make payments on your site with your live API keys.

## Test Google Pay

Google allows you to make test payments through their [Test card suite](https://developers.google.com/pay/api/android/guides/resources/test-card-suite). You can use Stripe [test cards](https://docs.stripe.com/testing.md) with the test suite.

Before you can use a Stripe test card, you must add a real card to your wallet to make Google Pay display. If you don’t meet device and integration requirements, Stripe doesn’t render Google Pay as a payment option. To troubleshoot rendering issues with Google Pay, use our [test page](https://docs.stripe.com/testing/wallets.md).

## Disputes

Users must authenticate payments with their Google Pay accounts, which reduces the risk of fraud or unrecognized payments. However, users can still dispute transactions after they complete payment. You can submit evidence to contest a dispute directly. The dispute process is the same as that for card payments. Learn how to [manage disputes](https://docs.stripe.com/disputes/responding.md).

### Liability shift for Google Pay charges

Google Pay supports [liability shift](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments) globally. This is true automatically for users on Stripe-hosted products and using Stripe.js. For Visa transactions outside of a Stripe-hosted product, you must enable liability shift in the Google Pay & Wallet Console. To do so, go to your **_Google Pay & Wallet Console_**, select **_Google Pay API_** in the navigation bar on the left, and then enable **_Fraud Liability Protection for Visa Device Tokens_** for liability shift protection.

There are three use cases of Google Pay transactions:

1. If the user adds a card to the Google Pay app using their mobile device, this card is saved as a Device Primary Account Number (DPAN), and it supports liability shift by default.
1. If the user adds a card to Chrome or a Google property (for example, YouTube, or Play), it’s saved as a Funding Primary Account Number (FPAN). When you use [3D Secure](https://docs.stripe.com/payments/3d-secure.md), we globally support liability shift for all major networks, including Visa. You can customize [Stripe Radar rules](https://docs.stripe.com/radar/rules.md#request-3d-secure) to request activation of 3D Secure.
1. If the user selects Google Pay as the payment method on an e-commerce site or in an app that pays with Google Pay, the cards are saved as e-commerce tokens that represent the cards on file. Neither liability shift nor 3D Secure are supported for e-commerce tokens at this time.

For Sigma users, the `charges` table contains a `card_token_type` field that indicates the Google Pay transaction type. An FPAN transaction sets the `card_token_type` to `fpan`. DPAN and ecommerce token transactions set the `card_token_type` to `dpan_or_ecommerce_token`.

## Refunds

You can partially or fully refund any successful Google Pay payment. The refund process is the same as that for card payments. See [Refund and cancel payments](https://docs.stripe.com/refunds.md) for instructions on initiating or managing refunds.
