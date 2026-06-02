---
title: "PayPal Security Guidelines for Developers"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "paypal-security-guidelines-2025.md"
tags: [paypal, security, oauth, tls, pci-dss, webhooks, credentials, csp]
---

## Summary

Comprehensive security guidelines for PayPal API and SDK integrations. Covers general principles, integration-specific requirements, OAuth token examples in 7 languages, webhook signature verification, and a security tools reference.

## Key Takeaways

- **Never expose client secret client-side** — server-side only
- **TLS 1.2+ required** — PayPal does not support older protocols
- **Validate every webhook signature** before processing events
- **Principle of least privilege** — separate credentials per environment/role
- **SDK**: load only from official PayPal CDN; use CSP + SRI headers; validate payment events server-side before fulfilling orders
- **Webhook verification**: use `paypal-transmission-sig` + cert from `paypal-cert-url` + SHA256 hash of `transmission_id|timestamp|webhook_id|sha256(body)`

## 12 General Security Principles

1. OAuth 2.0 for all API auth
2. HTTPS everywhere (required for PCI DSS)
3. Never expose client secret in client-side code
4. Store credentials in env vars or secure vaults (not source code)
5. Rotate credentials regularly; remove unused ones
6. Validate all webhook signatures
7. Keep all dependencies/SDKs up to date
8. TLS 1.2 or higher
9. Enable 2FA on PayPal account
10. Monitor and log all payment/API activity
11. Principle of least privilege
12. Never log access tokens or payment details

## Integration-Specific Requirements

### API path
OAuth 2.0 + HTTPS + server-side credentials + webhook validation + TLS 1.2 + 2FA + monitoring + no sensitive logging

### SDK path
Load from official PayPal CDN only; CSP + SRI headers; validate all payment events server-side before fulfilling; never include secrets in client-side code

### Webhook path
Always validate signature; never trust without verification; HTTPS endpoints; log all activity for auditing

## Security Tools Reference

| Tool | Purpose |
| --- | --- |
| OAuth 2.0 | Secure API authentication |
| Webhook signature verification | Validate event authenticity |
| TLS | Secure data in transit |
| API credential management (Developer Dashboard) | Manage/rotate keys |
| JavaScript SDK | Secure client-side integration |
| Fraud detection tools | Prevent/detect fraud |

## Related Pages

- [[paypal]] — company page
- [[paypal-fraud-risk]] — PayPal fraud & risk tools
- [[source-paypal-rest-api-get-started]] — OAuth token setup, credentials

## Raw Sources

- [[paypal-security-guidelines-2025]] — full security guidelines: 12 principles, OAuth examples in 7 languages, webhook verification (Python), SDK CSP/SRI requirements, security tools table
