<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/payment-failures -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling payment failures with PayPal

Detect and respond to payment failures using PayPal's Orders v2 API and Subscriptions API. This guide explains common failure reasons, how to surface errors to buyers, best practices for retrying or recovering failed payments, and how to leverage PayPal's intelligent retry mechanism.

## Key concepts

- Payment failures can happen for many reasons, such as declined cards, expired payment methods, insufficient funds, risk restrictions, or business validation errors.
- PayPal's APIs (Orders v2 and Subscriptions) return clear error codes and messages in their responses.
- Proper handling improves user experience, reduces lost sales, and ensures smooth subscription renewals.
- Some payment failures are asynchronous, meaning they might not be immediately apparent during the initial transaction.

## Common payment failure scenarios

Here are some of the most frequent failure reasons and how to handle them:

| Error Code / Issue                         | What It Means                                                                           | What To Do                                                                                                                  |
| :----------------------------------------- | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| `INSTRUMENT_DECLINED`                      | Payment method was declined.                                                            | Prompt the buyer to select a different payment method. Restart the payment flow using `actions.restart()`.                  |
| `CARD_EXPIRED`                             | Card is expired.                                                                        | Inform the buyer and ask for a new card.                                                                                    |
| `AMOUNT_MISMATCH`, `ITEM_TOTAL_MISMATCH`   | Totals do not add up.                                                                   | Fix item or amount totals in your API request and retry.                                                                    |
| `CURRENCY_NOT_SUPPORTED`                   | Unsupported currency.                                                                   | Use a supported currency or update your PayPal account settings.                                                            |
| `ORDER_NOT_APPROVED`                       | Buyer did not approve the order.                                                        | Redirect the buyer to approve the order again.                                                                              |
| `MAX_NUMBER_OF_PAYMENT_ATTEMPTS_EXCEEDED`  | Too many failed attempts.                                                               | Ask the buyer to use a different payment method or contact PayPal support.                                                  |
| `REDIRECT_PAYER_FOR_ALTERNATE_FUNDING`     | Funding source failed, alternate source needed.                                         | Prompt the buyer to choose a different payment method.                                                                      |
| `VALIDATION_ERROR`, `UNPROCESSABLE_ENTITY` | Invalid or missing data.                                                                | Show a clear error, ask the buyer to correct the information, and retry.                                                    |
| `PAYMENT_DENIED`                           | The payment was denied by PayPal.                                                       | Investigate the reason for denial and contact PayPal support if needed. Prompt the buyer to use a different payment method. |
| `PAYER_CANNOT_PAY`                         | The payer is unable to pay using the selected payment method.                           | Prompt the buyer to select a different payment method or contact PayPal support.                                            |
| `CANNOT_BILL_PAST_DUE_BALANCE`             | The subscription is suspended because the past due balance exceeds the maximum allowed. | Contact PayPal support to resolve the suspension or prompt the buyer to pay the outstanding balance.                        |
| `REJECTED_DUE_TO_RISK_REVERSAL`            | The payment was rejected due to a risk reversal, such as a chargeback or dispute.       | Investigate the reason for the reversal and contact PayPal support if needed.                                               |
| `TRANSACTION_REFUSED`                      | The transaction was refused by the processor.                                           | Prompt the buyer to use a different payment method or contact their bank.                                                   |
| `INVALID_ACCOUNT_STATUS`                   | The payer's account is in an invalid state, such as locked or inactive.                 | Prompt the buyer to contact PayPal support to resolve their account issue.                                                  |
| `INVALID_REQUEST`                          | The request was malformed or missing required parameters.                               | Review the request parameters and ensure they are valid.                                                                    |
| `AUTHENTICATION_FAILURE`                   | Authentication failed due to invalid credentials.                                       | Verify your API credentials and ensure they are correct.                                                                    |
| `NOT_AUTHORIZED`                           | You are not authorized to perform this action.                                          | Check your account permissions and ensure you have the necessary privileges.                                                |
| `RESOURCE_NOT_FOUND`                       | The requested resource was not found.                                                   | Verify the resource ID and ensure it exists.                                                                                |
| `UNPROCESSABLE_ENTITY`                     | The request was well-formed but could not be processed due to semantic errors.          | Review the request data and ensure it is valid and consistent.                                                              |

See the [Orders v2 API Troubleshooting Guide](https://developer.paypal.com/api/rest/integration/orders-api/troubleshooting/) and the [Subscriptions API documentation](https://developer.paypal.com/docs/subscriptions/) for a more comprehensive list of error codes.

## Detect and handle payment failures

### 1. Check API responses

- Always inspect responses from the Orders API (create, authorize, or capture endpoints) or the Subscriptions API (create, update, or activate subscription endpoints).
- If the response contains an error code, use it to determine the next step.

**Example: Handling a Declined Payment in JavaScript (Orders API)**

<Tabs>
  <Tab title="Vanilla JS">
    ```javascript theme={null}
    paypal.Buttons({
      onApprove: (data, actions) => {
        return actions.order.capture().then(details => {
          // Payment successful
        }).catch(err => {
          // Handle payment failure
          if (err.name === "INSTRUMENT_DECLINED") {
            // Restart the payment flow to let buyer choose another method
            return actions.restart();
          } else {
            // Show a generic error message
            alert("Payment could not be completed. Please try again.");
          }
        });
      }
    }).render('#paypal-button-container');
    ```
  </Tab>

  <Tab title="React (JS)">
    ```javascript theme={null}
    import React, { useEffect } from 'react';

    function PayPalButton() {
      useEffect(() => {
        paypal.Buttons({
          onApprove: (data, actions) => {
            return actions.order.capture().then(details => {
              // Payment successful
            }).catch(err => {
              // Handle payment failure
              if (err.name === "INSTRUMENT_DECLINED") {
                // Restart the payment flow to let buyer choose another method
                return actions.restart();
              } else {
                // Show a generic error message
                alert("Payment could not be completed. Please try again.");
              }
            });
          }
        }).render('#paypal-button-container');
      }, []);

      return <div id="paypal-button-container"></div>;
    }

    export default PayPalButton;
    ```

  </Tab>

  <Tab title="React (TS)">
    ```typescript theme={null}
    import React, { useEffect } from 'react';

    function PayPalButton() {
      useEffect(() => {
        (window as any).paypal.Buttons({
          onApprove: (data: any, actions: any) => {
            return actions.order.capture().then((details: any) => {
              // Payment successful
            }).catch((err: any) => {
              // Handle payment failure
              if (err.name === "INSTRUMENT_DECLINED") {
                // Restart the payment flow to let buyer choose another method
                return actions.restart();
              } else {
                // Show a generic error message
                alert("Payment could not be completed. Please try again.");
              }
            });
          }
        }).render('#paypal-button-container');
      }, []);

      return <div id="paypal-button-container"></div>;
    }

    export default PayPalButton;
    ```

  </Tab>

  <Tab title="ES Module">
    ```javascript theme={null}
    paypal.Buttons({
      onApprove: (data, actions) => {
        return actions.order.capture().then(details => {
          // Payment successful
        }).catch(err => {
          // Handle payment failure
          if (err.name === "INSTRUMENT_DECLINED") {
            // Restart the payment flow to let buyer choose another method
            return actions.restart();
          } else {
            // Show a generic error message
            alert("Payment could not be completed. Please try again.");
          }
        });
      }
    }).render('#paypal-button-container');
    ```
  </Tab>
</Tabs>

- `actions.restart()` restarts the payment flow so the buyer can select a different funding source.

### 2. Surface errors to buyers

- Show clear, actionable error messages, such as “Your card was declined. Please try another payment method.”
- For validation or data errors, prompt the buyer to correct the issue and retry.

### 3. Retry or recover

- For funding failures, prompt the buyer to choose another payment method.
- For expired cards or exceeded attempts, ask the buyer to update their information or use a new card.
- For business validation errors, correct the data and resend the request.

## Intelligent retries for subscriptions

PayPal's **intelligent retry** mechanism automatically attempts to recover failed subscription payments.

- When a subscription payment fails, PayPal uses a proprietary algorithm to determine the best time to retry the payment.
- This algorithm considers factors such as the buyer's payment history, risk signals, and bank availability.
- Merchants can configure retry schedules and monitor retry attempts in the PayPal dashboard.
- Intelligent retries can significantly increase subscription renewal rates without requiring any action from the merchant.

## Asynchronous payment processing and webhooks

- Some payment failures are **asynchronous** and might not be immediately reflected in the API response.
- For example, a buyer's bank might initially authorize a payment but later decline it due to fraud concerns.
- To track these asynchronous failures reliably, it's highly recommended to use PayPal Webhooks.

### Relevant webhook events

- **Orders API**
  - `PAYMENT.CAPTURE.COMPLETED`: Indicates a successful payment capture.
  - `PAYMENT.CAPTURE.DENIED`: Indicates a failed payment capture.

- **Subscriptions API**
  - `BILLING.SUBSCRIPTION.PAYMENT.FAILED`: Indicates a failed subscription payment.
  - `BILLING.SUBSCRIPTION.PAYMENT.SUCCEEDED`: Indicates a successful subscription payment.

- Configure your webhook listener to receive these events and take appropriate action (e.g., notify the buyer, update your database).

## Manual retries for subscriptions

In addition to intelligent retries, you can also manually retry failed subscription payments.

- **PayPal Dashboard:** You can retry payments directly from the [PayPal dashboard](https://www.paypal.com/businessmanage/subscriptions).
- **Subscriptions API:** You can use the Subscriptions API to trigger a manual retry.

## Monitor and log failures

- Log all failed payment attempts with error codes and messages for troubleshooting.
- Use PayPal Webhooks to track asynchronous failures and notify your team or the buyer when needed.

## Best practices

- Promptly inform buyers of the failure reason and guide them to resolve it.
- Restart the payment flow for funding source errors using `actions.restart()` in the Smart Buttons integration (for Orders API).
- Validate all order data before sending requests to avoid preventable errors.
- Monitor webhook events for real-time updates on payment status for both Orders and Subscriptions.
- Leverage intelligent retries for Subscriptions to automatically recover failed payments.
- Consider manual retries for Subscriptions if intelligent retries are unsuccessful.
- Test payment failure scenarios during integration to ensure your system handles them correctly.

## Troubleshooting

- **Check the PayPal status page:** Verify that PayPal services are operating normally.
- **Review your API logs:** Look for any errors or warnings in your API requests and responses.
- **Use the PayPal Developer Dashboard:** Monitor your webhook events and API usage.
- **Contact PayPal support:** If you're unable to resolve the issue, contact PayPal support for assistance.

With these steps, you can handle payment failures smoothly, helping buyers complete their purchase, ensuring smooth subscription renewals, and reducing lost sales.

## See also

- [Orders v2 API Reference](/reference/api/rest/orders/create-order)
- [Orders v2 integration documentation](https://developer.paypal.com/api/rest/integration/orders-api/)
- [Common errors for the Orders v2 API](https://developer.paypal.com/api/rest/integration/orders-api/errors/)
- [Troubleshooting errors for the Orders v2 API](https://developer.paypal.com/api/rest/integration/orders-api/troubleshooting/)
- [Handle funding failures for direct merchants](https://developer.paypal.com/docs/checkout/standard/customize/handle-funding-failures/)
- [Handle funding failures for partners](https://developer.paypal.com/docs/multiparty/checkout/standard/customize/handle-funding-failures/)
- [Subscriptions API Reference](https://developer.paypal.com/docs/api/subscriptions/v1/)
- [Subscriptions integration documentation](https://developer.paypal.com/docs/subscriptions/)
- [Subscription payment failures and recovering balances](https://developer.paypal.com/docs/subscriptions/customize/payment-failure-retry/)
