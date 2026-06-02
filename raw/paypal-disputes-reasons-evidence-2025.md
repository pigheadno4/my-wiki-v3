<!-- Source URL: https://docs.paypal.ai/growth/disputes/reference/dispute-reasons -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dispute reasons and evidence

You can determine what evidence to provide for a dispute or chargeback based on its reason.

To defend a dispute or chargeback effectively:

1. Use the <a href="/growth/disputes/handle-disputes/use-disputes-api#show-dispute-details" target="_blank" rel="noopener noreferrer">Show dispute details</a> response to determine the required evidence. The `reason` and `evidences.evidence_type` parameters denote the dispute reason and the evidence type respectively.
2. Use the <a href="/growth/disputes/handle-disputes/use-disputes-api#provide-evidence" target="_blank" rel="noopener noreferrer">Provide evidence</a> endpoint to submit the evidence to PayPal.

Each dispute reason requires specific evidence that helps PayPal review and resolve the case. The following sections list the dispute reasons and the required evidence for each reason.

### MERCHANDISE_OR_SERVICE_NOT_RECEIVED

The buyer did not receive the merchandise or service.

| Evidence type          | Required evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `PROOF_OF_FULFILLMENT` | Provide one of the following to PayPal:<ul><li>Carrier name and tracking number through `evidences.evidence_info.tracking_info.carrier_name` and `evidences.evidence_info.tracking_info.tracking_number` parameters respectively.</li>Or<li>Notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, a document can be a proof of delivery signature or a proof of receipt copy. For more information about supported files, see <a href="/growth/disputes/reference/supported-file-types-sizes" target="_blank" rel="noopener noreferrer">Supported file types and sizes</a>.</li></ul> |
| `PROOF_OF_REFUND`      | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED

The buyer reports that the merchandise or service was not as described.

| Evidence type     | Required evidence                                                                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, you can include a product description, item URL, return policy, or a copy of a contract or an affidavit. |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                                                                                                                                                    |

### UNAUTHORISED

The buyer did not authorize purchase of the merchandise or service.

| Evidence type          | Required evidence                                                                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PROOF_OF_FULFILLMENT` | Provide the carrier name and tracking number through `evidences.evidence_info.tracking_info.carrier_name` and `evidences.evidence_info.tracking_info.tracking_number` parameters respectively.  |
| `PROOF_OF_REFUND`      | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                                                                                                                       |
| `OTHER`                | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, a document can be a proof of delivery signature or a proof of receipt copy. |

### CREDIT_NOT_PROCESSED

The refund or credit transaction was not processed for the buyer.

| Evidence type     | Required evidence                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                                                                                  |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, a document can be a credit due reason. |

### DUPLICATE_TRANSACTION

The transaction was a duplicate.

| Evidence type     | Required evidence                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                              |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. |

### INCORRECT_AMOUNT

The buyer was charged an incorrect amount.

| Evidence type     | Required evidence                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter for the difference in amount.                                                           |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, a document can be a price difference reason. |

### PAYMENT_BY_OTHER_MEANS

The buyer paid for the transaction through other means.

| Evidence type     | Required evidence                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter for the difference in amount. |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. |

### CANCELED_RECURRING_BILLING

The buyer was incorrectly charged after canceling the subscription or recurring billing.

| Evidence type     | Required evidence                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter for the difference in amount.                                                          |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. For example, a document can be a subscription agreement. |

### OTHER

| Evidence type     | Required evidence                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| `PROOF_OF_REFUND` | Pass the refund ID in the `evidences.evidence_info.refund_ids` parameter.                              |
| `OTHER`           | Pass the notes or documents in the `evidences.notes` or `evidences.documents` parameters respectively. |
