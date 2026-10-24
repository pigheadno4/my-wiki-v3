---
title: "DANA for Android integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/android"
raw_files:
  - "adyen/docs/payment-methods/dana/android/2026-09-15.md"
tags: [adyen, dana, android, navigation]
---

## Overview

This 2026-09-15 Adyen page is an **Android integration chooser** for DANA. It links Drop-in and Components child guides and four main Android integration guides. It says the main integration should be created before adding DANA, but supplies no independent method setup or payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The **Drop-in** child link is presented as an all-in-one UI route for DANA in an Android app. The **Components** child link names `InstantPaymentComponent` for handling a redirect to DANA. This describes the linked route; the chooser does not give the component configuration or redirect completion sequence. (raw lines 19–27)
- The See also section directs readers to create the main integration first and links Android Drop-in and Android Components main guides for **Sessions** and **Advanced** flows. These are base-guide links; the page alone does not establish each child guide's supported flows or SDK/API minimum versions. (raw lines 29–36)
- This chooser does not specify DANA eligibility, request fields, app-switch or return behavior, token/recurring conditions, TEST/LIVE setup, webhook results or observed authorization/capture/settlement. Consult the appropriate child and method guides for those matters. (raw lines 15–36)

## Detail locators

- Drop-in and Components child-guide choices: raw lines 19–27.
- Main-integration sequencing and Sessions/Advanced base-guide links: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-dana]]
- [[source-adyen-docs-payment-methods-dana-android-drop-in]]
- [[source-adyen-docs-payment-methods-dana-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/android/2026-09-15|Adyen DANA for Android, 2026-09-15 snapshot]]
