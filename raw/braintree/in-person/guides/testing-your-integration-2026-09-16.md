<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/testing-your-integration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Testing Your Integration
slug: /in-person/guides/testing-your-integration/
createTime: '2024-11-20T19:01:54.410Z'
updateTime: '2025-01-17T05:05:41.776Z'
---



# Testing Your Integration


### Testing Best Practices

We recommend that you test your integration end to end in the sandbox environment before deploying in production. This means that you should test from the POS application UI to invoke API calls to the Braintree card reader, complete payment using test cards, check the Braintree control panel and validate the solution works end to end, including the unhappy path flows.



In order to make sure your application can handle various context status' use the amounts in the table below to simulate different scenarios in the [Braintree sandbox](https://sandbox.braintreegateway.com/login) environment.

**NOTE**
The sandbox and production environments are entirely separate. **Nothing created in the sandbox (e.g. contexts, locations, transactions) will transfer to production.** Your login information, [merchant ID](/braintree/articles/control-panel/important-gateway-credentials#merchant-id), and [API keys](/braintree/articles/control-panel/important-gateway-credentials#api-keys) will also be different. See [Try It Out](/braintree/articles/get-started/try-it-out/) for more details. The content of this page is only applicable in the sandbox environment.


### Testing with Digital Wallets

The Braintree sandbox does not allow for testing of digital wallets on the Braintree dev kit readers. The behavior of these payments methods is exactly the same as contactless cards from both an API perspective and from a UX/UI perspective.


### Transaction amounts

When working with in-store transactions in the sandbox environment, you can pass specific amounts to simulate different context status'. Transactions performed with the test amounts below will end with the corresponding [Context Status](/braintree/graphql/reference/#Enum--InStoreContextStatus) and [Payment Status](/braintree/graphql/reference/#Enum--PaymentStatus).

| **Amount** | **Context Status** | **Payment Status** |
| 0.01 - 1999.99 | COMPLETE | SUBMITTED_FOR_SETTLEMENT |
| 1004.00 | COMPLETE | SUBMITTED_FOR_SETTLEMENT |
| 2000.00 - 2999.99 | FAILED | PROCESSOR_DECLINED |
| 3000.00 - 3000.99 | FAILED | FAILED |
| 5001.00 | FAILED | GATEWAY_REJECTED |
| 5002.00 and up (except 9000.00) | COMPLETE | SUBMITTED_FOR_SETTLEMENT |
| 9000.00 (insert card to test) | FAILED | VOIDED |


### Simulating Processor Responses

Braintree will also return raw processor response codes in the API response. You may want to parse and consume these detailed [processor response](/braintree/articles/control-panel/transactions/declines/#authorization-decline-codes) codes to provide detailed reason codes to your cashier or accounting team.

**NOTE**
Click on the link above. Try passing the number listed in the "code" column as the "amount in your request. This will simulate that processor response.


### Integration Readiness Questionnaire

It is most important to test all of the the use cases relevant to your business, however, it is also critical that your integration meets the most basic requirements to function properly once you deploy to the production environment. The questions below are meant as a gut check to make sure you are meeting those requirements and using best development practices:

Have you implemented[Idempotency](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging)to your sale and refund requests?Are you specifying your[Merchant Account ID](/braintree/articles/control-panel/important-gateway-credentials/#merchant-account-id)in your sale and refund API requests?[Hint](/braintree/in-person/guides/making-a-transaction/#important-tips-for-building-out-your-charge-refund-flows)Have you built[timeout logic](/braintree/in-person/guides/making-a-transaction/#recommended-timeout-logic)based on our recommendations?Are you properly[handling errors](/braintree/in-person/guides/graphql-error-handling/)and non-happy path flows?Are you parsing out the required[EMV receipt data](/braintree/in-person/guides/making-a-transaction/#receipt-data-handling)from the API response?Is your integration[logging](/braintree/in-person/guides/graphql-error-handling/#extensions-1)the requestId and other important data elements from the API response?If you answered yes to the above questions then we suggest you schedule a demo and code review with your PayPal Solutions Engineer or Integration Engineer![Reporting and Reconciliation](/braintree/in-person/guides/reporting-and-reconciliation/)[Ready for Launch?](/braintree/in-person/guides/ready-for-launch/)