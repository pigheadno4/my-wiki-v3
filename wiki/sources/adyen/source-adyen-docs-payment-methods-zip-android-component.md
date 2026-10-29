---
title: "Adyen Zip Android Component v5.0.0"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/android-component"
raw_files:
  - "adyen/docs/payment-methods/zip/android-component/2026-09-15.md"
tags: [adyen, zip, android, component, sessions, advanced]
---

## Overview

This 2026-09-15-captured guide explains how to add Zip to an existing Android Components integration. It identifies itself as for **v5.0.0**, released in October 2023, and directs earlier versions to a separate guide. The page gives method-specific additions for Sessions and Advanced flows, not current account eligibility or proof of a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flow tabs require an existing Android Components integration at **minimum v5.0.0** and Zip added in Customer Area. The Sessions and Advanced base guides are linked separately (pinned raw lines 21–39).
- In this Android Component v5.0.0 guide, Zip requires no additional fields for the Sessions `/sessions` request or Advanced `/payments` request, and no additional Zip-specific Component configuration for either flow. Sessions readers next create the checkout session; Advanced readers launch and show the Component (lines 41–67). These are method-specific statements and do not waive the base integration's requirements.
- The test instructions refer to Zip test credentials and checking test payments in Adyen's test Customer Area. Live acceptance requires submitting a Zip request in the live Customer Area (lines 69–75). These instructions do not establish current live enablement or a successful transaction.

## Detail locators

- Page identity, version boundary and flow prerequisites: pinned raw lines 15–39.
- API and Component configuration, and flow-specific next steps: lines 41–67.
- Test/live setup and related base guides: lines 69–81.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-zip]] — Zip method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/android-component/2026-09-15|Zip Android Component v5.0.0 guide, captured 2026-09-15]]
