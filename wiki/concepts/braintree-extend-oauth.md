---
title: "Braintree Extend OAuth"
type: concept
category: technology
tags: [braintree, braintree-extend, oauth, connected-merchants, access-tokens]
---

## Braintree Extend OAuth

Retrieval hub for collected Braintree Extend OAuth documentation. This route covers a merchant-consented OAuth connection in which the merchant returns to the platform's configured redirect URI and the platform server exchanges the authorization code for credentials used on that merchant's behalf. Preserve the scopes the merchant agreed to and the page's environment qualifications; this route does not establish current access, enablement or successful payment execution.

Keep Extend OAuth distinct from [[braintree-auth]]. The collected documentation exposes separate product paths and different availability wording even though both routes use connected-merchant OAuth credentials and overlapping Node token operations. Shared terminology alone does not transfer product eligibility, scope, credential or lifecycle claims between them.

## Principal flow and responsibilities

The merchant agrees to the requested OAuth scopes, Braintree returns `code`, `merchantId` and the supplied `state` to the redirect URI, and the platform server exchanges the code for an access token and refresh token. The access token is used for actions on the merchant's behalf within the granted scope. Exact Connect URL, scope and state controls remain in their dedicated sources rather than being inferred from this access-token page.

Token refresh and revocation are separate operations. Use the source page for its snapshot-qualified token lifetimes, refreshed credential-pair behavior, platform revocation call, merchant Control Panel revocation and authentication-error consequence; do not treat an example response as proof that a token was issued or used successfully.

## Sources
- [[source-braintree-extend-oauth-shared-vault-node]] - Node.js-route guide to the Shared Vault scope for using platform-owned Vault tokens and IDs when creating a transaction for a connected merchant
- [[source-braintree-extend-oauth-overview]] - unversioned product overview for separate-account OAuth, merchant scope consent and server-side delegation, with snapshot beta qualifications
- [[source-braintree-extend-oauth-configuration]] - environment-specific Control Panel setup for a platform OAuth application, merchant-facing identity and support fields, redirect allowlisting, production closed-beta and sandbox open-beta qualifications, and an explicit boundary from undocumented client-secret handling
- [[source-braintree-extend-oauth-client-side-javascript-v3]] - JavaScript v3 client-side Connect-button guide for starting merchant consent with a server-generated Extend OAuth URL, with return-page display and environment parameter qualifications
- [[source-braintree-extend-oauth-client-side-android-v5]] - Android v5 client-side Connect route using a server-supplied URL, Android `Intent` and `IntentFilter`, with server-owned access-token creation and return redirect, production closed-beta and sandbox open-beta qualifications, a future Intent Filter verification note, and a dated Mobile SDK certificate/version warning
- [[source-braintree-extend-oauth-connect-urls-node]] - Node.js Connect URL generation for merchant login and requested-scope consent, with environment-qualified application credentials, redirect allowlisting, scope selection and CSRF state controls
- [[source-braintree-extend-oauth-reference]] - unversioned Extend OAuth catalog for resource-oriented and additional OAuth scopes, facilitator-qualified variants, snapshot availability and raw-table rendering limits

- [[source-braintree-extend-oauth-access-tokens-node]] - Node.js post-consent redirect values, server-side authorization-code exchange, token lifecycle and platform or merchant revocation routes

## Related

- [[braintree]] - provider company and exhaustive source catalog
- [[braintree-payment-platform]] - provider product-orientation route separating Direct, Extend and Auth
- [[braintree-auth]] - separate platform-to-merchant OAuth product route with its own collected availability and source ownership
- [[braintree-server-sdk]] - shared server-side gateway boundary; exact SDK and credential behavior remains source-qualified
- [[braintree-webhooks]] - event-delivery route including OAuth access-revocation notifications
