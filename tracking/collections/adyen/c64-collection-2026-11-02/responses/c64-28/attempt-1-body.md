# GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions - View executions of a managed payout schedule

View information about the executions of a managed payout schedule on the specified balance account. An execution is an attempt to make a payout according to the payout schedule.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the payout schedule on the balance account. |
| balanceAccountId | string | Yes | The unique identifier of the balance account. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| offset | integer | Yes | The page number to be returned.  Default: **1** |
| limit | integer | No | The number of items returned per page.  Default: **10** |
| results | string | No | Contains a comma-separated list of payout statuses. If included, the response returns only executed payouts that currently have one of the specified statuses.  Possible statuses:  - **succeeded**: The payout was sent successfully.  - **failed**: The payout was not sent due to an error.  - **skipped**: The payout was not triggered as expected.  Examples: `results=succeeded`, `results=failed,skipped` |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| payoutScheduleExecutions | array of object | Yes | Contains a list of executions of the payout schedule. |
|   - id | string | No | The unique identifier of the payout execution. |
|   - result | string | No | The status of the payout execution.  Possible values:  - **succeeded**: The payout was sent successfully.  - **failed**: The payout could not be sent because an error occurred.  - **skipped**: The payout was not triggered as expected. |
|   - resultDetails | object | No | Contains information about the result of the payout execution. |
|     - reason | string | No | Human readable reason for why execution was not successful if applicable. |
|     - reasonCode | string | No | Reason Code for why execution was not successful if applicable. |
|     - transferId | string | No | The id of the transfer from executing the payout. |
|   - triggeredAt | string | No | The date and time when the payout execution was initiated. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 404 Client Error
The resource was not found

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |

## Response examples

### 200 Success

**list-payout-schedule-executions**
```json
{
  "payoutScheduleExecutions": [
    {
      "id": "PS0000000000001",
      "result": "skipped",
      "triggeredAt": "2026-03-11T08:00:00Z",
      "resultDetails": {
        "reasonCode": "noBalanceToPayOut",
        "reason": "No balance to pay out"
      }
    },
    {
      "id": "PS0000000000002",
      "result": "succeeded",
      "triggeredAt": "2026-03-12T08:00:00Z",
      "resultDetails": {
        "transferId": "A0A0A0A0A0A0A0A0"
      }
    }
  ]
}
```