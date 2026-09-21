<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/processor-responses/avs-cvv-responses -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: AVS and CVV Response Codes
slug: /docs/reference/general/processor-responses/avs-cvv-responses/
createTime: '2025-04-01T23:34:33.504Z'
updateTime: '2025-04-01T23:34:33.525Z'
---



# AVS and CVV Response Codes

Available on theandresponse objects.
## AVS

| Response | Description |
| --- | --- |
| Postal Code matches (M) | The postal code provided matches the information on file with the cardholder's bank. |
| Postal Code does not match (N) | The postal code provided does not match the information on file with the cardholder's bank. |
| Postal Code not verified (U) | The card-issuing bank received the postal code but did not verify whether it was correct. This typically happens if the processor declines an authorization before the bank evaluates the postal code. |
| Postal Code not provided (I) | No postal code was provided. |
| Street Address matches (M) | The street address provided matches the information on file with the cardholder's bank. |
| Street Address does not match (N) | The street address provided does not match the information on file with the cardholder's bank. |
| Street Address not verified (U) | The card-issuing bank received the street address but did not verify whether it was correct. This typically happens if the processor declines an authorization before the bank evaluates the address. |
| Street Address not provided (I) | No street address was provided. |
| Issuing bank does not support AVS (S) | AVS information was provided but the card-issuing bank does not participate in address verification. This typically indicates a card-issuing bank outside of the US, Canada, and the UK. |
| AVS system error (E) | A system error prevented any verification of street address or postal code. |
| AVS not applicable (A) | AVS information was provided but this type of transaction does not support address verification. |
| AVS skipped (B) | AVS checks were skipped for this transaction. |


## CVV

| Response | Description |
| --- | --- |
| CVV matches (M) | The CVV provided matches the information on file with the cardholder's bank. |
| CVV does not match (N) | The CVV provided does not match the information on file with the cardholder's bank. |
| CVV is not verified (U) | The card-issuing bank received the CVV, but did not verify whether it was correct. This typically happens if the bank declines an authorization before evaluating the CVV. |
| CVV not provided (I) | No CVV was provided. This also happens if the transaction was made with a vaulted payment method.[Learn more about AVS and CVV rules in the Vault.](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules#avs-and-cvv-rules-in-the-vault) |
| Issuer does not participate (S) | The CVV was provided but the card-issuing bank does not participate in card verification. |
| CVV not applicable (A) | The CVV was provided but this type of transaction does not support card verification. |
| CVV skipped (B) | CVV checks were skipped for this transaction. |

