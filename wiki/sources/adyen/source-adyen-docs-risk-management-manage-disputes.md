---
title: "Adyen Docs: Manage disputes"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/manage-disputes"
raw_files:
  - "adyen/docs/risk-management/manage-disputes/2026-09-15.md"
tags: [adyen, disputes, chargebacks, risk-management]
---

## Overview

This Adyen webpage snapshot describes how an eligible merchant can view, accept, or defend disputes in Customer Area. It also points to the [[source-adyen-docs-risk-management-disputes-api|Disputes API]] for automated handling. It is a documentation snapshot, not proof of current account access, scheme rules, or a particular dispute outcome. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- Customer Area access requires a listed dispute-management role; handling pre-arbitration requires Risk Admin or Pre-arbitration dispute management. Standard webhook subscription and dispute-event enablement are needed if following disputes by webhook. The page assumes an online-payments integration. See raw **Requirements**.
- For a defensible chargeback, Customer Area offers acceptance or defense-material upload. After acceptance **and expiry of the defense period**, the final status is *Lost*, the dispute cycle ends, and *DisputeDefensePeriodEnded* is booked. See raw **View disputes** and **Accept disputes**.
- Defense documents can be uploaded at Request for Information or Chargeback stage, within the applicable timeframe and according to the reason-code and scheme requirements. Adyen says each booked chargeback incurs a chargeback fee and advises defense only with sufficient compelling evidence. PDF, JPG, or TIFF files must exclude sensitive data; Adyen says it refuses specified sensitive material. An upload books *InformationSupplied* and changes an RFI dispute to *Responded* or a chargeback-stage dispute to *Pending*. These are intermediate statuses, not a defense win. See raw **Defend disputes**.
- Adyen automatically defends applicable chargebacks; the page says this is typically limited to credit/debit-card payments, while alternative-payment-method disputes and those requiring RFI-stage defense cannot be auto-defended. Its examples include pre-chargeback refunds, fraud codes with liability shift (excluding digital wallets in the stated example), invalid technical chargebacks, and MCC mismatch. Examples do not establish eligibility for every case. See raw **Adyen auto-defense for disputes**.
- In some flows, an issuer can open pre-arbitration after declining defense. Merchant acceptance or decline is available only when eligible, supported by the flow, and configured and approved by Adyen. Accepting loses the dispute and brings a second chargeback; declining can lead to scheme arbitration. Additional documents depend on the payment method, and new evidence may be disregarded. If the scheme rules for the issuer, the page says a fee of up to USD 600 can be added to the second chargeback; arbitration can take months. See raw **Accept or decline pre-arbitration cases**.

## Detail locators

- Raw **View disputes** gives the Customer Area merchant-account path and dispute tabs.
- Raw **Accept disputes** lists illustrative reasons to accept; raw **Defend disputes** lists evidence and document guidance.
- Raw **See also** routes to dispute flow, reason-code defense requirements, and timeframes; consult those scheme-specific sources before treating a deadline or allowed evidence type as fixed.

## Related

- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — dispute lifecycle and status context.
- [[source-adyen-docs-risk-management-disputes-api]] — API handling route.

## Raw Sources

- [[raw/adyen/docs/risk-management/manage-disputes/2026-09-15|Manage disputes (2026-09-15 snapshot)]]
