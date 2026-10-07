---
title: "Braintree IP Addresses and Firewall Allowlisting"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/braintree-ip-addresses"
raw_files:
  - "braintree/docs/reference/general/braintree-ip-addresses-2026-09-16.md"
tags: [braintree, ip-addresses, domains, allowlisting, firewall, production, sandbox]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website reference describes merchant/server security-policy and firewall allowlisting for requests from a merchant server to Braintree production or Sandbox destination domains and their IP ranges. The page characterizes allowlisting as an additional control on top of SSL and warns that incomplete rules can prevent payment processing, but the IP inventory can change: this snapshot and its domain lists are not a current-IP guarantee, an inbound Braintree-origin allowlist, merchant-specific network configuration, proof of request authenticity or broader security, or evidence of connectivity or payment success. Use [[braintree-payment-platform]] for the provider-level route.

## Key takeaways

- The documented direction is a request from the merchant's server to a Braintree server. The merchant applies allowlisting when its own security policy would otherwise prevent access; the page does not document Braintree-to-merchant inbound source addresses.
- Incorrectly allowlisting the Braintree domain names and IP addresses can leave the merchant unable to process payments. This is a connectivity warning, not evidence that allowlisting alone makes a payment path available or secure.
- The reference separates Production and Sandbox fully qualified domain names and says each environment's names may resolve to ranges and addresses in the linked `ips.json`; environment-specific domain lists and IP-range routes should not be interchanged.
- Braintree says its IP addresses are subject to change and recommends watching `ips.json`. Therefore the addresses represented by a collected snapshot, cached DNS answer or earlier firewall rule are not guaranteed to be current.

> [!warning] Allowlist ownership and time boundary
> Apply this page only to the merchant-managed server/firewall path and the intended Braintree environment. Revalidate the provider-published `ips.json` and destination domains through an authorized operational process before changing rules; this collected page does not specify a polling interval, change-overlap window, ports, protocols, DNS behavior, rollback procedure, or a complete security control set.

## Detail locators

- Allowlist purpose, merchant-server-to-Braintree direction and additive-to-SSL framing: `# Braintree IP Addresses`, raw line 16.
- Operational overhead and payment-processing failure warning: `# Braintree IP Addresses`, raw line 18.
- `ips.json` download route, changing-address warning and watch recommendation: `# Braintree IP Addresses`, raw lines 20-22.
- Production fully qualified domain names and production range/address route: `## Braintree production domains` through `## Braintree production IP addresses`, raw lines 25-38.
- Sandbox fully qualified domain names and sandbox range/address route: `## Braintree sandbox domains` through `## Braintree sandbox IP addresses`, raw lines 39-52.

## Related

- Company: [[braintree]]
- Concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/reference/general/braintree-ip-addresses-2026-09-16|Braintree IP Addresses reference]] - complete collected webpage covering allowlist purpose, server-to-Braintree direction, payment-connectivity warning, changing-address notice, and separate Production and Sandbox domain/IP routes
