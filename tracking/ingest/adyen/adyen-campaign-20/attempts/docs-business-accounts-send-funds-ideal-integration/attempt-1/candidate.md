---
title: "Adyen Business Accounts: iDEAL account-to-account payments"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds-ideal-integration"
raw_files:
  - "adyen/docs/business-accounts/send-funds-ideal-integration/2026-09-15.md"
tags: [adyen, business-accounts, ideal, a2a, sca]
---

## Overview

This page, last modified 2025-08-22 and captured 2026-09-15, describes the iDEAL account-to-account issuer flow in which a user pays an online checkout from an Adyen Business Account in the Netherlands. The user selects Adyen and the platform, signs in on the platform, views the payment and source balance account, and authorizes with Strong Customer Authentication (SCA). The payee is the counterparty shown in the payment details. This is a platform or marketplace integration guide, not a general Issuing card-payment guide or proof of account opening, live eligibility, completed funds movement or recipient-bank receipt.

## Key takeaways

- Scope and prerequisites: the captured guide applies to Netherlands-operating platforms or marketplaces with an Adyen for Platforms integration supporting Business Accounts, an Adyen Business Account, and an API user with **Role for A2A Issuer payments - API**. Payments use the iDEAL network only. The platform must implement SCA and either redirect or QR capture; QR requires an in-app reader that sends raw QR information to the endpoint. The guide also requires specified HTTPS redirect URLs, transaction-context query handling, iDEAL-compliant screens, and a platform logo supplied to the Adyen contact. These dated requirements do not establish current availability for a particular account.
- The platform supplies `payment_redirect_url` for sign-in, the incoming `payload` query parameter and payment-detail display, plus `authenticate_redirect_url` for iDEAL profile authentication. After redirect sign-in or scanning, its server calls `POST /payments/details` with `method: ideal`, `source: redirect` or `qr`, and the iDEAL payload. The response's short-lived `token` (around 15 minutes in this guide) is used for confirm or cancel; details include amount, payee/counterparty and expiry.
- Confirmation has an SCA challenge boundary: device/browser eligibility supplies `sdkOutput`; the first `POST /payments/confirm` sends that output in the `WWW-Authenticate` header with the token and source `balanceAccountId`. The documented 401 response contains the challenge `sdkInput`; after the user authenticates, the second confirm sends the resulting `sdkOutput` within 10 minutes of the first request. The guide describes a `links.success.href` return URL for the success path. A challenge, SDK result or return link alone is not independent evidence of settlement or bank receipt.
- The guide says `POST /payments/cancel` can cancel a still-pending, unexpired, unconfirmed payment, but says cancellation occurs when the returned `links.cancel.href` is opened. For desktop QR flows, the mobile app shows confirmation and does not redirect the user to checkout; the desktop browser handles that transition.
- Payment, profile and authentication screens have iDEAL UX requirements including logo, amount/currency, payee, description, balance-account switch where needed and result details. The platform must share wireframes with Adyen before go-live. iDEAL profile register, management-link and authentication endpoints are optional for standard payment processing; their redirect URLs are short-lived.

## Detail locators

- **Requirements; iDEAL for A2A payments; How it works** — integration scope, API role, Netherlands/iDEAL limitation, setup, platform-directed user flow and source balance account.
- **Configure required redirect URLs; Retrieve payment information** — HTTPS URLs, payload acquisition, server-side `/payments/details`, short-lived token and payment fields.
- **Check SCA eligibility; Initiate SCA payment confirmation; Authenticate user; Complete SCA payment confirmation** — Android/iOS/web SDK examples, the 401 challenge, two confirm requests, 10-minute authentication interval and success-path link. The completion prose calls for a `success` object, while its response example shows only `links.success.href`; verify actual API response structure against the relevant API reference before implementing that check.
- **Cancel a payment; Payment screen requirements; iDEAL profile endpoints; Error codes and messages** — cancellation/open-link boundary, screen/wireframe requirements, optional profile flow and invalid/expired/locked payment or payload errors. In particular, `1069_005` can indicate a payment locked by a confirm, cancel or concurrent request; do not infer retry safety from this table.

## Related

- [[adyen-business-accounts]] — product and account-resource context.
- [[adyen-platforms]] — platform integration context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds-ideal-integration/2026-09-15|iDEAL A2A integration guide, captured 2026-09-15]]
