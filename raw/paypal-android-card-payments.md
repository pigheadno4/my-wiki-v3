<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/android/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Integrate card payments in Android

# Integrate card payments in Android

Accept PayPal, credit, and debit card payments in a web or native experience using the PayPal Mobile Android SDK. For more implementation details, see the PayPal GitHub repository: https://github.com/paypal/paypal-android/

## Know before you code

You need a combination of PayPal and third-party tools:
- Android SDK (https://github.com/paypal/paypal-android): Adds PayPal-supported payment methods for Android.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

## Before you begin your integration

### Check your account setup for advanced card payments

This integration requires a sandbox business account with the **Advanced Credit and Debit Card Payments** capability.

To confirm:
1. Log into the PayPal Developer Dashboard, toggle Sandbox, go to Apps & Credentials.
2. In REST API apps, select your app.
3. Go to Features > Accept payments.
4. Select the Advanced Credit and Debit Card Payments checkbox and save.

### Check 3D Secure requirements

Add 3D Secure to reduce fraud. Visit the 3D Secure page to see if required in your region.

### SDK setup via Maven Central

```gradle
allprojects {
  repositories {
    mavenCentral()
  }
}
```

### Snapshot builds

```gradle
// Add snapshots repository
allprojects {
  repositories {
    mavenCentral()
    maven {
      url 'https://oss.sonatype.org/content/repositories/snapshots/'
    }
  }
}

// Add snapshot dependency
dependencies {
  implementation 'com.paypal.android:card-payments:CURRENT-VERSION-SNAPSHOT'
}
```

---

## Payment integrations

Three payment types available via the PayPal Mobile SDK:
- **Card payments**: Add card fields that align with your branding.
- **PayPal native payments**: Launch a checkout page within your app (DEPRECATED since July 2024).
- **PayPal web payments**: Lighter integration that launches checkout in a browser within your app.

---

## Card Payments

### 1. Add card payments module

```gradle
dependencies {
  implementation "com.paypal.android:card-payments:CURRENT-VERSION"
}
```

### 2. Create CardClient

```kotlin
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val cardClient = CardClient(config)
```

### 3. Get Order ID (server-side)

```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{
    "intent": "CAPTURE|AUTHORIZE",
    "purchase_units": [
      {
        "amount": {
          "currency_code": "USD",
          "value": "5.00"
        }
      }
    ]
  }'
```

Response:
```json
{
  "id": "ORDER_ID",
  "status": "CREATED"
}
```

### 4. Create card request

#### 1. Collect card payment details

```kotlin
val card = Card(
  number = "4005519200000004",
  expirationMonth = "01",
  expirationYear = "2025",
  securityCode = "123",
  billingAddress = Address(
    streetAddress = "123 Main St.",
    extendedAddress = "Apt. 1A",
    locality = "Anytown",
    region = "CA",
    postalCode = "12345",
    countryCode = "US"
  )
)
```

Collecting a billing address can reduce the number of authentication challenges to customers.

#### 2. Build CardRequest

```kotlin
val cardRequest = CardRequest(
  orderID = "ORDER_ID",
  card = card,
  returnUrl = "myapp://return_url", // custom URL scheme needs to be configured in AndroidManifest.xml
  sca = SCA.SCA_ALWAYS // default value is SCA.SCA_WHEN_REQUIRED
)
```

SCA options:
- `SCA.SCA_WHEN_REQUIRED` — launches SCA challenge when applicable (default)
- `SCA.SCA_ALWAYS` — requires SCA challenge for all card transactions

#### 3-6. App setup for browser switching

Provide a `returnUrl` with format `myapp://return_url`. Register the `myapp://` custom URL scheme in `AndroidManifest.xml`:

```xml
<activity
  android:name=".MyCardPaymentActivity"
  android:launchMode="singleTop"
  android:exported="true">
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="myapp" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
  </intent-filter>
</activity>
```

Add `onNewIntent` to your activity:

```kotlin
override fun onNewIntent(newIntent: Intent?) {
  super.onNewIntent(intent)
  intent = newIntent
}
```

### 5. Approve order

```kotlin
class MyCardPaymentActivity: FragmentActivity {
  fun cardCheckoutTapped(cardRequest: CardRequest) {
    cardClient.approveOrder(this, cardRequest)
  }
}
```

### 6. Handle payment result scenarios

```kotlin
class MyCardPaymentActivity: FragmentActivity, ApproveOrderListener {
  fun setupCardClient() {
    cardClient.listener = this
  }
  fun onApproveOrderSuccess(result: CardResult) {
    // order was approved and is ready to be captured/authorized
  }
  fun onApproveOrderFailure(error: PayPalSDKError) {
    // inspect 'error' for more information
  }
  fun onApproveOrderCanceled() {
    // 3D Secure flow was canceled
  }
  fun onApproveOrderThreeDSecureWillLaunch() {
    // 3D Secure flow will launch
  }
  fun onApproveOrderThreeDSecureDidFinish() {
    // 3D Secure auth did finish successfully
  }
}
```

### 7. Authorize and capture order

Authorize:
```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/authorize' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw ''
```

Capture:
```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/capture' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw ''
```

### 8. Test integration

Use test card numbers, rejection triggers, and 3D Secure test scenarios from the Card Testing page. Use the credit card generator for additional test cards.

---

## Native Payments (DEPRECATED)

> **Deprecation notice:** `PayPalNativePayments` module is deprecated since July 2024. Updates and bug fixes end in July 2025. Use `PayPalWebPayments` instead.

### Screenshots (for reference)

**First-time customer:**
![Native checkout first-time flow screen 1](assets/paypal-android-native-checkout-first-time-01.png)
![Native checkout first-time flow screen 2](assets/paypal-android-native-checkout-first-time-02.png)

**Returning customer:**
![Native checkout returning customer flow](assets/paypal-android-native-checkout-returning.png)

### 1. Add PayPalNativePayments module

```gradle
dependencies {
  implementation "com.paypal.android:paypal-native-payments:CURRENT-VERSION"
}
```

Also requires Cardinal Commerce Maven repository:
```gradle
allprojects {
  repositories {
    maven {
      url "https://cardinalcommerceprod.jfrog.io/artifactory/android"
      credentials {
        username "paypal_sgerritz"
        password "AKCp8jQ8tAahqpT5JjZ4FRP2mW7GMoFZ674kGqHmupTesKeAY2G8NcmPKLuTxTGkKjDLRzDUQ"
      }
    }
  }
}
```

### 2-5. Setup (abbreviated — deprecated, migrate to WebPayments)

```kotlin
val coreConfig = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val payPalNativeClient = PayPalNativeCheckoutClient(
  application = requireActivity().application,
  coreConfig = coreConfig,
  returnUrl = "RETURN_URL"
)

payPalNativeClient.listener = object : PayPalNativeCheckoutListener {
  override fun onPayPalCheckoutStart() { }
  override fun onPayPalCheckoutSuccess(result: PayPalNativeCheckoutResult) {
    // ready to capture/authorize
  }
  override fun onPayPalCheckoutFailure(error: PayPalSDKError) { }
  override fun onPayPalCheckoutCanceled() { }
}

// Shipping listener (only when shipping_preference = GET_FROM_FILE)
payPalNativeClient.shippingListener = object : PayPalNativeShippingListener {
  override fun onPayPalNativeShippingAddressChange(
    actions: PayPalNativePaysheetActions,
    shippingAddress: PayPalNativeShippingAddress
  ) {
    actions.approve() // or actions.reject()
  }
  override fun onPayPalNativeShippingMethodChange(
    actions: PayPalNativePaysheetActions,
    shippingMethod: PayPalNativeShippingMethod
  ) {
    try {
      // patch order on server, then:
      actions.approve()
    } catch (e: Exception) {
      actions.reject()
    }
  }
}

// Start checkout
val request = PayPalNativeCheckoutRequest("ORDER_ID")
paypalNativeClient.startCheckout(request)
```

---

## Web Payments (RECOMMENDED)

### 1. Add PayPalWebPayments module

```gradle
dependencies {
  implementation "com.paypal.android:paypal-web-payments:CURRENT-VERSION"
}
```

### 2. Set up app for browser switching

Update `AndroidManifest.xml`:

```xml
<activity android:name="com.company.app.MyPaymentsActivity"
          android:exported="true"
          android:launchMode="singleTop">
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="custom-url-scheme" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
  </intent-filter>
</activity>
```

Add `onNewIntent`:
```kotlin
override fun onNewIntent(newIntent: Intent?) {
  super.onNewIntent(intent)
  intent = newIntent
}
```

### 3. Create PayPalWebCheckoutClient

```kotlin
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val returnUrl = "custom-url-scheme"
val payPalWebCheckoutClient = PayPalWebCheckoutClient(requireActivity(), config, returnUrl)

payPalWebCheckoutClient.listener = object : PayPalWebCheckoutListener {
  override fun onPayPalWebSuccess(result: PayPalWebCheckoutResult) {
    // ready to capture/authorize
  }
  override fun onPayPalWebFailure(error: PayPalSDKError) { }
  override fun onPayPalWebCanceled() { }
}
```

### 4-6. Create request and start checkout

```kotlin
val payPalWebCheckoutRequest = PayPalWebCheckoutRequest(
  "ORDER_ID",
  fundingSource = PayPalWebCheckoutFundingSource.PAYPAL // PAYPAL, PAY_LATER, or PAYPAL_CREDIT
)
payPalWebCheckoutClient.start(payPalWebCheckoutRequest)
```

---

## Payment Buttons

### Add PaymentButtons module

```gradle
dependencies {
  implementation "com.paypal.android:payment-buttons:CURRENT-VERSION"
}
```

Three button types: `PayPalButton`, `PayPalPayLater`, `PayPalCredit`

Button corner radius options: `rectangle`, `rounded` (default), `pill`, `customCornerRadius` (min 10px)

```xml
<com.paypal.android.paymentbuttons.PayPalButton
    android:id="@+id/paypal_button"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```kotlin
val payPalButton = findViewById<PayPalButton>(R.id.paypal_button)
payPalButton.setOnClickListener {
  // start the PayPal web or native payment
}
```

---

## Fraud Protection

### Add FraudProtection module

```gradle
dependencies {
  implementation "com.paypal.android:fraud-protection:CURRENT-VERSION"
}
```

```kotlin
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val dataCollector = PayPalDataCollector(coreConfig = coreConfig)

// Collect before starting payment — do not cache or store
val dataCollectorRequest = PayPalDataCollectorRequest(hasUserLocationConsent)
val clientMetadataId = payPalDataCollector.collectDeviceData(context, dataCollectorRequest)
// Pass clientMetadataId to your server for inclusion in the payment request
```

`hasUserLocationConsent` — set `true` only if user has granted location consent per Google Play policies.

---

## Go live

- Log into PayPal Developer Dashboard with your PayPal business account.
- Complete production onboarding.
- Request Advanced Credit and Debit Card Payments for your business account.

Note: The integration checks eligibility requirements, so card fields only display when the production request is successful.
