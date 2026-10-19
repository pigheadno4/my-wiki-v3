---
title: "Adyen Issuing: Create cards"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/create-cards"
raw_files:
  - "adyen/docs/issuing/create-cards/2026-09-15.md"
tags: [adyen, issuing, cards, payment-instruments]
---

## Overview

Adyen's 2026-09-15-captured Issuing guide describes creating virtual or physical cards as `paymentInstrument` resources linked to a balance account, then conditionally assigning authorized users to company cards. It provides test-environment request and response examples and live physical-card requirements; the examples do not establish current eligibility, card activation, or completed payment. [[adyen]] [[adyen-issuing]]

## Key takeaways

- An account holder and balance account precede issuance. Cards need a Visa or Mastercard pre-approved use case (scheme program), handled by Adyen by default. PCI scope depends on card type and use; Adyen directs the platform to its contact for a use-case assessment. See raw lines 19-23.
- Creating a card means POSTing a card `paymentInstrument` associated with a `balanceAccountId`. A virtual card has no physical form and returns card details; a physical-card creation request starts a manufacturing order and does **not** return full card details. Physical requests include manufacturing-profile and delivery information. The balance-account association can be changed later only while the card is inactive. See raw lines 31-53 and 598-610.
- The guide says cards default to `active`, recommends `inactive` for physical cards until delivery, and uses an inactive physical-card test example. The companion [[source-adyen-docs-issuing-account-holder-status]] instead labels `inactive` as the initial payment-instrument status (its raw status-definition table); these captured initial-status descriptions conflict, so do not infer one universal default from them. Test physical cards are not delivered, though card-order created/updated events are sent asynchronously. Live physical-card creation requires a card and mailer design approved by Visa or Mastercard; to stop personalization, status must be updated before the order reaches the manufacturer. See raw lines 25-29, 53-57, 591-596 and 972-976.
- For multiple authorized users of a company card, the guide says all users must be identified when the card is created. It requires Configuration and Legal Entity Management API credentials, and says existing cards intended for multiple users must be updated before contacting Adyen to enable the feature. Each user needs a legal entity and requested `authorisedPaymentInstrumentUser` capability; a newly requested capability starts `pending`. Assignment follows verification and `allowed` capability status. `invalid` needs more information; `rejected` is final and the user cannot use the card. Subsequent daily sanctions checks can change capability to invalid/rejected and suspend the card. See raw lines 927-958.
- After card creation, POST assigns authorized-user legal-entity IDs; GET lists them. PATCH **replaces the entire authorized-user list**, so a one-user removal must send the retained users too; DELETE removes all users. Successful mutation examples return HTTP 204 only. See raw lines 960-970.

## Detail locators

- Physical request fields, test examples in curl and eight SDK variants, response and card-order events: raw lines 38-596.
- Virtual request fields, test examples in curl and eight SDK variants, response with card details: raw lines 598-925.
- Authorized-user legal-entity data, verification timing and API sequence: raw lines 927-970. Adyen says verification can take up to 48 hours and recommends waiting at least 48 hours to check status; this is advice, not a guarantee.
- Funding, authorization and lifecycle are directed to separate guides under `## Next steps`: raw lines 978-998.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[source-adyen-docs-issuing-integration-checklist]] — integration and go-live sequence.

## Raw Sources

- [[raw/adyen/docs/issuing/create-cards/2026-09-15|Adyen Create cards, captured 2026-09-15]]
