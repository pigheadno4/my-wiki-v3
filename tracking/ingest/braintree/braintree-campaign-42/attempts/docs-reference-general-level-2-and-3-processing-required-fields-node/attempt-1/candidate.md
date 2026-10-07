---
title: "Braintree Level 2 and 3 Required Fields (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/level-2-and-3-processing/required-fields/node"
raw_files:
  - "braintree/docs/reference/general/level-2-and-3-processing/required-fields/node-2026-09-16.md"
tags: [braintree, node-js, transactions, level-2, level-3, line-items]
---

## Overview

This collected Braintree website reference describes Level 2 and Level 3 data supplied in Node.js transaction requests. It shows `gateway.transaction.sale()` callback and Promise examples and a separately approval-gated `gateway.transaction.submitForSettlement()` route. The page is an unversioned website snapshot with body metadata updated 2026-06-09 and raw fetched 2026-09-16; it is not package-version, exact deployed-schema, current eligibility, interchange-result or transaction-outcome evidence.

## Key takeaways

- The page says a transaction must include the Level 2 fields to qualify for Level 2 processing. Its captured required-field bullets are blank, while the Node sale examples show `purchaseOrderNumber` and `taxAmount`; use the raw code locator as an example, not as proof of a complete field contract. The page also says the required-field values determine lower-interchange qualification, but the captured sentence that gives Visa and Mastercard percentage ranges omits the field name, so this source does not reconstruct that missing subject.
- To qualify for Level 3 processing, the page requires Level 2 data plus additional Level 3 data and line items. The visible raw list names `line_items.name`, `line_items.kind`, `line_items.quantity`, `line_items.unit_amount`, `line_items.unit_of_measure`, `line_items.total_amount`, `line_items.tax_amount`, `line_items.discount_amount`, `line_items.product_code` and `line_items.commodity_code`; adjacent Level 3 field bullets are blank. The Node examples use camelCase request keys. Preserve those displayed naming contexts rather than treating the field labels as a complete executable API contract.
- Processor amount validation compares line-item totals with the root transaction amount, and a discrepancy may decline the transaction. The page gives a calculation using item totals, tax, shipping, shipping tax and discount; it separately warns that EU and UK transactions with non-zero shipping amount may be rejected when shipping tax is zero. Use the raw formula and Node example for the exact displayed arithmetic and values.
- For selected line-item fields, the page limits statement-safe characters to letters, digits, apostrophe, period, hyphen and spaces. Other characters may still qualify for Level 3 processing, but the page says unsupported characters are converted to spaces on the cardholder statement. The captured bullets naming the affected fields are blank, so their identities are not reconstructed here.
- Supplying Level 2/3 data through `submitForSettlement()` requires internal approval. This route applies the data at settlement submission instead of the sale call, overrides all Level 2/3 data previously supplied in the sale request, and is recommended as an either/or choice rather than using both request points.
- A transaction result may contain Level 3-field or line-item validation errors when a value's format or length is outside expected bounds. This validation statement does not establish that all semantic, processor, eligibility or amount problems produce the same error route.

> [!warning] Snapshot, eligibility and outcome boundaries
> Field supply and example calls do not establish merchant, account, processor, card or region eligibility; internal approval for the settlement-submission route; lower interchange; current Node SDK support; exact gateway acceptance; or authorization, settlement and funding of an individual transaction. Several captured required-field bullets and one Level 2 range sentence are incomplete, so consult the exact raw locators and current Braintree authority rather than filling those gaps from field labels or examples.

## Detail locators

- Level 2 qualification statement, blank captured field bullets and incomplete interchange-range sentence: `## Level 2 data`, lines 17-30.
- Node callback and Promise sale examples for the displayed Level 2 request keys: `### Creating a transaction`, lines 31-54.
- Level 3 dependency on Level 2, CEDP context, blank additional-field bullets and visible `line_items.*` labels: `## Level 3 data`, lines 56-85.
- Character-set behavior and the missing affected-field bullets: `### Supported characters`, lines 89-99.
- Processor total comparison, possible decline, EU/UK shipping-tax condition and displayed formula: `### Amount validation`, lines 100-106.
- Full amount-validation Node example and its exact camelCase names and values: `### Amount validation > ### node`, lines 108-147.
- Callback and Promise examples described by the page as using minimum required Level 3 fields: `### Creating a transaction`, lines 149-230.
- Internal-approval requirement, settlement-time purpose, override effect and either/or recommendation: `### Specifying level 2 and 3 data when submitting for settlement`, lines 232-240.
- Full callback and Promise settlement-submission examples: lines 243-315.
- Qualified validation-error behavior and separate error-reference route: `## Validation errors`, lines 317-321.

## Related raw API references

The captured page links to the transaction sale tax-amount route, Braintree contact route and Level 3 validation-errors reference. Those linked targets are navigation only here and are not imported as behavioral evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Overlapping settlement-operation route: [[source-braintree-transaction-submit-for-settlement-node]]
- In-Person comparison route: [[source-braintree-in-person-guides-making-a-transaction-level-2-and-level-3-data-processing]]

## Raw Sources

- [[raw/braintree/docs/reference/general/level-2-and-3-processing/required-fields/node-2026-09-16|Braintree Node.js Level 2 and Level 3 required-fields reference]] - complete collected page covering sale-time examples, line-item and amount rules, approval-gated settlement-time override behavior and validation-error navigation
