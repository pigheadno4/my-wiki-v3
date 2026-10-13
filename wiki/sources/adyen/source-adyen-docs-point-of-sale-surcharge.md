---
title: "Adyen point-of-sale surcharge overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/surcharge"
raw_files:
  - "adyen/docs/point-of-sale/surcharge/2026-09-15.md"
tags: [adyen, point-of-sale, surcharging, terminal-api, disclosure, dcc]
---

## Overview

This Adyen Docs overview describes passing payment acceptance fees to shoppers as a **point-of-sale surcharge**. It compares configuration-based rules with a dynamic merchant/third-party calculated amount sent in an integrated payment request. The selected in-person solution and hardware determine which method is supported. This POS guide is separate from Adyen's online-payments API-only surcharge pilot; neither page alone proves current merchant enablement or legal compliance.

## Key takeaways

- Configuration-based surcharges are calculated automatically from rules that can consider card brand, funding source, issuing country, and currency at company/merchant, store, or terminal scope. Dynamic surcharge uses merchant or third-party calculation, possibly after card acquisition, and puts the calculated fee in the payment request. Standalone terminals support **configuration-based only**. If both methods are configured for an integrated transaction, a surcharge amount in the request **overrides** the configured surcharge rather than adding a second one. The detailed method pages carry setup and request mechanics.
- The snapshot lists availability in Australia, Canada, Europe, Great Britain, New Zealand, and the United States, with local and scheme restrictions still applying. It gives EEA-issued consumer cards used in the EEA and US debit cards as examples where surcharge is disallowed. Adyen says the feature does not enforce global compliance automatically: merchants must review current law/scheme rules and disclose applicable methods and costs. The Terminal API receipt data include the surcharge on shopper and merchant receipts; a customized receipt puts disclosure responsibility on the merchant. Standalone built-in printing is described separately.
- A terminal may present a surcharge confirmation screen showing total, surcharge, and payment method. A Mobile solution does **not** support that screen in this snapshot, but disclosure remains required. The merchant may choose another disclosure form; `surcharge.askConfirmation` is a Management API terminal setting, with Support as the route if the merchant cannot configure the feature. The guide does not establish Customer Area roles or account-specific permission from these instructions.
- A surcharge and DCC cannot apply to the **same transaction**. For terminal software earlier than v1.112 Adyen recommends not configuring both features on the same terminals; at v1.112 or later Adyen says DCC is automatically skipped when surcharge is greater than zero. Surcharges also cannot be added to authorization adjustments or overcaptures because they cannot exceed what was shown at purchase. These version and disclosure constraints are POS-specific and do not imply identical online pilot behavior.
- For reporting visibility, Adyen recommends enabling surcharge data in Standard `AUTHORISATION` webhooks via **Include Extra Costs Surcharge** or **Developers > Additional data > Surcharge amount**. The fields are `extraCostsCurrency` and `extraCostsValueSurcharge` in minor units; adding a Surcharge Amount column to Payment Accounting and Settlement Detail reports is also recommended. The sample webhook is illustrative and does not establish capture, refund, settlement, or downstream fee outcomes.

## Detail locators

- Method-dependent hardware, snapshot regions, Mobile/DCC/adjustment limits, and compliance preparation: `## Requirements`, raw lines 21–34. Local restriction examples, signage, receipt responsibilities: `## Compliance`, lines 36–50.
- Configuration versus dynamic calculation, scope, standalone boundary, and override precedence: `## Surcharge methods`, raw lines 52–73. Terminal disclosure, Mobile exception, Management API setting: `## Surcharge confirmation screen`, lines 75–97.
- DCC mutual exclusion and firmware-qualified behavior: `## Surcharge or DCC`, raw lines 99–105. Optional webhook/report visibility and minor-unit fields: `## Surcharge in AUTHORISATION webhooks` and `## Surcharge in reports`, lines 107–167. Linked detailed method routes: `## Next steps`, lines 169–180.

## Related

- [[adyen]] — provider context.
- [[adyen-surcharging]] — Adyen surcharge concept; keep POS methods separate from online pilot implementation.
- [[adyen-terminal-api]] — integrated terminal payment and receipt context.
- [[adyen-webhooks]] — separate Standard webhook configuration and outcome handling.
- [[source-adyen-docs-point-of-sale-surcharge-configuration]] — linked configuration-based detail; do not infer its full setup from this overview.
- [[source-adyen-docs-point-of-sale-surcharge-dynamic]] — linked POS dynamic detail; separate from online surcharge pilot.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/surcharge/2026-09-15|Adyen Docs: Surcharge (2026-09-15 snapshot)]]
