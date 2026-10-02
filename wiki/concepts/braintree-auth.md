---
title: "Braintree Auth"
type: concept
category: technology
tags: [braintree, braintree-auth, oauth, connected-merchants, platforms]
---

## Braintree Auth

Retrieval hub for collected Braintree Auth documentation. Keep Braintree Auth distinct from generic payment-transaction authorization: this route concerns a platform's OAuth connection to Braintree merchants and authorized actions on their behalf. Each source retains its environment, SDK, credential, merchant and closed-beta qualifications; collected documentation does not establish current availability, account eligibility or live payment acceptance.

After a merchant completes the separate Connect flow, Braintree returns an authorization code to the platform's redirect URI; the platform exchanges that code using its Braintree Auth client ID and client secret, then uses the resulting access token for actions on that connected merchant's behalf subject to the OAuth permissions granted through the separate Connect configuration. This OAuth-flow source does not select or enumerate those scopes. [[source-braintree-auth-oauth-flow-node]]

## OAuth credential lifecycle

The guide states that access tokens expire 24 hours after creation and initially issued refresh tokens expire after 180 days. A refresh returns a new access token and refresh token. Refreshing and revoking are distinct in the guide: the platform can explicitly revoke an access token, while a merchant can revoke OAuth access in the Control Panel; a revoked access token produces an authentication error when used through the Merchant API. [[source-braintree-auth-oauth-flow-node]]

## Scope boundary

Keep Braintree Auth distinct from generic transaction authorization, Braintree Direct merchant credentials and the ordinary payment client-token flow. This concept routes the platform-to-connected-merchant authorization model; exact scope selection remains in the dedicated server-side Connect guide, the scope catalog remains in the reference, and Merchant API operations, webhooks, merchant-account and multi-currency behavior remain in their dedicated sources. This OAuth-flow source does not select or enumerate scopes. The collected closed-beta statement does not establish current eligibility or enablement for an individual platform.

## Reference and security boundaries

The reference routes new-account field pre-population, existing-merchant-only login, OAuth scope selection, the redirect-returned `merchantId`, and an intermediary-server pattern for downloadable software. It says platform `client_id` and `client_secret` values must remain secret and explicitly warns that its worked `state` example is insecure, directing implementers to the server-side guide for safe handling. Its OAuth prose says three additional scopes while the rendered table contains four entries; preserve that source inconsistency rather than inferring a corrected count. Exact fields, scope meanings, validation errors and the worked redirect sequence remain in the raw reference. [[source-braintree-auth-reference-node]]

## Sources

- [[source-braintree-auth-overview]] - closed-beta product overview for ecommerce-platform and merchant-service-provider connections to Braintree merchants, authorized-action purpose, service and payment use cases, and dedicated Shared Vault and Grant API routes

- [[source-braintree-auth-connect]] - closed-beta merchant-facing Connect route from a platform button through hosted login or signup, OAuth authorization and return redirect, with login-only and Finish Later boundaries

- [[source-braintree-auth-configuration]] - closed-beta OAuth application setup route for platform-owned Control Panel configuration, merchant-facing identity and support, allowlisted redirects, and environment-specific server-held credentials

- [[source-braintree-auth-server-side-node]] - closed-beta Node.js route for server-built merchant Connect URLs, allowlisted OAuth returns, least-privilege scopes, and non-guessable, matched and escaped `state` handling

- [[source-braintree-auth-oauth-flow-node]] - Node.js post-Connect authorization-code exchange, merchant-scoped access-token use, refresh lifetimes and platform/merchant revocation routes
- [[source-braintree-auth-multi-currency-node]] - closed-beta Node.js route for adding and listing presentment currencies for connected merchants who signed up through Braintree Auth, with access-token, payment-method support and Amex-specific qualifications

- [[source-braintree-auth-merchant-api-node]] - closed-beta Node.js route for using an access token to initialize the gateway for connected-merchant transaction and customer examples, with the revoked-authorization authentication-error boundary

- [[source-braintree-auth-reference-node]] - closed-beta Node.js-route reference for signup/login controls, scopes, merchant identity, downloadable-software credential handling and exact raw-detail locators

- [[source-braintree-auth-testing-go-live-node]] - Node.js route for sandbox OAuth and signup testing, test authorization-code behavior, the separate production Connect and underwriting boundary, and payment-enablement prerequisites

## Related

- [[braintree-payment-platform]] - Braintree Direct, Extend and Auth product-orientation route
- [[braintree-webhooks]] - event-specific notification and delivery routes, including separate Braintree Auth notifications
