---
title: "Oracle Opera | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/oracle-opera"
raw_files:
  - "adyen/docs/plugins/oracle-opera/2026-09-15.md"
tags: [adyen, oracle-opera, hospitality, opi, terminals, tokenization]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot describes the Oracle Opera hospitality/property-management integration using Oracle Payment Interface (OPI) 6.2 to connect Opera workstations to Adyen terminals. It also describes merchant-account-enabled OPI tokens for ecommerce payments. Its transaction-type list and example `/payments` payload are capabilities and instructions, not evidence that an individual guest payment, token migration or settlement succeeded. [[adyen-oracle-opera]]

## Key takeaways

- Adyen says its plugin supports Opera workstations compatible with OPI across on-premise, hosted and cloud setups; it does not provide an exact Opera release matrix. After creating a test account, the merchant must contact Support to enable OPI in Customer Area. OPI sends workstation transaction messages directly to the Adyen terminal; this route should not be merged with a separate Oracle retail/Xstore integration.
- Listed hospitality transaction types include preauthorization at check-in, optional daily top-up, authorization release, sales completion at checkout, direct Sale/Purchase, refund, same-settlement-day Void, connection-loss/timeout Reversal, and Get Token / Get Token Bulk. A preauthorized amount is a temporary hold, not a charge; Sales Completion or Sale/Purchase is the charging step described here. Void has the stated settlement-day limit. The page's labels do not verify the final state of any actual operation.
- Terminal-entered data can be exchanged for an OPI token kept in the Oracle database for later top-ups or final settlement. Get Token Bulk is also described for token migration, third-party reservations and manually entered phone reservations; it is not evidence that a bulk migration has been performed or is safe without its detailed controls.
- For ecommerce OPI tokens, Support must enable settings for the merchant account first. The guide instructs a Checkout `/payments` request with `additionalData.opi.includeTransToken=true`, `shopperInteraction=Ecommerce`, `shopperReference=not_provided`, `recurringProcessingModel=CardOnFile` and `storePaymentMethod=true`. The flag requests an OPI token; `opi.transToken` is returned in the response and is distinct from a recurring detail reference. The `not_provided` value is this guide's stated OPI-flow input, not a universal stored-credential rule; the sample `Authorised` response is not proof of any actual payment or permission.

## Detail locators

- **OPI architecture, workstation/platform scope and test enablement:** raw lines 23–44.
- **Hospitality transaction types, hold/charge distinction and void limit:** raw lines 48–74.
- **Ecommerce OPI-token enablement, request settings and illustrative response:** raw lines 76–143.

## Related

- [[adyen]]
- [[adyen-oracle-opera]]
- [[adyen-terminal-api]] — separate terminal-message architecture context; OPI is the named Opera interface here
- [[adyen-tokenization]] — separate online stored-credential context

## Raw Sources

- [[raw/adyen/docs/plugins/oracle-opera/2026-09-15|Adyen Oracle Opera integration — collected 2026-09-15]]
