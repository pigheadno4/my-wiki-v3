---
title: "Adyen Docs: Assign terminals in Customer Area"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/assign-terminals"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, customer-area, terminal-assignment]
---

## Overview

This Adyen guide, last modified 2024-08-19 and captured 2026-09-15, explains initial terminal assignment and reassignment through Customer Area for Terminal API or standalone payment terminals. Assignment sends a terminal from company inventory to a store or merchant account representing a store; the physical terminal must then be boarded. The page also points to assignment during boarding and Management API automation, but its detailed steps are for Customer Area. See [[adyen-terminal-management]], [[adyen-standalone-terminals]], and [[adyen]].

## Key takeaways

- Adyen adds shipped terminals to the **Inventory** of the company account. A user with **Merchant POS Terminal Management Admin** or **Manage terminals** Customer Area role can select terminals in **Devices > Device list > Terminals** and reassign them to a store, or back to inventory. Use the test Customer Area for a test terminal and live Customer Area for a live terminal. Pre-assignment by itself is not physical boarding or payment readiness.
- Customer Area also offers **Bulk reassignment** by CSV for many terminals or stores. The guide directs users to the Customer Area file-description and example links; it does not specify a durable CSV schema in this source.
- A terminal already boarded to an old store keeps that store's configuration until it synchronizes with Adyen. It then removes that configuration and displays **Board the terminal**, after which staff must board it again to obtain the new configuration. Keep the device powered on with stable internet; the guide says reassignment can take up to three hours because platform synchronization occurs every three hours.
- For faster effect, the guide points to enabling WebSockets **before** reassignment, or manually updating configuration for **non-Android** terminals. These are conditional routes, not proof of immediate completion. The device's observed state and boarding must be checked before using it at the new store.
- Assignment is a fleet-management action. The page does not report payment outcomes, hardware order creation, or current account-specific authorization. Management API assignment and manual boarding have separate linked procedures.

## Detail locators

- Three assignment routes, integration scope, Customer Area roles: [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Requirements|Requirements]] and the introduction immediately above it.
- Company inventory, environment selection and single-store assignment steps: [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Assign a terminal from your Customer Area|Assign a terminal from your Customer Area]].
- CSV file-instructions route and upload flow: [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Assign terminals in bulk|Assign terminals in bulk]].
- Old-store configuration, synchronization timing, WebSockets/non-Android alternatives and reboarding: [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Reassign boarded terminals|Reassign boarded terminals]].

## Related

- [[adyen-terminal-management]] — fleet administration and Management API route.
- [[adyen-standalone-terminals]] — standalone payment solution supported by this assignment guide.
- [[adyen-terminal-api]] — integrated POS payment messages, distinct from Customer Area assignment.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15|Adyen Assign terminals, 2026-09-15 snapshot]]
