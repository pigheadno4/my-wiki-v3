# Klarna Debit Risk Android retrieval checks

## Q1 — What does this Android page cover, and what must it not be used to infer?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-debit-risk-android]]` → `[[raw/adyen/docs/payment-methods/klarna-debit-risk/android/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-klarna-debit-risk-android`. Full pinned raw path: `raw/adyen/docs/payment-methods/klarna-debit-risk/android/2026-09-15.md`. Raw lines 15–27 identify this as an Android Drop-in/Components chooser. It does not provide request schema, eligibility, API/SDK versions, payment outcome or settlement proof.

## Q2 — Which integration routes and prerequisite does it give?

Use the same root/provider/concept/source/raw route. Raw lines 21–27 link separate Drop-in and Components method guides; line 27 names `InstantPaymentComponent` for redirect handling. Line 31 says to create the main integration before adding Klarna Debit Risk. Lines 33–36 link base Android Sessions and Advanced guides for both Drop-in and Components. Read the relevant child and base guides for implementation detail; this chooser alone does not establish a completed redirect or payment.
