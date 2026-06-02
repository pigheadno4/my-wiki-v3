---
title: Test Disputes
slug: /docs/disputes/testing/
createTime: "2024-05-13T19:37:15.717Z"
updateTime: "2025-02-27T07:47:31.526Z"
---

# Test Disputes

You can run negative tests on your integration to manage the responses you give to your customers.

## Know before you code

- Before you trigger a simulation, you'll need to you need to [get an access token](https://developer.paypal.com/api/rest/authentication/) .
- Use Postman to explore and test PayPal APIs.

To trigger a simulation for the Disputes API, you can [use a path parameter in the request URI](/docs/disputes/testing/#use-a-path-parameter-in-the-request-uri) .

### Use a path parameter in the request URI

| Trigger or test value                                  | Simulated error response |
| ------------------------------------------------------ | ------------------------ |
| v1/customer/disputes?disputed_transaction_id=ERRDIS023 | FORBIDDEN                |

#### **`Request`**

```curl
curl -X GET \
  https://api-m.sandbox.paypal.com/v1/customer/disputes?disputed_transaction_id=ERRDIS023 \
  -H 'Authorization: Bearer <Access Token>' \
  -H 'Content-Type: application/json'
```

#### **`Response`**

```curl
{
    "name": "FORBIDDEN",
    "message": "No permission for the requested operation.",
    "debug_id": "e90ec082e0e4d"
}
```

## Test values

Use the following test values to trigger negative responses for these disputes actions:

- [List disputes](/docs/disputes/testing/#list-disputes)
- [Show dispute details](/docs/disputes/testing/#show-dispute-details)
- [Send message to other party](/docs/disputes/testing/#send-message-to-other-party)
- [Make offer to resolve dispute](/docs/disputes/testing/#make-offer-to-resolve-dispute)
- [Escalate dispute to claim](/docs/disputes/testing/#escalate-dispute-to-claim)
- [Provide evidence](/docs/disputes/testing/#provide-evidence)
- [Accept claim](/docs/disputes/testing/#accept-claim)
- [Acknowledge return item](/docs/disputes/testing/#acknowledge-return-item)
- [Appeal dispute](/docs/disputes/testing/#appeal-dispute)

**Note:** Test values are case sensitive.

### List disputes

#### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at GET /v1/customer/disputes?disputed_transaction_id={transaction_id} .

| Trigger or test value                                   | Simulated error response |
| ------------------------------------------------------- | ------------------------ |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS023 | FORBIDDEN                |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS024 | INVALID_RESOURCE_ID      |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS025 | NOT_ACCEPTABLE           |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS026 | UNSUPPORTED_MEDIA_TYPE   |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS027 | RATE_LIMIT_REACHED       |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS028 | SERVICE_UNAVAILABLE      |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS029 | INTERNAL_SERVICE_ERROR   |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS030 | AUTHORIZATION_ERROR      |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS031 | VALIDATION_ERROR         |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS032 | VALIDATION_ERROR         |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS033 | VALIDATION_ERROR         |
| /v1/customer/disputes?disputed_transaction_id=ERRDIS034 | VALIDATION_ERROR         |

### Show dispute details

#### Negative response test values

Use the JSON pointer method to simulate the following error responses at GET /v1/customer/disputes/{dispute_id} .

| Trigger or test value           | Simulated error response |
| ------------------------------- | ------------------------ |
| /v1/customer/disputes/ERRDIS015 | FORBIDDEN                |
| /v1/customer/disputes/ERRDIS016 | INVALID_RESOURCE_ID      |
| /v1/customer/disputes/ERRDIS017 | NOT_ACCEPTABLE           |
| /v1/customer/disputes/ERRDIS018 | UNSUPPORTED_MEDIA_TYPE   |
| /v1/customer/disputes/ERRDIS019 | RATE_LIMIT_REACHED       |
| /v1/customer/disputes/ERRDIS020 | SERVICE_UNAVAILABLE      |
| /v1/customer/disputes/ERRDIS021 | INTERNAL_SERVICE_ERROR   |
| /v1/customer/disputes/ERRDIS022 | AUTHORIZATION_ERROR      |

### Send message to other party

#### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/customer/disputes/{dispute_id}/send-message .

| Trigger or test value                        | Simulated error response |
| -------------------------------------------- | ------------------------ |
| /v1/customer/disputes/ERRDIS091/send-message | FORBIDDEN                |
| /v1/customer/disputes/ERRDIS092/send-message | INVALID_RESOURCE_ID      |
| /v1/customer/disputes/ERRDIS093/send-message | NOT_ACCEPTABLE           |
| /v1/customer/disputes/ERRDIS094/send-message | UNSUPPORTED_MEDIA_TYPE   |
| /v1/customer/disputes/ERRDIS095/send-message | RATE_LIMIT_REACHED       |
| /v1/customer/disputes/ERRDIS096/send-message | SERVICE_UNAVAILABLE      |
| /v1/customer/disputes/ERRDIS097/send-message | INTERNAL_SERVICE_ERROR   |
| /v1/customer/disputes/ERRDIS098/send-message | AUTHORIZATION_ERROR      |
| /v1/customer/disputes/ERRDIS099/send-message | UNPROCESSABLE_ENTITY     |

### Make offer to resolve dispute

#### Negative response test values

Use the path parameter in the request URI method to simulate the following response at POST /v1/customer/disputes/{dispute_id}/make-offer .

| Trigger or test value                      | Simulated error response |
| ------------------------------------------ | ------------------------ |
| /v1/customer/disputes/ERRDIS100/make-offer | FORBIDDEN                |
| /v1/customer/disputes/ERRDIS101/make-offer | INVALID_RESOURCE_ID      |
| /v1/customer/disputes/ERRDIS102/make-offer | NOT_ACCEPTABLE           |
| /v1/customer/disputes/ERRDIS103/make-offer | UNSUPPORTED_MEDIA_TYPE   |
| /v1/customer/disputes/ERRDIS104/make-offer | RATE_LIMIT_REACHED       |
| /v1/customer/disputes/ERRDIS105/make-offer | SERVICE_UNAVAILABLE      |
| /v1/customer/disputes/ERRDIS106/make-offer | INTERNAL_SERVICE_ERROR   |
| /v1/customer/disputes/ERRDIS107/make-offer | AUTHORIZATION_ERROR      |
| /v1/customer/disputes/ERRDIS108/make-offer | UNPROCESSABLE_ENTITY     |

#### Escalate dispute to claim

#### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/customer/disputes/{dispute_id}/escalate .

| Trigger or test value                    | Simulated response     |
| ---------------------------------------- | ---------------------- |
| /v1/customer/disputes/ERRDIS082/escalate | FORBIDDEN              |
| /v1/customer/disputes/ERRDIS083/escalate | INVALID_RESOURCE_ID    |
| /v1/customer/disputes/ERRDIS084/escalate | NOT_ACCEPTABLE         |
| /v1/customer/disputes/ERRDIS085/escalate | UNSUPPORTED_MEDIA_TYPE |
| /v1/customer/disputes/ERRDIS086/escalate | RATE_LIMIT_REACHED     |
| /v1/customer/disputes/ERRDIS087/escalate | SERVICE_UNAVAILABLE    |
| /v1/customer/disputes/ERRDIS088/escalate | INTERNAL_SERVICE_ERROR |
| /v1/customer/disputes/ERRDIS089/escalate | AUTHORIZATION_ERROR    |
| /v1/customer/disputes/ERRDIS090/escalate | UNPROCESSABLE_ENTITY   |

### Provide evidence

#### Negative response test values

Use the path parameter in the request URI method to simulate the following error responses at POST /v1/customer/disputes/{dispute_id}/provide-evidence .

| Trigger or test value                            | Simulated response     |
| ------------------------------------------------ | ---------------------- |
| /v1/customer/disputes/ERRDIS035/provide-evidence | FORBIDDEN              |
| /v1/customer/disputes/ERRDIS036/provide-evidence | INVALID_RESOURCE_ID    |
| /v1/customer/disputes/ERRDIS037/provide-evidence | NOT_ACCEPTABLE         |
| /v1/customer/disputes/ERRDIS038/provide-evidence | UNSUPPORTED_MEDIA_TYPE |
| /v1/customer/disputes/ERRDIS039/provide-evidence | RATE_LIMIT_REACHED     |
| /v1/customer/disputes/ERRDIS040/provide-evidence | SERVICE_UNAVAILABLE    |
| /v1/customer/disputes/ERRDIS041/provide-evidence | INTERNAL_SERVICE_ERROR |
| /v1/customer/disputes/ERRDIS042/provide-evidence | AUTHORIZATION_ERROR    |
| /v1/customer/disputes/ERRDIS043/provide-evidence | UNPROCESSABLE_ENTITY   |
| /v1/customer/disputes/ERRDIS044/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS045/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS046/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS047/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS048/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS049/provide-evidence | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS050/provide-evidence | VALIDATION_ERROR       |

### Accept claim

#### Negative response test values

Use the path parameter in the request URI method to simulate the following response at POST /v1/customer/disputes/{dispute_id}/accept-claim .

| Trigger or test value                        | Simulated response     |
| -------------------------------------------- | ---------------------- |
| /v1/customer/disputes/ERRDIS051/accept-claim | FORBIDDEN              |
| /v1/customer/disputes/ERRDIS052/accept-claim | INVALID_RESOURCE_ID    |
| /v1/customer/disputes/ERRDIS053/accept-claim | NOT_ACCEPTABLE         |
| /v1/customer/disputes/ERRDIS054/accept-claim | UNSUPPORTED_MEDIA_TYPE |
| /v1/customer/disputes/ERRDIS055/accept-claim | RATE_LIMIT_REACHED     |
| /v1/customer/disputes/ERRDIS056/accept-claim | SERVICE_UNAVAILABLE    |
| /v1/customer/disputes/ERRDIS057/accept-claim | INTERNAL_SERVICE_ERROR |
| /v1/customer/disputes/ERRDIS058/accept-claim | AUTHORIZATION_ERROR    |
| /v1/customer/disputes/ERRDIS059/accept-claim | UNPROCESSABLE_ENTITY   |
| /v1/customer/disputes/ERRDIS060/accept-claim | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS061/accept-claim | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS062/accept-claim | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS063/accept-claim | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS064/accept-claim | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS065/accept-claim | UNPROCESSABLE_ENTITY   |

### Acknowledge return item

#### Negative response test values

Use the path parameter in the request URI method to simulate the following response at POST /v1/customer/disputes/{dispute_id}/acknowledge-return-item .

| Trigger or test value                                   | Simulated response     |
| ------------------------------------------------------- | ---------------------- |
| /v1/customer/disputes/ERRDIS109/acknowledge-return-item | FORBIDDEN              |
| /v1/customer/disputes/ERRDIS110/acknowledge-return-item | INVALID_RESOURCE_ID    |
| /v1/customer/disputes/ERRDIS111/acknowledge-return-item | NOT_ACCEPTABLE         |
| /v1/customer/disputes/ERRDIS112/acknowledge-return-item | UNSUPPORTED_MEDIA_TYPE |
| /v1/customer/disputes/ERRDIS113/acknowledge-return-item | RATE_LIMIT_REACHED     |
| /v1/customer/disputes/ERRDIS114/acknowledge-return-item | SERVICE_UNAVAILABLE    |
| /v1/customer/disputes/ERRDIS115/acknowledge-return-item | INTERNAL_SERVICE_ERROR |
| /v1/customer/disputes/ERRDIS116/acknowledge-return-item | AUTHORIZATION_ERROR    |
| /v1/customer/disputes/ERRDIS117/acknowledge-return-item | UNPROCESSABLE_ENTITY   |

### Appeal dispute

#### Negative response test values

Use the path parameter in the request URI method to simulate the following response at POST /v1/customer/disputes/{dispute_id}/appeal .

| Trigger or test value                  | Simulated response     |
| -------------------------------------- | ---------------------- |
| /v1/customer/disputes/ERRDIS066/appeal | FORBIDDEN              |
| /v1/customer/disputes/ERRDIS067/appeal | INVALID_RESOURCE_ID    |
| /v1/customer/disputes/ERRDIS068/appeal | NOT_ACCEPTABLE         |
| /v1/customer/disputes/ERRDIS069/appeal | UNSUPPORTED_MEDIA_TYPE |
| /v1/customer/disputes/ERRDIS070/appeal | RATE_LIMIT_REACHED     |
| /v1/customer/disputes/ERRDIS071/appeal | SERVICE_UNAVAILABLE    |
| /v1/customer/disputes/ERRDIS072/appeal | INTERNAL_SERVICE_ERROR |
| /v1/customer/disputes/ERRDIS073/appeal | AUTHORIZATION_ERROR    |
| /v1/customer/disputes/ERRDIS074/appeal | UNPROCESSABLE_ENTITY   |
| /v1/customer/disputes/ERRDIS075/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS076/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS077/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS078/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS079/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS080/appeal | VALIDATION_ERROR       |
| /v1/customer/disputes/ERRDIS081/appeal | VALIDATION_ERROR       |
