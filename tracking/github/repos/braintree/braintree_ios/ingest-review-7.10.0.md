# Braintree iOS 7.10.0 ingest review

- Item: `github-72f033218ff5ef2cfae0`; mode: delta; reviewed 2026-10-04.
- Focused reading approved by the user's continuation approval: changed retained implementation and complete patch read; manifest inventories and unchanged changelog history verified mechanically. No whole-repository read or runtime test claimed.
- Both snapshot file inventories passed SHA-256 verification (285 prior, 291 current files). The prior changelog body is an exact suffix of the new changelog.
- No packet evidence gaps or unclassified changes; excluded tests/project/CI files remain outside the capsule. Optional campaign inputs and nonce parsing fix are contained, not a new payment-processing flow.

## Grounding quotes

Current snapshot `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/files/`:

- `Sources/BraintreePayPal/Models/PayPalCheckoutPOSTBody.swift`, CodingKeys: `case payPalCampaigns = "paypal_campaigns"`
- `Sources/BraintreeShopperInsights/Models/Variables.swift`, CodingKeys: `case payPalCampaigns = "paypalCampaigns"`
- `Sources/BraintreeShopperInsights/V2/BTCustomerRecommendationsResult.swift`: `public let expiresAt: String?`
- `Sources/BraintreeVenmo/BTVenmoAccountNonce.swift`, venmoAccount: `externalID: json["details"]["commonId"].asString()`

## Cycle

- [x] Evidence read and grounding
- [x] Concept audit and update
- [x] Cumulative source
- [x] Company update and source-count check (272 unchanged)
- [x] Concept citation check
- [x] Comparison disposition (no substantive cross-company comparison)
- [x] Contradiction check (version-qualified additions; pre-baseline history boundary clarified)
- [x] Provider index
- [x] Provider and root log
- [x] Validation and lifecycle completion (five schema pages pass; plain index/root log have pre-existing no-frontmatter convention; links checked at closure)
