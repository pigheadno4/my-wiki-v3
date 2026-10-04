---
title: "Braintree Chase Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/chase/transactions/descriptors"
raw_files:
  - "braintree/articles/chase/transactions/descriptors-2026-09-16.md"
tags: [braintree, chase, transactions, descriptors, bank-statements]
---

## Overview

This collected Braintree-owned Chase processor article explains the statement descriptor associated with a purchase through a merchant's mobile app or website. It documents Chase's automatic configuration from information supplied in the Transaction Division Information section of the merchant application, then routes the exact merchant-name, city and state constraints to the pinned raw. The customer's bank ultimately controls how the descriptor appears.

## Key takeaways

- The Chase path describes three descriptor fields: merchant name (DBA), merchant city and merchant state. This is processor-specific Braintree documentation, not independent current Chase authority or a basis for transferring the same rules to another processor or region.
- A refund descriptor defaults to the descriptor passed with the original transaction. That statement describes the displayed descriptor default; it does not establish refund success, settlement or funding.
- The merchant-name field has capitalization, length and character rules. The article also documents a more-specific name format in which a shortened DBA and the rest of the text are separated by an asterisk at one of three permitted positions.
- The merchant-city field can instead carry a customer-service phone number, URL or email address, subject to the field's length and format rules. The merchant-state field is not presented as interchangeable: it should list the state where the business is located.
- PayPal-transaction descriptors follow a separate PayPal-console update route rather than the Chase descriptor path described by this article.

> [!warning] Scope and evidence boundaries
> This is a 2026-09-16 snapshot of a Braintree article for the Chase processor path. It does not prove current Chase requirements, account eligibility, regional applicability or successful transaction/refund processing. A customer's bank can render the business descriptor differently from the article's example.

## Detail locators

- Separate PayPal-console route: note below `# Descriptors`, lines 17-18.
- Descriptor purpose, bank-controlled rendering and example statement text: `# Descriptors`, lines 22-24.
- Chase automatic configuration and the three descriptor fields: `# Descriptors`, lines 26-31.
- Refund descriptor default: note below the field list, lines 34-35.
- Merchant-name requirements and Mastercard question-mark rendering: `## Descriptor field requirements` → `### Merchant name (DBA) field`, lines 43-53.
- More-specific merchant-name formatting and examples: `#### Customizing the merchant name field`, lines 58-73.
- Merchant-city alternatives, base limits and phone/URL/email rules: `### Merchant city field`, lines 76-106.
- Merchant-state requirement: `### Merchant state field`, lines 109-111.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General Braintree descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/chase/transactions/descriptors-2026-09-16|Braintree Chase Transaction Descriptors]] - complete collected Braintree article for Chase-specific descriptor configuration, field rules and statement-display qualifications
