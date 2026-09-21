<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/customers -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Customers Basics Guide
slug: /graphql/guides/customers/
createTime: '2025-01-16T11:25:58.057Z'
updateTime: '2025-04-28T16:03:12.194Z'
---



# Customers

Customer is a type of object that can be used to store and organize payment methods. A single customer can have multiple payment methods. This guide will demonstrate how to create, update, delete, and search for a customer object.


## Create

You can create a customer object using the [createCustomer](/braintree/graphql/reference/#Mutation--createCustomer) mutation. This mutation has no required inputs, so you can choose which inputs are important for your needs.


### With customer input

You can provide customer input that includes fields like firstName, lastName, company and more to create a customer with the characteristics that you pass in. For a full list of customer input options, check the reference for [CustomerInput](/braintree/graphql/reference/#input_object--customerinput).

### Mutation
```graphql
mutation CreateCustomer($input: CreateCustomerInput!) {
  createCustomer(input: $input) {
    customer {
      id
      legacyId
      firstName
      lastName
      company
    }
  }
}

```


### Variables
```json
{
  "input": {
    "customer": {
      "firstName": "Luke",
      "lastName": "Skywalker",
      "company": "Rebellion"
    }
  }
}
```

### Response
```json
{
  "data": {
    "createCustomer": {
      "customer": {
        "id": "id_of_customer",
        "legacyId": "legacy_id_of_customer",
        "firstName": "Luke",
        "lastName": "Skywalker",
        "company": "Rebellion"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Blank customer

Since the createCustomer mutation doesn't have any required inputs, you can create a blank customer and add fields to it later.

### Mutation
```graphql
mutation CreateCustomer($input: CreateCustomerInput!) {
  createCustomer(input: $input) {
    customer {
      id
      legacyId
      firstName
      lastName
      company
    }
  }
}

```


### Variables
```json
{
  "input": {}
}
```

### Response
```json
{
  "data": {
    "createCustomer": {
      "customer": {
        "id": "id_of_customer",
        "legacyId": "legacy_id_of_customer",
        "firstName": null,
        "lastName": null,
        "company": null
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

### Use custom fields

You can use custom fields to store additional data about your customers. You'll need to [configure your custom fields in the Control Panel](/braintree/articles/control-panel/custom-fields) to use them via the API.

### Mutation
```graphql
mutation CreateCustomer($input: CreateCustomerInput!) {
  createCustomer(input: $input) {
    customer {
      id
      legacyId
      firstName
      lastName
      company
      customFields {
        name
        value
      }
    }
  }
}

```


### Variables
```json
{
  "input": {
    "customer": {
      "firstName": "Luke",
      "lastName": "Skywalker",
      "company": "Rebellion",
      "customFields": {
        "name": "space_ship",
        "value": "X-wing"
      }
    }
  }
}
```

### Response
```json
{
  "data": {
    "createCustomer": {
      "customer": {
        "id": "id_of_customer",
        "legacyId": "legacy_id_of_customer",
        "firstName": "Luke",
        "lastName": "Skywalker",
        "company": "Rebellion",
        "customFields": {
          "name": "space_ship",
          "value": "X-wing"
        }
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Update

You can update a customer's information using the [updateCustomer](/braintree/graphql/reference/#Mutation--updateCustomer) mutation. This mutation requires a customerId as input.

### Mutation
```graphql
mutation UpdateCustomer($input: UpdateCustomerInput!) {
  updateCustomer(input: $input) {
    customer {
      id
      legacyId
      firstName
      lastName
      company
    }
  }
}

```


### Variables
```json
{
  "input": {
    "customerId": "id_of_customer",
    "customer": {
      "company": "Jedi"
    }
  }
}
```

### Response
```json
{
  "data": {
    "updateCustomer": {
      "customer": {
        "id": "id_of_customer",
        "legacyId": "legacy_id_of_customer",
        "firstName": "Luke",
        "lastName": "Skywalker",
        "company": "Jedi"
      }
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Delete

You can delete a customer using the [deleteCustomer](/braintree/graphql/reference/#Mutation--deleteCustomer) mutation. This mutation requires a customerId as input. Deleting a customer will break the association between the customer and any of their transactions.

The customer will not be deleted if the customer has existing payment methods. Before deleting a customer,[delete their payment methods from your Vault](/braintree/graphql/reference/#Mutation--deletePaymentMethodFromVault).### Mutation
```graphql
mutation DeleteCustomer($input: DeleteCustomerInput!) {
  deleteCustomer(input: $input) {
    clientMutationId
  }
}

```


### Variables
```json
{
  "input": {
    "customerId": "id_of_customer"
  }
}
```

### Response
```json
{
  "data": {
    "deleteCustomer": {
      "clientMutationId": "id_of_client_mutation"
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```
If the customer with the inputted ID can't be found, the mutation will raise a NOT_FOUND error.


## Search

You can search for customers based on their characteristics using the [search](/braintree/graphql/reference/#Query--search) mutation. For a list of characteristics you can search on, see the reference for [CustomerSearchInput](/braintree/graphql/reference/#input_object--customersearchinput).

### Mutation
```graphql
query Search($input: CustomerSearchInput!) {
  search {
    customers(input: $input) {
      edges {
        node {
          id
          legacyId
          firstName
          lastName
          company
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
    "company": {
      "is": "Rebellion"
    }
  }
}
```

### Response
```json
{
  "data": {
    "search": {
      "customers": {
        "edges": [
          {
            "node": {
              "id": "id_of_customer",
              "legacyId": "legacy_id_of_customer",
              "firstName": "Han",
              "lastName": "Solo",
              "company": "Rebellion"
            }
          },
          {
            "node": {
              "id": "id_of_customer",
              "legacyId": "legacy_id_of_customer",
              "firstName": "Leia",
              "lastName": "Organa",
              "company": "Rebellion"
            }
          },
          {
            "node": {
              "id": "id_of_customer",
              "legacyId": "legacy_id_of_customer",
              "firstName": "Luke",
              "lastName": "Skywalker",
              "company": "Rebellion"
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
If you know the id of the customer you are searching for and want to get their characteristics, then you can use the [node](/braintree/graphql/reference/#Query--node) query.

### Mutation
```graphql
query GetCustomer {
  node(id: "id_of_customer") {
    ... on Customer {
      id
      legacyId
      firstName
      lastName
      company
    }
  }
}

```


### Response
```json
{
  "data": {
    "node": {
      "id": "id_of_customer",
      "legacyId": "legacy_id_of_customer",
      "firstName": "Leia",
      "lastName": "Organa",
      "company": "Rebellion"
    }
  },
  "extensions": {
    "requestId": "a-uuid-for-the-request"
  }
}
```

## Errors

If you run into errors while working with customer objects, check the [customer error codes page](/braintree/docs/reference/general/validation-errors/all#customer) to see what errors you received and why you may be receiving them.

