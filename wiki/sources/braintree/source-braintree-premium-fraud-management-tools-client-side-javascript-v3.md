---
title: "Braintree Premium Fraud Management Tools Client-Side Implementation (JavaScript v3)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, premium-fraud-management, javascript, device-data, data-collector]
---

## Overview

This collected Braintree JavaScript v3 client-side implementation guide describes how a checkout page collects customer-device information with `dataCollector` and hands the resulting `deviceData` string to the merchant server. It covers custom integrations and Drop-in, plus a conditional FraudNet initialization callback and an automatic-vault verification caveat.

This is client-side integration evidence from a 2026-09-16 website snapshot. It does not document how the server attaches device data to a transaction or verification, identify which named Premium Fraud Management Tool is enabled, or establish current SDK support, merchant eligibility, account enablement, a fraud decision, processor approval, settlement, or protection from chargebacks. Named products such as **Fraud Protection**, **Fraud Protection Advanced**, and chargeback-protection tools are not interchangeable with this umbrella implementation route.

## Key takeaways

- For a custom integration, the page loads the Braintree Web client and data-collector components, creates an authorized client, and passes that client to `braintree.dataCollector.create`. It says the resulting `deviceData` string must be provided to the merchant server; injecting it into a form as a hidden input is presented only as a common mechanism, not as the sole required transport.
- The same Braintree client can be reused for `dataCollector` and other components such as Hosted Fields or PayPal. Callback and Promise examples, script URLs, form wiring, and error-handling shapes remain in the raw locators rather than being treated as invariant API guarantees.
- For Drop-in, setting `dataCollector: true` makes `requestPaymentMethod` include `deviceData` alongside the payment-method nonce for server handoff. This client-side response does not itself show server receipt, risk evaluation, payment execution, or successful processing.
- If an integration needs to use a CMID before FraudNet finishes loading, the page conditionally advises passing a `cb1` callback name to `dataCollector.create` and defining the named function on `window`; the callback is invoked after FraudNet initialization. This is troubleshooting advice for that race condition, not a universal prerequisite.

> [!warning] Automatic-vault verification boundary
> When a new payment method is automatically vaulted, the page says its verification is evaluated by Premium Fraud Management Tools without device data; subsequent transactions can still pass device data. Do not infer that automatic vaulting preserves device-data coverage for the initial verification.

> [!warning] Version, product, and snapshot boundary
> The `/javascript/v3` route identifies the guide family, while its custom script-tag example pins Braintree Web `3.87.0`; the snapshot does not establish a current recommended package version or compatibility with another retained SDK baseline. Its umbrella **Premium Fraud Management Tools** wording does not transfer capabilities, decisions, eligibility, liability treatment, or bypass behavior among named fraud products. Recheck current official guidance for operational decisions.

## Detail locators

- Device-data purpose and custom-versus-Drop-in branch: `## Collecting device data`, raw lines 17-21.
- Custom script tags, client reuse, `dataCollector` creation, callbacks, Promises and error examples: `### Custom`, raw lines 24-77.
- Returned `deviceData`, merchant-server responsibility and optional hidden-input transport example: `### Custom`, raw lines 78-129.
- Conditional CMID/FraudNet race callback: `### Troubleshooting fraudnet loading race condition`, raw lines 131-133.
- Drop-in `dataCollector: true`, `requestPaymentMethod`, nonce/device-data response and form examples: `### Drop-in`, raw lines 136-232.
- Automatic-vault verification warning: `### Drop-in > **NOTE**`, raw lines 234-235.
- PayPal Vault navigation and next-page server-side route: `### PayPal`, raw lines 240-244.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]

## Related raw API references

- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Premium Fraud Management Tools server-side Node.js guide]] - linked next-page family navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v3-2026-09-16|Braintree Premium Fraud Management Tools client-side implementation (JavaScript v3)]] - complete collected snapshot for custom and Drop-in device-data collection, merchant-server handoff, race-condition advice and the automatic-vault verification warning
