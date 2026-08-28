<!-- Source URL: https://docs.metronome.com/api-reference/api-quickstart.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API quickstart

> Get connected to Metronome's API and make your first call in minutes.

## Create an API token

1. Log into the Metronome App [here](https://app.metronome.com/).
2. Navigate to **Developer → API tokens → Add.**
3. Create a new token and give it a descriptive name.
4. Make sure to copy the token to a secure location before clicking Done.

> Learn more about Metronome API authentication [here](/api-reference/authorization).

## Install the Metronome SDK

1. Install the SDK in your environment.

<CodeGroup>
  ```bash Python theme={null}
  pip install --pre metronome-sdk
  ```

  ```bash Node theme={null}
  npm install @metronome/sdk
  ```

  ```bash Ruby theme={null}
  gem install metronome-sdk
  ```

  ```bash Go theme={null}
  go get -u 'github.com/Metronome-Industries/metronome-go'
  ```
</CodeGroup>

2. Configure the SDK by passing in your API key . By default, the SDK looks for the API key under the environment variable METRONOME\_BEARER\_TOKEN.

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
    "fmt"
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

> Learn more about the Metronome SDK [here](/guides/get-started/developer-sdks).

## Test the API

1. Make a test API call - for example, list the customers in your Metronome account. This will work even if your customer list is empty.

<CodeGroup>
  ```python Python theme={null}
  response = client.v1.customers.list()
  print("✓ Connected to Metronome!")
  if response.data:
      customer = response.data[0]
      print(f"  First customer: {customer.name}")
  else:
      print("  No customers found.")
  ```

  ```javascript Node theme={null}
  const resp = await client.v1.customers.list();
  console.log('✓ Connected to Metronome!');
  if (resp.data && resp.data.length > 0) {
    console.log(`  First customer: ${resp.data[0].name}`);
  } else {
    console.log('  No customers found.');
  }
  ```

  ```ruby Ruby theme={null}
  resp = client.v1.customers.list
  puts '✓ Connected to Metronome!'
  if resp.data && !resp.data.empty?
    puts "  First customer: #{resp.data.first.name}"
  else
    puts '  No customers found.'
  end
  ```

  ```go Go theme={null}
  resp, err := client.V1.Customers.List(context.TODO(), metronome.V1CustomerListParams{})
  if err != nil {
    return fmt.Errorf("failed to list customers: %w", err)
  }
  fmt.Println("✓ Connected to Metronome!")
  if len(resp.Data) > 0 {
    fmt.Printf("  First customer: %s\n", resp.Data[0].Name)
  } else {
    fmt.Println("  No customers found.")
  }
  ```
</CodeGroup>

**Success!** You're now connected to Metronome. Once connected, you can track usage, set pricing, and automate invoicing.

## Next Steps

* **Send your first usage event:** track customer usage in real-time [View guide →](/guides/get-started/core-concepts/send-usage-events)
* Check out the implementation guides [View guide →](/guides/pricing-packaging/billing-model-guides/guides-home)
