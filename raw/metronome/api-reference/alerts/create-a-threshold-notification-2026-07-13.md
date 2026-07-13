<!-- Source URL: https://docs.metronome.com/api-reference/alerts/create-a-threshold-notification.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a threshold notification

> Create a new threshold notification to monitor customer spending, balances, and billing metrics in real-time. Metronome's notification system provides industry-leading speed with immediate evaluation capabilities, enabling you to proactively manage customer accounts and prevent revenue leakage.

This endpoint creates configurable threshold notifications that continuously monitor various billing thresholds including spend limits, credit balances, commitment utilization, and invoice totals. Threshold notifications can be configured globally for all customers or targeted to specific customer accounts.

### Use this endpoint to:
- Proactively monitor customer spending patterns to prevent unexpected overages or credit exhaustion
- Automate notifications when customers approach commitment limits or credit thresholds
- Enable real-time intervention for accounts at risk of churn or payment issues
- Scale billing operations by automating threshold-based workflows and notifications

### Key response fields: 
A successful response returns a CustomerAlert object containing:

- The threshold notification configuration with its unique ID and current status
- The customer's evaluation status (ok, in_alarm, or evaluating)
- Threshold notification metadata including type, threshold values, and update timestamps

### Usage guidelines:
- Immediate evaluation: Set `evaluate_on_create` : `true` (default) for instant evaluation against existing customers
- Uniqueness constraints: Each threshold notification must have a unique `uniqueness_key` within your organization. Use `release_uniqueness_key` : `true` when archiving to reuse keys
- Notification type requirements: Different threshold notification types require specific fields (e.g., `billable_metric_id` for usage notifications, `credit_type_id` for credit-based threshold notifications)
- Webhook delivery: Threshold notifications trigger webhook notifications for real-time integration with your systems. Configure webhook endpoints before creating threshold notifications
- Performance at scale: Metronome's event-driven architecture processes threshold notification evaluations in real-time as usage events stream in, unlike competitors who rely on periodic polling or batch evaluation cycles




## OpenAPI

````yaml /openapi.json post /v1/alerts/create
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
  /v1/alerts/create:
    post:
      tags:
        - Alerts
      summary: Create a threshold notification
      description: >
        Create a new threshold notification to monitor customer spending,
        balances, and billing metrics in real-time. Metronome's notification
        system provides industry-leading speed with immediate evaluation
        capabilities, enabling you to proactively manage customer accounts and
        prevent revenue leakage.


        This endpoint creates configurable threshold notifications that
        continuously monitor various billing thresholds including spend limits,
        credit balances, commitment utilization, and invoice totals. Threshold
        notifications can be configured globally for all customers or targeted
        to specific customer accounts.


        ### Use this endpoint to:

        - Proactively monitor customer spending patterns to prevent unexpected
        overages or credit exhaustion

        - Automate notifications when customers approach commitment limits or
        credit thresholds

        - Enable real-time intervention for accounts at risk of churn or payment
        issues

        - Scale billing operations by automating threshold-based workflows and
        notifications


        ### Key response fields: 

        A successful response returns a CustomerAlert object containing:


        - The threshold notification configuration with its unique ID and
        current status

        - The customer's evaluation status (ok, in_alarm, or evaluating)

        - Threshold notification metadata including type, threshold values, and
        update timestamps


        ### Usage guidelines:

        - Immediate evaluation: Set `evaluate_on_create` : `true` (default) for
        instant evaluation against existing customers

        - Uniqueness constraints: Each threshold notification must have a unique
        `uniqueness_key` within your organization. Use `release_uniqueness_key`
        : `true` when archiving to reuse keys

        - Notification type requirements: Different threshold notification types
        require specific fields (e.g., `billable_metric_id` for usage
        notifications, `credit_type_id` for credit-based threshold
        notifications)

        - Webhook delivery: Threshold notifications trigger webhook
        notifications for real-time integration with your systems. Configure
        webhook endpoints before creating threshold notifications

        - Performance at scale: Metronome's event-driven architecture processes
        threshold notification evaluations in real-time as usage events stream
        in, unlike competitors who rely on periodic polling or batch evaluation
        cycles
      operationId: createAlert-v1
      requestBody:
        description: The details of the threshold notification to create
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCustomerAlertPayload'
            example:
              alert_type: spend_threshold_reached
              credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              name: $100 spend threshold reached
              threshold: 10000
              customer_id: 4db51251-61de-4bfe-b9ce-495e244f3491
              credit_grant_type_filters:
                - enterprise
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
                  id: 58fb0650-e54a-4d17-93cb-ba8e56c32c65
components:
  schemas:
    CreateCustomerAlertPayload:
      required:
        - alert_type
        - name
        - threshold
      type: object
      properties:
        alert_type:
          type: string
          enum:
            - spend_threshold_reached
            - monthly_invoice_total_spend_threshold_reached
            - usage_threshold_reached
            - low_remaining_days_for_commit_segment_reached
            - low_remaining_commit_balance_reached
            - low_remaining_commit_percentage_reached
            - low_remaining_days_for_contract_credit_segment_reached
            - low_remaining_contract_credit_balance_reached
            - low_remaining_contract_credit_percentage_reached
            - low_remaining_contract_credit_and_commit_balance_reached
            - invoice_total_reached
            - low_remaining_seat_balance_reached
          description: Type of the threshold notification
        name:
          type: string
          description: Name of the threshold notification
        uniqueness_key:
          $ref: '#/components/schemas/UniquenessKey'
        threshold:
          type: number
          description: >-
            Threshold value of the notification policy.  Depending upon the
            notification type, this number may represent a financial amount, the
            days remaining, or a percentage reached.
        credit_type_id:
          type: string
          format: uuid
          description: >-
            ID of the credit's currency, defaults to USD. If the specific
            notification type requires a pricing unit/currency, find the ID in
            the [Metronome
            app](https://app.metronome.com/offering/pricing-units).
        customer_id:
          type: string
          format: uuid
          description: >-
            If provided, will create this threshold notification for this
            specific customer. To create a notification for all customers, do
            not specify a `customer_id`.
        billable_metric_id:
          type: string
          format: uuid
          description: >-
            For threshold notifications of type `usage_threshold_reached`,
            specifies which billable metric to track the usage for.
        credit_grant_type_filters:
          type: array
          items:
            type: string
          description: >-
            An array of strings, representing a way to filter the credit grant
            this threshold notification applies to, by looking at the
            credit_grant_type field on the credit grant. This field is only
            defined for CreditPercentage and CreditBalance notifications
        evaluate_on_create:
          type: boolean
          description: >-
            If true, the threshold notification will evaluate immediately on
            customers that already meet the notification threshold. If false, it
            will only evaluate on future customers that trigger the threshold.
            Defaults to true.
        custom_field_filters:
          type: array
          description: >-
            A list of custom field filters for threshold notification types that
            support advanced filtering. Only present for contract invoices.
          items:
            $ref: '#/components/schemas/CustomFieldFilterType'
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
            Required for `low_remaining_seat_balance_reached` notifications. The
            alert is scoped to this seat group key-value pair.
          required:
            - seat_group_key
          properties:
            seat_group_key:
              type: string
              description: The seat group key (e.g., "seat_id", "user_id")
            seat_group_value:
              type: string
              description: Optional seat identifier the alert is scoped to.
        alert_specifiers:
          type: array
          description: >-
            Can be used with only
            `low_remaining_contract_credit_and_commit_balance_reached`
            notifications. Defines the balances that are considered when
            evaluating the alert.
          items:
            $ref: '#/components/schemas/AlertSpecifier'
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    UniquenessKey:
      type: string
      minLength: 1
      maxLength: 128
      description: >-
        Prevents the creation of duplicates. If a request to create a record is
        made with a previously used uniqueness key, a new record will not be
        created and the request will fail with a 409 error.
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
