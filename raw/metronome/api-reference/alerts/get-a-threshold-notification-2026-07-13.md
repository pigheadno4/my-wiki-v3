<!-- Source URL: https://docs.metronome.com/api-reference/alerts/get-a-threshold-notification.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a threshold notification

> Retrieve the real-time evaluation status for a specific threshold notification-customer pair. This endpoint provides instant visibility into whether a customer has triggered a threshold notification condition, enabling you to monitor account health and take proactive action based on current threshold notification states.

### Use this endpoint to:
- Check if a specific customer is currently violating an threshold notification (`in_alarm` status)
- Verify threshold notification configuration details and threshold values for a customer
- Monitor the evaluation state of newly created or recently modified threshold notification
- Build dashboards or automated workflows that respond to specific threshold notification conditions
- Validate threshold notification behavior before deploying to production customers
- Integrate threshold notification status checks into customer support tools or admin interfaces

### Key response fields: 
A CustomerAlert object containing:

- `customer_status`: The current evaluation state

- `ok` - Customer is within acceptable thresholds
- `in_alarm` - Customer has breached the threshold for the notification
- `evaluating` - Notification is currently being evaluated (typically during initial setup)
- `null` - Notification has been archived
- `triggered_by`: Additional context about what caused the notification to trigger (when applicable)
- `updated_at`: Timestamp of when the `customer_status` was last updated
- alert: Complete threshold notification configuration including:
  - Notification ID, name, and type
  - Current threshold values and credit type information
  - Notification status (enabled, disabled, or archived)
  - Any applied filters (credit grant types, custom fields, group values)

### Usage guidelines:
- Customer status: Returns the current evaluation state, not historical data. For threshold notification history, use webhook notifications or event logs
- Required parameters: Both customer_id and alert_id must be valid UUIDs that exist in your organization
- Archived notifications: Returns null for customer_status if the notification has been archived, but still includes the notification configuration details
- Performance considerations: This endpoint queries live evaluation state, making it ideal for real-time monitoring but not for bulk status checks
- Integration patterns: Best used for on-demand status checks in response to user actions or as part of targeted monitoring workflows
- Error handling: Returns 404 if either the customer or alert_id doesn't exist or isn't accessible to your organization




## OpenAPI

````yaml /openapi.json post /v1/customer-alerts/get
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
  /v1/customer-alerts/get:
    post:
      tags:
        - Alerts
      summary: Get a threshold notification
      description: >
        Retrieve the real-time evaluation status for a specific threshold
        notification-customer pair. This endpoint provides instant visibility
        into whether a customer has triggered a threshold notification
        condition, enabling you to monitor account health and take proactive
        action based on current threshold notification states.


        ### Use this endpoint to:

        - Check if a specific customer is currently violating an threshold
        notification (`in_alarm` status)

        - Verify threshold notification configuration details and threshold
        values for a customer

        - Monitor the evaluation state of newly created or recently modified
        threshold notification

        - Build dashboards or automated workflows that respond to specific
        threshold notification conditions

        - Validate threshold notification behavior before deploying to
        production customers

        - Integrate threshold notification status checks into customer support
        tools or admin interfaces


        ### Key response fields: 

        A CustomerAlert object containing:


        - `customer_status`: The current evaluation state


        - `ok` - Customer is within acceptable thresholds

        - `in_alarm` - Customer has breached the threshold for the notification

        - `evaluating` - Notification is currently being evaluated (typically
        during initial setup)

        - `null` - Notification has been archived

        - `triggered_by`: Additional context about what caused the notification
        to trigger (when applicable)

        - `updated_at`: Timestamp of when the `customer_status` was last updated

        - alert: Complete threshold notification configuration including:
          - Notification ID, name, and type
          - Current threshold values and credit type information
          - Notification status (enabled, disabled, or archived)
          - Any applied filters (credit grant types, custom fields, group values)

        ### Usage guidelines:

        - Customer status: Returns the current evaluation state, not historical
        data. For threshold notification history, use webhook notifications or
        event logs

        - Required parameters: Both customer_id and alert_id must be valid UUIDs
        that exist in your organization

        - Archived notifications: Returns null for customer_status if the
        notification has been archived, but still includes the notification
        configuration details

        - Performance considerations: This endpoint queries live evaluation
        state, making it ideal for real-time monitoring but not for bulk status
        checks

        - Integration patterns: Best used for on-demand status checks in
        response to user actions or as part of targeted monitoring workflows

        - Error handling: Returns 404 if either the customer or alert_id doesn't
        exist or isn't accessible to your organization
      operationId: getCustomerAlert-v1
      requestBody:
        description: >-
          The customer ID and notification ID of the threshold notification to
          get
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetCustomerAlertPayload'
            example:
              customer_id: 9b85c1c1-5238-4f2a-a409-61412905e1e1
              alert_id: 8deed800-1b7a-495d-a207-6c52bac54dc9
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
                    $ref: '#/components/schemas/CustomerAlert'
              example:
                data:
                  customer_status: in_alarm
                  alert:
                    id: 8deed800-1b7a-495d-a207-6c52bac54dc9
                    uniqueness_key: 823j7fqzo1
                    name: Low credit balance alert
                    type: low_credit_balance_reached
                    status: enabled
                    credit_type:
                      id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                      name: USD (cents)
                    threshold: 0
                    updated_at: '2022-01-01T00:00:00Z'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    GetCustomerAlertPayload:
      required:
        - customer_id
        - alert_id
      type: object
      properties:
        customer_id:
          type: string
          format: uuid
          description: The Metronome ID of the customer
        alert_id:
          type: string
          format: uuid
          description: The Metronome ID of the threshold notification
        plans_or_contracts:
          x-mint:
            groups:
              - ff:plans-contracts-parallel-alerts
          type: string
          enum:
            - PLANS
            - CONTRACTS
          description: >-
            When parallel threshold notifications are enabled during migration,
            this flag denotes whether to fetch notifications for plans or
            contracts.
        group_values:
          type: array
          description: >-
            Only present for `spend_threshold_reached` notifications. Retrieve
            the notification for a specific group key-value pair.
          items:
            $ref: '#/components/schemas/GroupKeyFilterType'
        seat_filter:
          type: object
          description: >-
            Only allowed for `low_remaining_seat_balance_reached` notifications.
            This filters alerts by the seat group key-value pair.
          required:
            - seat_group_key
            - seat_group_value
          properties:
            seat_group_key:
              type: string
              description: The seat group key (e.g., "seat_id", "user_id")
            seat_group_value:
              type: string
              description: The specific seat identifier to filter by
        alert_specifiers:
          type: array
          description: >-
            Can be used with only
            `low_remaining_contract_credit_and_commit_balance_reached`
            notifications. Used to filter the alert by the custom field
            key-value pair.
          items:
            $ref: '#/components/schemas/AlertSpecifierFilter'
        custom_field_filters:
          x-stainless-skip: true
          x-mint:
            groups:
              - ff:alert-specifiers-enabled
          type: array
          description: Used to filter the alert by the custom field key-value pair.
          items:
            $ref: '#/components/schemas/CustomFieldFilterType'
        webhook_notification_id:
          x-mint:
            groups:
              - ff:api-allow-webhook-notification-id
          x-stainless-skip: true
          type: string
          description: >-
            Indicates that this API request was triggered by a webhook
            notification with the provided ID.
    CustomerAlert:
      required:
        - customer_status
        - alert
      type: object
      properties:
        customer_status:
          type: string
          enum:
            - ok
            - in_alarm
            - evaluating
          nullable: true
          description: >-
            The status of the threshold notification. If the notification is
            archived, null will be returned.
        triggered_by:
          type: string
          nullable: true
          description: >-
            If present, indicates the reason the threshold notification was
            triggered.
        alert:
          $ref: '#/components/schemas/Alert'
    GroupKeyFilterType:
      type: object
      description: >-
        Scopes threshold notification evaluation to a specific presentation
        group key on individual line items. Only present for spend
        notifications.
      required:
        - key
        - value
      properties:
        key:
          type: string
        value:
          type: string
    AlertSpecifierFilter:
      type: object
      required:
        - custom_field_filters
      properties:
        custom_field_filters:
          type: array
          description: >-
            A list of custom field filters for notification types that support
            advanced filtering
          items:
            $ref: '#/components/schemas/CustomFieldFilterType'
        exclude:
          type: array
          description: >-
            If provided, the specifier will not apply to balances that matches
            the inclusion criteria and any of the excluding values.
          items:
            $ref: '#/components/schemas/ExcludeAlertSpecifier'
    CustomFieldFilterType:
      type: object
      required:
        - entity
        - key
        - value
      properties:
        entity:
          type: string
          enum:
            - Contract
            - Commit
            - ContractCredit
            - ContractCreditOrCommit
          x-mint-enum:
            ContractCreditOrCommit:
              - ff:alert-specifiers-enabled
        key:
          type: string
        value:
          type: string
    Alert:
      required:
        - id
        - name
        - type
        - status
        - threshold
        - updated_at
      type: object
      properties:
        id:
          type: string
          description: the Metronome ID of the threshold notification
        name:
          type: string
          description: Name of the threshold notification
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        type:
          type: string
          enum:
            - spend_threshold_reached
            - monthly_invoice_total_spend_threshold_reached
            - low_remaining_days_for_commit_segment_reached
            - low_remaining_commit_balance_reached
            - low_remaining_commit_percentage_reached
            - low_remaining_days_for_contract_credit_segment_reached
            - low_remaining_contract_credit_balance_reached
            - low_remaining_contract_credit_percentage_reached
            - low_remaining_contract_credit_and_commit_balance_reached
            - low_remaining_seat_balance_reached
            - invoice_total_reached
          description: Type of the threshold notification
        status:
          type: string
          enum:
            - enabled
            - archived
            - disabled
          description: Status of the threshold notification
        credit_type:
          $ref: '#/components/schemas/CreditType'
          nullable: true
        threshold:
          type: number
          description: Threshold value of the notification policy
        updated_at:
          type: string
          format: date-time
          description: >-
            Timestamp for when the threshold notification's customer status was
            last updated
        credit_grant_type_filters:
          type: array
          items:
            type: string
          description: >-
            An array of strings, representing a way to filter the credit grant
            this threshold notification applies to, by looking at the
            credit_grant_type field on the credit grant. This field is only
            defined for CreditPercentage and CreditBalance notifications
        custom_field_filters:
          type: array
          description: >-
            A list of custom field filters for notification types that support
            advanced filtering
          items:
            $ref: '#/components/schemas/CustomFieldFilterType'
        group_key_filter:
          $ref: '#/components/schemas/GroupKeyFilterType'
          x-mint:
            groups:
              - client_id:462b838b-1582-4100-816e-f6c07bb604fe
              - client_id:c187f54f-e807-4cf6-8fa1-a01f09d05412
              - client_id:aa2899ec-16ad-413b-b20b-ec9ba4692d4e
              - client_id:2f0c6751-0b61-46f2-8664-2eb1be6136cf
              - client_id:b2c5d30a-6078-4cd4-9e98-340ca0883789
              - client_id:67c6fe5e-5715-4b05-aa2a-b3885cd68b81
              - client_id:f9b1ebc0-19f5-43cd-ba0b-7cf7da34fe7c
              - client_id:98ac66cc-88b4-447f-a2e6-a84ebc81e36a
        invoice_types_filter:
          $ref: '#/components/schemas/InvoiceTypesFilterType'
        group_values:
          type: array
          description: >-
            Only present for `spend_threshold_reached` notifications. Scope
            notification to a specific group key on individual line items.
          items:
            $ref: '#/components/schemas/GroupValueFilterType'
        seat_filter:
          type: object
          description: >-
            Only present for low_remaining_seat_balance_reached notifications.
            The seat group key or seat group key-value pair the alert is scoped
            to.
          required:
            - seat_group_key
          properties:
            seat_group_key:
              type: string
              description: >-
                The seat group key (e.g., "seat_id", "user_id") that the alert
                is scoped to.
            seat_group_value:
              type: string
              description: The seat group value that the alert is scoped to.
        alert_specifiers:
          type: array
          description: >-
            Present for
            `low_remaining_contract_credit_and_commit_balance_reached`
            notifications. The filters that define the balances that are
            considered when evaluating the alert.
          items:
            $ref: '#/components/schemas/AlertSpecifier'
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    ExcludeAlertSpecifier:
      type: object
      properties:
        custom_field_filters:
          type: array
          description: >-
            A list of custom field filters for notification types that support
            advanced filtering
          items:
            $ref: '#/components/schemas/CustomFieldFilterType'
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
    CreditType:
      required:
        - name
        - id
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          format: uuid
    InvoiceTypesFilterType:
      type: array
      description: >-
        Only supported for invoice_total_reached threshold notifications. A list
        of invoice types to evaluate.
      items:
        $ref: '#/components/schemas/InvoiceType'
    GroupValueFilterType:
      type: object
      required:
        - key
      properties:
        key:
          type: string
        value:
          type: string
    AlertSpecifier:
      type: object
      properties:
        custom_field_filters:
          type: array
          description: >-
            A list of custom field filters for notification types that support
            advanced filtering
          items:
            $ref: '#/components/schemas/AlertSpecifierInclusiveCustomFieldFilter'
        exclude:
          type: array
          description: >-
            If provided, the specifier will not apply to balances that matches
            the inclusion criteria and any of the excluding values.
          items:
            $ref: '#/components/schemas/ExcludeAlertSpecifier'
    InvoiceType:
      type: string
      example: SCHEDULED or USAGE
    AlertSpecifierInclusiveCustomFieldFilter:
      type: object
      required:
        - entity
        - key
      properties:
        entity:
          type: string
          enum:
            - Contract
            - Commit
            - ContractCredit
            - ContractCreditOrCommit
          x-mint-enum:
            ContractCreditOrCommit:
              - ff:alert-specifiers-enabled
        key:
          type: string
        value:
          type: string
  responses:
    NotFound:
      description: The specified resource was not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
