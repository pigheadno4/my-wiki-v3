<!-- Source URL: https://docs.paypal.ai/grow/reports-analytics/how-it-works -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How reports and analytics work

PayPal's reporting system processes transaction data in real-time and batch modes, providing comprehensive insights through various access methods and data formats.

## Getting started

### Data flow architecture

1. **Transaction processing**: PayPal captures all payment events.
2. **Data aggregation**: Information is compiled and indexed.
3. **Report generation**: Data is formatted for various output types.
4. **Delivery methods**: Reports delivered via dashboard, API, or automation.

## Core components

### Data collection

- Real-time transaction capture.
- Event logging and timestamping.
- Multi-currency processing.
- Geographic data tracking.

### Processing pipeline

- Data validation and cleansing.
- Aggregation and summarization.
- Format conversion and optimization.
- Security and compliance filtering.

### Delivery mechanisms

- **Synchronous**: Immediate API responses.
- **Asynchronous**: Scheduled report generation.
- **Event-driven**: Webhook notifications.

## Integration patterns

### Pull-based access

- API calls initiated by your system.
- On-demand data retrieval.
- Real-time query capabilities.

### Push-based delivery

- PayPal initiates data delivery.
- Scheduled report generation.
- Webhook event notifications.

## Best practices

- Understand data latency characteristics.
- Implement appropriate caching strategies.
- Plan for peak processing times.
- Monitor API rate limits.
