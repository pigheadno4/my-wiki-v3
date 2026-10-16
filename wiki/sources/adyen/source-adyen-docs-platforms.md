---
title: "Adyen for Platforms overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms"
raw_files:
  - "adyen/docs/platforms/2026-09-15.md"
tags: [adyen, platforms, onboarding, split-payments, payouts]
---

## Overview

This 2026-09-15-captured **Adyen for Platforms** landing page addresses commerce, ordering, POS, retail-management and SaaS platforms that process online and/or in-person payments on behalf of their users. It routes to user onboarding/verification, split payment processing, managed or custom payouts/transfers, risk and reporting. It points readers who need a different model to a separate marketplace integration guide. This is current-platform orientation, not the classic Marketplace/Marketpay contract or an assertion that the platform is merchant of record. See [[adyen-platforms]] and [[adyen]].

## Key takeaways

- **User versus platform roles:** The page calls the integrating business the platform and its sellers, service providers or contractors its users. It says Adyen verifies onboarded users before payout and informs the platform of check results. API example links for legal-entity creation, split `/payments` and `/transfers` are navigation; they do not define legal-entity, account-holder, balance-account, liable/reserve-account or transfer-instrument relationships, required credentials or the user's actual capability status.
- **Payment and payout lifecycle:** The page says the platform processes payments on behalf of users, may split amounts between one or more users, deduct costs, hold funds, and choose managed payouts or custom payout timing; it also lists within-platform fund movement. Those are capability descriptions, not proof of a particular split, transfer, payout bank receipt or settlement. The page gives no allocation of legal seller, payee, merchant of record, chargeback liability or fund ownership for a specific commercial model.
- **Geography is qualified:** The snapshot lists user-onboarding countries in Europe, North America and Asia Pacific and a separate set of acquiring regions. The Channel Islands and Isle of Man footnote excludes **in-person payments and store creation** there even though included in the UK onboarding list. Listed geography does not establish a merchant's current entity, method, product or acquiring eligibility.
- **Separate optional financial products:** Issuing, business accounts and Capital are presented as additional products beyond platform payment processing. Their availability and extra verification are expressly routed to a separate guide; this page's brief feature descriptions do not grant any user a card, bank account or financing offer, or prove issuer authorization or funds movement.
- **Next-step boundary:** The page links to get-started, integration checklist and verification overview guides. Actual entity/account creation, permissions, verification, compliance, payment and payout behavior require those child routes and operational evidence.

## Detail locators

- Lines 15–28: Adyen for Platforms audience/model and marketplace alternative.
- Lines 30–40: API example navigation and onboarding, split payments, managed/custom payouts, risk and reports.
- `## Supported countries/regions`, lines 42–98: user-onboarding list and Channel Islands/Isle of Man exclusion.
- `## Acquiring regions`, lines 100–113: separate acquiring geography.
- `## Offer additional financial products`, lines 115–142: issuing/business accounts/Capital and separate availability/verification route.
- `## Next steps`, lines 144–162: get-started, checklist and verification navigation.

## Related

- [[adyen-platforms]] — Adyen for Platforms concept and scope boundary.
- [[adyen-payments]] — general payments and channel orientation.
- [[adyen-mirakl]] — Mirakl connector that uses Adyen for Platforms; its operator/pay-in boundaries are separate.
- [[adyen-reporting]] — general reporting concept; platform report details require the child route.

## Raw Sources

- [[raw/adyen/docs/platforms/2026-09-15|Adyen for Platforms overview, captured 2026-09-15]]
