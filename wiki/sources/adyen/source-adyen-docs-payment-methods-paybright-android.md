---
title: "PayBright for Android | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/android"
raw_files:
  - "adyen/docs/payment-methods/paybright/android/2026-09-15.md"
tags: [adyen, paybright, affirm, android, navigation]
---

## Overview

This 2026-09-15 Adyen Docs page is an Android integration chooser for PayBright. It links Android **Drop-in** and **Redirect Component** child routes plus base Android Sessions integration guides. Its opening says PayBright was acquired by Affirm and **Adyen will not accept new PayBright integrations**. The chooser does not override that restriction or establish a merchant's current availability, an implemented flow or a payment outcome. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- The Drop-in child is described as the all-in-one UI route; the Components child is described as a Redirect Component. Read the selected child for flow/version prerequisites, server requests, return handling and modification behavior.
- The closing base-guide links point to Android Drop-in and Components **Sessions** flows. They are navigation, not proof that every child guide uses Sessions; the linked PayBright Android Drop-in guide itself states an **Advanced** prerequisite. Select the actual child guide's flow requirement before implementation.

## Detail locators

- Acquisition/no-new-integration notice: pinned raw line 19.
- Drop-in and Redirect Component child links: `## How do you want to integrate?`, lines 21–33.
- Base Android Sessions links: line 35. Compare the Advanced requirement in [[source-adyen-docs-payment-methods-paybright-android-drop-in]] rather than treating this navigation as a universal flow rule.

## Related

- [[adyen-online-payments]] — provider online-payments context.
- [[source-adyen-docs-payment-methods-paybright-android-drop-in]] — Android Drop-in procedure and its Advanced-flow prerequisite.

## Related raw API references

- The Components child at `/payment-methods/paybright/android-component` is linked by this chooser; its implementation details are outside this pinned page.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/android/2026-09-15|2026-09-15 PayBright Android integration chooser]]
