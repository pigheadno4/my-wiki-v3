<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/split-shipments -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Split shipments

Ship items from a single order to multiple addresses. Common scenarios include:

- Holiday gifts sent to different recipients
- Corporate orders shipped to various office locations
- Drop shipping to different addresses

Use multiple `purchase_units` in a single PayPal order, each with its own shipping address. The customer pays once but items ship to different locations.

## Prerequisites

- Complete [the quick start PayPal integration](/payments/methods/paypal/integrate).
- Implement inventory management per shipping location.

## Integrate server side

<Info>
  Endpoint: [`POST /v2/checkout/orders`](/reference/api/rest/orders/)
</Info>

<CodeGroup>
  ```bash cURL expandable lines theme={null}
  curl -X POST https://api-m.paypal.com/v2/checkout/orders \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{
      "intent": "CAPTURE",
      "purchase_units": [
        {
          "reference_id": "SHIPMENT_1",
          "amount": {
            "currency_code": "USD",
            "value": "50.00"
          },
          "shipping": {
            "name": {
              "full_name": "Recipient 1"
            },
            "address": {
              "address_line_1": "123 Main St",
              "admin_area_2": "San Jose",
              "admin_area_1": "CA",
              "postal_code": "95131",
              "country_code": "US"
            }
          }
        },
        {
          "reference_id": "SHIPMENT_2",
          "amount": {
            "currency_code": "USD",
            "value": "30.00"
          },
          "shipping": {
            "name": {
              "full_name": "Recipient 2"
            },
            "address": {
              "address_line_1": "456 Oak Ave",
              "admin_area_2": "Austin",
              "admin_area_1": "TX",
              "postal_code": "78701",
              "country_code": "US"
            }
          }
        }
      ]
    }'
  ```

```javascript Node.js expandable lines theme={null}
const paypal = require("@paypal/checkout-server-sdk");

// Configure environment
const environment = new paypal.core.SandboxEnvironment(
  "YOUR_CLIENT_ID",
  "YOUR_CLIENT_SECRET",
);
const client = new paypal.core.PayPalHttpClient(environment);

// Create order with multiple purchase units
async function createSplitShipmentOrder() {
  const request = new paypal.orders.OrdersCreateRequest();
  request.requestBody({
    intent: "CAPTURE",
    purchase_units: [
      {
        reference_id: "SHIPMENT_1",
        amount: {
          currency_code: "USD",
          value: "50.00",
        },
        shipping: {
          name: {
            full_name: "Recipient 1",
          },
          address: {
            address_line_1: "123 Main St",
            admin_area_2: "San Jose",
            admin_area_1: "CA",
            postal_code: "95131",
            country_code: "US",
          },
        },
      },
      {
        reference_id: "SHIPMENT_2",
        amount: {
          currency_code: "USD",
          value: "30.00",
        },
        shipping: {
          name: {
            full_name: "Recipient 2",
          },
          address: {
            address_line_1: "456 Oak Ave",
            admin_area_2: "Austin",
            admin_area_1: "TX",
            postal_code: "78701",
            country_code: "US",
          },
        },
      },
    ],
  });

  try {
    const response = await client.execute(request);
    console.log("Order ID:", response.result.id);
    return response.result;
  } catch (error) {
    console.error("Error creating order:", error);
    throw error;
  }
}
```

```python Python expandable lines theme={null}
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest

# Configure environment
environment = SandboxEnvironment(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET'
)
client = PayPalHttpClient(environment)

# Create order with multiple purchase units
def create_split_shipment_order():
    request = OrdersCreateRequest()
    request.request_body({
        'intent': 'CAPTURE',
        'purchase_units': [
            {
                'reference_id': 'SHIPMENT_1',
                'amount': {
                    'currency_code': 'USD',
                    'value': '50.00'
                },
                'shipping': {
                    'name': {
                        'full_name': 'Recipient 1'
                    },
                    'address': {
                        'address_line_1': '123 Main St',
                        'admin_area_2': 'San Jose',
                        'admin_area_1': 'CA',
                        'postal_code': '95131',
                        'country_code': 'US'
                    }
                }
            },
            {
                'reference_id': 'SHIPMENT_2',
                'amount': {
                    'currency_code': 'USD',
                    'value': '30.00'
                },
                'shipping': {
                    'name': {
                        'full_name': 'Recipient 2'
                    },
                    'address': {
                        'address_line_1': '456 Oak Ave',
                        'admin_area_2': 'Austin',
                        'admin_area_1': 'TX',
                        'postal_code': '78701',
                        'country_code': 'US'
                    }
                }
            }
        ]
    })

    try:
        response = client.execute(request)
        print(f'Order ID: {response.result.id}')
        return response.result
    except Exception as error:
        print(f'Error creating order: {error}')
        raise

create_split_shipment_order()
```

```java Java expandable lines theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.orders.*;
import java.util.Arrays;
import java.util.List;

public class SplitShipmentOrder {

    public static void main(String[] args) {
        // Configure environment
        PayPalEnvironment environment = new PayPalEnvironment.Sandbox(
            "YOUR_CLIENT_ID",
            "YOUR_CLIENT_SECRET"
        );
        PayPalHttpClient client = new PayPalHttpClient(environment);

        createSplitShipmentOrder(client);
    }

    public static OrderRequest buildRequestBody() {
        OrderRequest orderRequest = new OrderRequest();
        orderRequest.checkoutPaymentIntent("CAPTURE");

        List<PurchaseUnitRequest> purchaseUnits = Arrays.asList(
            new PurchaseUnitRequest()
                .referenceId("SHIPMENT_1")
                .amountWithBreakdown(new AmountWithBreakdown()
                    .currencyCode("USD")
                    .value("50.00"))
                .shippingDetail(new ShippingDetail()
                    .name(new Name().fullName("Recipient 1"))
                    .addressPortable(new AddressPortable()
                        .addressLine1("123 Main St")
                        .adminArea2("San Jose")
                        .adminArea1("CA")
                        .postalCode("95131")
                        .countryCode("US"))),

            new PurchaseUnitRequest()
                .referenceId("SHIPMENT_2")
                .amountWithBreakdown(new AmountWithBreakdown()
                    .currencyCode("USD")
                    .value("30.00"))
                .shippingDetail(new ShippingDetail()
                    .name(new Name().fullName("Recipient 2"))
                    .addressPortable(new AddressPortable()
                        .addressLine1("456 Oak Ave")
                        .adminArea2("Austin")
                        .adminArea1("TX")
                        .postalCode("78701")
                        .countryCode("US")))
        );

        orderRequest.purchaseUnits(purchaseUnits);
        return orderRequest;
    }

    public static void createSplitShipmentOrder(PayPalHttpClient client) {
        OrdersCreateRequest request = new OrdersCreateRequest();
        request.requestBody(buildRequestBody());

        try {
            HttpResponse<Order> response = client.execute(request);
            System.out.println("Order ID: " + response.result().id());
        } catch (IOException e) {
            System.err.println("Error creating order: " + e.getMessage());
        }
    }
}
```

```php PHP expandable lines theme={null}
<?php
require __DIR__ . '/vendor/autoload.php';

use PayPalCheckoutSdk\Core\PayPalHttpClient;
use PayPalCheckoutSdk\Core\SandboxEnvironment;
use PayPalCheckoutSdk\Orders\OrdersCreateRequest;

// Configure environment
$environment = new SandboxEnvironment('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET');
$client = new PayPalHttpClient($environment);

// Create order with multiple purchase units
function createSplitShipmentOrder($client) {
    $request = new OrdersCreateRequest();
    $request->body = [
        'intent' => 'CAPTURE',
        'purchase_units' => [
            [
                'reference_id' => 'SHIPMENT_1',
                'amount' => [
                    'currency_code' => 'USD',
                    'value' => '50.00'
                ],
                'shipping' => [
                    'name' => [
                        'full_name' => 'Recipient 1'
                    ],
                    'address' => [
                        'address_line_1' => '123 Main St',
                        'admin_area_2' => 'San Jose',
                        'admin_area_1' => 'CA',
                        'postal_code' => '95131',
                        'country_code' => 'US'
                    ]
                ]
            ],
            [
                'reference_id' => 'SHIPMENT_2',
                'amount' => [
                    'currency_code' => 'USD',
                    'value' => '30.00'
                ],
                'shipping' => [
                    'name' => [
                        'full_name' => 'Recipient 2'
                    ],
                    'address' => [
                        'address_line_1' => '456 Oak Ave',
                        'admin_area_2' => 'Austin',
                        'admin_area_1' => 'TX',
                        'postal_code' => '78701',
                        'country_code' => 'US'
                    ]
                ]
            ]
        ]
    ];

    try {
        $response = $client->execute($request);
        echo "Order ID: " . $response->result->id . "\n";
        return $response->result;
    } catch (Exception $e) {
        echo "Error creating order: " . $e->getMessage() . "\n";
        throw $e;
    }
}

createSplitShipmentOrder($client);
?>
```

```ruby Ruby expandable lines theme={null}
require 'paypal-checkout-sdk'

# Configure environment
environment = PayPal::SandboxEnvironment.new(
  'YOUR_CLIENT_ID',
  'YOUR_CLIENT_SECRET'
)
client = PayPal::PayPalHttpClient.new(environment)

# Create order with multiple purchase units
def create_split_shipment_order(client)
  request = PayPalCheckoutSdk::Orders::OrdersCreateRequest.new
  request.request_body({
    intent: 'CAPTURE',
    purchase_units: [
      {
        reference_id: 'SHIPMENT_1',
        amount: {
          currency_code: 'USD',
          value: '50.00'
        },
        shipping: {
          name: {
            full_name: 'Recipient 1'
          },
          address: {
            address_line_1: '123 Main St',
            admin_area_2: 'San Jose',
            admin_area_1: 'CA',
            postal_code: '95131',
            country_code: 'US'
          }
        }
      },
      {
        reference_id: 'SHIPMENT_2',
        amount: {
          currency_code: 'USD',
          value: '30.00'
        },
        shipping: {
          name: {
            full_name: 'Recipient 2'
          },
          address: {
            address_line_1: '456 Oak Ave',
            admin_area_2: 'Austin',
            admin_area_1: 'TX',
            postal_code: '78701',
            country_code: 'US'
          }
        }
      }
    ]
  })

  begin
    response = client.execute(request)
    puts "Order ID: #{response.result.id}"
    response.result
  rescue => error
    puts "Error creating order: #{error.message}"
    raise error
  end
end

create_split_shipment_order(client)
```

</CodeGroup>
