---
title: "Braintree Risk and Security Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/overview"
raw_files:
  - "braintree/articles/risk-and-security/overview-2026-09-16.md"
tags: [braintree, risk, security, chargebacks, compliance, control-panel, underwriting]
---

## Overview

This collected Braintree article is an umbrella navigation page for payment risk and security. It routes merchants to five dedicated areas: chargebacks and retrievals, compliance, Control Panel security, risk factors, and underwriting. It identifies the merchant, Braintree teams, and Braintree as merchant-account provider as different actors; detailed procedures and obligations remain in the linked destination pages.

## Key takeaways

- The page characterizes chargebacks as a standard part of doing business, especially for online payments, and says the Disputes team helps merchants understand how to handle and minimize them. The linked chargeback guide owns the process details.
- Its compliance orientation extends beyond PCI DSS to Braintree-enforced requirements, governmental law, and other factors affecting the business. It positions the Compliance team as helping align the merchant's website, integration, and payment flow with applicable regulations; this overview is not a compliance specification or certification.
- The Control Panel is identified as a tool for reporting and managing payments. The page points to security tools and best practices but leaves their operation to the linked Control Panel security article.
- For fraud risk, the page assigns ultimate responsibility for protecting the business to the merchant. It describes the Risk team as providing guidance on credit risk and fraud trends and assistance investigating suspicious activity; it does not describe a guaranteed prevention or decision outcome.
- In its underwriting orientation, Braintree identifies itself as the merchant-account provider, says it collects information during onboarding to help prevent later processing interruptions, and describes continued account assistance as the business grows.

> [!warning] Suspected compromise
> The page directs a merchant who believes a Braintree integration may have been compromised to contact Braintree for assistance. Treat that as the captured escalation route, not proof that an incident was investigated or resolved.

> [!warning] Navigation and snapshot boundary
> This is a 2026-09-16 snapshot of a routing overview. The outbound links identify where to continue; they do not by themselves establish the linked pages' detailed procedures, obligations, eligibility, outcomes, or current behavior.

## Detail locators

- Chargeback context, Disputes-team role, and detailed-guide route: `## Chargebacks and retrievals`, raw lines 19-23.
- Compliance scope and Compliance-team role: `## Compliance`, raw lines 26-30.
- Control Panel identity and security route: `## Control Panel security`, raw lines 33-37.
- Merchant fraud-protection responsibility and Risk-team advisory role: `## Risk factors`, raw lines 40-44.
- Merchant-account-provider identity, onboarding information collection, and ongoing Underwriting-team assistance: `## Underwriting`, raw lines 47-51.
- Suspected-integration-compromise contact warning: `IMPORTANT`, raw lines 54-55.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Chargeback context: [[disputes]]
- Administration and security context: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/overview-2026-09-16|Braintree Chargebacks and Retrievals Overview]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/compliance/overview-2026-09-16|Braintree Compliance Overview]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys-2026-09-16|Braintree Rotating API Keys]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/risk-factors/mitigating-risk-2026-09-16|Braintree Mitigating Risk]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/underwriting/overview-2026-09-16|Braintree Underwriting Overview]] - linked navigation; not read as factual evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/overview-2026-09-16|Braintree Risk and Security Overview]] - complete collected snapshot providing the five-topic risk/security navigation map, team and merchant roles, and suspected-compromise escalation warning
