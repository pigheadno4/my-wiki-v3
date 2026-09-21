<!-- Source URL: https://developer.paypal.com/braintree/in-person/reference/general-payments-terminology -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: General Payments Terminology
slug: /in-person/reference/general-payments-terminology/
createTime: '2024-11-20T19:05:17.215Z'
updateTime: '2024-11-20T19:05:17.524Z'
---



# General Payments Terminology

This page is meant as a glossary of relevant payment industry terminology referenced throughout the Braintree documentation.


## [](#payments-industry-terminology/)Payments Industry Terminology

| **Payments Industry term** | **Description** |
| **Payment Card Industry (PCI) Council** | The PCI council is a non governmental industry standard for the payments industry. They generally set the best practices for the processing of card data safely and securely. They are also issue industry standard certifications |
| **End to End Encryption (E2EE)** | E2EE is a PCI standard of encrypting sensitive card data from the point of collection (card reader) to the point of processing. This standard protects the card data while it's passed from merchant to processor. The Braintree solution is E2EE |
| **Point to Point Encryption (P2PE)** | P2PE is a slightly higher PCI standard than E2EE which not only deals with the secure transmission of the card data but also the chain of custody of the card readers which are used to collect the card data. Braintree is currently undergoing P2PE certification with the PCI council |
| **EuroPay, Mastercard, and Visa (EMV) Standard** | EMV refers to the collective standard set by EuroPay, Mastercard and Visa which deals with the encryption of card data for cards that have EMV chips embedded in them. Most cards issued today have these chips |
| **EMV Liability Shift** | In 2015 the United States banking industry adopted the EMV standard and incentivized merchant and payment processor adoption by shifting the liability of chargebacks from the merchant to the card issuer for eligible transactions when the EMV standard is used |
| **Card Networks** or sometimes referred to as Card Schemes | This term refers to the entity which creates the infrastructure on which credit and debit cards are issued and processed. Example: Visa, Mastercard, Discover, AMEX, etc... |
| **Interchange Fees** | These are the transaction fees levied on a merchant by the Card Networks and are generally shared between the Card Network, Issuing Bank, and Acquiring Bank |
| **US Pin Debit Gateways** | The US Pin Debit gateways are payment networks that specialize in the processing of US issued Debit Cards. This industry was boosted by the 2010 legislation called the [Durbin Amendment](https://www.federalreserve.gov/econres/feds/bank-profitability-and-debit-card-interchange-regulation-bank-responses-to-the-durbin-amendment.htm) which aimed to create more competition in the debit card processing space, as well as to cap the interchange fees which can be collected on debit cards issued by banks with over $10 billion in assets |


## [](#omni-channel-eco-system-terminology/)Omni-Channel Eco-System Terminology

| **General Industry term** | **Description** |
| **Point of Sale System (POS)**, sometimes referred to as Electronic Cash Register (ECR), Cash Register, etc... | The software and hardware that the cashier uses to input an order and initiate a transaction from in the store which is often integrated with a payment processor such as Braintree or PayPal |
| **Property Management System (PMS)** or sometimes referred to as Booking System, Point of Sale System (POS), etc... | This is software and hardware that functions like a POS system but is tailored for the hotel industry |
| **Order Management System (OMS)** | This is the software that manages orders which are generally received from an e-commerce channel such as a website, or mobile app, or sometimes a Point of Sale System. From order acceptance to fulfillment and often the trigger for the capture of funds from the payment processor such as Braintree or PayPal |
| **Enterprise Resource Planning (ERP) System** | This is a software that generally manages the book keeping and accounting and is typically the final source of truth for an accounting team, this can be integrated with Braintree or PayPal for certain use cases |
| **Call Center Application** | Software that hosts an application typically used in a merchant customer service center or call center for things like refunding customers or taking orders over the phone and charging a customer |
| **E-Commerce Front-end Software** | Referring to the software hosting a merchant's E-commerce website which is often integrated with a payment processor such as Braintree or PayPal |


## [](#braintree-payments-terminology/)Braintree Payments Terminology

| **Braintree term** | **Description** |
| **Card Reader or Reader**, sometimes referred to as Payment Terminal, Card Terminal, Pin Entry Device (PED), Pin Pad | The hardware device that is used to accept card present payments. For example Braintree supports [P400](/braintree/in-person/hardware/verifone-p400/), [M400](/braintree/in-person/hardware/verifone-m400/), [E285](/braintree/in-person/hardware/verifone-e285/), and [V400m](/braintree/in-person/hardware/verifone-v400m/) card reader models |
| **GraphQL API** | [Braintree API](/braintree/in-person/about/technical-overview/#intro-to-braintree-graphql) that allows for integrated communication to a Braintree card reader from a merchant software application or web app |
| **Tokenization** | The process of collecting sensitive card data or transaction data and generating a reference token that can be used to refer to that sensitive data within the Braintree platform. Example use cases: Referenced refunds, capture of funds against an authorization, card on file payments, recurring payments, etc.. |
| **Vaulting** | [Vaulting](/braintree/in-person/guides/vaulting-and-customers/) is the process of creating a unique customer record (customerId) within the Braintree platform and linking data to it such as email, phone, customer name, or transaction data. Example use cases: marketing database, customer purchase history, subscriptions billing, loyalty, etc... |
| **Contactless or Near Field Communication (NFC)** | The technology that allows for a card reader to accept digital wallets or contactless chip enabled credit and debit cards simply by tapping the payment instrument on the card reader NFC interface |
| **QR Code (QRC) Payment Method** | Refers to [the acceptance of PayPal and Venmo](/braintree/in-person/guides/paypal-and-venmo-qrc/) digital wallets as a payment method via a QR code rendered on the card reader display or merchant POS system |
| **Digital Wallets** | The [digital wallets](/braintree/in-person/about/solution-coverage/#digital-wallets-supported) which often utilize NFC or contactless payment interfaces. For example: Apple Pay, Google Pay, Samsung Pay, etc... |
| **Store and Forward** | [Store and Forward](/braintree/in-person/guides/offline-transactions/) is a common offline processing solution which allows a merchant to continue accepting payments even with they are experiencing a network outage in the store |
| **Offline Floor Limits** | Refers to the maximum transaction amount which a merchant would allow for a store and forward offline solution. This configuration is [managed by the POS system](/braintree/in-person/guides/offline-transactions/#offline-floor-limits) and helps the merchant mitigate the liability risks associated with an offline transaction |
| **Safety Stock** | This refers to the extra card readers purchased by the merchant from Braintree to maintain in their inventory in the event that a store needs a quick card reader replacement |

[EMV Receipt Reference](/braintree/in-person/reference/emv-receipt-reference/)[GraphQL Docs](/braintree/in-person/reference/graphql-docs/)