---
title: "Adyen Oracle Xstore integration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/oracle-xstore"
raw_files:
  - "adyen/docs/plugins/oracle-xstore/2026-09-15.md"
tags: [adyen, oracle-xstore, pos, eftlink]
---

## Overview

This Adyen webpage introduces the **Oracle Xstore** retail POS integration. Xstore provides POS and back-office functions; Adyen terminals use Oracle **EFTLink with Oracle Payment Interface (OPI)** to take in-person payments through the Adyen payments platform. **Xstore Mobile** is a distinct mobile-app route using Adyen Android all-in-one terminals. This 2023-modified page was captured in 2026 and does not establish current support, merchant enablement or a completed payment. See [[adyen]] and the proposed [[adyen-oracle-xstore]] concept.

## Key takeaways

- The page states **Xstore version 15 or later** with **EFTLink version 17 or later**, and says Adyen terminals implement OPI version 17 and later. EFTLink maps a transaction to a terminal and sends the Xstore request to that device. This is an in-person POS route, not an online checkout or standalone Terminal API implementation contract.
- Its terminal matrix separates Xstore from **Xstore Mobile**. Every listed model has an Xstore mark; only **S1E2L, S1F2 and S1F2L** also have an Xstore Mobile mark. **V240m Plus** is labeled Brazil only. This is a dated compatibility table, not a guarantee for any merchant or present device fleet.
- Listed features include sale, void, referenced/unreferenced refunds, partial authorisations, dynamic currency conversion, MOTO, manual key entry, tax-free shopping, gift cards, private-label cards and enhanced scheme data. The page says **void is supported only within the same settlement day** and private-label support is **Bread Financial cards only**. The feature list does not prove transaction success, current regional eligibility, fee savings or every terminal/model combination.
- Setup begins with an Adyen test account and **Support enablement of OPI** in Customer Area, then store creation, terminal order/assignment, feature configuration and terminal boarding. Xstore Mobile adds APK creation/upload, certificate upload and deployment. Linked guides own detailed configuration and live-account requirements; this source is an orientation page.

## Detail locators

- Xstore and Xstore Mobile identities, EFTLink/OPI and version gates: pinned raw lines 15–31.
- Terminal model matrix and Brazil-only qualification: pinned raw lines 33–50.
- Message routing and feature-specific limits: pinned raw lines 52–77.
- Test account, OPI enablement and terminal setup routes: pinned raw lines 79–93.
- Xstore Mobile app/certificate/deployment steps: pinned raw lines 95–101.

## Related

- [[adyen-oracle-xstore]] — provider concept for this distinct POS integration family.
- [[adyen-payment-terminals]] — general Adyen terminal context; this source owns Xstore's compatibility table.

## Raw Sources

- [[raw/adyen/docs/plugins/oracle-xstore/2026-09-15|Adyen Oracle Xstore overview, captured 2026-09-15]]
