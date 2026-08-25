<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### Breaking Changes 🛠
* [ECP-9904] Stop setting cc_type in payment additional_information by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3264
* [ECP-9885] Refactor sortAndFilterPaymentMethods return value by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3274
* [ECP-9891] Return structured /payments/details response in case of refusals and errors by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3277
* [ECP-9847] Enhance the authorized amount comparison logic by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3284
* [ECP-8668] Refactor the logic of getting capture mode of payment methods by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3286 https://github.com/Adyen/adyen-magento2/pull/3331
### New Features 💎
* [ECP-9944] Add cron to clean up stale adyen_payment_response rows by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3297
* [ECP-9946] Enable NEA region and upgrade checkout component to [v6.35.0](https://docs.adyen.com/online-payments/release-notes?title%5B0%5D=Web+Components%2FDrop-in&version%5B0%5D=6.35.0#releaseNote=2026-05-05-web-componentsdrop-in-6.35.0) by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3323
### Fixes ⛑️
* [ECP-9923] Make invoicing and order status consistent on partial payments by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3311
### Other Changes 🖇️
* [ECP-9835] Upgrade PHP API Library to [V29.0.0](https://github.com/Adyen/adyen-php-api-library/releases/tag/v29.0.0) by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3272
* [ECP-9905] Refactor: Remove duplicated payment response handling logic by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3273
* [ECP-9893] Remove unused supports_auto_capture configuration flag by @candemiralp in https://github.com/Adyen/adyen-magento2/pull/3280
* [ECP-9897] Read shopper data from window.checkoutConfig instead of the window.customerData global by @shubhamk67 in https://github.com/Adyen/adyen-magento2/pull/3275  https://github.com/Adyen/adyen-magento2/pull/3324
* Release v11.0.0 by @AdyenAutomationBot in https://github.com/Adyen/adyen-magento2/pull/3337

Current Checkout API version: v71
Current Checkout Component version: 6.35.0


**Full Changelog**: https://github.com/Adyen/adyen-magento2/compare/v10.10.3...v11.0.0