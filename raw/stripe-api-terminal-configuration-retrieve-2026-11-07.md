<!-- Source URL: https://docs.stripe.com/api/terminal/configuration/retrieve -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Retrieve a Configuration

Retrieves a `Configuration` object.

## Prerequisites

Before you can run the following code snippet, you need to call these APIs with the provided parameters to set up the prerequisite API object(s).

1. createTerminalConfiguration
POST /v1/terminal/configurations

## Request

```curl
curl https://api.stripe.com/v1/terminal/configurations/{{CONFIGURATION_ID}} \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive"
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "is_account_default": false,
  "livemode": false
}
```

## Parameters

- `id` (string, required)
  Unique identifier for the object.

## Returns

Returns a `Configuration` object if a valid identifier was provided.
