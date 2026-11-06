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

The 2026-11-03-captured merchant-credential Management API v3 generation endpoint says its new API key can be used a few minutes after generation and the old one stops working after 24 hours. Its response returns a generated key but does not prove successful downstream authentication. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-generateapikey]]

> [!warning] Contradiction
> This merchant-credential endpoint states a few minutes before new-key use, while the separate balance-platform Customer Area guide states immediate activation. The broad immediate-activation sentence above must be read as scoped to that guide, not universal across these routes. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-generateapikey]] [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]]


The 2026-09-15-captured balance-platform Customer Area guide says a newly generated API key becomes active immediately and its predecessor remains active for 24 hours. The separate 2026-11-03-captured Management API v3 company- and merchant-credential generation references say a new key can be used a few minutes after generation and the old key stops working after 24 hours. [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials-apicredentialid-generateapikey]] [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-generateapikey]] Basic-authentication password replacement instead deactivates the previous password immediately, so overlapping migration requires a separate credential. Live credentials must come from the live environment. IP allowlisting can restrict request origins, and a credential can be deactivated immediately and later reactivated but cannot be deleted.

These snapshot statements do not prove current merchant or user eligibility, successful authentication, endpoint access, correct secret storage, API availability, idempotent processing, or payment execution. Future authentication, role-catalog, idempotency, and API-security sources should extend this route without transferring their claims before review.



## Mutual authentication

Adyen's 2026-09-15 mTLS guide adds a client certificate to API-key authentication for supported APIs using a company-level API credential. The merchant keeps the private key, links the certificate subject DN to the credential, and presents the leaf plus full CA chain at an mTLS endpoint. Linking is a cutover: supported-API requests with that credential fail without the certificate. The guide excludes merchant-level and balance-platform credentials and identifies separate supported/unsupported APIs and endpoints; see the source for scope and regions. This TLS client certificate is distinct from the JWE card-encryption certificate, whose retained EC/RSA sample conflict remains unresolved.
## Sources

- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins-originid]] — 2026-11-05-captured Management API v3 TEST detail read of one merchant-credential allowed origin; the role-gated resource readback does not demonstrate browser client-key acceptance or payment authorization.

> [!warning] Contradiction
> This reference lists a TEST `/v3` server, but its `200` example self-link uses `/v1/merchants/...`. The capture does not establish the correct versioned self-link or Live route. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins-originid]]


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-apicredentials-apicredentialid-allowedorigins-originid]] — 2026-11-05-captured Management API v3 TEST deletion of an allowed origin under a merchant API credential; the reference says client-side requests from that domain stop being accepted immediately after removal, while 204 returns no resource readback.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]] — 2026-11-05-captured Management API v3 TEST POST to add a domain allowed origin for a merchant-path API credential; the required API-credentials read/write caller role and 200/204 configuration result do not prove later client authentication or payment acceptance.

> [!warning] Contradiction
> The reference lists a TEST `/v3` server, while its `200` example allowed-origin self link uses `/v1`. The example does not resolve the version mismatch. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]] — 2026-11-03-captured Management API v3 TEST read of allowed origins for a merchant-path API credential, requiring API-credentials read/write permission; readback does not add an origin or prove client acceptance.

> [!warning] Contradiction
> This reference lists a TEST `/v3` server, but both 200 sample origin links use `/v1`. The captured example does not resolve current routing. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid-allowedorigins]]


- [[source-adyen-api-explorer-management-latest-delete-companies-companyid-apicredentials-apicredentialid-allowedorigins-originid]] — 2026-11-03 Management API v3 TEST deletion of an allowed origin under a company API credential; the reference says client-side requests from that domain stop being accepted immediately after removal, while 204 has no resource readback.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid-allowedorigins-originid]] — 2026-11-03-captured Management API v3 TEST credential-scoped allowed-origin detail read; configuration visibility is not client-side acceptance or payment proof.

> [!warning] Contradiction
> This reference lists a `/v3` TEST server, but its 200 example self link uses `/v1/companies/`. The example establishes neither the v3 self-link route nor the correct Live route.


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials-apicredentialid-allowedorigins]] — 2026-11-03-captured Management API v3 TEST creation of a domain allowed origin for a company API credential; `200` is a configuration result, not client authentication or payment proof, and its example self-link uses `/v1` despite the listed `/v3` server.

> [!warning] Contradiction
> The allowed-origin POST reference lists a `/v3` TEST server but illustrates a `/v1` response self-link. The example does not resolve the version mismatch. [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials-apicredentialid-allowedorigins]]


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid-allowedorigins]] — 2026-11-03-captured Management API v3 TEST list of allowed origins for a company-path API credential, requiring API-credentials read/write; optional `data` readback is not origin propagation or client-key use proof.
> [!warning] Contradiction
> This source lists a `/v3` TEST server, but both `200` example origin self links use `/v1`; the page does not reconcile the version difference. [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid-allowedorigins]]


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials-apicredentialid-generateclientkey]] — 2026-11-03-captured Management API v3 TEST merchant-credential client-key generation; new key usable after a few minutes, old key stops after 24 hours, and 200/204 do not prove successful client authentication.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid]] — 2026-11-03-captured Management API v3 TEST merchant-credential GET, requiring API credentials read/write on the caller and returning target credential status, roles, IP list, client key and links; readback does not rotate keys or prove endpoint access.

> [!warning] Contradiction
> The reference lists a `/v3` TEST server, while its `200` example's resource hrefs all use `/v1`. The example establishes neither the v3 self-link route nor the correct Live route. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials-apicredentialid]]


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials-apicredentialid-generateclientkey]] — 2026-11-03-captured Management API v3 TEST company/target-credential client-key generation reference: required credential role, a few-minute new-key usability delay and 24-hour old-client-key expiry; generation is distinct from API-key rotation or payment readiness.


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials-apicredentialid-generateapikey]] — 2026-11-03-captured Management API v3 TEST POST for a new company-path credential API key, requiring API-credentials read/write; the 200 key is not proof of authentication or payment execution.

> [!warning] Contradiction
> This API endpoint says the new key can be used a few minutes after generation, while [[source-adyen-docs-development-resources-api-credentials]] says a newly generated key becomes active immediately. Both describe a 24-hour previous-key window; the new-key timing remains unresolved for this route.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-apicredentials-apicredentialid]] — 2026-11-03-captured Management API v3 TEST merchant-credential PATCH for active state, origins, roles, description or subject DN, requiring the API-credentials read/write role; `200` readback or `204` is not later authentication or payment proof.
> [!warning] Contradiction
> This source lists a `/v3/merchants/.../apiCredentials/...` PATCH, while the `200` sample links that credential under `/v1/companies/.../apiCredentials/...`; the example does not establish the PATCH route. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-apicredentials-apicredentialid]]


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials]] — 2026-11-03-captured Management API v3 TEST merchant-path API credential creation, optional roles/origins and secret/IP response fields; account-scope wording and /v1 example links conflict with the path and server, while creation does not prove live authentication.

> [!warning] Contradiction
> The pinned POST /merchants/{merchantId}/apiCredentials introduction calls the path a company account, while its path table defines merchantId as a merchant-account ID. The listed TEST server is /v3, but the 200 example includes company-scoped /v1/companies/.../apiCredentials links alongside a merchant link. The snapshot does not reconcile account scope or the versioned route for later calls. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-apicredentials]] — 2026-11-03-captured Management API v3 TEST, role-gated merchant API-credential list with paging, public client-key, role, active and IP/origin readback; listing does not generate an API key or prove usable Live access.

> [!warning] Contradiction
> This source lists a TEST v3 server while its example pagination and credential links use v1. Those illustrative links do not resolve the v3 resource-link path.


- [[source-adyen-api-explorer-management-latest-patch-companies-companyid-apicredentials-apicredentialid]] — 2026-11-03-captured Management API v3 TEST PATCH for company API-credential settings, with role delegation limited by the company web-service credential and explicit merchant IDs distinct from company-wide access; updated readback is not key generation or downstream authorization proof.

> [!warning] Contradiction
> This reference lists a `/v3` test server, but its response-example resource links use `/v1`. The snapshot does not reconcile the base-path difference. [[source-adyen-api-explorer-management-latest-patch-companies-companyid-apicredentials-apicredentialid]]


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid]] — 2026-11-03-captured Management API v3 TEST readback of a company-path API credential's status, IPs, roles, client key and scope; response values do not prove successful authentication or payment.

> [!warning] Contradiction
> This credential GET lists a /v3 TEST server, but its 200 example resource links use /v1. The sample cannot resolve current routing. [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials-apicredentialid]]


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials]] — 2026-11-03-captured Management API v3 TEST paged read of a company's API-credential metadata and explicit merchant scope; listing and key-generation links are not key rotation or successful access, and the example links use `/v1` despite the listed `/v3` server.

> [!warning] Contradiction
> This listing reference names the TEST `/v3` server, while its response example uses `/v1` pagination and credential links. The example does not resolve the version mismatch. [[source-adyen-api-explorer-management-latest-get-companies-companyid-apicredentials]]


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-apicredentials]] — 2026-11-03-captured Management API v3 TEST company-credential creation reference for optional merchant scope, roles and origins, returned secrets and one-time API-key retrieval boundary; creation is not proof of endpoint access or payment execution.

> [!warning] Contradiction
> The reference lists a `/v3` TEST server, but its 200 example credential, origin and generate-key links use `/v1/`. The example establishes neither v3 links nor correct Live routes.


- [[source-adyen-api-explorer-management-latest-delete-me-allowedorigins-originid]] — 2026-11-03-captured Management API v3 TEST DELETE for an allowed-origin ID under the request API key's credential, permitting any Management API role; `204` has no success body and does not establish propagation or browser acceptance.


- [[source-adyen-api-explorer-management-latest-get-me]] — 2026-09-15-captured Management API v3 TEST `GET /me` reference for reading the API-key-associated credential's identity, roles, active flag, IP restrictions and client-side settings; resource links are not merchant-account management or key rotation.


- [[source-adyen-api-explorer-management-latest-get-companies]] — 2026-09-15-captured Management API test-server company-account list scoped to credential access and Account read role, with pagination and company-status meanings; response sample uses older /v1 links than the listed /v3 server.


- [[source-adyen-api-explorer-management-latest-post-me-generateclientkey]] — 2026-09-15-captured Management API v3 TEST client-key generation reference requiring an API credential with Management API credentials read/write role; new client key usable after a few minutes and old client key expires after 24 hours, separate from API-key rotation.


- [[source-adyen-api-explorer-management-latest-post-me-allowedorigins]] — 2026-09-15-captured Management API v3 TEST reference for adding an allowed origin to the API credential identified by the request API key; exact origin syntax and propagation are outside this endpoint capture.


- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins]] — 2026-09-15-captured Management API v3 TEST GET reference for allowed origins of the API-key-selected credential; any Management API role can read, and the response does not create an origin or establish client-key/payment acceptance.

- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins-originid]] — 2026-11-03-captured Management API v3 TEST GET for one allowed-origin domain/ID under the request-API-key-selected credential; any Management API role can read, without proving client-key acceptance or payment authorization.



- [[source-adyen-api-explorer-management-latest-overview]] — 2026-09-15-captured Management API v3 overview for API-key and test/live endpoint orientation plus company, merchant, store and terminal route catalog; operation details remain in separate references.


- [[source-adyen-api-explorer-checkout-latest-post-originkeys]] — 2026-09-15-captured Checkout API v72 test-server `POST /originKeys` contract for domain-to-origin-key creation, with client-key migration recommendation; no live availability or migration proof.


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
