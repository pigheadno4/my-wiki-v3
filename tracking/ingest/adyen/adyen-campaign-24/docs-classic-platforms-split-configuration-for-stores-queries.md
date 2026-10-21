# docs-classic-platforms-split-configuration-for-stores — attempt 1 retrieval checks

## Q1. What configures an automatic Classic store split, and where does it apply?

In this **Classic** guide, a store-based POS or partner-platform integration must be enabled by Support and have the Customer Area split-configuration role (raw lines 78–82). Create a Customer Area rule profile and UUID, then attach it to a store with `splitConfigurationUUID` and the holder account-code `virtualAccount` using Classic Account API `/updateAccountHolder` (raw lines 84–111). The TEST examples use Account API v6 (raw lines 117–168). Rules select a commission fee using channel, currency and payment-method conditions, with priority currency → payment method → funding source → channel (raw lines 28–53). Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-split-configuration-for-stores]] → [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15]].

## Q2. What happens when no rule matches or the API supplies a split, and when is the store update final?

If **no rule matches**, all funds go to the liable account; a catchall is recommended (raw line 42). Payment/capture API split instructions **override** the automatic store split (raw line 44). `/updateAccountHolder` is asynchronous, so the response is not the final store-change result; rely on `ACCOUNT_HOLDER_UPDATED` notification (raw lines 169–171). The example calculations do not prove a particular capture, allocation or settlement (raw lines 55–76). Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-split-configuration-for-stores]] → [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15]].
