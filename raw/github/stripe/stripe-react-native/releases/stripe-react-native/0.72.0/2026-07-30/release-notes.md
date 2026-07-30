**Changes**
* Updated Stripe iOS SDK from 26.3.0 to 26.4.1.
* Updated Stripe Android SDK from 23.12.0 to 23.13.1.
* [Changed] `useLinkController` (private preview): SetupIntent confirmation is now a separate step. The SDK no longer confirms the SetupIntent automatically inside `presentLinkController`; instead, confirmation is triggered explicitly after the payment method is selected.