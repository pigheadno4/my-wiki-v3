<!-- Source URL: https://docs.metronome.com/api-reference/authentication.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Authentication

Metronome’s API uses bearer tokens to authenticate requests. This page walks through how to create and manage tokens.

## **Create a token**

API tokens can be created through the Metronome app.

1. Click on **Connections** in the navigation bar.
2. Click on **API tokens & webhooks** in the horizontal navigation bar on the resulting page.
3. Click on the **+ Add** button.
4. Enter a descriptive name for the token and click **Create new token.**
5. Copy the token string to a secure location before clicking **Done.**

<Warning>
  **SAVE YOUR TOKEN**

  Be sure to save the token you create. You cannot view the full token again.
</Warning>

Create as many tokens as is useful, providing descriptive names for each. The token's name is associated with API calls made using it, which can be helpful when tracking changes and requests in the Metronome's [audit logs](../guides/platform-configuration/audit-logs).

## Using tokens

When making API calls, provide the token using the `Authorization` header. If using the SDK, the SDK will look for the API key under the environment variable `METRONOME_BEARER_TOKEN` by default. See **SDK documentation** for more details.

<CodeGroup>
  ```python Python theme={null}
  from metronome import Metronome

  client = Metronome(
    # Defaults to os.environ.get("METRONOME_BEARER_TOKEN") if omitted
    bearer_token="My bearer token",
  )
  ```

  ```javascript Node theme={null}
  import Metronome from "@metronome/sdk";

  const client = new Metronome({
    // Defaults to os.environ.get("METRONOME_BEARER_TOKEN") if omitted
    bearerToken: "My bearer token",
  });
  ```

  ```ruby Ruby theme={null}
  require "bundler/setup"
  require "metronome_sdk"

  metronome = MetronomeSDK::Client.new(
      bearer_token: "My Bearer Token" # defaults to ENV["METRONOME_BEARER_TOKEN"]
  )
  ```

  ```go Go theme={null}
  package main

  import (
    "context"
    "github.com/Metronome-Industries/metronome-go"
    "github.com/Metronome-Industries/metronome-go/option"
  )

  func main() {
    client := metronome.NewClient(
      option.WithBearerToken("My bearer token"), // defaults to os.LookupEnv("METRONOME_BEARER_TOKEN") if omitted
    )
  }
  ```
</CodeGroup>

If your token is valid, you’ll receive a JSON payload from the API—either data (if the endpoint returns records) or a 404 JSON error object if no resources are found.

If your token is invalid, you’ll receive a 401 or 403 error. See API status codes for more detail.

## Postman Setup

If you use Postman:

1. Import the [Metronome OpenAPI spec](https://api.metronome.com/v1/docs/openapi).
2. In the collection settings, set **Authorization** to **Bearer Token** and use `{{api_token}}` as the token.
3. Add `api_token` to your Postman environment variables.

See our [Postman guide](./postman) for step-by-step instructions.

## Permissions

By default, Metronome API tokens will retain the same permissions as the user that created them. Metronome API tokens can also be limited in scope to reduce risk and follow the principle of least privilege. Metronome supports scoping by:

* Access level (e.g., read-only)
* Environment (e.g., sandbox only)
* Endpoint (e.g., only getCustomers)

To adjust permissions, contact your Metronome representative.

## Archiving tokens

Metronome enables archiving tokens that are no longer in use. To do this, simply hit the Trash icon next to the relevant token in the Metronome UI. This action cannot be undone.

<Tip>
  **BEST PRACTICES**

  Follow security best practices by removing unused tokens and regularly rotating tokens in use.
</Tip>
