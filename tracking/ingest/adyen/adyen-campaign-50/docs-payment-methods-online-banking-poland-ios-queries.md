# Fixed queries — Online banking Poland iOS chooser

## Q1 — purpose and limits

**Query:** What does the captured Online banking Poland iOS page provide, and what cannot be inferred from it?

**Expected answer:** `https://docs.adyen.com/payment-methods/online-banking-poland/ios` is a 2026-09-15-captured **iOS chooser** linking Poland Drop-in and Components child guides and four main Sessions/Advanced iOS integration routes. It is not a full implementation recipe and gives no method request fields, SDK minimum, merchant eligibility or successful-payment proof. The PL/PLN Przelewy24 payment-method context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-poland/ios/2026-09-15.md`, `# Online banking Poland for iOS` lines 15–17 and chooser lines 19–27). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-ios.md`.

## Q2 — child routes and malformed wording

**Query:** Which iOS routes are offered, which base guides are linked, and how should “Use the None” be interpreted?

**Expected answer:** The page offers Drop-in, described as the all-in-one UI solution, and Components, linking respectively to `/payment-methods/online-banking-poland/ios-drop-in` and `/payment-methods/online-banking-poland/ios-component` (pinned `raw/adyen/docs/payment-methods/online-banking-poland/ios/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). The Components description literally says “Use the None”; treat it as malformed placeholder text, not a method type. The page says to establish the main integration first and links iOS Drop-in and Components base guides under **both Sessions and Advanced** flows (raw `## See also` lines 29–36). Use the relevant child source for actual flow-specific requirements. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-ios.md`.
