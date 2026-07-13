<!-- Source URL: https://docs.metronome.com/api-reference/rate-cards/create-a-rate-card.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a rate card

> In Metronome, the rate card is the central location for your pricing. Rate cards were built with new product launches and pricing changes in mind - you can update your products and pricing in one place, and that change will be automatically propagated across your customer cohorts. Most clients need only maintain one or a few rate cards within Metronome.

### Use this endpoint to:
- Create a rate card with a name and description
- Define the rate card's single underlying fiat currency, and any number of conversion rates between that fiat currency and custom pricing units. You can then add products and associated rates in the fiat currency or custom pricing unit for which you have defined a conversion rate. 
- Set aliases for the rate card. Aliases are human-readable names that you can use in the place of the id of the rate card when provisioning a customer's contract. By using an alias, you can easily create a contract and provision a customer by choosing the paygo rate card, without storing the rate card id in your internal systems. This is helpful when launching a new rate card for paygo customers, you can update the alias for paygo to be scheduled to be assigned to the new rate card without updating your code.

### Key response fields:
- The ID of the rate card you just created

### Usage guidelines:
- After creating a rate card, you can now use the addRate or addRates endpoints to add products and their prices to it
- A rate card alias can only be used by one rate card at a time. If you create a contract with a rate card alias that is already in use by another rate card, the original rate card's alias schedule will be updated. The alias will reference the rate card to which it was most recently assigned.




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/rate-cards/create
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
  /v1/contract-pricing/rate-cards/create:
    post:
      tags:
        - Rate cards
      summary: Create a rate card
      description: >
        In Metronome, the rate card is the central location for your pricing.
        Rate cards were built with new product launches and pricing changes in
        mind - you can update your products and pricing in one place, and that
        change will be automatically propagated across your customer cohorts.
        Most clients need only maintain one or a few rate cards within
        Metronome.


        ### Use this endpoint to:

        - Create a rate card with a name and description

        - Define the rate card's single underlying fiat currency, and any number
        of conversion rates between that fiat currency and custom pricing units.
        You can then add products and associated rates in the fiat currency or
        custom pricing unit for which you have defined a conversion rate. 

        - Set aliases for the rate card. Aliases are human-readable names that
        you can use in the place of the id of the rate card when provisioning a
        customer's contract. By using an alias, you can easily create a contract
        and provision a customer by choosing the paygo rate card, without
        storing the rate card id in your internal systems. This is helpful when
        launching a new rate card for paygo customers, you can update the alias
        for paygo to be scheduled to be assigned to the new rate card without
        updating your code.


        ### Key response fields:

        - The ID of the rate card you just created


        ### Usage guidelines:

        - After creating a rate card, you can now use the addRate or addRates
        endpoints to add products and their prices to it

        - A rate card alias can only be used by one rate card at a time. If you
        create a contract with a rate card alias that is already in use by
        another rate card, the original rate card's alias schedule will be
        updated. The alias will reference the rate card to which it was most
        recently assigned.
      operationId: createRateCard-v1
      requestBody:
        description: >
          In Metronome, the rate card is the central location for your pricing.
          Rate cards were built with new product launches and pricing changes in
          mind - you can update your products and pricing in one place, and that
          change will be automatically propagated across your customer cohorts.
          Most clients need only maintain one or a few rate cards within
          Metronome.


          ### Use this endpoint to:

          - Create a rate card with a name and description

          - Define the rate card's single underlying fiat currency, and any
          number of conversion rates between that fiat currency and custom
          pricing units. You can then add products and associated rates in the
          fiat currency or custom pricing unit for which you have defined a
          conversion rate. 

          - Set aliases for the rate card. Aliases are human-readable names that
          you can use in the place of the id of the rate card when provisioning
          a customer's contract. By using an alias, you can easily create a
          contract and provision a customer by choosing the paygo rate card,
          without storing the rate card id in your internal systems. This is
          helpful when launching a new rate card for paygo customers, you can
          update the alias for paygo to be scheduled to be assigned to the new
          rate card without updating your code.


          ### Key response fields:

          - The ID of the rate card you just created


          ### Usage guidelines:

          - After creating a rate card, you can now use the addRate or addRates
          endpoints to add products and their prices to it

          - A rate card alias can only be used by one rate card at a time. If
          you create a contract with a rate card alias that is already in use by
          another rate card, the original rate card's alias schedule will be
          updated. The alias will reference the rate card to which it was most
          recently assigned.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateRateCardPayload'
            example:
              name: My Rate Card
              description: My Rate Card Description
              fiat_credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
              credit_type_conversions:
                - custom_credit_type_id: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
                  fiat_per_custom_credit: 2
              aliases:
                - name: my-rate-card
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
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    CreateRateCardPayload:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Used only in UI/API. It is not exposed to end customers.
        description:
          type: string
        fiat_credit_type_id:
          type: string
          format: uuid
          example: 2714e483-4ff1-48e4-9e25-ac732e8f24f2
          description: >-
            The Metronome ID of the credit type to associate with the rate card,
            defaults to USD (cents) if not passed.
        credit_type_conversions:
          type: array
          items:
            $ref: '#/components/schemas/CreditTypeConversionInput'
          description: Required when using custom pricing units in rates.
        aliases:
          type: array
          items:
            $ref: '#/components/schemas/RateCardAlias'
          description: >-
            Reference this alias when creating a contract. If the same alias is
            assigned to multiple rate cards, it will reference the rate card to
            which it was most recently assigned. It is not exposed to end
            customers.
        custom_fields:
          $ref: '#/components/schemas/CustomField'
    Id:
      required:
        - id
      type: object
      properties:
        id:
          type: string
          format: uuid
    Error:
      required:
        - message
      type: object
      properties:
        message:
          type: string
    CreditTypeConversionInput:
      type: object
      required:
        - custom_credit_type_id
        - fiat_per_custom_credit
      properties:
        custom_credit_type_id:
          type: string
          format: uuid
        fiat_per_custom_credit:
          type: number
    RateCardAlias:
      type: object
      required:
        - name
      properties:
        name:
          type: string
        starting_at:
          type: string
          format: date-time
        ending_before:
          type: string
          format: date-time
    CustomField:
      type: object
      description: 'Custom fields to be added eg. { "key1": "value1", "key2": "value2" }'
      additionalProperties:
        type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````
