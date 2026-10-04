**Changes**
* Updated Stripe iOS SDK from 26.9.0 to 26.11.0.
* Updated Stripe Android SDK from 23.17.1 to 23.19.0.

**Features**

* [Added] Added `idType` to Crypto Onramp `KycInfo`, supporting US SSN, Canada SIN, Colombia NIT, and Philippines TIN.

**Changes**

* Updated Stripe iOS SDK from 26.9.0 to 26.11.0.
* Updated Stripe Android SDK from 23.17.1 to 23.19.0.
* [Changed] Android: Migrated Google Pay payment method and token creation to the Activity Result API.
* [Changed] Android: Checkout billing details collection is now controlled by the Checkout Session; `paymentElement.billingDetailsCollectionConfiguration` applies only to iOS.

**Breaking changes**

* [Removed] Removed support for the React Native old architecture. Enable the new architecture with `newArchEnabled=true` in `gradle.properties` for Android, `RCT_NEW_ARCH_ENABLED=1` in your `Podfile` for iOS, or `newArchEnabled: true` in your app configuration for Expo.

**Fixes**

* [Fixed] Android: Fixed Crypto Onramp presentation failures after Activity recreation by recreating the presenter for the current Activity.