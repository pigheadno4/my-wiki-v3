## New

- New: `onOrderUpdated` now also returns the latest `sessionData` in Sessions flow. (https://github.com/Adyen/adyen-web/pull/4235)

## Improvements

- Improved: securedFields now send messages informing about invalid hosting. This PR picks up these messages and converts them to analytic error events (https://github.com/Adyen/adyen-web/pull/4271)

- Improved: Null-safety in ClickToPay and the shared Modal component (https://github.com/Adyen/adyen-web/pull/4254)

## Bug fixes

- Fixed: Apple Pay no longer throws unhandled promise rejections when the payment sheet can no longer be completed or aborted, while completing the payment or the merchant validation (https://github.com/Adyen/adyen-web/pull/4265)

- Fixed: Preserve the address lookup query when focus leaves the search field. (https://github.com/Adyen/adyen-web/pull/4266)

- Fixed: a stale 3DS2 challenge `postMessage` listener no longer resolves after its component is removed from the DOM outside of Preact's lifecycle, preventing a duplicate `onAdditionalDetails`/`/paymentDetails` call. (https://github.com/Adyen/adyen-web/pull/4273)


