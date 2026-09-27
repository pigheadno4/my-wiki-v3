---
title: "Braintree Control Panel Expiring and Expired Cards Report"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/expiring-cards"
raw_files:
  - "braintree/articles/control-panel/reporting/expiring-cards-2026-09-16.md"
tags: [braintree, control-panel, reporting, expiring-cards, vault, recurring-billing]
---

## Overview

This collected Braintree article documents the Control Panel Expiring Cards report, which lists cards that have expired or will expire within a selected time frame. It is a visibility tool that can support recurring-billing follow-up; running it does not itself update a card, contact a customer, or request an Account Updater refresh.

## Key takeaways

- The report identifies expired and soon-to-expire cards for a chosen time frame. The article gives recurring billing as a use case and suggests pulling cards that will expire within the next month so the merchant can send customers update reminders.
- Merchants run the report from the Control Panel's **Reports** navigation under **Vault**. They can choose a custom date range or use **View All Expired** for the comprehensive expired-card list.
- Separately, depending on account setup, most Braintree Direct merchants domiciled in the US or transacting primarily with US customers may be able to enable Account Updater to request vaulted-payment-method updates automatically. That qualified option is not an action performed by the report.

## Detail locators

- Report scope, recurring-billing use case and merchant reminder example: `# Expiring and Expired Cards`, line 16.
- Control Panel route, custom date range and all-expired view: `## Running an Expiring Cards report`, lines 21-28.
- Account-setup, merchant and US qualifications for the separate Account Updater option: `## Reducing expired cards`, lines 31-33.

## Evidence boundary

> [!warning] Identification is not card updating or customer outreach
> The report lists expired or soon-to-expire cards. The article describes reminder emails as a merchant action and Account Updater as a separately enabled, account-qualified option; it does not state that running the report changes vaulted payment methods, sends reminders, enrolls a merchant in Account Updater, or guarantees updated card details.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[recurring-payments]]

## Related raw API references

- [[raw/braintree/articles/guides/account-updater-2026-09-16|Braintree Account Updater guide]] - navigation-only destination linked for the separately enabled update service; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/expiring-cards-2026-09-16|Braintree Control Panel Expiring and Expired Cards article]] - complete collected article covering report scope, Control Panel filters and the separate qualified Account Updater route
