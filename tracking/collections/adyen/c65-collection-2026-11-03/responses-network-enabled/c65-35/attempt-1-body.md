# POST /legalEntities/{id}/requestPeriodicReview - Request periodic data review.

Requests a periodic data review for the legal entity of the user specified in the path.

## Servers
- https://kyc-test.adyen.com/lem/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the legal entity. |

## Responses

### 204 Success
The request has been successfully processed, but there is no additional content.
