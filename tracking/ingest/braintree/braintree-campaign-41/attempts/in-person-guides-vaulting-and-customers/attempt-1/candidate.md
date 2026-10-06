---
title: "Braintree In-Person Vaulting and Customers"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/vaulting-and-customers"
raw_files:
  - "braintree/in-person/guides/vaulting-and-customers-2026-09-16.md"
tags: [braintree, in-person, card-readers, vaulting, customers, graphql]
---

## Overview

This 2026-09-16 snapshot of an unversioned Braintree In-Person website guide describes using a card reader to collect a physically presented payment method and store it for later transactions. It covers an optional Braintree customer profile, a vault-only reader flow, and a separate immediate-charge flow that also requests vaulting. The guide does not establish current product or reader availability, merchant eligibility, production enablement, package-qualified SDK behavior, exact commit-qualified GraphQL schema, consent or PCI obligations, or successful payment execution. [[braintree]] [[braintree-payment-methods]]

## Key takeaways

- A vaulted payment method may be linked to a Braintree customer ID, whose profile can contain customer data such as name, email and phone number, or retained as a standalone payment-method token for a customer profile held in the merchant's own CRM or POS. The customer object is optional, and one customer ID can organize multiple payment methods.
- The vault-only route requests vaulting without a related transaction. The reader request returns an in-store context ID to poll; when that context reaches `COMPLETE`, the guide says the response supplies a `paymentMethod.id` for later charge requests. The reader, asynchronous context and resulting payment method are distinct objects, and completing this vault flow is not evidence of an authorization, capture or settlement.
- The charge-and-vault route is a different operation: the guide adds `vaultPaymentMethodAfterTransacting` to `requestChargeFromInStoreReader` for a normal immediate-charge flow and then polls a charge context. Its prose says the completed response exposes `RequestChargeInStoreContext.transaction.customer`, while the displayed example nests customer data under `transaction.paymentMethod`; use the raw locator for the rendered example and current GraphQL authority for an exact response contract. A sample transaction status is not proof of a real authorization, capture or settlement.
- Later charges use the standard Braintree eCommerce GraphQL charge, authorization and capture mutations against the generated `paymentMethod.id`. The guide expressly classifies future charges against a Multi Use Payment Method as card-not-present and says card-not-present pricing applies. Vaulting therefore does not itself perform or guarantee any later authorization, capture or settlement.
- For a digital wallet used on the card reader, the guide says a later transaction using the vaulted token is automatically marked as merchant initiated and has a 24-hour authorization-expiry window. It recommends using `authorizationExpiresAt` to inform capture and reauthorization logic. This statement is specific to authorizations initiated from a token originating from a card-present digital wallet; it is not a universal authorization window.
- The tips distinguish the unique-per-vault-request `paymentMethodId`, which can be used for future charges but is discouraged for analytics, from `uniqueNumberIdentifier`, which the page describes as per-card-number analytics data that cannot perform future charges and is unavailable for PayPal and Venmo QRC methods. The page also routes vault criteria that can request a token only after a successful authorization attempt or `ALWAYS`, including after an unsuccessful attempt; consult the exact enum/schema authority before implementation.

## Detail locators

- **Purpose, future-charge scenarios and card-not-present pricing:** raw lines 14–28.
- **Optional customer ID and displayed customer mutation example:** raw lines 31–35.
- **Vault without a transaction, reader request, context polling and verification route:** raw lines 36–51.
- **Immediate charge plus vault request, polling language and displayed response example:** raw lines 54–68.
- **Separate future charge, authorization and capture mutation routes:** raw lines 69–80.
- **Vaulted card-present digital-wallet MIT treatment and 24-hour authorization expiry:** raw lines 85–90.
- **Payment-method token, analytics identifier, QRC exclusion and vault-criteria tips:** raw lines 93–105.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/in-person/guides/vaulting-and-customers-2026-09-16|Braintree In-Person Vaulting and Customers (2026-09-16 snapshot)]]
