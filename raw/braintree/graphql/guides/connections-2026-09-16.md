<!-- Source URL: https://developer.paypal.com/braintree/graphql/guides/connections -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Connections and Pagination
slug: /graphql/guides/connections/
createTime: '2025-01-16T11:26:02.784Z'
updateTime: '2025-12-17T00:44:17.536Z'
---



# Pagination and Relay Connections

If you've used connections from other GraphQL APIs, the Braintree API's implementation will be familiar. It adheres to the [Relay specification](https://relay.dev/graphql/connections.htm).

A connection is a collection of objects (called edges ) and the information needed to paginate through them (called pageInfo ). When you request a connection field, you can specify how many results you want and where to start in the list.

Connections are used in the API in places where there can be an unbounded number of results, for example [search](/braintree/graphql/guides/search). Other examples include the transactions and payment methods attached to a customer or the verifications attached to a payment method.


## The Contents of a Connection

For every type that can be paginated ( Transaction, Customer, etc.) there is a corresponding *Connection type ( TransactionConnection, CustomerConnection, etc.). They have this structure:


### GraphQL
```graphql
genericConnection {
  edges {
    node {
      # the objects themselves
    }
    cursor # a pointer to the current edge's location in the list
  }
  pageInfo {
    # information about the current page of results
  }
}
```
and requesting a connection field returns something like this (this structure may be nested in a larger JSON object):


### JSON
```json

        {
  "genericConnection": {
    "edges": [
      {
        "node": {
          "id": "id-for-first-object-in-page",
          // ...other requested fields for this object type
        },
        "cursor": "opaque-string-for-first-object"
      },
      {
        "node": {
          "id": "id-for-second-object-in-page",
          // ...other requested fields for this object type
        },
        "cursor": "opaque-string-for-second-object"
      },
      # ...additional elements in page
    ],
    "pageInfo": {
      "hasNextPage": true
    }
  }
}
    
```
The edges list makes up a page's worth of objects; the list of edges is one page of results. Each edge holds a single element in the results, and contains a node (the object itself) and a cursor, which is an opaque string denoting that edge's place in the larger set of results.

You can think of "node" here as meaning the same thing as it does in a [node query](/braintree/graphql/guides/node_query) : a fetchable object with a unique ID. However, unlike the node query, in most cases, the field will specify what type its node objects are.

The hasNextPage boolean tells you whether there are more results—more edges—in the connection than were returned in the current page.


## Simple Use

If you don't care about moving through the full list of results, and only want a subset, you can omit the optional fields used for pagination.


### GraphQL
```graphql
query Search($txnCriteria: TransactionSearchInput!) {
  search {
    transactions(input: $txnCriteria) {
      edges {
        node {
          id
          # ...all desired transaction fields
        }
      }
    }
  }
}

```
That query would yield the following result:


### Response
```json
{
  "data": {
    "search": {
      "transactions": {
        "edges": [
          {
            "node": {
              "id": "transaction-id"
              // ...all desired transaction fields
            },
            "node": {
              "id": "another-transation-id"
              // ...all desired transaction fields
            }
            // up to forty-nine more transactions meeting the search criteria
          }
        ]
      }
    }
  }
}

```

## Complex Connections

When requesting a connection field, you can provide arguments to more finely control the results you get back.

You can slice, and request only a certain number of items:


### GraphQL
```graphql
paymentMethods(first: 5) {
  edges {
    node
  }
}
    
```
You can paginate, and request items only after a certain point:


### GraphQL
```graphql
paymentMethods(after: "opaque-cursor-from-an-edge-on-a-previous-page") {
  edges {
    node
    cursor
  }
}
    
```
You can do both, and select the next x items after a certain point:


### GraphQL
```graphql
paymentMethods(first: 20, after: "opaque-cursor-from-an-edge-on-a-previous-page") {
  edges {
    node
    cursor
  }
  pageInfo {
    hasNextPage
  }
}
    
```
For some connections, you can also add in criteria determining which items are selected and what order they will appear in.


### Pagination

Here is a complete example of searching with pagination:


### GraphQL
```graphql
query InitialSearch($txnCriteria: TransactionSearchInput!) {
  search {
    transactions(input: $txnCriteria, first: 20) {
      edges {
        node {
          id
        }
        cursor
      }
      pageInfo {
        hasNextPage
      }
    }
  }
}

```
This query will return the twenty most recently created transactions that meet the input search criteria as nodes, each wrapped in an edge, with a cursor marking its place in the full result set. The pageInfo field will indicate whether there are more than twenty transactions that meet your search criteria.


### Response
```json
{
  "data": {
    "search": {
      "transactions": {
        "edges": [
          // ...19 prior nodes...
          {
            "node": {
              "id": "transaction-id-for-last-result-in-list"
            },
            "cursor": "cursor-for-last-transaction-in-list"
          }
        ],
        "pageInfo": {
          "hasNextPage": true
        }
      }
    }
  }
}

```
In order to obtain the next page in the results—or to get any new set of subsequent results after a particular node in the list—perform a second search, adding the appropriate cursor to your input.


### GraphQL
```graphql
query SecondSearch($txnCriteria: TransactionSearchInput!) {
  search {
    transactions(input:$txnCriteria, first: 20, after: "cursor-for-last-transaction-in-list") {
      # ...
    }
  }
}
    
```
This will return twenty different transactions that meet your search criteria: the next twenty created subsequent to the transaction indicated by "cursor-for-last-transaction-in-list".

When hasNextPage is false, then there are no more objects that meet your search criteria, and the last element in the current list is the oldest object in your result set.


### More on Relay

For more information on the Relay specifications, including connections, edges, and cursors, here are some good resources:


- [Learning GraphQL: Pagination](https://graphql.org/learn/pagination)
- [Relay Connections Guide](https://relay.dev/docs/guides/graphql-server-specification/#connections)
- [Relay Cursor Connections Specification](https://relay.dev/graphql/connections.htm)
- [Understanding pagination: REST, GraphQL, and Relay](https://www.apollographql.com/blog/understanding-pagination-rest-graphql-and-relay)

