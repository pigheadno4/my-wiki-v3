# Fixed retrieval answers — api-explorer-webhooks-latest-overview

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-webhooks-latest-overview.md` (`https://docs.adyen.com/api-explorer/Webhooks/latest/overview`).

## Q1

The 2026-09-15 captured overview identifies **Webhooks v1** and says Adyen uses webhooks for payment-status updates, newly available reports and other subscribed events (raw lines 5–7). Its General table lists incoming `POST` event-reference routes and short purposes: e.g. `/AUTHORISATION` result of an authorisation request (line 15), `/CAPTURE` result of a capture request (line 21), `/CHARGEBACK` payment charged back (line 23), `/PAIDOUT_REVERSED` financial institution rejected payout (line 38), and `/REPORT_AVAILABLE` report available (line 55). The table spans lines 11–63. This overview provides no event-code property, resource/reference identifiers, required or conditional payload fields, response contract, trigger details beyond route summaries, or timing rules. Consult individual event references for event-specific detail; this catalog itself supplies none of those rules. Source: `raw/adyen/api-explorer/Webhooks/latest/overview/2026-09-15.md:5-63`; canonical URL above.

## Q2

The page is a catalog, so it establishes neither receiver request acceptance nor payment/capture/settlement/payout finality. It separately lists failure/reversal events including `/CAPTURE_FAILED` (scheme rejection, line 22), `/REFUND_FAILED` and `/REFUND_NOT_CLEARED` (lines 52–53), and `/SETTLED_REVERSED` (line 61). It has no acknowledgement or relayed-decision response rules, delivery order, retries, deduplication, signatures, or deprecation statements. Its title says Webhooks v1 while the canonical URL uses `latest`; that is a snapshot label, not a version guarantee. Source: `raw/adyen/api-explorer/Webhooks/latest/overview/2026-09-15.md:5-63`; canonical URL above.
