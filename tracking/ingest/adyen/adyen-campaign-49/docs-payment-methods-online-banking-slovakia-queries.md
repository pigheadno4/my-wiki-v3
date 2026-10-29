# Fixed queries — Online banking Slovakia overview

## Q1 — purpose, scope and limits

**Query:** What does the captured Online banking Slovakia overview establish, and what should not be inferred from it?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-slovakia` is a 2026-09-15-captured SK/EUR online-banking method overview. It describes issuer-bank selection and redirect, an Adyen contract statement, matrix marks, and integration routes. Its “second most popular” ranking is a dated source assertion. None of this proves current ranking, merchant-account enablement or payment success (full pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/2026-09-15.md`, `# Online banking Slovakia` lines 15–27; capability table lines 29–31). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia.md`.

## Q2 — contract, capability and routes

**Query:** In the captured Slovakia online-banking overview, what are the shopper flow, acquiring-bank contract statement, lifecycle marks and integration routes?

**Expected answer:** The shopper chooses an issuing bank and is redirected to its website or mobile app to complete payment. The page says merchants integrating via Adyen do not need separate acquiring-bank contracts (pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/2026-09-15.md`, raw lines 25–27). The SK/EUR matrix labels Online Banking redirect; recurring, separate/partial/multiple partial captures and chargebacks are crossed, while refunds including partial/multiple partial are checked (lines 29–31). This does **not** assert all capture is unsupported or guarantee current merchant capability. Routes cover Web, iOS, Android, React Native, Flutter, API-only website/iOS/Android, and Pay by Link (lines 33–75); generic See also links do not imply method-specific 3D Secure/capture support (lines 79–84). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia.md`.
