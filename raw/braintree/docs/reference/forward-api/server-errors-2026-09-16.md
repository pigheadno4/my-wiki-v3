<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/server-errors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Server Errors
slug: /docs/reference/forward-api/server-errors/
createTime: '2025-04-01T22:06:49.779Z'
updateTime: '2025-04-01T22:06:49.808Z'
---



# Server Errors

**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility.   Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 Server errors are returned when the [Forward API](/braintree/docs/reference/forward-api/overview/) is unable to complete the request. The body is a JSON structure with a format resembling the following example: 
### json
```json
{
    "error": "Connect timeout",
    "message": {
        "server_error?": true,
        "connect_timeout": 10000
    },
    "request-uuid": "a-unique-identifier-for-the-request"
}
```

| Error | Explanation | Additionalmessagefields | HTTP Status Code |
| --- | --- | --- | --- |
| Connect timeout | Time establishing a TCP connection to the destination exceeded the configured threshold | [connect_timeout](/braintree/docs/reference/forward-api/config#connect_timeout) | 504 |
| Request timeout | Elapsed time processing request exceeded the configured threshold | [request_timeout](/braintree/docs/reference/forward-api/config#request_timeout) | 504 |
| Socket timeout | Time between packets exceeded the configured threshold | [socket_timeout](/braintree/docs/reference/forward-api/config#socket_timeout) | 504 |
| TLS error | The[TLS handshake](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_handshake)with the destination API failed |  | 502 |

**NOTE**
If the destination returns a 5xx error, the [Forward API response](/braintree/docs/reference/forward-api/overview/#example) will have a status code of 200, but the response body will show the destination's response error in the status field.

