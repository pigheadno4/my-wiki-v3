# C44 Klarna iOS retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-ios`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/ios/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-ios]]` → `[[raw/adyen/docs/payment-methods/klarna/ios/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does the Klarna for iOS page cover, and what does it not establish?

**Answer path:** Raw lines 15–29 show a navigation chooser for adding Klarna to an iOS app. It links Drop-in and Redirect Component child guides and generic iOS Sessions base guides. The chooser itself does not establish method eligibility for a merchant, an SDK version, or live payment success.

## Q2 — central capability, prerequisites and warnings

**Query:** Which iOS integration routes are offered, and where do implementation requirements live?

**Answer path:** `## How do you want to integrate?` lines 19–27 identifies the all-in-one Drop-in route and Redirect Component route. Line 29 links generic iOS Sessions base guides. Request fields, SDK setup, return handling, capture and recurring conditions are not specified on this chooser; follow the child and base guides and use the Klarna overview for product/eligibility scope.
