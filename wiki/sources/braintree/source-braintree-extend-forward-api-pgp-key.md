---
title: "Braintree Forward API PGP Public Key"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/pgp-key"
raw_files:
  - "braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, pgp, encryption]
---

## Overview

This collected unversioned Braintree guide is a retrieval page for the PayPal Braintree Forward API PGP public key. It says the key is needed to encrypt secrets sent during communication with the Forward API team. The raw was fetched on 2026-09-16, and its embedded metadata records creation and update timestamps on 2025-04-02. Production use of the Forward API is subject to eligibility; the page directs readers to an Account Manager or the Business Development inquiry route.

## Key takeaways

- The snapshot identifies the key name as **PayPal Braintree Forward API**, with the contact address `forward-api@getbraintree.com`.
- It identifies a 4096-bit RSA PGP public key with key ID `D26C77FA` and fingerprint `8BE6 69D2 D1ED 9DCA B4B5 E0E8 85D1 D4A4 D26C 77FA`.
- The complete armored public-key block is retained in the raw locator rather than duplicated here.
- The page does not state an expiration date, rotation schedule, revocation status or a method for establishing current trust. This collected snapshot therefore does not by itself establish that the key remains current or trusted, that encrypted material was delivered or accepted, or that any forwarded request or payment outcome occurred.

## Evidence boundary

> [!warning] Snapshot identity is not current-key validation
> Use the recorded fingerprint and displayed key identity only as facts from the 2026-09-16 collected snapshot. The page's wording is specifically about encrypting secrets sent during communication with the Forward API team, and production Forward API use remains eligibility-gated.

## Detail locators

- Source URL, fetch date and discovery provenance: raw lines 1-3.
- Page title and embedded create/update timestamps: frontmatter, raw lines 5-10.
- Encryption purpose and production-eligibility qualification: `# PGP Public Key`, raw lines 14-18.
- Key name/identity, contact, type, key ID, length, algorithm and fingerprint: raw lines 20-29.
- Complete armored public-key block: fenced block, raw lines 31-84.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]
- Related cryptography source: [[source-braintree-extend-forward-api-cryptography]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] — unread navigation-only destination for the eligibility link; not used as behavioral evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16|Braintree Forward API PGP Public Key]] — complete collected retrieval page for the encryption purpose, eligibility notice, key name/identity and contact, fingerprint, metadata dates and armored public-key block
