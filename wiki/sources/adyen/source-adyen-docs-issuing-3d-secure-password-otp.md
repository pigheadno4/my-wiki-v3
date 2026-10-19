---
title: "Adyen Issuing: one-time password authentication"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/password-otp"
raw_files:
  - "adyen/docs/issuing/3d-secure/password-otp/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, authentication]
---

## Overview

This Adyen Issuing guide (last modified 2021-09-09; captured 2026-09-15) describes enrolling an Adyen-issued card for password plus one-time password (OTP) 3D Secure authentication. The platform configures the card's authentication data; the cardholder supplies the password and an SMS or email OTP on the authentication page for an online payment. Successful authentication sends the payment to Adyen for a separate Issuing authorisation decision; failed authentication fails the payment. This is an issuer-side cardholder-authentication guide, not an acquiring checkout integration or proof that a payment was authorised, captured, or settled. [[adyen-issuing]]

## Key takeaways

- The integration is Issuing, and the API credential needs the **Bank SCA Webservice Role** to enroll cards in 3D Secure. When creating a card, the platform can include `card.authentication` with a password (required for either SMS or email OTP), a mobile phone object, and an email address. It may add or update authentication data later with `PATCH /paymentInstruments/{id}`.
- The documented OTP preference is SMS when a phone number is available, with email fallback when it is absent; some countries always use email OTP. If neither contact method is available, the transaction is declined because an OTP cannot be sent. Do not assume the SMS preference applies in every country.
- Adyen says `balancePlatform.authentication.created` is sent regardless of authentication outcome. The page includes authenticated frictionless, authenticated challenge, and rejected retries-exceeded webhook examples. Those examples show possible outcomes and fields; their sample values, retry count, and OOB challenge flow do not establish a universal OTP challenge sequence or a successful authorisation. The separately captured [[source-adyen-docs-issuing-3d-secure-troubleshooting]] says failed 3D Secure authentication yields no relayed authorization or webhook, without naming the webhook event family (raw troubleshooting line 33). Its scope relative to this page's `balancePlatform.authentication.created` statement remains unresolved; do not assume one statement supersedes the other.
- The card-creation and update snippets use test Balance Platform API endpoints and inactive example cards, with language-library versions shown in the raw. They illustrate request shape rather than proving a live card or completed payment. The guide separately says funding accounts, processing payments, and card lifecycle management are needed before users can make purchases.

## Detail locators

- Raw lines 19–31 describe cardholder authentication and the separate authorisation step; lines 33–38 give integration type and credential role.
- Raw lines 40–56 state authentication fields, OTP order, country exception, and missing-contact decline; lines 58–635 contain create-card snippets across curl, Java, PHP, C#, JavaScript, Go, Python, Ruby, and TypeScript.
- Raw lines 636–942 describe later `PATCH /paymentInstruments/{id}` and language snippets.
- Raw lines 943–1081 describe the authentication webhook and test examples for frictionless, challenge, and rejected outcomes; lines 1083–1101 point to separate funding, payment authorisation, and 3D Secure transaction guides.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/password-otp/2026-09-15|Adyen Issuing OTP authentication guide, captured 2026-09-15]]
