# Create test cards retrieval checks — attempt 2

## Q1 — Purpose and scope

**Query:** What does Adyen's Create test cards page let me create, and does it fund or validate live payments?

**Answer:** It documents custom card-number ranges for Adyen's test platform, through the test Customer Area or `/createTestCardRanges`. Test-card transactions do not produce credits or debits to live accounts. This is a test simulation guide; it does not establish production card, merchant or payment-method eligibility, or live payment success. **Raw locators:** `raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15.md:15-21`, `:41-53`. **Canonical route:** [[source-adyen-docs-development-resources-test-cards-and-credentials-create-test-cards]] → [[raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15]]; [[adyen-payment-testing]].

## Q2 — Creation prerequisites and result boundary

**Query:** What checks apply when generating custom test-card ranges, and can I copy the SOAP request example as a working template?

**Answer:** Customer Area use requires the **Manage test cards** role. Ranges must use a shared 6–19 digit length and valid BIN/card constraints; billing address needs a street address, with ZIP optional. Creation does not Luhn-check range bounds, but a generated card used for a test payment receives normal checks including Luhn. The pinned SOAP request example reverses start and end in both ranges, while the page says that condition fails generation with a 4XX or 5XX response, so it is illustrative rather than a working creation request. The API example responses show `ALREADY_EXISTS`, not newly created ranges. Inspect response codes and faults, including range or merchant-account errors, before claiming a range was created. The guide routes failure simulations to result-code/refusal-reason guidance. **Raw locators:** `raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15.md:21-39`, `:102-147`, `:149-210`, `:225-256`. **Canonical route:** [[source-adyen-docs-development-resources-test-cards-and-credentials-create-test-cards]] → [[raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15]]; [[adyen-payment-testing]].
