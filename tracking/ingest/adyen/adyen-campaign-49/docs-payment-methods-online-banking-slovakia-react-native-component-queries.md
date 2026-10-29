# Fixed queries — Online banking Slovakia React Native Component

## Q1 — purpose, scope and limits

**Query:** What does the captured Online banking Slovakia React Native Component guide cover, and is Sessions supported?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-slovakia/react-native-component` is a 2026-09-15-captured React Native Component add-on guide. It explicitly says **React Native Components do not support Sessions flow** and gives Advanced redirect, issuer and test/live additions only. It does not prove current account enablement or payment completion. Method-level SK/EUR context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/react-native-component/2026-09-15.md`, `## Sessions flow Component` lines 25–29; `## Advanced flow Component` lines 31–42). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-react-native-component.md`.

## Q2 — Advanced prerequisites, issuer and gaps

**Query:** For the captured React Native Component Advanced flow, what is required and which prerequisite/example details need verification?

**Expected answer:** Advanced requires an existing React Native Components integration, redirect handling with `action.type: redirect`, and Customer Area addition (pinned `raw/adyen/docs/payment-methods/online-banking-slovakia/react-native-component/2026-09-15.md`, `## Advanced flow Component` lines 31–42). The Components row links to a **Drop-in** base guide and the Checkout API minimum is blank (“v or later”), so neither a correct base guide nor version number can be inferred from that row. No extra Component configuration is needed (lines 44–48). `paymentMethod.issuer` in `/payments` is required and represents the bank the shopper selected (lines 50–58); `onlineBanking_SK`, `cs`, EUR and `returnUrl` are sample values (lines 60–80). The Go example labels v10.4.0 while importing `/v9/` paths (lines 237–246). The page directs test status checks to test Customer Area Payment list and live method addition to Customer Area (lines 372–378); these do not prove completed payment. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-react-native-component.md`.
