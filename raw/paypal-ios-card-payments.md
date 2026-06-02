<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/ios/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Integrate card payments in iOS apps

# Integrate card payments in iOS apps

In certain countries, Apple allows apps to link to an external website for processing payments.

Sample integration repo: https://github.com/paypal-examples/paypal-ios-sdk-demo-app

Accept PayPal, credit, and debit card payments using the PayPal Mobile iOS SDK. For more implementation details, see the PayPal GitHub repository: https://github.com/paypal/paypal-ios/

## Know before you code

You need a combination of PayPal and third-party tools:
- iOS SDK (https://github.com/paypal/paypal-ios/): Adds PayPal-supported payment methods for iOS.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

## Before you begin

### Check your account setup for advanced card payments

Requires a sandbox business account with the **Advanced Credit and Debit Card Payments** capability.

To confirm:
1. Log into PayPal Developer Dashboard, toggle Sandbox, go to Apps & Credentials.
2. In REST API apps, select your app.
3. Go to Features > Accept payments.
4. Select the Advanced Credit and Debit Card Payments checkbox and save.

### Check 3D Secure requirements

Visit the 3D Secure page to see if required in your region.

## Integrate the SDK into your app

Two payment types:
- **Card payments**: Add card fields that align with your branding.
- **PayPal web payments**: Browser-based checkout within your app.

---

## Card Payments

### 1. Add card payments module

**Swift Package Manager:**
- Xcode → add package dependency
- URL: `https://github.com/paypal/paypal-ios/`
- Select `CardPayments` framework

**CocoaPods:**
```ruby
# Podfile
pod 'PayPal/CardPayments'
```

### 2. Create CardClient

```swift
let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let cardClient = CardClient(config: coreConfig)
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
{ "id": "ORDER_ID", "status": "CREATED" }
```

### 4. Create card request

#### 1. Collect card payment details

```swift
let card = Card(
  number: "4005519200000004",
  expirationMonth: "01",
  expirationYear: "2025",
  securityCode: "123",
  cardholderName: "Jane Smith",
  billingAddress: Address(
    addressLine1: "123 Main St.",
    addressLine2: "Apt. 1A",
    locality: "City",
    region: "IL",
    postalCode: "12345",
    countryCode: "US"
  )
)
```

Collecting a billing address can reduce the number of authentication challenges to customers.

#### 2. Build CardRequest

```swift
let cardRequest = CardRequest(
  orderID: "ORDER_ID",
  card: card,
  sca: .scaAlways  // default value is .scaWhenRequired
)
```

SCA options:
- `.scaWhenRequired` — launches SCA challenge when applicable (default)
- `.scaAlways` — requires SCA challenge for all card transactions

### 5. Approve order

```swift
class MyViewController: UIViewController {
  func cardCheckoutTapped(cardRequest: CardRequest) {
    cardClient.approveOrder(request: cardRequest)
  }
}
```

### 6. Handle payment result scenarios (CardDelegate)

```swift
extension MyViewController: CardDelegate {
  func setupCardClient() {
    cardClient.delegate = self
  }
  // MARK: - CardDelegate
  func card(_ cardClient: CardClient, didFinishWithResult result: CardResult) {
    // Order was approved and is ready to be captured/authorized
  }
  func card(_ cardClient: CardClient, didFinishWithError error: CoreSDKError) {
    // handle the error by accessing `error.localizedDescription`
  }
  func cardDidCancel(_ cardClient: CardClient) {
    // 3D Secure auth was canceled by the user
  }
  func cardThreeDSecureWillLaunch(_ cardClient: CardClient) {
    // 3D Secure auth will launch
  }
  func cardThreeDSecureDidFinish(_ cardClient: CardClient) {
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

Use test card numbers, rejection triggers, and 3D Secure test scenarios from the Card Testing page.

---

## PayPal Web Payments

### 1. Add PayPalWebPayments module

**Swift Package Manager:** Select `PayPalWebPayments` framework from `https://github.com/paypal/paypal-ios/`

**CocoaPods:**
```ruby
# Podfile
pod 'PayPal/PayPalWebPayments'
```

### 2. Create PayPalWebCheckoutClient

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let payPalClient = PayPalWebCheckoutClient(config: config)
```

### 3-4. Get Order ID and create request

```swift
let payPalWebRequest = PayPalWebCheckoutRequest(
  orderID: "ORDER_ID",
  fundingSource: .paypal  // .paypal (default), .payLater, .payPalCredit
)
```

### 5. Approve order (PayPalWebCheckoutDelegate)

```swift
extension MyViewController: PayPalWebCheckoutDelegate {
  func checkoutWithPayPal(payPalWebRequest: PayPalWebCheckoutRequest) {
    payPalWebCheckoutClient.delegate = self
    payPalWebCheckoutClient.start(request: payPalWebRequest)
  }
  // MARK: - PayPalWebCheckoutDelegate
  func payPal(_ payPalClient: PayPalWebCheckoutClient, didFinishWithResult result: PayPalWebCheckoutResult) {
    // order was approved and is ready to be captured/authorized
  }
  func payPal(_ payPalClient: PayPalWebCheckoutClient, didFinishWithError error: CoreSDKError) {
    // handle the error by accessing `error.localizedDescription`
  }
  func payPalDidCancel(_ payPalClient: PayPalWebCheckoutClient) {
    // the user canceled
  }
}
```

---

## Payment Buttons

**Swift Package Manager:** Select `PaymentButtons` framework

**CocoaPods:**
```ruby
pod 'PayPal/PaymentButtons'
```

Three button types: `PayPalButton`, `PayPalPayLater`, `PayPalCredit`

Button corner radius options: `rectangle`, `rounded` (default), `pill`, `custom(CGFloat)` (min 10px)

**UIKit:**
```swift
class MyViewController: UIViewController {
  lazy var payPalButton: PayPalButton = {
    let payPalButton = PayPalButton()
    payPalButton.addTarget(self, action: #selector(payPalButtonTapped), for: .touchUpInside)
    return payPalButton
  }()
  @objc func payPalButtonTapped() {
    // Insert your code here
  }
  override func viewDidLoad() {
    super.viewDidLoad()
    view.addSubview(payPalButton)
  }
}
```

**SwiftUI:**
```swift
struct MyApp: View {
  @ViewBuilder
  var body: some View {
    VStack {
      PayPalButton.Representable() {
        // Insert your code here
      }
    }
  }
}
```

---

## Fraud Protection

**Swift Package Manager:** Select `FraudProtection` framework

**CocoaPods:**
```ruby
pod 'PayPal/FraudProtection'
```

```swift
let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let dataCollector = PayPalDataCollector(config: coreConfig)

// Collect before starting payment — do not cache or store
let clientMetadataId = dataCollector.collectDeviceData()
// Pass clientMetadataId to your server
```

---

## Go live

- Log into PayPal Developer Dashboard with your PayPal business account.
- Complete production onboarding.
- Request Advanced Credit and Debit Card Payments for your business account.

Note: The integration checks eligibility requirements, so card fields only display when the production request is successful.
