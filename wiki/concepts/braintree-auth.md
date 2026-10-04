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
- [[source-braintree-extend-oauth-client-side-ios-v7]] - iOS v7 OAuth Connect route under the site's Extend path, with production closed-beta and sandbox open-beta qualifications, server-created access-token return, custom-scheme interception risk and a dated Mobile SDK certificate notice; the route name alone does not identify the Braintree Extend payment-data-sharing product

- [[source-braintree-auth-client-side-javascript-v3]] - closed-beta JavaScript v3 browser-side Connect-button route using `braintree-oauth-connect.js` and a server-generated `connect_url`, with parameter locators and a Finish Later denial-return boundary but no modal, parity, current-eligibility or payment-authorization inference

- [[source-braintree-auth-client-side-android-v5]] - closed-beta Android v5 client-side Connect route using a server-supplied `connect_url`, Android `Intent` and `IntentFilter`, with server-owned OAuth exchange and snapshot-preserved mobile SDK certificate qualifications
- [[source-braintree-auth-branding-ios-v7]] - closed-beta iOS v7 branding snapshot for PayPal powered by Braintree identity, dashboard and marketing presentation, payment marks, recommended transaction-versus-link-only explanatory copy, and an iOS Connect button asset without current-support, modal-behavior or cross-variant parity inference

- [[source-braintree-auth-branding-javascript-v3]] - closed-beta JavaScript v3 branding route for PayPal powered by Braintree identity, transaction versus account-linking copy variants, Connect button presentation, redirect via a server-generated `connect_url` and post-authorization display condition

- [[source-braintree-auth-client-side-ios-v7]] - closed-beta iOS v7 client-side Connect route from a server-provided Connect URL through Braintree-hosted merchant authorization, server-side OAuth exchange and custom-URL return, with interception and dated SDK-certificate warnings
- [[source-braintree-auth-branding-android-v5]] - closed-beta Android v5 branding snapshot for platform and dashboard presentation, recommended logo, payment-mark and explanatory-copy routes, and an Android Connect button asset without current-support or cross-variant parity inference

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
