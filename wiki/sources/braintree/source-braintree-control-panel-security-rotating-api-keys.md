---
title: "Braintree Control Panel Rotating API Keys"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys"
raw_files:
  - "braintree/articles/risk-and-security/control-panel-security/rotating-api-keys-2026-09-16.md"
tags: [braintree, control-panel, api-keys, credential-rotation, account-security]
---

## Overview

This collected Braintree article is a retrieval guide for rotating a Control Panel user's API keys after possible exposure or compromise. It documents the overlapping-validity cutover, the page's per-user Control Panel generation route and the required confirmation before old keys are deleted; it concerns API credential handling, not customer payment authentication.

## Key takeaways

- The page compares API keys to a username and password and recommends generating new keys whenever there is any chance of exposure or compromise, including after a developer leaves or keys are sent in email.
- Generating new keys does not revoke the old ones: the old keys continue to work until they are deleted. The article presents that overlap as the way to rotate without customer downtime.
- The guide says the new key set is "for your user" and routes generation through the Control Panel's **API Keys** section. It does not state which Control Panel roles or permissions can perform the action.
- After generation, the documented sequence is to update the code with the new values, confirm the new keys work as expected and only then delete the old keys.

## Evidence boundary

> [!warning] Replacement is not revocation
> Do not treat new-key generation as disabling the previous keys: this page says the old keys remain usable until deletion. Do not delete them until the new values have been updated in code and confirmed working. This collected page does not disclose credential values or document role eligibility, Control Panel login authentication, payment authentication, 3D Secure or transaction fraud screening.

## Detail locators

- Credential sensitivity and rotation triggers: `# Rotating API Keys`, line 16.
- Overlapping old/new key validity and stated no-downtime purpose: `# Rotating API Keys`, line 18.
- Do-not-delete-before-confirmation warning: `# Rotating API Keys > IMPORTANT`, lines 21-22.
- Per-user Control Panel generation route: `# Rotating API Keys`, lines 26-33.
- Code update, confirmation and old-key deletion sequence: `# Rotating API Keys`, line 35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Related credential inventory: [[source-braintree-control-panel-important-gateway-credentials]]

## Related raw API references

- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree Important Gateway Credentials]] - navigation-only credential inventory linked by this article; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys-2026-09-16|Braintree Control Panel Rotating API Keys]] - complete collected article covering exposure-driven rotation, overlapping key validity, the per-user Control Panel route and safe deletion order
