---
title: "Universal Commerce Protocol (UCP)"
type: concept
category: standard
tags: [ucp, universal-commerce-protocol, agentic-commerce, open-standard, payment-token-exchange, oauth]
---

## Overview

The **Universal Commerce Protocol (UCP)** is an open standard for agentic commerce interoperability. It defines how different participants in commerce transactions — platforms, sellers, agents, credential providers — can exchange data and operate across each other's systems. Developed at [ucp.dev](https://ucp.dev); Stripe is a member of the UCP Tech Council.

## Key Capabilities

- **Checkout**: Create and manage checkout flows (cart, tax, payment) with or without human intervention
- **Identity linking**: OAuth 2.0-based authorization — platforms act on a buyer's behalf across systems
- **Order**: Webhook-based lifecycle updates for shipping, delivery, and returns
- **Payment token exchange**: Secure exchange of payment tokens and credentials between platforms, businesses, and credential providers

## Relationship to Other Standards

- **x402**: HTTP payment protocol (machine-to-machine, Base/USDC) — complementary; UCP is broader scope
- **MPP** (Machine Payments Protocol): covers fiat + crypto for machine-to-machine payments
- **ACP** (Agentic Commerce Protocol, by OpenAI): product feed + agentic checkout + delegated payment — similar scope to UCP

## Key Players

- **Stripe**: UCP Tech Council member; implements UCP payment handlers
- **Universal Commerce Protocol org**: GitHub at `Universal-Commerce-Protocol/ucp`

## Sources

- [[source-stripe-ucp]] — Stripe's overview of UCP and their payment handler implementation
