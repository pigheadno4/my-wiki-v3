---
title: "Braintree Control Panel Email Receipts"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/email-receipts"
raw_files:
  - "braintree/articles/control-panel/transactions/email-receipts-2026-09-16.md"
tags: [braintree, control-panel, email-receipts, transactions, refunds]
---

## Overview

This collected Braintree Control Panel article documents activation and configuration of gateway email receipts for transactions and refunds successfully submitted for settlement. It also distinguishes manual or merchant-built receipts from the gateway feature and explicitly routes subscription failed-payment alerts to separate notification documentation; the collected snapshot does not establish current availability.

## Key takeaways

- A Braintree gateway can be configured to send customers email receipts for each transaction or refund successfully submitted for settlement. Using the feature requires Control Panel enablement and an email address in the customer information for transactions created either in the Control Panel or through the API.
- Activation must first be requested from Support by the account's authorized signer. After Support confirms activation, the merchant enables and configures Email Receipts under the Control Panel's Processing settings.
- With **Send Receipt by Default?** enabled, the page says receipts are sent for every successful transaction; each transaction must specify an email address or use a Vault customer with one, otherwise submission triggers a validation error.
- Gateway receipt customization is limited: the sender address is fixed, while Reply To, BCC and up to 1,000 characters of plain-text email text are configurable. HTML and broader content or delivery customization require merchant-built receipts.
- PayPal already sends its own PayPal-transaction receipts by default, so PayPal customers receive both a Braintree receipt and a PayPal receipt when Braintree receipts are enabled.

> [!warning] Notification and delivery boundaries
> This page does not document subscription failed-charge notification emails; it directs that use case to a separate recurring-billing article. For merchant-built receipts, consult the raw section's card-data display warning rather than treating this gateway-configuration page as a general email-notification or receipt-compliance specification.

## Detail locators

- Separate subscription failed-payment notification scope: `# Email Receipts`, lines 17-18.
- Gateway receipt trigger, email prerequisite and customization boundary: `# Email Receipts`, lines 22-30.
- Duplicate PayPal and Braintree receipt behavior: `## PayPal email receipts`, lines 33-35.
- Support activation and Control Panel enablement path: `## Enabling email receipts`, lines 38-50.
- Default sending, missing-email validation, sender, Reply To, BCC and plain-text limits: `## Enabling email receipts > ### Configuration options`, lines 53-74.
- Authorized-signer identity and change route: `## Enabling email receipts > #### Authorized signer`, lines 79-87.
- Manual sending, merchant-built receipt routes and card-data display warning: `## Sending an email receipt manually` through `## Sending your own email receipts`, lines 99-114.

## Related

- Company: [[braintree]]
- Control Panel concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/email-receipts-2026-09-16|Braintree Control Panel Email Receipts]] - complete collected article covering transaction/refund receipt triggers, activation, configuration, delivery and customization boundaries
