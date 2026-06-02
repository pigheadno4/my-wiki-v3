<!-- Source URL: https://docs.paypal.ai/grow/reports-analytics/troubleshooting -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting reports and analytics

Common reporting issues can be resolved by following systematic troubleshooting steps and understanding PayPal's error responses and system limitations.

## Getting started

### Common error types

- Authentication failures
- API rate limit exceeded
- Invalid request parameters
- Data availability issues
- Network connectivity problems

### Error response format

PayPal API errors follow a standard format:

```json theme={null}
{
  "error": "invalid_client",
  "error_description": "Client authentication failed",
  "error_uri": "https://developer.paypal.com/docs/api/overview/#error"
}
```

### Error codes

| Error                    | Message                                                                                      | Description                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `INTERNAL_SERVICE_ERROR` | Internal service error.                                                                      | Something unexpected occurred on the server.                                                                                     |
| `INVALID_REQUEST`        | Invalid request - see details.                                                               | The request is not well-formed or is syntactically incorrect or violates the schema.                                             |
| `INVALID_RESOURCE_ID`    | The resource was not found.                                                                  | The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible. |
| `RESULTSET_TOO_LARGE`    | Result set size is greater than the maximum limit. Change the filter criteria and try again. | The request returned more items than the maximum limit. To reduce the result set, include additional query                       |

### Troubleshooting steps

#### 1. Authentication issues

##### Symptoms

- HTTP 401 Unauthorized responses
- "invalid_client" errors
- Token expiration messages

##### Solutions

```javascript theme={null}
// Check token validity
const validateToken = async (token) => {
  try {
    const response = await fetch(
      "https://api-m.paypal.com/v1/identity/oauth2/userinfo",
      {
        headers: {
          Authorization: `Bearer ${token}`,
          Accept: "application/json",
        },
      },
    );

    if (!response.ok) {
      console.error("Token invalid:", response.status);
      return false;
    }

    return true;
  } catch (error) {
    console.error("Token validation failed:", error);
    return false;
  }
};

// Refresh token if needed
const refreshAccessToken = async () => {
  // Implement token refresh logic
  const newToken = await getAccessToken();
  return newToken;
};
```

#### 2. Rate limiting problems

##### Symptoms

- HTTP 429 Too Many Requests
- Temporary service unavailable
- Slow response times

##### Solutions

```javascript theme={null}
// Implement exponential backoff
const makeRequestWithRetry = async (url, options, maxRetries = 3) => {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url, options);

      if (response.status === 429) {
        const retryAfter =
          response.headers.get("Retry-After") || Math.pow(2, attempt);
        await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));
        continue;
      }

      return response;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      await new Promise((resolve) =>
        setTimeout(resolve, Math.pow(2, attempt) * 1000),
      );
    }
  }
};
```

#### 3. Data query issues

##### Invalid date ranges

```javascript theme={null}
// Validate date parameters
const validateDateRange = (startDate, endDate) => {
  const start = new Date(startDate);
  const end = new Date(endDate);
  const now = new Date();
  const maxRangeMs = 31 * 24 * 60 * 60 * 1000; // 31 days

  if (start > end) {
    throw new Error("Start date must be before end date");
  }

  if (end > now) {
    throw new Error("End date cannot be in the future");
  }

  if (end - start > maxRangeMs) {
    throw new Error("Date range cannot exceed 31 days");
  }

  return true;
};
```

##### Missing transaction data

```javascript theme={null}
// Handle incomplete data
const processTransactionSafely = (transaction) => {
  const safeTransaction = {
    id: transaction.transaction_id || "UNKNOWN",
    amount: transaction.transaction_amount?.value || "0.00",
    currency: transaction.transaction_amount?.currency_code || "USD",
    date: transaction.transaction_initiation_date || new Date().toISOString(),
    status: transaction.transaction_status || "UNKNOWN",
  };

  // Log missing fields for monitoring
  if (!transaction.transaction_id) {
    console.warn("Missing transaction ID:", transaction);
  }

  return safeTransaction;
};
```

#### 4. Network and connectivity issues

##### Connection timeouts

```javascript theme={null}
// Configure appropriate timeouts
const fetchWithTimeout = async (url, options = {}) => {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 30000); // 30 second timeout

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });

    clearTimeout(timeoutId);
    return response;
  } catch (error) {
    clearTimeout(timeoutId);

    if (error.name === "AbortError") {
      throw new Error("Request timeout");
    }

    throw error;
  }
};
```

### Diagnostic tools

#### API response logging

```javascript theme={null}
// Comprehensive error logging
const logApiError = (error, requestDetails) => {
  console.error("PayPal API Error:", {
    timestamp: new Date().toISOString(),
    endpoint: requestDetails.url,
    method: requestDetails.method,
    status: error.status,
    message: error.message,
    requestId: error.headers?.["paypal-request-id"],
  });
};
```

#### Health check implementation

```javascript theme={null}
// Regular API health monitoring
const checkApiHealth = async () => {
  try {
    const token = await getAccessToken();
    const response = await fetch(
      "https://api-m.paypal.com/v1/reporting/transactions?page_size=1",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    );

    return response.ok;
  } catch (error) {
    console.error("API health check failed:", error);
    return false;
  }
};
```

## Error prevention best practices

- Implement comprehensive error handling.
- Use appropriate request timeouts.
- Monitor API rate limits.
- Validate input parameters.
- Log errors with sufficient detail.
- Set up alerting for critical failures.
- Regular health checks and monitoring.
- Keep API credentials secure and up-to-date.
