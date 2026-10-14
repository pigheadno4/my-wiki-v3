---
title: "Adyen Docs: Standalone terminal setup"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone"
raw_files:
  - "adyen/docs/point-of-sale/standalone/standalone-build/set-up-standalone/2026-09-15.md"
tags: [adyen, point-of-sale, standalone, terminal-settings]
---

## Overview

Adyen's standalone setup guide, captured 2026-09-15, explains how to make **test** payment terminals ready to accept transactions directly on the terminal, with optional tipping and refund-passcode settings. It offers Customer Area and Management API configuration paths. This standalone device path is distinct from a merchant POS app sending [[adyen-terminal-api|Terminal API]] payment requests. Live terminals need their own setup when going live; this snapshot does not establish account eligibility, current device support, or a successful payment.

## Key takeaways

- The guide requires a standalone-capable terminal. For Customer Area setup it names Merchant POS Terminal Management and Merchant POS Terminal View roles. API setup needs an API key with Management API Terminal settings read/write and Terminal Advanced settings read/write roles; a cloud Terminal API integration's existing API key can be reused if it has those roles. See **Requirements** in raw.
- In Customer Area, **Devices > Device settings > Integrations > Standalone** includes enablement, Start button, currency, and optional transaction reference. At company, merchant, store, or individual-terminal scope, the Management API path PATCHes the corresponding `/terminalSettings` endpoint with `standalone.enableStandalone` and `standalone.currencyCode`. The latter is a default three-digit ISO 4217 code. See **Set up standalone > Tab: Customer Area** and **Tab: API** in raw.
- After Customer Area Save, the terminal downloads configuration at its maintenance call (described as every 180 minutes); settings take effect after restart, normally at the configured restart hour. Manual terminal configuration update downloads and restarts immediately. See **Set up standalone > Tab: Customer Area**, step 4.
- Tipping can be a shopper-entered amount or predefined choices, configured in Customer Area or through Management API `standalone.enableGratuities` plus `gratuities`. The page limits predefined choices to four, or three plus a custom amount. Its Quebec section recommends manual entry or fixed CAD amounts with custom entry to facilitate pre-tax-tip compliance, and explicitly says not to use percentage options for the fixed-amount path. See **Configure tipping** and **Configure compliant tipping in Quebec, Canada** in raw. A POS app's per-payment tipping override belongs to a separate integrated flow.
- A standalone Refunds passcode is an optional six-digit safeguard **in addition to** the Transactions passcode: both are entered to initiate a refund. Configure it in Customer Area or PATCH `passcodes.refundPin` through Management API at company, merchant, store, or terminal scope. See **Configure refund passcode** in raw.
- If operating as a payment facilitator, the guide says to configure remaining required sub-merchant data on the sub-merchant's store. It routes test payment/refund execution to a separate testing guide; neither configuration nor that route proves a payment outcome. See **Payment facilitators** and **Testing** in raw.

## Detail locators

- **Requirements** — integration type, terminal hardware, role gates, Quebec limitation, and live-terminal setup reminder.
- **Set up standalone > Tab: Customer Area / Tab: API** — exact menu, endpoint scopes, request keys, test examples, and response visibility by API credential.
- **Configure tipping > Tab: Customer Area / Tab: API** — modes, maximum choices, Management API fields, and version-labeled SDK examples.
- **Configure compliant tipping in Quebec, Canada** — dated recommendation and CAD fixed-amount/manual-entry paths.
- **Configure refund passcode > Tab: Customer Area / Tab: API** — safety rationale, terminal update timing, exact endpoint and `refundPin` examples.
- **Payment facilitators / Testing** — conditional sub-merchant store data and separate test instructions.

## Related

- [[adyen]] — provider overview.
- [[adyen-terminal-api]] — integrated merchant POS-to-terminal messaging; different payment initiation path.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/standalone/standalone-build/set-up-standalone/2026-09-15|Standalone setup (2026-09-15 snapshot)]]
