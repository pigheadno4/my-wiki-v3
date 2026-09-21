<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23 -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Mastercard Networks
slug: /articles/risk-and-security/compliance/network-updates/2023/mastercard-f23/
createTime: '2025-04-02T01:22:43.901Z'
updateTime: '2025-04-02T01:22:43.924Z'
---



# Mastercard Networks


## **What is the Mastercard Preauthorization Fee mandate?**

**FEE CHANGE** | **Mastercard** | **US**

From 8 October 2023, Mastercard will begin charging all US merchants who use pre-authorizations a 1.25bps (0.0125%) per transaction fee for pre-authorizations on Mastercard card-not-present (CNP) transactions with a minimum of $0.01.


## **What is the revised excessive authorization transaction processing excellence program mandate?**

**FEE CHANGE** | **Mastercard** | **US**

Starting 1 November 2023, merchants will incur fees if they retry a transaction more than 35 times in a 30-day period. As part of Mastercard's Transaction Processing Excellence Program (TPE)—a series of transaction monitoring initiatives to drive complaint behavior in the ecosystem—any further retry attempt(s) past the 35 allowed will incur a $0.15 per transaction fee.

**Note** : this retry fee will further increase to $0.30/transaction from 1 January 2024, and $.50/transaction from 1 January 2025.

| **Rate** | **Effective Date** |
| $0.15 | 1/1/23 |
| $0.30 | 1/1/24 |
| $0.50 | 1/1/25 |


## **What is the Authorization optimizer for CNP transactions mandate?**

**FEE CHANGE** | **Mastercard** | **US, CA, EU**

Mastercard is introducing the Authorization Optimizer Program for recurring card-not-present (CNP) transactions with insufficient funds, effective 9 October 2023 in the US, 1 January 2024 in EU, and TBD 2024 in CA. Mastercard will send a Merchant Advice Code (MAC) in response to decline code 51 (NSF). The MAC will provide the merchant an optimal time to retry the transaction.

| **Region** | **Effective Date** | **Fee** |
| US | 1 October 2023 | $0.02 |
| Canada | TBD 2024 | $0.02 |
| EEA, UK | 1 January 2024 | €0.004 |
| Non-EEA | 1 January 2024 | €0.01 |



Merchants who receive a response code 51 (insufficient funds) and a MAC 24-30 will receive a fee.





Merchants should use the MAC received to guide their retry strategy. A fee applies whether the merchant uses the MAC or not.



| **MAC Value** | **Description** |
| 24 | Retry after 1 hour |
| 25 | Retry after 24 hours |
| 26 | Retry after 2 days |
| 27 | Retry after 4 days |
| 28 | Retry after 6 days |
| 29 | Retry after 8 days |
| 30 | Retry after 10 days |

Merchant Advice Codes (MACs) are a set of codes that Mastercard supports to enable issuers to further communicate to acquirers and merchants the reasons for declining a transaction. These codes indicate to the merchant and acquirer the best action to take following a declined transaction.

MACs are part of Mastercard's Transaction Processing Excellence (TPE) Program. The TPE program is a series of transaction monitoring initiatives to drive complaint behavior in the ecosystem.


## **What is the Authorization Optimizer for CNP Transactions (APAC) mandate?**

**FEE CHANGE** | **Mastercard** | **APAC**

Starting 9 October 2023, Mastercard is introducing authorization optimizer for declines codes 79 (Lifecycle), 82 (Policy), and 83 (Security) and Merchant Advice Code (MAC) 01 or 03. A fee of 3bps (0.03%) will be charged when the combination of declines codes 79, 832, 83 and MAC 01 or 03 are used. These MACs have been live in other regions since April 2022.

Merchant Advice Codes (MACs) are a set of codes that Mastercard supports to enable issuers to further communicate to acquirers and merchants the reasons for declining a transaction. These codes indicate to the merchant and acquirer the best action to take following a declined transaction.

MACs are part of Mastercard's Transaction Processing Excellence (TPE) Program. The TPE program is a series of transaction monitoring initiatives to drive complaint behavior in the ecosystem.

**APAC Countries in Scope** : Bhutan, Brunei, Cambodia, India, Malaysia, Maldives, Nepal, Philippines, Singapore, South Korea, Sri Lanka, Thailand, Vietnam, Myanmar, Bangladesh.


## What are the new Mastercard merchant advice codes mandate?

**FEE CHANGE** | **Mastercard** | **GLOBAL**

Starting 7 October 2023, Mastercard is introducing 2 new Merchant Advice Codes (MAC) to provide intelligence to acquirers and merchants on consumers using non-reloadable prepaid cards and single-use virtual accounts:


- **40**: Consumer non-reloadable prepaid card
- **41**: Consumer single-use virtual card

This data is currently only available from the card BIN, which not all merchants receive. These codes will be sent for approved and declined transactions. There are no fees associated with these MACs.

The intent of the new merchant advice codes is to improve Card Not Present authorization rates for non-reloadable pre-paid and single use virtual card products and provide intelligence to merchants processing subscriptions or recurring transactions.

Merchants that accept non-reloadable prepaid and single use virtual cards have the opportunity to use the MAC and proactively inform their customers using these products for ongoing purchases that a replacement payment source should be added to ensure uninterrupted service. Merchants can use the intelligence as part of a re-attempt strategy to avoid retrying a decline unnecessarily.

