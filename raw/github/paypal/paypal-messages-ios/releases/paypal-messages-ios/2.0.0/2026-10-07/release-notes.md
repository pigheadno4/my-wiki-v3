## [2.0.0](https://github.com/paypal/paypal-messages-ios/compare/1.2.0...2.0.0) (2026-09-10)


### ⚠ BREAKING CHANGES

* minimum supported iOS version raised from 14.0 to
15.0 across the podspec, SPM package manifest, and all Xcode projects
(library, Demo app, CarthageTest, SPMTest). Consumers still targeting
iOS 14 must stay on the previous major version.

* fix: resolve pre-existing SwiftLint violations

Combine multiple pattern bindings in Environment.swift's .develop
case match, and drop a superfluous force_unwrapping disable comment
in PayPalMessageModalMocks.swift that no longer matches any
violation. Unrelated to the iOS 15 bump but surfaced by CI on this
branch since no lint run had happened against develop since May.

### Features

* bump minimum iOS deployment target to 15.0 ([#57](https://github.com/paypal/paypal-messages-ios/issues/57)) ([6681c9b](https://github.com/paypal/paypal-messages-ios/commit/6681c9bccb0967d1991018c97d5d75b4da0811b9))


### Documentation

* add Braintree SDK requirement disclaimer to README ([#55](https://github.com/paypal/paypal-messages-ios/issues/55)) ([fdd1868](https://github.com/paypal/paypal-messages-ios/commit/fdd18681f486a3b2f1c60e3c47f8669f55a73a96))

