---
title: "Braintree In-Person Troubleshooting"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/post-launch-activities/troubleshooting"
raw_files:
  - "braintree/in-person/post-launch-activities/troubleshooting-2026-09-16.md"
  - "braintree/in-person/reference/app-version-release-notes-2026-09-16.md"
tags: [braintree, in-person, troubleshooting, card-reader]
---

## Overview

This 2026-09-16 unversioned [[braintree]] In-Person website snapshot is a post-launch troubleshooting guide for reader firmware, payment-app restart and reader shutdown, Sandbox connectivity, network/firewall reachability, reader-admin diagnostics, and support escalation. It routes through [[braintree-in-person]].

The snapshot documents troubleshooting actions and navigation, not current device or feature availability, merchant eligibility or enablement, exact API schema, deployed runtime or installed-version state, reader health, or successful payment, settlement or funding outcomes.

## Key takeaways

- A reader firmware update can sometimes resolve an issue when a known bug was fixed in the payment app; the guide routes to the firmware-management page rather than guaranteeing that an update will resolve the issue.
- On the pictured error screen, the guide directs the user to follow the **Restart the App** prompt to restart the payment app. Alternatively, pressing and holding the green circle button reboots the device. Reader shutdown is a separate action: unplug the device from its power source or press and hold the pictured red button for at least five seconds.
- For a Sandbox connection failure, the guide says to check Sandbox credentials and the reader's Wi-Fi connection, then contact support if the problem continues.
- When the reader is on the local network but cannot reach Braintree, the guide identifies an onsite firewall as a possible cause and routes readers to the Braintree endpoint whitelist and network diagnostics.
- The troubleshooting snapshot says Network Diagnostics is supported as of payment-application version 5.1.0 and describes access from the reader admin menu by pressing `2+8`, entering the admin-menu password, and selecting **Run Connection Test**. The separately reviewed [[source-braintree-in-person-reference-app-version-release-notes]] snapshot identifies 5.1.0 as Sandbox-only and 5.2.0 as the production release for those features. These historical release statements do not establish current availability or enablement, or the version installed on a merchant's reader.
- The stated purpose of the diagnostics tool is to help identify where network communication is breaking down; the page does not establish a successful repair or transaction outcome. If the troubleshooting tips do not resolve the issue, the guide routes to the contact page and asks for detailed issue information.

## Detail locators

- Firmware-update rationale and firmware-page route: troubleshooting raw lines 17-21.
- Payment-app restart and reader shutdown actions: troubleshooting raw lines 22-29.
- Error-screen app-restart prompt and alternative device reboot: troubleshooting raw lines 32-34.
- Sandbox credentials, Wi-Fi and support route: troubleshooting raw lines 37-39.
- Firewall, endpoint-whitelist and diagnostics routes: troubleshooting raw lines 42-44.
- Version-qualified network diagnostics access and purpose: troubleshooting raw lines 47-51.
- Support escalation: troubleshooting raw lines 52-54.
- 5.1.0 Sandbox-only qualification, 5.2.0 production-release direction and Network Diagnostics feature: payment-application release-notes raw lines 218-239.

## Related

- [[braintree]]
- [[braintree-in-person]]
- [[source-braintree-in-person-reference-app-version-release-notes]]

## Related raw API references

The troubleshooting snapshot links to adjacent Braintree In-Person pages for firmware management, endpoint whitelisting/setup, the network connection test, and support contact. Those linked pages are navigation only here unless separately ingested and reviewed.

## Raw Sources

- [[raw/braintree/in-person/post-launch-activities/troubleshooting-2026-09-16|Braintree In-Person Troubleshooting (2026-09-16)]]
- [[raw/braintree/in-person/reference/app-version-release-notes-2026-09-16|Braintree In-Person Payment Application Version Release Notes (2026-09-16)]]
