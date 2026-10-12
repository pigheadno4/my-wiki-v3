# Adyen C01 correction verification — token-location finding

## Verification

- Current canonical source still contains the ambiguous statement at `wiki/sources/adyen/source-adyen-docs-online-payments-tokenization-make-token-payments.md:19`: “The request includes the token…” across the one-click `/sessions` and `/payments` scope.
- Pinned raw hash is unchanged and matches the manifest: `6982814b2c74fe578e667a8daa2d416df63500c3b08dc1ff28896e48a89c2a43`.
- Relevant raw context confirms the correction: the `/sessions` server request lists `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: CardOnFile`, with Drop-in/Component handling the selected stored-method flow (`raw/adyen/docs/online-payments/tokenization/make-token-payments/2026-09-15.md:63-75,299-301`). The `/payments` route explicitly requires `paymentMethod.storedPaymentMethodId` plus the matching `shopperReference`, `ContAuth`, and `CardOnFile` (`raw:303-325`). Merchant-initiated Subscription/UnscheduledCardOnFile payments separately require `/payments` with the token (`raw:711-727`).

## Exact approved replacement

Replace source line 19 in full with:

> - One-click is shopper-initiated and uses `CardOnFile`. For `/sessions`, send the matching `shopperReference` with `shopperInteraction` set to `ContAuth` and `recurringProcessingModel` set to `CardOnFile`; Drop-in/Component presents and handles the selected stored method. For `/payments`, also send `paymentMethod.storedPaymentMethodId` and the matching shopper reference.

## Residual query verdict

- **Before replacement: FAIL** for fixed query 1 because the source can imply that the `/sessions` request body carries the token.
- **After the exact replacement above: PASS** for both fixed queries. The endpoint ownership and token-location distinction becomes correct, while the existing source retains the central purpose, credential/method/webhook prerequisites, SCA and CVC/PCI warnings, outcome routes, and precise raw retrieval locators.
- No further correction is required for this finding. Repository remains untouched.
