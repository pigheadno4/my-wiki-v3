<!-- Source URL: https://docs.paypal.ai/grow/reports-analytics/transaction-reports-api -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate reports using Transaction Reports API

The [Transaction Search API](https://developer.paypal.com/docs/api/transaction-search/v1/) provides programmatic access to your PayPal transaction data, enabling real-time queries and automated reporting workflows. You can use this API to get transaction data with various query parameters and filters.

It takes a maximum of three hours for executed transactions to appear in the API calls, and it provides transaction data for the previous three years.

## Prerequisites

- PayPal Developer account.
- API credentials (Client ID and Secret).
- Access token generation capability.
- Understanding of REST API principles.

## Server-side integration

### Authentication setup

```javascript theme={null}
// Generate access token
const getAccessToken = async () => {
  const auth = Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString("base64");

  const response = await fetch("https://api-m.paypal.com/v1/oauth2/token", {
    method: "POST",
    headers: {
      Authorization: `Basic ${auth}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "grant_type=client_credentials",
  });

  return await response.json();
};
```

### Basic transaction search

```javascript theme={null}
// Search transactions
const searchTransactions = async (accessToken, params) => {
  const queryString = new URLSearchParams(params).toString();

  const response = await fetch(
    `https://api-m.paypal.com/v1/reporting/transactions?${queryString}`,
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
    },
  );

  return await response.json();
};
```

## Steps for implementation

1. **Set up authentication**
   - Obtain API credentials from PayPal Developer portal.
   - Implement token generation and refresh logic.
   - Secure credential storage.

2. **Build query parameters**
   - Define date ranges.
   - Set transaction status filters.
   - Configure pagination settings.

3. **Make API calls**
   - Send authenticated requests.
   - Handle response data.
   - Implement error handling.

4. **Process results**
   - Parse transaction data.
   - Transform for your business logic.
   - Store or forward as needed.

### Warnings

- API rate limits apply (check documentation).
- Date ranges are limited to specific periods.
- Some transaction details may have delays.

## Samples

```javascript theme={null}
// Example transaction search with filters
const params = {
  start_date: "2024-01-01T00:00:00Z",
  end_date: "2024-01-31T23:59:59Z",
  transaction_status: "SUCCESS",
  page_size: 100,
};

const transactions = await searchTransactions(accessToken, params);
```

## Testing

- Use sandbox endpoints for development.
- Test with various date ranges and filters.
- Verify pagination handling.
- Check error response handling.

## Best practices

- Implement proper authentication refresh.
- Use appropriate page sizes.
- Handle rate limiting gracefully.
- Store transaction IDs for deduplication.
