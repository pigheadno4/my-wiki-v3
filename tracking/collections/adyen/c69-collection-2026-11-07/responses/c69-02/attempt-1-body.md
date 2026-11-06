# POST /merchants/{merchantAccount}/devices/{deviceId}/sync - Send a Terminal API request and receive a synchronous response

Sends a Terminal API request and receives the response synchronously.

The request body is a JSON object containing a Terminal API request. For the structure, see the various request types under [Terminal API](https://docs.adyen.com/api-explorer/terminal-api/1/overview).

The response returns a Terminal API response. See [Receiving a synchronous result](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/#sync).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- **Cloud Device API role**

## Servers

**Test environment**
- https://device-api-test.adyen.com/v1

**Live environment for Australia**
- https://device-api-live-au.adyen.com/v1

**Live environment for East Asia**
- https://device-api-live-apse.adyen.com/v1

**Live environment for Europe**
- https://device-api-live.adyen.com/v1

**Live environment for United States of America**
- https://device-api-live-us.adyen.com/v1

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| deviceId | string | Yes | The unique identifier of the payment device that you send this request to. Must be the same as the `POIID` in the `MessageHeader` of the Terminal API request.  In an integration with payment terminals, use the terminal ID in the format *[terminal model]-[serial number]*, for example, **P400‑123456789**. In a Mobile solution, use the installation ID of the SDK. |
| merchantAccount | string | Yes | The unique identifier of the merchant account. |

## Responses

### 200 Success
The request has succeeded.
