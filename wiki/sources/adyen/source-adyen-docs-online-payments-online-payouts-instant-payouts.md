---
title: "Adyen Instant Card Payouts"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/online-payouts/instant-payouts"
raw_files:
  - "adyen/docs/online-payments/online-payouts/instant-payouts/2026-09-15.md"
tags: [adyen, payouts, cards, instant-payouts]
---

## Overview

Adyen's instant card payouts guide describes the legacy Payout API `/payout` flow for paying out to eligible Mastercard and Visa cards, across funds disbursements and money transfers. The 2026-09-15 webpage snapshot explicitly says Adyen is no longer accepting **new Payout API integrations**: new integrations should use the **Transfers API** card-payout guide, while existing Payout API integrations should contact Adyen about migration. This page is evidence for the documented legacy flow, not approval or live execution.

## Key takeaways

- In the documented Payout API flow, Adyen returns the result of the payout attempt immediately; it says funds are made available within 30 minutes, typically within 2 minutes, depending on the issuer. That timing is a documentation claim, not a guarantee for a particular card or account.
- Enablement requires contacting Adyen, compliance approval and Adyen-side configuration; a local entity is often required. The guide configures additional response data, checks card payout eligibility with a Checkout API zero-value `/payments` request, and tokenizes card details for recurring payouts before calling `/payout`. Raw card data may be passed only when fully PCI compliant; otherwise the guide directs use of Card Component for secure collection and encryption.
- Funds disbursements pay sellers, customers or freelancers for goods or services. Money transfers move funds between individuals or from a virtual wallet/account onto a card. The latter scenarios use different `fundSource` data for the sender card versus the wallet/account; the Visa money-transfer instructions include the preceding pay-in's `networkTxReference`. These are payout use cases, not checkout purchase flows.
- The documented service is domestic by default: recipient card use must be in its issuing country/region and currency; EEA card payouts within the EEA count as domestic. Cross-border cases require contacting Adyen, and in most cases a local entity. The guide lists supported recipient countries/regions. Additional validation for transfers between different entities can decline requests with nonconforming data.

## Detail locators

- `## Check if the card is eligible for payouts`: `payoutEligible` values (`Y`, Mastercard domestic-only `D`, `N`, `U`) and `fundsAvailability` (`I`, `N`), including the Mastercard condition; `### Tokenize the card details` gives the recurring setup.
- `## Funds disbursements`: one-off and recurring `/payout` request and response examples. `## Money transfers`: individual-to-individual, wallet/account-to-card and recurring examples, with `fundSource` and Visa pay-in linkage. The examples use test endpoints and versioned SDK snippets; they are examples, not production qualification.
- `## Data validation` and `## Supported countries/regions and currencies`: field validation, domestic and cross-border boundary, and recipient list.

## Related

- [[adyen]]
- [[adyen-card-payouts]]

## Raw Sources

- [[raw/adyen/docs/online-payments/online-payouts/instant-payouts/2026-09-15|Adyen instant card payouts webpage snapshot (2026-09-15)]]
