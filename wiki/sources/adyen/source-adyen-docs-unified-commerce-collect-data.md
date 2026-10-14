---
title: "Adyen Unified Commerce customer identifier collection"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/collect-data"
raw_files:
  - "adyen/docs/unified-commerce/collect-data/2026-09-15.md"
tags: [adyen, unified-commerce, customer-data, identifiers, webhooks, terminal-api]
---

## Overview

This dated Adyen guide describes merchant-side collection of customer identifiers from payment details for the merchant's **own data warehouse and analysis** across sales channels. It recommends configured Standard webhooks for a common cross-channel format and identifies Terminal API payment responses as a POS alternative with a different format. It does not create a customer profile automatically, authorize use of raw PAN, or establish a particular merchant's privacy basis. See [[adyen]], [[adyen-unified-commerce]], [[adyen-terminal-api]] and [[adyen-tokenization]].

## Key takeaways

- Consider data privacy before collecting identifiers. The guide says Standard webhooks can deliver payment details across sales channels when set up; merchants select desired `additionalData` settings in Customer Area. The sample POS `AUTHORISATION` webhook is an illustration (`live=false`), not evidence of a current merchant's enabled fields or successful cross-channel identity match.
- **Card alias** represents a card PAN for recognition of a returning card, but **cannot be used to make payments**. **PAR** identifies the payment account behind a card or NFC wallet and can help where wallet transactions do not expose the PAN. The page's 2021-modified text says PAR is returned for Visa and Mastercard when available, for ecommerce and Terminal API payment/card-acquisition contexts; this is dated availability guidance, not a universal guarantee. Neither identifier is raw PAN or a stored payment method token.
- **Shopper reference** is merchant-defined and at least three characters; this page says it should not contain PII such as name or email. A collected **shopper email** may link multiple aliases, shopper references and stored-payment identifiers in the merchant's analysis. The guide says shopper reference **and** stored payment method token are needed for recurring contract payments; an alias or PAR alone does not grant payment authority. Email is collected/stored in the recurring-contract context described here, not automatically available on every payment.
- Funding source and issuer country are optional analytical fields; the page calls issuer country a useful indicator of residence, not proof of shopper residence. Token variant is another optional field exposed through configuration. Field availability depends on the selected webhook settings and underlying transaction data.
- For Standard webhook `additionalData`, choose **Include Alias Info**, **Include Funding Source**, **Include Issuer Country**, **Include Shopper Details**, **Add Payment Account Reference** and/or **Include tokenTxVariant** as relevant. PAR and token variant additionally require **Developers > Additional data** enablement; enabling those settings also makes the identifiers appear in API responses. This page states configuration steps, not a role or permission grant beyond normal Customer Area access.
- A Terminal API POS merchant can collect the same identifier categories from payment responses, but in a **different format** from Standard webhooks. The page points to a separate POS identifier guide for response details. Do not assume the example webhook `additionalData` fields occur automatically in every Terminal API response.

## Detail locators

- `## Requirements`, `## Overview of identifiers`: privacy prerequisite, alias/PAR/shopper-reference/email identities, recurring-token distinction and optional funding/issuer attributes.
- `## Using data from webhooks`: Standard webhook setup, per-field Customer Area additional settings and extra PAR/token-variant enablement.
- `### Example standard webhook`: illustrated POS event and `additionalData` shape, with `live=false`; this is an example rather than a current configuration.
- `## Using data from Terminal API responses`: POS payment-response alternative and its distinct format.

## Related

- [[adyen-unified-commerce]] — primary merchant cross-channel data route.
- [[adyen-terminal-api]] — POS payment responses and card acquisition.
- [[adyen-tokenization]] — stored payment method tokens for authorized recurring use.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/collect-data/2026-09-15|Adyen Collect data, captured 2026-09-15]]
