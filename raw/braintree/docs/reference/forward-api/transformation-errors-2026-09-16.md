<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/transformation-errors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transformation Errors
slug: /docs/reference/forward-api/transformation-errors/
createTime: '2025-04-02T01:46:34.331Z'
updateTime: '2025-04-02T01:46:34.497Z'
---



# Transformation Errors


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility. 

 Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Transformation errors are returned in the response body to your application. The body is a JSON structure with a format resembling this example:
### json
```json
{
    "error": "Received invalid transformation. Does not type check",
    "message": {
        "transformation_error?": true,
        "expression": ["not_a_real_function", 1],
        "type_errors": ["Function \"not_a_real_function\" does not exist"]
    },
    "request-uuid": "a-unique-identifier-for-the-request"
}
```
| Error | Explanation | Additional `message` fields |
| --- | --- | --- |
| Received invalid transformation. Does not type check | One or more[type errors](#type-errors)were found. | type_errors: An array of type errors |
| Transformations must return one of boolean, nil, number, string | All Forward API functions must return a type that can be serialized. | return_type: The type currently returned by the transformation |
| Invalid expiration year | The year argument passed to theformat_expirationfunction was a valid string but not a valid year. | expiration_year: The invalid value passed for the year |
| Invalid expiration month | The month argument passed to theformat_expirationfunction was a valid string but not a valid month (01 - 12). | expiration_month: The invalid value passed for the month |
| encodereceived an unsupported charset | The first argument (charset) was not a valid[character encoding](https://en.wikipedia.org/wiki/Character_encoding#Common_character_encodings). | charset: the provided charset |
| integerreceived a non-numeric string | The argument was a valid string but could not be parsed as an integer. | None |
| slice index range out of bounds for value length | The provided substring start and end index are out of bounds for the given string value | slice-start: given start index (inclusive)\n |

**slice-stop:** given end index (exclusive) **value-string:** given string value **value-length:** given string length


## Type errors

Before the Forward API performs a transformation, it first type checks the transformation to ensure correctness.

All type errors haveReceived invalid transformation. Does not type checkas theerrorfield. In themessagethey all include"transformation_error?": trueand the triggering transformation as theexpression, so those fields aren't listed below.

Thetype_errorsfield contains a list of errors detected by the type checker. There are three categories of type error:| Type error category | Example type error | Explanation |
| --- | --- | --- |
| Invalid arity | Function "join" expects 2 arguments but received 1 of them. | The[function](/braintree/docs/reference/forward-api/functions)was given an unexpected number of arguments. |
| Invalid argument type | "join" arg 0: expected string but received number | A[function](/braintree/docs/reference/forward-api/functions)was called with an incorrect argument type. Arguments are 0-indexed. |
| Invalid function name | Function "not_a_real_function" does not exist | A[function](/braintree/docs/reference/forward-api/functions)that doesn't exist was called. |

A transformation may return multiple type errors if multiple arguments have invalid types or if both arity and argument type(s) are invalid.