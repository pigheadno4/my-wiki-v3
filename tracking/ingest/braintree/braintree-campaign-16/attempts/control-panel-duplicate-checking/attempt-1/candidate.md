---
title: "Braintree Control Panel Duplicate Transaction Checking"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/duplicate-checking"
raw_files:
  - "braintree/articles/control-panel/transactions/duplicate-checking-2026-09-16.md"
tags: [braintree, control-panel, transactions, duplicate-checking, gateway-rejections]
---

## Overview

This collected Braintree article documents gateway-side duplicate transaction checking for repeated transaction requests, including its matching window, general and payment-method-specific conditions, immediate rejection behavior, and Control Panel configuration boundary. The article notes that repeated checkout actions can issue new API requests, but the operation it describes is gateway duplicate screening configured in the Control Panel, not an API or SDK request-construction guide. Its 2026-09-16 collection is evidence of the documented behavior at that snapshot, not proof of current support or settings.

## Key takeaways

- The article says duplicate transaction checking is enabled in the gateway by default. Its documented default window is 30 seconds, and the configuration section says the feature is enabled with that window in both Sandbox and Production.
- A suspected duplicate is Gateway Rejected only when all relevant conditions match within the configured timeframe. The general comparison covers amount, the applicable order-or-subscription identifier condition, and an initial transaction that the article classifies as successful; additional matching depends on the payment method.
- The payment-method-specific comparison uses the same DPAN for Google Pay or Apple Pay, payer email for PayPal, or card number and expiration date for credit cards. These are gateway matching conditions, not documentation of API idempotency keys or SDK retry guarantees.
- A duplicate request is rejected immediately without waiting for an in-flight initial request to receive a card-network response. If that initial transaction is later declined, the article says neither transaction is automatically retried.
- Users with Account Admin permissions can enable or disable the checking feature and change its timeframe in the Control Panel. The article separately recommends form-level safeguards, such as disabling a buy button after it is clicked, to reduce repeated submissions.

## Detail locators

- Repeated-checkout causes, gateway purpose, default enablement, and Control Panel configuration route: `# Duplicate Transaction Checking`, lines 16-22.
- Timeframe-qualified gateway-rejection rule and default 30-second window: `## Duplicate checking logic`, lines 27-31.
- General amount, order/subscription identifier, initial-status matching, and in-flight/automatic-retry warning: `### General conditions`, lines 34-46.
- Google Pay, Apple Pay, PayPal, and credit-card matching categories: `### Payment method-specific conditions`, lines 51-58.
- Sandbox/Production default and Account Admin configuration boundary: `## Configuring duplicate transaction checking`, lines 61-72.

## Evidence limitations

> [!warning] Gateway screening is not API idempotency evidence
> This collected article explains Braintree's gateway duplicate-screening logic and where Account Admin users configure it in the Control Panel. It does not document an API idempotency key, SDK retry contract, exactly-once processing, or the broader semantics of a Gateway Rejected transaction. Follow the linked gateway-rejections authority for that status and the applicable API or SDK authority for request-level behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree Control Panel Gateway Rejections]] - navigation-only authority linked by the article for the resulting status; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/duplicate-checking-2026-09-16|Braintree Duplicate Transaction Checking]] - complete collected article covering gateway duplicate matching, timeframe, immediate-rejection behavior, payment-method-specific conditions, and Control Panel configuration
