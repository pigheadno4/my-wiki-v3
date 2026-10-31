# C59 Dispute webhooks v4 overview fixed-query answers

## Q1

The 2026-09-15-captured API Explorer page labels the family **Dispute webhooks v4**. It says Adyen sends these webhooks about creation or update of raised disputes and chargebacks resulting from raised disputes (raw lines 5–9). Its endpoint catalog lists incoming POST event types `balancePlatform.dispute.created` and `balancePlatform.dispute.updated`, summarized as dispute created and dispute updated (lines 11–17). The overview supplies no event payload schema, resource identity fields, requiredness, state transitions or example; those need the separate event references. `latest` is a route label, not independent current-version proof. Canonical route: [[source-adyen-api-explorer-dispute-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/dispute-webhooks/latest/overview.

## Q2

The overview establishes the webhook family purpose and two event routes, but not a particular dispute stage, chargeback result, amount, booking, reversal or funds outcome (raw lines 5–17). It says nothing about event payload requirements, delivery, ordering, retry, deduplication, authentication/signature or acknowledgement. The wording about chargebacks resulting from raised disputes does not map either listed event to a final chargeback outcome. The captured title says v4; `latest` does not prove current status beyond the snapshot. Canonical route: [[source-adyen-api-explorer-dispute-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/dispute-webhooks/latest/overview.
