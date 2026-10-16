---
title: "Adyen Dynamics 365 Commerce payment connector"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/microsoft-dynamics"
raw_files:
  - "adyen/docs/plugins/microsoft-dynamics/2026-09-15.md"
tags: [adyen, microsoft-dynamics, dynamics-365-commerce, pos, ecommerce, connector]
---

## Overview

Adyen's 2023-modified Dynamics 365 Commerce guide describes the **Dynamics 365 Payment Connector for Adyen** across retail POS, e-Commerce and Call Center channels. Modern POS uses local Terminal API communications and can continue processing while offline; Cloud POS uses cloud Terminal API communications, runs in a browser and cannot work offline; e-Commerce and Call Center use Checkout API. This is a channel-specific setup guide, not an ERP-wide feature claim or evidence of a live transaction or funds movement.

## Key takeaways

- Begin with an Adyen test account; application for a live account is a separate process. For multiple sales channels, the guide requires a **separate merchant account per channel** and emphasizes **separate API credentials per channel**. Do not configure the default company API credential. The channel API key must be securely stored; the guide says it cannot be restored if lost. These instructions do not identify the legal seller, merchant of record, settlement account or actual merchant eligibility.
- MPOS and CPOS credentials use Web service/API key; the merchant enables Merchant Recurring Role while Adyen Support enables additional POS, terminal-management, encryption and firmware roles and configures the back office. The POS merchant-account setup selects **Immediate** POS Capture Delay. e-Commerce and Call Center have their own Checkout/payment roles; the e-Commerce list additionally includes `API Payment RefundWithData`. For **V002** of the connector, the e-Commerce setup also has an Origin Key step. Read each channel tab before assigning roles; creating a key alone does not establish role or merchant-account access.
- MPOS/CPOS need Adyen-software-injected terminals, store IDs, ordered test terminals and boarding. Dynamics POS hardware profiles use terminal IP, POIID and encryption-key identifiers/passphrase/version from Customer Area. MPOS local communication can work offline and directly reach peripherals; CPOS cloud communication cannot work offline and reaches peripherals through a hardware station. These are documented channel capabilities, not proof of a particular terminal's availability or completed payment.
- Dynamics 365 connector setup routes to Microsoft documentation. For **e-Commerce/Call Center**, Optional Domain may be blank in test but requires the live Adyen merchant prefix at go-live to avoid `PaymentException`; for **CPOS**, the live Optional Domain is `https://terminal-api-live.adyen.com/sync`, with a reminder to check current cloud endpoint versions. The document's specific instructions are a dated snapshot, not a current version-compatibility matrix.
- Tokenization is supported only after Adyen-side configuration requested through Support. Before accepting payments, test methods in each channel and inspect test payments; live setup separately requires live merchant accounts as needed, stores/live terminals for POS, live account configuration, and Dynamics Headquarters **Gateway environment = Live** plus the channel's Optional Domain. Setup and tests do not establish payment authorization, capture, refund, settlement, payout or bank receipt.

## Detail locators

- Opening before `## Requirements` — connector identity, supported channels and local/cloud/Checkout API split.
- `## Requirements` — test-account start, separate merchant account per channel, live-account application boundary.
- `## Step 1: Configure your Adyen account` > MPOS, CPOS, eCommerce and Call Center tabs — separate credentials, default-credential warning, secure API keys, distinct roles/Support tasks, Immediate POS Capture Delay and V002 Origin Key.
- `## Step 2 (MPOS or CPOS)` — Adyen-software terminals, stores, ordering and boarding.
- `## Step 3: Set up Dynamics 365` — Microsoft documentation route, test/live Optional Domain differences and POS hardware-profile fields.
- `## Tokenization`, `## Test and go live` — Support-enabled tokenization, per-channel testing, live merchant/store/terminal setup and Dynamics Headquarters environment.

## Related

- Company: [[adyen]]
- Dynamics 365 Commerce connector concept: [[adyen-microsoft-dynamics]]
- Terminal API context: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/plugins/microsoft-dynamics/2026-09-15|2026-09-15 Dynamics 365 Commerce connector guide]]
