## New

- New: Gift cards accept brand-specific placeholders through `brandsConfiguration[brand].placeholders`, falling back per key to the top-level `placeholders`. (https://github.com/Adyen/adyen-web/pull/4247)

- New: Detect when multiple instances of AdyenCheckout are created on the same page, and generate suppressible console.warning (https://github.com/Adyen/adyen-web/pull/4077)

## Improvements

- Improved: Null-safety in the shared Address component (https://github.com/Adyen/adyen-web/pull/4228)

- Improved: Null-safety in Amazon Pay (https://github.com/Adyen/adyen-web/pull/4222)

- Improved: Null-safety in browser info collection, Click to Pay, Google Pay, Dragonpay and 3DS2 challenge and fingerprint types. (https://github.com/Adyen/adyen-web/pull/4226)

- Improved: Null-safety in Cash App Pay, PayPal and Fastlane (https://github.com/Adyen/adyen-web/pull/4221)

- Improved: Null-safety in shared form fields (Field, InputBase, InputDate, Select) (https://github.com/Adyen/adyen-web/pull/4223)

- Improved: Payment components handle missing optional callbacks and unmounted root nodes more safely (https://github.com/Adyen/adyen-web/pull/4217)

- Improved: Added validation null-safety and fixed untranslated Riverty consent links by falling back to English payment conditions. (https://github.com/Adyen/adyen-web/pull/4225)

## Bug fixes

- Fixed: Gift card balance check failures are now surfaced to the shopper instead of failing silently. (https://github.com/Adyen/adyen-web/pull/4206)

- Fixed: SDK buttons now inherit the page font instead of the browser default (https://github.com/Adyen/adyen-web/pull/4238)

- Fixed: Drop-in page jumping and content overflowing while payment methods expand or collapse (https://github.com/Adyen/adyen-web/pull/4238)

- Fixed: amounts and dates are now formatted using the locale requested by the merchant, even when we do not ship translations for it (https://github.com/Adyen/adyen-web/pull/4241)

- Fixed: Gift card pay button staying in the loading state in Drop-in after a failed balance check (https://github.com/Adyen/adyen-web/pull/4253)

- Fixed: Drop-in payment method items no longer show a tap highlight on mobile browsers (https://github.com/Adyen/adyen-web/pull/4238)

- Fixed: Card installment plans that do not provide installment values. (https://github.com/Adyen/adyen-web/pull/4207)

- Fixed: Link button styling and layout issue by passing the text via the `label` prop instead of children. (https://github.com/Adyen/adyen-web/pull/4236)


