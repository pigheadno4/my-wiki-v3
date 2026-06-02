---
title: "Log in with PayPal"
type: concept
category: technology
tags: [paypal, login-with-paypal, oauth, openid, identity, sso]
---

## Log in with PayPal

PayPal's OAuth 2.0 / OpenID Connect-based SSO product. Lets users authenticate with their PayPal account on third-party websites/apps. Used both as a standalone login and as a customer acquisition tool for [[paypal-payouts]] (AAC pattern).

## OAuth Flow

1. User clicks Log in with PayPal button → redirected to PayPal consent screen
2. User approves → PayPal redirects to merchant's Return URL with authorization code
3. Merchant server exchanges code for access token + refresh token (`POST /v1/oauth2/token`, `grant_type=authorization_code`)
4. Access token used to call `GET /v1/identity/oauth2/userinfo?schema=openid`
5. Access token expires in **8 hours** — refresh with `grant_type=refresh_token` before each user info call

## Key Scopes

For payouts/withdrawal integrations, request: **Email**, **Account verification status**, **Payer ID**. Fewer scopes → higher consent rate.

5 distinct scope values: `openid` (required), `profile`, `email`, `address` (covers all 5 address fields), `https://uri.paypal.com/services/paypalattributes` (covers both verification status and payer ID).

## App Requirements

- Enable in Developer Dashboard: Apps & Credentials → App → Other features → Log in with PayPal
- Set Return URL, Privacy policy URL, User agreement URL
- **Live app review required** (typically a few weeks); sandbox needs no review
- URLs reviewed by PayPal privacy/security team before go-live

## Button Options

- **Generate button**: auto-generated JS, simplest; 10 configurable parameters
- **Build button**: manual control over auth endpoint and parameters

**`authend` gotcha**: pass `sandbox` for test; **omit entirely for live** (do not pass "production"). **`nonce` gotcha**: without it → mini browser popup; with any random number → redirects to parent browser.

## Best Practices

- **Don't disconnect PayPal session on site logout** — keep SSO alive for returning users
- **Anti-spam**: no auto-newsletter enrollment; only post-purchase transactional emails without explicit opt-in
- **Account linking**: offer existing users a way to link their pre-existing account to PayPal; scan for duplicates in real-time
- **Checkout**: pre-fill forms; show editable confirmation page; set PayPal as default payment for SSO users

## Key Players

- [[paypal]] — Identity API provider

## Sources

- [[source-paypal-login-with-paypal]] — Full integration guide: OAuth flow, token exchange, go-live steps
