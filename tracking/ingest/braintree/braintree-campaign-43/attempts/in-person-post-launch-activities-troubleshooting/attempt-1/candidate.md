---
title: "Braintree In-Person Troubleshooting"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/post-launch-activities/troubleshooting"
raw_files:
  - "braintree/in-person/post-launch-activities/troubleshooting-2026-09-16.md"
tags: [braintree, in-person, troubleshooting, card-reader]
---

## Overview

This 2026-09-16 unversioned [[braintree]] In-Person website snapshot is a post-launch troubleshooting guide for reader firmware, payment-app restart and reader shutdown, Sandbox connectivity, network/firewall reachability, reader-admin diagnostics, and support escalation. It routes through [[braintree-in-person]].

The snapshot documents troubleshooting actions and navigation, not current device or feature availability, merchant eligibility or enablement, exact API schema, deployed runtime state, reader health, or successful payment, settlement or funding outcomes.

## Key takeaways

- A reader firmware update can sometimes resolve an issue when a known bug was fixed in the payment app; the guide routes to the firmware-management page rather than guaranteeing that an update will resolve the issue.
- Holding the reader's green circle button restarts the payment app/device. On the pictured error screen, the guide directs the user to follow the **Restart the App** prompt or use that button action. Reader shutdown is instead performed by unplugging the power source or holding the pictured red button for at least five seconds.
- For a Sandbox connection failure, the guide says to check Sandbox credentials and the reader's Wi-Fi connection, then contact support if the problem continues.
- When the reader is on the local network but cannot reach Braintree, the guide identifies an onsite firewall as a possible cause and routes readers to the Braintree endpoint whitelist and network diagnostics.
- As of payment-app version 5.1.0, the network diagnostics tool is available from the reader admin menu: press `2+8`, enter the admin-menu password, and select **Run Connection Test**. The stated purpose is to help identify where network communication is breaking down; the page does not establish a successful repair or transaction outcome.
- If the troubleshooting tips do not resolve the issue, the guide routes to the contact page and asks for detailed issue information.

## Detail locators

- Firmware-update rationale and firmware-page route: raw lines 17-21.
- Payment-app restart and reader shutdown actions: raw lines 22-29.
- Error-screen restart path: raw lines 32-34.
- Sandbox credentials, Wi-Fi and support route: raw lines 37-39.
- Firewall, endpoint-whitelist and diagnostics routes: raw lines 42-44.
- Version-qualified network diagnostics access and purpose: raw lines 47-51.
- Support escalation: raw lines 52-54.

## Related

- [[braintree]]
- [[braintree-in-person]]

## Related raw API references

The troubleshooting snapshot links to adjacent Braintree In-Person pages for firmware management, endpoint whitelisting/setup, the network connection test, application release notes, and support contact. Those linked pages are navigation only here unless separately ingested and reviewed.

## Raw Sources

- [[raw/braintree/in-person/post-launch-activities/troubleshooting-2026-09-16|Braintree In-Person Troubleshooting (2026-09-16)]]
