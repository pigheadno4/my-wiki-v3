---
title: "Braintree Local Payment Methods Configuration for iOS v7"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/configuration/ios/v7"
raw_files:
  - "braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16.md"
tags: [braintree, local-payment-methods, ios, configuration, client-token, webhooks]
---

## Overview

This captured Braintree configuration page is an iOS v7-routed checklist for preparing to accept Local Payment Methods. It assigns account setup, server token generation and transaction creation, client integration, webhook configuration, and a successful Sandbox or Production transaction as separate prerequisites. It is a 2026-09-16 website snapshot for [[braintree]], [[braintree-payment-methods]] and the [[braintree-ios-sdk]] route, not exact-package evidence, current merchant or buyer eligibility, or proof that any payment was initiated, completed, settled or funded.

## Key takeaways

- The page requires a valid PayPal business account that has been created, verified and linked in the Braintree Control Panel before Local Payment Methods processing. This records the page's account prerequisite; it does not show that a particular merchant account is linked or enabled.
- Server responsibilities include generating the client token used to initialize client components and creating the Local Payment transaction. Client integration, server transaction creation and webhook configuration remain distinct responsibilities.
- The page says a Local Payment transaction must be processed successfully in either Sandbox or Production. Those are alternative environment routes in the checklist, not evidence that this snapshot, a client token, account setup or an integration step executed a transaction in either environment.
- Although the route is labelled iOS v7, the body says Local Payment Methods were introduced in v4 of the iOS SDK, alongside v3 of the JavaScript SDK and v2 of the Android SDK. That historical introduction statement does not identify the exact installed iOS v7 package, establish current compatibility, or transfer behavior across SDK families.
- The captured notice says Braintree Mobile SDK certificates were set to expire on March 30, 2026, directs iOS SDK upgrades to version 6.17.0 or newer for new certificates, and warns that traffic from app versions retaining older SDK certificates will fail after the date. Because the notice is historical and appears on an iOS v7-routed page, use it as snapshot migration evidence rather than a current package-support or runtime-status claim.

## Evidence boundaries

> [!warning] Historical certificate deadline
> The snapshot describes a March 30, 2026 certificate-expiration deadline and a severe all-traffic failure consequence for published app versions retaining older SDK certificates. It names iOS SDK 6.17.0 or newer as the upgrade floor for new certificates, not the exact v7 package represented by the route. Recheck current official package and support authority before operational use.

> [!warning] Configuration is not execution proof
> A linked PayPal business account, generated client token, client integration, server integration and configured webhooks are prerequisites, not evidence that a particular Sandbox or Production payment was initiated, authorized, completed, settled or funded. The checklist's final successful-transaction step is a requirement, not a result produced by this document.

> [!warning] Platform and version scope
> The canonical route is iOS v7, while the body separately records introduction versions for JavaScript v3, iOS v4 and Android v2. Do not infer sibling-platform behavior, an exact installed iOS v7 release, or current SDK compatibility from that introduction history.

## Detail locators

- Historical Braintree Mobile certificate-expiration date and iOS 6.17.0-or-newer direction: `# Configuration > IMPORTANT`, raw lines 17-18.
- Stated failure consequence for app versions retaining older SDK certificates: `# Configuration > IMPORTANT`, raw line 20.
- Configuration checklist purpose: `# Configuration`, raw line 22.
- Valid PayPal business-account creation, verification and Control Panel linking prerequisite: `# Configuration`, raw line 25.
- Server-generated client token and component-initialization use: `# Configuration`, raw lines 26-27.
- Client integration and cross-platform introduction-version statement: `# Configuration`, raw lines 30-31.
- Server transaction creation, webhook configuration and successful Sandbox-or-Production transaction steps: `# Configuration`, raw lines 34-36.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Native SDK route: [[braintree-ios-sdk]]

## Related raw API references

The following collected files were not used as factual authority for this entry; they are exact-file navigation for client, server, webhook and environment follow-up:

- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16|Braintree Local Payment Methods custom client integration — iOS v7]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods server integration — Node.js]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Braintree Local Payment Methods testing and go-live — Node.js]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16|Braintree Local Payment Methods Configuration — iOS v7 (captured 2026-09-16)]] - fully read pinned snapshot covering the prerequisite checklist and historical mobile SDK certificate warning
