<!-- Source URL: https://docs.stripe.com/billing/subscriptions/manage-subscriptions-ios -->
<!-- Fetched: 2026-05-13 -->

# Manage subscriptions on iOS

Accept recurring payments and manage entitlements with the BillingSDK for iOS.

Accept subscription payments, let customers manage their subscriptions, and manage [Entitlements](https://docs.stripe.com/billing/entitlements.md) directly in your iOS app with the [BillingSDK for iOS](https://github.com/stripe-samples/billing-ios-sdk). The SDK provides prebuilt UI components to display buy buttons, present the [customer portal](https://docs.stripe.com/customer-management/activate-no-code-customer-portal.md), and check entitlements to gate premium features.

## Before you begin

To use the BillingSDK for iOS, you’ll need:

- A backend server to create [Customer Sessions](https://docs.stripe.com/api/customer_sessions.md)
- A Stripe account with access to the private preview
- iOS 15.0 or later and macOS 12.0 or later
- Xcode 15.0 or later

## What you’ll build

This guide shows you how to:

- Set up a server endpoint to create [Customer Sessions](https://docs.stripe.com/api/customer_sessions.md)
- Install and configure the BillingSDK for iOS
- Display buy buttons for subscription purchases
- Check entitlements to gate premium features
- Present the customer portal for subscription management
- Handle errors and manage session state

You can find a complete example app in the [BillingSDK for iOS repository](https://github.com/stripe-samples/billing-ios-sdk).

## Set up your backend [Server]

Create a server endpoint that [generates Customer Sessions](https://docs.stripe.com/api/customer_sessions/create.md) for authenticated users. These sessions securely authenticate your iOS app with Stripe’s billing APIs.

### Create a customer session endpoint

The endpoint needs to:

1. Verify that the user is authenticated
1. Create or retrieve the Stripe [Customer ID](https://docs.stripe.com/api/customers/object.md) for the user
1. Create a Customer Session with the required components enabled
1. Return the session details to your app

Here’s an example implementation:

```javascript
import 'dotenv/config';
import express from 'express';
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || '', {
  apiVersion: '2025-07-30.basil',
});

const app = express();
app.use(express.json());

app.post('/authenticate', async (req, res) => {
  try {
    // Replace with your auth; return 401 if the user is not logged in
    const user = authUser(req);
    if (!user) {
      res.status(401).json({ error: { type: 'no_session_present' } });
      return;
    }

    const customerSession = await stripe.customerSessions.create({
      customer: user.stripeCustomerId,
      components: {
        buy_button: { enabled: true },
        active_entitlements: { enabled: true },
        customer_portal: { enabled: true },
      } as any,
    });

    res.json({
      clientSecret: customerSession.client_secret,
      expiresAt: customerSession.expires_at,
      customer: customerSession.customer as string,
    });
  } catch (err) {
    res.status(500).json({ error: { message: 'Internal server error' } });
  }
});

app.listen(3000);
```

### Response format

The endpoint must return these fields for successful authentication:

| Field          | Type   | Description                                              |
| -------------- | ------ | -------------------------------------------------------- |
| `clientSecret` | string | The Customer Session secret used to authenticate the SDK |
| `expiresAt`    | number | Expiration timestamp in seconds since epoch              |
| `customer`     | string | The Stripe Customer ID                                   |

When authentication fails, return HTTP 401 to trigger the SDK’s unauthenticated state.

## Install and configure the SDK [iOS]

The BillingSDK for iOS provides a native iOS experience for subscription management and feature access control.

### Add the SDK to your project

During private preview, install the BillingSDK package:

1. Open your project in Xcode
1. Select **File** → **Add Package Dependencies**
1. Type `https://github.com/stripe-samples/billing-ios-sdk` into the **Search or Enter Package URL** field
1. Select `BillingSDK` and click **Add Package**

### Configure the SDK

Initialize the SDK in a shared class to handle the BillingSDK setup and authentication:

```swift
import Foundation
import BillingSDK
import SwiftUI

class BillingManager {
    static let shared = BillingManager()

    public let billing: BillingSDK

    private init() {
        // Initialize with your publishable key and set how long entitlements can be stale before needing to refresh.
        let configuration = BillingSDK.Configuration(
          publishableKey: "pk_test_…",
          maximumStaleEntitlementsDuration: TimeInterval(60 * 5)
        )
        self.billing = BillingSDK(configuration: configuration)

        // Set up authentication (see below for implementation)
        setupCustomerSessionProvider()

        // Add entitlement change listener (see below for implementation)
        setupEntitlementListener()
    }
}
```

> The SDK handles thread safety internally—you can safely call its methods from any thread.

### Set up the Customer Session provider

Add the authentication method to your billing manager:

```swift
import Foundation
import BillingSDK

extension BillingManager {
    func setupCustomerSessionProvider() {
        billing.setCustomerSessionProvider { [weak self] () async -> UBCustomerSessionDetails? in
            await self?.fetchCustomerSession()
        }
    }

    private func fetchCustomerSession() async -> UBCustomerSessionDetails? {
        // Configure request to your backend endpoint
        guard let url = URL(string: "https://your-backend.example.com/customer-session") else {
            print("Invalid URL")
            return nil
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        // Send any additional headers needed to authenticate the user, for example, an auth token.
        request.setValue("Bearer \(authToken)", forHTTPHeaderField: "Authorization")

        do {
            // Make the request
            let (data, response) = try await URLSession.shared.data(for: request)

            guard let httpResponse = response as? HTTPURLResponse else {
                print("Invalid response format")
                return nil
            }

            switch httpResponse.statusCode {
            case 200:
                // Parse the successful response
                let decoder = JSONDecoder()
                decoder.dateDecodingStrategy = .secondsSince1970
                return try decoder.decode(UBCustomerSessionDetails.self, from: data)

            case 401:
                // User not authenticated - SDK will enter unauthenticated state
                print("Authentication required")
                return nil

            default:
                print("Unexpected status code: \(httpResponse.statusCode)")
                return nil
            }
        } catch {
            print("Session provider error: \(error.localizedDescription)")
            return nil
        }
    }

    // Call this method when your user signs out
    func handleSignOut() async {
        await billing.reset() // Clear session data and caches
    }
}
```

> The BillingSDK automatically calls your session provider whenever it needs to authenticate with Stripe. When the provider returns `nil`, the SDK enters an unauthenticated state.

## Display subscription buy buttons [iOS]

Buy buttons provide a prebuilt UI element to let customers purchase subscriptions. Each button is linked to a specific product and price in your Stripe account.

### Create buy buttons in the Dashboard

Follow [this guide](https://docs.stripe.com/payment-links/buy-button.md) to create buy buttons in the Dashboard. If you plan to use the entitlement checking functionality, ensure that the products you’ve created have [Entitlements](https://docs.stripe.com/billing/entitlements.md) attached to them.

### Display a buy button

```swift
import SwiftUI
import BillingSDK

struct SubscriptionView: View {
    @State private var buyButton: BuyButton?
    @State private var isLoading = true
    @State private var errorMessage: String?

    // Replace with your buy button ID from the Dashboard
    let buttonId = "buy_btn_1Abcdef123456"

    var body: some View {
        VStack {
            if isLoading {
                ProgressView("Loading subscription options...")
            } else if let buyButton = buyButton {
                // Display the prebuilt buy button UI
                // Alternatively the BuyButton class also provides all the data to render
                // a custom UI element.
                buyButton.view()
                    .frame(height: 56)
                    .padding(.horizontal)
            } else if let errorMessage = errorMessage {
                Text("Error: \(errorMessage)")
                    .foregroundColor(.red)
                Button("Retry") {
                    loadBuyButton()
                }
            }
        }
        .onAppear {
            loadBuyButton()
        }
    }

    func loadBuyButton() {
        isLoading = true
        errorMessage = nil

        Task {
            do {
                // Fetch the button from Stripe
                buyButton = try await BillingManager.shared.billing.getBuyButton(id: buttonId)
                isLoading = false
            } catch {
                errorMessage = "Failed to load buy button"
                isLoading = false
            }
        }
    }
}
```

> Buy buttons work even when users aren’t authenticated. The SDK creates a new Stripe Customer during purchase if needed.

## Check and validate entitlements [iOS]

Entitlements let you control access to premium features based on a customer’s active subscriptions.

### Check a specific entitlement

Verify if a user has access to a specific feature:

```swift
func checkPremiumAccess() async {
    do {
        let hasPremiumAccess = try await BillingManager.shared.billing.hasEntitlement(lookupKey: "premium_tier")

        if hasPremiumAccess {
            // User has premium access - enable features
            unlockPremiumFeatures()
        } else {
            // User doesn't have access - show upsell
            showPremiumUpsell()
        }
    } catch {
        showErrorMessage("Couldn't verify entitlements status")
    }
}
```

### Get all active entitlements

Retrieve all entitlements the customer has access to:

```swift
func loadUserEntitlements() async {
    do {
        // Force refresh ensures we get the latest data from the server
        let entitlements = try await BillingManager.shared.billing.getActiveEntitlements(forceRefresh: true)

        // Map entitlements to app features
        let features = entitlements.map { $0.lookupKey }
        updateAvailableFeatures(features)

    } catch {
        handleError(error)
    }
}
```

### Listen for entitlement changes

Set up a listener to be notified when entitlements change:

```swift
import Foundation
import BillingSDK

extension BillingManager {
    func setupEntitlementListener() {
        billing.onEntitlementsChanged { updatedEntitlements in
            // Update UI based on new entitlements
            DispatchQueue.main.async {
                self.updateAppFeatures(based: updatedEntitlements)
                self.refreshUI()
            }
        }
    }
}
```

> When no session is present, `getActiveEntitlements()` returns an empty array.

## Present the customer portal [iOS]

The customer portal lets subscribers manage their subscriptions, payment methods, and billing information.

### Show the customer portal

Present the portal when users need to manage their subscription:

```swift
func manageSubscriptionTapped() {
    Task {
        do {
            let portal = try await BillingManager.shared.billing.getCustomerPortal()

            // Show portal within your app (recommended)
            portal.presentCustomerPortal(from: self)

        } catch {
            if let billingError = error as? BillingSDKError {
                switch billingError {
                case .unauthenticated:
                    // User needs to log in first
                    showLoginPrompt()
                default:
                    // Handle other errors
                    showErrorMessage("Could not load subscription management")
                }
            } else {
                showErrorMessage("Could not load subscription management")
            }
        }
    }
}
```

> The customer portal requires an active authenticated session. If the user isn’t logged in, the SDK throws an `.unauthenticated` error.

### External redirection (optional)

You can also open the portal in a browser:

```swift
let portal = try await BillingManager.shared.billing.getCustomerPortal()
portal.redirectToCustomerPortal() // Opens in default browser
```

## Session management [iOS]

### Session management

Reset the SDK when users sign out to clear session data and caches:

```swift
func signOut() async {
    // Clear your app's auth state
    UserDefaults.standard.removeObject(forKey: "auth_token")

    // Reset the BillingSDK state
    await BillingManager.shared.billing.reset()

    // Navigate to login screen
    showLoginScreen()
}
```

## Test your integration

During development, use your [sandbox API keys](https://docs.stripe.com/keys.md#obtain-api-keys) and sandbox Customer IDs to avoid creating real charges.

### Testing scenarios

Test these common scenarios:

| Scenario                  | Steps                                         |
| ------------------------- | --------------------------------------------- |
| New subscription purchase | Present a buy button to a new user            |
| Subscription management   | Use the customer portal to change plans       |
| Entitlement verification  | Check a premium feature with `hasEntitlement` |
| Error handling            | Test with invalid keys or expired sessions    |
| Sign out flow             | Verify `billing.reset()` clears cached data   |

## See also

- [Entitlements](https://docs.stripe.com/billing/entitlements.md)
- [Configure the customer portal](https://docs.stripe.com/customer-management/integrate-customer-portal.md)
- [How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview.md)
