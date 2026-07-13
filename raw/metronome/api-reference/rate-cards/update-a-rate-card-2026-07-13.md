<!-- Source URL: https://docs.metronome.com/api-reference/rate-cards/update-a-rate-card.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a rate card

> Update the metadata properties of an existing rate card, including its name, description, and aliases. This endpoint is designed for managing rate card identity and reference aliases rather than modifying pricing rates.

Modifies the descriptive properties and alias configuration of a rate card without affecting the underlying pricing rates or schedules. This allows you to update how a rate card is identified and referenced throughout your system.

### Use this endpoint to:
- Rate card renaming: Update display names or descriptions for organizational clarity
- Alias management: Add, modify, or schedule alias transitions for seamless rate card migrations
- Documentation updates: Keep rate card descriptions current with business context
- Self-serve provisioning setup: Configure aliases to enable code-free rate card transitions

#### Active contract impact:
- Alias changes: Already-created contracts continue using their originally assigned rate cards.
- Other changes made using this endpoint will only impact the Metronome UI.

#### Grandfathering existing PLG customer pricing:
- Rate card aliases support scheduled transitions, enabling seamless rate card migrations for new customers, allowing existing customers to be grandfathered into their existing prices without code. Note that there are multiple mechanisms to support grandfathering in Metronome. 

#### How scheduled aliases work for PLG grandfathering:
Initial setup:
- Add alias to current rate card: Assign a stable alias (e.g., "standard-pricing") to your active rate card
- Reference alias during contract creation: Configure your self-serve workflow to create contracts using `rate_card_alias` instead of direct `rate_card_id`
- Automatic resolution: New contracts referencing the alias automatically resolve to the rate card associated with the alias at the point in time of provisioning

#### Grandfathering process:
- Create new rate card: Build your new rate card with updated pricing structure
- Schedule alias transition: Add the same alias to the new rate card with a `starting_at` timestamp
- Automatic cutover: Starting at the scheduled time, new contracts created in your PLG workflow using that alias will automatically reference the new rate card




## OpenAPI

````yaml /openapi.json post /v1/contract-pricing/rate-cards/update
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
  /v1/contract-pricing/rate-cards/update:
    post:
      tags:
        - Rate cards
      summary: Update a rate card
      description: >
        Update the metadata properties of an existing rate card, including its
        name, description, and aliases. This endpoint is designed for managing
        rate card identity and reference aliases rather than modifying pricing
        rates.


        Modifies the descriptive properties and alias configuration of a rate
        card without affecting the underlying pricing rates or schedules. This
        allows you to update how a rate card is identified and referenced
        throughout your system.


        ### Use this endpoint to:

        - Rate card renaming: Update display names or descriptions for
        organizational clarity

        - Alias management: Add, modify, or schedule alias transitions for
        seamless rate card migrations

        - Documentation updates: Keep rate card descriptions current with
        business context

        - Self-serve provisioning setup: Configure aliases to enable code-free
        rate card transitions


        #### Active contract impact:

        - Alias changes: Already-created contracts continue using their
        originally assigned rate cards.

        - Other changes made using this endpoint will only impact the Metronome
        UI.


        #### Grandfathering existing PLG customer pricing:

        - Rate card aliases support scheduled transitions, enabling seamless
        rate card migrations for new customers, allowing existing customers to
        be grandfathered into their existing prices without code. Note that
        there are multiple mechanisms to support grandfathering in Metronome. 


        #### How scheduled aliases work for PLG grandfathering:

        Initial setup:

        - Add alias to current rate card: Assign a stable alias (e.g.,
        "standard-pricing") to your active rate card

        - Reference alias during contract creation: Configure your self-serve
        workflow to create contracts using `rate_card_alias` instead of direct
        `rate_card_id`

        - Automatic resolution: New contracts referencing the alias
        automatically resolve to the rate card associated with the alias at the
        point in time of provisioning


        #### Grandfathering process:

        - Create new rate card: Build your new rate card with updated pricing
        structure

        - Schedule alias transition: Add the same alias to the new rate card
        with a `starting_at` timestamp

        - Automatic cutover: Starting at the scheduled time, new contracts
        created in your PLG workflow using that alias will automatically
        reference the new rate card
      operationId: updateRateCard-v1
      requestBody:
        description: Update a rate card. Must provide at least one of name or description.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateRateCardPayload'
            example:
              rate_card_id: d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc
              name: My Updated Rate Card
              description: My Updated Rate Card Description
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
        '404':
          $ref: '#/components/responses/NotFound'
components:
  schemas:
    UpdateRateCardPayload:
      type: object
      required:
        - rate_card_id
      properties:
        rate_card_id:
          type: string
          format: uuid
          description: ID of the rate card to update
        name:
          type: string
          description: Used only in UI/API. It is not exposed to end customers.
        description:
          type: string
        aliases:
          type: array
          items:
            $ref: '#/components/schemas/RateCardAlias'
          description: >-
            Reference this alias when creating a contract. If the same alias is
            assigned to multiple rate cards, it will reference the rate card to
            which it was most recently assigned. It is not exposed to end
            customers.
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
