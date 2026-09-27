---
title: "Braintree Getting Started Overview"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/overview"
raw_files:
  - "braintree/articles/get-started/overview-2026-09-16.md"
tags: [braintree, getting-started, braintree-direct, braintree-extend, braintree-auth, merchant-account, payment-gateway]
---

## Overview

This collected Braintree article is a getting-started map for businesses evaluating how to accept payments in an app or website. It explains the roles of a business bank account, merchant account, payment gateway and developer work; outlines Braintree Direct, Braintree Extend and Braintree Auth; and distinguishes Control Panel interaction from API integration.

Its product, PCI, Control Panel, developer-documentation, sales and third-party-integration links are navigation routes, not evidence for the linked destinations. The 2026-09-16 snapshot preserves the page's statements but does not establish current availability, pricing, eligibility or integration requirements.

## Key takeaways

- The page distinguishes a merchant account from a business bank account: the merchant account routes funds from customer accounts to the business bank account. It describes Braintree's payment gateway as the connection to banking institutions and payment processors and as the channel through which the merchant receives the bank's approval result.
- Braintree Direct is described as including both a merchant account and payment gateway. The article also says a business with its own merchant account may be able to use Braintree as a gateway-only integration by contacting Sales, with the separate merchant-account provider's fees added to Braintree processing fees.
- The page describes Braintree Direct as an end-to-end web-and-mobile payment solution, Braintree Extend as secure payment-data sharing between partners, and Braintree Auth as a way for ecommerce platforms and merchant service providers to connect to users' Braintree merchant accounts and take authorized actions for them. In this collected snapshot, Direct and Extend are stated to be available in supported countries, while Auth is limited to US merchants.
- The two documented interaction channels are the Control Panel and API. The page attributes manual recurring-billing setup, transaction management, report access and payment-method enablement to the Control Panel, while API requests are described as the route for automation and customized gateway interaction.
- For readers without developer capability, the page points to partner shopping-cart and ecommerce applications. That link is an alternative-integration route; this page does not establish any particular partner's features, eligibility or current availability.

## Detail locators

- Business bank account role: `## What you will need > ### Business bank account`, lines 19-24.
- Merchant-account purpose, Braintree Direct inclusion and gateway-only route: `## What you will need > ### Merchant account`, lines 27-31.
- Payment-gateway role and developer/SDK orientation: `## What you will need > ### Payment gateway` and `### Developer knowledge`, lines 34-41.
- Braintree Direct, Extend and Auth purposes and collected availability statements: `## How we can help`, lines 44-67.
- Control Panel and API roles: `## How to connect`, lines 70-88.
- Partner shopping-cart and ecommerce-application route: `## Other ways to integrate`, lines 91-93.

## Evidence boundary

> [!warning] Orientation and navigation, not current product proof
> This page gives high-level roles and collected availability statements. It does not document settlement timing, completed bank funding, the linked products' complete capabilities, PCI obligations, API contracts, SDK support, sales eligibility, partner behavior or a full integration procedure. Verify current product and regional support through the relevant dedicated authority before making an integration decision.

## Related

- Company: [[braintree]]
- Primary concept: [[braintree-payment-platform]]
- Supporting concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI Compliance article]] - unread navigation-only destination for the linked PCI-compliance detail; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/overview-2026-09-16|Braintree Auth overview]] - unread navigation-only destination for Braintree Auth implementation detail; not used as factual evidence here
- [[raw/braintree/articles/control-panel/overview-2026-09-16|Braintree Control Panel overview]] - unread navigation-only destination for Control Panel behavior; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/get-started/overview-2026-09-16|Braintree Getting Started Overview]] - complete collected article covering prerequisite roles, product orientations, Control Panel/API interaction channels and alternative-integration navigation
