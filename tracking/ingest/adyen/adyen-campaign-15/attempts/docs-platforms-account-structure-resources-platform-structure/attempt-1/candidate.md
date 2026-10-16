---
title: "Adyen platform payment-facilitator account structure"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/account-structure-resources/platform-structure"
raw_files:
  - "adyen/docs/platforms/account-structure-resources/platform-structure/2026-09-15.md"
tags: [adyen, platforms, payment-facilitators, account-structure, balance-accounts]
---

## Overview

This Adyen for Platforms page explains a **payment-facilitator account-structure example**, separating resources that belong to the platform from those assigned to each platform user. It says platform users have the contractual relationship with payment methods, while the platform maintains a relationship with its users and customers typically interact with those users. The **EU/US Example Travel LLC** names, regions, stores and fund flow are illustrative. The page does not determine the legal seller or merchant of record for every transaction, establish a particular business's account eligibility or prove a payment, settlement or bank payout.

## Key takeaways

- The page distinguishes this setup from general Platforms where the business is already Visa/Mastercard-registered as a payment facilitator, has individual users accepting in-person payments, or has users with high-risk MCCs. In those cases it says onboarding is as a payment facilitator. This is a conditional integration model, not a blanket classification for every platform.
- For each region where a platform is registered and wishes to acquire, the guide says it must have a **balance platform and merchant account**. Its example has one company account, three merchant accounts across NL/DE/US, two balance platforms across EU/US, a **liable account holder and liable balance account for platform funds**, and a platform legal entity per acquiring region for KYC.
- Each example user has physical-location stores tied to the respective merchant account, at least one account holder **per country of operation** defining payment-processing capabilities, at least one **base-currency balance account per account holder** for user funds, and a **verified transfer instrument** for each balance account's payout. It also lists a user legal entity and business line per operating country for KYC and industry information. These account holders, legal entities, balance accounts, merchant accounts and transfer instruments are separate resources, not interchangeable labels.
- The Amsterdam example routes a customer's payment through a user store to the Dutch merchant account, settles funds into balance accounts on the EU balance platform, splits between platform liable and user balance accounts, holds the user share until payout, then pays to that account holder's verified bank-account transfer instrument. It is a design illustration, not a live trace or bank-receipt proof; split configuration and actual processing must be assessed separately.
- The page provides no role/credential specification, account-creation procedure, verification-status result, contractual seller allocation, country eligibility decision, actual split instruction or payout confirmation. Follow the resource-specific guides and current account state for those questions.

## Detail locators

- Raw lines 15–33: platform/user/customer relationship and conditional payment-facilitator triggers.
- Raw lines 35–60: per-acquiring-region requirement and illustrative platform company/merchant/balance/liable/legal-entity resources.
- Raw lines 62–78: user stores, per-country account holder/legal entity/business line, balance accounts and verified transfer instruments.
- Raw lines 80–84: example resource-relationship diagram.
- Raw lines 86–94: illustrative Amsterdam payment, split, balance retention and payout sequence.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform account, onboarding, verification and money-flow context.
- [[adyen-pos-payment-facilitators]] — distinct POS payment-facilitator integration details.

## Raw Sources

- [[raw/adyen/docs/platforms/account-structure-resources/platform-structure/2026-09-15|Platform structure, fetched 2026-09-15]]
