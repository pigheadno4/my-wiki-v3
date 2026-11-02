# DELETE /storedPaymentMethods/{storedPaymentMethodId} - Delete a token for stored payment details

Deletes the token identified in the path. The token can no longer be used with payment requests.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- API tokenise payment details

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| storedPaymentMethodId | string | Yes | The unique identifier of the token. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantAccount | string | Yes | Your merchant account. |
| shopperReference | string | Yes | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.  Your reference must not include personally identifiable information (PII), for example name or email address. |

## Responses

### 204 Success
Look at the actual response code for the status of the request.
