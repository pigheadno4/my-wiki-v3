---
title: "FPX Online Banking Malaysia iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-drop-in/2026-09-15.md"
tags: [adyen, fpx, online-banking, malaysia, ios, drop-in]
---

## Overview

This 2026-09-15 Adyen page describes FPX Online Banking Malaysia additions to an existing iOS Drop-in integration, split into Sessions and Advanced server-side flows. It documents method-specific setup, request/configuration omissions, TEST guidance and a separate live request. It is not a standalone checkout or evidence of a completed bank payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The existing iOS Drop-in Sessions integration requires Checkout API v68 or later and FPX Online Banking Malaysia added in Customer Area. The page says there are no additional `/sessions` or method configuration parameters. It does not separately state a Sessions redirect-handling prerequisite on this page. (raw lines 25–46)
- **Advanced:** The existing iOS Drop-in Advanced integration must handle `action.type: redirect` and have FPX Online Banking Malaysia added in Customer Area. No extra method configuration or `/payments` parameters are stated. This section does not give an Advanced Checkout API minimum. (raw lines 58–80)
- **Test and live gates:** Both flow sections direct test payments using any issuer ID available for the Online Banking Malaysia Component in the relevant country/region, with status inspection in the TEST Customer Area. This is cross-reference guidance, not an issuer list on this page or proof of a particular result. Before accepting live payments, the merchant must submit a separate Online Banking Malaysia request in the live Customer Area. (raw lines 48–56, 82–90)
- **Scope boundary:** The page does not provide the issuer IDs, shopper bank/return sequence, webhook result processing, capture/refund rules or observed authorization. The FPX overview and main iOS integration guides are separate authority for those claims; TEST status or redirect setup does not prove authorization, capture or settlement. (raw lines 15–90)

## Detail locators

- Sessions prerequisites, `/sessions` and configuration: raw lines 25–46.
- Sessions TEST and live request instructions: raw lines 48–56.
- Advanced prerequisites, configuration and `/payments`: raw lines 58–80.
- Advanced TEST and live request instructions: raw lines 82–90.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]]
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-drop-in/2026-09-15|Adyen FPX Online Banking Malaysia iOS Drop-in guide, 2026-09-15 snapshot]]
