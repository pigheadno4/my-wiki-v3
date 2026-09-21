<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/extend/forward-api/transformations -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Transformations
slug: /docs/guides/extend/forward-api/transformations/
createTime: '2025-04-02T00:36:07.813Z'
updateTime: '2025-04-02T00:36:07.868Z'
---



# Transformations

**AVAILABILITY**
 **Use of the production**  [**Forward API**](/braintree/docs/reference/forward-api/overview/) **is subject to eligibility.**   Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact).

 Configs include a [transformations](/braintree/docs/reference/forward-api/config/#transformations) key which specifies where payment method data should be included in outbound forwarding requests. Transformations are applied in the order they appear and may take advantage of a small domain-specific language (DSL) to programmatically modify request contents. For example, you could concatenate a PAN and CVV then base64 encode it before inserting it into the outbound request: 
### JSON
```json
{
    "path": "/body/number",
    "value": ["base64", ["join", ":", ["array", "$number", "$cvv"]]]
}
```
 This might look like base64(join(":", [number, cvv])) in another programming language.


## Path

A path is used in a transformation to specify the destination of a transform. For example, if applying a transform to the Authorization header, the path would be /header/Authorization.     There are four valid base paths: "/body", "/header", "/urlparam", and "/var".     The first three base paths are used to construct the request (body, headers, and query string) to the destination. The "/var" base path is a variable register you can use to temporarily store the result of a transformation for further use. They are commonly used with [cryptographic functions](/braintree/docs/guides/extend/forward-api/cryptography).     Nested paths are content–type aware - the transformation {"path": "/body/parent/child", "value": 1} would result in one of the following, dependent on the [request_format](/braintree/docs/reference/forward-api/config#request_format) :      
### JSON
```json
{
    "parent": {
        "child": 1
    }
}
```
  
### XML
```xml
<code>
    <parent>
        <child>1</child>
    </parent>
</code>
```
  
### urlencode
```html
parent=child%3D1
```
 Hierarchical data is undefined in URL encoding (which only supports key/value pairs). The transformation for the PHP-style "parent[child]=1" is {"path": "/body/parent[child]", "value": 1}.


### Numerical indices

Numerical indices in paths are 0-based and used to reference [XML siblings](/braintree/docs/guides/extend/forward-api/examples#xml-sibling-elements-sharing-a-name) or elements of a JSON array.     These transformations: 
### JSON
```json
[
    {
        "path": "/body/parent/[0]/child",
        "value": "first"
    },
    {
        "path": "/body/parent/[1]/child",
        "value": "second"
    }
]
```
 would result in the following XML: 
### XML
```xml
<code>
    <parent>
        <child>first</child>
        <child>second</child>
    </parent>
</code>
```
 or JSON: 
### JSON
```json
{
    "parent": [
        { "child": "first" },
        { "child": "second" }
    ]
}
```
 The index value -1 causes the transformation to append to the array or set of siblings, primarily useful for [forwarding a variable number of payment methods](/braintree/docs/guides/extend/forward-api/examples#forwarding-multiple-payment-methods).


## Functions

Here is an example of a transformation which builds an authorization header based on a username and password passed in on the request: 
### JSON
```json
{
    "path": "/header/Authorization",
    "value": [
        "join",
        "",
        [
            "array",
            "Basic ",
            ["base64", ["join", ":", ["array", "$user", "$password"]]]
        ]
    ]
}
```
 This might look like "Basic " + base64(join(":", [user, password])) in another programming language.     In the DSL everything may be evaluated. JSON primitives (numbers, null, true, false, and most strings) return themselves. Arrays represent a function. The first array item is called as the name of the function, and the rest of the items are passed as arguments.     So, ["func", "arg0", "arg1"] in the DSL might look like func(arg0, arg1) in many programming languages.     The DSL is strict, and all arguments are evaluated before the function is called.     Since arrays are used to represent functions, to create an array within the DSL the [array](/braintree/docs/reference/forward-api/functions#array) function is used.     Each function accepts and returns specific types, as documented in the [functions](/braintree/docs/reference/forward-api/functions) reference.


## Types

While most strings return themselves, strings beginning with "$" are handled specially. They reference, and when evaluated return, variables and parts of the outbound forwarding request. They're described in more detail in the [variables](/braintree/docs/reference/forward-api/variables) reference.     The outermost function in a transformation must return either a boolean, a number, null, or a string. The exception is transformations which write to a local variable (as explained in the [variables](/braintree/docs/reference/forward-api/variables) reference), for which any return type is allowed.



[Next Page:Tokenization Support→](/braintree/docs/guides/extend/forward-api/tokenization-support)

