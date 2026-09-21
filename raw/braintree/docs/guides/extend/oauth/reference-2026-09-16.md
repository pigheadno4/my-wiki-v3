<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/oauth/reference -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reference
slug: /docs/guides/extend/oauth/reference/
createTime: '2025-04-01T22:25:35.172Z'
updateTime: '2025-04-01T22:25:35.202Z'
---



# Reference

**AVAILABILITY**
OAuth is in closed beta in production, and open beta in sandbox. [Contact us](https://www.braintreepayments.com/products/braintree-auth#contact) to express interest in the production beta release.


## Resource-oriented OAuth scopes

| Scope | Description |
| --- | --- |
| Address Resource |
| address:create | [Address: Create](/braintree/docs/reference/request/address/create) |
| address:delete | [Address: Delete](/braintree/docs/reference/request/address/delete) |
| address:find | [Address: Find](/braintree/docs/reference/request/address/find) |
| address:update | [Address: Update](/braintree/docs/reference/request/address/update) |
| Apple Pay Resource |
| apple_pay:manage_web_domains | [Apple Pay: Register Domain](/braintree/docs/reference/request/apple-pay/register-domain)[Apple Pay: Registered Domains](/braintree/docs/reference/request/apple-pay/registered-domains)[Apple Pay: Unregister Domain](/braintree/docs/reference/request/apple-pay/unregister-domain) |
| Client Token Resource |
| client_token:generate | [Client Token: Generate](/braintree/docs/reference/request/client-token/generate) |
| Credit Card Verification Resource |
| credit_card_verification:search | [Credit Card Verification: Search](/braintree/docs/reference/request/credit-card-verification/search) |
| Credit Card Resource |
| credit_card:expiring_between | [Credit Card: Expiring Between](/braintree/docs/reference/request/credit-card/expiring-between) |
| Customer Resource |
| customer:create | [Customer: Create](/braintree/docs/reference/request/customer/create) |
| customer:delete | [Customer: Delete](/braintree/docs/reference/request/customer/delete) |
| customer:find | [Customer: Find](/braintree/docs/reference/request/customer/find) |
| customer:search | [Customer: Search](/braintree/docs/reference/request/customer/search) |
| customer:update | [Customer: Update](/braintree/docs/reference/request/customer/update) |
| Dispute Resource |
| dispute:accept | [Dispute: Accept](/braintree/docs/reference/request/dispute/accept) Also available asdispute:accept/facilitated, which only allows acting on the dispute if the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| dispute:add_evidence | [Dispute: Add File Evidence](/braintree/docs/reference/request/dispute/add-file-evidence)[Dispute: Add Text Evidence](/braintree/docs/reference/request/dispute/add-text-evidence) Also available asdispute:add_evidence/facilitated, which only allows acting on the dispute if the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| dispute:finalize | [Dispute: Finalize](/braintree/docs/reference/request/dispute/finalize) Also available asdispute:finalize/facilitated, which only allows acting on the dispute if the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| dispute:find | [Dispute: Find](/braintree/docs/reference/request/dispute/find) Also available asdispute:find/facilitated, which only allows find the dispute if the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| dispute:remove_evidence | [Dispute: Remove Evidence](/braintree/docs/reference/request/dispute/remove-evidence) Also available asdispute:remove_evidence/facilitated, which only allows acting on the dispute if the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| dispute:search | [](/braintree/docs/reference/request/dispute/search) Also available asdispute:search/facilitated, which only allows searching disputes where the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details). |
| Document Upload |
| document_upload:create | [Document Upload: Create](/braintree/docs/reference/request/document-upload/create) |
| Merchant Account Resource |
| merchant_account:all | [Merchant Account: All](/braintree/docs/reference/request/merchant-account/all) |
| merchant_account:find | [Merchant Account: Find](/braintree/docs/reference/request/merchant-account/find) |
| Payment Method Resource |
| payment_method:create | [Payment Method: Create](/braintree/docs/reference/request/payment-method/create) |
| payment_method:delete | [Payment Method: Delete](/braintree/docs/reference/request/payment-method/delete) |
| payment_method:find | [Payment Method: Find](/braintree/docs/reference/request/payment-method/find) |
| payment_method:update | [Payment Method: Update](/braintree/docs/reference/request/payment-method/update) |
| Payment Method Nonce Resource |
| payment_method_nonce:create | [Payment Method Nonce: Create](/braintree/docs/reference/request/payment-method-nonce/create) |
| payment_method_nonce:find | [Payment Method Nonce: Find](/braintree/docs/reference/request/payment-method-nonce/find) |
| Settlement Batch Summary Resource |
| settlement_batch_summary:generate | [Settlement Batch Summary: Generate](/braintree/docs/reference/request/settlement-batch-summary/generate) |
| Subscription Resource |
| subscription:cancel | [Subscription: Cancel](/braintree/docs/reference/request/subscription/cancel) |
| subscription:create | [Subscription: Create](/braintree/docs/reference/request/subscription/create) |
| subscription:find | [Subscription: Find](/braintree/docs/reference/request/subscription/find) |
| subscription:search | [Subscription: Search](/braintree/docs/reference/request/subscription/search) |
| subscription:update | [Subscription: Update](/braintree/docs/reference/request/subscription/update) |
| Transaction Resource |
| transaction:manage_escrow | [Transaction: Cancel Release](/braintree/docs/reference/request/transaction/cancel-release)[Transaction: Hold In Escrow](/braintree/docs/reference/request/transaction/hold-in-escrow)[Transaction: Release From Escrow](/braintree/docs/reference/request/transaction/release-from-escrow) |
| transaction:clone | [Transaction: Clone Transaction](/braintree/docs/reference/request/transaction/clone-transaction) |
| transaction:find | [Transaction: Find](/braintree/docs/reference/request/transaction/find)[Transaction Line Item: Find All](/braintree/docs/reference/request/transaction-line-item/find-all) |
| transaction:refund | [Transaction: Refund](/braintree/docs/reference/request/transaction/refund) |
| transaction:sale | [Transaction: Sale](/braintree/docs/reference/request/transaction/sale) |
| transaction:search | [Transaction: Search](/braintree/docs/reference/request/transaction/search) |
| transaction:manage_settlement | [Transaction: Submit For Partial Settlement](/braintree/docs/reference/request/transaction/submit-for-partial-settlement)[Transaction: Submit For Settlement](/braintree/docs/reference/request/transaction/submit-for-settlement) |
| transaction:void | [Transaction: Void](/braintree/docs/reference/request/transaction/void) |


## Additional OAuth scopes

| Scope | Description |
| --- | --- |
| view_facilitated_transaction_metrics | Allows grantor to view metrics on facilitated transactions |
| grant_payment_method | Allows usage of the[Grant API](/braintree/docs/reference/xml-api/grant-api/overview) |
| read_facilitated_transactions | Allows[Transaction: Search](/braintree/docs/reference/request/transaction/search)but only returns results where the connected OAuth application was a[facilitator](/braintree/docs/reference/response/transaction#facilitator_details) |
| shared_vault_transactions | Allows[Shared Vault](/braintree/docs/guides/extend/oauth/shared-vault) |

