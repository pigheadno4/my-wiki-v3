---
title: "Braintree In-Person Setup Reader"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/setup-reader"
raw_files:
  - "braintree/in-person/guides/setup-reader-2026-09-16.md"
tags: [braintree, in-person, card-reader, verifone-p400, sandbox, graphql, network-setup]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide documents how to assemble and network a Braintree Dev Kit P400 reader, check its available software update, create a Braintree in-store location, and pair the reader to a Braintree Sandbox Account. It is a Sandbox setup and reader-management route, not evidence of production provisioning, payment-method enablement, reader-online state, or a successful card-present transaction.

## Key takeaways

- The documented starting set includes the Braintree Dev Kit P400 hardware and cables, test cards, a Braintree Sandbox Account configured for Dev Kit testing, Braintree GraphQL documentation, and WiFi or Ethernet. The page recommends its In-Person Postman collection for making GraphQL requests; that recommendation does not make Postman an API or runtime requirement.
- Online reader operation requires internet connectivity. For a restrictive LAN firewall, the guide says rules must allow incoming and outgoing communication to and from the reader and supplies environment-labeled Braintree, time-service and S3 domains to whitelist. Network selection, password entry, DHCP versus static IPv4 fields, recovery after a failed connection, device-settings access and status-bar interpretation remain at the raw locators below.
- The guide says to make sure the reader is on the latest available version and describes checking the installed and available-to-update versions in device settings. Its test-device admin password is explicitly different from production-device credentials. The collected page does not establish the currently available version.
- This flow is specifically for pairing a Dev Kit reader to a Sandbox Account. A Dev Kit reader may be paired to only one Sandbox Account. Pairing requires at least one defined location; the initial request associates the reader with the created `location.id` and uses the six-character `userCode` displayed by the reader, which the page says refreshes every five minutes until pairing.
- Reader, context and transaction states are distinct. The on-device screen first represents pairing mode; the guide's sample pairing response shows `status: OFFLINE`; and the success screen represents connection to the Braintree Sandbox Account. The page then routes separately to a transaction guide. Neither the sample response nor successful setup proves that the reader is online, that production or payment methods are enabled, or that any authorization, sale, settlement or funding occurred.

## Material warnings

> [!warning] Sandbox and outcome boundary
> The guide's completed flow connects a Dev Kit reader to a Braintree Sandbox Account. Setup, location creation, a pairing request or a success screen must not be treated as production provisioning, live-payment enablement, reader-online proof or transaction success.

> [!warning] Network reconfiguration effect
> The page says resetting network configuration after a connection failure causes the device to enter the network-pairing flow again on reboot. Static IP assignment also requires a network administrator to avoid duplicate address use; the exact fields and recovery choices are retained in the raw.

## Detail locators

- Dev Kit P400 components, test cards, configured Sandbox Account, GraphQL documentation, network and Postman recommendation: `## What you will need to get started`, lines 19-54.
- Physical assembly, power-up and Start Setup screen: `## Step 1: Install the Hardware`, lines 59-85.
- Internet/firewall requirement and environment-labeled domain allowlist: `## Step 2: Network Configuration Requirements` and `### Braintree Domains to Whitelist`, lines 88-108.
- WiFi/Ethernet selection, WiFi password key map, DHCP/static IP choice and fields, reset behavior, device-settings access and network-status display: `### Connect to the Internet` through the end of Step 2, lines 110-192.
- Available-versus-installed software version check, update path and test-versus-production admin-password distinction: `## Step 3: Check for Reader Update`, lines 195-208.
- GraphQL/Postman or Reader Management System routes, Sandbox scope and one-Sandbox-account limit: `## Step 4: Connect to Sandbox`, lines 211-218.
- Location prerequisite, returned identifier, QR-code `internalName` qualification and example mutation/response: `### Create Location ID`, lines 221-228.
- Pairing-mode screen, Sandbox account and location association, six-character rotating `userCode`, example mutation and sample `OFFLINE` response state: `### Pair Reader to a Location ID`, lines 231-244.
- Optional location update and reader reassignment examples: `### Update an Existing Location (Optional)` and `### Update Reader Location Pairing (optional)`, lines 245-254.
- Reader-ID retention guidance, Sandbox success state and separate make-a-transaction route: `## Success!` and `## All set!`, lines 255-265.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/get-started-1/configure-sandbox-2026-09-16|Configure Sandbox]] - unread navigation linked by the setup guide
- [[raw/braintree/in-person/reference/app-version-release-notes-2026-09-16|App version release notes]] - unread navigation linked by the setup guide
- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|Making a transaction]] - unread next-step navigation linked by the setup guide

## Raw Sources

- [[raw/braintree/in-person/guides/setup-reader-2026-09-16|Braintree In-Person Setup Reader]] - complete collected guide for Dev Kit P400 hardware and network setup, software update checking, Sandbox location creation and reader pairing
