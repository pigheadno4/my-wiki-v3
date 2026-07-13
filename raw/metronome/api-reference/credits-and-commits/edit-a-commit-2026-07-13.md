<!-- Source URL: https://docs.metronome.com/api-reference/credits-and-commits/edit-a-commit.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit a commit

> Edit specific details for a contract-level or customer-level commit. Use this endpoint to modify individual commit access schedules, invoice schedules, applicable products, invoicing contracts, or other fields. 

### Usage guidelines:
- As with all edits in Metronome, draft invoices will reflect the edit immediately, while finalized invoices are untouched unless voided and regenerated.
- If a commit's invoice schedule item is associated with a finalized invoice, you cannot remove or update the invoice schedule item.
- If a commit's invoice schedule item is associated with a voided invoice, you cannot remove the invoice schedule item.
- You cannot remove an commit access schedule segment that was applied to a finalized invoice. You can void the invoice beforehand and then remove the access schedule segment.




## OpenAPI

````yaml /openapi.json post /v2/contracts/commits/edit
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
  /v2/contracts/commits/edit:
    post:
      tags:
        - Credits and commits
      summary: Edit a commit
      description: >
        Edit specific details for a contract-level or customer-level commit. Use
        this endpoint to modify individual commit access schedules, invoice
        schedules, applicable products, invoicing contracts, or other fields. 


        ### Usage guidelines:

        - As with all edits in Metronome, draft invoices will reflect the edit
        immediately, while finalized invoices are untouched unless voided and
        regenerated.

        - If a commit's invoice schedule item is associated with a finalized
        invoice, you cannot remove or update the invoice schedule item.

        - If a commit's invoice schedule item is associated with a voided
        invoice, you cannot remove the invoice schedule item.

        - You cannot remove an commit access schedule segment that was applied
        to a finalized invoice. You can void the invoice beforehand and then
        remove the access schedule segment.
      operationId: editCommit-v2
      requestBody:
        description: Commit and customer IDs and fields to update
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditCommitPayload'
            example:
              customer_id: 4c91c473-fc12-445a-9c38-40421d47023f
              commit_id: 5e7e82cf-ccb7-428c-a96f-a8e4f67af822
              access_schedule:
                update_schedule_items:
                  - id: d5edbd32-c744-48cb-9475-a9bca0e6fa39
                    ending_before: '2025-03-12T00:00:00Z'
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
                    $ref: '#/components/schemas/Id'
              example:
                data:
                  id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
        '400':
          description: Error
          content:
            application/json:
              schema:
                type: object
                required:
                  - code
                  - message
                properties:
                  code:
                    type: string
                    enum:
                      - CustomerNotFound
                  message:
                    type: string
components:
  schemas:
    EditCommitPayload:
      type: object
      required:
        - customer_id
        - commit_id
      properties:
        customer_id:
          type: string
          format: uuid
          description: ID of the customer whose commit is being edited
        commit_id:
          type: string
          format: uuid
          description: ID of the commit to edit
        name:
          type: string
          description: Updated name for the commit
        description:
          type: string
          description: Updated description for the commit
        access_schedule:
          $ref: '#/components/schemas/UpdateAccessScheduleInput'
        invoice_schedule:
          $ref: '#/components/schemas/UpdateInvoiceScheduleInput'
        invoice_contract_id:
          type: string
          format: uuid
          description: ID of contract to use for invoicing
        applicable_product_ids:
          type: array
          nullable: true
          items:
            type: string
            format: uuid
          description: >-
            Which products the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
        applicable_product_tags:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            Which tags the commit applies to. If applicable_product_ids,
            applicable_product_tags or specifiers are not provided, the commit
            applies to all products.
        specifiers:
          nullable: true
          type: array
          description: >-
            List of filters that determine what kind of customer usage draws
            down a commit or credit. A customer's usage needs to meet the
            condition of at least one of the specifiers to contribute to a
            commit's or credit's drawdown. This field cannot be used together
            with `applicable_product_ids` or `applicable_product_tags`. Instead,
            to target usage by product or product tag, pass those values in the
            body of `specifiers`.
          items:
            $ref: '#/components/schemas/CommitSpecifierInput'
        product_id:
          type: string
          format: uuid
        priority:
          type: number
          nullable: true
          description: >-
            If multiple commits are applicable, the one with the lower priority
            will apply first.
        rate_type:
          type: string
          enum:
            - LIST_RATE
            - list_rate
            - COMMIT_RATE
            - commit_rate
          description: >-
            If provided, updates the commit to use the specified rate type for
            current and future invoices. Previously finalized invoices will need
            to be voided and regenerated to reflect the rate type change.
        hierarchy_configuration:
          $ref: '#/components/schemas/CommitHierarchyConfiguration'
          description: Optional configuration for commit hierarchy access control
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    UpdateAccessScheduleInput:
      type: object
      properties:
        add_schedule_items:
          type: array
          items:
            type: object
            required:
              - amount
              - starting_at
              - ending_before
            properties:
              amount:
                type: number
              starting_at:
                type: string
                format: date-time
              ending_before:
                type: string
                format: date-time
        update_schedule_items:
          type: array
          items:
            type: object
            required:
              - id
            properties:
              id:
                type: string
                format: uuid
              amount:
                type: number
              starting_at:
                type: string
                format: date-time
              ending_before:
                type: string
                format: date-time
        remove_schedule_items:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
    UpdateInvoiceScheduleInput:
      type: object
      properties:
        add_schedule_items:
          type: array
          items:
            type: object
            required:
              - timestamp
            properties:
              timestamp:
                type: string
                format: date-time
              amount:
                type: number
              quantity:
                type: number
              unit_price:
                type: number
        update_schedule_items:
          type: array
          items:
            type: object
            required:
              - id
            properties:
              id:
                type: string
                format: uuid
              timestamp:
                type: string
                format: date-time
              amount:
                type: number
              quantity:
                type: number
              unit_price:
                type: number
        remove_schedule_items:
          type: array
          items:
            required:
              - id
            type: object
            properties:
              id:
                type: string
                format: uuid
    CommitSpecifierInput:
      type: object
      properties:
        product_id:
          type: string
          format: uuid
          description: >-
            If provided, the specifier will only apply to the product with the
            specified ID.
        product_tags:
          type: array
          items:
            type: string
          description: >-
            If provided, the specifier will only apply to products with all the
            specified tags.
        pricing_group_values:
          type: object
          additionalProperties:
            type: string
          description: >-
            If provided, the specifier will apply to product usage with these
            set of pricing group values.
        presentation_group_values:
          type: object
          additionalProperties:
            type: string
          description: >-
            If provided, the specifier will apply to product usage with these
            set of presentation group values.
        exclude:
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:exclude-specifiers-ga
          type: array
          description: >-
            If provided, the specifier will not apply to product usage that
            matches the inclusion criteria and any of the excluding values.
          items:
            $ref: '#/components/schemas/ExcludeSpecifier'
    CommitHierarchyConfiguration:
      type: object
      required:
        - child_access
      properties:
        child_access:
          oneOf:
            - $ref: '#/components/schemas/CommitHierarchyChildAccessAll'
            - $ref: '#/components/schemas/CommitHierarchyChildAccessNone'
            - $ref: '#/components/schemas/CommitHierarchyChildAccessContractIds'
    ExcludeSpecifier:
      type: object
      properties:
        product_tags:
          type: array
          items:
            type: string
          description: >-
            If provided, the specifier will not apply to products with all the
            specified tags.
    CommitHierarchyChildAccessAll:
      type: object
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - ALL
            - all
    CommitHierarchyChildAccessNone:
      type: object
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - NONE
            - none
    CommitHierarchyChildAccessContractIds:
      type: object
      required:
        - type
        - contract_ids
      properties:
        type:
          type: string
          enum:
            - CONTRACT_IDS
            - contract_ids
        contract_ids:
          type: array
          minItems: 1
          items:
            type: string
            format: uuid
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
