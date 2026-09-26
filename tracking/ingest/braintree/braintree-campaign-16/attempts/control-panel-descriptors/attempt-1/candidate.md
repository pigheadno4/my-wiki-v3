---
title: "Braintree Control Panel Descriptors"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/descriptors"
raw_files:
  - "braintree/articles/control-panel/transactions/descriptors-2026-09-16.md"
tags: [braintree, control-panel, descriptors, transactions, bank-statements]
---

## Overview

This collected Braintree Control Panel article explains the descriptors customers may see on bank statements, distinguishes soft, hard and dynamic descriptors, and routes merchants to region- and payment-path-specific configuration. It separates account-level Control Panel editing from per-transaction dynamic descriptors passed through the API; the collected snapshot does not establish current availability.

## Key takeaways

- A descriptor identifies a purchase on a customer's bank statement, but the customer's bank ultimately determines exactly how the business descriptor appears.
- A soft descriptor appears after authorization while the charge remains pending. A hard descriptor appears after settlement and, once the customer's bank finalizes the transaction status, remains as the charge description.
- A dynamic descriptor is custom data configured and passed with each transaction through the API. Processor support varies: the article says some processors support only soft dynamic descriptors, while others support both hard and soft dynamic descriptors.
- For merchants located in the United States, Europe or Australia, the article routes account-descriptor viewing and editing to the Business page in the Control Panel. It directs merchants in other regions to contact Braintree for descriptor updates.
- Descriptor requirements and availability are bank-specific. PayPal-transaction descriptors are updated separately in the PayPal console rather than through the Braintree Control Panel route documented here.

> [!warning] Configuration and evidence boundaries
> This Control Panel article does not specify the API request shape, processor-by-processor support, or bank-specific descriptor rules. Use the related API reference only as navigation for integration detail, and treat this 2026-09-16 collected page as evidence of what the article documents rather than proof of current feature or regional support.

## Detail locators

- Descriptor purpose and bank-controlled presentation: `# Descriptors`, lines 16-18.
- Soft, hard and dynamic descriptor meanings and processor qualification: `# Descriptors`, lines 20-25.
- United States, Europe and Australia Control Panel route: `# Descriptors`, line 27.
- Other-region assistance route: `# Descriptors`, line 29.
- Bank-specific requirements/availability and separate PayPal-console route: `# Descriptors`, lines 31-33.

## Related

- Company: [[braintree]]
- Control Panel concept: [[braintree-control-panel]]
- API/SDK concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/descriptors-2026-09-16|Braintree Control Panel Descriptors]] - complete collected article covering descriptor meanings, statement visibility and configuration boundaries

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js Transaction Sale]] - navigation-only route for dynamic-descriptor API/SDK details; not factual evidence for this source entry
