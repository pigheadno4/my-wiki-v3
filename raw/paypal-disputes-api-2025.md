<!-- Source URL: https://docs.paypal.ai/growth/disputes/handle-disputes/use-disputes-api -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Disputes API

You can use the PayPal Disputes API to handle and resolve disputes programmatically throughout their lifecycle. This guide shows you how to gather dispute information, respond based on lifecycle stages, and automate dispute handling using webhooks.

## Prerequisites

Before you use the Disputes API, ensure you:

- Have a [PayPal developer account](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdashboard%2F&intent=developer&ctxId=ul14c2e612301b4f5c99383ae8f762a937).
- Have your accounts and environment set up as described in [Set up accounts and environment](/growth/disputes/set-up).

## Understand dispute lifecycle stages

Every dispute goes through defined stages from creation to resolution. Understanding them helps you determine the required [actions and responses at each stage](#respond-to-a-dispute).

<Tabs>
  <Tab title="Inquiry stage">
    The inquiry or dispute stage begins immediately when a customer files a dispute. This is a pre-claim stage designed to reduce the occurrence of chargebacks and claims. PayPal provides a platform for both parties to communicate and resolve issues directly without its intervention. This stage only applies to cases with the item/service not received (INR) and significantly not as described (SNAD) issues.

    The inquiry stage lasts up to 20 days unless escalated to a claim. If the dispute remains unresolved, either party can escalate it to a claim within the 20-day inquiry period. If not, PayPal considers the dispute canceled and closes the case.

    If you do not want to engage with buyers directly, you can opt out of the inquiry stage. In this case, all disputes are created directly in the [claim stage](#claim-stage). To opt out of the inquiry stage, <a href="https://www.paypal-support.com/" target="_blank" rel="noopener noreferrer">contact PayPal</a> or your PayPal account manager.

    For this stage, the value of `dispute_life_cycle_stage` parameter in [Show dispute details](#show-dispute-details) response is `INQUIRY`.

    <Note>The inquiry stage is only applicable for internal disputes.</Note>

    PayPal is introducing an enhancement to the inquiry stage for eligible merchants. To understand this enhancement, see [Accelerated Response](/growth/disputes/handle-disputes/use-disputes-api#accelerated-response).

  </Tab>

  <Tab title="Claim stage">
    If both parties cannot resolve the issue during the dispute stage, either party can escalate the dispute to PayPal within the 20-day inquiry period. This moves the dispute to the claim stage. All external and non-merchandise disputes proceed directly to the claim stage. This includes claims for incorrect charges, duplicate payments, or unauthorized transactions due to account compromise.

    For this stage, the value of `dispute_life_cycle_stage` parameter in [Show dispute details](#show-dispute-details) response can be one of these values:

    * `CHARGEBACK`: A buyer or merchant can escalate an inquiry to a claim. This authorizes PayPal to review the case and adjudicate. During this stage, only PayPal agents can view the buyer’s notes. The buyer waits for PayPal's response before taking further action. PayPal shares dispute details with the merchant, who can accept the claim, submit evidence to challenge the claim, or offer to resolve the dispute.
      <Note>The `CHARGEBACK` stage is a PayPal dispute lifecycle stage, not a credit or debit card chargeback.</Note>

    * `PRE_ARBITRATION`: This is the first appeal stage for merchants. A merchant can appeal a chargeback if the outcome is not in the merchant's favor. If the merchant does not appeal within the appeal period, PayPal considers the case resolved.

    * `ARBITRATION`: This is the second appeal stage for merchants. If the first appeal is denied, a merchant can appeal a dispute for a second time. If the merchant does not appeal within the appeal period, PayPal returns the case to the resolved status in the `PRE_ARBITRATION` stage.

  </Tab>

  <Tab title="Dispute resolution">
    PayPal adjudicates only internal dispute cases. To resolve the claim, PayPal reviews the submitted evidence and adjudicates within 10 days in favor of either the buyer or merchant. PayPal then informs both parties about the resolution.

    Disputes can be resolved at any stage of the dispute lifecycle. After resolution, PayPal updates the `status` of the case as `RESOLVED`.

    <Note>For external cases, the card issuer adjudicates the cases in `CHARGEBACK` and `PRE_ARBITRATION` stages based on the card network's rules. However, the card network adjudicates the external cases in the `ARBITRATION` stage.</Note>

  </Tab>
</Tabs>

### Accelerated Response

Accelerated Response enhances the inquiry stage. As a merchant, you can submit supporting documentation within 10 days after the inquiry starts.

During this period, either you or the buyer can escalate the inquiry to a claim. Post escalation, you may be given additional time to submit supporting documents. The time available to submit documents depends on who escalates the case and when.

Once the required documentation is submitted, we will proceed to adjudicate the case.

| Scenario                     | Escalating party  | Message or offer sent during inquiry | Time to submit documents (post-escalation)   | Outcome if no documents submitted               |
| :--------------------------- | :---------------- | :----------------------------------- | :------------------------------------------- | :---------------------------------------------- |
| Escalated before day 8       | Buyer or Merchant | Not required                         | Remaining time within original 10-day window | Case adjudicated on available information       |
| Escalated on day 8, 9, or 10 | Buyer             | Yes                                  | 3 days                                       | Case adjudicated on available information       |
| Escalated on day 8, 9, or 10 | Buyer             | No                                   | Remaining time within original 10-day window | Case adjudicated on available information       |
| Escalated after day 10       | Buyer             | Yes                                  | 3 days                                       | Case closed buyer's favor                       |
| Escalated after day 10       | Buyer             | No                                   | No additional time                           | Case closed buyer's favor                       |
| Escalated after day 8        | Merchant          | Not required                         | 3 days                                       | Case adjudicated based on available information |

<Note> PayPal is rolling out Accelerated Response in phases. PayPal notifies eligible merchants when this enhancement becomes available on their accounts. </Note>

## Gather dispute information

You can use the Disputes API to gather information about disputes associated with your account. The following sections describe how to [list all disputes](#list-disputes) and [retrieve details of a specific dispute](#show-dispute-details).

### List disputes

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `GET` call to the `/v1/customer/disputes` endpoint to view all the disputes associated with an account.

<Tip>You can also filter the results using query parameters. For example, use the `disputed_transaction_id` query parameter to show disputes for a specific transaction. For information on query parameters, see <a href="https://docs.paypal.ai/reference/api/rest/disputes/list-disputes" target="_blank" rel="noopener noreferrer">API reference</a>.</Tip>

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X GET https://api-m.sandbox.paypal.com/v1/customer/disputes \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN'
  ```

```json expandable lines Sample response theme={null}
{
  "items": [
    {
      "dispute_id": "PP-R-ORC-10135512",
      "create_time": "2025-09-23T09:25:28.000Z",
      "update_time": "2025-09-23T09:47:03.000Z",
      "disputed_transactions": [
        {
          "buyer_transaction_id": "1XC473123G8516345",
          "seller": {
            "merchant_id": "HAAP3SNYZZ9NG"
          }
        }
      ],
      "reason": "MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED",
      "status": "RESOLVED",
      "dispute_state": "RESOLVED",
      "dispute_amount": {
        "currency_code": "USD",
        "value": "10.00"
      },
      "dispute_life_cycle_stage": "INQUIRY",
      "dispute_channel": "INTERNAL",
      "outcome": "LOST",
      "links": [
        {
          "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-ORC-10135512",
          "rel": "self",
          "method": "GET"
        }
      ]
    },
    {
      "dispute_id": "PP-R-AYP-10135034",
      "create_time": "2025-09-18T09:46:54.000Z",
      "update_time": "2025-09-23T09:57:13.000Z",
      "disputed_transactions": [
        {
          "buyer_transaction_id": "7XB07472F52871902",
          "seller": {
            "merchant_id": "HAAP3SNYZZ9NG"
          }
        }
      ],
      "reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
      "status": "WAITING_FOR_SELLER_RESPONSE",
      "dispute_state": "REQUIRED_ACTION",
      "dispute_amount": {
        "currency_code": "USD",
        "value": "2.00"
      },
      "dispute_life_cycle_stage": "CHARGEBACK",
      "dispute_channel": "INTERNAL",
      "seller_response_due_date": "2025-10-04T06:59:59.000Z",
      "links": [
        {
          "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034",
          "rel": "self",
          "method": "GET"
        }
      ]
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes",
      "rel": "first",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response. The response includes the following parameter:

| Parameter                                                                                     | Description                        | Further action                                                                                                               |
| --------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `items[].dispute_id`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | Unique identifier for the dispute. | Use this value to [retrieve the dispute details](#show-dispute-details) and [respond to the dispute](#respond-to-a-dispute). |

<Note>For information on all response parameters, see the [API reference](/reference/api/rest/disputes/list-disputes)</Note>

### Show dispute details

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `GET` call to the `/v1/customer/disputes/{ID}` endpoint to retrieve details of a specific dispute.

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X GET https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034 \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN'
  ```

```json expandable lines Sample response theme={null}
{
  "dispute_id": "PP-R-AYP-10135034",
  "create_time": "2025-09-18T09:46:54.926Z",
  "update_time": "2025-09-18T09:49:53.336Z",
  "disputed_transactions": [
    {
      "buyer_transaction_id": "7XB07472F52871902",
      "seller_transaction_id": "8AW70038VH226914P",
      "create_time": "2025-09-18T09:42:33.000Z",
      "transaction_status": "HELD",
      "gross_amount": {
        "currency_code": "USD",
        "value": "2.00"
      },
      "buyer": {
        "name": "John Doe"
      },
      "seller": {
        "email": "sb-ekqdo43289257@business.example.com",
        "merchant_id": "HAAP3SNYZZ9NG",
        "name": "The Happy Store"
      },
      "items": [
        {
          "item_name": "Check Ngo",
          "item_description": "Check Ngo",
          "item_quantity": "1",
          "reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
          "item_type": "PRODUCT"
        }
      ],
      "seller_protection_eligible": true,
      "seller_protection_type": "EXPANDED_SELLER_PROTECTION"
    }
  ],
  "reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
  "status": "WAITING_FOR_SELLER_RESPONSE",
  "dispute_amount": {
    "currency_code": "USD",
    "value": "2.00"
  },
  "dispute_state": "REQUIRED_ACTION",
  "dispute_life_cycle_stage": "INQUIRY",
  "dispute_channel": "INTERNAL",
  "messages": [
    {
      "posted_by": "BUYER",
      "time_posted": "2025-09-18T09:46:54.926Z",
      "content": "Test support case"
    }
  ],
  "extensions": {
    "merchant_contacted": false,
    "buyer_contacted_time": "2025-09-18T09:46:53.836Z"
  },
  "evidences": [
    {
      "evidence_type": "CREATE",
      "notes": "Test support case",
      "source": "SUBMITTED_BY_BUYER",
      "date": "2025-09-18T09:46:54.926Z",
      "dispute_life_cycle_stage": "INQUIRY"
    },
    {
      "evidence_type": "PROOF_OF_FULFILLMENT",
      "source": "REQUESTED_FROM_SELLER",
      "date": "2025-09-18T09:49:53.336Z"
    }
  ],
  "seller_response_due_date": "2025-10-08T09:46:54.926Z",
  "offer": {
    "buyer_requested_amount": {
      "currency_code": "USD",
      "value": "2.00"
    }
  },
  "refund_details": {
    "allowed_refund_amount": {
      "currency_code": "USD",
      "value": "2.00"
    }
  },
  "allowed_response_options": {
    "accept_claim": {
      "accept_claim_types": ["PARTIAL_REFUND", "REFUND"]
    },
    "make_offer": {
      "offer_types": ["REFUND"]
    }
  },
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/send-message",
      "rel": "send_message",
      "method": "POST"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/escalate",
      "rel": "escalate",
      "method": "POST"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/accept-claim",
      "rel": "accept_claim",
      "method": "POST"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/make-offer",
      "rel": "make_offer",
      "method": "POST"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/provide-evidence",
      "rel": "provide_evidence",
      "method": "POST"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response. The response includes the following parameters:

| Parameter                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Further action                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dispute_id`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                                  | Unique identifier for the dispute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this value to [respond to a dispute](#respond-to-a-dispute).                                                                                                                                                                               |
| `reason`<a id="reason" /><br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                     | Reason for the dispute.<Note>See [Dispute reasons and evidence](/growth/disputes/reference/dispute-reasons) for more information. </Note>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this value to determine and [provide the required evidence](#provide-evidence).                                                                                                                                                            |
| `status`<a id="status" /><br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                     | Current status of the dispute.<br /><br />**Possible values**: `OPEN`, `WAITING_FOR_SELLER_RESPONSE`, `WAITING_FOR_BUYER_RESPONSE`, `UNDER_REVIEW`, `RESOLVED`.<br /><br />PayPal may request additional evidence multiple times throughout the dispute’s lifecycle and the `WAITING_FOR_SELLER_RESPONSE` status indicates that you need to provide evidence.                                                                                                                                                                                                                                                                                                                                                                                | Use this value to determine your [response to a dispute](#respond-to-a-dispute).                                                                                                                                                               |
| `dispute_life_cycle_stage`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                    | Current stage of the dispute lifecycle. <br /><br />**Possible values**: `INQUIRY`, `CHARGEBACK`, `PRE_ARBITRATION`, `ARBITRATION`.<Note>For more information, see [Understand dispute lifecycle stages](#understand-dispute-lifecycle-stages).</Note>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this value to determine your [response to a dispute](#respond-to-a-dispute).                                                                                                                                                               |
| `evidences`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span>                                                    | Array of evidence documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this array to find the evidence requested for the dispute and share it using the [Provide evidence](#provide-evidence) endpoint.                                                                                                           |
| `evidences.evidence_type`<a id="evidences-evidence-type" /><br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>   | Type of evidence requested by PayPal.<br /><br />**Possible values**: `PROOF_OF_FULFILLMENT`, `PROOF_OF_REFUND`, `OTHER`, and so on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Use this value to determine the evidence you need to provide.                                                                                                                                                                                  |
| `evidences.source`<a id="evidences-source" /><br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                 | Source of the evidence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | If the value is `REQUESTED_FROM_SELLER`, you need to provide the evidence.                                                                                                                                                                     |
| `evidences.document.url`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                      | Downloadable URL for the evidence document. <br /><Note>Contact your PayPal account manager to add the <a href="/growth/disputes/set-up#disputes-api-2" target="_blank" rel="noopener noreferrer">additional scope</a> to enable document downloads.</Note>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this link to download the document provided as evidence.                                                                                                                                                                                   |
| `seller_response_due_date`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>                                    | Due date and time by which you need to respond to the dispute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Respond within this timeline to prevent the dispute from automatically closing in the customer's favor.                                                                                                                                        |
| `allowed_response_options`<a id="allowed-response-options" /><br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span> | Allowed response options for the dispute.<br /><br />**Response options**: <ul><li>`make_offer.offer_types`: Types of applicable offers.<br /><br />**Possible values**: `REFUND`, `REFUND_WITH_RETURN`, `REFUND_WITH_REPLACEMENT`, `REPLACEMENT_WITHOUT_REFUND`.</li><li>`accept_claim.accept_claim_types`: Types of applicable refunds.<br /><br />**Possible values**: `REFUND`, `REFUND_WITH_RETURN`, `PARTIAL_REFUND`, `REFUND_WITH_RETURN_SHIPMENT_LABEL`.</li><li>`acknowledge_return_item.acknowledgement_types`: Types of applicable acknowledgements for the item returned by the buyer.<br /><br />**Possible values**: `ITEM_RECEIVED`, `ITEM_NOT_RECEIVED`, `DAMAGED`, `EMPTY_PACKAGE_OR_DIFFERENT`, `MISSING_ITEMS`.</li></ul> | Use this value to respond with one of the following options:<ul><li>[Make an offer](#make-offer-to-resolve-dispute).</li><li>[Accept the claim](#accept-claim).</li><li>[Acknowledge the returned item](#acknowledge-returned-item).</li></ul> |
| `links`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span>                                                        | Array of HATEOAS links that list the applicable actions for the dispute at its current stage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Use these links to take further actions on the dispute.                                                                                                                                                                                        |

<Note>For information on all response parameters, see the [API reference](/reference/api/rest/disputes-actions/provide-evidence).</Note>

## Respond to a dispute

After gathering dispute information, you can determine the appropriate response action using the following key parameters from the [Show dispute details](#show-dispute-details) response:

- Use the HATEOAS `links` to understand the actions available at any stage of the dispute case lifecycle.
- Review the values of the `dispute_life_cycle_stage` and `status` parameters. Based on these values, the following table lists the possible response actions you can perform to ensure proper dispute handling:

| **Stage**                                                    | **Status**                    | **Description**                  | **Possible response actions**                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------ | ----------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INQUIRY`                                                    | `OPEN`                        | Dispute is created.              | None                                                                                                                                                                                                                                                                                                                                                                      |
| `INQUIRY`                                                    | `WAITING_FOR_SELLER_RESPONSE` | Waiting for merchant response.   | <ul><li>[Send message to other party](#send-message-to-other-party)</li><li>[Make offer to resolve dispute](#make-offer-to-resolve-dispute)</li><li>[Accept claim](#accept-claim)</li><li>[Escalate dispute to claim](#escalate-dispute-to-claim)</li><li>[Provide evidence](#provide-evidence)</li><li>[Acknowledge returned item](#acknowledge-returned-item)</li></ul> |
| `CHARGEBACK`, `PRE_ARBITRATION`, or `ARBITRATION`            | `UNDER_REVIEW`                | PayPal is reviewing the dispute. | [Provide supporting information](https://docs.paypal.ai/growth/disputes/handle-disputes/use-disputes-api#provide-supporting-information)                                                                                                                                                                                                                                  |
| `INQUIRY`, `CHARGEBACK`, `PRE_ARBITRATION`, or `ARBITRATION` | `WAITING_FOR_BUYER_RESPONSE`  | Waiting for buyer response.      | None                                                                                                                                                                                                                                                                                                                                                                      |
| `CHARGEBACK`, `PRE_ARBITRATION`, or `ARBITRATION`            | `WAITING_FOR_SELLER_RESPONSE` | Waiting for merchant response.   | <ul><li>[Provide evidence](#provide-evidence)</li><li>[Accept claim](#accept-claim)</li><li>[Make offer to resolve dispute](#make-offer-to-resolve-dispute)</li><li>[Appeal dispute](#appeal-dispute) (available only for disputes resolved in buyer's favor)</li><li>[Acknowledge returned item](#acknowledge-returned-item)</li></ul>                                   |
| `INQUIRY`, `CHARGEBACK`, `PRE_ARBITRATION`, or `ARBITRATION` | `RESOLVED`                    | Dispute is resolved.             | None                                                                                                                                                                                                                                                                                                                                                                      |

### Send message to other party

You can send a message to the other party during the inquiry stage to share information that helps resolve the dispute.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/send-message` endpoint with the [request parameter](/reference/api/rest/disputes-actions/send-message-about-dispute-to-other-party).

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<Tip>You can also attach documents and pictures to the message. To do this, you need to send a multipart request instead of a JSON one. For constraints and rules regarding documents, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Tip>

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/send-message \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
      "message": "Shipment is in progress."
    }'
  ```

```shell lines Sample multipart request theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/send-message \
  -H 'Content-Type: multipart/form-data' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -F 'input={
    "message": "Shipment is in progress."
  };type=application/json' \
  -F 'file1=@doc.pdf;type=application/pdf'
```

```json lines Sample response theme={null}
{
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034",
      "rel": "detail",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Make offer to resolve dispute

You can make an offer to the buyer to resolve the dispute. To determine which offer types are available for a specific dispute, check the `allowed_response_options.make_offer.offer_types` parameter in the [Show dispute details](#show-dispute-details) response.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/make-offer` endpoint with the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/make-offer-to-resolve-dispute" target="_blank" rel="noopener noreferrer">request parameters</a>.

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-ORC-10135512/make-offer \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
      "note": "Offer refund with replacement item.",
      "offer_amount": {
        "currency_code": "USD",
        "value": "10"
      },
      "offer_type": "REFUND_WITH_REPLACEMENT"
    }'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-ORC-10135512",
      "rel": "detail",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Accept claim

You can accept liability for a dispute by accepting the claim. This closes the dispute in the buyer's favor, and PayPal automatically refunds the buyer. To determine which refund types are available for a specific dispute, check the `allowed_response_options.accept_claim.accept_claim_types` parameter in the [Show dispute details](#show-dispute-details) response.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/accept-claim` endpoint with the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/accept-claim" target="_blank" rel="noopener noreferrer">request parameters</a>. You can also include the accept claim reason or invoice ID if required.

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803/accept-claim \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
      "note": "Full refund to the customer."
    }'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "rel": "self",
      "method": "GET",
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Provide evidence

You can provide evidence for a dispute to support your case. PayPal requests specific evidence based on the dispute reason. Check the following parameters in the [Show dispute details](#show-dispute-details) response to determine what evidence to provide:

- [`reason`](#reason)
- [`evidences.evidence_type`](#evidences-evidence-type)
- [`evidences.source`](#evidences-source)

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/provide-evidence` endpoint. Include the following parameters:

| Parameter name                                                                                     | Action                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `evidences.evidence_type`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | Set the evidence type as the value received in the [Show dispute details](#show-dispute-details) response. For example, `PROOF_OF_FULFILLMENT`.                                                                                                                                                      |
| `evidences.documents`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span>      | Provide the document details and attach the required evidence documents in the request.<Note>For constraints and rules regarding documents, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Note> |
| `evidences.notes`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>         | Provide any additional notes regarding the evidence.                                                                                                                                                                                                                                                 |
| `evidences.evidence_info`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span> | Provide details such as `refund_ids` or `tracking_info` in this object based on the `evidence_type`. For example, provide refund ID for `PROOF_OF_REFUND` and tracking information for `PROOF_OF_FULFILLMENT`.                                                                                       |

<Note>For more information on all request parameters, see the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/provide-evidence" target="_blank" rel="noopener noreferrer">API reference</a>.</Note>

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803/provide-evidence \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -H 'Content-Type: multipart/form-data' \
    -F 'input={
      "evidences": [
        {
          "evidence_type": "PROOF_OF_FULFILLMENT",
          "evidence_info": {
            "tracking_info": [
              {
                "carrier_name": "FEDEX",
                "tracking_number": "122533485"
              }
            ]
          },
          "notes": "Test"
        }
      ]
    };type=application/json' \
    -F 'file1=@NewDoc.pdf;type=application/pdf'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "rel": "self",
      "method": "GET",
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Escalate dispute to claim

If either party is unsatisfied with the other party's response during the inquiry stage, they can escalate the dispute to a claim. The dispute then moves to the claim stage.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/escalate` endpoint.

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034/escalate \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
    "note": "Escalating to PayPal claim for resolution."
    }'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-AYP-10135034",
      "rel": "detail",
      "method": "GET"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

<Note>For more information, see the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/escalate-dispute-to-claim" target="_blank" rel="noopener noreferrer">API reference</a>.</Note>

### Provide supporting information

You can provide additional supporting information for a case under PayPal's review to help with the review process.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/provide-supporting-info` endpoint with the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/provide-evidence" target="_blank" rel="noopener noreferrer">request parameter</a>.

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<Tip>You can also provide documents and pictures by sending a multipart request instead of a JSON one. For constraints and rules regarding documents, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Tip>

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803/provide-supporting-info \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
      "notes": "Additional supporting information"
    }'
  ```

```shell lines Sample multipart request theme={null}
curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803/provide-supporting-info \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'Content-Type: multipart/form-data'
  -F 'input={
        "notes": "Additional supporting information"
  };type=application/json' \
  -F 'file1=@NewDoc.pdf;type=application/pdf'
```

```json lines Sample response theme={null}
{
  "links": [
    {
      "rel": "self",
      "method": "GET",
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Appeal dispute

You can appeal a dispute that was resolved in the buyer's favor. To determine if a dispute is eligible for appeal, check whether the HATEOAS link for appeal is present in the [Show dispute details](#show-dispute-details) response.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/appeal` endpoint. Include the following parameters:

| Parameter name                                                                                     | Action                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `evidences.evidence_type`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span> | Set the evidence type based on the evidence you are providing for your appeal. For example, `PROOF_OF_FULFILLMENT`.                                                                                                                                                                                  |
| `evidences.documents`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>array</span>      | Provide the document details and attach the required evidence documents in the request.<Note>For constraints and rules regarding documents, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</Note> |
| `evidences.notes`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>string</span>         | Provide any additional notes regarding the evidence.                                                                                                                                                                                                                                                 |
| `evidences.evidence_info`<br /><span style={{color: '#95a5a6', fontSize: 'smaller'}}>object</span> | Provide details such as `refund_ids` or `tracking_info` in this object based on the `evidence_type`. For example, provide refund ID for `PROOF_OF_REFUND` and tracking information for `PROOF_OF_FULFILLMENT`.                                                                                       |

<Note>For information on all request parameters, see the <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/appeal-dispute" target="_blank" rel="noopener noreferrer">API reference</a>.</Note>

**Path parameter**: `ID` is the `dispute_id` returned in the [List disputes](#list-disputes) response.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803/appeal \
    -H 'Content-Type: multipart/form-data' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -F 'input={
      "evidences": [
        {
          "evidence_type": "PROOF_OF_FULFILLMENT",
          "evidence_info": {
            "tracking_info": [
              {
                "carrier_name": "FEDEX",
                "tracking_number": "122533485"
              }
            ]
          },
          "notes": "Test"
        }
      ]
    };type=application/json' \
    -F 'file1=@NewDoc.pdf;type=application/pdf'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "rel": "self",
      "method": "GET",
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-D-27803"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

### Acknowledge returned item

For SNAD disputes with the `MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED` reason, you can [make an offer to resolve the dispute](#make-offer-to-resolve-dispute) by offering a full refund in exchange for returning the item. After the buyer ships the returned item and reports it to PayPal, the acknowledge return item action becomes available. Use this endpoint to acknowledge receipt of the item.

To determine which acknowledgements are available for a specific dispute, check the `allowed_response_options.acknowledge_return_item.acknowledgement_types` parameter in the [Show dispute details](#show-dispute-details) response.

Use a <a href="/developer/how-to/api/get-started#2-get-an-access-token" target="_blank" rel="noopener noreferrer">valid access token</a> and make a `POST` call to the `/v1/customer/disputes/{ID}/acknowledge-return-item` endpoint. You can also include the note or acknowledgement type.

**Path parameter**: `ID` is the `dispute_id` for which you are acknowledging receipt of the returned item.

<CodeGroup>
  ```shell lines Sample request theme={null}
  curl -v -X POST https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-000-000-651-454/acknowledge-return-item \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ACCESS-TOKEN' \
    -d '{
      "note": "I have received the item back.",
      "acknowledgement_type": "ITEM_RECEIVED"
    }'
  ```

```json lines Sample response theme={null}
{
  "links": [
    {
      "rel": "self",
      "method": "GET",
      "href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-000-000-651-454"
    }
  ]
}
```

</CodeGroup>

A successful call returns a `200 OK` response and a HATEOAS link for the dispute.

<Note>For more information, see <a href="https://docs.paypal.ai/reference/api/rest/disputes-actions/acknowledge-returned-item" target="_blank" rel="noopener noreferrer">API reference</a>.</Note>

## Common issues

When calling the Disputes API, you may see these common errors:

- 400 Bad Request when required fields or formats are invalid. Fix: Validate request body and parameters against the Disputes API reference.
- 401 Unauthorized when the access token is missing, expired, or invalid. Fix: Regenerate the access token and retry the call with the updated token.
- 403 Forbidden when the app or account is not permitted to perform the requested action. Fix: Confirm Disputes API access, scopes, and account permissions.

For more details, see the [HTTP status codes and error messages](/developer/how-to/api/troubleshooting/common-errors/overview#http-status-codes-and-error-messages).

## Use webhooks to monitor dispute events

Webhook events are external events that your app does not know about unless it receives event notifications. For example, a new dispute raised or resolved is a webhook event. You can subscribe to such events and register a callback (listener) URL. When the event occurs, PayPal sends a notification to the registered callback URL. You can code your app to perform relevant actions based on the event notification it receives.

To handle webhook events:

1. Review the <a href="/reference/webhook-events/disputes-v1" target="_blank">list of webhook events for disputes</a> and select the events for your app to subscribe.
2. Subscribe to the selected webhook events through one of the following means:
   - **PayPal developer account**: Log in to your account, go to <strong>App details</strong> page > <strong>Features</strong> > <strong>Webhooks</strong>, and subscribe to webhook events.
   - <a href="https://docs.paypal.ai/reference/api/rest/webhooks/list-webhooks" target="_blank">Webhooks management API</a>.
3. In your server-side app code, define a webhook handler that:
   - <a href="https://docs.paypal.ai/reference/api/rest/webhooks/create-webhook#body-url" target="_blank">Listens to the webhook event</a>.
   - <a href="https://docs.paypal.ai/reference/webhook-events/webhook-format" target="_blank">Processes the webhook event message sent to your listener URL</a>.
   - <a href="https://docs.paypal.ai/reference/api/rest/verify-webhook-signature/verify-webhook-signature#body-webhook-event" target="_blank">Verifies the source of the event notification</a>.
   - Performs further actions based on event data.

See [Webhook management](https://docs.paypal.ai/reference/api/rest/webhooks/list-webhooks) for more information.
