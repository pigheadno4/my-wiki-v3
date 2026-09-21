<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/ach_direct_debit -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: ACH Direct Debit
slug: /graphql/integration_guides/ach_direct_debit/
createTime: '2025-01-16T11:25:44.965Z'
updateTime: '2026-06-15T14:27:51.775Z'
---



# ACH Direct Debit

**AVAILABILITY**
Merchants can integrate with ACH Direct Debit on the client-side using our [JavaScript v3 SDK](/braintree/docs/guides/client-sdk/setup/javascript/v3). It is currently not available in our Drop-in UI



ACH Direct Debit is a payment method that runs on the ACH (Automated Clearing House) network in the United States. It allows customers to pay for transactions by debiting directly from their bank account, as opposed to processing through a card brand.

At a high level, accepting ACH payments consists of four concepts:


- Tokenizing
- Vaulting
- Verifying
- Transacting

Depending on how you wish to verify your customer's bank account, these concepts will overlap in different ways.


## Tokenizing

Tokenizing is the process of exchanging raw payment information for a secure, single-use payment method ID.


### Tokenizing without verification

You can tokenize a bank account by collecting a customer's bank details, including account and routing numbers. However, this will not verify the bank account, and the resulting payment method will not be transactable. Before you can create a transaction, you will need to store the tokenized bank account information in your Vault, and then verify it.

To tokenize an US bank account, use the [tokenizeUsBankAccount](/braintree/graphql/reference/#Mutation--tokenizeUsBankAccount) mutation. Make sure to provide the bank account details in the [usBankAccount](/braintree/graphql/reference/#Input--TokenizeUsBankAccountInput) input field:

### Mutation
```graphql
mutation TokenizeUsBankAccount($input: TokenizeUsBankAccountInput!) {
  tokenizeUsBankAccount(input: $input) {
    paymentMethod {
      id
      usage
      createdAt
      details {
        ... on UsBankAccountDetails {
          accountholderName
          accountType
          bankName
          last4
          routingNumber
          verified
          achMandate {
            acceptedAt
            acceptanceText
          }
        }
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "usBankAccount": {
      "routingNumber": "a_routing_number",
      "accountNumber": "an_account_number",
      "accountType": "CHECKING",
      "achMandate": "I agree to give away all my money",
      "individualOwner": {
        "firstName": "Busy",
        "lastName": "Bee"
      },
      "billingAddress": {
        "streetAddress": "111 Main St",
        "extendedAddress": "#7",
        "city": "San Jose",
        "state": "CA",
        "zipCode": "94085"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "tokenizeUsBankAccount": {
      "paymentMethod": {
        "id": "id_of_payment_method",
        "usage": "SINGLE_USE",
        "createdAt": "created_at_date",
        "details": {
          "accountholderName": "Busy Bee",
          "accountType": "CHECKING",
          "bankName": "name_of_bank",
          "last4": "last_4_digits_of_an_account_number",
          "routingNumber": "a_routing_number",
          "verified": false,
          "achMandate": null
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Vaulting

Vaulting is the process of exchanging a single-use payment method ID for a multi-use payment method ID. For our ACH integration, vaulting includes the following verification options:


- [Vaulting with verification](#vaulting-with-verification)
- [Vaulting without verification](#vaulting-without-verification)


### Vaulting with verification

When vaulting a bank account, you can choose to specify a verification method. This creates a vaulted payment method and initiates a verification in a single step. If the verification fails, you can keep retrying verifications on the same payment method. A vaulted payment method will only be transactable once it has had a successful verification.

To vault an ACH payment method, use the [vaultUsBankAccount](/braintree/graphql/explorer/#:~:text=.-,vaultUsBankAccount,-Mutation) mutation. Provide the [VaultPaymentMethodInput](/braintree/graphql/reference/#Input--VaultUsBankAccountInput) input field with at least a single-use ACH [paymentMethodId](/braintree/graphql/reference/#Scalar--ID). Optionally, you can also provide a [verificationMethod](/braintree/graphql/reference/#Enum--UsBankAccountVerificationMethod) which specifies the way in which you want the given bank account verified.

### Mutation
```graphql
mutation VaultUsBankAccount($input: VaultUsBankAccountInput!) {
  vaultUsBankAccount(input: $input) {
    paymentMethod {
      id
      legacyId
      details {
        ... on UsBankAccountDetails {
          accountholderName
          accountType
          bankName
          last4
          routingNumber
          verified
          achMandate {
            acceptedAt
            acceptanceText
          }
        }
      }
    }
    verification {
      id
      status
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "verificationMerchantAccountId": "id_of_merchant_account",
    "verificationMethod": "MICRO_TRANSFERS"
  }
}
```

### Response
```json
{
  "data": {
    "vaultUsBankAccount": {
      "paymentMethod": {
        "id": "id_of_payment_method",
        "legacyId": "legacy_id_of_payment_method",
        "details": {
          "accountholderName": "Busy Bee",
          "accountType": "CHECKING",
          "bankName": "name_of_bank",
          "last4": "3210",
          "routingNumber": "a_routing_number",
          "verified": false,
          "achMandate": {
            "acceptedAt": "accepted_at_date",
            "acceptanceText": "I agree to give away all my money"
          }
        }
      },
      "verification": {
        "id": "id_of_verification",
        "status": "PENDING"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Vaulting without verification

You can also vault a bank account without specifying a verification method. This will vault the payment method as usual, but no verification will be attempted. As stated above, this payment method will not be transactable until it has a subsequent successful verification. If you prefer to perform verification on your own, the [verificationMethod](/braintree/graphql/reference/#Enum--UsBankAccountVerificationMethod) should be set as INDEPENDENT_CHECK.


## Verifying

Braintree’s ACH Direct Debit integration offers several methods for verifying that the customer owns the bank account they provide to you for payment:


- **Network check**– instantly verifies the bank account details using bank account and routing number. Personal/business information verification can be requested additionally with verification add ons.
- **Micro-transfers**– issues two separate credits of less than a dollar each to the customer’s bank account and requires the customer to confirm the exact amounts once they’re visible in the account
- **Independent check**– allows you to use your own verification method that’s not listed above and manually mark payment methods as verified

You can use any combination of these methods in order to meet your business needs. For example, one recommended flow is to use network check as an initial verification method with micro-transfers as a backup option.


### Verifying with network check

To verify an US bank account, use the [verifyUsBankAccount](/braintree/graphql/reference/#Mutation--verifyUsBankAccount) mutation.Provide the [VerifyUsBankAccountInput](/braintree/graphql/reference/#Input--VerifyUsBankAccountInput) a [paymentMethodId](/braintree/graphql/reference/#Scalar--ID) and [verificationMethod](/braintree/graphql/reference/#Enum--UsBankAccountVerificationMethod) at the minumum.

### Mutation
```graphql
mutation VerifyUsBankAccount($input: VerifyUsBankAccountInput!) {
  verifyUsBankAccount(input: $input) {
    verification {
      id
      legacyId
      status
      merchantAccountId
      createdAt
      gatewayRejectionReason
      paymentMethod {
        id
      }
      processorResponse {
        legacyCode
        message
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "verificationMethod": "NETWORK_CHECK",
    "verificationAddOns": [
      "CUSTOMER_VERIFICATION" // this is optional } }
    ]
  }
}
```

### Response
```json
{
  "data": {
    "verifyUsBankAccount": {
      "verification": {
        "id": "id_of_verification",
        "legacyId": "legacy_id_of_verification",
        "status": "VERIFIED",
        "merchantAccountId": "id_of_merchant_account",
        "createdAt": "created_at_date",
        "gatewayRejectionReason": null,
        "paymentMethod": {
          "id": "id_of_payment_method"
        },
        "processorResponse": {
          "legacyCode": "1000",
          "message": "Approved"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Verifying with Micro-deposit

If you inputed MICRO_TRANSFERS as your verificationMethod on the [vaultUsBankAccount](/braintree/graphql/explorer/#:~:text=.-,vaultUsBankAccount,-Mutation) call, you’ll need to collect the micro-deposit amounts entered by the customer in your own UI and pass them to Braintree in a separate call.

To complete the verification process for a US bank account via micro-transfer, use the [confirmMicroTransferAmounts](/braintree/graphql/reference/#Mutation--confirmMicroTransferAmounts) mutation. Provide [ConfirmMicroTransferAmountsInput](/braintree/graphql/reference/#Input--ConfirmMicroTransferAmountsInput) with a [verificationId](/braintree/graphql/reference/#Scalar--ID) and the previously collected [amountInCents](/braintree/graphql/reference/#Scalar--Int) at the minimum.

### Mutation
```graphql
mutation ConfirmMicroTransferAmounts(
  $input: ConfirmMicroTransferAmountsInput!
) {
  confirmMicroTransferAmounts(input: $input) {
    verification {
      id
      paymentMethod {
        id
        usage
      }
      merchantAccountId
      status
      processorResponse {
        message
      }
    }
    status
  }
}

```


### Variables
```json
{
  "input": {
    "verificationId": "id_of_verification",
    "amountsInCents": [
      17,
      44
    ]
  }
}
```

### Response
```json
{
  "data": {
    "confirmMicroTransferAmounts": {
      "verification": {
        "id": "id_of_verification",
        "paymentMethod": {
          "id": "id_of_payment_method",
          "usage": "MULTI_USE"
        },
        "merchantAccountId": "id_of_merchant_account",
        "status": "CONFIRMED",
        "processorResponse": {
          "message": "Approved"
        }
      }
    },
    "extensions": {
      "requestId": "a-uuid-for-the-request"
    }
  }
}
```

### Verifying with Instant verification


**NOTE**
Instant Verifications is in limited beta and is only available to pilot merchants. If you want to participate in the beta, [contact us](https://developer.paypal.com/braintree/help?issue=acceptPaymentTypes) .

Instant Verifications can instantly verify a customer's US bank account through open banking connections before initiating an ACH payment. It provides real-time confirmation that the account is valid and has sufficient funds.
**IMPORTANT**
Before starting your Graphql integration, generate a client token on your [server side](https://developer.paypal.com/braintree/docs/guides/ach/Instant-Verifications/server-side/) and make it available to your client.


#### Generate a client token

To get started, [generate a client token](https://developer.paypal.com/braintree/graphql/guides/collecting_payment_information/#requesting-a-client-token). You'll need to generate it on the server and make it accessible to your client.

If you would like to use a merchant account ID other than your default, specify the merchant_account_id when generating the client token. The merchant account ID used to create the client token must match the merchant account ID used to create the subsequent transaction.


#### Generate Instant Verification JWT

Create a JWT that contains the return and cancel URLs for the Instant Verification flow. Be sure to generate it on the server and make it accessible to your client.

GraphQL Mutation
### JSON
```json
mutation CreateBankAccountInstantVerificationJwt($input: CreateBankAccountInstantVerificationJwtInput!) {
  createBankAccountInstantVerificationJwt(input: $input) {
    jwt
  }
}
```
Input
### Response
```json
{
  "input": {
    "businessName": "Your Business Name",
    "returnUrl": "https://yoursite.com/bank_transactions?session_id=session_123",
    "cancelUrl": "https://yoursite.com/bank_transactions?session_id=session_123",
  }
}
```

#### Redirect customer to Instant Verification experience


- Decode your client token and extract your authorization fingerprint
- Use your authorization fingerprint and contextJWT to compose the experience URL
- Redirect your customer to the composed URL
- The customer will be prompted to select their bank and connect their bank account.


### Response
```json
require "net/http"
require "uri"
require "json"
require "base64"

URL = URI("https://payments.braintree-api.com/graphql")
USERNAME = "CLIENT_ID"
PASSWORD = "CLIENT_SECRET"
BUSINESS_NAME = "MERCHANT_ACCOUNT_SHORT_BUSINESS_NAME"
YOUR_DOMAIN = "MERCHANT_DOMAIN (like example.com)"
MERCHANT_ACCOUNT_ID = "MERCHANT_ACCOUNT_ID"

def post_gql_query(query, variables)
  body = { query: query, variables: variables }.to_json

  http = Net::HTTP.new(URL.host, URL.port)
  http.use_ssl = true

  request = Net::HTTP::Post.new(URL)
  request["Authorization"] = "Basic " + Base64.strict_encode64("#{USERNAME}:#{PASSWORD}")
  request["Braintree-Version"] = "2018-07-10"
  request["Content-Type"] = "application/json"
  request.body = body

  response = http.request(request)
  JSON.parse(response.body)
end

###########################################################################
##    Obtaining authorization fingerprint from client token              ##
###########################################################################
query = <<~GRAPHQL
  mutation CreateClientToken($input: CreateClientTokenInput) {
    createClientToken(input: $input) {
      clientToken
    }
  }
GRAPHQL

variables = {
  input: {
    clientToken: {
      merchantAccountId: MERCHANT_ACCOUNT_ID
    }
  }
}

client_token = post_gql_query(query, variables).dig("data", "createClientToken", "clientToken")
client_token_decoded = JSON.parse(Base64.decode64(client_token))
authorization_fingerprint = client_token_decoded["authorizationFingerprint"]

###########################################################################
##    Obtaining ContextJWT                                               ##
###########################################################################

query = <<~GRAPHQL
  mutation CreateBankAccountInstantVerificationJwt($input: CreateBankAccountInstantVerificationJwtInput!) {
    createBankAccountInstantVerificationJwt(input: $input) {
        jwt
    }
  }
GRAPHQL

variables = {
  "input": {
    "businessName": BUSINESS_NAME,
    #query params in the URLs below are provided as examples. You can define any set of params there or none at all. 
    #only domain names is expected to be whitelisted
    "returnUrl": "https://#{YOUR_DOMAIN}/payment_methods/create?session_id=session_123",
    "cancelUrl": "https://#{YOUR_DOMAIN}/payment_methods/cancel?session_id=session_123",
  }
}

jwt = post_gql_query(query, variables).dig("data", "createBankAccountInstantVerificationJwt", "jwt")

###########################################################################
##    Compose Experience URL                                             ## 
###########################################################################

experience_url = "https://www.paypal.com/openfinance/v1/bank/payment-method/create?at=#{authorization_fingerprint}&ct=#{jwt}"

### Redirect your customer to the experience_url, where they will select their bank and authorize and connect their account. 
### After successful verification, PayPal will redirect them back to the returnURL you provided, with a payment method nonce as a query parameter. 
```

#### Handle redirect from PayPal Open Finance

Handle redirect back to your website from the Instant verification experience. Upon finishing the instant verification flow, the customer will be redirected back to thereturnURL- The verified and tokenized payment info is appended as a query string parameter to thereturnURL
### Response
```json
require "net/http"

class PaymentMethodsController < ApplicationController
  URL = URI("https://payments.sandbox.braintree-api.com/graphql")
  USERNAME = "CLIENT_ID"
  PASSWORD = "CLIENT_SECRET"

  # /payment_methods/create?session_id=123&success=<serialized_success_object>
  # OR
  # /payment_methods/create?session_id=123&error=<serialized_error_object>
  def create
    session_id = params.require(:session_id)
    success = params[:success]
    error = params[:error]

    if success
      # {
      #   "type":"success",
      #   "context":{
      #     "key":"BRAINTREE",
      #     "value":"15Ladders"
      #     },
      #     "tokenizedAccounts":[
      #       {
      #         "tokenized_account":"the-nonce",
      #         "token_issuer":"BRAINTREE"
      #       }
      #     ]
      # }
      nonce = JSON.parse(Base64.decode64(success)).dig("tokenizedAccounts", 0, "tokenized_account")
      mandate_text = mandate_text(nonce)
      payment_method_id = vault_payment_method(nonce, mandate_text)

      render json: { status: "success", payment_method_id: payment_method_id, session_id: session_id }
    else
      # {
      #   "type":"error",
      #   "error":{
      #       "code":"UNPROCESSABLE_ENTITY",
      #       "message":"The requested action could not be performed.",
      #       "type":"TERMINAL_ERROR"
      #   },
      #   "context":{
      #       "key":"BRAINTREE",
      #       "value":"15Ladders"
      #   }
      # }
      render json: { error: error, session_id: session_id }, status: :unprocessable_entity
    end
  end

  # /payment_methods/cancel?session_id=123&cancel=<serialized_cancel_object>
  def cancel
    session_id = params.require(:session_id)
    # {
    #   "type": "cancel",
    #   "context": {
    #     "value": "15Ladders",
    #     "key": "BRAINTREE"
    #   }
    # }
    render json: { status: "cancelled", session_id: session_id }
  end

  private

  def vault_payment_method(nonce, mandate_text)
    query = <<~GRAPHQL
      mutation VaultBankAccount($input: VaultUsBankAccountInput!) {
        vaultUsBankAccount(input: $input) {
          paymentMethod {
            id
          }
        }
      }
    GRAPHQL

    variables = {
      "input": {
        "paymentMethodId": nonce,
        "verificationMethod": "INSTANT_VERIFICATION_ACCOUNT_VALIDATION",
        "achMandate": mandate_text,
        "achMandateAcceptedAt": Time.now.iso8601
      }
    }

    post_gql_query(query, variables).dig("data", "vaultUsBankAccount", "paymentMethod", "id")
  end

  def mandate_text(nonce)
    query = <<~GRAPHQL
      query GetPaymentMethod($id: ID!) {
        node(id: $id) {
          ...on PaymentMethod {
            id
            details {
              ... on UsBankAccountDetails {
                accountholderName,
                last4,
                routingNumber
              }
            }
          }
        }
      }
    GRAPHQL

    variables = {
        "id": nonce
    }

    account_holder_name, last_4, routing_number = post_gql_query(query, variables).dig("data", "node", "details").values

    "Here goes the mandate text for #{account_holder_name} with account ending in #{last_4} and routing number #{routing_number}"
  end

  def post_gql_query(query, variables)
    body = { query: query, variables: variables }.to_json

    http = Net::HTTP.new(URL.host, URL.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(URL)
    request["Authorization"] = "Basic " + Base64.strict_encode64("#{USERNAME}:#{PASSWORD}")
    request["Braintree-Version"] = "2018-07-10"
    request["Content-Type"] = "application/json"
    request.body = body

    response = http.request(request)
    JSON.parse(response.body)
  end
end
```

#### Retrieve Bank Details for ACH Mandate

For all ACH transactions, you are required to collect a mandate or “proof of authorization” from the customer to prove that you have their explicit permission to debit their bank account.
- Pass the payment method ID received as a query string parameter in thereturnURLto retrieve the customer’s bank details and display an accurate ACH mandate
- [Show the required authorization language](https://developer.paypal.com/braintree/docs/guides/ach/client-side/javascript/v3/#show-required-authorization-language)for your use-case in your checkout flow after user returns from Instant Verification experience
- Pass text asmandateText(required) to Braintree on[v[aultUsBankAccount](https://developer.paypal.com/braintree/graphql/reference/#Mutation--vaultUsBankAccount)](https://developer.paypal.com/braintree/graphql/reference/#Mutation--vaultUsBankAccount)or[chargeUsBankAccount](https://developer.paypal.com/braintree/graphql/reference/#Mutation--chargeUsBankAccount)calls.

**Query**
### Response
```json
query PaymentMethod {
  node(id: "id_of_payment_method") {
    id
    ... on PaymentMethod {
      id
      legacyId
      usage
      createdAt
      details {
        __typename
        accountholderName
        accountType
        ownershipType
        bankName
        last4
        routingNumber
        verified
      }
    }
  }
}
```
**Response**
### Response
```json
{
  "data": {
    "node": {
      "id": "id_of_payment_method",
      "legacyId": "legacy_id_of_payment_method",
      "usage": "usage_of_payment_method",
      "createdAt": "created_at_date",
      "details" => {
        "__typename" => "UsBankAccountDetails",
        "accountholderName" => "Cris amountsimulator",
        "accountType" => "CHECKING",
        "ownershipType" => "PERSONAL",
        "bankName" => "OCALA COMMUNITY CREDIT UNION",
        "last4" => "7779",
        "routingNumber" => "263181151",
        "verified" => true
       },
      "extensions": {
        "requestId": "a-uuid-for-the-request"
      }
  }
}
```

### Checking verification status

To check for successful verification, you should examine the message field of the [VerificationProcessorResponse](/braintree/graphql/reference/#Object--VerificationProcessorResponse) returned by [verifyUsBankAccount](/braintree/graphql/reference/#Mutation--verifyUsBankAccount) and look for "Approved". If verification has failed, some other message will be returned, such as "Processor Network Unavailable - Try Again".

You can also request additionalInformation under processorResponse and depending on the type of processor failure, it will return details about the error. For example, it may say "Invalid routing number" or "Invalid account type".


### Looking up individual verification status

This step is required when using the micro-transfers method.After successfully confirming micro-deposit amounts, the bank account may be ready for transacting, still waiting for transfers to settle, or may eventually report that settlement failed. You can periodically check the state of a verification with its id like so:

### Query
```graphql
query ($input: VerificationSearchInput!) {
  search {
    verifications(input: $input) {
      edges {
        node {
          id
          status
        }
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "id": {
      "is": "id_of_verification"
    }
  }
}
```

### Response
```json
{
  "data": {
    "search": {
      "verifications": {
        "edges": [
          {
            "node": {
              "id": "id_of_verification",
              "status": "VERIFIED"
            }
          }
        ]
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Retrying verification

Sometimes verification will fail. You can retry verification by sending the the previous request again or using the previous request with a different [verificationMethod](/braintree/graphql/reference/#Enum--UsBankAccountVerificationMethod). For example, if NETWORKCHECK was used and it failed with the message "No Data Found - Try Another Verification Method", you can retry with MICRO_TRANSFERS as an alternative.


## Creating Transactions


### From multi-use payment methods

This step is applicable to all verification methods.You will receive a multi-use payment method id when you successfully call [vaultUsBankAccount](/braintree/graphql/reference/#Mutation--vaultUsBankAccount) using a single-use payment method created from [tokenizeUsBankAccount](/braintree/graphql/reference/#Mutation--tokenizeUsBankAccount). You can use the multi-use payment method id to charge the account using [chargeUsBankAccount](/braintree/graphql/reference/#Mutation--chargeUsBankAccount) once the payment method is verified.

[Collect device data](/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v3/#collecting-device-data) from the client and include the collected client device data via the deviceData parameter inside riskData. Doing so will help reduce decline rates. Below includes an example call using device data:

### Mutation
```graphql
mutation ChargeUsBankAccount($input: ChargeUsBankAccountInput!) {
  chargeUsBankAccount(input: $input) {
    transaction {
      id
      amount {
        value
      }
      paymentMethodSnapshot {
        ... on UsBankAccountDetails {
          accountholderName
          accountType
          verified
        }
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "paymentMethodId": "id_of_payment_method",
    "transaction": {
      "amount": "10.00",
      "orderId": "id_of_order",
      "riskData": {
        "customerBrowser": "web_browser_type",
        "customerIp": "ip_address",
        "deviceData": "device_type"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "chargeUsBankAccount": {
      "transaction": {
        "id": "id_of_transaction",
        "amount": {
          "value": "10.00"
        },
        "paymentMethodSnapshot": {
          "accountholderName": "Busy Bee",
          "accountType": "CHECKING",
          "verified": false
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Common errors

Note that each tokenized single-use payment method ID can only be vaulted once. If you attempt to vault the same single-use payment method ID more than once, you will get the following error.


### JSON
```json
{
  "errors": [
    {
      "message": "Cannot use a single-use payment method more than once.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "vaultUsBankAccount"
      ],
      "extensions": {
        "errorClass": "VALIDATION",
        "errorType": "user_error",
        "inputPath": [
          "input",
          "paymentMethodId"
        ],
        "legacyCode": "93107"
      }
    }
  ],
  "data": {
    "vaultUsBankAccount": null
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If you do not provide [verificationMethod](/braintree/graphql/reference/#Enum--UsBankAccountVerificationMethod) in the inputs, you will get the following error.


### JSON
```json
{
  "errors": [
    {
      "message": "Variable 'input' has an invalid value: Field 'verificationMethod' has coerced Null value for NonNull type 'UsBankAccountVerificationMethod!'",
      "locations": [
        {
          "line": 1,
          "column": 29
        }
      ]
    }
  ],
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
