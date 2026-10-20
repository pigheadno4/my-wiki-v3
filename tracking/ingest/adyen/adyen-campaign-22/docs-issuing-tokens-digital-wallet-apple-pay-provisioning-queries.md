# C22 Apple Pay provisioning retrieval checks

## Q1 — What routes and prerequisites does the captured Issuing guide give for adding a card to Apple Wallet?

The 2023-modified guide captured 2026-09-15 describes Adyen Apple Pay Provisioning SDK flows from an issuer iOS app and directly from Apple Wallet; it calls for both when the business has an iOS app (raw lines 21–23, 39–43, 135–146). It lists iOS 13.4+, Xcode 14+ and Swift 5.7+, plus a specified payment instrument, a server GET for activation data, and the Bank Issuing PaymentInstrument Network Token Activation Data API role (raw lines 31–37, 55–74). The Wallet route also requires Wallet and Authentication UI extensions (raw lines 141–182). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-tokens-digital-wallet-apple-pay-provisioning]] → [[raw/adyen/docs/issuing/tokens-digital-wallet/apple-pay-provisioning/2026-09-15]].

## Q2 — What eligibility, timing and outcome boundaries matter?

The page is explicitly work in progress (raw line 19). In-app `canAddCard()` governs button display and `canAddCardDetails()` checks device compatibility; the `didFinishProvisioning` callback carries a possible error (raw lines 76–92, 123–133). The direct-Wallet extension status and pass-entry stages have distinct 100 ms and 20 s limits, with a fresh activation-data GET specified if exceeded (raw lines 251–270, 332–348). The test-host examples and SDK flow do not establish current program eligibility or a successfully provisioned card. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-tokens-digital-wallet-apple-pay-provisioning]] → [[raw/adyen/docs/issuing/tokens-digital-wallet/apple-pay-provisioning/2026-09-15]].
