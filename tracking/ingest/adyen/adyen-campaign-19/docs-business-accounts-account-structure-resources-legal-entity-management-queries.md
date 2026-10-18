# Fixed queries — docs-business-accounts-account-structure-resources-legal-entity-management

## Q1 — resource identity and purpose

**Query:** Which Legal Entity Management resources does the captured Business Accounts page require for verification, and what does each represent?

**Answer boundary:** It lists a legal entity for user details, a payout transfer instrument described as the user's verified bank account, and a supporting document for legal-entity or transfer-instrument information. It points to the Legal Entity Management API for management. This is a resource description, not proof of account opening, verification completion, bank ownership, or payout receipt.

**Forward route:** [[index]] → [[adyen-index]] (coordinator must add forward [[adyen-business-accounts]] route) → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-account-structure-resources-legal-entity-management]] → [[raw/adyen/docs/business-accounts/account-structure-resources/legal-entity-management/2026-09-15]]. Exact raw locators: lines 19–31.

## Q2 — verification prerequisite and relationship limit

**Query:** Does creating a legal entity or supporting document mean a Business Account user has passed verification, and does this capture define the association cardinality?

**Answer boundary:** No. The page says resources provide information Adyen requires to verify users before payments, payouts, or financial products. It offers an image of connections but no textual cardinality; the captured Markdown cannot support a detailed association model. Check separate verification and account lifecycle sources for outcomes.

**Forward route:** [[index]] → [[adyen-index]] (coordinator must add forward [[adyen-business-accounts]] route) → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-account-structure-resources-legal-entity-management]] → [[raw/adyen/docs/business-accounts/account-structure-resources/legal-entity-management/2026-09-15]]. Exact raw locators: lines 17–21 and 23–33.
