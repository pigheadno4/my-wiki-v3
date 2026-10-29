# Clearpay iOS chooser retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-clearpay-ios`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-ios.md` → `raw/adyen/docs/payment-methods/clearpay/ios/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What is this Clearpay iOS page for, and can its options prove that a merchant has Clearpay enabled?

**Expected:** It is an iOS navigation chooser for Clearpay Drop-in and Components, with main iOS integration guide links. It does not provide request fields, regional eligibility, merchant enablement or a payment result. The related Clearpay overview gives GB/GBP scope and distinguishes regional brands. Evidence: pinned raw `# Clearpay for iOS` lines 15–17, `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36.

## Q2 — Central routes and prerequisite

**Query:** Which iOS child routes are offered and what main-integration prerequisite does the chooser state?

**Expected:** Drop-in is labelled an all-in-one UI route; Components points to `InstantPaymentComponent`. The page says to create the main integration before adding Clearpay and links iOS Drop-in/Components base guides for both Sessions and Advanced flows. Those links do not replace child-specific requirements or establish a live outcome; consult the chosen child guide for flow, request, redirect and lifecycle details. Evidence: pinned raw `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36.
