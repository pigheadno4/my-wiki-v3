---
title: "Boleto Bancário for Web integration chooser"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/web"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/web/2026-09-15.md"
tags: [adyen, boleto-bancario, web, integration-router]
---

## Overview

This 2026-09-15-captured Adyen page is the **Web integration chooser** for Boleto Bancário. It routes to Web Drop-in or Components child guides, and to the corresponding Sessions or Advanced base guides. It does not itself define request fields, voucher status, due-date handling, merchant enablement or completed payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-boleto-bancario|method overview]].

## Key takeaways

- **Drop-in** is described as Adyen's all-in-one UI option for adding Boleto Bancário to a website. Follow [[source-adyen-docs-payment-methods-boleto-bancario-web-drop-in]] for method-specific Sessions/Advanced details; the chooser itself gives only a route (raw lines 19–23).
- **Components** is the other website route. The page's description says “Use the Boleto” and links the Web Component child; follow [[source-adyen-docs-payment-methods-boleto-bancario-web-component]] for actual Component and flow details. The chooser does not specify a Component class or API action from that short label (raw lines 25–27).
- The **See also** section explicitly says to create the main integration before adding Boleto Bancário and links four base routes: Web Drop-in or Components, each with Sessions or Advanced flow (raw lines 29–36).
- The separate [[source-adyen-docs-payment-methods-boleto-bancario|overview]] identifies Boleto as a **BR/BRL voucher** and distinguishes voucher issue from later cash/ATM/online payment. It also records unpaid due-date versus later `Offer cancelled` status timing; these are method-level facts, not claims made by this chooser (overview pinned raw lines 23–43).

## Detail locators

- Web chooser and Drop-in route: raw lines 15–23.
- Components route and source's “Use the Boleto” wording: raw lines 25–27.
- Base Sessions/Advanced guides and main integration prerequisite: raw lines 29–36.
- Method-level voucher lifecycle, BR/BRL and cancellation timing: [[source-adyen-docs-payment-methods-boleto-bancario]] and its pinned raw lines 23–43; this entry's raw_files remains chooser-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]
- [[source-adyen-docs-payment-methods-boleto-bancario-web-drop-in]]
- [[source-adyen-docs-payment-methods-boleto-bancario-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/web/2026-09-15|Boleto Bancário Web chooser, captured 2026-09-15]]
