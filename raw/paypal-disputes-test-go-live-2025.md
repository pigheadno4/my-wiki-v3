<!-- Source URL: https://docs.paypal.ai/growth/disputes/test-go-live -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test and go live

Implement and validate the PayPal Disputes API in sandbox and live environments as a developer or QA engineer.

## Simulate test scenarios

Before going live, you can use the PayPal sandbox environment to test the Disputes API integration. This ensures it works as expected and meets all business and technical requirements.

### Prerequisites

1. Ensure you <a href="/growth/disputes/set-up#disputes-api" target="_blank" rel="noopener noreferrer">set up the sandbox environment</a>.
2. Ensure you <a href="/growth/disputes/set-up#set-up-buyer-side-credentials" target="_blank" rel="noopener noreferrer">set up buyer-side credentials</a> in the sandbox environment. This is required to [create disputes](#create-dispute) or [change dispute reasons](#change-dispute-reason) as a buyer.

### Simulate buyer actions

Before testing dispute responses for your integration, you need to simulate buyer actions to create the disputes and transactions in the sandbox environment.

<AccordionGroup>
  <Accordion title="Create transaction">
    To create a transaction in the sandbox environment, do these steps:

    1. Log in to your <a href="https://www.sandbox.paypal.com/" target="_blank" rel="noopener noreferrer">sandbox personal account</a> as a buyer.
    2. Select **Send and Request** and follow the on-page instructions to send money to your sandbox business account's email ID.
       <Note>For a transaction to be eligible for chargeback, ensure you use a credit card to send money.</Note>
    3. Select **Go to Summary**.
    4. In the **Recent activity** section, select the transaction.
    5. On the **Summary** page, copy the **Transaction ID**. Use this value to [create a dispute](#create-dispute).

  </Accordion>

  <Accordion title="Create dispute">
    You can create disputes as a buyer using this endpoint and test how to handle them in the sandbox environment.

    <Note>This is a sandbox-only endpoint. You cannot use it to create disputes in the live environment.</Note>

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a>, include the <a href="/growth/disputes/set-up#use-paypal-auth-assertion-request-header" target="_blank" rel="noopener noreferrer">PayPal-Auth-Assertion request header with a valid JWT</a>, and make a `POST` call to the `/v1/customer/disputes` endpoint. Include the following parameters:

    | Parameter                                                                                       | Description                                                                                                                                                                        | Action                                                                                                                         |
    | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
    | `disputed_transactions`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span> | Array of transaction details for which the dispute is created.                                                                                                                     | Pass the transaction ID retrieved after [creating a transaction](#create-transaction) in the `buyer_transaction_id` parameter. |
    | `reason`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>               | Reason for the dispute. <Note>For more information, see <a href="/growth/disputes/reference/dispute-reasons" target="_blank" rel="noopener noreferrer">Dispute reasons</a>.</Note> | Pass the reason for which you are disputing the transaction.                                                                   |
    | `dispute_amount`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>       | Currency and value of the amount in dispute. The amount value must be less than or equal to the transaction amount of the [created transaction](#create-transaction).              | Pass the currency and amount details.                                                                                          |
    | `extensions`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>           | Additional dispute details, including whether the merchant was contacted, the contact outcome, and the issue type.                                                                 | Pass the additional dispute details as needed.                                                                                 |

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes \
      -H 'Authorization: Bearer ACCESS-TOKEN' \
      -H 'Content-Type: multipart/form-data' \
      -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
      -F 'input={
          "disputed_transactions": [{
              "buyer_transaction_id": "BUYER-TRANSACTION-ID"
              }],
          "reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
          "dispute_amount": {
              "currency_code":"USD",
              "value": "20"
              },
          "extensions": {
              "merchant_contacted": true,
              "merchant_contacted_outcome": "NO_RESPONSE",
              "merchandize_dispute_properties": {
                "issue_type": "PRODUCT"
              }
          }
      };type=application/json'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns a `201 Created` response and an HATEOAS link for the dispute. Use the dispute ID from the HATEOAS link to perform subsequent tests on the dispute.

    To test Accelerated Response, see [Accelerated Response sandbox testing](/growth/disputes/test-go-live#accelerated-response-sandbox-testing).

  </Accordion>

  <Accordion title="Create chargeback">
    You can create chargebacks using this endpoint and test how to handle them in the sandbox environment.

    <Note>This is a sandbox-only endpoint. You cannot use it to create chargebacks in the live environment.</Note>

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v2/customer-support/process-chargeback` endpoint. Include the following parameters:

    | Parameter                                                                                                                                                                     | Description                                                                                                               | Action                                                                                                                                    |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | `adjacency`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                       | Payment method used for the transaction.                                                                                  | Set the value as `PAYPAL` for PayPal transactions.                                                                                        |
    | `file_layout`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                     | Format or layout for the chargeback event.                                                                                | Set the value as `ATCK_CB` for PayPal transactions.                                                                                       |
    | `merchant_id`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                     | Unique identifier for the merchant.                                                                                       | Pass the merchant ID associated with the PayPal account.                                                                                  |
    | `financial_institution.processor`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | Name of the payment processor.                                                                                            | Set the value as `FDMS` for PayPal transactions.                                                                                          |
    | `transaction.id_enc`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>              | Encrypted transaction identifier of the transaction for which the chargeback is created.                                  | Pass the `SELLER-TRANSACTION-ID` in this parameter. This is the transaction ID available when you log in using the business test account. |
    | `transaction.amount`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>              | Currency and amount for the transaction.                                                                                  | Pass the currency and amount details.                                                                                                     |
    | `instrument`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>                      | Details about the payment instrument used for the transaction.                                                            | Pass the payment instrument details.                                                                                                      |
    | `instrument.instrument_type`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>      | Type of payment instrument used for the transaction.<br /><br />**Possible values**: `CARD`, `BANK`, `CREDIT`, and so on. | Set the value as `CARD` for card-funded transactions.                                                                                     |
    | `dispute`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span>                         | Details about the dispute.                                                                                                | Pass the dispute details.                                                                                                                 |
    | `dispute.receive_date`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                                               | Date and time when the chargeback was received.                                                                           | Pass a current value for this parameter.                                                                                                  |
    | `dispute.money_movement_date`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                                        | Date and time when the money movement happened.                                                                           | Pass a current value for this parameter.                                                                                                  |
    | `dispute.response_date`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                                              | Date and time when the response to the chargeback is due.                                                                 | Pass a future value for this parameter.                                                                                                   |

    <CodeGroup>
      ```shell lines expandable Sample request theme={null}
      curl -X POST https://api-m.sandbox.paypal.com/v2/customer-support/process-chargeback \
      -H 'Authorization: Bearer ACCESS-TOKEN' \
      -H 'Content-Type: application/json' \
      -d '{
          "adjacency": "PAYPAL",
          "file_layout": "ATCK_CB",
          "merchant_id": "99038409233245",
          "financial_institution": {
              "processor": "FDMS"
          },
          "transaction": {
              "id_enc": "SELLER-TRANSACTION-ID",
              "amount": {
                  "currency_code": "USD",
                  "value": "20"
              }
          },
          "instrument": {
              "instrument_type": "CARD",
              "card_brand": "VISA",
              "credit_card_transaction_id": "2347289342893472",
              "external": false
          },
          "dispute": {
              "id": null,
              "stage": "CHARGEBACK",
              "response_date": "2023-07-16T12:05:22.544Z",
              "status": "2",
              "amount": {
                  "currency_code": "USD",
                  "value": "10"
              },
              "receive_date": "2025-06-16T12:05:22.544Z",
              "event_code": "CHARGEBACK_INITIATED",
              "money_movement_date": "2025-06-16T12:05:22.544Z",
              "event_type": "DEBIT",
              "chargeback_type": "REPORTED_TO_PROCESSOR",
              "processor_info": {
                  "reference_number": "31639435342702423793399",
                  "reason_code": "1330",
                  "notes": "TEST_MEMO"
              }
          }
      }'
      ```

      ```json lines Sample response theme={null}
      {
        "dispute_id": "PP-D-1234"
      }
      ```
    </CodeGroup>

    A successful call returns a `201 Created` response and a dispute ID. Use the dispute ID to perform subsequent tests on the dispute.

  </Accordion>

  <Accordion title="Change dispute reason">
    You can change the reason for a dispute using this endpoint in the sandbox environment. This allows you to test how your integration handles changes to dispute reasons.

    <Note>This is a sandbox-only endpoint. You cannot use it to change dispute reasons in the live environment.</Note>

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a>, include the <a href="/growth/disputes/set-up#use-paypal-auth-assertion-request-header" target="_blank" rel="noopener noreferrer">PayPal-Auth-Assertion request header with a valid JWT</a>, and make a `POST` call to the `/v1/customer/disputes/{ID}/change-reason` endpoint. Include the following parameters:

    | Parameter name                                                                      | Description                                                                                      | Action                                                                                                                                                                                 |
    | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `reason`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>   | New reason for the dispute.                                                                      | Set the value to the new dispute reason. For more information, see <a href="/growth/disputes/reference/dispute-reasons" target="_blank" rel="noopener noreferrer">Dispute reasons</a>. |
    | `note`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>     | Note explaining the reason for the change.                                                       | Pass the reason for the change if needed.                                                                                                                                              |
    | `item_info`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span> | Details about the disputed item if more than one item was available in the disputed transaction. | Pass the item details if needed.                                                                                                                                                       |

    **Path parameter**: `ID` is the `dispute_id` returned in the [Create dispute](#create-dispute) response.

    <CodeGroup>
      ```shell lines expandable Sample request theme={null}
      curl -X POST "https://api-m.sandbox.paypal.com/v1/customer/disputes/{ID}/change-reason" \
      -H 'Authorization: Bearer ACCESS-TOKEN' \
      -H 'Content-Type: multipart/related' \
      -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
      -F 'input={
          "reason": "MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED",
          "note": "Product is not as advertised",
          "item_info":
          [
              {
                  "item_name": "item 1",
                  "item_quantity": "2",
                  "reason": "MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED",
                  "item_type": "PRODUCT",
                  "product_details":
                  {
                      "sub_reason": "DELAYED",
                      "category": "OTHER"
                  },
                  "expected_refund":
                  {
                      "currency_code": "USD",
                      "value": "10"
                  }
              }
          ]
      };type=application/json'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns a `200 OK` response and an HATEOAS link for the dispute.

  </Accordion>

  <Accordion title="Accept offer to resolve dispute">
    Accept a merchant's offer to resolve a dispute by ID. PayPal automatically refunds the proposed amount to the customer.

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{id}/accept-offer` endpoint. Include the following parameter:

    | Parameter                                                                       | Description                                                                                           | Action                 |
    | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------- |
    | `note`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | The customer's notes about accepting the offer. PayPal can view these notes, but the merchant cannot. | Pass a note if needed. |

    **Path parameter**: `id` is the `dispute_id` returned in the [Create dispute](#create-dispute) response.

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl --request POST \
        --url https://api-m.sandbox.paypal.com/v1/customer/disputes/{id}/accept-offer \
        --header 'Authorization: Bearer ACCESS TOKEN' \
        --header 'Content-Type: application/json' \
        --header 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
        --data '{
        "note": "I am ok with the refund offered."
      }'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns an HTTP `200 OK` status code and a HATEOAS link to the dispute. If money movement for the offer is delayed due to internal reasons, the call returns an HTTP `202 Accepted` status code instead.

  </Accordion>

  <Accordion title="Deny offer to resolve dispute">
    The customer denies a merchant's offer to resolve a dispute, by ID.

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{id}/deny-offer` endpoint. Include the following parameter:

    | Parameter                                                                                                                                          | Description                                                                                               | Action                                 |
    | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------- |
    | `note`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | The customer's notes about the denial of the offer. PayPal can view these notes, but the merchant cannot. | Pass the reason for denying the offer. |

    **Path parameter**: `id` is the `dispute_id` returned in the [Create dispute](#create-dispute) response.

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl --request POST \
        --url https://api-m.sandbox.paypal.com/v1/customer/disputes/{id}/deny-offer \
        --header 'Authorization: Bearer ACCESS-TOKEN' \
        --header 'Content-Type: application/json' \
        --header 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
        --data '{
        "note": "Refund offer is low."
      }'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns an HTTP `200 OK` status code and a HATEOAS link to the dispute.

  </Accordion>
</AccordionGroup>

### Simulate PayPal actions

<AccordionGroup>
  <Accordion title="Settle dispute">
    <Note>This is a sandbox-only endpoint. You cannot use it to settle disputes in the live environment.</Note>

    Settle a dispute in the customer's or merchant's favor to complete end-to-end dispute resolution testing in the sandbox. Before you make this call, confirm that the dispute `status` is `UNDER_REVIEW` and the `adjudicate` link is available in the HATEOAS links of the show dispute details response.

    To make this call, the dispute `status` must be `UNDER_REVIEW` and the `adjudicate` link must be available in the HATEOAS links of the show dispute details response.

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{id}/adjudicate` endpoint. Include the following parameter:

    | Parameter                                                                                                                                                          | Description                                                                                    | Action                                                                                              |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
    | `adjudication_outcome`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | The outcome of the adjudication.<br /><br />**Possible values**: `BUYER_FAVOR`, `SELLER_FAVOR` | Pass the outcome to indicate whether the dispute is resolved in the customer's or merchant's favor. |

    **Path parameter**: `id` is the `dispute_id` returned in the [Create dispute](#create-dispute) response.

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl --request POST \
        --url https://api-m.sandbox.paypal.com/v1/customer/disputes/{id}/adjudicate \
        --header 'Authorization: Bearer ACCESS-TOKEN' \
        --header 'Content-Type: application/json' \
        --data '{
        "adjudication_outcome": "BUYER_FAVOR"
      }'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns an HTTP `200 OK` status code and a HATEOAS link to the dispute.

  </Accordion>

  <Accordion title="Update dispute status">
    <Note>This is a sandbox-only endpoint. You cannot use it to update dispute statuses in the live environment.</Note>

    Updates the status of a dispute, by ID, from `UNDER_REVIEW` to either `WAITING_FOR_BUYER_RESPONSE` or `WAITING_FOR_SELLER_RESPONSE`. This status change enables either the customer or merchant to submit evidence for the dispute.

    To make this call, the dispute `status` must be `UNDER_REVIEW` and the `require-evidence` link must be available in the HATEOAS links of the show dispute details response.

    Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{id}/require-evidence` endpoint. Include the following parameter:

    | Parameter                                                                                                                                            | Description                                                                                                                                                  | Action                                                                                                                                    |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | `action`<br /><span style={{color: 'red', fontSize: 'smaller'}}>Required</span>, <span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | Indicates whether the status change enables the customer or merchant to submit evidence.<br /><br />**Possible values**: `BUYER_EVIDENCE`, `SELLER_EVIDENCE` | Pass `BUYER_EVIDENCE` to set the status to `WAITING_FOR_BUYER_RESPONSE`, or `SELLER_EVIDENCE` to set it to `WAITING_FOR_SELLER_RESPONSE`. |

    **Path parameter**: `id` is the `dispute_id` returned in the [Create dispute](#create-dispute) response.

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl --request POST \
        --url https://api-m.sandbox.paypal.com/v1/customer/disputes/{id}/require-evidence \
        --header 'Authorization: Bearer ACCESS-TOKEN' \
        --header 'Content-Type: application/json' \
        --data '{
        "action": "BUYER_EVIDENCE"
      }'
      ```

      ```json lines Sample response theme={null}
      {
        "links": [
          {
            "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803",
            "rel": "self",
            "method": "GET"
          }
        ]
      }
      ```
    </CodeGroup>

    A successful call returns an HTTP `200 OK` status code and a HATEOAS link to the dispute.

  </Accordion>
</AccordionGroup>

### Test dispute scenarios

You can use the scenarios in this section to test how your integration handles disputes and chargebacks in the sandbox environment.

<AccordionGroup>
  <Accordion title="Test internal disputes">
    You can test internal disputes by [creating a dispute](#create-dispute) for a transaction with PayPal. The dispute can be for payments made using a card, bank account, digital wallet, or other supported payment methods.

    **Test data condition**: Use `OTHER` as the evidence type when you <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">provide evidence</a>.

    | Scenario                                                                                     | Description                                                                                                                                                                                                                              | Test steps                                                                                                                                                                                                                                                                 | Expected outcome                                                                                                                                                                                                                                                     |
    | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Dispute NO HOLD, MERCHANT WINS CASE                                                          | <ul><li>The buyer creates a dispute for a transaction where PayPal does not hold the money in the merchant's account.</li><li>The merchant provides evidence and the case resolves in the merchant's favor.</li></ul>                    | <ol><li>**Buyer**: [Create a dispute](#create-dispute) using the PayPal wallet.</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the requested evidence</a>.</li></ol> | <ol><li>The merchant receives the relevant [notifications](#internal-dispute-possible-notifications).</li><li>The merchant's account balance remains unchanged.</li></ol>                                                                                            |
    | Dispute WITH HOLD, MERCHANT WINS CASE                                                        | <ul><li>The buyer creates a dispute for a transaction where PayPal holds the money in the merchant's account.</li><li> The merchant provides evidence and the case resolves in the merchant's favor. PayPal releases the hold.</li></ul> | <ol><li>**Buyer**: [Create a dispute](#create-dispute) using the PayPal wallet.</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the requested evidence</a>.</li></ol> | <ol><li>The merchant receives the relevant [notifications](#internal-dispute-possible-notifications).</li><li>PayPal releases the hold on the merchant's account.</li></ol>                                                                                          |
    | Dispute NO HOLD, MERCHANT LOSES CASE (no data), NO SELLER PROTECTION, DISPUTE FEE is charged | <ul><li>The buyer creates a dispute for a transaction where PayPal does not hold the money in the merchant's account.</li><li>The merchant does not provide evidence and the case resolves in the buyer's favor.</li></ul>               | <ol><li>**Buyer**: [Create a dispute](#create-dispute) using the PayPal wallet.</li><li>**Merchant**: Do not provide evidence.</li></ol>                                                                                                                                   | <ol><li>The merchant receives the relevant [notifications](#internal-dispute-possible-notifications).</li><li>The case resolves in the buyer's favor. The transaction is not eligible for Seller Protection.</li><li>PayPal debits the merchant's account.</li></ol> |

    **Possible notifications**<a id="internal-dispute-possible-notifications" />

    * **Webhooks**:
      * Case creation: `CUSTOMER.DISPUTE.CREATED`
      * Merchant response for evidence submission: `CUSTOMER.DISPUTE.UPDATED`
      * Case resolution: `CUSTOMER.DISPUTE.RESOLVED`
    * **Emails**: Case creation, response request, and resolution.

  </Accordion>

  <Accordion title="Test chargebacks">
    You can [create chargebacks](#create-chargeback) for card transactions and test them using these scenarios.

    **Test data conditions:**

    * **Mastercard**: Reason code - `4853`
    * **Visa**: Reason code - `C2`
    * For test conditions where a temporary hold applies, the hold is placed and released when the case is resolved in the merchant's favor.

    | Scenario                                                               | Description                                                                                                                                                                                                                                                        | Test steps                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                 |
    | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Chargeback WITH PROVISIONAL CREDIT, MERCHANT WINS CASE                 | <ul><li>A chargeback is created for a transaction.</li><li>The merchant provides evidence, the case resolves in the merchant’s favor, and the merchant retains the provisional credit.</li></ul>                                                                   | <ol><li>**Buyer**: [Create a chargeback](#create-chargeback).</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the requested evidence</a>.</li></ol> | <ol><li>The merchant receives the relevant [notifications](#chargeback-possible-notifications).</li><li>The merchant's account balance remains unchanged.</li></ol>                                                              |
    | Chargeback WITHOUT PROVISIONAL CREDIT, MERCHANT WINS CASE              | <ul><li>A chargeback is created for a transaction where PayPal does not hold the money in the merchant's account.</li><li>The merchant provides evidence and the case resolves in the merchant's favor.</li></ul>                                                  | <ol><li>**Buyer**: [Create a chargeback](#create-chargeback).</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the requested evidence</a>.</li></ol> | <ol><li>The merchant receives the relevant [notifications](#chargeback-possible-notifications).</li><li>The merchant's account balance remains unchanged.</li></ol>                                                              |
    | Chargeback WITH PROVISIONAL CREDIT, MERCHANT LOSES CASE (no data)      | <ul><li>A chargeback is created for a transaction where PayPal does not hold the money in the merchant's account.</li><li>The merchant does not provide evidence, the case resolves in the buyer's favor, and the merchant loses the provisional credit.</li></ul> | <ol><li>**Buyer**: [Create a chargeback](#create-chargeback).</li><li>**Merchant**: Do not provide evidence.</li></ol>                                                                                                                                   | <ol><li>The merchant receives the relevant [notifications](#chargeback-possible-notifications).</li><li>The case resolves in the buyer's favor. </li><li>PayPal debits the merchant's account.</li></ol>                         |
    | Chargeback WITHOUT PROVISIONAL CREDIT, MERCHANT LOSES CASE (no data)   | <ul><li>A chargeback is created for a transaction where PayPal does not hold the money in the merchant's account.</li><li>The merchant does not provide evidence and the case resolves in the buyer's favor.</li></ul>                                             | <ol><li>**Buyer**: [Create a chargeback](#create-chargeback).</li><li>**Merchant**: Do not provide evidence.</li></ol>                                                                                                                                   | <ol><li>The merchant receives the relevant [notifications](#chargeback-possible-notifications).</li><li>The case resolves in the buyer's favor.</li><li> PayPal debits the merchant's account.</li></ol>                         |
    | Chargeback WITH PROVISIONAL CREDIT, MERCHANT LOSES CASE (adjudication) | <ul><li>A chargeback is created for a transaction where PayPal does not hold the money in the merchant's account.</li><li> The merchant provides evidence and the case resolves in the buyer's favor and the merchant loses the provisional credit.</li></ul>      | <ol><li>**Buyer**: [Create a chargeback](#create-chargeback).</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the requested evidence</a>.</li></ol> | <ol><li>The merchant receives the relevant [notifications](#chargeback-possible-notifications).</li><li>The case adjudicates in the buyer's favor after evidence review.</li><li>PayPal debits the merchant's account.</li></ol> |

    **Possible notifications**<a id="chargeback-possible-notifications" />

    * **Webhooks**:
      * Case creation: `CUSTOMER.DISPUTE.CREATED`
      * Merchant response for evidence submission: `CUSTOMER.DISPUTE.UPDATED`
      * Case resolution: `CUSTOMER.DISPUTE.RESOLVED`
    * **Emails**: Case creation, response request, and resolution.

  </Accordion>
</AccordionGroup>

### Test merchant response

You can test and determine how to respond to disputes using different scenarios. This ensures that your integration correctly handles the merchant actions during the dispute process.

**Key terms**:

- **INR**: Item Not Received
- **SNAD**: Significantly Not As Described

#### Check response due date and HATEOAS links

You can use the <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Show dispute details</a> response to determine how and when to respond to disputes.

| Test steps                                                                                                                                                                                                                                                                                                                                                         | Expected outcome                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**: <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li></ol> | The API returns a `200 OK` response. It includes `status`, `seller_response_due_date`, and `links` parameters that help you respond appropriately within the timeframe. |

#### Inquiry stage

You can use the procedures in this section to test dispute response handling during the inquiry stage.

<AccordionGroup>
  <Accordion title="Send message to other party">
    You can test sending a message to the buyer during the inquiry stage of a dispute. For example, when a buyer creates an INR or SNAD case for a completed transaction, you can send a message to the buyer directly and help resolve the issue before it escalates.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                         |
    | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the send message action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#send-message-to-other-party" target="_blank" rel="noopener noreferrer">Send a message to the other party</a>.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `messages` array in the response. |

  </Accordion>

  <Accordion title="Make offer to resolve dispute">
    You can test making an offer to the buyer in these scenarios.

    > **Note**: Merchant must have sufficient funds to issue a refund.

    <AccordionGroup>
      <Accordion title="REFUND_WITH_RETURN - SNAD case">
        For a SNAD case in the inquiry stage, you can test offering the buyer a refund in exchange for returning the item.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Expected outcome                                                                                                                                                                                                                                                                                        |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the following parameters:<ul><li>`offer_amount`: Set the amount that you are willing to refund the buyer.</li><li>`offer_type`: Set the value as `REFUND_WITH_RETURN`.</li><li>`return_shipping_address`: Pass the shipping address for returning the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.seller_offered_amount` and `offer.offer_type` parameters in the response. |
      </Accordion>

      <Accordion title="REFUND_WITH_REPLACEMENT - SNAD case">
        For a SNAD case in the inquiry stage, you can test offering the buyer a replacement item along with a refund.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Expected outcome                                                                                                                                                                                                                                                                                        |
        | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the following parameters:<ul><li>`offer_amount`: Set the amount that you are willing to refund the buyer.</li><li>`offer_type`: Set the value as `REFUND_WITH_REPLACEMENT`.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.seller_offered_amount` and `offer.offer_type` parameters in the response. |
      </Accordion>

      <Accordion title="REPLACEMENT_WITHOUT_REFUND - SNAD case">
        For a SNAD case in the inquiry stage, you can test offering the buyer a replacement item without a refund.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Expected outcome                                                                                                                                                                                                                                                     |
        | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the `offer_type` parameter value as `REPLACEMENT_WITHOUT_REFUND`.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.offer_type` parameter in the response. |
      </Accordion>

      <Accordion title="REFUND">
        For an INR or SNAD case in the inquiry stage, you can test offering the buyer a refund without the replacement of the item.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Expected outcome                                                                                                                                                                                                                                                                                        |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the following parameters:<ul><li>`offer_amount`: Set the amount that you are willing to refund the buyer.</li><li>`offer_type`: Set the value as `REFUND`.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.seller_offered_amount` and `offer.offer_type` parameters in the response. |
      </Accordion>
    </AccordionGroup>

    For the actions involving return, you can <a href="#acknowledge-returned-item">acknowledge returned item</a> when the buyer returns the item and uploads the tracking information.

  </Accordion>

  <Accordion title="Acknowledge returned item">
    You can test [offering a refund with the return of the item](#refund-with-return-snad-case), accept it as a buyer and upload the return tracking information. After this, the acknowledge return item option will be available for you.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Expected outcome                                                                                                                                                                                                                                                                                                                 |
    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the following parameters:<ul><li>`offer_amount`: Set the amount that you are willing to refund the buyer.</li><li>`offer_type`: Set the value as `REFUND_WITH_RETURN`.</li><li>`return_shipping_address`: Pass the shipping address for returning the item.</li></ul></li></ol></li><li>**Buyer**:<ol><li>In the <a href="https://www.sandbox.paypal.com/disputes/dashboard/" target="_blank" rel="noopener noreferrer">PayPal Resolution Center</a>, view the dispute details and accept the offer.</li><li>Add the tracking information for the returned item.</li></ol></li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the acknowledge returned item action is available in HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#acknowledge-returned-item" target="_blank" rel="noopener noreferrer">Acknowledge the returned item</a>.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.seller_offered_amount`, `offer.offer_type`, and `acknowledgement_type` parameters in the response. |

  </Accordion>

  <Accordion title="Provide evidence">
    You can test providing evidence for these evidence types. This section applies to INR cases only.

    <AccordionGroup>
      <Accordion title="PROOF_OF_FULFILLMENT">
        You can test the `PROOF_OF_FULFILLMENT` evidence type by providing tracking information for the INR cases.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                                                                                                              |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `PROOF_OF_FULFILLMENT` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_FULFILLMENT`.</li><li>`evidence_info.tracking_info`: Pass the tracking information for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, and `evidence_info.tracking_info` parameters within the `evidences` object in the response. |
      </Accordion>

      <Accordion title="PROOF_OF_REFUND">
        You can test the `PROOF_OF_REFUND` evidence type by providing refund details for the INR cases.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Expected outcome                                                                                                                                                                                                                                                                                                                           |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `PROOF_OF_REFUND` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_REFUND`.</li><li>`evidence_info.refund_ids`: Pass the refund ID for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, and `evidence_info.refund_ids` parameters within the `evidences` object in the response. |
      </Accordion>

      <Accordion title="OTHER">
        You can test the `OTHER` evidence type by providing notes or documents (including photos and files) for the INR cases.
        <Note>For more information about the supported file types and size limits, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Note>

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Expected outcome                                                                                                                                                                                                                                                                                                                     |
        | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `OTHER` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `OTHER`.</li><li>`notes`: Pass the additional evidence details as notes.</li><li>`documents`: Pass the document details.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, `notes`, and `documents` parameters within the `evidences` object in the response. |
      </Accordion>
    </AccordionGroup>

  </Accordion>

  <Accordion title="Accept claim">
    You can test accepting the claim and refunding the buyer when you choose not to dispute the case.

    > **Note**: Merchant must have sufficient funds to issue a refund.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Expected outcome                                                                                                                                                                                                                                                                                                                                                    |
    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the accept claim action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#accept-claim" target="_blank" rel="noopener noreferrer">Accept the claim</a> with the `accept_claim_type` parameter value as `REFUND`.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `dispute_outcome` object in the response. The `CUSTOMER.DISPUTE.RESOLVED` webhook notification with the refund details is sent to the buyer. |

  </Accordion>

  <Accordion title="Escalate dispute to claim">
    You can test escalating the dispute to a claim to simulate cases where you cannot reach an amicable resolution with the buyer.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Expected outcome                                                                                                                                                                                                                                                                                                                                                              |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the escalate action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#escalate-dispute-to-claim" target="_blank" rel="noopener noreferrer">Escalate the dispute to claim</a>.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `dispute_life_cycle_stage` parameter value is updated from `INQUIRY` to `CHARGEBACK`. The system also triggers the `CUSTOMER.DISPUTE.UPDATED` webhook. |

    To test Accelerated Response, see [Accelerated Response sandbox testing](/growth/disputes/test-go-live#accelerated-response-sandbox-testing).

  </Accordion>
</AccordionGroup>

#### Claim stage

You can use the procedures in this section to test dispute response handling during the claim stage.

<AccordionGroup>
  <Accordion title="Provide evidence">
    You can test providing evidence for these evidence types.

    <AccordionGroup>
      <Accordion title="PROOF_OF_FULFILLMENT - INR case">
        You can test the `PROOF_OF_FULFILLMENT` evidence type by providing tracking information for the INR cases.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                                                                                                              |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `PROOF_OF_FULFILLMENT` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_FULFILLMENT`.</li><li>`evidence_info.tracking_info`: Pass the tracking information for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, and `evidence_info.tracking_info` parameters within the `evidences` object in the response. |
      </Accordion>

      <Accordion title="PROOF_OF_REFUND">
        You can test the `PROOF_OF_REFUND` evidence type by providing refund details for the INR or SNAD cases.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                                                                                                           |
        | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `PROOF_OF_REFUND` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_REFUND`.</li><li>`evidence_info.refund_ids`: Pass the refund ID for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, and `evidence_info.refund_ids` parameters within the `evidences` object in the response. |
      </Accordion>

      <Accordion title="OTHER">
        You can test the `OTHER` evidence type by providing notes or documents (including photos and files) for the INR or SNAD cases.
        <Note>For more information about the supported file types and size limits, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Note>

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Expected outcome                                                                                                                                                                                                                                                                                                                     |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the provide evidence is available in the HATEOAS links and if the `evidences` object contains `evidence_type` as `OTHER` and `source` as `REQUESTED_FROM_SELLER`.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide the evidence</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `OTHER`.</li><li>`notes`: Pass the additional evidence details as notes.</li><li>`documents`: Pass the document details.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidence_type`, `source`, `notes`, and `documents` parameters within the `evidences` object in the response. |
      </Accordion>
    </AccordionGroup>

  </Accordion>

  <Accordion title="Accept claim">
    You can test accepting the claim and refunding the buyer if you choose to resolve the case using these accept claim types.

    > **Note**: Merchant must have sufficient funds to issue a refund.

    <AccordionGroup>
      <Accordion title="REFUND">
        The test procedure to refund the dispute amount is identical in the inquiry and claim stages. For detailed information, see [Accept claim](#accept-claim).
      </Accordion>

      <Accordion title="REFUND_WITH_RETURN">
        You can test accepting the claim for a SNAD case and refunding the buyer after they return the item to a specified address.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                                                                                            |
        | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD dispute.</li><li>**Merchant**: <ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the accept claim action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#accept-claim" target="_blank" rel="noopener noreferrer">Accept the claim</a> with the following parameters:<ul><li>`return_shipping_address`: Pass the shipping address for returning the item.</li><li>`accept_claim_type`: Set the value as `REFUND_WITH_RETURN`.</li></ul></li></ol></li><li>**Buyer**: In the <a href="https://www.sandbox.paypal.com/disputes/dashboard/" target="_blank" rel="noopener noreferrer">PayPal Resolution Center</a>, view the dispute details and provide the tracking information for the returned item.</li></ol> | The system triggers the `CUSTOMER.DISPUTE.UPDATED` webhook.<br />You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the response parameters to get the tracking information and update the case. |
      </Accordion>

      <Accordion title="PARTIAL_REFUND">
        You can test accepting the claim and providing a partial refund (amount less than the buyer-requested refund) to the buyer for a INR or SNAD cases.

        | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
        | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD dispute.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the accept claim action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#accept-claim" target="_blank" rel="noopener noreferrer">Accept the claim</a> with the following parameters:<ul><li>`refund_amount`: Amount to refund.</li><li>`accept_claim_type`: Set the value as `PARTIAL_REFUND`.</li></ul></li></ol></li></ol> | <ul><li>The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and track the updates.</li><li>If the refund amount is greater than or equal to the buyer-requested refund amount, the case is resolved, and you receive the `CUSTOMER.DISPUTE.RESOLVED` webhook notification.</li><li>If the amount is less than the buyer-requested refund amount, it triggers an email to the buyer for their consent in the Resolution Center.</li></ul> |
      </Accordion>
    </AccordionGroup>

  </Accordion>

  <Accordion title="Acknowledge returned item">
    You can test [offering a refund with the return of the item](#refund-with-return-snad-case), accept it as a buyer and upload the return tracking information. After this, the acknowledge return item option will be available for you.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Expected outcome                                                                                                                                                                                                                                                                                                                 |
    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case.</li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the make offer action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">Make an offer</a> with the following parameters:<ul><li>`offer_amount`: Set the amount that you are willing to refund the buyer.</li><li>`offer_type`: Set the value as `REFUND_WITH_RETURN`.</li><li>`return_shipping_address`: Pass the shipping address for returning the item.</li></ul></li></ol></li><li>**Buyer**:<ol><li>In the <a href="https://www.sandbox.paypal.com/disputes/dashboard/" target="_blank" rel="noopener noreferrer">PayPal Resolution Center</a>, view the dispute details and accept the offer.</li><li>Add the tracking information for the returned item.</li></ol></li><li>**Merchant**:<ol><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the acknowledge returned item action is available in HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#acknowledge-returned-item" target="_blank" rel="noopener noreferrer">Acknowledge the returned item</a>.</li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `offer.seller_offered_amount`, `offer.offer_type`, and `acknowledgement_type` parameters in the response. |

  </Accordion>
</AccordionGroup>

#### Appeal dispute

When PayPal adjudicates a case against a party, you or the buyer may be eligible to appeal the decision. PayPal uses predefined rules to determine appeal eligibility.

To test appeals, create a buyer account with a primary email address that includes `allowappeal` (for example, [testallowappeal@personal.example.com](mailto:testallowappeal@personal.example.com)). The disputes created with this account will trigger:

- The seller appeal workflow if you are found liable.
- The buyer appeal workflow if the buyer is found liable.

<Note>Each party can submit only one appeal per case.</Note>

To simulate cases where appeals are not allowed for a buyer, create a buyer account with a primary email address that includes `noappeal` (for example, [testnoappeal@personal.example.com](mailto:testnoappeal@personal.example.com)).

You can appeal the case and provide evidence using these evidence types.

<AccordionGroup>
  <Accordion title="PROOF_OF_FULFILLMENT">
    If the case is resolved in the buyer's favor, you can appeal by providing the fulfillment information for INR, unauthorized, or other cases.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case.</li><li>**Merchant**:<ol><li><a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `BUYER_FAVOR` to resolve the case in the buyer's favor.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the appeal action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#appeal-dispute" target="_blank" rel="noopener noreferrer">Appeal the case</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_FULFILLMENT`.</li><li>`evidence_info.tracking_info`: Pass the tracking information for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check:<ul><li>If the `evidences` object contains the `evidence_type` and `evidence_info.tracking_info` parameter values you provided.</li><li>If the `status` and `dispute_life_cycle_stage` parameter values are `UNDER_REVIEW` and `PRE_ARBITRATION` respectively.</li></ul> |

  </Accordion>

  <Accordion title="PROOF_OF_REFUND">
    If the case is resolved in the buyer's favor, you can appeal by providing the refund information for all the dispute reasons.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `BUYER_FAVOR` to resolve the case in the buyer's favor.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the appeal action is available in the HATEOAS links.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#appeal-dispute" target="_blank" rel="noopener noreferrer">Appeal the case</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `PROOF_OF_REFUND`.</li><li>`evidence_info.refund_ids`: Pass the refund ID for the item.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check:<ul><li>If the `evidences` object contains the `evidence_type` and `evidence_info.refund_ids` parameter values you provided.</li><li>If the `status` and `dispute_life_cycle_stage` parameter values are `UNDER_REVIEW` and `PRE_ARBITRATION` respectively.</li></ul> |

  </Accordion>

  <Accordion title="OTHER">
    If the case is resolved in the buyer's favor, you can appeal by providing notes or documents. You can use the `OTHER` evidence type if the requested evidence is not covered by the `PROOF_OF_FULFILLMENT` and `PROOF_OF_REFUND` evidence types.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Expected outcome                                                                                                                                                                                                                                           |
    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**:<ol><li><a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `BUYER_FAVOR` to resolve the case in the buyer's favor.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Retrieve the dispute details</a>.</li><li>Check if the appeal action is available in the HATEOAS links and the `evidences` object for the requested evidence.</li><li><a href="/growth/disputes/handle-disputes/use-disputes-api#appeal-dispute" target="_blank" rel="noopener noreferrer">Appeal the case</a> with the following parameters within the `evidences` object:<ul><li>`evidence_type`: Set the value as `OTHER`.</li><li>`notes`: Pass the additional evidence details as notes.</li><li>`documents`: Pass the document details.</li></ul></li></ol></li></ol> | The API returns a `200 OK` response. You can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the `evidences` object in the response. |

  </Accordion>
</AccordionGroup>

## Accelerated Response sandbox testing

To enable Accelerated Response for a dispute, include the value `ACCELERATED_RESPONSE_ENABLED` in the `notes` field under `evidences` when submitting your `create_dispute` API request.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes \
  -H 'Authorization: Bearer A21AAItEDV4r4hH1p72Aw8iciCdCyVmIeiXi7XkX8I38AHTDN7Zc4KywkWgsjH8gP4hfQwWFVn8Hj880z_s2ormzjPh80D_5w' \
  -H 'Content-Type: multipart/form-data' \
  -H 'PayPal-Auth-Assertion: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJBWmdidVpPU1B0YnJIWnNrNFZHeFAxOVFvZFUzVk91R1R5UEhhRTZJNkJVVm9NdTJvSnpIZExGeVc3Rmpvd1labGdVaEk4eWRzcXh6RlAtSSIsImVtYWlsIjoic2ItcmstYnV5ZXJAcGVyc29uYWwuZXhhbXBsZS5jb20ifQ.' \
  -F 'input={
      "disputed_transactions": [{
          "buyer_transaction_id": "2NJ45340EV624100G"
          }],
      "reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
      "dispute_amount": {
          "currency_code":"USD",
          "value": "5"
          },
      "extensions": {
          "merchant_contacted": true,
          "merchant_contacted_outcome": "NO_RESPONSE",
          "merchandize_dispute_properties": {
            "issue_type": "PRODUCT"
          }
      },
      "evidences": [{
              "notes": "ACCELERATED_RESPONSE_ENABLED"
          }
      ]
  };type=application/json'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-TOW-10161582",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

### Escalation simulation

To simulate the day of escalation in the sandbox environment, use the following transaction amounts:

| Transaction amount (USD) | Simulated escalation day |
| ------------------------ | ------------------------ |
| 5.00 – 5.99              | Day 5 escalation         |
| 9.00 – 9.99              | Day 9 escalation         |
| ≥ 11.00                  | Day 11 escalation        |

Create a transaction with one of the listed amounts, then use that transaction when creating the dispute to simulate the corresponding escalation day.

### Applicable dispute reasons

Accelerated Response currently applies to these dispute reasons:

- `MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED`
- `MERCHANDISE_OR_SERVICE_NOT_RECEIVED`

Once the dispute is created, you can perform any of the actions listed under the [Inquiry stage](https://docs.paypal.ai/growth/disputes/handle-disputes/use-disputes-api#inquiry-stage) section.

## Applicable document proofs

Refer to the applicable documentation requirements in [Supported file types and sizes](/growth/disputes/reference/supported-file-types-sizes).

## Test webhooks

To test disputes webhooks, you need to wait a few minutes after creating the dispute for the actions to become available. You can then perform the actions to trigger the webhooks.

### Test dispute created webhook

You can test the `CUSTOMER.DISPUTE.CREATED` webhook in both the [inquiry](#test-dispute-created-inquiry-stage) and [claim](#test-dispute-created-claim-stage) stages.

#### **Inquiry stage** <a id="test-dispute-created-inquiry-stage" />

You can test this webhook in the inquiry stage for these scenarios.

<AccordionGroup>
  <Accordion title="SNAD case">
    You can create a SNAD case for a transaction and test triggering the webhook.

    | Test steps                                                                                                                                                    | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are `MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED` and `INQUIRY` respectively.</li></ol> |

  </Accordion>

  <Accordion title="INR case">
    You can create an INR case for a transaction and test triggering the webhook.

    | Test steps                                                                                                                                                    | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are `MERCHANDISE_OR_SERVICE_NOT_RECEIVED` and `INQUIRY` respectively.</li></ol> |

  </Accordion>
</AccordionGroup>

#### **Claim stage** <a id="test-dispute-created-claim-stage" />

You can test this webhook in the claim stage for these scenarios.

<AccordionGroup>
  <Accordion title="SNAD case">
    If you have opted out of the dispute stage, you can create a SNAD case for a transaction and test triggering this webhook in the claim stage.

    | Test steps                                                                                                                                                    | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD case. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are `MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED` and `CHARGEBACK` respectively.</li></ol> |

  </Accordion>

  <Accordion title="INR case">
    If you have opted out of the dispute stage, you can create an INR case for a transaction and test triggering this webhook in the claim stage.

    | Test steps                                                                                                                                                    | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR case. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are `MERCHANDISE_OR_SERVICE_NOT_RECEIVED` and `CHARGEBACK` respectively.</li></ol> |

  </Accordion>

  <Accordion title="Unauthorized case">
    You can create an unauthorized case for a transaction and test triggering the webhook.

    <Note>For unauthorized disputes, the buyer and merchant receive different dispute IDs. For merchants, the format and identifiers of the notifications stay the same as those of other dispute types.</Note>

    | Test steps                                                                                                                                                             | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an unauthorized case. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are `UNAUTHORISED` and `CHARGEBACK` respectively.</li></ol> |

  </Accordion>

  <Accordion title="Transaction error case">
    You can test triggering the webhook by creating a dispute for a transaction error using one of these dispute reasons: `CREDIT_NOT_PROCESSED`, `DUPLICATE_TRANSACTION`, `INCORRECT_AMOUNT`, `PAYMENT_BY_OTHER_MEANS`, `CANCELED_RECURRING_BILLING`, or `OTHER`.

    <Note>For more information about the dispute reasons, see <a href="/growth/disputes/reference/dispute-reasons" target="_blank" rel="noopener noreferrer">Dispute reasons</a>.</Note>

    | Test steps                                                                                                                                                                               | Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a case with one of the dispute reasons. | <ol><li>The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the parameter values of `reason` and `dispute_life_cycle_stage` are the dispute reason that you provided and `CHARGEBACK` respectively.</li></ol> |

  </Accordion>

  <Accordion title="Duplicate dispute creation (negative testing)">
    You can test that a buyer cannot open a duplicate dispute on a transaction that already has an existing dispute. Even after the original dispute case is closed, the buyer cannot open a new dispute on the same transaction.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Expected outcome                                             |
    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>**Merchant**: <a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `BUYER_FAVOR` to resolve the case in the buyer's favor.</li><li>**Buyer**: Check if you can create a dispute for the same transaction.</li></ol> | You cannot open a duplicate dispute on the same transaction. |

  </Accordion>
</AccordionGroup>

### Test dispute updated webhook

You can test the `CUSTOMER.DISPUTE.UPDATED` webhook in both the [inquiry](#test-dispute-updated-inquiry-stage) and [claim](#test-dispute-updated-claim-stage) stages.

#### **Inquiry stage** <a id="test-dispute-updated-inquiry-stage" />

You can test this webhook in the inquiry stage for this scenario.

<Accordion title="Buyer sends message to merchant">
  You can test this webhook by sending a message to the merchant as a buyer for the INR or SNAD case.

| Test steps                                                                                                                                                                                                                                             | Expected outcome                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Buyer**: <ol><li>Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR or SNAD case.</li><li>Select the case ID and send a message to the merchant.</li></ol> | <ol><li>The system triggers `CUSTOMER.DISPUTE.UPDATED` webhook. </li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the message details are available in the `messages` array.</li></ol> |

</Accordion>

#### **Claim stage** <a id="test-dispute-updated-claim-stage" />

You can test this webhook in the claim stage for these scenarios.

<AccordionGroup>
  <Accordion title="Buyer provides return tracking information">
    If you have opted out of the dispute stage, you can accept a claim for a case and provide the buyer with the return shipping address. Then, test as a buyer by returning the item and providing the return tracking information.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Expected outcome                                                                                                                                                                                                                                                                                                                                                    |
    | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a SNAD dispute.</li><li>**Merchant**: <a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_accept-claim" target="_blank" rel="noopener noreferrer">Accept the claim</a>.</li><li>**Buyer**: Provide the tracking number through the <a href="https://www.sandbox.paypal.com/disputes/dashboard/" target="_blank" rel="noopener noreferrer">PayPal Resolution Center</a>.</li></ol> | <ol><li>The system triggers `CUSTOMER.DISPUTE.UPDATED` webhook. </li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check the response parameters to get the tracking information.</li></ol> |

  </Accordion>

  <Accordion title="Buyer changes reason">
    You can test changing the dispute reason of the INR dispute to SNAD or unauthorized activity.

    | Test steps                                                                                                                                                                                                                                                                     | Expected outcome                                                                                                                                                                                                                                                                                                                                                               |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **Buyer**: <ol><li>Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create an INR dispute.</li><li>Select **Change case type** and update the reason to SNAD or unauthorized activity.</li></ol> | <ol><li>The system triggers `CUSTOMER.DISPUTE.UPDATED` webhook.</li><li>After receiving the webhook notification, you can <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">retrieve the dispute details</a> and check if the `reason` parameter value contains the updated dispute reason.</li></ol> |

  </Accordion>
</AccordionGroup>

### Test dispute resolved webhook

You can test the `CUSTOMER.DISPUTE.RESOLVED` webhook for these scenarios.

<AccordionGroup>
  <Accordion title="Buyer cancels dispute">
    You can test cancelling the dispute in the Resolution Center as a buyer to trigger the webhook.

    | Test steps                                                                                                                                                                                                                                | Expected outcome                                         |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
    | **Buyer**:<ol><li>Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a dispute.</li><li>Select the case ID and then, select **Cancel case**.</li></ol> | The system triggers `CUSTOMER.DISPUTE.RESOLVED` webhook. |

  </Accordion>

  <Accordion title="Settle dispute (buyer wins)">
    You can test settling the case in the buyer's favor to trigger the webhook.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                            | Expected outcome                                         |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a dispute.</li><li>**Merchant**: <a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `BUYER_FAVOR` to resolve the case in the buyer's favor.</li></ol> | The system triggers `CUSTOMER.DISPUTE.RESOLVED` webhook. |

  </Accordion>

  <Accordion title="Settle dispute (merchant wins)">
    You can test settling the case in the merchant's favor to trigger the webhook.

    | Test steps                                                                                                                                                                                                                                                                                                                                                                                                                                                | Expected outcome                                         |
    | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
    | <ol><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a dispute.</li><li>**Merchant**: <a href="https://developer.paypal.com/docs/api/customer-disputes/v1/#disputes_adjudicate" target="_blank" rel="noopener noreferrer">Settle the dispute</a> with `adjudication_outcome` as `SELLER_FAVOR` to resolve the case in the merchant's favor.</li></ol> | The system triggers `CUSTOMER.DISPUTE.RESOLVED` webhook. |

  </Accordion>
</AccordionGroup>

### Identify unique webhook through webhook ID

You can test identifying a specific webhook using the webhook ID in the webhook payload.

| Test steps                                                                                                                                                                                                                                                                                                                             | Expected outcome                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ol><li>**Merchant**: Subscribe and listen to the dispute webhooks: `CUSTOMER.DISPUTE.CREATED`, `CUSTOMER.DISPUTE.RESOLVED`, `CUSTOMER.DISPUTE.UPDATED`.</li><li>**Buyer**: Log in to your <a href="https://sandbox.paypal.com" target="_blank" rel="noopener noreferrer">sandbox personal account</a> and create a dispute.</li></ol> | The system triggers the `CUSTOMER.DISPUTE.CREATED` webhook notification. You can use the unique webhook ID in the payload to identify the webhook. |

### Test API calls: use test values and simulate responses <a id="test-api-calls-use-test-values-and-simulate-responses" />

To simulate Disputes API responses, inject test values as a path or query parameter in the request URL. These methods allow you to trigger specific error responses without creating actual disputes.

<Tabs>
  <Tab title="Sample - test value as path parameter" id="tab1">
    | Path parameter                    | Simulated error response |
    | --------------------------------- | ------------------------ |
    | `/v1/customer/disputes/ERRDIS015` | `FORBIDDEN`              |

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl -X GET https://api-m.sandbox.paypal.com/v1/customer/disputes/ERRDIS015 \
        -H 'Authorization: Bearer ACCESS-TOKEN' \
        -H 'Content-Type: application/json'
      ```

      ```json lines Sample response theme={null}
      {
          "name": "FORBIDDEN",
          "message": "No permission for the requested operation",
          "debug_id": "e90ec082e0e4d"
      }
      ```
    </CodeGroup>

  </Tab>

  <Tab title="Sample - test value as query parameter" id="tab2">
    | Query parameter                                           | Simulated error response |
    | --------------------------------------------------------- | ------------------------ |
    | `/v1/customer/disputes?disputed_transaction_id=ERRDIS023` | `FORBIDDEN`              |

    <CodeGroup>
      ```shell lines Sample request theme={null}
      curl -X GET https://api-m.sandbox.paypal.com/v1/customer/disputes?disputed_transaction_id=ERRDIS023 \
        -H 'Authorization: Bearer ACCESS-TOKEN' \
        -H 'Content-Type: application/json'
      ```

      ```json lines Sample response theme={null}
      {
          "name": "FORBIDDEN",
          "message": "No permission for the requested operation",
          "debug_id": "e90ec082e0e4d"
      }
      ```
    </CodeGroup>

  </Tab>
</Tabs>

### Common issues

If an API call fails while you test , check for these common issues:

- 400 Bad Request when required fields or formats are invalid.
- 401 Unauthorized when the access token is missing, expired, or invalid.
- 403 Forbidden when the app is not permitted to perform this action.

For more details, see the [HTTP status codes and error messages](/developer/how-to/api/troubleshooting/common-errors/overview#http-status-codes-and-error-messages).

## Go live

1. <a href="/growth/disputes/set-up#disputes-api-2" target="_blank" rel="noopener noreferrer">Set up live account</a>.
2. <a href="https://docs.paypal.ai/reference/webhook-events/webhook-format#webhook-message-format" target="_blank" rel="noopener noreferrer">Set up webhooks</a> to get real-time notifications about dispute events, such as created, updated, or resolved disputes.
3. Go live with your app.
