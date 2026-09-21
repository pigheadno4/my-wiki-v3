<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/financing_options -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Brazil Billing Agreement with Installments
slug: /graphql/integration_guides/financing_options/
createTime: '2025-01-16T11:26:55.610Z'
updateTime: '2025-05-01T16:29:20.170Z'
---



# Brazil Billing Agreement with Installments Overview

This feature is only available to merchants domiciled in Brazil.

Consumers using credit cards in Brazil are accustomed to seeing installment options to pay for some or all of the items in their shopping cart. Now, Braintree will support Billing Agreement with Installments in Brazil. Merchants will integrate using the Braintree GraphQL API to offer [Pay with PayPal](/braintree/articles/guides/payment-methods/paypal/overview) to their customers. Server SDKs will be supported in the future.


## Consumer Experience


- From the merchant checkout page the consumer clicks thePay with PayPalbutton and is directed to Hermes flow where the consumer will set up the billing agreement and be able to select/change their funding instrument.
- On the backend, merchant server will call PayPal CalculatedFinancingOptions API (through Braintree GraphQL API) to get installment options.
- Consumer will be redirected back to the merchant checkout page and will see their billing agreement and the option to select installments on the checkout page.
- Consumer will then be able to Checkout with their billing agreement and a selected installment option.


## Checkout with Installments

To pay in installments follow the steps below.


### 1. Calculate Financing Options

In order to calculate financing options with paypalFinancingOptions, you'll need a payment method's ID, information about the transaction, the currency code, and the country code.

### Query
```graphql
query PayPalFinancingOptions($input: PayPalFinancingOptionsInput!) {
  paypalFinancingOptions(input: $input) {
    financingOptions {
      creditProductIdentifier
      qualifyingFinancingOptions {
        apr
        nominalRate
        term
        intervalDuration
        countryCode
        creditType
        minimumAmount {
          value
          currencyIsoCode
          currencyCode
        }
        monthlyInterestRate
        periodicPayment {
          value
          currencyIsoCode
          currencyCode
        }
        monthlyPayment {
          value
          currencyIsoCode
          currencyCode
        }
        discountAmount {
          value
          currencyIsoCode
          currencyCode
        }
        discountPercentage
        totalInterest {
          value
          currencyIsoCode
          currencyCode
        }
        totalCost {
          value
          currencyIsoCode
          currencyCode
        }
        paypalSubsidized
      }
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "paymentMethodId": "vaulted_payment_method_id",
    "amount": {
      "value": "10.00",
      "currencyCode": "BRL"
    },
    "countryCode": "BR"
  }
}
```

### Response
```json
{
  "paypalFinancingOptions": {
    "financingOptions": [
      {
        "creditProductIdentifier": "CREDIT_CARD_INSTALLMENTS_BR",
        "qualifyingFinancingOptions": [
          {
            "apr": "10",
            "nominalRate": "15.5",
            "term": 1,
            "intervalDuration": "P1M",
            "countryCode": "BR",
            "creditType": "INSTALLMENT",
            "minimumAmount": {
              "value": "10.00",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "monthlyInterestRate": "10.00",
            "periodicPayment": {
              "value": "10.00",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "monthlyPayment": {
              "value": "10.00",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "discountAmount": {
              "value": "25.50",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "discountPercentage": "10",
            "totalInterest": {
              "value": "10.00",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "totalCost": {
              "value": "10.00",
              "currencyIsoCode": "BRL",
              "currencyCode": "BRL"
            },
            "paypalSubsidized": false
          }
        ]
      }
    ]
  }
}
```

### 2. Charge PayPal Account with Selected Financing Option

In order to charge a PayPal account with chargePayPalAccount, you'll need the payment method's ID, information about the transaction you'd like to create using it, and a financing option.

### Mutation
```graphql
mutation ChargePayPalAccount($input: ChargePayPalAccountInput!) {
  chargePayPalAccount(input: $input) {
    transaction {
      status
      paymentMethodSnapshot {
        __typename
        ... on PayPalTransactionDetails {
          selectedFinancingOption {
            term
            monthlyPayment {
              value
              currencyIsoCode
              currencyCode
            }
            discountPercentage
            discountAmount {
              value
              currencyIsoCode
              currencyCode
            }
          }
        }
      }
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "paymentMethodId": "vaulted_payment_method_id",
    "transaction": {
      "amount": "120.00"
    },
    "options": {
      "selectedFinancingOption": {
        "term": 6,
        "currencyCode": "BRL",
        "monthlyPayment": "20.00",
        "discountPercentage": "4.59",
        "discountAmount": "5.00"
      }
    }
  }
}
```

#### Response

A successful charge results in a transaction with the [SETTLING](/braintree/docs/reference/general/statuses/#settling), [SUBMITTED_FOR_SETTLEMENT](/braintree/docs/reference/general/statuses/#submitted-for-settlement), or [SETTLED](/braintree/docs/reference/general/statuses/#settled) state.


### Response
```json
{
  "chargePayPalAccount": {
    "transaction": {
      "status": "SETTLING",
      "paymentMethodSnapshot": {
        "__typename": "PayPalTransactionDetails",
        "selectedFinancingOption": {
          "term": 6,
          "monthlyPayment": {
            "value": "20.00",
            "currencyIsoCode": "BRL",
            "currencyCode": "BRL"
          },
          "discountPercentage": "4.59",
          "discountAmount": {
            "value": "5.00",
            "currencyIsoCode": "BRL",
            "currencyCode": "BRL"
          }
        }
      }
    }
  }
}
```
