# Retrieval checks: PaySafeCard for Android

## Q1 — Purpose and scope
Query: What does the PaySafeCard Android page cover, and what does it not establish?
Expected: A 2026-09-15-captured Android integration chooser linking method-specific Drop-in and Components guides plus main Sessions/Advanced Android guides. It does not supply full request/action rules, prove current eligibility, or show live payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paysafecard-android]] → [[raw/adyen/docs/payment-methods/paysafecard/android/2026-09-15|pinned raw]]. Verify canonical stem `/payment-methods/paysafecard/android`, raw lines 15–19 and **See also** lines 29–36.

## Q2 — UI route and flow-label caveat
Query: Which PaySafeCard Android UI routes does the chooser offer, and how does its redirect wording compare with the overview?
Expected: Drop-in points to `/payment-methods/paysafecard/android-drop-in` as all-in-one UI; Components points to `/payment-methods/paysafecard/android-component` and names `InstantPaymentComponent` handling redirect. It links Android Drop-in and Components base guides for Sessions and Advanced. The chooser's redirect wording (child raw line 27) conflicts with the linked PaySafeCard overview's Direct capability label (overview raw lines 25–27); preserve both captured labels without deciding current behavior. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paysafecard-android]] → [[raw/adyen/docs/payment-methods/paysafecard/android/2026-09-15|pinned raw]], with [[source-adyen-docs-payment-methods-paysafecard]] for overview context. Verify canonical stem and child raw lines 19–36.
