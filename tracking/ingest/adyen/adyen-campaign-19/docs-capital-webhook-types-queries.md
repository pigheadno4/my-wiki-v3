# Retrieval probes — Capital webhook types

Q1. Which Capital events represent offers and grant lifecycle, and do grant-initiation updates imply a funds-transfer event?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-webhook-types]] → [[raw/adyen/docs/capital/webhook-types/2026-09-15]].

Expected answer: Dynamic offers use `balancePlatform.capital.dynamicOffer.created`; static offers use `balancePlatform.balanceAccountHolder.capitalOffer.created`; grant creation/update use `balancePlatform.grants.created` and `.updated`. The page expressly says grant initiation status updates generate only Capital notifications, not Transfer or Transaction notifications. Created offer/grant notices do not prove acceptance or funding. Raw locators: lines 19–35, 37–60; opening and three Capital webhook headings.

Q2. How does the page distinguish grant disbursement, regular versus unscheduled repayment, and a booked transaction?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-webhook-types]] → [[raw/adyen/docs/capital/webhook-types/2026-09-15]].

Expected answer: Transfer created/updated events use `category=grants`; nested transfer type/direction classify disbursement (grant/incoming), regular repayment (repayment/outgoing), and unscheduled repayment (capitalFundsCollection plus repayment, incoming plus outgoing). After booking in a balance account, `balancePlatform.transaction.created` identifies a transaction; its `transfer.id` should match the grant-movement transfer and `transfer.reference` the grant ID in the related transfer. The hub provides no full status enumeration, Configuration-webhook taxonomy or external bank-receipt proof. Raw locators: lines 62–98; `## Transfer webhook`, `## Transaction webhook`.
