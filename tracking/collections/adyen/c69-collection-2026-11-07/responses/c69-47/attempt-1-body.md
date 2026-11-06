# POST balancePlatform.balanceAccountSweepExecution.skipped - Sweep skipped

Adyen sends this webhook when a sweep execution is skipped.

## Parameters

### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | object | Yes | Contains event details. |
|   - balanceAccountId | string | No | The unique identifier of the balance account from which the sweep is initiated. |
|   - balanceAccountSweepId | string | No | The unique identifier of the sweep configuration. |
|   - balancePlatform | string | No | The unique identifier of the balance platform. |
|   - id | string | No | The ID of the resource. |
|   - result | string | No | The outcome of the sweep execution.  Possible results:  - **succeeded**: The sweep payout was completed successfully.  - **failed**: The sweep payout was not completed due to an error.  - **skipped**: The sweep payout was not triggered as expected. |
|   - resultDetails | object | No | The details of the execution result. |
|     - reason | string | No | Human readable reason for why execution was not successful if applicable. |
|     - reasonCode | string | No | Reason Code for why execution was not successful if applicable. |
|     - sweepConfigurationDisabled | boolean | No | Is true if the sweep configuration was disabled. |
|     - transferId | string | No | The id of the transfer from executing the sweep. |
|   - triggeredAt | string | No | The timestamp of when the execution was triggered. |
| environment | string | Yes | The environment from which the webhook originated.  Possible values: **test**, **live**. |
| timestamp | string | No | When the event was queued. |
| type | string | Yes | Type of webhook. |

## Request examples

### balancePlatform-sweep-execution-skipped
```json
{
  "data": {
    "balancePlatform": "YOUR_BALANCE_PLATFORM",
    "id": "SWPE00000000000000000000000002",
    "balanceAccountId": "BA00000000000000000001",
    "balanceAccountSweepId": "SWPC4227C224555B5FTD2NT2JV4WN5",
    "result": "skipped",
    "resultDetails": {
      "reason": "No balance to pay out",
      "reasonCode": "noBalanceToPayOut"
    },
    "triggeredAt": "2026-05-11T13:02:00Z"
  },
  "environment": "test",
  "timestamp": "2026-05-11T13:02:00.982Z",
  "type": "balancePlatform.balanceAccountSweepExecution.skipped"
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| notificationResponse | string | No | Respond with any **2xx** HTTP status code to [accept the webhook](https://docs.adyen.com/development-resources/webhooks/#accept-webhooks). |
