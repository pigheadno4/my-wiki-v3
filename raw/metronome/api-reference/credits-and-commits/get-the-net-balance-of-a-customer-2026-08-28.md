<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/get-the-net-balance-of-a-customer.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the net balance of a customer

> Retrieve the combined current balance across any grouping of credits and commits for a customer in a single API call.
- Display real-time available balance to customers in billing dashboards
- Build finance dashboards showing credit utilization across customer segments
- Validate expected vs. actual balance during billing reconciliation

### Key response fields:
- `balance`: The combined net balance available to use at this moment across all matching commits and credits
- `credit_type_id`: The credit type (fiat or custom pricing unit) the balance is denominated in

### Filtering options:
Balance filters allow you to scope the calculation to specific subsets of commits and credits. When using multiple filter objects, they are OR'd together — if a commit or credit matches any filter, it's included in the net balance. Within a single filter object, all specified conditions are AND'd together.
- **Balance types**: Include any combination of `PREPAID_COMMIT`, `POSTPAID_COMMIT`, and `CREDIT` (e.g., `["PREPAID_COMMIT", "CREDIT"]` to exclude postpaid commits). If not specified, all balance types are included.
- **Specific IDs**: Target exact commit or credit IDs for precise balance queries
- **Custom fields**: Filter by custom field key-value pairs; when multiple pairs are provided, commits must match all of them

**Example**: To get the balance of all free-trial credits OR all signup-promotion commits, you'd pass two filter objects — one filtering for CREDIT with custom field campaign: free-trial, and another filtering for PREPAID_COMMIT with custom field campaign: signup-promotion.

### Usage guidelines:
- **Balance ledger details**: Use the [listBalances](https://docs.metronome.com/api-reference/credits-and-commits/list-balances) endpoint instead to understand detailed ledger drawdowns for each individual balance
- **Draft invoice handling**: Use `invoice_inclusion_mode` to control whether pending draft invoice deductions are included (`FINALIZED_AND_DRAFT`, the default) or excluded (`FINALIZED`) from the balance calculation
- **Account hierarchies**: When querying a child customer, shared commits from parent contracts are not included — query the parent customer directly to see shared commit balances
- **Negative balances**: Manual ledger entries can cause negative segment balances; these are treated as zero when calculating the net balance
- **Credit types**: If `credit_type_id` is not specified, the balance defaults to USD (cents)




## OpenAPI

````yaml /openapi.json post /v1/contracts/customerBalances/getNetBalance
openapi: 3.0.1
info:
  title: Metronome
  version: 1.0.0
servers:
  - url: https://api.metronome.com
    description: Production server
security:
  - bearerAuth: []
tags:
  - name: Customers
    description: >-
      [Customers](https://docs.metronome.com/provisioning/create-customers/) in
      Metronome represent your users for all billing and reporting. Use these
      endpoints to create, retrieve, update, and archive customers and their
      billing configuration.
  - name: Billable metrics
    description: >-
      [Billable
      metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics)
      in Metronome represent the various consumption components that Metronome
      meters and aggregates.
  - name: Usage
    description: >-
      [Usage
      events](https://docs.metronome.com/connecting-metronome/send-usage-data/)
      are the basis for billable metrics. Use these endpoints to send usage
      events to Metronome and retrieve aggregated event data.
  - name: Products
    description: Products are the items that customers purchase.
  - name: Rate cards
    description: Rate cards are used to define default pricing for products.
  - name: Contracts
    description: >-
      A contract defines a customer’s products, pricing, discounts, commitments,
      and more. Use these endpoints to create and update contracts data.
  - name: Credits and commits
    description: Credits and commits are used to manage customer balances.
  - name: Invoices
    description: >-
      [Invoices](https://docs.metronome.com/invoicing/) reflect how much a
      customer spent during a period, which is the basis for billing. Metronome
      automatically generates invoices based upon your pricing, packaging, and
      usage events. Use these endpoints to retrieve invoices.
  - name: Alerts
    description: >-
      [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor
      customer spending, balances, and other billing factors. Use these
      endpoints to create, retrieve, and archive customer alerts. To view sample
      alert payloads by alert type, navigate
      [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
  - name: Custom fields
    description: >-
      [Custom fields](https://docs.metronome.com/integrations/custom-fields/)
      enable adding additional data to Metronome entities. Use these endpoints
      to create, retrieve, update, and delete custom fields.
  - name: Security
    description: >-
      [Security](https://docs.metronome.com/developer-resources/security/)
      endpoints allow you to retrieve security-related data.
  - name: Settings
    description: >-
      Use these endpoints to configure a billing API key, a webhook secret, or
      invoice finalization behavior.
  - name: Named schedules
    description: >-
      Named schedules are used for storing custom data that can change over
      time. Named schedules are often used in custom pricing logic.
paths:
  /v1/contracts/customerBalances/getNetBalance:
    post:
      tags:
        - Credits and commits
      summary: Get the net balance of a customer
      description: >
        Retrieve the combined current balance across any grouping of credits and
        commits for a customer in a single API call.

        - Display real-time available balance to customers in billing dashboards

        - Build finance dashboards showing credit utilization across customer
        segments

        - Validate expected vs. actual balance during billing reconciliation


        ### Key response fields:

        - `balance`: The combined net balance available to use at this moment
        across all matching commits and credits

        - `credit_type_id`: The credit type (fiat or custom pricing unit) the
        balance is denominated in


        ### Filtering options:

        Balance filters allow you to scope the calculation to specific subsets
        of commits and credits. When using multiple filter objects, they are
        OR'd together — if a commit or credit matches any filter, it's included
        in the net balance. Within a single filter object, all specified
        conditions are AND'd together.

        - **Balance types**: Include any combination of `PREPAID_COMMIT`,
        `POSTPAID_COMMIT`, and `CREDIT` (e.g., `["PREPAID_COMMIT", "CREDIT"]` to
        exclude postpaid commits). If not specified, all balance types are
        included.

        - **Specific IDs**: Target exact commit or credit IDs for precise
        balance queries

        - **Custom fields**: Filter by custom field key-value pairs; when
        multiple pairs are provided, commits must match all of them


        **Example**: To get the balance of all free-trial credits OR all
        signup-promotion commits, you'd pass two filter objects — one filtering
        for CREDIT with custom field campaign: free-trial, and another filtering
        for PREPAID_COMMIT with custom field campaign: signup-promotion.


        ### Usage guidelines:

        - **Balance ledger details**: Use the
        [listBalances](https://docs.metronome.com/api-reference/credits-and-commits/list-balances)
        endpoint instead to understand detailed ledger drawdowns for each
        individual balance

        - **Draft invoice handling**: Use `invoice_inclusion_mode` to control
        whether pending draft invoice deductions are included
        (`FINALIZED_AND_DRAFT`, the default) or excluded (`FINALIZED`) from the
        balance calculation

        - **Account hierarchies**: When querying a child customer, shared
        commits from parent contracts are not included — query the parent
        customer directly to see shared commit balances

        - **Negative balances**: Manual ledger entries can cause negative
        segment balances; these are treated as zero when calculating the net
        balance

        - **Credit types**: If `credit_type_id` is not specified, the balance
        defaults to USD (cents)
      operationId: getNetBalance-v1
      requestBody:
        description: Get the combined net balance for any grouping of credits and commits.
        content:
          application/json:
            schema:
              type: object
              required:
                - customer_id
              properties:
                customer_id:
                  type: string
                  format: uuid
                  description: The ID of the customer.
                credit_type_id:
                  type: string
                  format: uuid
                  description: >-
                    The ID of the credit type (can be fiat or a custom pricing
                    unit) to get the balance for. Defaults to USD (cents) if not
                    specified.
                access_type:
                  x-mint:
                    groups:
                      - ff:create-quantity-based-commits
                  x-stainless-skip: true
                  type: string
                  enum:
                    - SPEND
                    - spend
                    - QUANTITY
                    - quantity
                  description: >-
                    Filters balances by how they are drawn down. Defaults to
                    `SPEND`. If set to `QUANTITY`, `credit_type_id` must not be
                    provided.
                filters:
                  type: array
                  description: >-
                    Balance filters are OR'd together, so if a given commit or
                    credit matches any of the filters, it will be included in
                    the net balance.
                  items:
                    $ref: '#/components/schemas/BalanceFilter'
                invoice_inclusion_mode:
                  type: string
                  description: >-
                    Controls which invoices are considered when calculating the
                    remaining balance. `FINALIZED` considers only deductions
                    from finalized invoices. `FINALIZED_AND_DRAFT` also includes
                    deductions from pending draft invoices.
                  enum:
                    - FINALIZED
                    - FINALIZED_AND_DRAFT
                  default: FINALIZED_AND_DRAFT
            example:
              customer_id: 13117714-3f05-48e5-a6e9-a66093f13b4d
              credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              filters:
                - balance_types:
                    - CREDIT
                  custom_fields:
                    campaign: free-trial
                - balance_types:
                    - PREPAID_COMMIT
                    - POSTPAID_COMMIT
                  custom_fields:
                    campaign: signup-promotion
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                properties:
                  data:
                    type: object
                    required:
                      - balance
                      - credit_type_id
                    properties:
                      balance:
                        type: number
                        description: >-
                          The combined net balance that the customer has access
                          to use at this moment across all pertinent commits and
                          credits.
                      credit_type_id:
                        type: string
                        format: uuid
                        description: >-
                          The ID of the credit type (can be fiat or a custom
                          pricing unit) that the balance is for.
                example:
                  data:
                    balance: 123.45
                    credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    BalanceFilter:
      type: object
      properties:
        balance_types:
          type: array
          description: The balance type to filter by.
          items:
            type: string
            enum:
              - PREPAID_COMMIT
              - POSTPAID_COMMIT
              - CREDIT
        ids:
          type: array
          items:
            type: string
            format: uuid
          description: Specific IDs to compute balance across.
        custom_fields:
          type: object
          description: >-
            Custom fields to compute balance across. Must match all custom
            fields
          additionalProperties:
            type: string
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
