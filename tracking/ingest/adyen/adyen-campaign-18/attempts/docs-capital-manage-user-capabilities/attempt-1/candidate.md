---
title: "Adyen Capital user capability management"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/manage-user-capabilities"
raw_files:
  - "adyen/docs/capital/manage-user-capabilities/2026-09-15.md"
tags: [adyen, capital, platforms, capabilities, verification]
---

## Overview

This 2026-09-15 Adyen Capital guide explains how a platform requests, views, enables, and disables an account holder's Capital capabilities. The two named capabilities are `getGrantOffers` and `receiveGrants`. Capability states govern eligibility and access to later offer and grant steps; requesting, allowing, or enabling one is not itself an offer accepted, funds disbursed, or a grant repaid.

## Key takeaways

- Each user is represented by an account holder in the balance platform. The guide says Adyen usually configures Capital capabilities during integration design so new account holders are automatically requested, while the platform may request later or enable/disable for individuals. Prerequisites are Adyen for Platforms with Capital enabled, a supported user country/region, Adyen setup, and compliance/verification guidance. API management requires a Balance Platform API key with **Balance Platform BCL role**; Customer Area management requires **Manage account holder capabilities**.
- `getGrantOffers` permits eligibility evaluation for financing offers based on payment-processing volume. Adyen generates offers when the user qualifies and the capability is **allowed**. `receiveGrants` relates to receiving financing; requesting it prompts Adyen to check whether the account holder signed Terms of Service. When terms have been signed and **both capabilities are allowed**, the guide says the platform can proceed to the separate disbursement request. An allowed flag does not itself establish an issued offer, accepted terms, or completed grant transfer.
- A platform can request either capability in Customer Area or with Configuration API `PATCH /accountHolders/{id}` setting that capability's `requested=true`. Customer Area submission sends the request to Adyen for approval. The example API response shows `requested=true`, `allowed=false`, `verificationStatus=pending`: these states must not be collapsed into approval. The test API URL and sample account-holder ID are illustrative.
- To inspect account-holder capabilities, use Customer Area or Configuration API `GET /accountHolders/{id}`. The response distinguishes `allowed` (whether Adyen allows it), `enabled` (whether the user can use it), `verificationStatus` (`invalid`, `pending`, `rejected`, or `valid`), and a `problems` array for errors to address. Those fields describe capability and checks at read time, not Capital offer terms or funding status.
- The platform can enable or disable a capability in Customer Area or by `PATCH /accountHolders/{id}` with `enabled=true/false`. The disable example returns `enabled=false` while `allowed=true` and verification remains `valid`, demonstrating independent switches. A disable action should not be interpreted as revoking an existing grant or settling any financing obligation; those are separate lifecycles.

## Detail locators

- Opening and `## Requirements`: account-holder model, enabled Capital integration, roles, region and setup/compliance prerequisites.
- `## Capital capabilities`: getGrantOffers versus receiveGrants and Terms of Service gate.
- `## Request a capability`: Customer Area approval request and Configuration API requested=true with pending example.
- `## View capabilities`: GET/Customer Area and allowed/enabled/verification/problems fields.
- `## Enable or disable a capability`: user-facing and API control plus allowed-but-disabled example.

## Related

- [[adyen-capital]] — main Capital product concept.
- [[adyen-platforms]] — parent platform context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/manage-user-capabilities/2026-09-15|Adyen Capital manage user capabilities (fetched 2026-09-15)]]
