# Fixed retrieval checks — docs-point-of-sale-standalone

## Query 1: What is Adyen's standalone POS solution, and does a merchant POS app have to integrate with Terminal API to use it?

**Purpose and scope:** The 2026-09-15 standalone overview describes in-person transactions initiated directly on the standalone terminal without POS app development or integration. The POS-app-to-terminal Terminal API flow is a different integration path. Use [[source-adyen-docs-point-of-sale-standalone]] through [[adyen-standalone-terminals]] for the overview; use [[adyen-terminal-api]] for integrated POS messaging.

**Capability and prerequisites:** Staff can initiate payments directly on a supported standalone terminal. The page restricts standalone use to built-in-printer devices because a printed customer receipt must be possible and lists S1F2, S1F2L, V210, V240m Plus (Brazil), V400c Plus and V400m in this snapshot.

**Warnings and do not infer:** No development/integration work on this path does not waive terminal setup, merchant enablement, payment-method restrictions, current model/country availability, or operational reconciliation. The source is not proof of current eligibility, payment success or security certification. It expressly excludes shopper recognition and tax-free shopping, and calls for manual reconciliation against sales and returns.

**Retrieval route:** Root [[index]] → [[adyen-index]] → proposed [[adyen-standalone-terminals]] → [[source-adyen-docs-point-of-sale-standalone]] → `[[raw/adyen/docs/point-of-sale/standalone/2026-09-15]]`. The concept and C06 source/index entries are pending coordinator promotion.

## Query 2: Can a standalone terminal keep taking payments if an integrated POS app loses connectivity, and what does this page support?

**Purpose and scope:** The overview proposes a standalone terminal as fallback when a POS app cannot communicate with integrated terminals. The operator starts the transaction directly on the standalone device; this is not evidence that a POS Terminal API request was delivered or recovered.

**Capability and prerequisites:** The page says to enable cellular connectivity or offline payments on the standalone terminal for the described fallback. It lists basic payment-related functions and points to separate build/use and feature guides for procedures. A built-in printer remains the stated standalone terminal constraint.

**Warnings and do not infer:** The page does not guarantee operation during every network failure or later success of an offline payment. It does not determine merchant enablement, current carrier connectivity, eligible transaction types, liability, payment outcome, or a safe retry procedure. Consult the linked cellular or offline guide and the merchant's actual configuration for those questions. Manual reconciliation remains necessary; shopper recognition and tax-free shopping are excluded.

**Retrieval route:** Root [[index]] → [[adyen-index]] → proposed [[adyen-standalone-terminals]] → [[source-adyen-docs-point-of-sale-standalone]] → raw line 25 under `## Fallback`, plus lines 27–35 and 65–67 for printer/operation limits. The detailed standalone build/use and cellular/offline pages are navigation from this overview; their claims are outside this read.
