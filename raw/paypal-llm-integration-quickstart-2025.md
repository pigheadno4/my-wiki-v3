<!-- Source URL: https://docs.paypal.ai/developer/tools/ai/llm-integration -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM integration quickstart guide

PayPal recently launched a <a href="https://www.paypal.ai/tools/mcp-quickstart" target="_blank">Model Context Protocol (MCP) server</a> that customers can use to access the power of PayPal using natural language with any AI agent. PayPal's remote MCP server now supports large language models (LLMs) from [Anthropic](https://www.anthropic.com/) and [OpenAI](https://openai.com/), which brings even greater flexibility.

## Before you begin

Before you begin, generate a PayPal access token. You can generate an access token by making a POST request to PayPal's token endpoint, or you can generate it programmatically. For more information, see [Get client ID and client secret](https://developer.paypal.com/api/rest/#link-getclientidandclientsecret).

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api-m.paypal.com/v1/oauth2/token" \
    -u "$PAYPAL_CLIENT_ID:$PAYPAL_CLIENT_SECRET" \
    -H "Accept: application/json" \
    -H "Accept-Language: en_US" \
    -d "grant_type=client_credentials"
  ```

```python Python theme={null}
response = requests.post(
    "https://api-m.paypal.com/v1/oauth2/token",
    headers={
        "Accept": "application/json",
        "Accept-Language": "en_US",
    },
    data={"grant_type": "client_credentials"},
    auth=HTTPBasicAuth(client_id, client_secret)  # Basic Auth
)
access_token = response.json()["access_token"]
```

```typescript TypeScript theme={null}
const clientId = process.env.PAYPAL_CLIENT_ID!;
const clientSecret = process.env.PAYPAL_CLIENT_SECRET!;
const auth = Buffer.from(`${clientId}:${clientSecret}`).toString("base64");

(async () => {
  const response = await fetch("https://api-m.paypal.com/v1/oauth2/token", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Accept-Language": "en_US",
      "Content-Type": "application/x-www-form-urlencoded",
      Authorization: `Basic ${auth}`,
    },
    body: "grant_type=client_credentials",
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const data = await response.json();
  const accessToken = data.access_token;
  console.log(accessToken);
})();
```

</CodeGroup>

## Anthropic integration

When you have your access token, you can connect the remote MCP server with the Anthropic LLM using the steps on this page from [Anthropic](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector). For more information about connecting to PayPal's remote MCP server, see the <a href="/developer/tools/ai/mcp-quickstart" target="_blank" rel="noopener noreferrer">MCP server quickstart guide</a>.

After you connect, you can start using Anthropic's LLM with PayPal's MCP server tools by initializing the client and making a request. For example, you could ask it to create an invoice, as shown in the following code examples.

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "X-API-Key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mcp-client-2025-04-04" \
    -d '{
      "model": "claude-sonnet-4-20250514",
      "max_tokens": 1000,
      "messages": [{"role": "user", "content": "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour."}],
      "mcp_servers": [
        {
          "type": "url",
          "url": "https://mcp.paypal.com/sse",
          "name": "example-mcp",
          "authorization_token": "YOUR_TOKEN"
        }
      ]
    }'
  ```

```python Python theme={null}
import os
import requests

api_key = os.environ["ANTHROPIC_API_KEY"]
url = "https://api.anthropic.com/v1/messages"
payload = {
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 1000,
    "messages": [{
        "role": "user",
        "content": "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour."
    }],
    "mcp_servers": [{
        "type": "url",
        "url": "https://mcp.paypal.com/sse",
        "name": "example-mcp",
        "authorization_token": "YOUR_TOKEN"
    }]
}
headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key,
    "anthropic-version": "2023-06-01",
    "anthropic-beta": "mcp-client-2025-04-04"
}
response = requests.post(url, json=payload, headers=headers)
print(response.text)
```

```typescript TypeScript theme={null}
const apiKey = process.env.ANTHROPIC_API_KEY!;
const url = "https://api.anthropic.com/v1/messages";

const payload = {
  model: "claude-sonnet-4-20250514",
  max_tokens: 1000,
  messages: [
    {
      role: "user",
      content:
        "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour.",
    },
  ],
  mcp_servers: [
    {
      type: "url",
      url: "https://mcp.paypal.com/sse",
      name: "example-mcp",
      authorization_token: "YOUR_TOKEN",
    },
  ],
};

(async () => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": apiKey,
      "anthropic-version": "2023-06-01",
      "anthropic-beta": "mcp-client-2025-04-04",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const data = await response.json();
  console.log(data);
})();
```

</CodeGroup>

## OpenAI integration

For additional information about the OpenAI side of this integration, see [this post](https://gist.github.com/stevenheidel/a6c8ed8ce1632dff1284e44a17554993) from OpenAI.

- When you have your access token, you can connect to the MCP server. For details about connecting to PayPal's remote MCP server, see the <a href="/developer/tools/ai/mcp-quickstart" target="_blank" rel="noopener noreferrer">MCP server quickstart guide</a> in PayPal's developer documentation.
- After you connect, you can start using OpenAI with PayPal's MCP server tools by initializing the client and making a request. For example, you can ask the client to create an invoice, as shown in the following code examples.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST https://api.openai.com/v1/responses \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
      "model": "gpt-4.1",
      "tools": [
        {
          "type": "mcp",
          "server_label": "paypal-mcp",
          "server_url": "https://mcp.paypal.com/sse",
          "require_approval": "never",
          "headers": { "Authorization": "Bearer $PAYPAL_ACCESSTOKEN" }
        }
      ],
      "input": "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour."
    }'
  ```

```python Python theme={null}
import os
import requests

api_key = os.environ["OPENAI_API_KEY"]
url = "https://api.openai.com/v1/chat/completions"
payload = {
    "model": "gpt-4.1",
    "tools": [
        {
            "type": "mcp",
            "server_label": "paypal-mcp",
            "server_url": "https://mcp.paypal.com/sse"
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour."
        }
    ]
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
response = requests.post(url, json=payload, headers=headers)
print(response.text)
```

```typescript TypeScript theme={null}
const apiKey = process.env.OPENAI_API_KEY!;
const url = "https://api.openai.com/v1/chat/completions";

const payload = {
  model: "gpt-4.1",
  tools: [
    {
      type: "mcp",
      server_label: "paypal-mcp",
      server_url: "https://mcp.paypal.com/sse",
    },
  ],
  messages: [
    {
      role: "user",
      content:
        "Create an invoice for john.doe@example.com for 2 hours of consulting services at the rate of $150 per hour.",
    },
  ],
};

(async () => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  const data = await response.json();
  console.log(data);
})();
```

</CodeGroup>
