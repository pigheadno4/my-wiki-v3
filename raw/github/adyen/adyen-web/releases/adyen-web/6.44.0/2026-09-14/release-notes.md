## Improvements

- Improved: replace deprecated keypress event with keydown event (https://github.com/Adyen/adyen-web/pull/4143)

## Bug fixes

- Fixed: Card expiry date and security code fields no longer lose their format guidance when they enter an error state (https://github.com/Adyen/adyen-web/pull/4091)

- Fixed: Announce loading to screen readers for QR/redirect payment methods and for Card and stop these announcements being cleared from the shared screen reader panel before they can be read (https://github.com/Adyen/adyen-web/pull/4098)

- Fixed: Components crashing when `null` data was passed (https://github.com/Adyen/adyen-web/pull/4134)


