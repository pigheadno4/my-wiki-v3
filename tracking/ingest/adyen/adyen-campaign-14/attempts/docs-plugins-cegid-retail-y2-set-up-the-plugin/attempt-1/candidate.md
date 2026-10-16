---
title: "Adyen Cegid Retail Y2 CPOS plugin setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2/set-up-the-plugin"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/set-up-the-plugin/2026-09-15.md"
tags: [adyen, cegid-retail-y2, pos, plugin, setup]
---

## Overview

Adyen’s setup guide for its Cegid Retail Y2 CPOS plugin covers installing the v2.1.33 file, configuring Adyen and Cegid Retail Y2 for local or cloud Terminal API communications, mapping terminal payment-method variants, configuring refunds, and moving from test setup to a live setup. It is a procedure for a merchant’s POS integration, not evidence that a particular merchant is eligible or has processed a live payment. See [[adyen-cegid-retail-y2]] for the plugin family.

## Key takeaways

- The v2.1.33 installation ZIP is password-protected; request its password from Adyen Support. For an existing integration upgrading to a later version, uninstall the older plugin and reboot the Cegid device before installing. The installer targets the CPOS directory; changing that directory after installation requires uninstalling and reinstalling. The later upgrade section says to repeat the download/install steps, without repeating the other setup steps.
- Adyen account configuration requires the Merchant POS Terminal Management Admin role and company account level. Local communications require enabling Terminal API and securely storing the encryption key identifier, passphrase, and version for the Cegid EPT settings. If encryption fields are unavailable, ask Support for the required permission. Cloud communications use a Web service API credential and securely stored API key, Terminal API enabled, and Support-enabled WebSockets.
- The plugin communicates only with terminals injected with Adyen software. The documented test path creates stores, orders test terminals and a test card, and boards the terminals. In Cegid, local EPT settings use the device IP `https://YOUR_DEVICE_IP:8443/nexo`, Local connection type, Sale ID, terminal POI ID, and the encryption key values. Cloud settings use the test sync endpoint for test or a geographically appropriate live endpoint for live, Cloud connection type, Sale ID, POI ID, and API key. The source’s local and cloud field tables are the authority for required versus optional fields.
- Cegid payment methods must be created and a mapping table activated so Adyen terminal `paymentMethodVariant` values map to Cegid values. A payment method’s Mixed direction permits refunds. The EPT payment configuration defaults to `D:CP,RR` (referenced refunds); `D:CP,NR` selects unreferenced as default. Referenced refunds need additional register settings, yet partial refunds and multi-method payments can use unreferenced refunds regardless of the default. Optional merchant-reference configuration requires administrator rights and a number length greater than the prefix length; otherwise CPOS uses date/time instead.
- Treat configuration choices carefully: the optional Allow Booking of Undetermined Payment accepts a payment with an unknown result after a failed transaction; Legacy Mode should remain off unless Cegid instructs otherwise; Confirm Void is recommended for explicit cashier confirmation. These settings are described in both EPT field tables.
- The guide’s device test checks plugin-terminal communication, followed by a separate test-card transaction and Cegid receipt check. Before real payments, it calls for new live terminals, repeating Adyen account configuration in the live Customer Area, and testing the configured integration. This source does not establish that those steps were performed or that a live payment succeeded.

## Detail locators

- Installation version, password, uninstall/reboot, CPOS path and EPT driver: pinned raw lines 23–55.
- Local versus cloud Customer Area credentials and WebSockets: pinned raw lines 57–105.
- Test terminal acquisition and boarding: pinned raw lines 107–115.
- Cegid EPT field-by-field requiredness, endpoints, timeouts, receipts, unknown-result booking, Legacy Mode and void handling: pinned raw lines 116–187.
- Cash-register authorization choices and payment-method mapping: pinned raw lines 188–249.
- Refund types and exceptions: pinned raw lines 250–267. Optional merchant reference and length rule: lines 269–284.
- Device test, test transaction, live transition and upgrade instructions: pinned raw lines 286–318.

## Related

- [[adyen]]
- [[adyen-cegid-retail-y2]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/set-up-the-plugin/2026-09-15|Adyen Cegid Retail Y2 CPOS setup snapshot (2026-09-15)]]
