<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/account_onboarding -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Creating Applications for Merchant Accounts
slug: /graphql/integration_guides/account_onboarding/
createTime: '2025-01-16T11:27:02.314Z'
updateTime: '2025-05-01T16:13:53.935Z'
---



# Creating Applications for Merchant Accounts

The account onboarding API is only available for select merchants at this time.

If your business has hundreds of billers, franchisees, or sub-merchants, this API streamlines the process of submitting their information for underwriting. Once a biller is approved, you can process payment in its name and create payout calls to move funds.


## Requirements

In order to use this API, you must have completed the initial application process for Partners and have been set up by your PayPal Account Manager, with login credentials to the Braintree control panel. You'll also need to work with your Account Manager to configure and set up all the features you require.


## Creating an Application

To create an account application, you will specify all relevant business information for underwriting and configuration options for each payment method you will accept. A few input fields define the structure of a createBusinessAccount mutation.

Under createBusinessAccount you will find some settings for the account, such as the supported countryCode, externalId, etc. In addition, the financialInstruments and business inputs are all nested under it.

business represents the legal entity of your biller and its business details. business.stakeholders represents personas who are owners/office bearers of the business, and optional business.pointsOfContact are additional people who should be involved in the vetting and review process other than stakeholders.

financialInstruments represents the payout method for the merchant account.

All relevant inputs should be provided to the createBusinessAccount mutation. You can learn more about the fields and their respective values from our [data-dictionary](/braintree/articles/guides/application-uploader/paypal-uob-api-data-dictionary).

### Mutation
```graphql
mutation CreateBusinessAccount($input: CreateBusinessAccountInput!) {
  createBusinessAccount(input: $input) {
    accountRequest {
      id
    }
  }
}

```


### Variables,
```json
{
  "input": {
    "externalId": "Paymi-1234",
    "clientMutationId": "91527a16-2e8e-11eb-adc1-0242ac120002",
    "countryCode": "USA",
    "business": {
      "legalName": "Demo Logistics",
      "doingBusinessAs": "Demo",
      "type": "PRIVATE_CORPORATION",
      "merchantCategoryCode": "5978",
      "incorporationDetails": {
        "countryCode": "USA",
        "dateOfIncorporation": "2001-01-23",
        "province": "CA"
      },
      "stakeholders": [
        {
          "legalName": {
            "givenName": "Mary",
            "surname": "Collins"
          },
          "ownershipPercentage": 100,
          "beneficialOwner": true,
          "significantResponsibility": false,
          "position": "PARTNER",
          "emails": [
            "demo1@demoinc.com"
          ],
          "dateOfBirth": "1970-12-31",
          "addresses": [
            {
              "types": [
                "HOME_ADDRESS"
              ],
              "address": {
                "streetAddress": "2211 N First St",
                "locality": "San Jose",
                "region": "CA",
                "postalCode": "95131",
                "countryCode": "USA"
              }
            }
          ],
          "phoneNumbers": [
            {
              "type": "MOBILE",
              "phone": {
                "countryPhoneCode": "001",
                "phoneNumber": "7733441458"
              }
            }
          ],
          "identificationDocuments": [
            {
              "type": "SOCIAL_SECURITY_NUMBER",
              "identificationDocument": {
                "identificationNumber": "008713245",
                "countryCode": "USA"
              }
            }
          ]
        }
      ],
      "pointsOfContact": [
        {
          "legalName": {
            "givenName": "George",
            "surname": "Collins"
          },
          "emails": [
            "demo2@demoinc.com"
          ]
        }
      ],
      "emails": [
        {
          "email": "demo1@demoinc.com",
          "type": "CUSTOMER_SERVICE"
        }
      ],
      "website": "https://www.jayashree.com",
      "logoUrl": "http://example.com/logo.png",
      "addresses": [
        {
          "types": [
            "MAILING_ADDRESS"
          ],
          "address": {
            "streetAddress": "2211 N First St",
            "locality": "San Jose",
            "region": "CA",
            "postalCode": "95131",
            "countryCode": "USA"
          }
        }
      ],
      "phoneNumbers": [
        {
          "type": "MOBILE",
          "phone": {
            "countryPhoneCode": "1",
            "phoneNumber": "7733441458"
          }
        }
      ],
      "businessOperation": {
        "averageAnnualTransactionVolume": {
          "currencyCode": "USD",
          "value": "60000"
        },
        "averageTransactionSize": {
          "currencyCode": "USD",
          "value": "500000"
        },
        "largestTransactionSize": {
          "currencyCode": "USD",
          "value": "1000000"
        },
        "refundPolicy": "NO_REFUND_OR_EXCHANGE",
        "businessSubscriptions": {
          "percentMonthly": 0,
          "percentQuarterly": 0,
          "percentSemiAnnual": 0,
          "percentAnnual": 0
        }
      },
      "identificationDocuments": [
        {
          "type": "EMPLOYER_IDENTIFICATION_NUMBER",
          "identificationDocument": {
            "identificationNumber": "201234567",
            "countryCode": "USA"
          }
        }
      ]
    },
    "financialInstruments": {
      "bankAccounts": [
        {
          "transferType": "BANK_ACCOUNT",
          "accountNumber": "0123456789",
          "branchId": "261171480",
          "accountType": "CURRENT"
        }
      ]
    },
    "paymentProcessingOptions": {
      "achDetails": {
        "companyName": "1123456789",
        "entry": "Crestace",
        "reinitiationEnabled": true,
        "softDescriptor": "hello"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "createBusinessAccount": {
      "accountRequest": {
        "id": "bWVyY2hhbnRhY2NvdW50YXBwbGljYXRpb25fYWNjMGVkOGYtMTcxMi00YjE2\\nLTg0M2QtYjYyOTE0NmY1ODZj\\n"
      }
    }
  },
  "extensions": {
    "requestId": "e32da8a6-9313-4806-872b-7fe00ef8c073"
  }
}
```

## Error Samples

[General API error documentation](/braintree/graphql/guides/making_api_calls/#understanding-responses)


### JSON,
```json
{
  "errors": [
    {
      "message": "Business identification number is invalid.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "createBusinessAccount"
      ],
      "extensions": {
        "errorClass": "VALIDATION",
        "errorType": "user_error",
        "inputPath": [
          "input",
          "business",
          "identificationDocuments",
          0,
          "identificationDocument",
          "identificationNumber"
        ]
      }
    }
  ],
  "data": {
    "createBusinessAccount": null
  },
  "extensions": {
    "requestId": "446ac3ca-c5ea-4ecf-997d-c13ab3a9a551"
  }
}
```

### JSON,
```json
{
  "errors": [
    {
      "message": "Stakeholder date of birth must be at least 18 years ago.",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "createBusinessAccount"
      ],
      "extensions": {
        "errorClass": "VALIDATION",
        "errorType": "user_error",
        "inputPath": [
          "input",
          "business",
          "stakeholders",
          0,
          "dateOfBirth"
        ]
      }
    }
  ],
  "data": {
    "createBusinessAccount": null
  },
  "extensions": {
    "requestId": "0b54f48c-3146-429a-a5e3-5d94eff2de17"
  }
}
```
