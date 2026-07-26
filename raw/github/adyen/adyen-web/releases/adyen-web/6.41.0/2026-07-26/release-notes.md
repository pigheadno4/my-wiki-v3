## Improvements

- Improved: Propagate `healthcare` field to the `onBinLookup` callback (https://github.com/Adyen/adyen-web/pull/4084)

- Improved: Detect if 3DS2 challenge token is missing a valid domain for the threeDSNotificationURL. Without a valid domain we will never receive the postMessage telling us the 3DS2 process is complete. (https://github.com/Adyen/adyen-web/pull/4073)

- Improved: replace deprecated keypress event with keydown event (https://github.com/Adyen/adyen-web/pull/4066)

## Bug fixes

- Fixed: Remove explicit any types from Dropin, ANCV, Giftcard and ThreeDS2 components (https://github.com/Adyen/adyen-web/pull/4080)

- Fixed:Stop displaying installments defined at the component level when in a sessions integration, and put a warning message in the console. This installment configuration could end up in being shown in the UI, but was then always ignored by the backend. (https://github.com/Adyen/adyen-web/pull/4079)

- Fixed: aria-checked missing in the Dropin payment method list if openFirstPaymentMethod set to false (https://github.com/Adyen/adyen-web/pull/4085)


