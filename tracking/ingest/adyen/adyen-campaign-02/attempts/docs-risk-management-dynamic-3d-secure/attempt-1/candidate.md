---
title: "Adyen Dynamic 3D Secure"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/dynamic-3d-secure"
raw_files:
  - "adyen/docs/risk-management/dynamic-3d-secure/2026-09-15.md"
tags: [adyen, risk-management, 3d-secure, authentication, rules]
---

## Overview

This Adyen documentation snapshot explains how an online-payments integration with 3D Secure 2 can set default and conditional Dynamic 3D Secure preferences for card transactions. Rules can request authentication and, in selected cases, express a preference for a challenge. It also describes payment-request overrides and Protect premium risk-based authentication and exemptions. See [[adyen]], [[adyen-3d-secure]], and [[adyen-risk-management]].

## Key takeaways

- The prerequisite is an online-payments integration with 3D Secure 2. Changing Dynamic 3D Secure rules requires an eligible Customer Area role. Risk management must be enabled when Dynamic 3D Secure is used with it; Protect premium is required for risk-based authentication and for custom risk rules linked to Dynamic 3D Secure rules.
- The default rule begins at **Prefer not** for a new company or merchant account. **Prefer not** does not preclude 3D Secure where regulation, issuer requirements, or performance handling call for it. **Always** requests 3D Secure wherever possible, but does not ensure that authentication occurs when, for example, the issuer lacks support or the card is not enrolled. A request to authenticate also does not choose the eventual frictionless or challenge flow; the issuer determines that path.
- Dynamic rules evaluate in order and stop at the first triggered rule. Merchant-account rules have priority over company-account rules and affect that merchant only. Conditions within a rule combine as AND, while multiple selected values within one condition match as alternatives. The page warns that the **Risk score** criterion belongs to the classic risk engine and does not apply to Protect.
- Requesting a challenge is a preference that adds shopper friction and may reduce conversion; the page recommends an **Always** challenge preference only in special circumstances. Both successful frictionless and challenge authentication are discussed in relation to liability shift, subject to the separate scheme, issuer, and transaction qualifications in [[adyen-3d-secure]].
- Payment-request parameters override configured Dynamic 3D Secure rules. The page identifies `authenticationData.attemptAuthentication` for an authentication request and `threeDS2RequestData.threeDSRequestorChallengeInd` for a challenge preference, with different fields for Checkout API v68-and-earlier and v67-and-earlier respectively. The challenge field is used only if 3D Secure is requested.
- Protect premium risk-based authentication routes transactions that its machine-learning fraud rule would otherwise block to 3D Secure 2. In the described path, failed authentication leaves the transaction blocked; if 3D Secure is unavailable, Protect reverts to a decline without an authentication fee. These are documented flow statements, not proof of an individual authorization, liability shift, or merchant enablement.
- **Risk-based exemptions are limited availability in this snapshot**: Adyen says it began rolling them out to select Protect premium companies in July 2026, subject to business and region availability. For low-risk payments, the described behavior uses a TRA exemption inside PSD2 markets or skips 3D Secure outside them. The page's performance language is an estimate, not a guaranteed authorization improvement.

## Detail locators

- Purpose, 3DS2 and role/tier prerequisites, and setup sequence: lines 15–38.
- Regulatory/default preference context and issuer distinction: `## How Dynamic 3D Secure works`, lines 40–51; `## Default 3D Secure rule`, lines 53–59.
- Authentication and challenge preferences, conversion trade-off, rule precedence and condition semantics: `## Dynamic 3D Secure rules`, lines 61–88. Configuration criteria, including the classic-engine **Risk score** caveat and premium **Risk check** prerequisite: lines 90–121.
- Fictional rule scenarios: `## Example scenarios`, lines 123–159; these illustrate configurations rather than guarantee outcomes.
- Payment-request precedence and Checkout API version-specific fields: `## Override using the payment request`, lines 161–172.
- Protect premium risk-based authentication outcomes, settings, and analytics: lines 174–186. Limited-availability risk-based exemptions, PSD2/out-of-scope paths, and enablement guidance: lines 188–205.

## Related

- [[adyen]] — provider context.
- [[adyen-3d-secure]] — merchant 3DS2 concept and reciprocal source route.
- [[adyen-risk-management]] — Protect and premium-feature context.
- [[adyen-psd2-sca-and-3d-secure]] — qualified regulatory, issuer, exemption, and API-preference boundaries.

## Raw Sources

- [[raw/adyen/docs/risk-management/dynamic-3d-secure/2026-09-15|Adyen Dynamic 3D Secure (2026-09-15)]]
