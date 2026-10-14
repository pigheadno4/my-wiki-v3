# Fixed retrieval checks: iOS Mobile security

1. **Question:** What happens if staff remove the passcode from an iOS device using Mobile SDK 3.18.0 or later, including one with stored offline payments?
   **Expected answer:** The SDK requires a passcode to call any `PaymentService` function from version 3.18.0. Changing the passcode is allowed, but removing it prevents further transactions on that device and makes store-and-forward offline payments made while a passcode was set unrecoverable. The page's display-lock and simple-passcode workarounds still keep a passcode. Source: pinned raw `### Setting a device passcode` (2026-09-15 snapshot).

2. **Question:** Does the iOS page's PCI approval make a merchant POS app certified, and where should API credentials be held?
   **Expected answer:** The page describes Tap to Pay on iPhone as an MPoC-validated solution for iOS 18.4 and later, with a version-specific one-year support/session window and an earlier-version qualification. It does not certify a particular merchant app. Adyen API keys must remain secret on the server; the mobile app must not call Adyen APIs directly. Mutual authentication such as mTLS between the POS app and server is recommended. Source: pinned raw `## PCI approval of Tap to Pay on iPhone`, `## Security best practices` (2026-09-15 snapshot).
