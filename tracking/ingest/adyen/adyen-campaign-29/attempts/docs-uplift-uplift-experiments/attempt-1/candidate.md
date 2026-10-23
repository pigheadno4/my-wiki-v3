---
title: "Adyen Uplift experiments"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/uplift/uplift-experiments"
raw_files:
  - "adyen/docs/uplift/uplift-experiments/2026-09-15.md"
tags: [adyen, uplift, experiments, checkout, optimization, risk]
---

## Overview

This 2026-09-15 Adyen documentation snapshot describes how merchants start, evaluate, and stop Uplift checkout and optimization experiments, and routes risk A/B tests to separate Protect documentation. These are experiments on real transactions in a live Adyen account, not simulations or evidence that any merchant achieved uplift. See [[adyen]] and [[adyen-uplift]].

## Key takeaways

- The integration must support Adyen Uplift. All Customer Area users can see the Experiments page, but starting a checkout experiment requires Merchant admin or Merchant manage Uplift optimize settings together with Change payment methods; a recommendation-based optimization experiment requires Merchant manage Uplift optimize settings; a risk experiment requires Risk admin and Protect premium. [Requirements, raw lines 23–33; Risk experiments, lines 57–61]
- A checkout payment-method experiment tests temporarily excluding an already activated method for a selected country or region, with at least three active methods; primary methods such as credit or debit cards cannot be tested this way. Dynamic-ordering experiments require the Personalize requirements and, for Advanced flow, `shopperConversionId`; dynamic ordering must already be enabled. [Requirements, lines 32–33; Checkout experiments, lines 43–47; Dynamic ordering, lines 93–96]
- An optimization experiment is available only when an applicable recommendation offers it and its country, payment-method, feature, and other stated requirements are met. The selected transaction traffic is split evenly between current Variant A and recommended Variant B. Choosing a recommendation and creating a test does not itself adopt the recommended setting. [Optimization experiments, lines 49–55; Start, lines 126–149]
- Results for running and completed experiments can be compared in Customer Area; first results take about four hours, with later updates. Adyen recommends waiting for statistical significance before stopping. If stopped early, it recommends rerunning longer or with more traffic. These are evaluation guidance, not a measured outcome for an account. [Results, lines 151–161; Stop, lines 163–167]
- For optimization, **End** stops while retaining the current setting, whereas **End & change setting** acts on the recommendation and changes settings. Checkout uses **End**. The live-transaction exposure and setting-change choice are material operational boundaries. [Stop, lines 169–176]

## Detail locators

- Checkout payment-method creation, merchant-account/country choice, traffic percentage and ability to change traffic: raw lines 65–91.
- Dynamic ordering goals Conversion and Cost, equal variant allocation, example percentages and editing limits: raw lines 93–124.
- Recommendation-based optimization creation and merchant-account/traffic selection: raw lines 126–149.
- Customer Area results navigation and experiment-type tabs: raw lines 151–161. Risk experiment procedure is only linked from this page: raw lines 57–61.

## Related

- [[adyen-uplift]]
- [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/uplift/uplift-experiments/2026-09-15|Adyen Uplift experiments, 2026-09-15 snapshot]]
