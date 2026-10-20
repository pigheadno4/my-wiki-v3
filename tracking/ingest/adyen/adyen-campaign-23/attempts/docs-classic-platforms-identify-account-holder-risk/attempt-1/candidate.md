---
title: "Adyen Classic Platforms: Identify account-holder risk with Score"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/identify-account-holder-risk"
raw_files:
  - "adyen/docs/classic-platforms/identify-account-holder-risk/2026-09-15.md"
tags: [adyen, classic-platforms, score, risk-signals, account-holders]
---

## Overview

This 2020-modified, 2026-09-15-captured **Classic Adyen for Platforms** overview describes Adyen Score for spotting unusual or potentially malicious account-holder behavior from verification (KYC) data and transactions. The page directs new implementations to the newer integration guide and says to contact an Adyen Account Manager to enable Score. It is a risk-investigation aid, not a fraud determination or automatic restriction. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- Adyen identifies **risk signals** and calculates an account-holder risk score from 0 to 100, with 100 highest. A score of 100 **does not confirm fraud or malicious behavior**; the platform must investigate and may mark a signal false positive. Signal weights can vary and the page says the platform can change weights or add its own signals. Its same-bank-account 20-to-100 scenario is an illustration, not a general formula or threshold.
- Adyen groups account holders sharing KYC characteristics into an **identity**. Signals raised for one account holder are applied to the whole identity, and all members receive the same risk score in the described model. This can change the score of an existing account holder when another linked holder is added; the page's example is illustrative.
- **By default, Adyen does not disable payouts or processing.** The platform is responsible for reviewing cases and taking manual action or implementing its own automated action. Listed possible actions include disabling payouts, suspending holders, flagging false positives and refunding payments. The overview itself does not perform or prove any such action.
- Adyen-defined KYC signals are described as evaluated in real time and transaction signals daily; platform-defined custom and high-risk-list signals are described as evaluated in real time. The page routes case review to Customer Area **Platform > Score** or a sub-merchant's **Score** tab, with separate child guides for action management and risk-signal notifications. These timing and UI descriptions are dated snapshot behavior, not proof of current feature enablement.

## Detail locators

- Pinned raw lines 15–25: Classic scope, Account Manager enablement, KYC/transaction signal inputs.
- Pinned raw lines 27–48: signals, 0–100 score, identity linking, default no payout/processing disablement, platform actions and Customer Area routes.
- Pinned raw lines 50–69: score interpretation, weights, non-confirmation of fraud and illustrative linked-identity score propagation.
- Pinned raw lines 71–83: Adyen and platform signal classes and evaluation cadence; lines 85–95: next-step child routes.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and payout context.
- [[source-adyen-docs-classic-platforms-identify-account-holder-risk-review-and-manage]] — case review and action procedures (navigation only).
- [[adyen-platforms]] — newer account-holder risk model, separate product path.

## Related raw API references

- [[raw/adyen/docs/classic-platforms/identify-account-holder-risk/configure-notifications-for-risk-signals/2026-09-15|Classic Score risk-signal notification guide]] — navigation only.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/identify-account-holder-risk/2026-09-15|Classic Platforms Score overview, captured 2026-09-15]]
