---
title: "Braintree In-Person FAQ"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/reference/faq"
raw_files:
  - "braintree/in-person/reference/faq-2026-09-16.md"
tags: [braintree, in-person, point-of-sale, card-readers, verifone, operations, faq]
---

## Braintree In-Person FAQ

## Overview

This unversioned Braintree website FAQ snapshot, collected on 2026-09-16, is a retrieval route for the Braintree In-Person solution's hardware, integrated-POS, deployment, testing, network, account and reader-operation boundaries. Its central posture is that the solution is not a standalone reader offering: POS software initializes transactions and handles reader responses, and third-party-acquired Verifone devices cannot be reused because Braintree provisions its own software and encryption keys.

The page is broad operational guidance rather than a complete integration contract. It identifies Verifone Engage reader models and captured territory coverage, but those snapshot statements do not establish current inventory, merchant eligibility, account enablement, supported software or firmware versions, or successful in-person payment execution. See [[braintree]] and [[braintree-payment-platform]].

## Key takeaways

- **Hardware and integration boundary:** the captured supported-reader list is P400, M400, E285 and V400m. The page rejects third-party-acquired Verifone devices and says the solution must be integrated into POS software; it does not describe a standalone, non-integrated mode.
- **Attendance and reader-operation limits:** semi-attended use is described as supportable only when the device is in range and monitored by merchant staff; unattended vending and fuel scenarios require specialized hardware and were not supported in this snapshot. E285-specific troubleshooting is qualified by 2.4 GHz Wi-Fi and battery state.
- **Territory statement is snapshot-scoped:** the FAQ says the solution was supported throughout the United States, Puerto Rico and the US Virgin Islands, while describing possible other-country use cases only as discussion opportunities. It is not present account or deployment eligibility evidence.
- **Production transition is coordinated, not automatic:** the FAQ routes a completed integration through a Braintree Solutions Engineer or Integration Engineer for production-account creation, production-reader ordering and code review. Additional hardware ordering can have procurement and delivery lead times. These preparation steps are not proof of launch approval or production readiness.
- **Network and account conditions remain material:** the onsite firewall must allow reader communications; the FAQ separately routes payment-method coverage, Sandbox test media, dynamic descriptors, AMEX seller-number setup and external-settlement considerations to their linked documentation or Braintree project contacts. Those linked pages were not read for this entry and are navigation rather than evidence here.
- **Reset is destructive:** resetting a reader removes its network connection, offline certificate and screensaver configuration, and also deletes stored offline transactions. The page advises against resetting or un-pairing a production reader unless required.
- **Certification statement is snapshot-scoped:** the page states that Braintree In-Person was listed on the PCI website as the P2PE-certified solution and application named PayPal Enterprise Omni-Channel (EOC). This collected FAQ does not verify the listing's present status or a particular deployment's compliance.

## Detail locators

- Supported Verifone Engage models and the provider-provisioned-device restriction: raw lines 19-40, under `What card readers do you support?` and `Can I use my existing Verifone card readers with Braintree?`.
- Payment-method coverage navigation, Sandbox test-card scope and PayPal/Venmo QRC testing route: raw lines 43-52.
- Integrated POS requirement and semi-attended versus unattended deployment boundary: raw lines 55-62.
- E285 2.4 GHz Wi-Fi and low-battery troubleshooting: raw lines 65-74.
- Captured territory coverage, dynamic descriptors and third-party IVR example/account prerequisite: raw lines 77-95. The named IVR provider is presented only as an example, not as a complete availability list or Braintree-operated call-center product.
- Production-launch coordination and additional-reader procurement: raw lines 98-126.
- Reader-network firewall, AMEX SE number/account-structure and external-settlement routes: raw lines 129-140.
- Destructive reset effects and the captured P2PE listing statement: raw lines 143-150.

## Evidence boundaries

This is a dated website snapshot, not exact-version SDK, reader firmware, GitHub implementation or current PCI-listing evidence. It does not prove present hardware availability, country or use-case eligibility, account approval, payment-method enablement, production launch, reader connectivity, authorization, settlement, funding, stored-offline-transaction recovery or compliance for a particular merchant. Linked pages and external sites are unread navigation unless separately ingested.

## Related

- [[braintree]] - provider company route
- [[braintree-payment-platform]] - provider-level merchant, gateway and interaction-channel context
- [[braintree-payment-methods]] - provider-wide method eligibility route; this FAQ does not itself enumerate method coverage

## Raw Sources

- [[raw/braintree/in-person/reference/faq-2026-09-16|Braintree In-Person FAQ (2026-09-16 snapshot)]]
