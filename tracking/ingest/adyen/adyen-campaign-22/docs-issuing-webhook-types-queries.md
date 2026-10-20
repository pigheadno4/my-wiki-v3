# C22 worker retrieval checks — docs-issuing-webhook-types

## Q1: Which Issuing events does this catalog route, and how should an event be read?

The captured catalog maps balance-platform resource changes, card payment/refund and fund movement, disputes and reports to webhook families (raw lines 19–35, 39–96). `type` identifies an event; some families add `data.status` for lifecycle outcome (line 37). Transfer `created` is a request to credit or deduct a balance account, whereas `updated` is a status change (lines 62–69). The catalog marks older payment webhooks deprecated and directs use of transfer webhooks (lines 98–109). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-webhook-types]] → [[raw/adyen/docs/issuing/webhook-types/2026-09-15]].

## Q2: What boundaries or conflicts affect payment and dispute interpretation?

A transfer-created event alone does not prove funds booked or a final payment outcome; statuses must be read in their own event context (raw lines 37, 62–79). This catalog calls the second-chargeback transfer `type: chargeback`, `status: secondChargeback` (line 79), whereas the related Issuing dispute guide says `type: secondChargeback`, `status: secondChargeback` (raw/adyen/docs/issuing/raise-disputes/2026-09-15.md:136). It also lists dispute-updated `secondChargeback` (line 88) where that guide's dispute lifecycle uses `secondPresentment` (related raw line 119). The opening subscription list and detailed sections do not align perfectly (this raw lines 28–35, 39–109). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-webhook-types]] → [[raw/adyen/docs/issuing/webhook-types/2026-09-15]].
