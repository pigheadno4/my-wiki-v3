## New

- New: Drop-in emits a new `paymentListDisplayed` analytics event reporting the payment methods it rendered (`availablePaymentMethods`, each with `displayMode`) in display order, plus the `/paymentMethods` items it did not render (`unavailablePaymentMethods`). (https://github.com/Adyen/adyen-web/pull/4081)

## Improvements

- Improved: the 3DS2 iframe to add attributes which enable WebAuthn and SPC challenges. (https://github.com/Adyen/adyen-web/pull/4116)

## Bug fixes

- Fixed: US postal code validation & postal code formatting for partial billing address mode (https://github.com/Adyen/adyen-web/pull/4111)


