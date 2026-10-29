# Fixed retrieval checks — docs-payment-methods-pix-flutter-drop-in

## Q1 — Identify the Flutter Pix flow and prerequisite scope

- Query: What does Adyen's captured Pix Flutter Drop-in guide add to Sessions and Advanced, and what account or payment outcome does it prove?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pix-flutter-drop-in.md` → `raw/adyen/docs/payment-methods/pix/flutter-drop-in/2026-09-15.md`.
- Expected: It is a 2026-09-15-captured add-on to existing Flutter Drop-in Sessions and Advanced flows (raw lines 15–25, 532–543). Sessions states Checkout API v68+, Support contact to add Pix, and a `/sessions` table with required amount (lines 29–50). Advanced requires `qrCode` additional-action handling, Customer Area addition, and a `/payments` table with required `paymentMethod` from front-end state plus amount (lines 536–567). Neither flow needs extra Pix configuration (lines 509–511, 546–548). The Sessions prerequisite URL points to Advanced flow despite the Sessions label (line 33). The Advanced `qrCode` action-handling link points to a generic `#handle-the-redirect` anchor (line 541), so verify the Flutter action handler for QR rather than assuming redirect handling alone is sufficient.
- Scope: TEST BR/BRL request samples, QR action and test offer promotion do not prove current merchant enablement or real paid execution. No Flutter SDK version is stated.

## Q2 — Recover Pix limits, Pending QR outcome and test/live boundary

- Query: Which field limits and expiry defaults differ by flow, and how should the QR response, refund and test promotion be interpreted?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pix-flutter-drop-in.md` → pinned raw.
- Expected: Sessions `shopperStatement` is shown with a 140-character maximum (raw line 48); Advanced says a supplied value must be under 60 characters, and `sessionValidity` defaults to one hour for Checkout API v71 or earlier versus 24 hours for v72 or later (lines 562–563). The Advanced example returns `resultCode: Pending` and `action.type: qrCode`, which is an intermediate QR step for an asynchronous method, not paid confirmation (lines 1055–1075, 1083). The source allows refund within 90 days after payment (lines 515, 1079). In TEST, promote a pending offer to sale and check Payment list for reconciliation simulation; live acceptance requires a separate Pix request in live Customer Area (lines 517–530, 1081–1094). Example validity timestamps from 2021 and 2025 are past the 2026 capture (lines 71, 597).
- Scope: `shopperName` and CPF/CNPJ `socialSecurityNumber` are advisable in Advanced but unmarked required (lines 559–568). Test promotion is a simulation, not a real shopper payment or live authorization.
