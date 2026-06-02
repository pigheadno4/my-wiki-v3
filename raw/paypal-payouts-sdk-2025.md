<!-- Source URL: https://docs.paypal.ai/growth/payouts/test-and-go-live/payouts-sdk -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Payouts SDK

You can use the PayPal Payouts SDK for Java or Python to work with the Payouts REST API. The SDK helps keep your integration up to date with API changes and is intended for server-side use only.

With the SDK, you can:

- Handle OAuth 2.0 authentication automatically.
- Call the Payouts API with less code.
- Manage API responses and handle errors.

<Note>If you want a more customized integration or use a language not supported by the SDK, use the Payouts API directly. For more information, see <a href="/growth/payouts/send-money/use-payouts-api" target="_blank" rel="noopener noreferrer">Use Payouts API</a>.</Note>

## Install SDK

Install the Payouts SDK in your preferred language.

<CodeGroup>
  ```bash Java lines theme={null}
  # Create a Java Maven or Gradle project in your directory, then add the following dependency to the project from Maven Central.
  <dependency>
    <groupId>com.paypal.sdk</groupId>
    <artifactId>payouts-sdk</artifactId>
    <version>1.1.1</version>
  </dependency>
  ```

```bash Python lines theme={null}
# Create a Python project in your directory, then run the following command to install the PayPal Payouts Python SDK.
pip install paypal-payouts-sdk
```

</CodeGroup>

## Set up your environment and credentials

1. Create a new file in your preferred language in the directory where you installed the SDK.
2. Copy the following code sample for your language to initialize the SDK and configure your environment.
3. Update the code with your PayPal client ID and secret.
4. Set the environment to `SandboxEnvironment` for testing or `LiveEnvironment` for production.

<CodeGroup>
  ```java Java lines expandable theme={null}
  import com.paypal.core.PayPalEnvironment;
  import com.paypal.core.PayPalHttpClient;

public class PayPalClient
{
/**
_ Set up PayPal SDK environment with your access credentials.
_ This sample uses SandboxEnvironment. In production, use LiveEnvironment.
\*/
private PayPalEnvironment environment = new PayPalEnvironment.Sandbox(
System.getProperty("PAYPAL_CLIENT_ID") != null ? System.getProperty("PAYPAL_CLIENT_ID") : "PAYPAL_CLIENT_ID",
System.getProperty("PAYPAL_CLIENT_SECRET") != null ? System.getProperty("PAYPAL_CLIENT_SECRET") : "PAYPAL_CLIENT_SECRET");
/**
_ Returns a PayPal HTTP client instance.
_ Use this instance to call PayPal APIs.
_/
PayPalHttpClient client = new PayPalHttpClient(environment);
/\*\*
_ Method to get client object
_ @return PayPalHttpClient client
_/
public PayPalHttpClient client()
{
return this.client;
}
}

````

```python Python lines expandable theme={null}
import os
from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment

class PayPalClient:
    def __init__(self):
        self.client_id =  os.environ["PAYPAL_CLIENT_ID"] if 'PAYPAL_CLIENT_ID' in os.environ else "PAYPAL_CLIENT_ID"
        self.client_secret = os.environ["PAYPAL_CLIENT_SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else "PAYPAL_CLIENT_SECRET"

        # Set up and return PayPal Python SDK environment with PayPal Access credentials.
        # This sample uses SandboxEnvironment. In production, use LiveEnvironment.
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        # Returns a PayPal HTTP client instance.
        # Use this instance to call PayPal APIs.
        self.client = PayPalHttpClient(self.environment)
````

</CodeGroup>

<Note>For more information on finding your REST API credentials for both sandbox and live environments, see <a href="https://developer.paypal.com/api/rest/sandbox/accounts/" target="_blank" rel="noopener noreferrer">Sandbox accounts</a>.</Note>

## Create payout batch

Use the following code samples to create a payout batch.

<CodeGroup>
  ```java Java lines expandable theme={null}
  package com.paypal;

import com.paypal.http.Encoder;
import com.paypal.http.HttpResponse;
import com.paypal.http.exceptions.HttpException;
import com.paypal.http.serializer.Json;
import com.paypal.payouts.Error;
import com.paypal.payouts.\*;
import org.apache.commons.lang3.RandomStringUtils;
import org.json.JSONObject;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class CreatePayoutsBatch extends PayPalClient {
private static final Encoder encoder = new Encoder();
/**
_ This sample creates a payout batch with five payout items.
_ Calls the create batch payout API (POST - /v1/payments/payouts).
_ A maximum of 15000 payout items are supported in a single batch request.
_ @return - Response for the create batch payout call.
_ @throws IOException - Throws exception if the API call fails.
_/
public HttpResponse<CreatePayoutResponse> createPayout() throws IOException {
PayoutsPostRequest request = buildRequestBody(false);
HttpResponse<CreatePayoutResponse> response = client().execute(request);
System.out.println("Response Body:");
System.out.println(new JSONObject(new Json().serialize(response.result())).toString(4));
return response;
}
/**
_ Builds a request body to create payout batch with five payout items to receivers' email.
_ @param isValidationFailure - Includes validation failure in payload.
_ @return - Request payload for Payouts create (POST) request.
_/
private PayoutsPostRequest buildRequestBody(boolean isValidationFailure) {
List<PayoutItem> items = IntStream
.range(1, 6)
.mapToObj(index -> new PayoutItem()
.senderItemId("Test*txn*" + index)
.note("Thank you for your business!")
.receiver("payout-sdk-" + index + "@paypal.com")
.amount(new Currency()
.currency("USD")
.value(isValidationFailure ? "1.0.0" : "1.00")))
.collect(Collectors.toList());
CreatePayoutRequest payoutBatch = new CreatePayoutRequest()
.senderBatchHeader(new SenderBatchHeader()
.senderBatchId("Test*sdk*" + RandomStringUtils.randomAlphanumeric(7))
.emailMessage("SDK payouts test txn")
.emailSubject("This is a test transaction from SDK")
.recipientType("EMAIL"))
.items(items);
return new PayoutsPostRequest()
.requestBody(payoutBatch);
}
/\*\*
_ Driver method to execute this sample.
_ This creates a payout batch with five items and prints the response.
_ @param args
_ @throws IOException - Throws exception if the API call fails.
\*/
public static void main(String[] args) throws IOException {
new CreatePayoutsBatch().createPayout();
}
}

````

```python Python lines expandable theme={null}
import json
import random
import string
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalhttp.serializers.json_serializer import Json
from paypalhttp.http_error import HttpError
from paypalhttp.encoder import Encoder

class CreatePayouts(PayPalClient):
    # Creates a payout batch with two payout items.
    # Calls the create batch payout API (POST - /v1/payments/payouts).
    # A maximum of 15000 payout items are supported in a single batch request.
    @staticmethod
    def build_request_body(include_validation_failure = False):
        senderBatchId = str(''.join(random.sample(string.ascii_uppercase + string.digits, k=7)))
        amount = "1.0.0" if include_validation_failure else "1.00"
        return {
            "sender_batch_header": {
                "recipient_type": "EMAIL",
                "email_message": "SDK payouts test txn",
                "sender_batch_id": senderBatchId,
                    "email_subject": "This is a test transaction from SDK"
                },
                "items": [{
                    "note": "Thank you for your business!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-1@paypal.com",
                    "sender_item_id": "Test_txn_1"
                }, {
                    "note": "Thank you for your business!",
                    "amount": {
                        "currency": "USD",
                        "value": amount
                    },
                    "receiver": "payout-sdk-2@paypal.com",
                    "sender_item_id": "Test_txn_2"
                }]
            }

    def create_payouts(self, debug=False):
        request = PayoutsPostRequest()
        request.request_body(self.build_request_body(False))
        response = self.client.execute(request)
        if debug:
            print("Status Code: ", response.status_code)
            print("Payout Batch ID: " + response.result.batch_header.payout_batch_id)
            print("Payout Batch Status: " + response.result.batch_header.batch_status)
            print("Links: ")
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            # To toggle print the whole body comment/uncomment the below line
            # json_data = self.object_to_json(response.result)
            # print "json_data: ", json.dumps(json_data, indent=4)
        return response

# Driver function which invokes the create_payouts function to create a payout batch.
if __name__ == "__main__":
    CreatePayouts().create_payouts(debug=True)
````

</CodeGroup>

## Track status

Use the payout batch ID to retrieve the payout batch details.

<CodeGroup>
  ```java Java lines expandable theme={null}
  package com.paypal;

import com.paypal.http.Encoder;
import com.paypal.http.HttpResponse;
import com.paypal.http.exceptions.HttpException;
import com.paypal.http.serializer.Json;
import com.paypal.payouts.CreatePayoutResponse;
import com.paypal.payouts.Error;
import com.paypal.payouts.PayoutBatch;
import com.paypal.payouts.PayoutsGetRequest;
import org.json.JSONObject;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class GetPayoutBatch extends PayPalClient {
private static final Encoder encoder = new Encoder();
/**
_ Uses the show payout batch details API (GET - /v1/payments/payouts/<batchId>) to retrieve the payout batch details.
_ This paginated API supports retrieving a maximum of 1000 items per page.
_ Check 'links' in the response for previous and next page of URIs.
_ Add 'totalRequired' parameter to know the total number of pages available. \*
_ @param batchId - Id of a Payouts batch.
_ @return - Returns the details of the payout batch.
_ @throws IOException - Throws exception if the API call fails.
_/
public HttpResponse<PayoutBatch> getPayoutBatch(String batchId) throws IOException {
PayoutsGetRequest request = new PayoutsGetRequest(batchId)
//Optional parameters, maximum of 1000 items are retrieved by default.
.page(1)
.pageSize(10)
.totalRequired(true);
try {
HttpResponse<PayoutBatch> response = client().execute(request);
System.out.println("Response Body:");
System.out.println(new JSONObject(new Json().serialize(response.result())).toString(4));
return response;
} catch (IOException e) {
//Client side failure
System.out.println(e);
throw e;
}
}
/**
_ Driver method to execute this sample and retrieve the payout batch details.
_ To retrieve a valid Payouts batch it creates a Payouts Batch with 5 items and use that id for retrieval \*
_ @param args
_ @throws IOException when call to the api fails
\*/
public static void main(String[] args) throws IOException {
HttpResponse<CreatePayoutResponse> response = new CreatePayoutsBatch().createPayout();
new GetPayoutBatch().getPayoutBatch(response.result().batchHeader().payoutBatchId());
}
}

````

```python Python lines expandable theme={null}
# Creates a request to get the payout batch status
import json
from paypal_client import PayPalClient
from paypalpayoutssdk.payouts import PayoutsGetRequest
from create_payouts import CreatePayouts
from paypalhttp.serializers.json_serializer import Json
from paypalhttp.http_error import HttpError
from paypalhttp.encoder import Encoder

class GetPayouts(PayPalClient):
    # Retrieves a payout batch details based on the provided payout_batch_id.
    # This API is paginated and by default 1000 payout items are retrieved per page.
    # Use pagination links to navigate through all the items, add 'total_required' parameter to get the total pages.
    def get_payouts(self, payout_batch_id, debug=False):
        request = PayoutsGetRequest(payout_batch_id)
        request.page(1)
        request.page_size(10)
        request.total_required(True)
        try:
            response = self.client.execute(request)
            if debug:
                print(response.result)
                print("Status Code: ", response.status_code)
                print("Payout Batch ID: " + response.result.batch_header.payout_batch_id)
                print("Payout Batch Status: " + response.result.batch_header.batch_status)
                print("Items count: ", len(response.result.items))
                print("First item id: " + response.result.items[0].payout_item_id)
                print("Links: ")
                for link in response.result.links:
                    print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
                # To toggle print the whole body comment/uncomment the below line
                # json_data = self.object_to_json(response.result)
                # print "json_data: ", json.dumps(json_data, indent=4)
            return response
        except IOError as ioe:
            # Handles client side connection failures
            print(ioe.message)

# This is the driver function which invokes the get_payouts function to retrieve the payouts batch details.
if __name__ == "__main__":
    create_response = CreatePayouts().create_payouts(debug=True)
    batch_id = create_response.result.batch_header.payout_batch_id
    GetPayouts().get_payouts(batch_id, True)
````

</CodeGroup>

## SDK reference

- <a href="https://github.com/paypal/Payouts-Java-SDK" target="_blank" rel="noopener noreferrer">Payouts Java SDK</a>
- <a href="https://github.com/paypal/Payouts-Python-SDK" target="_blank" rel="noopener noreferrer">Payouts Python SDK</a>
