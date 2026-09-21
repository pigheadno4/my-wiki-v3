<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/integration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Integration
slug: /docs/guides/pinless-debit/optimized-debit-routing/integration/
createTime: '2025-04-02T01:21:10.792Z'
updateTime: '2026-02-25T13:13:59.967Z'
---



## Integration


**NOTE**
For managing your authorization workflow for transactions routed on debit networks, see [here](/braintree/docs/guides/pinless-debit/optimized-debit-routing/managing-authorization) 

Enabling PINless debit doesn't require any modifications to your integration. Contact PayPal to enable PINless debit routing for your integration.

Merchants can identify which debit network was used for transactions in their merchant report. If the merchant wants to know which low-cost debit network was used for a transaction without waiting for a report, update their integration to the following version.

SDK Availability:| SDK | Version |
| --- | --- |
| GraphQL | Always the latest version |
| Java | &gt;=3.32.0 |
| Ruby | &gt;=4.18.0 |
| Node.js | &gt;=3.21.0 |
| PHP | &gt;=6.17.0 |
| .NET | &gt;=5.24.0 |
| Python | &gt;=4.26.0 |


### Network Transaction Identifier

The **Network Transaction Identifier (NTI)** is a unique value returned by signature card brand networks in an authorization response. It is used to improve authorization approval rates for subsequent stored credential (Credential on File – CoF) transactions.   Not all networks participate equally in this framework. At this moment, PINless debit networks do not support the CoF framework and therefore do not issue NTIs.

As a result:
- When a transaction is routed over a signature network, a network-generated NTI is returned.
- When routed over a PINless debit network, the NTI field in the authorization response may not always be populated with a network-generated value, even if the authorization is successful.

This behavior is expected and dependent on the network.


## Authorization response behavior


#### PINless debit network transactions


- Braintree returns an NTI value authorization response for PINless Debit transactions.
- Behavior is consistent with existing signature processing flows.


**NOTE**
NTI return behavior is subject to network-specific processing rules and Credential on File (CoF) participation requirements.


### Integration Impact


- **Merchants vaulting with Braintree:**
No integration changes are required.

- **Merchants integrated through a third-party vault or payment orchestration provider:**
The Optimized Debit Routing (ODR) engine returns an NTI in the authorization response, where applicable, in accordance with network CoF mandates. Merchants using an external vault must pass the NTI from the original CIT transaction in the[:previous_network_transaction_id:](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#external_vault-previous_network_transaction_id)to link subsequent recurring transactions.
For fetching the routed debit network of a transaction or to search transactions by debit network, refer the code samples[here](/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/ruby)