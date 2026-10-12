---
title: "Adyen Test a Chargeback Scenario"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/disputes-api/test-applicable-dispute-reasons"
raw_files:
  - "adyen/docs/risk-management/disputes-api/test-applicable-dispute-reasons/2026-09-15.md"
tags: [adyen, disputes, chargebacks, testing, webhooks, disputes-api]
---

## Overview

This [[adyen]] guide explains how to simulate selected chargeback scenarios in the test environment, observe their webhooks, and practice accepting or defending the simulated dispute through the Disputes API or test Customer Area. It is a test fixture route under [[adyen-payment-testing]], with dispute-management context at [[adyen-risk-management]]; it does not establish live chargeback timing, merchant eligibility, or a real defense outcome.

## Key takeaways

- The test sequence is to choose a scenario, send a test payment with a scenario-triggering `paymentMethod.holderName`, capture that payment, monitor the resulting webhook, then use test dispute data to accept or defend. A chargeback with a reason code, without a code, a reversal, and a second chargeback are listed. Not all dispute types can be simulated; ACH Direct Debit is routed to separate instructions.
- The raw gives `holderName` patterns for a chargeback with the payment's value and currency, or with a specified quantity in minor units and currency. For custom amounts, partial chargebacks have a maximum 50% difference from the test payment; greater-than-payment chargebacks have a maximum 20% difference. Exact trigger strings and example amounts are in the raw, not general production cardholder names.
- The payment response `pspReference` is used to make the test capture request. The capture response has a distinct capture `pspReference`; a later dispute webhook has its own dispute `pspReference`. Keep these object identities separate when correlating the simulated payment and dispute.
- After capture, the guide describes a `CAPTURE` webhook and a test payment moving through SentforSettle and Settled to Chargeback; it says that process can take up to 24 hours. A `NOTIFICATION_OF_CHARGEBACK` webhook is the illustrated chargeback signal, and its sample payload is an example rather than a universal promise for every scenario.
- Disputes API testing requires an API key credential with the **API dispute management** role; Customer Area dispute management needs **Merchant dispute management** or **Risk admin**. The guide also calls for a configured Standard webhook with dispute events, and notes a RevenueProtect classic-risk check that may need temporary adjustment for nonalphabetic `holderName` triggers.

## Detail locators

- **Scope, separate ACH route, prerequisites, and simulation limits:** raw lines 15–42.
- **Test sequence, trigger patterns, custom amount constraints, and examples:** raw lines 43–113.
- **Test `/payments` example and original payment reference:** raw lines 115–146.
- **Capture API and distinct capture reference:** raw lines 148–170.
- **Webhook timing, illustrative dispute payload, and accept/defend routes:** raw lines 172–229.

## Related

- [[adyen]]
- [[adyen-payment-testing]]
- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-disputes-api-dispute-notifications]]
- [[source-adyen-docs-risk-management-disputes-api-disputes-api-reference]]

## Raw Sources

- [[raw/adyen/docs/risk-management/disputes-api/test-applicable-dispute-reasons/2026-09-15|Adyen Test a chargeback scenario — collected 2026-09-15]]
