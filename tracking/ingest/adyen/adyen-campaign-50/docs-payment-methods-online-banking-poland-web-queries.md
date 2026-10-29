# Fixed queries — Online banking Poland Web chooser

## Q1 — purpose and limits

**Query:** What does the captured Online banking Poland Web page provide, and what cannot be inferred from it?

**Expected answer:** `https://docs.adyen.com/payment-methods/online-banking-poland/web` is a 2026-09-15-captured **Web chooser** linking Poland Drop-in and Components child guides and four main Sessions/Advanced Web integration routes. It is not a complete implementation recipe and gives no payment request fields, SDK minimum, merchant enablement or successful-payment proof. The PL/PLN Przelewy24 payment-method context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-poland/web/2026-09-15.md`, `# Online banking Poland for Web` lines 15–17 and chooser lines 19–27). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-web.md`.

## Q2 — Web child and base-guide routes

**Query:** Which Web integrations does the Poland chooser offer, and what base guides must be used before adding the method?

**Expected answer:** The chooser offers Drop-in, described as an all-in-one UI solution, at `/payment-methods/online-banking-poland/web-drop-in`, and Components, described with `OnlineBankingPL`, at `/payment-methods/online-banking-poland/web-component` (pinned `raw/adyen/docs/payment-methods/online-banking-poland/web/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). It says to establish the main Web integration before adding the method and links Drop-in and Components base guides under **both Sessions and Advanced** flows (raw `## See also` lines 29–36). Use the relevant child source for actual request and redirect requirements; the chooser's label does not itself establish a runnable setup. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-web.md`.
