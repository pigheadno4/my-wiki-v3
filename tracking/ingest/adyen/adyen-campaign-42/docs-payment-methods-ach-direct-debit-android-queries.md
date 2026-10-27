# Fixed retrieval checks — ACH Android chooser

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ach-direct-debit-android.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 source is an **Android ACH Direct Debit navigation chooser** for Drop-in versus Components, plus links to the matching main Sessions/Advanced integration guides (primary raw `raw/adyen/docs/payment-methods/ach-direct-debit/android/2026-09-15.md:15-36`; canonical source stem `source-adyen-docs-payment-methods-ach-direct-debit-android`). It does not state Checkout API/Android SDK minima, request fields, bank validation, mandate requirements, live eligibility or final payment outcome. The reviewed child sources `source-adyen-docs-payment-methods-ach-direct-debit-android-drop-in` and `source-adyen-docs-payment-methods-ach-direct-debit-android-component`, plus the ACH overview, carry those method details.

## Q2. What are the central routes, prerequisites and warnings?

Choose the linked Android **Drop-in** child for all-in-one UI or Android **Components** child for component integration (`:19-27`); build the main integration first using the linked Android Drop-in/Components Sessions or Advanced guide (`:29-36`). The Components blurb calls the route a **Redirect Component** (`:27`), while its link targets the ACH Android Component child; do not infer a redirect-only ACH action from the chooser. This page is navigation, not evidence that a payment or bank validation succeeded.
