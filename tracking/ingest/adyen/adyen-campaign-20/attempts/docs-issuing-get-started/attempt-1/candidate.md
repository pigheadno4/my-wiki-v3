---
title: "Adyen Issuing: Get started"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/get-started"
raw_files:
  - "adyen/docs/issuing/get-started/2026-09-15.md"
tags: [adyen, issuing, cards, integration]
---

## Overview

Adyen's Issuing get-started page is a seven-step, contact-led route from exploring a card program through designing and testing an Issuing integration to requesting and configuring a live account. It is a setup guide for [[adyen-issuing]], not evidence that an account has been opened or that cards or payments work in a live environment. This source is a 2026-09-15 capture of a page marked last modified 2022-10-26.

## Key takeaways

- Start by discussing business model, physical or virtual cards, estimated card volume, and payments with Adyen. Adyen then helps assess fit; an Adyen contact works with the platform on implementation design.
- Design decisions include who the account holders are and how balance accounts and payment instruments are grouped. That structure shapes onboarding, verification, and funds flow. Choose card type, relayed authorisation and/or transaction rules for approving or declining payments, and how to fund the liable balance account. The page names a wire as one funding option and directs existing Adyen integrators to their contact for other options.
- After design, Adyen sends test credentials by email. In the test Customer Area, create credentials for Legal Entity Management (legal entities for verification), Configuration and Transfers (account holders, balance accounts, payouts, transfers), and Checkout (processing users' payments). Customer Area users can be created for organization members. These API descriptions identify purposes, not completed operations.
- Build and test the Issuing integration, then contact Adyen about taking the account live. Test setup and configuration are not replicated to the live Issuing account; repeat setup in live and follow the go-live checklist.

## Detail locators

- `Step 1: Get in touch with us` (raw lines 19–27): intake and fit discussion.
- `Step 2: Design your implementation` (raw lines 29–47): account structure, card type, payment authorisation, and funding choices.
- `Step 3: Get your test accounts and generate API credentials` (raw lines 49–66): test Customer Area and API purposes.
- `Step 4` through `Step 7` (raw lines 68–86): users, build, contact for live account, and separate live configuration.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing topic route.

## Raw Sources

- [[raw/adyen/docs/issuing/get-started/2026-09-15|Adyen Issuing get started, captured 2026-09-15]]
