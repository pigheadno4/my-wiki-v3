---
title: "Braintree In-Person Managing Firmware Updates"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/post-launch-activities/managing-firmware-updates"
raw_files:
  - "braintree/in-person/post-launch-activities/managing-firmware-updates-2026-09-16.md"
tags: [braintree, in-person, card-reader, firmware, graphql]
---

## Overview

This collected 2026-09-16, unversioned [[braintree|Braintree]] website guide documents two ways to facilitate firmware updates for Braintree card readers: an install control in the reader admin menu and a GraphQL mutation sample. It says the reader must be powered on and connected to the internet, and recommends testing new versions in Sandbox before production. This snapshot is guidance, not evidence of a current release, a specific device's installed firmware, present support or enablement, a successful update, reader readiness, or payment execution. [[braintree-in-person]]

## Key takeaways

- For the reader-admin route, the page directs the operator from the PayPal-branded screensaver to press `2 + 8`, enter a passcode, and inspect the installed version. The displayed `123456` passcode is expressly Sandbox-only; production uses a different passcode obtained from PayPal support.
- When an update is available, the documented admin screen displays **Install Update**. Selecting it downloads and installs the update, and the reader restarts; the page says the reader is ready for use after it returns to the PayPal-branded screensaver. These instructions do not prove that an update is available or completed on any particular reader.
- The GraphQL section supplies a `requestFirmwareUpdateFromInStoreReader` mutation example whose input contains `readerId` and whose sample response includes context, reader status and `softwareVersion`. The example is not a guarantee of status, version, successful update, compatible hardware, account eligibility or production enablement.
- The linked firmware release notes, beta Reader Management System page and troubleshooting page are navigation routes only here; their version inventory, beta scope and troubleshooting behavior require their own fully read evidence.

## Material warnings

> [!warning] Environment and credential boundary
> The numeric passcode shown by this snapshot applies only to Sandbox. Production uses a different support-provided passcode, and the page does not establish current access, credential delivery or authorization for a particular operator or reader.

> [!warning] Snapshot and outcome boundary
> A documented control, mutation, sample response or return to the screensaver is not observed proof of current firmware availability, the installed version on a merchant device, update success, reader health or readiness, transaction processing, authorization, capture, payment, settlement or funding.

## Detail locators

- Page purpose and statement that there are primarily two update routes: raw lines 14-16.
- Why updates are published, powered-on and internet-connection conditions, Sandbox-before-production recommendation and release-note navigation: `## Why are Firmware Updates Important?`, raw lines 19-23.
- Reader-admin route and Sandbox-versus-production passcode distinction: `## 1) How to install an update to the Reader using the admin menu on the reader`, raw lines 24-29.
- Installed-version display, conditional **Install Update** control, download/install action, restart and screensaver return: raw line 31.
- GraphQL route, `requestFirmwareUpdateFromInStoreReader` mutation, `readerId` input and sample response fields: `## 2) How to install an update to the Reader using the GraphQL API`, raw lines 34-36.
- Reader Management System beta and troubleshooting navigation: raw line 36; linked pages were not read as evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[source-braintree-in-person-reference-app-version-release-notes|Braintree In-Person Payment Application Version Release Notes]] - linked release-note inventory; separate source authority, not used here to assert a current version or device state.
- Reader Management System (RMS) - Available in Beta Only - linked navigation only; beta scope and behavior require separate evidence.
- Troubleshooting - linked navigation only; troubleshooting behavior requires separate evidence.

## Raw Sources

- [[raw/braintree/in-person/post-launch-activities/managing-firmware-updates-2026-09-16|Braintree In-Person Managing Firmware Updates (fetched 2026-09-16)]]
