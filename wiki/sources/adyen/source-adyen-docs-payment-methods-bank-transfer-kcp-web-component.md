---
title: "Bank Transfer via KCP Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/web-component"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/web-component/2026-09-15.md"
tags: [adyen, bank-transfer, kcp, web, components]
---

## Overview

This 2026-09-15 guide describes method-specific additions for Bank Transfer via KCP in existing Adyen Web Components integrations. It has separate Sessions and Advanced sections; both require Customer Area setup and redirect handling. It is not a complete standalone Web checkout guide. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Sessions requires an existing Web Components Sessions integration and Checkout API v68 or later. It calls for existing `action.type: redirect` handling and adding the method in Customer Area; no extra `/sessions` parameters or KCP-specific configuration parameters are stated. See raw lines 25–42 and 56–60.
- Advanced requires an existing Web Components Advanced integration with `action.type: redirect` handling and Customer Area setup; its `/payments` section says no additional parameters are needed. The v68-or-later statement is in the Sessions requirements, not the Advanced requirements. See raw lines 78–86 and 112–116.
- In both sections the guide says to include `Redirect` when importing Adyen Web and use the `Redirect` class for the KCP component. The shown initializer uses `type:kcp_banktransfer` without a quoted string or defined variable in the snippet, so treat it as an illustrative example rather than a verified runnable JavaScript fragment. See raw lines 44–72 and 88–110.
- The page says there are no KCP bank-transfer test credentials because authorization requires a Public Identification Certificate (a digital signature for individuals). The setup and redirect instructions do not establish a successful TEST or LIVE bank transfer or current merchant eligibility. See raw lines 74–76 and 118–120.

## Detail locators

- Sessions requirements, parameters, import and initialization: raw lines 25–72.
- Advanced requirements, import, initialization and `/payments` parameters: raw lines 78–116.
- Test-credential limitation: raw lines 74–76 and 118–120.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]] — separate method overview.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/web-component/2026-09-15|Bank Transfer via KCP Web Component (2026-09-15)]]
