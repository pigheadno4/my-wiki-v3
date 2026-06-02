---
title: "Integrate Log in with PayPal"
type: source
date_ingested: 2026-04-16
original_format: webpage
raw_files:
  - "paypal-login-with-paypal-integrate.md"
  - "paypal-login-with-paypal-generate-button.md"
  - "paypal-login-with-paypal-build-button.md"
  - "paypal-login-with-paypal-best-practices.md"
  - "paypal-login-with-paypal-reference.md"
  - "paypal-login-with-paypal-button-placement.md"
  - "paypal-login-with-paypal-button-design.md"
  - "paypal-login-with-paypal-upgrade.md"
tags: [paypal, login-with-paypal, oauth, identity, openid, sso]
---

## Summary

Full integration guide for adding the Log in with PayPal button to a website or app. Covers app configuration, button options, OAuth token flow, user info retrieval, and go-live requirements.

## Key Takeaways

- Uses the **Identity API** (`/v1/identity/`)
- For payouts/withdrawal integrations, must request: Email, Account verification status, Payer ID
- Minimum permissions recommended — fewer scopes = higher user consent rate

### Full scope map

| Scope | Attributes covered |
| --- | --- |
| `openid` | Basic authentication (required) |
| `profile` | Full name |
| `email` | Email address |
| `address` | Street address, city, state, country, zip (all 5 in one scope) |
| `https://uri.paypal.com/services/paypalattributes` | Account verification status + Payer ID (both in one scope) |

## OAuth Flow

### 1. Exchange authorization code for tokens

`POST /v1/oauth2/token` with `grant_type=authorization_code&code={code}`

Response includes `access_token` (expires in **28800s / 8 hours**), `refresh_token`, `nonce`, and `scope`.

### 2. Refresh the access token

`POST /v1/oauth2/token` with `grant_type=refresh_token&refresh_token={token}`

**Always refresh before calling user info** — the access token expires after 8 hours.

### 3. Get user info

`GET /v1/identity/oauth2/userinfo?schema=openid` with Bearer access token.

## App Configuration (Developer Dashboard)

- Enable **Log in with PayPal** under Other features → Advanced Settings
- Set **Return URL** (redirect after login)
- Select scopes (Email, Account verification status, Payer ID for payouts)
- Set **Privacy policy URL** and **User agreement URL** — required for go-live; reviewed by PayPal security team

## Button Options

| Option | Use case |
| --- | --- |
| Generate button | Auto-generates JS — simplest integration |
| Build button | Manual control over auth endpoint and parameters |

### Build Button

Auth endpoint template:

```text
https://www.sandbox.paypal.com/signin/authorize?flowEntry=static&client_id=CLIENT-ID&scope=LIST-OF-SCOPES&redirect_uri=RETURN-URL
```

- **Button image**: `https://www.paypalobjects.com/devdoc/log-in-with-paypal-button.png` — **do not self-host**; load from PayPal CDN to stay in sync with branding
- `openid` must always be included in scope
- `redirect_uri` must be URL-encoded and match Return URL in app settings exactly
- `fullPage`: omit → mini browser; `true` → full page in same tab
- Authorization code returned as `?code={authorization_code}` appended to return URL

### Generate Button Parameters (10)

| Parameter | Required | Notes |
| --- | --- | --- |
| `appid` | Yes | Client ID from app creation |
| `authend` | Optional | `sandbox` for test; **omit entirely for live** (not "production") |
| `scope` | Yes | Space-separated scopes (e.g. `openid`) |
| `locale` | Yes | Language/country specifier |
| `buttonSize` | Yes | `sm`, `md`, `lg` |
| `theme` | Optional | PayPal blue or neutral |
| `returnurl` | Yes | Must match Return URL in app settings |
| `responseType` | Yes | `code`, `id_token`, or `code & id_token` |
| `fullpage` | Yes | `true` = full browser; `false` = mini browser (default) |
| `nonce` | Optional | Random number → redirects to parent browser; omitted → mini browser |

## Button Design (Custom Buttons)

- **Labels**: "Log in with PayPal" or "Continue with PayPal" (recommended); "Log in" or "Continue" also acceptable
- **Font**: min 13pt, Sans-serif; custom font/weight/kerning allowed
- **Colors**: PayPal blue `#0070BA` or gray `#EEEEEE`; white text on dark, black on light; best over white/light backgrounds
- **Shape**: pill (recommended — strong PayPal association) or rectangle
- **Icon**: white icon on colored button; colored icon on white button; always source from [PayPal Logo and Marks](https://www.paypal.com/webapps/mpp/logos-buttons); never use outdated/custom version
- **Don'ts**: don't reduce minimum padding, don't change element aspect ratio or alignment, don't stretch elements, don't change background color on colored version
- **In-context messaging**: "We don't share your money transaction history" / "We'll never transact anything without your permission"

## Best Practices

- **Don't disconnect PayPal session on site logout** — preserves SSO for returning users
- **Anti-spam**: auto-enrolling users in newsletters is prohibited; only transactional emails (order confirmation, receipt, shipping) allowed without explicit opt-in
- **Account linking**: scan for duplicates in real-time during session; offline scan + email fallback if real-time not feasible
- **Unlinking**: if discontinuing the feature, must request user permission to unlink + provide password creation for the user account
- **Checkout UX**:
  - Pre-fill forms from PayPal session data
  - Always show editable confirmation page (data was not entered by user — let them review/correct)
  - Set PayPal as default/first payment option for users who logged in with PayPal

## Legacy Migration (pre-January 2018)

Replace `/connect` with `/signin/authorize` in auth URLs:

- Old: `https://www.sandbox.paypal.com/connect?flowEntry=static&...`
- New: `https://www.sandbox.paypal.com/signin/authorize?flowEntry=static&...`

PayPal recommends OpenID Connect for new apps. Existing OpenID integrations continue to work but won't receive new features.

## Go Live

- **App review required**: typically a few weeks; plan ahead
- Sandbox: no review needed; enabled immediately after saving config
- URL swaps: `sandbox.paypal.com` → `paypal.com`; `api-m.sandbox.paypal.com` → `api-m.paypal.com`

## Related Pages

- [[paypal]] — company page
- [[paypal-login-with-paypal]] — Log in with PayPal concept page
- [[source-paypal-payouts-overview]] — AAC / Log in with PayPal for Payouts context

## Raw Sources

- [[paypal-login-with-paypal-integrate]] — verbatim integration guide with OAuth flow, code samples, go-live steps
- [[paypal-login-with-paypal-generate-button]] — Generate button: 10 JS parameters, nonce controls mini vs parent browser redirect, authend omitted for live
- [[paypal-login-with-paypal-build-button]] — Build button: auth URL template, do not self-host button image, fullPage omit=mini/true=full, code appended to return URL
- [[paypal-login-with-paypal-best-practices]] — Best practices: don't disconnect on logout, anti-spam policy, account linking/unlinking, pre-fill checkout, PayPal as default payment
- [[paypal-login-with-paypal-reference]] — Scope attributes: 5 scopes, address covers all 5 fields, paypalattributes covers both verification status and payer ID
- [[paypal-login-with-paypal-button-placement]] — Button placement: login/registration page (primary) and payment preferences/account settings (payouts flow)
- [[paypal-login-with-paypal-button-design]] — Button design guide: colors (#0070BA/#EEEEEE), min 13pt sans-serif, pill shape, icon color matching, in-context messaging examples
- [[paypal-login-with-paypal-upgrade]] — Upgrade: OpenID Connect recommended for new apps; legacy pre-2018 migration: /connect → /signin/authorize
