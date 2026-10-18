---
title: "Manage split configuration profiles in Customer Area | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/customer-area"
raw_files:
  - "adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/customer-area/2026-09-15.md"
tags: [adyen, platforms, automatic-splits, customer-area, balance-accounts]
---

## Overview

This Adyen for Platforms guide shows how a platform-model integration can use Customer Area to view merchant-account split-configuration profiles, add or remove rules, edit rule conditions or split logic, and delete a profile. It is a 2026-09-15 snapshot of configuration guidance, not evidence that a particular profile was changed or a transaction booked. Its key operational warning is that profiles are re-evaluated at capture: an edit can affect a payment authorized before the edit and captured afterward. [[adyen]] [[adyen-platforms]] [[adyen-automatic-split-configuration]]

## Key takeaways

- The operator needs the Customer Area role **Manage new split configuration settings** and must switch to the relevant merchant account. Under **Platform > New split configuration**, the list shows profiles configured for that merchant account, including store-use count, last-update date and profile ID; opening a profile shows its rules and split instructions. This page does not describe obtaining the role or prove a particular user's access.
- A rule can be added to an existing profile even after the profile has been applied to a store. Customer Area condition dimensions are shopper interaction/channel, payment method or variant, card funding source, and currency. The rule's split logic can specify a platform commission to the liable balance account, optional additional commission to a specified balance account, and account choices for payment fees, surcharge, potential chargeback and tips. Fixed fee amounts are stated in minor units; variable fees are percentages here. The page does not state the full priority algorithm for multiple matching rules; see the automatic-split overview for that hierarchy.
- An operator can edit a rule's conditions or split logic with **Edit rule** or **Edit logic**, preview and save. New conditions evaluate subsequent transactions, and new split logic governs subsequent transactions and associated fees. The guide explicitly says profiles are re-evaluated at capture, so newly added rules and changed conditions or logic can apply to payments authorized before the change but captured afterward. Treat rule edits as financially consequential configuration changes, while keeping actual booking subject to transaction evidence.
- A profile must retain at least one rule. The only rule cannot be removed; deleting the whole profile is the documented alternative. The page gives Customer Area steps to delete a profile but does not describe whether deletion unlinks stores, which fallback then applies, or the outcome for already authorized payments. Verify those effects before deleting a live profile.
- Customer Area cannot update the profile description or card-region condition; this snapshot routes both updates to the Management API. The page identifies the profile ID in the list but does not provide rule or logic IDs for Customer Area edits. It covers profile management, not initial profile creation, store linking, request-level split precedence, or proof of capture/settlement/payout.

## Detail locators

- Purpose, role, platform-model scope, and Management API-only limitations: pinned raw lines 15–34 (`## Requirements`).
- Merchant-account profile list, store count, last update, profile ID and rule details: pinned raw lines 36–60 (`## View all profiles`; `## View profile details`).
- Adding a rule, condition values, split-logic choices and effect on earlier authorizations at capture: pinned raw lines 62–120 (`## Add a rule`).
- Changing conditions and capture-time effect: pinned raw lines 122–161 (`## Change the conditions`).
- Changing split logic, fee effects and capture-time re-evaluation: pinned raw lines 163–201 (`## Change the split logic`).
- At-least-one-rule limit and profile deletion UI steps: pinned raw lines 203–222 (`## Remove a rule`; `## Delete a profile`).

## Related

- [[adyen-automatic-split-configuration]] — rule selection, request precedence and capture behavior for this Platforms configuration route.
- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — profile creation, Support enablement, Management API schema and store association.
- [[adyen-platforms]] — platform/user and liable-account context.

## Raw Sources

- [[raw/adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/customer-area/2026-09-15|Manage split configuration profiles in Customer Area — 2026-09-15 snapshot]]
