---
title: "Braintree Standalone Credit Card Verification Create (Node.js Route)"
type: source
date_ingested: 2026-10-08
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card-verification/create/node"
raw_files:
  - "braintree/docs/reference/request/credit-card-verification/create/node-2026-09-16.md"
tags: [braintree, node-js, credit-card-verification, vault, pci-compliance]
---

## Overview

This collected Braintree Node.js-routed request reference describes a standalone credit-card verification that does not store the card in the Vault. Its short body states the raw-card-data and PCI-environment condition and points uncertain readers toward standard card verification with vaulting. This is verification guidance, not a sale, authorization, settlement or funding operation.

## Key takeaways

- The page says a standalone credit-card verification can be performed without storing the card in the Vault.
- That no-storage path requires passing raw credit-card data, which the page says should be done only in a PCI-compliant environment.
- If in doubt, the page directs the reader toward standard card verification and vaulting the card. The captured sentence is damaged around the link, so it does not supply a reliable method name, request schema or executable example.

> [!warning] PCI and evidence boundary
> Preserve the provider's condition: the standalone no-storage path passes raw card data and should only be used in a PCI-compliant environment. This 2026-09-16 snapshot is an unversioned Node.js website route, not proof of an exact `braintree` package/version, current compliance, merchant enablement, successful verification or any payment lifecycle outcome.

## Detail locators

- Document identity: `# Credit Card Verification: Create`, raw line 13.
- Standalone verification without Vault storage: raw line 15.
- Raw-card-data and PCI-compliant-environment condition: raw line 16.
- Damaged fallback direction to standard card verification and vaulting: raw line 16.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Related response reference: [[source-braintree-docs-reference-response-credit-card-verification-node]]

## Related raw API references

- [[raw/braintree/docs/guides/credit-cards/server-side/node-2026-09-16|Braintree credit-cards server-side Node.js guide]] - navigation-only destination of the captured standard-card-verification link; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card-verification/create/node-2026-09-16|Braintree standalone credit-card-verification create reference - Node.js route]] - complete collected page containing the no-storage capability, raw-card-data PCI condition and damaged fallback direction
