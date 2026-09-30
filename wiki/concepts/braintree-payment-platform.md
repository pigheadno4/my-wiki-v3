---
title: "Braintree Payment Platform"
type: concept
category: technology
tags: [braintree, payment-platform, braintree-direct, braintree-extend, braintree-auth, merchant-account, payment-gateway]
---

## Braintree Payment Platform

Braintree's collected getting-started overview distinguishes a business bank account from the merchant account used to route customer funds to it and the payment gateway that connects the merchant to banking institutions and payment processors. Braintree Direct is described as providing both the merchant account and gateway; a business that already has a merchant account may instead ask Sales about gateway-only integration, with that provider's fees additional to Braintree processing fees. [[source-braintree-get-started-overview]]

## Product orientations

The overview describes Braintree Direct as an end-to-end web-and-mobile payment solution, Braintree Extend as secure payment-data sharing between partners, and Braintree Auth as allowing ecommerce platforms and merchant service providers to connect with users' Braintree merchant accounts and take authorized actions for them. In the collected snapshot, Direct and Extend are stated as available in supported countries, while Auth is stated as available only to US merchants. These are collected orientation and availability statements, not proof of current eligibility or complete product behavior. [[source-braintree-get-started-overview]]

## Interaction routes

The article separates the Control Panel's manual gateway-administration functions from API requests used to automate and customize gateway interaction. It also points readers without developer capability to partner shopping-cart and ecommerce applications, without establishing any named partner's features or current availability. Use [[braintree-control-panel]] for the dedicated administration route and the source's raw locators for the exact collected wording.

## Post-settlement funding route

Braintree's collected Get Paid guide starts after a transaction has settled. It says funds then pass through the merchant account to the bank account provided during application, with funding managed by the merchant-account provider; Braintree Direct is the page's Braintree-managed case. Payment method and account type affect how and when funds are paid, and the page treats its 2–5-business-day card and aggregated-Amex timing as typical or expected rather than guaranteed. This route is general funding guidance, not documentation of payment acceptance, evidence that an individual transaction settled, or proof that a deposit arrived. [[source-braintree-get-started-get-paid]]

PayPal transactions follow a separate collected funding route: by default PayPal funds them to the merchant's PayPal Business Account balance, after which the merchant can withdraw manually or have PayPal configure Settlement Withdrawal. The article says that feature sends the previous day's transactions to the bank within 2-3 business days and exposes a daily report for each withdrawal; this snapshot-scoped route is not evidence that an individual transaction funded or that a deposit arrived. [[source-braintree-payment-methods-paypal-funding-reconciliation]]

## Sources

- [[source-braintree-get-started-explore]] - collected navigation map with brief orientations for fraud tools, PCI compliance, Control Panel administration, recurring billing, chargebacks and retrievals, PayPal, reporting, and risk/security
- [[source-braintree-get-started-overview]] - business-bank-account, merchant-account and payment-gateway roles; Braintree Direct, Extend and Auth orientations; Control Panel/API interaction channels; and the partner-application route
