---
title: "Braintree Apple Pay Configuration for JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/configuration/javascript/v3"
raw_files:
  - "braintree/docs/guides/apple-pay/configuration/javascript/v3-2026-09-16.md"
tags: [braintree, apple-pay, javascript-v3, web-payments, domain-registration]
---

## Overview

This collected [[braintree]] website guide is the JavaScript v3 configuration route for Apple Pay on the web. It says configuration finishes with environment-appropriate iCloud account setup and registration of every web domain planned for Apple Pay use. It is a dated setup snapshot linked from [[braintree-apple-pay]], not native iOS provisioning, current merchant or device eligibility, or evidence of a completed payment.

## Key takeaways

- Testing requires an iCloud account corresponding to the environment: the page calls for an iTunes Connect sandbox tester account in sandbox and a production iCloud account in production.
- Each domain intended for Apple Pay on the web must be registered with Apple through the Braintree Control Panel or the linked registration API route. The page explicitly says not to register the domain through the Apple Developer Portal.
- For Apple Pay on the web in this Braintree route, the page says a merchant does not need to generate and upload a Payment Processing Certificate because transactions use Braintree's shared certificate. This qualification is web-specific and must not be carried over to native iOS provisioning.
- Sandbox and production domains are entered separately and must exactly match the fully qualified domain name, including `www` when applicable. Production additionally requires hosting the domain-association file at `/.well-known/apple-developer-merchantid-domain-association` before the domain is added.
- For production verification, the page requires the association file to avoid 3xx redirects, be served over HTTPS 1.1, return as a binary object rather than HTML or plain text, use `Content-Type: application/octet-stream`, and remain accessible outside a firewall.

## Detail locators

- Page purpose and two remaining configuration areas: raw lines 14-16.
- Sandbox versus production iCloud accounts: `## iCloud account setup`, raw lines 17-19.
- Optional `apple-touch-icon` recommendation: `## Specify an icon`, raw lines 20-22.
- Web-domain registration routes, Apple Developer Portal exclusion and Braintree shared-certificate qualification: `## Domain registration`, raw lines 23-25.
- Sandbox Control Panel path and exact fully qualified domain-name matching: `### Sandbox environment`, raw lines 26-40.
- Production Control Panel path, exact domain matching and domain-association file location: `### Production environment`, raw lines 43-58.
- Apple's production verification request conditions, binary response media type and firewall-access qualification: raw lines 60-68.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-apple-pay]]

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/configuration/javascript/v3-2026-09-16|Braintree Apple Pay configuration - JavaScript v3]] - complete collected web configuration page for iCloud environment alignment and Apple Pay domain registration
