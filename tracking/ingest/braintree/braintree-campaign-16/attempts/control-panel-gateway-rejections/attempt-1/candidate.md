---
title: "Braintree Control Panel Gateway Rejections"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/gateway-rejections"
raw_files:
  - "braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16.md"
tags: [braintree, control-panel, gateway-rejections, transactions, verifications, authorization-voids]
---

## Overview

This Braintree Control Panel article explains gateway rejections for transaction and verification requests that fail settings or rules in a merchant's Braintree gateway. It distinguishes them from declines attributed here to the customer's bank and documents both pre-processor rejection and rejection after authorization.

## Key takeaways

- A gateway rejection is caused by gateway settings, while the article describes a decline as being blocked by the customer's bank. The separate Declines article is linked only as navigation below and was not used as factual evidence for this source.
- Depending on the trigger, Braintree may reject a transaction or verification before sending information to the processor or after authorization completes. When authorization precedes rejection, the gateway automatically voids the transaction.
- A bank may not acknowledge the automatic void promptly, or at all. The article says a customer seeking removal of the authorization can contact their bank to speed the process.
- Braintree changes a rejected transaction or verification request to `Gateway Rejected` and provides a rejection reason. The complete reason list and linked reason-specific guidance remain at the raw locator below.
- `Application Incomplete` can apply when a provisionally processing merchant reaches its account limit before full approval; subsequent transaction or verification attempts are then rejected until the merchant has approval for a full merchant account.

> [!warning] Authorization removal is not necessarily immediate
> Automatic voiding after a post-authorization gateway rejection does not guarantee that the customer's bank will acknowledge or remove the authorization promptly.

## Detail locators

- Gateway rejection versus customer-bank decline: `# Gateway Rejections > **NOTE**`, lines 17-18.
- Pre-processor versus post-authorization rejection and automatic void: `# Gateway Rejections`, line 22.
- Bank acknowledgment limitation and customer route: `# Gateway Rejections > **NOTE**`, lines 25-26.
- `Gateway Rejected` status and complete reason list: `# Gateway Rejections`, lines 30-41.
- Provisional-account processing limit and `Application Incomplete` behavior: `## A note on Application Incomplete`, lines 44-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/transactions/declines-2026-09-16|Braintree transaction declines article]] - navigation-only destination linked by this article; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree Control Panel gateway-rejections article]] - complete collected page covering gateway-setting rejection, the customer-bank decline distinction, automatic voiding after authorization, rejection status and reasons, and the provisional-account limit
