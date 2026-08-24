---
title: "Metronome Security Principles"
type: concept
category: framework
tags: [metronome, security, zero-trust, least-privilege]
---

## Definition

Metronome describes its security practices through three platform principles: least privilege, zero-trust architecture, and avoiding access based on long-lived credentials or static configuration.

## Access model

Access is denied until explicitly granted and can be controlled at field level. Metronome says this applies to both human and system actors so they receive only the data and capabilities required for their task.

## Authenticated service communication

Metronome exposes a bearer-authenticated `GET /v1/services` registry for security allowlisting and firewall configuration. A successful response requires a `services` array; each item requires string `name`, enum `usage` (`makes_connections_from` or `accepts_connections_at`), and string-array `ips`. The page says new IPs typically appear 30 days or more before first use, but it defines neither the IP-string notation nor polling, freshness, removal, failure-recovery, protocol, port, environment, or directional-perspective semantics. Registry membership is not documented as message authentication or as a replacement for webhook signature verification.

Communication between systems, or between an actor and a system, is authenticated. The documentation describes forwarding the same security token through downstream service calls so that each service can independently verify the request and grant the relevant access.

Metronome's operational allowlisting guide tells customers to poll `getServices`, apply returned IPs through their own security tooling, automate updates, test the configuration, and retain a change log. It warns that stale rules can deny access as IPs rotate, which establishes a fail-closed availability risk but not an updater algorithm: the guide supplies no polling interval, freshness marker, removal or overlap period, atomic-update or rollback procedure, or behavior for retrieval, parsing, or rule-deployment failures. It also does not map the registry's named services or `makes_connections_from` and `accepts_connections_at` labels to a particular firewall direction. The guide says new IPs appear at least 30 days before first use, whereas the endpoint reference says they typically appear 30 or more days before use; preserve this difference in guarantee strength and do not turn it into a universal notice or removal SLA. IP allowlisting remains an additional layer to use with controls such as SSO and scoped RBAC, not documented proof of request authenticity.

## Credential lifetime

Metronome says almost no part of its system depends on long-lived API keys or static security tokens. Its engineers mint credentials daily, those credentials last 12 hours, and long-lived AWS credentials are not stored on developer machines.

## Billing-provider credential submission boundary

The bearer-authenticated account-level setup endpoint accepts an open provider-specific configuration object. Its examples submit AWS role and external identifiers, Azure client and tenant IDs plus `raw_azure_client_secret`, and GCP provider ID plus `raw_gcp_workload_identity_federation_config`. The page does not specify caller role or token scope, credential creation and ownership, validation, storage encryption, redaction, rotation, independent update, deletion, forwarding to providers, or audit attribution. A separate listing source says sensitive configuration may be omitted from responses, but setup success returns only `delivery_method_id` and does not establish a credential-retrieval surface. [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]]


### AWS Marketplace role delegation

The AWS guide has the seller create a cross-account role that allows `BatchMeterUsage`, `GetEntitlements`, `ListEntities`, and `DescribeEntity` on `Resource: "*"`; the trust setup uses Metronome's AWS account ID and generated external ID, and the role name must begin with `metronome-marketplace`. The role ARN is then saved in Metronome. The page does not define narrower resource scoping, validation, credential or external-ID rotation, independent update, rollback, deletion, or audit evidence. [[source-metronome-integrations-marketplace-integrations-aws]]

## Customer API tokens

Metronome's public API uses bearer tokens created and archived through the dashboard. Tokens inherit the creating user's permissions by default and can be restricted by access level, environment, or endpoint through a Metronome representative. The full token is visible only at creation, the SDKs default to `METRONOME_BEARER_TOKEN`, and archiving a token cannot be undone.

The API quickstart corroborates the creation boundary: give the token a descriptive name and copy it to a secure location before completing the flow. Its setup examples accept a bearer token directly or use `METRONOME_BEARER_TOKEN`, but the quickstart adds no expiry, recovery, rotation, scope, or revocation policy.

> [!info] Credential-scope boundary
> The 12-hour lifetime above describes credentials minted by Metronome engineers. The API-authentication page does not state a lifetime or expiry policy for customer-created bearer tokens, so the two credential classes should not be treated as having the same lifecycle.

## Role-based access control

Metronome separately documents SAML 2.0 SSO for team-member login, supporting both service-provider-initiated and identity-provider-initiated authentication. Identity-provider-side removal prevents subsequent login, but Metronome retains user metadata in Team Settings, including the role recorded at the user's last login. After attribute mapping and joint verification, an account switched to SSO no longer accepts its existing username-and-password logins. Although the page says Metronome handles user provisioning, it does not define SCIM, account-creation timing, profile-update behavior, record deletion, reactivation, active-session revocation, or fallback login.

Metronome documents three built-in roles: admin, member, and viewer. With SSO, an identity-provider claim maps users to a role and unmapped users are denied by default. Without SSO, users who already have Metronome access receive full access.

New API tokens can be assigned a selected role at creation, and that role cannot later be changed. The authentication reference separately says tokens inherit the creating user's permissions by default. These may describe default inheritance versus explicit RBAC assignment, but the sources do not define precedence; retain both as source-scoped facts.

## Audit visibility and attribution

Metronome says its audit log tracks actions across the system, including app and API activity, and records the time, responsible user or API token, affected resource, action, and success outcome. Example entries also carry an audit-entry ID, actor details, resource type and ID, request ID, and status, and the guide links to `/auditLogs` for access. This supports monitoring and change attribution but does not establish retention, completeness, delivery order or latency, export, access permissions, immutability, tamper evidence, authorization of the recorded action, or the full endpoint schema. The two example timestamps use an impossible April 32 date and an extra colon-delimited time component, so they are not valid timestamp-format evidence.

## Production-environment checklist boundary

Metronome's go-live checklist recommends creating and securely storing a production API token, enabling IP allowlisting when required, and pointing API calls to `https://api.metronome.com`. It does not define token scope, expiry, rotation, storage controls, allowlist maintenance, or evidence sufficient to establish secure, auditable, or reconciled billing. [[source-metronome-guides-implement-metronome-production-checklist]]

## Sources

- [[source-metronome-guides-platform-configuration-audit-logs]] — cross-channel action attribution, outcome visibility, request correlation, and audit-evidence boundaries

- [[source-metronome-guides-platform-configuration-single-sign-on-sso]] - SAML 2.0 team login, identity-provider-controlled access removal, retained user metadata, and password-login cutover

- [[source-metronome-guides-platform-configuration-allowlist]] — polling and automation guidance, stale-allowlist access risk, notice-wording tension, and layered-security boundaries

- [[source-metronome-api-reference-security-get-services]] — bearer-authenticated service registry, directional usage labels, IP strings, and allowlisting boundaries

- [[source-metronome-guides-platform-configuration-security-principles]] — least privilege, zero trust, and short-lived credential principles
- [[source-metronome-api-reference-authentication]] — customer bearer-token creation, use, scoping, and archival
- [[source-metronome-api-reference-api-quickstart]] — first-connection token handling and SDK environment-variable setup
- [[source-metronome-guides-platform-configuration-role-based-access-rbac]] — built-in roles, SSO claims, default denial, and token role selection

- [[source-metronome-api-reference-settings-set-up-account-level-billing-provider]] — bearer-authenticated submission of provider identity and secret-bearing configuration with unspecified custody and rotation semantics


- [[source-metronome-integrations-marketplace-integrations-aws]] — cross-account AWS role permissions, account and external-ID trust, role-name constraint, and credential-lifecycle unknowns

## Related

- [[metronome]]
- [[metronome-webhooks]]
