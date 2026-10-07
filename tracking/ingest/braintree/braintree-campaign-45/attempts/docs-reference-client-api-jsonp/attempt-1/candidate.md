---
title: "Braintree Client API JSONP Reference"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-api/jsonp"
raw_files:
  - "braintree/docs/reference/client-api/jsonp-2026-09-16.md"
tags: [braintree, client-api, jsonp, http]
---

## Overview

This narrow, unversioned [[braintree]] website-reference snapshot documents a JSONP calling pattern for most Braintree Client API methods. Instead of the method's ordinary POST request, the displayed example sends an HTTP GET with `_method=POST` and a callback name; the response invokes that callback with the API's JSON.

## Key takeaways

- The page says **most**, not all, Client API methods can be accessed through JSONP. Its example uses `GET` plus the `_method=POST` query parameter rather than issuing the ordinary POST directly.
- A `callback` query parameter names the function invoked with the returned JSON. The response object also contains a `status` key corresponding to the HTTP status code that the non-JSONP request would have returned.
- The page says unsuccessful requests return an error response. It does not define the error object's fields or handling, so those details must not be inferred from this example.

## Scope and boundaries

The shown `curl` command uses placeholder endpoint and callback values and demonstrates the HTTP request shape; it is not browser-execution proof. The snapshot does not name browser requirements, an exact Braintree Web SDK or other client-SDK version, authentication, environment selection, callback-safety requirements, current endpoint availability, current JSONP support, merchant enablement, or payment success. It is website documentation for the Client API transport pattern, not package-qualified SDK behavior, server-side gateway processing, or GitHub implementation and release history.

## Detail locators

- JSONP availability qualification and POST-replacement framing: `# Accessing the Client API via JSONP`, line 16.
- Example HTTP GET with `_method=POST` and `callback=myCallbackName`: `### curl`, lines 17-20.
- Callback invocation and returned JSON: paragraph after the curl example, line 21.
- Synthetic `status` key mapped to the non-JSONP HTTP status and unsuccessful-request error response: paragraph after the curl example, lines 21-24.
- Captured page create/update metadata: frontmatter, lines 5-10.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Client API orientation: [[source-braintree-docs-reference-client-api-overview]]
- Client API request authorization: [[source-braintree-docs-reference-client-api-authorization]]

## Raw Sources

- [[raw/braintree/docs/reference/client-api/jsonp-2026-09-16|Braintree Client API JSONP reference]] - fully read pinned webpage snapshot for the JSONP GET override, callback invocation, response status mapping and unsuccessful-request behavior
