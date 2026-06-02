<!-- Source URL: https://docs.stripe.com/payments/3d-secure/authentication-flow -->
<!-- Fetched: 2026-05-08 -->

# Authenticate with 3D Secure

Integrate 3D Secure (3DS) into your checkout flow.

> Major card brands no longer support 3D Secure 1. If your implementation uses 3D Secure 1, update it to use the [Payment Intents](https://docs.stripe.com/api/payment_intents.md) and [Setup Intents](https://docs.stripe.com/api/setup_intents.md) APIs. Using those APIs:
>
> - Supports [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2).

- Takes advantage of [Dynamic 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar).
- Complies with European [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md) regulations.

You can integrate 3D Secure (3DS) authentication into your checkout flow on multiple platforms, including Web, iOS, Android, and React Native. This integration runs [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2) when supported by the customer’s bank and falls back to 3D Secure 1 otherwise. You can also perform 3DS authentication on Stripe while acquiring the transaction with another payment service provider (PSP) by using the [standalone 3DS](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure.md) product.

#### Web

![Checkout page](assets/stripe-3ds-checkout-page.png)

The customer enters their card details.
![Loading symbol](assets/stripe-3ds-frictionless-flow.png)

The customer’s bank assesses the transaction and can complete 3D Secure at this step.
![Authentication modal](assets/stripe-3ds-challenge-flow.png)

If required by their bank, the customer completes an additional authentication step.

#### iOS

![Checkout Screen](assets/stripe-3ds-ios-checkout.png)

The customer enters their card details.
![Loading screen](assets/stripe-3ds-ios-loading.png)

The SDK presents a loading screen while the customer’s bank checks whether authentication is required.
![Challenge flow screen](assets/stripe-3ds-ios-otp.png)

If required by their bank, the SDK authenticates the customer.

#### Android

![Checkout screen](assets/stripe-3ds-android-confirm.png)

The customer enters their payment information.
![Initiate authentication](assets/stripe-3ds-android-processing.png)

The SDK presents a loading screen while the customer’s bank checks whether authentication is required.
![Challenge flow screen](assets/stripe-3ds-android-otp.png)

If required by their bank, the SDK authenticates the customer.

## Control the 3DS flow

Stripe triggers 3DS automatically if mandated by regulations such as [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md) in Europe, industry guidelines such as the Credit Card Security Guidelines in Japan, if requested by an issuer with a [soft decline](https://docs.stripe.com/declines/codes.md) code, or if certain Stripe optimizations apply.

You can also [use Radar](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar) or [the API](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#manual-three-ds) to decide when to prompt users for 3DS authentication. This allows you to customize the authentication process for each user based on your chosen parameters. However, not all transactions support 3DS, for example wallets or _off-session payments_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information).

When a payment triggers 3DS, the card issuer might require the customer to authenticate to complete the payment, as long as 3DS authentication is supported for that card. While Stripe initiates the authentication request, the requirement comes from the issuer. Depending on the front end you’re using, this might require you to [display the 3DS flow](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#when-to-use-3d-secure).

In a typical Payment Intent API flow that triggers 3DS:

1. The user enters their payment information, which confirms a PaymentIntent, SetupIntent, or attaches a PaymentMethod to a Customer.
1. Stripe assesses if the transaction supports and requires 3DS based on regulatory mandates, Radar rules, manual API requests, issuer soft declines, and other criteria.
1. If 3DS is:
   - **Not required**: For example, because of an _exemption_ (Some transactions that are deemed low risk, based on the volume of fraud rates associated with the payment provider or bank, may be exempt from Europe's Strong Customer Authentication requirements), Stripe attempts the charge. The PaymentIntent transitions to a status of `processing`. If requested by the issuer with a [soft decline](https://docs.stripe.com/declines/codes.md), we automatically reattempt and continue as if required.
   - **Not supported**: The PaymentIntent transitions to a status of `requires_payment_method`. Depending on the reason 3DS was triggered it might be permissible to continue to the authorization step for the charge. In that case, the PaymentIntent transitions to a status of `processing`.
   - **Required**: Stripe starts the 3DS authentication flow by contacting the card issuer’s 3DS Access Control Server (ACS) and starting the 3DS flow.
1. When 3DS flow information is received from the issuer, Stripe submits the request for the issuer to authenticate the cardholder. The PaymentIntent transitions to a status of `requires_action`:
   - See below for how to [display the required 3DS action](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#when-to-use-3d-secure). Issuers might request different 3DS flow action types, which might not always result in visibly displaying a 3DS challenge (for example, a frictionless flow).
   - If the issuer doesn’t support 3DS at all or has an outage, Stripe might attempt to complete the payment without authentication if permissible.
   - Data for 3DS authentication requests is typically provided by the customer at the time of the transaction. To reduce friction and the possibility of failed authentication, we might complete these requests with data we infer from other sources such as data collected from your customer during the payment flow, records related to your customer’s past transactions with you, or relevant information available from the customer’s card or issuers.
   - If Stripe already has access to all the required 3DS data elements, our optimized 3DS server might attempt to complete the authentication request for you while confirming the PaymentIntent. This can result in the PaymentIntent directly transitioning to a status of `processing` if the 3DS flow succeeds, or to a status of `requires_action` if additional steps or data elements are required to complete the 3DS flow.
1. Depending on the 3DS authentication result:
   - **Authenticated**: Stripe attempts the charge and the PaymentIntent transitions to a status of `processing`.
   - **Failure**: The PaymentIntent transitions to a status of `requires_payment_method`, indicating that you need to try a different payment method, or you can retry 3DS by reconfirming.
   - **Other scenarios**: Depending on the reason the payment triggered 3DS, it might be permissible to continue authorization for the charge in [edge cases](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure-result). For example, a result of `attempt_acknowledged` leads to a charge and the PaymentIntent transitions to a status of `processing`.
     - An exception is when creating [Indian e-mandates for recurring payments](https://docs.stripe.com/india-recurring-payments.md). Anything but an `authenticated` result is treated as failure.
1. The PaymentIntent transitions to one of the following statuses, depending on the outcome of the payment: `succeeded`, `requires_capture`, or `requires_payment_method`.

To track whether 3DS was supported and attempted on a card payment, read the [three_d_secure](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure) property on the card information in the Charge’s `payment_method_details`. Stripe populates the `three_d_secure` property when the customer attempts to authenticate the card—`three_d_secure.result` indicates the authentication outcome.

### Use Radar rules in the Dashboard

Stripe provides [fraud controls](https://docs.stripe.com/radar/rules.md#request-3d-secure) to dynamically request 3DS when creating or confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md). You can configure these rules in your [Dashboard](https://dashboard.stripe.com/settings/radar/rules).

If you have [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you can add [custom 3DS rules](https://docs.stripe.com/radar/rules.md#request-3d-secure).

### Manually request 3DS with the API

The default method to trigger 3DS is [using Radar to dynamically request 3D Secure](https://docs.stripe.com/radar/risk-settings.md#adaptive-3ds) based on risk level and other requirements. Triggering 3DS manually is for advanced users integrating Stripe with their own fraud engine.

To trigger 3DS manually, set `payment_method_options[card][request_three_d_secure]` depending on what you want to optimize for when either creating or confirming a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-request_three_d_secure) or [SetupIntent](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_options-card-request_three_d_secure), or creating a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_three_d_secure). This process is the same for one-time payments or when setting up a payment method for future payments. When you provide this parameter, Stripe attempts to perform 3DS and overrides any [dynamic 3D Secure Radar rules](https://docs.stripe.com/radar/rules.md) on the PaymentIntent, SetupIntent, or Checkout Session.

#### Payment Intents API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_options: {
    card: {
      request_three_d_secure: "any",
    },
  },
});
```

#### Setup Intents API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_options: {
    card: {
      request_three_d_secure: "any",
    },
  },
});
```

#### Checkout Session API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  payment_method_options: {
    card: {
      request_three_d_secure: "any",
    },
  },
});
```

When to provide this parameter depends on when your fraud engine detects risk. For example, if your fraud engine only inspects card details, you know whether to request 3DS before you create the PaymentIntent or SetupIntent. If your fraud engine inspects both card and transaction details, provide the parameter during confirmation—when you have more information. Then pass the resulting PaymentIntent or SetupIntent to your client to complete the process.

Explore the `request_three_d_secure` parameter’s usage for each case in the API reference:

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-request_three_d_secure)
- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a SetupIntent](https://docs.stripe.com/api/setup_intents/confirm.md#confirm_setup_intent-payment_method_options-card-request_three_d_secure)
- [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_three_d_secure)

Set `request_three_d_secure` to `any` to manually request 3DS with a preference for a `frictionless` flow, increasing the likelihood of the authentication being completed without any additional input from the customer.

Set `request_three_d_secure` to `challenge` to request 3DS with a preference for a `challenge` flow, where the customer must respond to a prompt for active authentication.

Stripe can’t guarantee your preference because the issuer determines the ultimate authentication flow. You can find out what the ultimate authentication flow was by inspecting the `authentication_flow` on the `three_d_secure` property of the [Charge](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure-authentication_flow) or [SetupAttempt](https://docs.stripe.com/api/setup_attempts/object.md#setup_attempt_object-payment_method_details-card-three_d_secure-authentication_flow). To learn more about 3DS flows, read our [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

> Stripe only prompts your customer to perform authentication if 3DS authentication is available for a card. If it’s not available for the given card or if an error occurred during the authentication process, the payment proceeds normally.

Stripe’s mandatory authentication rules run automatically, regardless of whether or not you manually request 3DS. Any 3DS requests from you’re additional to those required for SCA.

## Display the 3DS flow

#### Web

Stripe automatically displays the authentication UI in a pop-up modal when calling `confirmCardPayment` and `handleCardAction`. You can also redirect to the bank’s website or use an iframe.

Stripe.js collects [basic device information](https://support.stripe.com/questions/3d-secure-2-device-information) during 3DS2 authentication and sends it to the issuing bank for their risk analysis.

### Redirect to the bank website

To redirect your customer to the 3DS authentication page, pass a `return_url` to the PaymentIntent when confirming [on the server](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) or on the [client](https://docs.stripe.com/js/payment_intents/confirm_card_payment).

After confirmation, if a PaymentIntent has a _requires_action_ (This status appears as "requires_source_action" in API versions before 2019-02-11) status, inspect the PaymentIntent’s `next_action`. If it contains `redirect_to_url`, that means 3DS is required.

```js
next_action: {
    type: 'redirect_to_url',
    redirect_to_url: {
      url: 'https://hooks.stripe.com/...',
      return_url: 'https://mysite.com'
    }
}
```

In the browser, redirect the customer to the `url` in the redirect_to_url hash to complete authentication.

```javascript
var action = intent.next_action;
if (action && action.type === "redirect_to_url") {
  window.location = action.redirect_to_url.url;
}
```

When the customer finishes the authentication process, the redirect sends them back to the `return_url` you specified when you created or confirmed the PaymentIntent. The redirect also adds `payment_intent` and `payment_intent_client_secret` URL query parameters that your application can use to identify the PaymentIntent associated with the purchase.

### Display in an iframe

You can’t customize the authentication UI on the web to match your website’s design—the bank that issued the card controls the fonts and colors.

However, you can choose _how_ and _where_ to show the 3DS UI. Most businesses show it in a modal dialog above their payment page. If you have your own modal component, you can place the 3DS frame inside of it. You can also show the authentication content inline with your payment form.

#### Confirm the PaymentIntent

When your customer is ready to complete their purchase, you _confirm_ (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) the PaymentIntent to begin the process of collecting their payment.

If you want to control how to display 3DS, provide a `return_url`, which is where the 3DS `<iframe>` is redirected when authentication is complete. If your site uses a [content security policy](https://docs.stripe.com/security/guide.md#content-security-policy), check that it allows iframes from `https://js.stripe.com`, `https://hooks.stripe.com`, and the origin of the URL you passed to `return_url`.

If you’re confirming from the frontend, use the [confirmCardPayment](https://docs.stripe.com/js.md#stripe-confirm-card-payment) method in Stripe.js. For example, if you’re gathering card information using Stripe Elements:

```javascript
stripe
  .confirmCardPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: { card: cardElement },
      return_url: "https://example.com/return_url",
    },
    // Disable the default next action handling.
    { handleActions: false },
  )
  .then(function (result) {
    // Handle result.error or result.paymentIntent
    // More details in Step 2.
  });
```

If you confirm from your server, provide a `return_url`. Depending on your integration, you might want to pass other information to [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) as well.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.confirm(
  "{{PAYMENT_INTENT_ID}}",
  {
    return_url: "https://example.com/return_url",
  },
);
```

#### Check the PaymentIntent status (Server-side)

Next, inspect the [status property](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) property of the confirmed PaymentIntent to determine whether the payment completed successfully. The following list describes possible `status` values and their significance:

| Status                    | Description                                                                                                                                                                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requires_payment_method` | The request failed with a `402` HTTP status code, meaning that the payment was unsuccessful. Check the [last_payment_error](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error) property and try again, collecting new payment information from the customer if necessary. |
| `requires_capture`        | The request completed without authentication. You can continue to [capture the funds](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md#capture-funds).                                                                                                                                             |
| `requires_action`         | An additional step such as 3DS is required to complete the payment. Ask the customer to return to your application to complete payment.                                                                                                                                                                                |
| `succeeded`               | The payment completed, creating a Charge with the supplied payment method. No further steps are required.                                                                                                                                                                                                              |

On versions of the API before [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11), `requires_payment_method` appears as `requires_source` and `requires_action` appears as `requires_source_action`.

#### Render the 3DS iframe (Client-side)

When the value of the `status` property is `requires_action`, you need to complete an additional step before processing the payment. For a card payment that requires 3DS, the PaymentIntent’s `status` shows as `requires_action` and its [next_action](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action) property appears as `redirect_to_url`. The `redirect_to_url` payload contains a URL that opens in an iframe to display 3DS:

```javascript
var iframe = document.createElement("iframe");
iframe.src = paymentIntent.next_action.redirect_to_url.url;
iframe.width = 600;
iframe.height = 400;
yourContainer.appendChild(iframe);
```

For 3DS2, card issuers are required to support showing the 3DS content at sizes of 250x400, 390x400, 500x600, 600x400, and full screen (dimensions are width by height). You might enhance the 3DS UI by opening the iframe at exactly one of those sizes.

> You can’t use the `sandbox` attribute on the 3DS iframe. In live mode, the card issuer controls some content inside this iframe. Some issuers’ implementations fail if they’re sandboxed, and the payment won’t succeed.

#### Handle the redirect (Client-side)

After the customer completes 3DS, the iframe redirects to the `return_url` you provided when confirming the PaymentIntent. That page needs to `postMessage` to your top-level page to inform it that 3DS authentication is complete. Your top-level page then needs to determine whether the payment succeeded or requires further action from your customer.

For example, you might have your `return_url` page execute:

```javascript
window.top.postMessage("3DS-authentication-complete");
```

Your top payment page needs to listen for this postMessage to know when authentication has finished. You then need to retrieve the updated PaymentIntent and check on the status of the payment. If the authentication failed, the PaymentIntent’s status is `requires_payment_method`. If the payment completed successfully, the status is `succeeded`. If you use [separate authorize and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), the status is `requires_capture` instead.

```javascript
function on3DSComplete() {
  // Hide the 3DS UI
  yourContainer.remove();

  // Check the PaymentIntent
  stripe
    .retrievePaymentIntent("{{PAYMENT_INTENT_CLIENT_SECRET}}")
    .then(function (result) {
      if (result.error) {
        // PaymentIntent client secret was invalid
      } else {
        if (result.paymentIntent.status === "succeeded") {
          // Show your customer that the payment has succeeded
        } else if (result.paymentIntent.status === "requires_payment_method") {
          // Authentication failed, prompt the customer to enter another payment method
        }
      }
    });
}

window.addEventListener(
  "message",
  function (ev) {
    if (ev.data === "3DS-authentication-complete") {
      on3DSComplete();
    }
  },
  false,
);
```

#### iOS

> [PaymentSheet](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet) and [PaymentSheet.FlowController](https://stripe.dev/stripe-ios/stripepaymentsheet/documentation/stripepaymentsheet/paymentsheet/flowcontroller) automatically support 3DS authentication. If you’re using one of these classes, this guide doesn’t apply.

The [STPPaymentHandler](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stppaymenthandler) class presents UIViewControllers over your app for authentication. [STPPaymentHandler.threeDSCustomizationSettings](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpthreedscustomizationsettings) contains the customizable items for 3DS authentication.

The [authenticationTimeout](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpthreedscustomizationsettings/authenticationtimeout) property controls how long the 3DS authentication process runs before it times out. This duration includes both network round trips and awaiting customer input, and must be at least 5 minutes. If authentication times out, `STPPaymentHandler` reports an error with code `STPPaymentHandlerTimedOutErrorCode` in the completion block.

The [uiCustomization](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpthreedscustomizationsettings/uicustomization) property allows you to provide a [STPThreeDSUICustomization](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPThreeDSUICustomization.html) instance to control the look and feel of the authentication UI. For each customizable element of the UI, such as the navigation bar or the **Submit** button, there’s a corresponding class with properties to configure colors, fonts, text, borders, and so on. See the [STPThreeDSUICustomization documentation](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpthreedsuicustomization) for a detailed explanation of each parameter.

The Stripe iOS SDK collects [basic device information](https://support.stripe.com/questions/3d-secure-2-device-information) during 3DS2 authentication and sends it to the issuing bank for their risk analysis.
![UI Customization](assets/stripe-3ds-ios-customization.png)

The following example code demonstrates some of the configuration for a dark UI color theme.

#### Swift

```swift
      let uiCustomization = STPPaymentHandler.shared().threeDSCustomizationSettings.uiCustomization
      uiCustomization.textFieldCustomization.keyboardAppearance = .dark
      uiCustomization.navigationBarCustomization.barStyle = .black
      uiCustomization.navigationBarCustomization.textColor = .white
      uiCustomization.buttonCustomization(for: .cancel).textColor = .white
```

You have four different types of challenge screens that you can present to your customer. [Test your UI customization](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-cards) with these different screens with your customization.

You can also configure which view controller presents the authentication UI and other behavior using the [STPAuthenticationContext](https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stpauthenticationcontext) passed to `STPPaymentHandler`.

### Set up a return URL

The iOS SDK can present a webview in your app to authenticate your customer instead of a native view (for example, if your customer is using an outdated app version). When authentication finishes, the webview can automatically dismiss itself instead of having your customer close it. To enable this behavior, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) or [universal link](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content) and set up your app delegate to forward the URL to the SDK.

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}

// This method handles opening universal link URLs (for example, "https://example.com/stripe_ios_callback")
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
        if let url = userActivity.webpageURL {
            let stripeHandled = StripeAPI.handleURLCallback(with: url)
            if (stripeHandled) {
                return true
            } else {
                // This was not a Stripe url – handle the URL normally as you would
            }
        }
    }
    return false
}
```

Next, pass the URL as the `return_url` when you [confirm the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) (if you’re collecting a payment) or [SetupIntent](https://docs.stripe.com/api/setup_intents/confirm.md#confirm_setup_intent-return_url) (if you’re saving card details). After webview-based authentication finishes, Stripe redirects the user back to your app or web page with the `return_url` you provided.

#### Android

> [PaymentSheet](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html) and [PaymentSheet.FlowController](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html) automatically support 3DS authentication. If you’re using one of these classes, this guide doesn’t apply.

[PaymentAuthConfig.Stripe3ds2Config](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/index.html) contains the customizable items for 3DS authentication interactions.

The [timeout property](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-timeout.html) controls how long the 3DS authentication process runs before it times out. This duration includes both network round trips and awaiting customer input. This value must be at least 5 minutes to remain compliant with Strong _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) Authentication regulation. A value less than 5 minutes results in an error.

The [uiCustomization](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-ui-customization.html) property allows you to provide a `StripeUiCustomization` instance to control the look of views presented by the Android SDK during 3DS authentication. Stripe currently supports customization parameters for colors, fonts, text, borders on app bars, labels, text fields, and buttons. For a full explanation of each parameter, see the [Android SDK](https://stripe.dev/stripe-android/) reference.

The Stripe Android SDK collects [basic device information](https://support.stripe.com/questions/3d-secure-2-device-information) during 3DS2 authentication and sends it to the issuing bank for their risk analysis.

#### Java

```java
  final PaymentAuthConfig.Stripe3ds2UiCustomization uiCustomization =
          new PaymentAuthConfig.Stripe3ds2UiCustomization.Builder()
                  .setLabelCustomization(
                          new PaymentAuthConfig.Stripe3ds2LabelCustomization.Builder()
                                  .setTextFontSize(12)
                                  .build())
                  .build();
  PaymentAuthConfig.init(new PaymentAuthConfig.Builder()
          .set3ds2Config(new PaymentAuthConfig.Stripe3ds2Config.Builder()
                  .setTimeout(5)
                  .setUiCustomization(uiCustomization)
                  .build())
          .build());
```

#### React Native

> You don’t need to follow this guide if you’re using [PaymentSheet](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html) because it automatically supports 3DS authentication.

The `threeDSecureParams` property in `StripeProvider` contains the customizable items for 3DS authentication.

To automatically dismiss the webview when authentication completes, [configure a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) or [universal link](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content) and set your scheme in the `urlScheme` parameter.

You can use `timeout` to specify how much time the 3DS authentication process can elapse before timing out. This duration includes both network round trips and awaiting customer input, and must be at least 5 minutes.

Other properties allow you to control the look and feel of the authentication UI. For complete details, see the [React Native SDK reference](https://stripe.dev/stripe-react-native/api-reference/index.html).

Below is a customization example:

```javascript
function PaymentScreen() {
  return (
    <StripeProvider
      publishableKey="<<YOUR_PUBLISHABLE_KEY>>"
      urlScheme="your-url-scheme"
      threeDSecureParams={{
        backgroundColor: "#FFFFFF", // iOS only
        timeout: 5,
        label: {
          headingTextColor: "#0000",
          headingFontSize: 13,
        },
        navigationBar: {
          headerText: "3d secure",
        },
        footer: {
          // iOS only
          backgroundColor: "#FFFFFF",
        },
        submitButton: {
          backgroundColor: "#000000",
          cornerRadius: 12,
          textColor: "#FFFFFF",
          textFontSize: 14,
        },
      }}
    >
      // ....
    </StripeProvider>
  );
}
```

## Test the 3DS flow

Use a Stripe test card with any CVC, postal code, and future expiration date to trigger 3DS authentication challenge flows while in a sandbox.

When you build an integration with your test API keys, the authentication process displays a mock authentication page. On that page, you can either authorize or cancel the payment. Authorizing the payment simulates successful authentication and redirects you to the specified return URL. Clicking the **Failure** button simulates an unsuccessful attempt at authentication.

#### Web

#### Card numbers

| Number           | 3DS usage     | Description                                                                                                                                                                                                                                  |
| ---------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4000000000003220 | Required      | The payment must always complete 3DS2 authentication to be successful. By default, your Radar rules request 3DS authentication for this card.                                                                                                |
| 4000002500003155 | Required      | This card requires 3DS2 authentication for off-session payments unless you [set it up](https://docs.stripe.com/payments/save-and-reuse.md) for future payments. After you set it up, off-session payments no longer require authentication.  |
| 4000008400001629 | Required      | 3DS authentication is required, but payments will be declined with a `card_declined` failure code after authentication. By default, your Radar rules request 3DS authentication for this card.                                               |
| 4000000000003055 | Supported     | 3DS authentication can still be performed, but isn’t required. By default, your Radar rules won’t request 3DS authentication for this card.                                                                                                  |
| 4242424242424242 | Supported     | This card supports 3DS, but it isn’t enrolled in 3DS. This means that if your Radar rules request 3DS, the customer won’t go through additional authentication. By default, your Radar rules won’t request 3DS authentication for this card. |
| 378282246310005  | Not supported | This card doesn’t support 3DS and you can’t invoke it. The PaymentIntent proceeds without performing authentication.                                                                                                                         |

#### PaymentMethods

| Payment Method                               | 3DS usage     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pm_card_threeDSecure2Required`              | Required      | The payment must complete 3DS2 authentication for the payment to be successful. By default, your Radar rules request 3DS authentication for this card.                                                                                       |
| `pm_card_threeDSecureRequiredChargeDeclined` | Required      | 3D Secure authentication is required, but payments will be declined with a `card_declined` failure code after authentication. By default, your Radar rules request 3DS authentication for this card.                                         |
| `pm_card_threeDSecureOptional`               | Supported     | 3DS authentication can still be performed, but isn’t required. By default, your Radar rules won’t request 3DS authentication for this card.                                                                                                  |
| `pm_card_visa`                               | Supported     | This card supports 3DS, but it isn’t enrolled in 3DS. This means that if your Radar rules request 3DS, the customer won’t go through additional authentication. By default, your Radar rules won’t request 3DS authentication for this card. |
| `pm_card_amex_threeDSecureNotSupported`      | Not supported | This card doesn’t support 3DS and you can’t invoke it. The PaymentIntent proceeds without performing authentication.                                                                                                                         |

#### iOS

When testing your custom iOS integration, pick a test card to trigger a specific challenge flow.

| Number           | Challenge flow    | Description                                                                                                              |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 4000582600000094 | Out of Band       | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with Out of Band UI.       |
| 4000582600000045 | One Time Passcode | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with One Time Passcode UI. |
| 4000582600000102 | Single Select     | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with single-select UI.     |
| 4000582600000110 | Multi Select      | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with multi-select UI.      |

#### Android

When testing your custom Android integration, pick a test card to trigger a specific challenge flow.

| Number           | Challenge flow    | Description                                                                                                              |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 4000582600000094 | Out of Band       | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with Out of Band UI.       |
| 4000582600000045 | One Time Passcode | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with One Time Passcode UI. |
| 4000582600000102 | Single Select     | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with single-select UI.     |
| 4000582600000110 | Multi Select      | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with multi-select UI.      |

#### React Native

When testing your custom React Native integration, pick a test card to trigger a specific challenge flow.

| Number           | Challenge flow    | Description                                                                                                              |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 4000582600000094 | Out of Band       | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with Out of Band UI.       |
| 4000582600000045 | One Time Passcode | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with One Time Passcode UI. |
| 4000582600000102 | Single Select     | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with single-select UI.     |
| 4000582600000110 | Multi Select      | 3D Secure 2 authentication must be completed on all transactions. Triggers the challenge flow with multi-select UI.      |

All other Visa and Mastercard [test cards](https://docs.stripe.com/testing.md) don’t require authentication from the customer’s card issuer.

You can write [custom Radar rules in a test environment](https://dashboard.stripe.com/settings/radar/rules) to trigger authentication on test cards. Learn more about [testing your Radar rules](https://docs.stripe.com/radar/testing.md).

## Disputes and liability shift

The _liability shift_ (With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer) rule typically applies to payments successfully authenticated using 3DS. In some cases, liability shift applies with equivalent cryptograms, such as [Apple Pay](https://docs.stripe.com/apple-pay.md) or [Google Pay](https://docs.stripe.com/google-pay.md). If a cardholder [disputes](https://docs.stripe.com/disputes.md) a 3DS payment as fraudulent, the liability typically shifts from you to the card issuer.

If a card doesn’t support 3DS or an error occurs during the authentication process, the payment proceeds normally. When this occurs, liability doesn’t generally shift to the issuer, because a successful 3DS authentication hasn’t taken place.

In practice, this means you typically won’t receive disputes marked as fraudulent if the payment is covered by the liability shift rule, but you might still receive an [Early Fraud Warning](https://docs.stripe.com/disputes/how-disputes-work.md#early-fraud-warnings). You might still receive a low percentage of fraudulent disputes, and we list a few cases below where the liability shift rule might not apply.

You might receive a [dispute inquiry](https://docs.stripe.com/disputes/how-disputes-work.md#inquiries) on a successfully authenticated payment using 3DS. This type of dispute doesn’t precipitate a chargeback because it’s only a request for information.

If you receive an inquiry for a 3D-Secure-authenticated charge, you _must_ respond. If you don’t, the cardholder’s bank can initiate a financial chargeback known as a “no-reply” chargeback that could invalidate the liability shift. To prevent no-reply chargebacks on 3DS charges, submit sufficient information about the charge. Include information about what was ordered, how it was delivered, and who it was delivered to (whether it was physical or electronic goods, or services).

> If a customer disputes a payment for any other reason (for example, [product not received](https://docs.stripe.com/disputes/categories.md)), then the standard dispute process applies. Make informed decisions about your business management, especially in handling and completely avoiding disputes.

Liability shift might also occur when the card network requires 3DS, but it isn’t available for the card or issuer. This can happen if the issuer’s 3DS provider is down or if the issuer doesn’t support it, despite the card network requiring support. During the payment process, the cardholder isn’t prompted to complete 3DS authentication, because the card isn’t enrolled. Although the cardholder didn’t complete 3DS authentication, liability can still shift to the issuer.

Stripe returns the requested _Electronic Commerce Indicator_ (An Electronic Commerce Indicator (ECI) is a code returned alongside a 3D Secure authentication result. It indicates the authentication method and result and may be used subsequently to, for example, determine eligibility for liability shift) (ECI) in the `electronic_commerce_indicator` of the [3DS authentication outcome](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure). This indicator can aid in determining whether a charge should adhere to the liability shift rule. As 3DS occurs subsequent to the initial payment intent response, you typically get this from a `charge.succeeded` event that’s sent to one of your configured [webhook endpoints or other event destinations](https://docs.stripe.com/event-destinations.md). A requested ECI might be degraded in the issuer response, which we don’t reveal.

> Sometimes payments that are successfully authenticated using 3DS don’t fall under liability shift. This is rare and can happen, for example, if you have an excessive level of fraud on your account and are enrolled in a [fraud monitoring program](https://docs.stripe.com/disputes/monitoring-programs.md#visa-programs). Certain networks have also exempted some industries from liability shift. For example, Visa doesn’t support liability shift for businesses engaging in wire transfer or money orders, non-financial institutions offering foreign or non-fiat currency, or stored-value card purchase or load.

It’s also possible for liability shift to get downgraded post-authorization, or the card network’s dispute rejection system might fail to catch liability shift for a transaction. In these cases, if you counter the dispute, Stripe automatically adds the requested ECI and the [3DS authentication outcome](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-three_d_secure-result) of the payment to your evidence details, but we recommend you also include additional details to increase your chance of winning the dispute.

### Custom Radar rules for 3DS and liability shift

If you have [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you can [customize your rules](https://docs.stripe.com/radar/rules.md#request-3d-secure) to control when to request 3DS and how to handle each specific authentication outcome and liability shift. The Stripe [Strong Customer Authentication](https://stripe.com/guides/strong-customer-authentication) (SCA) rules run automatically and independently of custom Radar rules, and block unauthenticated payments unless exempted.

## See also

- [Import 3DS results](https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md)
- [Authentication analytics](https://docs.stripe.com/payments/analytics/authentication.md)
