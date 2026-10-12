---
title: "Adyen Docs: Manage disputes with the Disputes API"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/disputes-api"
raw_files:
  - "adyen/docs/risk-management/disputes-api/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, api]
---

## Overview

This Adyen guide explains the merchant's Defend Disputes API workflow: receive dispute webhooks, retrieve applicable defense reasons and evidence requirements, then either accept the dispute or upload an eligible evidence package and make a final defend request. Manual handling through Customer Area is a separate route. The page is a 2026-09-15 captured documentation snapshot whose own `last_modified` metadata is 2020-05-27; it is not proof of current account access, a successful API call, or a won dispute.

## Key takeaways

- The guide calls for an online payments integration and an API credential with API key and **API dispute management** role. To follow disputes by webhook, subscribe to the Standard webhook and enable dispute events. Not all dispute types can be defended. Scheme-specific chargeback rules and Adyen automatic handling are linked as separate checks. See **Requirements**.
- `REQUEST_FOR_INFORMATION` asks for information before a chargeback debit, while `NOTIFICATION_OF_CHARGEBACK` marks an incoming defendable chargeback and the start of the defense period; the page says debit usually follows days later. These are distinct triggers for the merchant's response. See **Handle dispute webhooks**.
- `/retrieveApplicableDefenseReasons` returns dispute-specific reason codes and document types with requirement levels. The guide distinguishes `Required`, `OneOrMore`, `Optional`, and support-enabled `AlternativeRequired`; its JSON is an example for an account where `AlternativeDefenseMaterial` is enabled. A defense using a chosen reason needs evidence meeting that reason's document requirements. See **Retrieve defense reasons and evidence requirements**.
- Uploading with `/supplyDefenseDocument` only stores the documents for the defense; it does not submit them to the issuer. Adyen says it refuses material containing sensitive data such as passports, social security numbers, PAN, or sensitive authentication data. File type, size, and page limits vary by scheme and use case; check **Upload dispute defense documents** before sending evidence. Previously uploaded documents can be deleted and replaced before the final defense.
- `/defendDispute` submits the complete defense to the scheme. After defending, the merchant can no longer supply additional information; the merchant then follows dispute status through webhooks. An API `success` result for document upload or defend submission is not a scheme decision. See **Defend the dispute**.
- Pre-arbitration handling is optional only when the merchant is eligible and the dispute flow supports it, and requires extra Adyen configuration and approval. Accepting or partially accepting leads to a lost or partially lost dispute and second chargeback. Declining may lead to scheme arbitration; this page warns of a fee up to USD 600 if the scheme rules for the issuer and says arbitration can take several months. Treat these fee and timing statements as captured documentation, not current scheme policy. See **Optional: Handle pre-arbitration cases**.

## Detail locators

- **Requirements, lines 23–36** — access, webhook qualification, non-defendable disputes, and scheme/automatic-handling links.
- **How it works / Handle dispute webhooks, lines 38–69** — stages and RFI versus notification-of-chargeback events.
- **Retrieve defense reasons and evidence requirements, lines 71–141** — identity fields, applicable reasons, document codes, requirement levels, and support-enabled alternative material.
- **Optional: Accept the dispute / Upload dispute defense documents, lines 143–239** — accept path, sensitive-data prohibition, formats and limits, upload versus submission, and replace-before-defend path.
- **Defend the dispute, lines 241–265** — final API request, no further evidence, and status-webhook follow-up.
- **Optional: Handle pre-arbitration cases, lines 267–363** — eligibility and approval, accept/partial-accept/decline paths, second chargeback, fee and timing warning.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[disputes]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/risk-management/disputes-api/2026-09-15|Adyen Docs — Manage disputes with the Disputes API (2026-09-15)]]
