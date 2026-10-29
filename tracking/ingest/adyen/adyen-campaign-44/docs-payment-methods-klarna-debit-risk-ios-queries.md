# C44 Klarna Debit Risk iOS retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-debit-risk-ios`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna-debit-risk/ios/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-debit-risk-ios]]` → `[[raw/adyen/docs/payment-methods/klarna-debit-risk/ios/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does the Klarna Debit Risk iOS page establish?

**Answer path:** It is an iOS integration chooser. Raw lines 15–27 route to Drop-in and Components child guides; lines 29–36 route to base iOS Sessions and Advanced guides. The source entry does not claim merchant eligibility, successful payment, working SDK class or token creation.

## Q2 — central routes and warnings

**Query:** Which iOS route should an implementer read, and can the chooser's `None` wording be used as an SDK class?

**Answer path:** Raw line 23 links the all-in-one Drop-in route; lines 25–27 link the Components route. Raw line 27 literally says `None`, matching an unresolved placeholder in [[source-adyen-docs-payment-methods-klarna-debit-risk-ios-component]], so verify the actual iOS SDK class in a matching version. `## See also` lines 29–36 supplies base Sessions/Advanced guides, while method-specific fields, redirect handling and outcomes belong to the selected child guide.
