---
title: "Braintree 3D Secure Overview"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/overview"
raw_files:
  - "braintree/docs/guides/3d-secure/overview-2026-09-16.md"
tags: [braintree, 3d-secure, 3ds2, sca, card-authentication]
---

## Overview

This 2026-09-16 snapshot of Braintree's unversioned developer overview introduces 3D Secure (3DS) and Strong Customer Authentication (SCA), describes 3DS2's added data-sharing purpose, and outlines the client-side authentication handoff before later Braintree operations. It is authentication guidance, not evidence that a payment was authorized, processor-approved, submitted for settlement or settled.

## Key takeaways

- The page defines 3DS as an online-transaction security protocol that links issuer, acquirer and interoperability domains to share data and add a verification step during checkout. It says further customer information can support identity verification and fraud-risk assessment.
- The page describes 3DS2 as adding data-transfer capabilities such as device information to improve issuer risk assessment and reduce unnecessary verification steps. Those statements describe the version's intended design and possible checkout effect, not a guaranteed issuer decision, frictionless result or conversion outcome.
- For SCA, the page names knowledge, possession and inherence as the three factor categories and says issuers vary in the factors and methods they support. Its snapshot-specific applicability statement says SCA is required when both acquirer and issuer countries are PSD2-regulated, such as countries in the EEA; this collected page is not current legal or merchant-eligibility advice.
- The high-level flow is to generate a client token, render checkout to collect payment information, verify the card amount and let the issuer or applicable local legislation determine whether the customer is prompted to authenticate. After successful authentication, or when none is required, the page routes the returned nonce or `authentication_id` into a later transaction, customer or payment-method operation. That handoff does not itself establish authorization, gateway acceptance or settlement.
- This overview broadly says chargeback liability shifts on transactions verified through 3DS. The separately collected Braintree support article provides the material qualification: liability shifts only in certain cases, not every 3DS transaction receives one, and a shift does not guarantee automatic chargeback representation. Treat the overview as an introduction, not a liability guarantee.

> [!warning] Authentication is not payment completion
> A successful or unnecessary 3DS authentication only supplies an input for a later Braintree operation. This page does not establish that the payment was authorized, accepted by fraud rules, submitted for settlement or settled. Its broad liability wording is also qualified by [[source-braintree-fraud-tools-3d-secure]].

## Detail locators

- Security and SCA purpose: `# Overview`, line 16.
- Protocol definition, three-domain data sharing, 3DS2 purpose and supported card-brand services: `## What's 3D Secure?`, lines 21-27.
- SCA factor categories and issuer variation: `## What is SCA?`, lines 32-39.
- Page-scoped PSD2 geography condition: `## When is SCA required?`, line 44.
- Client-token, checkout, amount-verification and possible authentication sequence: `## Payment flow`, lines 49-55.
- Returned nonce or `authentication_id` handoff to later operations: `## Payment flow`, lines 57-60.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]
- Qualifying support article: [[source-braintree-fraud-tools-3d-secure]]

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/overview-2026-09-16|Braintree 3D Secure developer overview]] - complete collected overview covering 3DS and SCA purpose, 3DS2 context and the high-level authentication handoff
