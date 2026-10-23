---
title: "Adyen API Access"
type: concept
category: technology
tags: [adyen, api-credentials, authentication, access-control]
---

## Definition

Adyen web service API credentials identify an integration for API requests. A credential combines a username, authentication secret, enabled roles, and an account scope; together these determine which account context and permitted operations the credential can reach. This is a provider-wide access route, separate from endpoint-specific authorization, idempotency, and payment lifecycle behavior.

## Access boundaries

Roles define credential permissions. Account scope defaults to company-wide access, including linked merchant accounts, when the credential is created on a company account, while a credential created on a merchant account is limited to that merchant account; company-level configuration can instead select particular account groups and merchant accounts. More credentials can narrow permissions across channels or systems but increase key-management overhead.

## Credential lifecycle

A newly generated API key is active immediately while its predecessor remains active for 24 hours by default. Basic-authentication password replacement instead deactivates the previous password immediately, so overlapping migration requires a separate credential. Live credentials must come from the live environment. IP allowlisting can restrict request origins, and a credential can be deactivated immediately and later reactivated but cannot be deleted.

These snapshot statements do not prove current merchant or user eligibility, successful authentication, endpoint access, correct secret storage, API availability, idempotent processing, or payment execution. Future authentication, role-catalog, idempotency, and API-security sources should extend this route without transferring their claims before review.



## Mutual authentication

Adyen's 2026-09-15 mTLS guide adds a client certificate to API-key authentication for supported APIs using a company-level API credential. The merchant keeps the private key, links the certificate subject DN to the credential, and presents the leaf plus full CA chain at an mTLS endpoint. Linking is a cutover: supported-API requests with that credential fail without the certificate. The guide excludes merchant-level and balance-platform credentials and identifies separate supported/unsupported APIs and endpoints; see the source for scope and regions. This TLS client certificate is distinct from the JWE card-encryption certificate, whose retained EC/RSA sample conflict remains unresolved.
## Sources

- [[source-adyen-docs-development-resources]] — 2026-09-15 Development resources landing page for integration-type selection, credentials, libraries, webhooks, examples and AI/documentation links; navigation only.


- [[source-adyen-docs-payouts-payout-service-manage-access-api-credentials-web-service]] — 2022-modified, 2026-09-15-captured Payout Service balance-platform web service credential guide covering company-level setup, roles, test/live keys, rotation and deactivation; access documentation only.


- [[source-adyen-docs-account-user-roles]] — 2026-09-15 Customer Area user-role catalog for human permissions and role-group assignment, including API-credential management; distinct from an API credential's own roles and account scope.


- [[source-adyen-docs-development-resources-security-sensitive-data]] — sensitive-data security landing page routing TLS transmission and PGP card-data-exchange guides, without configuration or compliance proof (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-mcp-server]] — locally run MCP server guide for credentialed Checkout and Management API tool calls, with role, endpoint-inventory and test/live configuration boundaries (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-client-side-authentication-migrate-from-origin-key-to-client-key]] — dated Web/iOS/Android origin- or public-key to client-key migration guide with version thresholds, credential and allowed-origin setup, environment scope, and old-key coexistence (2026-09-15 snapshot; raw last modified 2020).


- [[source-adyen-docs-development-resources-security-sensitive-data-tls]] — transport TLS version, cipher, SNI and certificate-rotation guidance, with existing/new integration split and conditional root-pinning exception (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-security-integration-security-allowlisting]] — network allowlisting guide for merchant-to-Adyen API endpoints and Adyen-to-merchant webhook traffic, with DNS rotation and Geo-IP cautions (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-client-side-authentication]] — 2026-09-15 client-key guide for public client-side credential identity, version-qualified SDK support, environment-bound allowed origins, and client-key rotation; API requests use a separate API key.


- [[source-adyen-docs-development-resources-security]] — 2026-09-15 security-resources landing page routing integration security, IAM, secure coding, API security, sensitive-data and incident guides; category navigation only.


- [[source-adyen-docs-development-resources-mtls]] — 2026-09-15 Adyen webpage guide to company-credential mTLS enrollment, certificate linking, supported APIs and endpoint routes, and the post-link certificate requirement.


- [[source-adyen-docs-development-resources-api-authentication]] — unversioned documentation snapshot for API-key and Basic request-header authentication, including library-managed versus direct-call responsibility

- [[source-adyen-docs-development-resources-security-api-security]] — unversioned guidance snapshot for API authentication, rate limiting and throttling, HTTPS/TLS, and security testing; guidance only, not a complete security standard or provider-runtime proof

- [[source-adyen-docs-development-resources-live-endpoints]] — unversioned live-endpoints documentation snapshot for test/live endpoint structure, company-specific URL prefixes, regional configuration matching, and network connection guidance

- [[source-adyen-docs-development-resources-api-credentials-roles]] — unversioned documentation snapshot for role-based API credential permissions, company credential delegation, frequently used payment and Management API role locators, and PCI/Support qualifications

- [[source-adyen-docs-development-resources-api-credentials]] — unversioned documentation snapshot for web service credential identity, permission and account scope, environment separation, rotation, IP restriction, and deactivation
