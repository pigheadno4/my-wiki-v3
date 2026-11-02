# PATCH /sessions/{sessionId} - Update a payment session

Updates an existing payment session with the `sessionId` specified in the path.

You can update the session's `amount` and `payable` fields. The session can only be updated if it is not yet payable.

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| sessionId | string | Yes |  |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | The amount to update for the payment session. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|   - value | integer | Yes | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| payable | boolean | No | Indicates if the session is payable. If the payment amount is final, set this to **true** to indicate that the session is payable, so that the shopper can proceed to submit the payment. When you set this to **true**, you can no longer update the session.  If you set this to **false**, you must make another request to update the session and set this to **true** before the shopper can submit the payment. |
| sessionData | string | Yes | The encoded payment session data from the `beforeSubmit` callback from [Drop-in](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow?platform=Web&integration=Drop-in#update-the-session-amount) or [the Component](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow?platform=Web&integration=Components#update-the-session-amount). |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| sessionData | string | No |  |
