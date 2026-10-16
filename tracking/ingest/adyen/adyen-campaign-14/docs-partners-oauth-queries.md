# Fixed queries — docs-partners-oauth

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen partner OAuth hub explains delegated API access to customer account resources and routes to the detailed integration guide. OAuth is partner-only here. The customer is the resource owner, Adyen APIs are the resource server, the partner application is the client, and Adyen's OAuth server authenticates and issues tokens. A hub description, Connect button, app registration or redirect is not proof of a customer grant, returned scope/accounts, live authorization, or an executed payment.

**Raw locators:** lines 15–23 (purpose, partner-only scope, consent and payment use case); 25–43 (party identity and flow); 45–52 (child guide navigation).

**Canonical route:** [[adyen-index]] → [[adyen-partner-oauth]] → [[source-adyen-docs-partners-oauth]] → [[raw/adyen/docs/partners/oauth/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** The partner requests scope; the customer confirms it at Adyen. The described flow redirects the customer for authentication/authorization, returns a code, exchanges it for access and refresh tokens, uses the access token for API calls on the customer's behalf, and refreshes after expiry. The hub does not define exact scopes, grant account identities, registration roles, app-installation state, test/live endpoints, token lifetime, or payment eligibility. Use the linked OAuth integration and scopes sources for those conditions and the actual token response for the granted scope/resources.

**Raw locators:** lines 19–23 (partner, customer and scope); 27–41 (parties and six steps); 45–52 (integration child route).

**Canonical route:** [[adyen-index]] → [[adyen-partner-oauth]] → [[source-adyen-docs-partners-oauth]]; detailed child routes [[source-adyen-docs-partners-oauth-integration]] and [[source-adyen-docs-partners-oauth-scopes]], full hub at [[raw/adyen/docs/partners/oauth/2026-09-15]].
