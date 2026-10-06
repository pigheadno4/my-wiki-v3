---
title: "Braintree In-Person Network Connection Test"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/post-launch-activities/network-connection-test"
raw_files:
  - "braintree/in-person/post-launch-activities/network-connection-test-2026-09-16.md"
tags: [braintree, in-person, card-reader, network-diagnostics, firmware]
---

## Overview

This collected 2026-09-16, unversioned [[braintree|Braintree]] website guide explains how to start a network connection test from a card reader's admin menu and interpret diagnostics for Braintree endpoint reachability, outside-internet access, a speed check and time-server access. The snapshot says the feature is supported in firmware version 5.1.0 and newer. It is not current firmware or feature-availability evidence, an observed test from a merchant's device or network, or proof of reader health, pairing, a transaction, authorization, payment, settlement or funding.

## Key takeaways

- The documented device interaction is to open the reader admin menu by pressing `2 + 8`, authenticate, and select **Run Connection Test**. The page gives `123456` only for test devices; production devices use a password provided to the operator.
- The page names four states: **Testing**, **Unavailable**, **Failed** and **Success**. It says some tests cannot run when the reader is not paired to a Location ID. The pictured E285 output is explicitly an example, so neither the image nor the listed states establish an actual reader result.
- The Braintree endpoint check covers the Braintree Public API, Reader API and Websocket API. For each endpoint, the guide separates URL parsing, DNS resolution, TCP connection and server-error steps. Its failure explanations are diagnostic categories: for example, a TCP failure may reflect the router, internet availability or Braintree platform availability, and therefore is not by itself a uniquely identified root cause.
- The outside-internet network test uses ICMP ping and DNS-resolution steps. The separate speed test can be **Failed** when internet is unavailable or **Unavailable** when the reader is not paired, and its documented failure steps are URL parsing and URL retrieval. Although the section is named **Speed Test**, this captured page publishes no latency value, unit, threshold or performance requirement; a connectivity or device-displayed speed result remains diagnostic evidence, not transaction or payment proof.
- A failed Time Server test is described as the reader being unable to retrieve date and time because NTP is blocked, with instructions to check firewall settings and follow the separate Braintree-domain allowlist route. The linked allowlist and troubleshooting pages require their own evidence.

## Material warnings

> [!warning] Diagnostic result boundary
> The result names and failure tables explain how to interpret a reader-side network diagnostic. They are not recorded results from a specific device or network and do not establish reader readiness, transaction creation, authorization, capture, payment success, settlement or funding.

> [!warning] Version, pairing and credential qualifications
> In this snapshot the feature starts at firmware 5.1.0, some tests may be unavailable until the reader is paired to a Location ID, and the displayed `123456` password applies only to test devices. Production credentials are separately provided.

## Detail locators

- Purpose and firmware qualification: introduction and **NOTE**, raw lines 14-19.
- Admin-menu key sequence, test-versus-production credential distinction and diagnostic start control: `## How to run a connection test on the card reader`, raw lines 22-31.
- E285 example-image label and **Testing**, **Unavailable**, **Failed** and **Success** meanings, including the Location ID pairing condition: raw lines 35-47.
- Three Braintree endpoints, displayed failed examples, four per-endpoint steps and failure explanations: `## Braintree Endpoint Check`, raw lines 52-69.
- Outside-internet purpose, network failure meaning, ICMP-ping and DNS steps: `## Internet Connection Check` and `#### Network Test`, raw lines 72-86.
- Speed-test **Failed** and pairing-dependent **Unavailable** rows plus URL-parsing and retrieval failure explanations: `#### Speed Test`, raw lines 89-99.
- Time-server failure, date/time retrieval, NTP and firewall/allowlist guidance: `#### Time Server Test`, raw lines 102-105.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- Braintree In-Person app version release notes (`/braintree/in-person/reference/app-version-release-notes/#version510`) - linked navigation only; not read as evidence for current firmware support.
- Braintree In-Person setup-reader pairing and domain-allowlist sections (`/braintree/in-person/guides/setup-reader/`) - linked navigation only for this source entry; pairing and allowlist details require their own source evidence.
- Braintree In-Person troubleshooting and support/contact routes - linked navigation only; not read as evidence.

## Raw Sources

- [[raw/braintree/in-person/post-launch-activities/network-connection-test-2026-09-16|Braintree In-Person Network Connection Test (fetched 2026-09-16)]]
