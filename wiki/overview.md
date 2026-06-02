# Payments Industry Overview

The payments industry is a layered ecosystem that moves money from buyers to sellers. Understanding it requires knowing what each layer does and which companies operate where.

## The layers

**Payment networks** — [[Visa]], [[Mastercard]], and [[American Express]] operate the rails that connect card-issuing banks (issuers) to merchant-acquiring banks (acquirers). They set [[interchange fees]], define transaction rules, and handle cross-border routing. These networks don't hold consumer accounts — they provide the infrastructure that makes card payments work globally.

**Processors** — Companies that handle the technical work of routing transactions between merchants, acquirers, and networks. Some processors are standalone; many are now bundled into larger platforms.

**Payment gateways** — The interface between a merchant's checkout experience and the processing infrastructure. A gateway encrypts card data, passes it to the processor, and returns the result. Historically a separate product, now typically integrated into PSPs.

**Payment service providers (PSPs)** — Integrated platforms that bundle gateway, processing, and merchant services into a single product. [[Stripe]], [[PayPal]], [[Adyen]], and [[Square]] are the major players. They handle everything from checkout to settlement, often including fraud detection, reporting, and [[PCI compliance]]. PSPs are where most of the innovation and competition happens today.

## Emerging areas

**Buy Now, Pay Later (BNPL)** — Companies like [[Klarna]] and [[Affirm]] offer installment-based payment at checkout, sitting alongside traditional card payments as an alternative method.

**[[Real-time payments]]** — Instant bank-to-bank transfer networks (FedNow in the US, Faster Payments in the UK, UPI in India) that bypass the card networks entirely.

**[[Embedded finance]]** — Non-financial companies embedding payment processing, lending, or banking directly into their products, powered by PSP APIs and [[banking-as-a-service]] platforms.

**[[Open banking]]** — Regulatory frameworks (PSD2 in Europe) that require banks to share account data via APIs, enabling third-party payment initiation and account aggregation.

---

_This page provides initial context for the wiki. It will be revised and expanded as sources are ingested._
