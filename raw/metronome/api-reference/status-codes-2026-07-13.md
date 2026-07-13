<!-- Source URL: https://docs.metronome.com/api-reference/status-codes.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API status codes

This page describes how Metronome uses HTTP status codes to indicate whether an API request succeeded or failed. It helps you interpret and handle different types of errors.

Metronome uses standard HTTP status codes:

* **2xx** indicates success
* **4xx** indicates a client error (e.g., a required parameter was omitted)
* **5xx** indicates a Metronome server error

Every `4XX` error uses this `application/json` format:

```json theme={null}
{
  "message": "Descriptive error text"
}

```

The table lists the most common HTTP status codes returned by the Metronome API, along with a possible solution.

| **Code** | **Meaning**          | **Description**                                                                                     | **Possible solution**                                                                                                                      |
| -------- | -------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 200      | OK                   | Everything worked as expected                                                                       | N/A—the request was successful                                                                                                             |
| 400      | Bad Request          | The request was unacceptable, often due to malformed syntax, or a missing or malformed parameter    | Ensure request syntax is correct                                                                                                           |
| 401      | Invalid access token | Requestor is unauthorized or does not have permission for this API call                             | Ensure API token is valid                                                                                                                  |
| 403      | Forbidden            | Requestor does not have access to this resource                                                     | Ensure API token is valid                                                                                                                  |
| 404      | Resource not found   | The requested resource does not exist                                                               | Ensure ID of requested resource is valid                                                                                                   |
| 409      | Conflict             | The request could not be processed due to a conflict with the current state of an existing resource | Ensure that the object doesn't already exist, and if using an [Idempotency-Key header](/api-reference/idempotency), check that it's unique |
| 429      | Too Many Requests    | Too many requests hit the API too quickly                                                           | Check the `X-Metronome-Rate-Limit-Type` header to determine the limit scope (see below), then backoff and try again later                  |
| 5XX      | Server Errors        | Something went wrong while servicing your request                                                   | Retry your request. If using Idempotency-Key header, verify that resource was not partially created and retry using a different key        |

## Rate limit headers

When a request is rate limited (HTTP 429), the response includes an `X-Metronome-Rate-Limit-Type` header indicating which limit was exceeded:

| **Header value** | **Meaning**                                                           |
| ---------------- | --------------------------------------------------------------------- |
| `client`         | Your organization's overall rate limit for this endpoint was exceeded |
| `customer`       | The per-customer rate limit for the targeted customer was exceeded    |
