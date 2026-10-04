---
title: "Braintree Refund Authorizations"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/refund-authorizations"
raw_files:
  - "braintree/articles/guides/refund-authorizations-2026-09-16.md"
tags: [braintree, refunds, authorizations, processor-responses]
---

## Overview

This collected Braintree article explains the move toward authorizing card refunds before sending them to cardholders, so an issuer can respond and an approved authorization can appear on a cardholder statement in real time. The page documents Braintree refund-response behavior, decline handling, SDK-version-dependent response forms, and sandbox simulation routes.

The captured scope is all merchants in the US and selected merchants in Australia, and the page warns that authorization and capture can incur merchant fees in some markets. These are source-qualified snapshot statements, not proof of current merchant eligibility, pricing, production rollout, issuer posting, or successful refund execution.

## Key takeaways

- The article lists Visa, Discover, Mastercard, and Amex, and identifies credit cards, Apple Pay, and Google Pay as affected payment methods. The lists and any later changes remain at the raw locators below.
- For an approved refund authorization, the issuer indicates that it will accept and deposit the refund. For a decline, the issuer indicates that the account cannot accept it, preventing that payment method from being refunded. The page separately warns that certain declined authorizations may be force-captured depending on the network response code, so a decline cannot be treated as an unconditional no-refund outcome.
- Under the article's "Current refund workflow" heading, Braintree says the refund API response for the named payment methods indicates whether the API request succeeded, not the refund's overall outcome; an issuer can still reject the refund afterward. Under "Future refund workflow," the page says real-time processor responses will apply once Braintree releases the framework by card network and region, and integrations will need to recognize refund processor responses. The snapshot therefore does not establish that this future production workflow is currently live for every network, region, or merchant.
- The decline-handling guidance says to attempt the refund of the original sale through Braintree's refund API or Control Panel first; after an issuer decline, the merchant may use an alternate method. The page's alternate-method examples and separate refund-policy qualification remain in the raw source.
- The technical section distinguishes listed newer SDK thresholds, which expose a processor response code on a processor-declined refund, from older SDK versions, which receive one of two validation errors instead. It separately states that GraphQL users receive processor response codes for all refund declines. Exact SDK thresholds, example codes, validation errors, and sandbox amounts are retained in the raw locators rather than generalized across integrations.

## Material qualifications

- Availability is explicitly limited to all US merchants and selected Australian merchants in this captured page.
- Authorization and capture may carry merchant fees in some markets.
- A successful API request is not the same as a successful overall refund, while an approved authorization is an issuer indication rather than evidence that funds were actually posted.
- Some declined refund authorizations may be force-captured depending on the network response code.
- The production processor-response behavior is described as a future workflow contingent on release by card network and region; the page only says the changes were available in Braintree sandbox at capture time.

## Detail locators

- Availability and fee qualifications: `# Refund Authorizations > **NOTE**`, lines 17-20.
- Industry purpose and real-time statement visibility: introductory paragraph, line 24.
- Affected card networks and payment methods: `## Card networks affected` and `## Payment methods affected`, lines 27-42.
- Approved and declined authorization meanings, common decline reasons, and the force-capture exception: `## Statuses of refund authorizations`, lines 44-66.
- Industry background and stated benefits: `## Background` through `## Benefits`, lines 70-102.
- Original-sale refund attempt, alternate-method guidance, examples, and the refund-policy qualification: `## How to handle refund declines`, lines 105-121.
- API-request success versus overall outcome and the release-qualified future processor-response workflow: `## Integration changes`, lines 124-135.
- SDK thresholds, processor-code behavior, GraphQL qualification, example decline codes, and older-SDK validation errors: `## API Updates and Sandbox Testing` through `### Previous SDK versions`, lines 137-176.
- Sandbox availability and the documented sale, settlement, refund, and amount-based decline simulation procedure: `## Sandbox testing`, lines 179-190.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Detailed Node refund API route: [[source-braintree-transaction-refund-node]]
- General processor authorization-response route: [[source-braintree-authorization-responses]]

## Raw Sources

- [[raw/braintree/articles/guides/refund-authorizations-2026-09-16|Braintree Refund Authorizations article]] - fully read collected page covering refund-authorization purpose, scope, outcomes, integration transition, SDK response differences, and sandbox testing
