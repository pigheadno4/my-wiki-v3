<!-- Source URL: https://docs.paypal.ai/reference/api/rest/cart-operations/update-cart -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update cart

> Updates a cart by completely replacing its contents with the provided PayPalCart object.
> This is used when customers make changes like adding items, updating shipping address,
> applying coupons, or completing checkout fields.

**⚠️ CRITICAL: Complete Replacement Operation**

- PUT replaces the ENTIRE cart with the provided PayPalCart object
- Any fields not included in the request will be removed/reset
- Missing fields will be lost (e.g., omitting customer info will remove it)

## OpenAPI

````yaml /api-reference/paypal-cart-agentic-commerce-v1.yaml put /merchant-cart/{cartId}
openapi: 3.0.3
info:
  title: PayPal Cart API v1
  version: 1.2.0
  description: >
    **PayPal Cart API v1 - Unified Merchant Integration**


    This API enables merchants to integrate with PayPal's Shopping Cart service
    for AI-powered agentic commerce.


    ## Key Features

    - **Unified Schema**: Same PayPalCart object for all operations

    - **Simple API**: 4 core endpoints (POST, GET, PUT, checkout)

    - **AI-Ready**: Built for conversational commerce


    ## Architecture

    ```

    Customer ↔ AI Agent ↔ PayPal Commerce Platform ↔ Your Merchant API

    ```
  contact:
    name: PayPal Developer Support
    url: https://developer.paypal.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
servers:
  - url: https://your-domain.com/api/paypal/v1
    description: Your merchant API server
security:
  - PayPalJWT: []
paths:
  /merchant-cart/{cartId}:
    put:
      tags:
        - Cart Operations
      summary: Update cart
      description: >
        Updates a cart by completely replacing its contents with the provided
        PayPalCart object.

        This is used when customers make changes like adding items, updating
        shipping address,

        applying coupons, or completing checkout fields.


        **⚠️ CRITICAL: Complete Replacement Operation**

        - PUT replaces the ENTIRE cart with the provided PayPalCart object

        - Any fields not included in the request will be removed/reset

        - Missing fields will be lost (e.g., omitting customer info will remove
        it)
      operationId: updateCart
      parameters:
        - name: cartId
          in: path
          required: true
          description: The cart identifier
          schema:
            type: string
            example: CART-123
        - name: Authorization
          in: header
          required: true
          description: PayPal-supplied JWT token for authentication
          schema:
            type: string
            example: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
        - name: Content-Type
          in: header
          required: true
          description: Request content type
          schema:
            type: string
            example: application/json
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/PayPalCart"
            examples:
              update_quantity:
                summary: Update item quantity in cart
                value:
                  items:
                    - variant_id: SHIRT-BASIC-001
                      quantity: 3
                      name: Basic T-Shirt
                      price:
                        currency_code: USD
                        value: "19.99"
                  customer:
                    email_address: customer@example.com
                  payment_method:
                    type: paypal
              add_shipping_address:
                summary: Add shipping address to existing cart
                value:
                  items:
                    - variant_id: JEANS-SLIM-32
                      quantity: 2
                      name: Slim Fit Jeans (32" waist)
                      price:
                        currency_code: USD
                        value: "79.99"
                  customer:
                    email_address: customer@example.com
                  shipping_address:
                    address_line_1: 456 New Street
                    address_line_2: Unit 201
                    admin_area_2: San Francisco
                    admin_area_1: CA
                    postal_code: "94105"
                    country_code: US
                  payment_method:
                    type: paypal
              change_shipping_selection:
                summary: Agent changes shipping option selection
                value:
                  items:
                    - variant_id: ELECTRONICS-001
                      quantity: 1
                      name: Wireless Headphones
                      price:
                        currency_code: USD
                        value: "199.99"
                  customer:
                    email_address: customer@example.com
                  shipping_address:
                    address_line_1: 123 Tech Street
                    admin_area_2: Austin
                    admin_area_1: TX
                    postal_code: "78701"
                    country_code: US
                  available_shipping_options:
                    - id: STANDARD
                      name: Standard Shipping (3-5 days)
                      price:
                        currency_code: USD
                        value: "5.99"
                      estimated_delivery: "2024-06-29"
                      is_selected: false
                    - id: EXPRESS
                      name: Express Shipping (1-2 days)
                      price:
                        currency_code: USD
                        value: "15.99"
                      estimated_delivery: "2024-06-26"
                      is_selected: true
                  payment_method:
                    type: paypal
      responses:
        "200":
          description: Cart updated successfully
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PayPalCart"
              examples:
                quantity_updated:
                  summary: Item quantity updated successfully
                  value:
                    id: CART-UPDATE-001
                    status: CREATED
                    validation_status: VALID
                    validation_issues: []
                    items:
                      - variant_id: SHIRT-BASIC-001
                        quantity: 3
                        name: Basic T-Shirt
                        price:
                          currency_code: USD
                          value: "19.99"
                    customer:
                      email_address: customer@example.com
                    totals:
                      subtotal:
                        currency_code: USD
                        value: "59.97"
                      shipping:
                        currency_code: USD
                        value: "6.99"
                      tax:
                        currency_code: USD
                        value: "6.12"
                      total:
                        currency_code: USD
                        value: "73.08"
                shipping_address_added:
                  summary: Shipping address added with enhanced options
                  value:
                    id: CART-SHIPPING-002
                    status: CREATED
                    validation_status: VALID
                    validation_issues: []
                    items:
                      - variant_id: JEANS-SLIM-32
                        quantity: 2
                        name: Slim Fit Jeans (32" waist)
                        price:
                          currency_code: USD
                          value: "79.99"
                    customer:
                      email_address: customer@example.com
                    shipping_address:
                      address_line_1: 456 New Street
                      address_line_2: Unit 201
                      admin_area_2: San Francisco
                      admin_area_1: CA
                      postal_code: "94105"
                      country_code: US
                    available_shipping_options:
                      - id: STANDARD
                        name: Standard Shipping (3-5 days)
                        price:
                          currency_code: USD
                          value: "9.99"
                        estimated_delivery: "2024-07-01"
                        is_selected: true
                      - id: EXPRESS
                        name: Express Shipping (1-2 days)
                        price:
                          currency_code: USD
                          value: "19.99"
                        estimated_delivery: "2024-06-27"
                        is_selected: false
                      - id: SAME_DAY
                        name: Same Day Delivery
                        price:
                          currency_code: USD
                          value: "29.99"
                        estimated_delivery: "2024-06-24"
                    totals:
                      subtotal:
                        currency_code: USD
                        value: "159.98"
                      shipping:
                        currency_code: USD
                        value: "9.99"
                      tax:
                        currency_code: USD
                        value: "15.45"
                      handling:
                        currency_code: USD
                        value: "3.00"
                      custom_charges:
                        currency_code: USD
                        value: "2.50"
                      total:
                        currency_code: USD
                        value: "190.92"
        "400":
          description: Invalid request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
        "401":
          description: Authentication failed
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/Error"
                  - type: object
                    properties:
                      details:
                        type: array
                        items:
                          type: object
                          properties:
                            field:
                              type: string
                              example: authorization
                            issue:
                              $ref: "#/components/schemas/AuthenticationIssueCode"
                            description:
                              type: string
                              example: The provided JWT could not be validated
              examples:
                token_invalid:
                  summary: JWT validation failed
                  value:
                    name: AUTHENTICATION_FAILED
                    message: The provided JWT could not be validated
                    debug_id: ERROR-401-00001
                    details:
                      - issue: TOKEN_INVALID
                        description: The provided JWT could not be validated
        "404":
          description: Cart not found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              examples:
                cart_not_found:
                  summary: Cart ID does not exist
                  value:
                    name: CART_NOT_FOUND
                    message: Cart with ID does not exist
                    debug_id: ERROR-404-67890
        "422":
          description: Business rules violation
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/BusinessError"
              examples:
                item_out_of_stock:
                  summary: Item out of stock
                  value:
                    name: UNPROCESSABLE_ENTITY
                    message: Item out of stock
                    details:
                      - field: items[0].quantity
                        issue: INSUFFICIENT_INVENTORY
                        description: Requested quantity exceeds available stock
        "500":
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              examples:
                database_error:
                  summary: Database connection failure
                  value:
                    name: INTERNAL_SERVER_ERROR
                    message: A temporary system error occurred. Please try again later.
                    debug_id: ERROR-500-44556
components:
  schemas:
    PayPalCart:
      type: object
      description: >
        Unified cart object used for all operations (create, update, checkout,
        responses).

        This is the core schema that makes the API simple and consistent.


        **Request Usage:** Include only writable fields (items, customer,
        shipping_address, billing_address, etc.)

        **Response Usage:** Includes all fields, with server-calculated fields
        marked as readOnly
      properties:
        id:
          type: string
          readOnly: true
          description: Unique cart identifier (server-generated)
          example: CART-123
        status:
          type: string
          readOnly: true
          description: |
            Current cart business status (server-calculated)

            **Note:** READY is deprecated. Use CREATED instead.
          enum:
            - CREATED
            - INCOMPLETE
            - COMPLETED
            - READY
          example: CREATED
        validation_status:
          type: string
          readOnly: true
          description: >
            Cart data validation status indicating whether the cart can proceed
            to checkout.


            **VALID**: Cart data is complete and valid, ready for checkout

            - All items are available with current pricing

            - Required information is complete (shipping address, customer data)

            - No business rule violations

            - validation_issues array is empty

            - Can proceed directly to checkout


            **INVALID**: Cart has data issues that prevent checkout

            - Items out of stock, price changes, business rule violations

            - Invalid or incomplete data that needs correction

            - validation_issues array contains specific problems

            - Customer/AI agent must resolve issues before checkout


            **REQUIRES_ADDITIONAL_INFORMATION**: Cart needs more data but is
            otherwise valid

            - Missing optional but required fields (shipping address, checkout
            fields)

            - Age verification, custom fields, delivery preferences needed

            - Items and pricing are valid, just needs customer input

            - validation_issues array indicates what information is needed
          enum:
            - VALID
            - INVALID
            - REQUIRES_ADDITIONAL_INFORMATION
          example: VALID
        validation_issues:
          type: array
          readOnly: true
          description: List of issues preventing checkout (empty = ready)
          items:
            $ref: "#/components/schemas/ValidationIssue"
        totals:
          $ref: "#/components/schemas/CartTotals"
          readOnly: true
        applied_coupons:
          type: array
          readOnly: true
          description: Successfully applied coupons (server-calculated)
          items:
            $ref: "#/components/schemas/AppliedCoupon"
        available_shipping_options:
          type: array
          description: Available shipping methods with selection state
          items:
            $ref: "#/components/schemas/ShippingOption"
        items:
          type: array
          description: Products in the cart
          items:
            $ref: "#/components/schemas/CartItem"
          minItems: 1
        customer:
          $ref: "#/components/schemas/Customer"
        shipping_address:
          $ref: "#/components/schemas/ShippingAddress"
        billing_address:
          $ref: "#/components/schemas/BillingAddress"
        payment_method:
          $ref: "#/components/schemas/PaymentMethod"
        checkout_fields:
          type: array
          description: Custom checkout fields (age verification, etc.)
          items:
            $ref: "#/components/schemas/CheckoutField"
        coupons:
          type: array
          description: Discount coupons to apply or remove from cart
          items:
            $ref: "#/components/schemas/Coupon"
        geo_coordinates:
          $ref: "#/components/schemas/GeoCoordinates"
          description: Optional precise location coordinates for enhanced delivery services
    Error:
      type: object
      description: >
        API error response for technical failures and invalid requests.


        **Use HTTP Errors when:**

        - Request format is incorrect and cannot be processed

        - Authentication/authorization fails

        - Technical system failures occur


        See ERROR_CODES.md for complete guidance on Error vs ValidationIssue
        usage.
      required:
        - name
        - message
      properties:
        name:
          type: string
          description: Error name/type
          example: INVALID_REQUEST
        message:
          type: string
          description: Error description
          example: The request could not be processed
        debug_id:
          type: string
          description: Unique error identifier for support
          example: ERROR-12345
        details:
          type: array
          description: Detailed error information
          items:
            type: object
            properties:
              field:
                type: string
                example: items
              issue:
                type: string
                example: MISSING_REQUIRED_FIELD
              description:
                type: string
                example: The items field is required and cannot be empty
    AuthenticationIssueCode:
      type: string
      description: Issue codes for authentication (401) errors
      enum:
        - TOKEN_EXPIRED
        - TOKEN_INVALID
        - TOKEN_MISSING
        - SIGNATURE_VERIFICATION_FAILED
        - INSUFFICIENT_PERMISSIONS
    BusinessError:
      type: object
      description: >
        API error response for 422 Unprocessable Entity - business logic
        failures that prevent cart operations.


        **Use BusinessError (422) when:**

        - Integrator cannot create a cart resource due to business constraints

        - Issues attempting to complete a cart resource due to business rules

        - Cart operation fails due to merchant policies or external service
        constraints


        Unlike technical errors (400/404/500), business errors can optionally
        include rich context about why the 

        operation failed and what actions can resolve the issue, maintaining
        consistency with validation_issues patterns.


        The `business_context` field is optional but only available on 422
        responses. When present, it provides

        the same ValidationIssue structure used in 200 responses, enabling
        consistent AI agent handling.


        See ERROR_CODES.md for complete guidance on Error vs ValidationIssue vs
        BusinessError usage.
      required:
        - name
        - message
      properties:
        name:
          type: string
          description: Error name/type
          example: UNPROCESSABLE_ENTITY
        message:
          type: string
          description: Error description
          example: Unable to complete cart operation due to business constraints
        debug_id:
          type: string
          description: Unique error identifier for support
          example: ERROR-12345
        business_context:
          $ref: "#/components/schemas/ValidationIssue"
          description: >
            Optional rich business context about why the cart operation failed.

            Only available on 422 Unprocessable Entity responses. Provides the
            same 

            structure as validation_issues to maintain consistency across error
            handling 

            patterns, enabling AI agents to understand and potentially resolve
            business 

            constraint violations. When present, includes resolution options and
            actionable guidance.
        details:
          type: array
          description: Additional technical details if needed
          items:
            type: object
            properties:
              field:
                type: string
                example: payment_method
              issue:
                $ref: "#/components/schemas/BusinessIssueCode"
              description:
                type: string
                example: Cart operation violates merchant business rules
    ValidationIssue:
      type: object
      description: >
        Business logic issues that allow cart creation but require buyer action
        to complete payment.


        **Use Validation Issues when:**

        - Cart can be created but buyer needs to make updates to complete
        payment

        - Cart was already created but has business logic problems

        - Items need updates, addresses need completion, or policies require
        acceptance


        Consolidated validation issue system with 6 main error categories and
        specific context schemas.

        This approach simplifies error handling while maintaining rich context
        and resolution options.


        **Error Categories:**

        - INVENTORY_ISSUE: Stock, availability, back-orders, discontinued items

        - PRICING_ERROR: Price changes, discounts, tax calculation, currency
        issues  

        - SHIPPING_ERROR: Address validation, delivery restrictions, shipping
        zones, billing address requirements

        - PAYMENT_ERROR: Payment limits, currency support, processor issues

        - DATA_ERROR: Field validation, format issues, required fields

        - BUSINESS_RULE_ERROR: Account restrictions, compliance, regional limits


        **Example - PO Box Shipping Restriction:**

        ```json

        {
          "code": "SHIPPING_ERROR",
          "type": "INVALID_DATA",
          "message": "Shipping address validation failed",
          "user_message": "We can't ship to PO Box addresses. Please use a street address.",
          "field": "shipping_address",
          "context": {
            "specific_issue": "SHIPPING_TO_PO_BOX_NOT_ALLOWED",
            "po_box_detected": true,
            "restricted_items": ["LARGE-FURNITURE-001"],
            "restriction_reason": "oversized_item"
          },
          "resolution_options": [
            {
              "action": "UPDATE_ADDRESS",
              "label": "Use street address instead of PO Box",
              "metadata": {
                "priority": "high",
                "auto_applicable": false
              }
            }
          ]
        }

        ```


        **Example - Price Change:**

        ```json

        {
          "code": "PRICING_ERROR", 
          "type": "BUSINESS_RULE",
          "message": "Product pricing issue",
          "user_message": "The price for Ocean Blue T-Shirt has increased from $29.99 to $34.99. Continue with new price?",
          "item_id": "SHIRT-OCEAN-BLUE",
          "context": {
            "specific_issue": "PRICE_MISMATCH",
            "item_id": "SHIRT-OCEAN-BLUE",
            "original_price": "29.99",
            "current_price": "34.99",
            "currency_code": "USD",
            "price_change_reason": "promotional_ended",
            "price_increase": "5.00"
          },
          "resolution_options": [
            {
              "action": "ACCEPT_NEW_PRICE",
              "label": "Continue with $34.99",
              "metadata": {
                "cost_impact": "+$5.00",
                "priority": "HIGH",
                "auto_applicable": false
              }
            }
          ]
        }

        ```


        **Example - Address Validation:**

        ```json

        {
          "code": "SHIPPING_ERROR",
          "type": "INVALID_DATA",
          "message": "Shipping address validation failed",
          "user_message": "The shipping address appears to be incomplete. Please check and correct.",
          "field": "shipping_address.postal_code",
          "context": {
            "specific_issue": "SHIPPING_ADDRESS_INVALID",
            "validation_failures": ["invalid_postal_code"],
            "suggested_corrections": {
              "postal_code": "90210"
            },
            "address_quality_score": 0.3
          },
          "resolution_options": [
            {
              "action": "UPDATE_ADDRESS",
              "label": "Use suggested corrections",
              "metadata": {
                "priority": "HIGH",
                "auto_applicable": true
              }
            }
          ]
        }

        ```


        **Example - Billing Address for Tax Calculation:**

        ```json

        {
          "code": "DATA_ERROR",
          "type": "MISSING_FIELD", 
          "message": "Billing address needed for tax calculation",
          "user_message": "We need your billing address to calculate the correct sales tax for your order.",
          "field": "billing_address",
          "context": {
            "specific_issue": "BILLING_ADDRESS_FOR_TAX",
            "tax_jurisdiction_required": true,
            "current_tax_rate": "unknown",
            "supported_tax_regions": ["US", "CA", "EU"]
          },
          "resolution_options": [
            {
              "action": "PROVIDE_MISSING_FIELD",
              "label": "Add billing address",
              "metadata": {
                "priority": "MEDIUM",
                "auto_applicable": false
              }
            },
            {
              "action": "USE_SHIPPING_AS_BILLING",
              "label": "Same as shipping address",
              "metadata": {
                "priority": "HIGH", 
                "auto_applicable": true
              }
            }
          ]
        }

        ```
      required:
        - code
        - type
        - message
      properties:
        code:
          type: string
          description: Consolidated error category
          enum:
            - INVENTORY_ISSUE
            - PRICING_ERROR
            - SHIPPING_ERROR
            - PAYMENT_ERROR
            - DATA_ERROR
            - BUSINESS_RULE_ERROR
          example: INVENTORY_ISSUE
        type:
          type: string
          description: Type classification for error handling
          enum:
            - MISSING_FIELD
            - INVALID_DATA
            - BUSINESS_RULE
          example: BUSINESS_RULE
        message:
          type: string
          description: Technical message for developers and logging
          example: Product availability issue
        user_message:
          type: string
          description: Customer-friendly message for end users
          example: We can't ship to PO Box addresses. Please use a street address.
        item_id:
          type: string
          description: >-
            Specific item ID if the issue is item-specific (DEPRECATED - please
            use `variant_id` instead as shown in the example)
          example: SHIRT-BLUE-M
        variant_id:
          type: string
          description: Specific variant ID if the issue is variant-specific
          example: SHIRT-001-BLUE-M
        field:
          type: string
          description: Specific field name if the issue is field-specific
          example: shipping_address.postal_code
        context:
          anyOf:
            - $ref: "#/components/schemas/InventoryIssueContext"
            - $ref: "#/components/schemas/PricingErrorContext"
            - $ref: "#/components/schemas/ShippingErrorContext"
            - $ref: "#/components/schemas/PaymentErrorContext"
            - $ref: "#/components/schemas/DataErrorContext"
            - $ref: "#/components/schemas/BusinessRuleErrorContext"
          description: Category-specific context information
        resolution_options:
          type: array
          description: Available actions to resolve this issue
          items:
            $ref: "#/components/schemas/ResolutionOption"
    CartTotals:
      type: object
      description: >
        Comprehensive cart pricing breakdown calculated by merchant and returned
        in all cart responses.

        All fields are merchant-owned and calculated based on business logic,
        inventory, shipping rules, and tax regulations.


        **Merchant Responsibility:**

        - Calculate all totals based on items, shipping address, and business
        rules

        - Ensure accuracy for tax compliance and customer transparency

        - Handle currency consistency across all money fields

        - Apply discounts, shipping rates, and custom charges appropriately


        **Field Calculation Guidelines:**

        - **subtotal**: Sum of all item prices × quantities (before discounts)

        - **discount**: Total amount saved from coupons, promotions, and
        discounts

        - **shipping**: Calculated shipping cost based on address and selected
        method

        - **tax**: Sales tax, VAT, or other applicable taxes based on
        billing/shipping jurisdiction

        - **handling**: Processing fees, packaging costs, or handling charges

        - **insurance**: Optional shipping insurance costs

        - **shipping_discount**: Discounts applied specifically to shipping
        costs

        - **custom_charges**: Additional fees like gift wrapping, expedited
        processing, etc.

        - **total**: Final amount customer pays (subtotal - discount + shipping
        + tax + handling + insurance - shipping_discount + custom_charges)


        **PayPal Orders API Integration:**

        When creating PayPal orders, custom_charges are typically rolled into
        the handling field or added as separate line items.

        The total amount must match the PayPal order total for successful
        payment capture.

        Fields map to PayPal Orders API breakdown structure where supported.
      required:
        - total
      properties:
        subtotal:
          $ref: "#/components/schemas/Money"
          description: >
            Sum of all item prices multiplied by quantities before any discounts
            are applied.

            This represents the base cost of all products in the cart.


            **Calculation:** Σ(item.price.value × item.quantity) for all items
        discount:
          $ref: "#/components/schemas/Money"
          description: >
            Total amount saved from all applied discounts, coupons, and
            promotions.

            This should be a positive value representing savings to the
            customer.


            **Includes:** Coupon discounts, promotional offers, loyalty program
            savings, bulk discounts
        shipping:
          $ref: "#/components/schemas/Money"
          description: >
            Cost of shipping the order to the customer's shipping address.

            Based on selected shipping method, package weight/dimensions, and
            destination.


            **Calculation factors:** Shipping method, distance, package size,
            delivery speed
        tax:
          $ref: "#/components/schemas/Money"
          description: >
            Sales tax, VAT, or other applicable taxes based on billing/shipping
            jurisdiction.

            Calculated according to local tax regulations and product tax
            categories.


            **Tax basis:** Usually applied to (subtotal - discount + shipping)
            depending on local laws
        handling:
          $ref: "#/components/schemas/Money"
          description: >
            Processing fees, packaging costs, or handling charges for order
            fulfillment.


            **PayPal Orders API:** Maps directly to the handling field in
            PayPal's order breakdown.

            **Common uses:** Processing fees, packaging materials, order
            handling costs
        insurance:
          $ref: "#/components/schemas/Money"
          description: >
            Optional shipping insurance costs to protect against loss or damage
            during transit.


            **PayPal Orders API:** Maps directly to the insurance field in
            PayPal's order breakdown.

            **Typical usage:** High-value orders, fragile items, international
            shipping
        shipping_discount:
          $ref: "#/components/schemas/Money"
          description: >
            Discounts applied specifically to shipping costs (free shipping
            promotions, etc.).

            This should be a positive value representing shipping savings to the
            customer.


            **PayPal Orders API:** Maps directly to the shipping_discount field
            in PayPal's order breakdown.

            **Examples:** Free shipping promotions, reduced shipping rates,
            shipping coupons
        custom_charges:
          $ref: "#/components/schemas/Money"
          description: >
            Sum of all custom charges (gift wrap, processing fees, expedited
            handling, etc.).


            **PayPal Orders API Note:** This field doesn't map directly to
            PayPal Orders API breakdown.

            When creating PayPal orders, these charges are typically:

            - Rolled into the handling field, or

            - Added as separate line items in the order


            Merchants should ensure the total amount includes custom_charges for
            payment accuracy.
        total:
          $ref: "#/components/schemas/Money"
          description: >
            Final amount the customer will pay. This is the sum of all charges
            minus all discounts.


            **Formula:** subtotal - discount + shipping + tax + handling +
            insurance - shipping_discount + custom_charges

            **PayPal Orders API:** Must match the total amount in the PayPal
            order for successful payment capture.

            **Critical:** This is the amount that will be charged to the
            customer's payment method.
    AppliedCoupon:
      type: object
      description: Successfully applied coupon
      properties:
        code:
          type: string
          example: SAVE10
        description:
          type: string
          example: 10% off entire order
        discount_amount:
          $ref: "#/components/schemas/Money"
    ShippingOption:
      type: object
      description: Available shipping method with selection state
      required:
        - id
        - name
        - price
        - is_selected
      properties:
        id:
          type: string
          description: Unique shipping option identifier
          example: STANDARD_SHIPPING
        name:
          type: string
          description: Display name
          example: Standard Shipping (5-7 days)
        description:
          type: string
          description: Detailed description
          example: Standard ground shipping via USPS
        price:
          $ref: "#/components/schemas/Money"
        is_selected:
          type: boolean
          description: Whether this shipping option is currently selected
          example: true
        estimated_delivery:
          type: string
          format: date
          description: Estimated delivery date in YYYY-MM-DD format
          pattern: ^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$
          example: "2024-07-01"
    CartItem:
      type: object
      description: Product item for cart creation/updates
      required:
        - quantity
      properties:
        item_id:
          type: string
          description: >-
            Unique product identifier (DEPRECATED - optional in v1 for backwards
            compatibility)
          example: SHIRT-001
        variant_id:
          type: string
          description: >-
            Product variant identifier (color, size, etc.) - unique id of the
            product
          example: SHIRT-001-BLUE-M
        parent_id:
          type: string
          description: >-
            Item grouping identifier - passed when item is part of a group in
            product catalog
          example: SHIRT-COLLECTION-001
        quantity:
          type: integer
          description: Number of items
          minimum: 1
        name:
          type: string
          description: Product display name
          example: Blue Cotton T-Shirt
        description:
          type: string
          description: Product description
          example: Comfortable cotton t-shirt in blue
        item_url:
          type: string
          format: uri
          description: URL for product details page
          example: https://merchant.com/products/product_123
        price:
          $ref: "#/components/schemas/Money"
        selected_attributes:
          type: array
          description: Selected product attributes
          items:
            type: object
            properties:
              name:
                type: string
                example: Color
              value:
                type: string
                example: Blue
        gift_options:
          $ref: "#/components/schemas/GiftOptions"
        custom_options:
          type: array
          description: Custom product options
          items:
            type: object
            properties:
              name:
                type: string
                example: Engraving
              value:
                type: string
                example: Happy Birthday!
              price_modifier:
                type: string
                description: Additional cost for this option
                example: "5.00"
    Customer:
      type: object
      description: Represents customer information for the shopping cart.
      properties:
        name:
          type: object
          description: >-
            The name of the payer. Supports only the given_name and surname
            properties.
          properties:
            given_name:
              description: When the party is a person, the party's given, or first, name.
              type: string
              minLength: 0
              maxLength: 140
              pattern: ^.*$
              example: John
            surname:
              description: >-
                When the party is a person, the party's surname or family name.
                Also known as the last name. Required when the party is a
                person. Use also to store multiple surnames including the
                matronymic, or mother's, surname.
              type: string
              minLength: 0
              maxLength: 140
              pattern: ^.*$
              example: Smith
        phone:
          title: Phone
          description: >-
            The phone number in its canonical international E.164 numbering plan
            format.
          type: object
          required:
            - country_code
            - national_number
          properties:
            country_code:
              description: >-
                The country calling code (CC), in its canonical international
                E.164 numbering plan format. The combined length of the CC and
                the national number must not be greater than 15 digits. The
                national number consists of a national destination code (NDC)
                and subscriber number (SN).
              type: string
              minLength: 1
              maxLength: 3
              pattern: ^[0-9]{1,3}?$
              example: "1"
            national_number:
              description: >-
                The national number, in its canonical international E.164
                numbering plan format. The combined length of the country
                calling code (CC) and the national number must not be greater
                than 15 digits. The national number consists of a national
                destination code (NDC) and subscriber number (SN).
              type: string
              minLength: 1
              maxLength: 14
              pattern: ^[0-9]{1,14}?$
              example: "5551234567"
            extension_number:
              description: The extension number.
              type: string
              minLength: 1
              maxLength: 15
              pattern: ^[0-9]{1,15}?$
              example: "1234"
        email_address:
          description: >-
            The internationalized email address. Note: Up to 64 characters are
            allowed before and 255 characters are allowed after the @ sign.
            However, the generally accepted maximum length for an email address
            is 254 characters. The pattern verifies that an unquoted @ sign
            exists.
          type: string
          minLength: 3
          maxLength: 254
          pattern: >-
            ^(?:[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[A-Za-z0-9-]*[A-Za-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
          example: customer@example.com
    ShippingAddress:
      $ref: "#/components/schemas/Address"
      title: Shipping Address
      description: International shipping address for cart delivery.
    BillingAddress:
      $ref: "#/components/schemas/Address"
      title: Billing Address
      description: >
        Billing address for merchant business purposes, obtained from customer's
        PayPal profile.

        Similar to shipping addresses, billing addresses can be retrieved from
        customer's 

        default address information stored in their PayPal account.


        **When Billing Address is Available:**

        - Customer has a default billing address in their PayPal profile

        - PayPal Credit and Buy Now Pay Later transactions

        - Guest checkout with credit/debit cards  

        - User explicitly consents to address sharing

        - Required for tax compliance and regulatory reporting


        **Primary Use Cases:**

        - **Tax calculation**: Sales tax/VAT rates determined by billing
        jurisdiction

        - **Export compliance**: Product restrictions based on customer's
        billing country

        - **Financial reporting**: Accounting systems requiring customer billing
        location

        - **Address verification**: Comparing billing vs shipping addresses for
        fraud prevention


        **Secondary Use Cases:**

        - **Business intelligence**: Customer demographics and market analysis

        - **B2B invoicing**: Legal invoices requiring customer billing details

        - **Compliance reporting**: Regulatory requirements based on customer
        location


        **Note**: Payment verification (AVS) and chargeback protection are
        handled by PayPal internally.


        **Implementation Notes:**

        - Billing address is typically available from customer profile data

        - Can be populated during cart creation if customer provides it

        - Falls back to shipping address when billing address is not specified

        - Merchants should handle graceful fallback scenarios
    PaymentMethod:
      type: object
      description: >
        Payment method information for PayPal Cart API. This API is specifically
        designed

        for PayPal's shopping cart service, so only PayPal payment methods are
        supported.


        **Payment Flow:**

        1. Cart creation generates a payment token (in payment_method.token)

        2. Customer completes PayPal approval (Smart Wallet)

        3. PayPal provides token and payer_id for checkout

        4. Merchant receives PayPal payment confirmation


        **Billing Address Behavior:**

        - PayPal handles all billing address collection internally for payment
        processing

        - Merchants can optionally collect billing addresses for tax calculation
        and business purposes

        - Billing address in cart is for merchant use cases, not payment
        requirements

        - Billing addresses are typically available from customer profile data


        **Note:** Other payment methods (credit cards, Apple Pay, etc.) would be
        handled

        by separate merchant payment systems outside of this PayPal Cart API.
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - paypal
          description: Payment method type - only PayPal is supported by this API
          example: paypal
        token:
          type: string
          description: PayPal payment token from cart creation or customer approval
          example: EC-7U8939823K567
        payer_id:
          type: string
          description: PayPal payer identifier provided after customer approval
          example: PAYER123456789
        approval_url:
          type: string
          format: uri
          description: URL used to inform merchant that the PayPal buyer approved the order
          example: https://paypal.com/checkoutnow?token=EC-7U8939823K567
    CheckoutField:
      type: object
      description: >
        PayPal-controlled checkout field for buyer data collection with
        structured values and validation.


        **Field Lifecycle:**

        - PENDING: Field needs customer input

        - COMPLETED: Valid value provided and accepted

        - REJECTED: Invalid/unacceptable value provided

        - ERROR: System error during processing


        **Structured Values:**

        Each field type has a specific value schema based on its requirements.

        Age verification uses boolean confirmation, text fields use strings,
        etc.
      required:
        - type
        - status
      properties:
        type:
          type: string
          description: PayPal-approved checkout field type
          enum:
            - AGE_VERIFICATION_18_PLUS
            - AGE_VERIFICATION_21_PLUS
            - GIFT_RECIPIENT_EMAIL
            - GIFT_RECIPIENT_NAME
            - GIFT_MESSAGE
            - DELIVERY_INSTRUCTIONS
            - DELIVERY_DATE_PREFERENCE
            - ALLERGY_INFORMATION
            - CUSTOM_ENGRAVING_TEXT
            - CUSTOM_SIZING_INFO
            - TERMS_ACCEPTANCE
            - PRIVACY_CONSENT
          example: AGE_VERIFICATION_21_PLUS
        status:
          type: string
          description: |
            Field completion and validation status:

            **PENDING**: Field needs customer input
            - Initial state when field is required
            - AI agent should collect this information
            - value field is null or empty

            **COMPLETED**: Valid value provided and accepted
            - Customer provided acceptable input
            - Value passes all validation rules
            - Cart can proceed with this field resolved

            **REJECTED**: Invalid or unacceptable value provided
            - Customer provided input that doesn't meet requirements
            - validation_issue explains the specific problem
            - AI agent should request corrected input

            **ERROR**: System error during processing
            - Technical failure in field processing
            - Should retry or escalate to support
            - Not caused by customer input
          enum:
            - PENDING
            - COMPLETED
            - REJECTED
            - ERROR
          example: COMPLETED
        value:
          description: >
            Structured value based on field type. Each checkout field type has a
            specific value schema.

            Use oneOf to validate against the appropriate structure for the
            field type.
          oneOf:
            - $ref: "#/components/schemas/AgeVerificationValue"
            - $ref: "#/components/schemas/GiftRecipientEmailValue"
            - $ref: "#/components/schemas/GiftRecipientNameValue"
            - $ref: "#/components/schemas/GiftMessageValue"
            - $ref: "#/components/schemas/DeliveryInstructionsValue"
            - $ref: "#/components/schemas/DeliveryDatePreferenceValue"
            - $ref: "#/components/schemas/AllergyInformationValue"
            - $ref: "#/components/schemas/CustomEngravingTextValue"
            - $ref: "#/components/schemas/CustomSizingInfoValue"
            - $ref: "#/components/schemas/TermsAcceptanceValue"
            - $ref: "#/components/schemas/PrivacyConsentValue"
          nullable: true
        context:
          type: object
          description: >
            Additional context and metadata for the checkout field. This is a
            flexible object

            that can contain any field-specific information needed for
            validation, display,

            or processing. The structure varies based on the field type.
          additionalProperties: true
          example:
            age_verification_21_plus:
              display_name: Age Verification (21+)
              description: >-
                We need to verify you are 21 or older to purchase alcoholic
                beverages
              required: true
              min_age: 21
              verification_methods:
                - self_declaration
                - id_scan
                - third_party
              compliance_note: Required by state law for alcohol purchases
              help_text: >-
                This is required for alcohol purchases in compliance with local
                laws
            gift_message:
              display_name: Gift Message
              description: Personal message for the gift recipient
              max_length: 500
              allowed_characters: letters, numbers, spaces, and basic punctuation
              placeholder: Enter your personal message for the recipient
              character_counter: true
              preview_available: true
            delivery_instructions:
              display_name: Special Delivery Instructions
              description: Additional instructions for delivery driver
              max_length: 200
              placeholder: e.g., Leave at front door, ring doorbell
              examples:
                - Leave at front door
                - Ring doorbell
                - Call upon arrival
              optional_fields:
                - access_code
                - contact_phone
            custom_engraving:
              display_name: Custom Engraving Text
              description: Text to be engraved on your item
              max_length: 100
              font_options:
                - arial
                - times
                - script
                - block
              position_options:
                - front
                - back
                - side
                - bottom
              character_limit_per_line: 25
              max_lines: 4
              prohibited_content:
                - profanity
                - copyrighted_text
                - personal_info
              preview_available: true
              additional_cost: 15
            allergy_information:
              display_name: Allergy Information
              description: Please list any allergies or dietary restrictions
              common_allergies:
                - peanuts
                - tree nuts
                - dairy
                - gluten
                - shellfish
                - eggs
              severity_levels:
                - mild
                - moderate
                - severe
                - life_threatening
              emergency_contact_required: true
              medical_alert_bracelet: recommended_for_severe
            custom_sizing:
              display_name: Custom Measurements
              description: Provide your measurements for custom fit
              measurement_units:
                - inches
                - centimeters
              required_measurements:
                - chest
                - waist
                - inseam
              optional_measurements:
                - shoulder
                - neck
                - sleeve
              measurement_guide_url: https://example.com/measurement-guide
              size_chart_available: true
              fit_guarantee: true
        validation_issue:
          $ref: "#/components/schemas/ValidationIssue"
          description: >
            Associated validation issue when status is REJECTED or ERROR.

            Provides detailed information about why the field value was not
            accepted.


            **When present:**

            - status is REJECTED: Customer input didn't meet requirements

            - status is ERROR: System error processing the field


            **When null:**

            - status is PENDING: No validation attempted yet

            - status is COMPLETED: Validation passed successfully
    Coupon:
      type: object
      description: >
        Discount coupon for cart operations. Multiple coupons can be applied
        simultaneously,

        with merchant business rules determining stacking behavior, priorities,
        and conflicts.


        **Common Scenarios:**

        - Apply multiple discount codes (percentage + fixed amount)

        - Stack loyalty discounts with promotional codes  

        - Remove specific coupons while keeping others

        - Apply category-specific and store-wide discounts together


        **Business Rules:**

        Merchants define stacking rules, maximum discounts, exclusions, and
        priority orders.

        Invalid combinations return validation issues with suggested
        resolutions.
      required:
        - code
        - action
      properties:
        code:
          type: string
          description: Coupon code identifier
          example: SAVE10
        action:
          type: string
          enum:
            - APPLY
            - REMOVE
          description: Action to perform on this specific coupon
          example: APPLY
    GeoCoordinates:
      type: object
      description: >
        Geographic coordinates with administrative division information for
        precise location services.

        Useful for enhanced delivery routing, location-based services, and
        regional compliance.
      properties:
        latitude:
          type: string
          description: Latitude coordinate in decimal degrees (-90 to 90). WGS84 datum.
          pattern: ^-?([1-8]?[0-9](\.\d+)?|90(\.0+)?)$
          example: "37.7749"
        longitude:
          type: string
          description: Longitude coordinate in decimal degrees (-180 to 180). WGS84 datum.
          pattern: ^-?((1[0-7]|[1-9])?[0-9](\.\d+)?|180(\.0+)?)$
          example: "-122.4194"
        subdivision:
          type: string
          description: >-
            Administrative subdivision code (state, province, region). ISO
            3166-2 format without country prefix (e.g., 'CA' for California,
            'ON' for Ontario).
          minLength: 1
          maxLength: 10
          pattern: ^[A-Z0-9-]+$
          example: CA
        country_code:
          type: string
          description: ISO 3166-1 alpha-2 country code for the coordinate location.
          minLength: 2
          maxLength: 2
          pattern: ^[A-Z]{2}$
          example: US
    BusinessIssueCode:
      description: >
        Union of all specific_issue codes from ValidationIssue context schemas.

        Used in BusinessError.details.issue to standardize 422 error responses.

        Adding a value to any individual issue code schema automatically
        includes

        it here.
      anyOf:
        - $ref: "#/components/schemas/InventoryIssueCode"
        - $ref: "#/components/schemas/PricingIssueCode"
        - $ref: "#/components/schemas/ShippingIssueCode"
        - $ref: "#/components/schemas/PaymentIssueCode"
        - $ref: "#/components/schemas/DataIssueCode"
        - $ref: "#/components/schemas/BusinessRuleIssueCode"
    InventoryIssueContext:
      type: object
      description: Context for inventory and stock-related issues
      properties:
        specific_issue:
          $ref: "#/components/schemas/InventoryIssueCode"
        item_id:
          type: string
          description: Product item identifier
        variant_id:
          type: string
          description: Product variant identifier if applicable
        available_quantity:
          type: integer
          description: Currently available quantity
          minimum: 0
        requested_quantity:
          type: integer
          description: Requested quantity
          minimum: 1
        reserved_quantity:
          type: integer
          description: Quantity reserved for other transactions
          minimum: 0
        restock_date:
          type: string
          format: date-time
          description: Expected restock date
        estimated_ship_date:
          type: string
          format: date-time
          description: Estimated shipping date for back-orders
        back_order_limit:
          type: integer
          description: Maximum allowed back-order quantity
        current_back_orders:
          type: integer
          description: Current number of back-orders
        discontinuation_date:
          type: string
          format: date-time
          description: Date product was discontinued
        suggested_alternatives:
          type: array
          items:
            type: string
          description: Alternative product IDs
        upgrade_available:
          type: boolean
          description: Whether newer version is available
        seasonal_start_date:
          type: string
          format: date-time
          description: When seasonal product becomes available
        last_sold:
          type: string
          format: date-time
          description: When item was last sold
    PricingErrorContext:
      type: object
      description: Context for pricing and financial issues
      properties:
        specific_issue:
          $ref: "#/components/schemas/PricingIssueCode"
        item_id:
          type: string
          description: Item with pricing issue
        original_price:
          type: string
          description: Original price value
        current_price:
          type: string
          description: Current price value
        currency_code:
          type: string
          description: Currency code
        price_change_reason:
          type: string
          description: Reason for price change
          enum:
            - promotional_ended
            - promotional_started
            - market_adjustment
            - cost_increase
            - seasonal_pricing
            - component_cost_increase
            - terms_updated
        price_increase:
          type: string
          description: Amount of price increase
        price_decrease:
          type: string
          description: Amount of price decrease
        coupon_code:
          type: string
          description: Coupon code with issues
        usage_limit:
          type: integer
          description: Coupon usage limit
        current_usage:
          type: integer
          description: Current coupon usage count
        expiration_date:
          type: string
          format: date-time
          description: Discount expiration date
        minimum_order_amount:
          type: string
          description: Minimum order for discount
        supported_currencies:
          type: array
          items:
            type: string
          description: List of supported currencies
        found_currencies:
          type: array
          items:
            type: string
          description: Multiple currencies found in cart
        tax_service_error:
          type: string
          description: Tax calculation service error
        current_date:
          type: string
          format: date-time
          description: Current system date for comparisons
        discount_amount:
          type: string
          description: Discount amount that was applied
        required_currency_consistency:
          type: boolean
          description: Whether all items must use same currency
        mixed_items:
          type: array
          items:
            type: object
            properties:
              item_id:
                type: string
              currency:
                type: string
          description: Items with different currencies
    ShippingErrorContext:
      type: object
      description: Context for shipping and address issues
      properties:
        specific_issue:
          $ref: "#/components/schemas/ShippingIssueCode"
        validation_failures:
          type: array
          items:
            type: string
          description: Specific address validation failures
        suggested_corrections:
          type: object
          description: Suggested address corrections
          properties:
            postal_code:
              type: string
            address_line_1:
              type: string
            admin_area_2:
              type: string
        address_quality_score:
          type: number
          minimum: 0
          maximum: 1
          description: Address validation quality score
        restricted_items:
          type: array
          items:
            type: string
          description: Items with shipping restrictions
        restriction_reason:
          type: string
          description: Reason for shipping restriction
          enum:
            - signature_required
            - age_verification_required
            - export_controlled
            - hazardous_material
            - oversized_item
            - po_box_restriction
        po_box_detected:
          type: boolean
          description: Whether PO Box was detected
        destination_country:
          type: string
          description: Destination country code
        restricted_region:
          type: string
          description: Restricted region identifier
        supported_countries:
          type: array
          items:
            type: string
          description: List of supported countries
        provided_address:
          type: string
          description: Address string that failed validation
    PaymentErrorContext:
      type: object
      description: Context for payment processing issues
      properties:
        specific_issue:
          $ref: "#/components/schemas/PaymentIssueCode"
        order_total:
          type: string
          description: Total order amount
        payment_limit:
          type: string
          description: Maximum payment limit
        minimum_amount:
          type: string
          description: Minimum payment amount
        excess_amount:
          type: string
          description: Amount exceeding limit
        payment_method:
          type: string
          description: Payment method being used
        currency_code:
          type: string
          description: Transaction currency
        from_currency:
          type: string
          description: Source currency for conversion
        to_currency:
          type: string
          description: Target currency for conversion
        conversion_service:
          type: string
          description: Currency conversion service status
        supported_payment_methods:
          type: array
          items:
            type: string
          description: List of supported payment methods
        processor_error_code:
          type: string
          description: Payment processor specific error code
        decline_reason:
          type: string
          description: Reason for payment decline
        payment_token:
          type: string
          description: Payment token that was declined
    DataErrorContext:
      type: object
      description: Context for data validation issues
      properties:
        specific_issue:
          $ref: "#/components/schemas/DataIssueCode"
        field_name:
          type: string
          description: Name of the field with validation error
        provided_value:
          type: string
          description: Value that failed validation
        expected_format:
          type: string
          description: Expected format description
        max_length:
          type: integer
          description: Maximum allowed length
        min_length:
          type: integer
          description: Minimum required length
        current_length:
          type: integer
          description: Current value length
        regex_pattern:
          type: string
          description: Required regex pattern
        suggested_value:
          type: string
          description: Suggested corrected value
        allowed_values:
          type: array
          items:
            type: string
          description: List of allowed values for enum fields
        required_fields:
          type: array
          items:
            type: string
          description: List of required field names
        field_descriptions:
          type: object
          additionalProperties: true
          description: Descriptions for required fields
    BusinessRuleErrorContext:
      type: object
      description: Context for business logic violations
      properties:
        specific_issue:
          $ref: "#/components/schemas/BusinessRuleIssueCode"
        current_amount:
          type: string
          description: Current order amount
        required_amount:
          type: string
          description: Required minimum amount
        maximum_amount:
          type: string
          description: Maximum allowed amount
        remaining_amount:
          type: string
          description: Amount needed to meet minimum
        account_status:
          type: string
          description: Customer account status
        suspension_reason:
          type: string
          description: Reason for account suspension
        suspension_date:
          type: string
          format: date-time
          description: Date of account suspension
        monthly_limit:
          type: string
          description: Monthly purchase limit
        current_month_total:
          type: string
          description: Current month purchase total
        reset_date:
          type: string
          format: date-time
          description: When limits reset
        total_quantity:
          type: integer
          description: Total quantity in bulk order
        approval_threshold:
          type: integer
          description: Quantity requiring approval
        maintenance_end_time:
          type: string
          format: date-time
          description: When maintenance ends
        service_status:
          type: string
          description: Current service status
        retry_after:
          type: integer
          description: Seconds before retry recommended
        contact_info:
          type: string
          description: Support contact information
        restricted_items:
          type: array
          items:
            type: string
          description: Items with restrictions
        age_requirement:
          type: integer
          description: Required minimum age
        business_hours:
          type: object
          description: Store business hours
          properties:
            open_time:
              type: string
            close_time:
              type: string
            timezone:
              type: string
        shortage_amount:
          type: string
          description: Amount needed to meet minimum requirements
        exceeds_by:
          type: string
          description: Amount by which limit is exceeded
    ResolutionOption:
      type: object
      description: Available action to resolve a validation issue
      required:
        - action
        - label
      properties:
        action:
          type: string
          description: Machine-readable action identifier
          enum:
            - REDIRECT_TO_MERCHANT
            - MODIFY_CART
            - ACCEPT_NEW_PRICE
            - ACCEPT_BACK_ORDER
            - SUGGEST_ALTERNATIVE
            - REMOVE_ITEM
            - UPDATE_ADDRESS
            - PROVIDE_MISSING_FIELD
            - USE_DIFFERENT_PAYMENT
            - SPLIT_ORDER
            - CONTACT_SUPPORT
            - RETRY_LATER
            - REQUEST_APPROVAL
            - WAIT_FOR_RESTOCK
            - USE_DIFFERENT_CURRENCY
            - ACCEPT_PRE_ORDER
            - UPDATE_SHIPPING_METHOD
            - ACCEPT_TERMS
            - VERIFY_ACCOUNT
            - APPLY_DIFFERENT_COUPON
            - REMOVE_COUPON
            - CHOOSE_DIFFERENT_VARIANT
        label:
          type: string
          description: Human-readable action label
          example: View similar colors
        url:
          type: string
          format: uri
          description: URL to redirect to for resolution
        metadata:
          type: object
          description: Additional action metadata
          properties:
            cost_impact:
              type: string
              description: Financial impact of this action
              example: +$5.00
            priority:
              type: string
              enum:
                - HIGH
                - MEDIUM
                - LOW
              description: Priority level for this resolution
            auto_applicable:
              type: boolean
              description: Whether this action can be applied automatically
            estimated_time:
              type: string
              description: Estimated time for resolution
              example: 2-3 weeks
            redirect_required:
              type: boolean
              description: Whether this action requires user redirect
    Money:
      type: object
      description: Monetary amount with currency
      required:
        - currency_code
        - value
      properties:
        currency_code:
          description: The 3-character ISO-4217 currency code that identifies the currency.
          type: string
          minLength: 3
          maxLength: 3
          pattern: ^[\S\s]*$
          example: USD
        value:
          description: >-
            The value, which might be: An integer for currencies like JPY that
            are not typically fractional. A decimal fraction for currencies like
            TND that are subdivided into thousandths. For the required number of
            decimal places for a currency code, see Currency Codes.
          type: string
          minLength: 0
          maxLength: 32
          pattern: ^((-?[0-9]+)|(-?([0-9]+)?[.][0-9]+))$
          example: "25.00"
    GiftOptions:
      type: object
      description: Gift-specific options
      properties:
        is_gift:
          type: boolean
          description: Whether this is a gift
          example: true
        recipient:
          type: object
          description: Gift recipient information
          properties:
            name:
              type: string
              example: Mary Johnson
            email:
              type: string
              format: email
              example: mary@example.com
            phone:
              type: string
              example: +1-555-987-6543
        delivery_date:
          type: string
          format: date-time
          description: >-
            Scheduled delivery date in RFC3339 format. Seconds are required
            while fractional seconds are optional.
          minLength: 20
          maxLength: 64
          pattern: >-
            ^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])[T,t]([0-1][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)([.][0-9]+)?([Zz]|[+-][0-9]{2}:[0-9]{2})$
          example: "2024-12-25T09:00:00Z"
        sender_name:
          type: string
          description: Name of gift sender
          example: John Smith
        gift_message:
          type: string
          description: Personal message (max 500 characters)
          maxLength: 500
          example: Happy Birthday! Hope you enjoy this gift.
        gift_wrap:
          type: boolean
          description: Whether to include gift wrapping
          example: true
    Address:
      title: Address
      description: >-
        Base address schema used for both shipping and billing addresses. Maps
        to AddressValidationMetadata and HTML 5.1 Autofilling form controls the
        autocomplete attribute.
      type: object
      required:
        - country_code
      properties:
        address_line_1:
          description: >-
            The first line of the address, such as number and street, for
            example, `173 Drury Lane`. Needed for data entry, and Compliance and
            Risk checks. This field needs to pass the full address.
          type: string
          minLength: 0
          maxLength: 300
          pattern: ^.*$
          example: 123 Main Street
        address_line_2:
          description: >-
            The second line of the address, for example, a suite or apartment
            number.
          type: string
          minLength: 0
          maxLength: 300
          pattern: ^.*$
          example: Apt 4B
        admin_area_2:
          description: A city, town, or village. Smaller than `admin_area_level_1`.
          type: string
          minLength: 0
          maxLength: 120
          pattern: ^.*$
          example: San Jose
        admin_area_1:
          description: >-
            The highest-level sub-division in a country, which is usually a
            province, state, or ISO-3166-2 subdivision. This data is formatted
            for postal delivery, for example, `CA` and not `California`. Value,
            by country, is UK. A county. US. A state. Canada. A province. Japan.
            A prefecture. Switzerland. A *kanton*.
          type: string
          minLength: 0
          maxLength: 300
          pattern: ^.*$
          example: CA
        postal_code:
          description: >-
            The postal code, which is the ZIP code or equivalent. Typically
            required for countries with a postal code or an equivalent. See
            postal code.
          type: string
          minLength: 0
          maxLength: 60
          pattern: ^.*$
          example: "95131"
        country_code:
          description: The 2-character ISO 3166-1 alpha-2 country code
          type: string
          minLength: 2
          maxLength: 2
          pattern: ^[A-Z]{2}$
          example: US
    AgeVerificationValue:
      type: object
      description: Age verification confirmation value
      required:
        - type
        - confirmed
      properties:
        type:
          type: string
          enum:
            - AGE_VERIFICATION_18_PLUS
            - AGE_VERIFICATION_21_PLUS
          description: This should match the CheckField type.
          example: AGE_VERIFICATION_21_PLUS
        confirmed:
          type: boolean
          description: Whether age verification was confirmed
          example: true
        verification_method:
          type: string
          enum:
            - self_declaration
            - id_verification
            - third_party
          description: Method used for age verification
          example: self_declaration
        verification_date:
          type: string
          format: date-time
          description: When verification was completed
          example: "2024-06-24T14:30:00Z"
    GiftRecipientEmailValue:
      type: object
      description: Gift recipient email information
      required:
        - type
        - email
      properties:
        type:
          type: string
          enum:
            - GIFT_RECIPIENT_EMAIL
          description: This should match the CheckField type.
        email:
          type: string
          format: email
          description: Recipient's email address
          example: recipient@example.com
        verified:
          type: boolean
          description: Whether email was verified
          example: true
    GiftRecipientNameValue:
      type: object
      description: Gift recipient name information
      required:
        - type
        - name
      properties:
        type:
          type: string
          enum:
            - GIFT_RECIPIENT_NAME
          description: This should match the CheckField type.
        name:
          type: string
          description: Recipient's full name
          example: Mary Johnson
        first_name:
          type: string
          description: Recipient's first name
          example: Mary
        last_name:
          type: string
          description: Recipient's last name
          example: Johnson
    GiftMessageValue:
      type: object
      description: Gift message content
      required:
        - type
        - message
      properties:
        type:
          type: string
          enum:
            - GIFT_MESSAGE
          description: This should match the CheckField type.
        message:
          type: string
          maxLength: 500
          description: Personal message for the recipient
          example: Happy Birthday! Hope you enjoy this gift card.
        sender_name:
          type: string
          description: Name of the person sending the gift
          example: John Smith
    DeliveryInstructionsValue:
      type: object
      description: Special delivery instructions
      required:
        - type
        - instructions
      properties:
        type:
          type: string
          enum:
            - DELIVERY_INSTRUCTIONS
          description: This should match the CheckField type.
        instructions:
          type: string
          maxLength: 200
          description: Special delivery instructions
          example: Leave at front door, ring doorbell
        access_code:
          type: string
          description: Building or gate access code
          example: "1234"
        contact_phone:
          type: string
          description: Contact phone for delivery
          example: +1-555-123-4567
    DeliveryDatePreferenceValue:
      type: object
      description: Preferred delivery date and time
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - DELIVERY_DATE_PREFERENCE
          description: This should match the CheckField type.
        preferred_date:
          type: string
          format: date
          description: Preferred delivery date
          example: "2024-06-28"
        time_window:
          type: string
          enum:
            - morning
            - afternoon
            - evening
            - anytime
          description: Preferred time window
          example: morning
        specific_time:
          type: string
          pattern: ^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$
          description: Specific preferred time (HH:MM format)
          example: "14:30"
    AllergyInformationValue:
      type: object
      description: Allergy and medical restriction information
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - ALLERGY_INFORMATION
          description: This should match the CheckField type.
        allergies:
          type: array
          items:
            type: string
          description: List of known allergies
          example:
            - peanuts
            - shellfish
            - latex
        severity:
          type: string
          enum:
            - mild
            - moderate
            - severe
            - life_threatening
          description: Allergy severity level
          example: severe
        medications:
          type: array
          items:
            type: string
          description: Medications to avoid
          example:
            - aspirin
            - ibuprofen
        emergency_contact:
          type: string
          description: Emergency contact information
          example: +1-555-999-8888
    CustomEngravingTextValue:
      type: object
      description: Custom engraving text specification
      required:
        - type
        - text
      properties:
        type:
          type: string
          enum:
            - CUSTOM_ENGRAVING_TEXT
          description: This should match the CheckField type.
        text:
          type: string
          maxLength: 100
          description: Text to be engraved
          example: Property of John Smith
        font:
          type: string
          enum:
            - arial
            - times
            - script
            - block
          description: Preferred font style
          example: script
        size:
          type: string
          enum:
            - small
            - medium
            - large
          description: Text size preference
          example: medium
        position:
          type: string
          enum:
            - front
            - back
            - side
            - bottom
          description: Engraving position
          example: back
    CustomSizingInfoValue:
      type: object
      description: Custom sizing measurements
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - CUSTOM_SIZING_INFO
          description: This should match the CheckField type.
        measurements:
          type: object
          description: Body measurements
          properties:
            chest:
              type: string
              description: Chest measurement
              example: 42 inches
            waist:
              type: string
              description: Waist measurement
              example: 34 inches
            height:
              type: string
              description: Height measurement
              example: 6 feet 2 inches
            weight:
              type: string
              description: Weight
              example: 180 lbs
        size_preference:
          type: string
          enum:
            - tight
            - regular
            - loose
          description: Fit preference
          example: regular
        special_requirements:
          type: string
          description: Special sizing requirements
          example: Extra long sleeves
    TermsAcceptanceValue:
      type: object
      description: Terms and conditions acceptance
      required:
        - type
        - accepted
        - terms_version
      properties:
        type:
          type: string
          enum:
            - TERMS_ACCEPTANCE
          description: This should match the CheckField type.
        accepted:
          type: boolean
          description: Whether terms were accepted
          example: true
        terms_version:
          type: string
          description: Version of terms accepted
          example: v2024.6
        acceptance_date:
          type: string
          format: date-time
          description: When terms were accepted
          example: "2024-06-24T14:30:00Z"
        ip_address:
          type: string
          description: IP address of acceptance
          example: 192.168.1.100
    PrivacyConsentValue:
      type: object
      description: Privacy policy consent
      required:
        - type
        - consented
      properties:
        type:
          type: string
          enum:
            - PRIVACY_CONSENT
          description: This should match the CheckField type.
        consented:
          type: boolean
          description: Whether privacy policy was consented to
          example: true
        consent_types:
          type: array
          items:
            type: string
            enum:
              - data_processing
              - marketing
              - third_party_sharing
              - analytics
          description: Types of consent given
          example:
            - data_processing
            - analytics
        policy_version:
          type: string
          description: Privacy policy version
          example: v2024.6
        consent_date:
          type: string
          format: date-time
          description: When consent was given
          example: "2024-06-24T14:30:00Z"
    InventoryIssueCode:
      type: string
      description: Specific inventory issue type
      enum:
        - ITEM_OUT_OF_STOCK
        - INSUFFICIENT_INVENTORY
        - BACK_ORDERED
        - PRE_ORDER_ONLY
        - ITEM_DISCONTINUED
        - LOW_STOCK_WARNING
        - INVENTORY_RESERVED
        - SEASONAL_UNAVAILABLE
        - VARIANT_NOT_AVAILABLE
        - CUSTOM_OPTION_UNAVAILABLE
    PricingIssueCode:
      type: string
      description: Specific pricing issue type
      enum:
        - PRICE_MISMATCH
        - DISCOUNT_EXPIRED
        - DISCOUNT_USAGE_LIMIT_EXCEEDED
        - DISCOUNT_CUSTOMER_INELIGIBLE
        - DISCOUNT_MINIMUM_NOT_MET
        - TAX_CALCULATION_FAILED
        - CURRENCY_NOT_SUPPORTED
        - CURRENCY_MISMATCH
        - PROMOTIONAL_CONFLICT
    ShippingIssueCode:
      type: string
      description: Specific shipping issue type
      enum:
        - MISSING_SHIPPING_ADDRESS
        - SHIPPING_ADDRESS_INVALID
        - SHIPPING_TO_PO_BOX_NOT_ALLOWED
        - NO_SHIPPING_OPTIONS
        - INTERNATIONAL_SHIPPING_RESTRICTED
        - REGION_RESTRICTED
        - OVERSIZED_ITEM_SHIPPING
        - HAZARDOUS_MATERIAL_SHIPPING
        - SHIPPING_ZONE_NOT_COVERED
        - MISSING_COORDINATES_FOR_ENHANCED_DELIVERY
    PaymentIssueCode:
      type: string
      description: Specific payment issue type
      enum:
        - PAYMENT_AMOUNT_TOO_LARGE
        - PAYMENT_AMOUNT_TOO_SMALL
        - PAYMENT_METHOD_NOT_ACCEPTED
        - CURRENCY_CONVERSION_FAILED
        - PAYMENT_PROCESSOR_UNAVAILABLE
        - MERCHANT_ACCOUNT_ISSUE
        - PAYMENT_DECLINED
        - PAYMENT_INSUFFICIENT_FUNDS
        - PAYMENT_EXPIRED
        - PAYMENT_FRAUD_DETECTED
    DataIssueCode:
      type: string
      description: Specific data validation issue type
      enum:
        - MISSING_CHECKOUT_FIELDS
        - MISSING_PAYMENT_METHOD
        - MISSING_POLICY_ACCEPTANCE
        - REQUIRED_FIELD_MISSING
        - INVALID_EMAIL_FORMAT
        - INVALID_PHONE_FORMAT
        - FIELD_VALUE_TOO_LONG
        - FIELD_VALUE_TOO_SHORT
        - INVALID_DATE_FORMAT
        - FUTURE_DATE_NOT_ALLOWED
        - INVALID_CUSTOMER_DATA
        - ITEM_NOT_FOUND
        - INVALID_ITEM_DATA
        - ITEM_ATTRIBUTE_MISMATCH
    BusinessRuleIssueCode:
      type: string
      description: Specific business rule issue type
      enum:
        - MINIMUM_ORDER_NOT_MET
        - MINIMUM_QUANTITY_NOT_MET
        - MAXIMUM_QUANTITY_EXCEEDED
        - CART_LIMIT_EXCEEDED
        - CUSTOMER_ACCOUNT_SUSPENDED
        - PURCHASE_LIMIT_EXCEEDED
        - BULK_ORDER_APPROVAL_REQUIRED
        - STORE_TEMPORARILY_CLOSED
        - AGE_RESTRICTED_PRODUCT
        - LOYALTY_PROGRAM_VALIDATION_FAILED
        - BUSINESS_HOURS_RESTRICTION
        - PRODUCT_ARCHIVED
  securitySchemes:
    PayPalJWT:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >
        PayPal-supplied JWT token for authenticating merchant API requests.


        **Important:** These JWT tokens are issued and managed by PayPal, not
        generated by merchants.

        PayPal provides these tokens to authenticate calls to your merchant API
        endpoints.


        **Usage:**

        - Include in Authorization header as "Bearer <paypal-jwt-token>"

        - Token is supplied by PayPal Shopping Cart service

        - Verify token signature using PayPal's public keys

        - Extract merchant identification from token claims


        **Example:**

        ```

        Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

        ```
````
