---
title: "Adyen sensitive-data protection routes"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/sensitive-data"
raw_files:
  - "adyen/docs/development-resources/security/sensitive-data/2026-09-15.md"
tags: [adyen, sensitive-data, encryption, tls, pgp]
---

## Overview

This [[adyen]] sensitive-data landing page tells integrators to protect sensitive information with encryption practices and routes to two distinct guides: TLS for data in transit and PGP for exchanging sensitive card data with Adyen. It is navigation and high-level responsibility framing, not a configuration specification, PCI compliance determination, or evidence that any integration protects data correctly. See [[adyen-api-access]] for the provider security-source route.

## Key takeaways

- The page says Adyen applies security practices to merchant data and systems, while the integrator also needs to protect sensitive information in its own integration.
- Its **Encryption in transit** entry names TLS/SSL for transmitted data and links to the TLS guide. The landing page itself gives no supported version, cipher, SNI, or certificate configuration; those details belong to the separately reviewed [[source-adyen-docs-development-resources-security-sensitive-data-tls|TLS source]].
- Its **PGP encryption** entry names generation and upload of a PGP key for sensitive-card-data exchange and links to the PGP guide. This entry alone does not describe key creation, registration steps, permitted exchange path, or whether a specific merchant can use it. The PGP raw route below is navigation only.
- The two named paths address different security tasks. Their presence here does not imply that both are required for every integration or that they establish PCI DSS compliance.

## Detail locators

- **Sensitive-data responsibility framing:** raw lines 15–21, under `# Protecting sensitive data`.
- **TLS transit and PGP card-data-exchange signposts:** raw lines 23–25.
- **Canonical next-step links:** raw lines 27–35, under `## Next steps`.

## Related

- [[adyen]]
- [[adyen-api-access]]
- [[source-adyen-docs-development-resources-security-sensitive-data-tls]]

## Related raw API references

- [[raw/adyen/docs/development-resources/security/sensitive-data/pgp-encryption/2026-09-15|PGP encryption guide — navigation only; raw not read for this entry]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/sensitive-data/2026-09-15|Adyen sensitive-data landing page — collected 2026-09-15]]
