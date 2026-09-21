<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/validation-errors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Validation Errors
slug: /docs/reference/forward-api/validation-errors/
createTime: '2025-04-01T22:15:29.927Z'
updateTime: '2026-02-25T09:00:17.540Z'
---



# Validation Errors


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility. 

 Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Validation errors are returned in the response body to your application. The body is a JSON structure with a format resembling this example:
### json
```json
{
  "error": "Unknown HTTP Method",
  "message": {
    "validation_error?": true,
    "method": "An-Erroneously-Misnamed-HTTP-Method"
  },
  "request-uuid": "a-unique-identifier-for-the-request"
}
```
All validation errors include"validation_error?": trueas part of themessage, so it isn't listed below| Error | Explanation | Additionalmessagefields |
| --- | --- | --- |
| Config 'methods' must be an array | The[methods](/braintree/docs/reference/forward-api/config#methods)parameter is required to be an array of supported HTTP methods. |  |
| Config must specify a valid URL regex | The[URL specified](/braintree/docs/reference/forward-api/config#url)in the configuration is not a valid regular expression. |  |
| Inline client certificates are not allowed in production | The[client_cert](/braintree/docs/reference/forward-api/forward#client_cert)parameter is sandbox-only. |  |
| Inline configurations are not allowed in production | The[config](/braintree/docs/reference/forward-api/forward#config)parameter isn't allowed in production. All configs must be submitted and approved. |  |
| Invalid client certificate | The[client_cert](/braintree/docs/reference/forward-api/forward#client_cert)parameter is not a valid[X.509 certificate](https://en.wikipedia.org/wiki/X.509#Certificates). |  |
| Invalid client key | The[client_key](/braintree/docs/reference/forward-api/forward#client_key)parameter is not a valid PEM-encoded[PKCS 8](https://en.wikipedia.org/wiki/PKCS_8)private key. |  |
| Invalid conditional predicates | One or more of the[conditional transformations](/braintree/docs/guides/extend/forward-api/examples#conditional-transformations)has an invalid[if_defined](/braintree/docs/reference/forward-api/config#transformations.if_defined)condition. | predicates: The invalid conditions. |
| Invalid HTTP headers, multiple values were provided for the same key | Providing multiple values for a HTTP header should instead use a single key with a comma-separated list of values and HTTP header names are case-insensitive, per[RFC 2616 4.2](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2). | headers: The full set of headers. |
| Invalid HTTP headers, must provide map | The[header](/braintree/docs/reference/forward-api/config#template.header)parameter must be a JSON object. |  |
| Invalid HTTP headers, headers cannot contain newlines or carriage returns | Keys and values in header object cannot contain newlines or carriage returns |  |
| Invalid request_format | The supported[request_format](/braintree/docs/reference/forward-api/config#request_format)s are "json", "urlencode", and "xml" | request_format: The invalid request_formats. |
| JSON Schema validation error | The request did not pass our[JSON Schema](http://json-schema.org/)validations.[See the schema here.](https://forwarding.sandbox.braintreegateway.com/schema.json) | detail: A description of the error.pointer: A[JSON Pointer](https://tools.ietf.org/html/rfc6901)to the errant data. |
| Missing required client cert parameter. client_cert and client_key are required. | It is necessary to specify both of the[client_cert](/braintree/docs/reference/forward-api/forward#client_cert)and[client_key](/braintree/docs/reference/forward-api/forward#client_key)parameters for TLS mutual auth. |  |
| No config specified | Request JSON lacks either a[config](/braintree/docs/reference/forward-api/forward#config)parameter (in Sandbox) or a config[name](/braintree/docs/reference/forward-api/forward#name)parameter. |  |
| No config specified for payment type | The[config](/braintree/docs/reference/forward-api/config)does not include the specified payment method type. | vault_type: Type of payment methodsupported_by_config: Types supported by the config. |
| No url specified | Neither the[url](/braintree/docs/reference/forward-api/forward#url)parameter nor the[urls](/braintree/docs/reference/forward-api/forward#urls)parameter are included. |  |
| No valid request_format specified | The[request_format](/braintree/docs/reference/forward-api/config#request_format)parameter isn't included. |  |
| Request URL does not match config URL regex | The[URL](/braintree/docs/reference/forward-api/forward#url)or[URLs](/braintree/docs/reference/forward-api/forward#urls)parameter provided does not match the validating regex set in the[config](/braintree/docs/reference/forward-api/config). |  |
| Request format must be JSON | The request isn't syntactically valid JSON. |  |
| Request method not allowed by config | The HTTP[method](/braintree/docs/reference/forward-api/forward#method)parameter isn't included in the config's[methods](/braintree/docs/reference/forward-api/config#methods)array. |  |
| Request must be a JSON dictionary | The request was not a valid JSON object. |  |
| Unknown HTTP Method | The HTTP[method](/braintree/docs/reference/forward-api/forward#method)parameter is not one ofGET,POST,HEAD,PUT, orPATCH. | method: The submitted HTTP method. |
| Unknown host | DNS lookup failed for the URL. | url: the URL of the attempted destination. |
| URL is invalid or resolves to private IP | Requests to a[private network](https://en.wikipedia.org/wiki/Private_network)are unsupported. | url: The URL of the attempted destination. |
| URL is malformed | The[url](/braintree/docs/reference/forward-api/forward#url)parameter was not a valid[URL](https://en.wikipedia.org/wiki/URL). | url: The URL of the attempted destination. |
| URL protocol must be http or https | The[url](/braintree/docs/reference/forward-api/forward#url)parameter's protocol must either be HTTP or HTTPS. | url: The URL of the attempted destination. |
| debug_transformations is not allowed in production | The[debug_transformations](/braintree/docs/reference/forward-api/forward#debug_transformations)parameter isn't allowed in production since it might otherwise return PCI sensitive data. |  |
| merchant_id is required | The[merchant_id](/braintree/docs/reference/forward-api/forward#merchant_id)parameter isn't included in the request. |  |
| override must be an object literal if provided | The[override](/braintree/docs/reference/forward-api/forward#override)parameter must be a JSON object. |  |
| payment_method_nonce or payment_method_token(s) is required | At least one of the[payment_method_nonce](/braintree/docs/reference/forward-api/forward#payment_method_nonce),[payment_method_token](/braintree/docs/reference/forward-api/forward#payment_method_token), and[payment_method_tokens](/braintree/docs/reference/forward-api/forward#payment_method_tokens)parameters must be included in the request. |  |
| request_format does not match override | The[override](/braintree/docs/reference/forward-api/forward#override)parameter could not be parsed in accordance with the[request_format](/braintree/docs/reference/forward-api/config#request_format). | content: the text that caused a parsing error.request_format: the format unsuccessfully attempted for decoding of the content. |
| request override contained invalid keys | The[override](/braintree/docs/reference/forward-api/forward#override)parameter contained top-level keys other thanbody,header, andurlparam. |  |
| Email address/phone number is missing | Email address or phone number is required for network tokenization of AMEX cards. Retry after updating the email/phone number in customer vault. |  |
| Unsupported payment method for this product offering | The endpoint supports only PayPalBillingAgreement and VenmoAccount. Retry after updating payment method. |  |

