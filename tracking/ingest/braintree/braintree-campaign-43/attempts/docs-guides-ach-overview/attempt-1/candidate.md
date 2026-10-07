---
title: "Braintree ACH Direct Debit Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/overview"
raw_files:
  - "braintree/docs/guides/ach/overview-2026-09-16.md"
tags: [braintree, ach, direct-debit, javascript-v3, tokenization, vaulting, verification]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website overview describes ACH Direct Debit as a US payment method that debits a customer's bank account through the ACH network rather than a card brand. Its captured availability statement limits the route to eligible merchants using a custom JavaScript v3 client-side integration, alongside a server-side SDK, and says the method is unavailable in Drop-in UI. These statements are snapshot qualifications, not proof of current availability, merchant eligibility, account enablement, exact SDK behavior or successful payment execution. See [[braintree-payment-methods]] for the provider-wide payment-method route.

## Key takeaways

- The page organizes ACH acceptance around tokenizing, vaulting, verifying and transacting. It says their overlap depends on the chosen verification approach; this overview is an orientation rather than an exact implementation contract.
- Tokenization exchanges collected bank details, including account and routing numbers, for a one-time-use payment-method nonce. The resulting nonce neither verifies the bank account nor supports a transaction by itself; the page requires vaulting and successful verification before transaction creation.
- Vaulting exchanges the nonce for a persistent payment-method token. A merchant can initiate verification while vaulting or vault without attempting verification, but the vaulted method becomes transactable only after successful verification.
- The captured overview lists network check, micro-transfers, independent check and Instant Verification as bank-account verification methods. It describes network check as an immediate rules-based result, micro-transfers as two sub-dollar credits whose amounts the customer confirms, independent check as a merchant-owned method followed by manually marking the payment method verified, and Instant Verification as customer bank authentication through secure open-banking connections. Use the exact raw section and dedicated implementation guides to determine applicable setup and qualifications; this list is not proof that any option is currently available or enabled for a merchant.
- The page says verification methods may be combined and gives network check followed by micro-transfers as a recommended example. That example is guidance, not a requirement or a success guarantee.

## Material boundaries

- This source is a captured website overview, not current eligibility or availability authority, package-qualified SDK evidence, exact API-schema evidence, bank-account ownership proof, or evidence of a successful debit, transaction, settlement or funding.
- The client-side condition is specifically a custom JavaScript v3 integration, and the captured page excludes Drop-in UI. Do not generalize the overview to other client surfaces.
- The page names verification methods but does not establish that every listed method has identical eligibility, environment, setup or lifecycle behavior. Follow the applicable detailed guide before relying on one.

## Detail locators

- ACH Direct Debit identity and US network scope: `# Overview`, line 16.
- Eligible-merchant, custom JavaScript v3, server-side SDK and Drop-in UI qualifications: `**AVAILABILITY**`, lines 18–21.
- Four-stage lifecycle and verification-dependent overlap: lines 23–33.
- Tokenization, nonce identity and non-transactable-before-vault-and-verification boundary: `## Tokenizing`, lines 36–38.
- Vaulting with or without an immediate verification attempt and successful-verification prerequisite: `## Vaulting`, lines 41–53.
- Verification-method descriptions and combination example: `## Verifying`, lines 56–72.
- Configuration navigation: `Next Page: Configuration`, line 74; navigation only, not evidence for configuration behavior.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/ach/overview-2026-09-16|Braintree ACH Direct Debit Overview (captured 2026-09-16)]]