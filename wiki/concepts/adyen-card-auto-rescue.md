---
title: "Adyen Card Auto Rescue"
type: concept
category: technology
tags: [adyen, auto-rescue, cards, recurring-payments, retries]
---

## Overview

Adyen Auto Rescue can retry eligible refused shopper-not-present card payments after account-level or transaction-level enablement by Adyen. A scheduled retry is not a successful payment: the merchant must handle per-attempt `AUTHORISATION` webhooks and a final `AUTORESCUE` outcome. Each retry is a distinct transaction. For manual-capture merchants, a rescued authorization still requires capture. The card guide also describes cancellation of an active rescue when payment details change or a subscription ends; success is reported by the later `CANCEL_AUTORESCUE` webhook.

## Sources

- [[source-adyen-docs-online-payments-auto-rescue-cards]] — Adyen card-specific Auto Rescue guide for enablement, retries and outcome webhooks, cancellation, tests, and reporting (webpage snapshot, 2026-09-15).
