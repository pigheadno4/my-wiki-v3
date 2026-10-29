# Atome iOS chooser retrieval checks

## Q1 — Purpose and scope

Query: What does Adyen's Atome for iOS page contain, and can it establish merchant eligibility or a completed payment?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2557 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-ios.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/atome/ios/2026-09-15.md` `# Atome for iOS` lines 15–27 and `## See also` lines 29–36. Expected answer: a 2026-09-15-captured chooser for iOS Atome Drop-in and Components plus main integration guide links, not behavioral or eligibility proof.

## Q2 — Routes and prerequisite

Query: Which iOS Atome integration guides does the chooser link to, and what main-integration prerequisite does it state?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-ios.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/atome/ios/2026-09-15.md` lines 19–36. Expected answer: iOS Drop-in for all-in-one UI, iOS Components for AtomeComponent, and base iOS Drop-in/Components guides in Sessions and Advanced flows; create the main integration before adding Atome. Warning: the chooser's four base links do not themselves prove that every child guide supports all flows or specify request fields, country/currency rules, redirect behavior, current enablement, or live success.
