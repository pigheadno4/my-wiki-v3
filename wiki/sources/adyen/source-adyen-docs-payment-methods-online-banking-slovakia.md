---
title: "Online banking Slovakia payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/2026-09-15.md"
tags: [adyen, online-banking-slovakia, slovakia, redirect, eur]
---

## Overview

This 2026-09-15-captured Adyen method overview describes Online banking Slovakia as an **SK/EUR online-banking redirect** method, gives a capability matrix and acquiring-bank contract statement, and routes to platform guides. It is a dated documentation snapshot, not current market ranking, merchant entitlement, or evidence of a successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The shopper is shown issuing banks, selects one, and is redirected to the bank website or mobile app to complete payment. The page says merchants integrating through Adyen **do not need contracts with acquiring banks**; this is the source's integration claim, not proof of a particular merchant's account setup (raw lines 25–27).
- The overview calls online banking the **second most popular method in Slovakia after cards**. Treat this as an unverified, dated source claim, not a current market measurement (raw line 23).
- The matrix labels the method **Online Banking**, **redirect**, **SK**, and **EUR**. It crosses **recurring**, **separate captures**, **partial captures**, **multiple partial captures**, and **chargebacks**; it checks **refunds**, **partial refunds**, and **multiple partial refunds**. These are captured overview marks, not a complete API recipe or guarantee of an account's current operation. The capture crosses cover the listed variants, not an assertion that every ordinary capture operation is unsupported (raw lines 29–31).
- The chooser links pre-built UI routes for Web, iOS, Android, React Native, and Flutter, an API-only custom UI route for website/iOS/Android, and Pay by Link. These are navigation routes, not proof of method configuration or transaction execution. The generic 3D Secure/Capture “See also” links do not add Slovakia-specific capability claims (raw lines 33–84).

## Detail locators

- Identity, dated ranking, bank redirect and contract statement: raw `# Online banking Slovakia` lines 15–27.
- SK/EUR capability matrix: raw lines 29–31.
- Platform/API-only/Pay by Link routes: raw `## How do you want to integrate?` lines 33–75.
- Generic See also links: raw lines 79–84.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/2026-09-15|Online banking Slovakia overview, captured 2026-09-15]]
