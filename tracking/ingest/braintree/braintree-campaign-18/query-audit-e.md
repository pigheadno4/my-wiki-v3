# Braintree C18 fixed query audit — Group E

Scope: exactly the four fixed Group E questions for Vault Update Customer Information and Card Verification. Both pinned raws were read completely; no additional factual evidence was needed.

## `control-panel-vault-update`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources` → `[[source-braintree-control-panel-vault-update]]`) → `wiki/sources/braintree/source-braintree-control-panel-vault-update.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/articles/control-panel/vault/update-2026-09-16.md`.

1. **Where is updating customer information in Braintree Control Panel Vault documented?**
   - **Object/action match:** Updating an existing Vault customer's details, payment methods, billing addresses and future-use shipping addresses in the Control Panel; not customer creation, an API/SDK update operation, subscription mutation or a completed transaction's shipping-address edit.
   - **Direct answer:** `source-braintree-control-panel-vault-update.md` is the promoted retrieval entry and routes to the complete collected `# Update Customer Information` raw above.
   - **Exact locator:** raw provenance/canonical URL at lines 1 and 6–7; page identity and update categories at lines 14–23.
   - **Verdict:** PASS.

2. **Which customer-information update actions and boundaries does this page document?**
   - **Object/action match:** Control Panel edits to one existing Vault record, including payment-method and address effects; not proof of card verification, AVS execution, subscription update, PCI status or retroactive transaction mutation.
   - **Direct answer:** Search for the customer, open the ID and edit customer details, payment methods or addresses; the page calls the Control Panel practical for one or two customers and recommends the API for many. Updating card numbers may affect PCI scope, and selecting `Verify card` is strongly recommended but does not prove success. Adding a payment method does not update existing subscriptions. A record supports up to 50 addresses: billing addresses attach to payment methods, while shipping addresses are selected per transaction. Billing-address edits/additions/selections do not trigger AVS; verify the stored card again with the new billing data. Updating a shared customer address propagates to payment methods already using it. A created transaction's shipping address cannot be changed, though customer addresses can be changed for future transactions.
   - **Exact locator:** update categories/API scale at lines 16–23; PCI, subscription and verification boundaries at lines 26–34; address identity/limit at lines 39–45; no-AVS and re-verification boundary at lines 48–54; billing actions and propagation at lines 59–110; transaction-specific versus future shipping at lines 115–126.
   - **Verdict:** PASS.

## `control-panel-vault-card-verification`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-control-panel]]`) → `wiki/concepts/braintree-control-panel.md` (`## Sources` → `[[source-braintree-control-panel-vault-card-verification]]`) → `wiki/sources/braintree/source-braintree-control-panel-vault-card-verification.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/articles/control-panel/vault/card-verification-2026-09-16.md`.

3. **Where is Braintree Control Panel Vault card verification documented?**
   - **Object/action match:** Account-wide verification and re-verification of credit/debit card payment methods associated with the Vault; not customer-identity verification, AVS/CVV rule configuration, or purchase authorization/settlement.
   - **Direct answer:** `source-braintree-control-panel-vault-card-verification.md` is the promoted retrieval entry and routes to the complete collected `# Card Verification` raw above.
   - **Exact locator:** raw provenance/canonical URL at lines 1 and 6–7; page identity and card-only availability at lines 14–18; account-wide Control Panel section at lines 48–69; vaulted-card section at lines 102–125.
   - **Verdict:** PASS.

4. **Which verification purpose, access, outcome and payment or Vault boundaries does this page document?**
   - **Object/action match:** Verification of a card payment method before Vault storage or re-verification of a token-linked vaulted card; its `$0`/`$1` authorization is a checking mechanism, not approval or settlement of a later purchase.
   - **Direct answer:** Card verification is a first-line fraud check for credit/debit cards: it checks card/account details and configured AVS/CVV rules before Vault storage, and an invalid card is not stored. Account-wide access is Control Panel → gear → `Processing` → `Vaulting` → `Card Verification`; individual verification is separately routed to developer docs, and the page does not identify a required Control Panel role. The gateway normally attempts `$0`, falls back automatically to `$1` only for the processor response that indicates `$0` is unsupported, and immediately voids a successful `$1` so it does not settle; some banks may still show the voided amount temporarily as a pending charge. Generic declines are not retried by default unless `Retry All Failed $0` is enabled; failed Apple Pay verification requires manual retry. Re-verifying a vaulted card operates on its token-linked payment method, requires CVV recollection because CVV is not stored, and returns CVV/AVS responses; it does not verify the Vault customer's identity or authorize a purchase.
   - **Exact locator:** eligibility/purpose and pre-Vault outcome at lines 17–32; `$0`/`$1`, automatic void and pending-charge boundary at lines 35–43; account-wide and individual access at lines 48–69; retry outcomes/settings at lines 74–97; CVV recollection, payment-method-token navigation and displayed outcome at lines 102–125.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- **Full selected evidence/hash check:** both raws were read from provenance through their final lines. SHA-256 identities match the manifest pins: Update `baeae87ce3a127978ad4f539fef9d2dff278b07da916d3f5533f3ce6177ca0cf`; Card Verification `872044dc270bc01303f8e0aac99161f3891e4523759aad2fc5eb21fe680f989b`.
- **Bounded gap sweep:** filename, answer-phrase and source-reference searches surfaced the two exact raws plus navigation-only Search, customer/payment-method API, PCI, subscription, AVS/CVV, authorization-response and void authorities. The exact Control Panel raws answer all four fixed questions and expose no conflict requiring another source; no historical raw or extra raw was selected or read in full, and unread neighbors were not used as evidence.
- **Reciprocal/route check:** root `[[braintree-index]]`, provider `[[braintree-control-panel]]`, both concept-to-source links, both source-to-concept links, both `raw_files` entries and both exact `## Raw Sources` links resolve. Each source and concept retains the relevant PCI, subscription, AVS, shipping-address, verification-versus-authorization and pending-`$1` boundaries.
- **Completeness:** 4/4 fixed questions contain object/action match, direct answer, exact raw locator and verdict. No retrieval repair or additional promotion is required.

**Group verdict: PASS (4/4).**
