<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/rate-limiting -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limiting with PayPal REST APIs

Rate limiting restricts the number of API requests you can make in a specific time frame. When you exceed this limit, PayPal's servers may deny further requests until your usage drops below the limit. This protects the system from overload.

If you or your customers receive a `429` status code, too many requests were sent, which might indicate anomalous traffic. PayPal uses rate limits to ensure stability.

Understanding rate limiting can help you avoid disruptions when building or scaling your app.

PayPal may enforce rate limits for several reasons:

- **Excessive polling:** Making too many requests instead of using webhooks.
- **Traffic spikes:** A sudden increase in requests due to user activity or system events.
- **Token misuse:** Failing to reuse OAuth 2.0 tokens and repeatedly fetching new ones.
- **Suspicious patterns:** Behavior flagged as atypical or potentially harmful.

> **Note:** PayPal doesn't publish exact rate limits because they vary depending on the API, environment, and circumstances. By keeping these limits flexible, PayPal can scale services to match demand while preventing abuse.

## How to prepare for rate limiting

Here's what you can do to reduce the chances of hitting a rate limit:

- **Use webhooks instead of polling:** [Webhooks](https://developer.paypal.com/api/rest/webhooks/) let PayPal send updates directly to your system, so you don't need to keep requesting information.
- **Cache OAuth 2.0 tokens:** Instead of creating new tokens for every request, securely store and reuse tokens until they expire.
- **Optimize your requests:** Minimize unnecessary calls, and don't request data more often than needed. Combine requests whenever possible.
- **Plan for scale:** If you expect high traffic, test your system to ensure it works efficiently under heavy load.

## What to do if you hit a rate limit

If your API requests start failing due to rate limiting, follow these steps:

- **Diagnose the issue:** Check your API logs to understand why the limit was triggered. Look for patterns in request frequency or behavior.
- **Reduce request frequency:** Slow down request rates or spread them out over time to stay within limits.
- **Retry with exponential backoff:** Increase the delay between requests each time a request fails.
- **Use webhooks instead of polling:** If you're polling for updates, switch to PayPal's webhooks to receive alerts automatically.
- **Implement error handling**: Implement error handling as in the following example code.

In a production environment, you'd want to:

- Use a more robust storage mechanism.
- Implement proper secure token management.
- Use a production-grade logging system.
- Consider more sophisticated retry strategies with maximum retry limits.
- Add additional error handling for different types of API responses.

```javascript theme={null}
// Example error handling for rate limits
function apiRequest(endpoint, data) {
  return fetch(endpoint, {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => {
      if (response.status === 429) {
        // Extract retry-after header if available
        const retryAfter = response.headers.get("Retry-After") || 30;

        // Log the rate limiting event
        console.log(`Rate limited. Retrying in ${retryAfter} seconds`);

        // Implement exponential backoff
        return new Promise((resolve) => {
          setTimeout(
            () => resolve(apiRequest(endpoint, data)),
            retryAfter * 1000,
          );
        });
      }

      return response.json();
    })
    .catch((error) => {
      // Log the error for debugging
      console.error("API request failed:", error);

      // Determine if retry is appropriate
      if (isRetryableError(error)) {
        return retryWithBackoff(apiRequest, [endpoint, data]);
      }

      throw error;
    });
}
```

If you need further assistance, reach out to [Merchant Technical Support](https://www.paypal.com/mts?_ga=2.12095284.1829917444.1751296466-935108042.1736183519&_gac=1.90987240.1749058302.CjwKCAjw3f_BBhAPEiwAaA3K5GZi7UMt1wQxD_c8GrhAiGQRTsNsuH7lglTyr9KlGTH_zQ73HWpLtBoCtrsQAvD_BwE).
