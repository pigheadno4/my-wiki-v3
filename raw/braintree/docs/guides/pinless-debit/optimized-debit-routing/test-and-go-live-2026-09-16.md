<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Test and Go Live
slug: /docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live/
createTime: '2025-04-01T23:47:57.629Z'
updateTime: '2025-04-01T23:47:57.673Z'
---



## Test and go live


**NOTE**
PINless debit is not automatically enabled in your sandbox account. Reach out to your Technical account manager to get enabled for PINless.

We recommended testing PINless debit in the sandbox before moving to a live environment.

The following card details can be used for testing. When these cards are used, the payer is routed through one of the debit networks:


- 5208233085365191 (Mastercard)
- 4070021557035923 (Visa)

Transactions are routed to any one of the STAR, STAR_ACCESS, ACCEL, NYCE or PULSE debit networks based on the optimized debit routing. The network depends on the transaction amount sent in the transaction sale request and the merchant category code (MCC) of the merchant account.
### Auto-retry

If a transaction routed to the debit network is not successful, Braintree can retry the transaction over Visa or Mastercard networks. Reach out to your technical account manager to get enabled for auto-retries.

The debit network is empty during a **successful retry**, because the retry will be routed on Visa, Mastercard networks.

If the retry attempt proves unsuccessful as well, the initial transaction is recorded as a **failed retry** along with both the original and all subsequent retried transaction IDs.


- getRetriedTransactionId(): The transaction ID of the transaction that was retried
- getRetryIds(): An array of transaction IDs for all retry attempts for this transaction
- isRetried(): Returns true if the transaction is retried; otherwise false

**Response:**
### Java,sample
```json
if (authResult.isSuccess()) {
    Transaction transaction = authResult.getTarget();
    transaction.getId();
    transaction.isRetried();
    transaction.getStatus();
    transaction.getRetryIds();
    transaction.getRetriedTransactionId();
    // Corrected line
    // ... transaction.getDebitNetwork();
}
```

### Successful,retry
```json
"transaction": {
    "id": "5p4z558e",  // other fields...
    "retriedTransactionId": "79cv9vpc",  // this shows the parent transaction that failed initially
    "retried": true,
    "debitNetwork": null
}
```

### Failed,retry
```json
"transaction": {
    "id": "79cv9vpc",  // other fields...
    "retryIds": [
        "02scmpqn",
        "5p4z558e"
    ],
    "retried": true,
    "debitNetwork": "STAR"
}
```

### Testing auto-retry

To test a retry of a PINless debit transaction in a sandbox environment, set the transaction amount to 2046. Please note that this is a negative test-case, the transaction will be unsuccessfully routed to a debit network, and the retry will be over Visa, or Mastercard network, and this will also result in failure.

