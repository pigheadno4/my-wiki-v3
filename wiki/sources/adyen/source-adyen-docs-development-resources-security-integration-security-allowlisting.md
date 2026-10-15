---
title: "Adyen network allowlisting guidance"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/integration-security/allowlisting"
raw_files:
  - "adyen/docs/development-resources/security/integration-security/allowlisting/2026-09-15.md"
tags: [adyen, integration-security, allowlisting, dns, webhooks]
---

## Overview

This [[adyen]] integration-security guide covers network allowlisting for connections from the merchant to Adyen endpoints and connections from Adyen to merchant systems such as webhook receivers. It applies to all Adyen integration types when the merchant uses or plans network allowlisting. The page says unrestricted outbound requests are compatible with Adyen; allowlisting is a merchant network policy choice, not a prerequisite for every integration. Use [[adyen-api-access]] for the broader API access context, while keeping this network guidance distinct from a credential's origin restrictions.

## Key takeaways

- Adyen recommends DNS resolution with domain-based allowlisting for merchant-to-Adyen connections because Adyen's underlying IP addresses change. The snapshot names `adyen.com` and `adyenpayments.com` as top-level domains; filtering by static resolved IPs needs continuing maintenance, and the page says not to use custom DNS records or hardcoded IPs because of SNI and address-rotation failure risks.
- For outgoing merchant requests to Adyen, the page lists endpoint IP ranges but instructs merchants to **always rely on DNS** for the destination endpoint. The ranges are a 2026-09-15 snapshot, not a current complete set or a substitute for endpoint DNS; Adyen can change endpoint IPs within ranges.
- For incoming traffic to the merchant, such as webhooks sent by Adyen, a restrictive firewall may need Adyen's outgoing IPs. The guide strongly recommends dynamic DNS-based allowlisting and gives `dig +short out.adyen.com` to resolve current addresses. Merchant-to-Adyen endpoint ranges and Adyen-to-merchant source addresses have opposite network directions and should not be interchanged.
- Geo-IP based regional blocks can mistakenly reject Adyen connectivity because geographic mappings may be unreliable. The page advises explicitly allowlisting Adyen domains and ranges to avoid those false positives. It does not provide a test-versus-live IP split or region-specific allowlist and does not prove a particular firewall configuration, endpoint reachability, or webhook delivery.

## Detail locators

- **Applicability and optional security-policy context:** raw lines 15–29, under `# Allowlisting IP addresses` and `## Requirements`.
- **Method comparison and DNS/domain recommendation:** raw lines 31–63, including `## DNS resolution and domain-based allowlist` and `## DNS resolution and IP allowlist`.
- **Custom DNS/SNI and hardcoded-IP failure warnings:** raw lines 65–78, under `## Custom DNS record` and `## Hardcoded IP addresses`.
- **Merchant-to-Adyen endpoint CIDR snapshot and mandatory DNS reliance:** raw lines 80–100, under `### Outgoing IP allowlisting (from you to Adyen)`.
- **Adyen-to-merchant webhook source resolution:** raw lines 102–116, under `### Incoming IP allowlisting (from Adyen to you)`; `out.adyen.com` command at line 113.
- **Geo-IP regional blocking warning:** raw lines 118–124, under `### Geo-IP-based firewalls and regional blocking`.

## Related

- [[adyen]]
- [[adyen-api-access]]
- [[adyen-webhooks]]
- [[source-adyen-docs-development-resources-live-endpoints]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/integration-security/allowlisting/2026-09-15|Adyen allowlisting guidance — collected 2026-09-15]]
