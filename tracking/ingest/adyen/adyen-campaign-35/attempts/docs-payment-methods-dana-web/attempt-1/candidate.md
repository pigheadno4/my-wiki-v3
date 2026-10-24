---
title: "Adyen DANA for Web integration chooser"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/web"
raw_files:
  - "adyen/docs/payment-methods/dana/web/2026-09-15.md"
tags: [adyen, dana, web, navigation]
---

## Overview

This [[adyen]] DANA for Web page is an **integration chooser**. It links DANA **Web Drop-in** and **Web Components** child guides, and the main Web **Sessions** and **Advanced** guides for each UI route. The Components description names Redirect, but the chooser itself supplies no redirect handling procedure, version requirement, merchant eligibility, recurring setup or payment-result evidence. [[adyen-online-payments]]

## Key takeaways

- **Method-specific children:** The Drop-in child is labelled an all-in-one UI solution. The Components child is described as using Redirect for DANA on a website. These labels point to distinct child documentation; they do not by themselves document implementation or a completed redirect/payment. See raw lines 19–27.
- **Main integration first:** The See also section says to create the main Web integration before adding DANA. It links Drop-in and Components main guides under both Sessions and Advanced flows, without stating their requirements on this chooser page. See raw lines 29–36.

## Detail locators

- DANA Web Drop-in and Components choices: raw lines 19–27.
- Main Web Sessions/Advanced routes: raw lines 29–36.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/web/2026-09-15|Adyen DANA Web chooser snapshot]]
