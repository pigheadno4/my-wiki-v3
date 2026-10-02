---
title: "Braintree Credit Card Configuration"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/configuration"
raw_files:
  - "braintree/docs/guides/credit-cards/configuration-2026-09-16.md"
tags: [braintree, credit-cards, configuration, avs, cvv]
---

## Overview

This collected Braintree configuration page is a short retrieval route for the initial configuration posture of credit and non-PIN debit card acceptance. It states that most such card payments need no additional configuration, identifies a qualified American Express exception, and points to separate card-verification and AVS/CVV protection routes.

## Key takeaways

- The page says no additional configuration is needed to begin accepting most credit and non-PIN debit card payments.
- Some merchants may need to contact Braintree before accepting American Express transactions, although the page says Amex is typically enabled by default. The snapshot does not establish an individual merchant's card-brand enablement or eligibility.
- Card verification and AVS/CVV rules are presented as optional fraud-protection routes. Their exact setup, decision behavior, and qualifications belong to the dedicated guides rather than this brief configuration page.

## Evidence limitations

> [!warning] Snapshot, not current enablement
> This immutable 2026-09-16 page snapshot does not prove current card-brand support, merchant-account configuration, American Express eligibility, successful authorization, or payment acceptance.

## Detail locators

- Default configuration posture, American Express qualification, and payment-method support contact route: `# Configuration`, line 16.
- Card verification and AVS/CVV navigation: `## AVS and CVV`, lines 19-21.
- Client-side continuation: `Next Page: Client-side`, line 25; navigation only.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Provider orientation: [[braintree-payment-platform]]
- Dedicated AVS/CVV behavior: [[source-braintree-fraud-tools-basic-avs-cvv-rules]]

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/configuration-2026-09-16|Braintree Credit Cards Configuration guide]] - complete collected page covering the default configuration posture, qualified Amex exception, and card-verification and AVS/CVV navigation
