# C23 worker queries — Issuing PIN reveal with iOS SDK

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data-reveal-pin-ios-sdk]] → [[raw/adyen/docs/issuing/manage-card-data/reveal-pin-ios-sdk/2026-09-15]].

## Q1. What is the PIN-reveal flow and what are its prerequisites?

For an Adyen-issued card, the platform can let the cardholder view the PIN in its iOS app (raw lines 19–23). It needs Configuration API credentials with the **Bank Issuing PIN Reveal Webservice role**, iOS 13.0+, and the Card Reveal iOS SDK (raw lines 36–46). The platform obtains a base64 RSA public key with `GET /publicKey?purpose=pinReveal&format=pem`, passes it to the client, uses `PinRevealService.generateEncryptedKey`, then requests `POST /pins/reveal` for the card's `paymentInstrumentId` and encrypted key (raw lines 48–57, 217–264). Adyen returns an encrypted PIN block and token, and the iOS SDK decrypts the block for app display (raw lines 465–495).

## Q2. What sensitive-data and version boundaries apply?

The response's encrypted block is an ISO Format 4 PIN block; the token is needed for decryption, and the plaintext PIN is handled in the app after the SDK call (raw lines 465–495). The page gives iOS 13.0 minimum but no Card Reveal SDK release version; separate server API-library snippets use named versions and TEST endpoints (raw lines 36–46, 63–214, 270–463). Some sample `/publicKey` calls contain `string` placeholders despite the required `pinReveal`/`pem` query values (raw lines 54–57, 83–85, 101–105). A test example does not prove live cardholder authentication, PIN delivery, or payment success.
