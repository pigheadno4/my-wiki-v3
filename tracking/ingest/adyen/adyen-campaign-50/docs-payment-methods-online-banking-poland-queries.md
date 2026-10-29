# Fixed queries — Online banking Poland overview

## Q1 — purpose, scope and limits

**Query:** What does the captured Online banking Poland overview establish, and what should not be inferred from it?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-poland` is a 2026-09-15-captured PL/PLN online-banking method overview identifying partner Przelewy24 (P24), bank selection and redirect, matrix marks, and integration routes. Its “one of the most popular” wording is a dated source assertion. None of this proves current ranking, merchant-account enablement or payment success (full pinned `raw/adyen/docs/payment-methods/online-banking-poland/2026-09-15.md`, `# Online banking Poland` lines 15–25; capability table lines 27–29). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md`.

## Q2 — redirect, capability and routes

**Query:** In the captured Poland overview, what is the shopper journey, which lifecycle operations are marked, and where do the integration links lead?

**Expected answer:** Adyen says it offers the method via **Przelewy24 (P24)**. The shopper chooses an issuing bank and is redirected to its website or mobile app to complete payment (pinned `raw/adyen/docs/payment-methods/online-banking-poland/2026-09-15.md`, raw lines 23–25). The PL/PLN Online Banking redirect matrix crosses recurring, separate/partial/multiple partial captures and chargebacks, while checking refunds including partial/multiple partial (lines 27–29). The crosses do not establish that every ordinary capture operation is unsupported. Routes cover Web, iOS, Android, React Native, Flutter, API-only website/iOS/Android and Pay by Link (lines 31–73); generic 3D Secure/Capture See also links do not imply method-specific support (lines 75–80). Redirect initiation and route links do not prove payment finality. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md`.
