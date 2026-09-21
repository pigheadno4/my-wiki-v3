<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/network-tokens/getting-started -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Getting Started with Network Tokens
slug: /docs/guides/network-tokens/getting-started/
createTime: '2025-04-02T00:11:37.179Z'
updateTime: '2025-04-02T00:11:37.193Z'
---



# Getting Started with Network Tokens

Network Tokens are available for merchants in the United States and select regions in North America, South America, and Europe who are processing full stack with Braintree.

To enable Network Tokens, please [contact us](/braintree/help?issue=feeHelp) to see if your merchant account is eligible. There is no integration lift or change required to start using and taking advantage of Network Tokens. Merchants tokenizing cards with another Payment Service Provider can utilize [Bring Your Own Tokens](/braintree/docs/guides/network-tokens/bring-your-own-token) to process transactions on Braintree using their existing Network Tokens

Cards stored in a merchant's Braintree vault will be enrolled as promptly as possible. Once enabled, Network Tokens will begin to be used to process transactions. As new cards are added to Vault in the future, we will attempt to enroll these cards with the card networks to generate a Network Token to be used in future transactions.

To see if a Network Token was used for a specific transaction: The 'is_network_tokenized?' field in the transaction response will indicate whether a Network Token exists for a payment method. The 'processed_with_network_token?' field will indicate whether a Network Token was used for a particular transaction.

Please note that a token may not always be used for a transaction. For more information, please visit [https://developers.braintreepayments.com/reference/general/network-tokenization/ruby](https://developers.braintreepayments.com/reference/general/network-tokenization/ruby)

Network tokens have an expiration date and can also be updated or cancelled for assorted reasons. Braintree manages this token lifecycle on the behalf of merchants and will update Network Tokens as updates become available from the card networks.

[Next Page: Bring Your Own Token](/braintree/docs/guides/network-tokens/bring-your-own-token)