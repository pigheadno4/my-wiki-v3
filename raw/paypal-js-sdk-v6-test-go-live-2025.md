<!-- Source URL: https://docs.paypal.ai/developer/how-to/js-sdk/v6/test-go-live -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test and go live

Before you go live with the JavaScript SDK v6, test your integration end to end, and confirm you've completed all items in the production checklist.

## Prerequisites

Before you test:

- Get a [client ID and secret](/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret).
- [Set up the v6 SDK](/developer/how-to/sdk/js/v6/configuration).

## Test

- Test across different browsers and devices.
- Verify popup blocker handling.
- Test all callback scenarios (approve, cancel, error).
- Validate eligibility logic works correctly.

## Production checklist

- Replace sandbox URLs with production URLs.
- Update environment configuration for production.
- Test eligibility on production environment.
- Implement comprehensive error handling.
- Add analytics and conversion tracking.
- Test across different devices and browsers.
- Implement proper loading and success states.
- Set up monitoring and alerting.
- Verify webhook endpoints are configured.
- Test order capture and fulfillment process.
