---
title: "Braintree In-Person PayPal and Venmo QR Code Guide"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/paypal-and-venmo-qrc"
raw_files:
  - "braintree/in-person/guides/paypal-and-venmo-qrc-2026-09-16.md"
tags: [braintree, in-person, paypal, venmo, qr-code, limited-release]
---

## Overview

This unversioned Braintree website snapshot documents a merchant-presented PayPal and Venmo QR Code payment option on Braintree In-Person readers. The page labels the feature limited release and requires additional approval before enablement; it is a reader- and account-setup guide, not evidence of present support, merchant approval or enablement, a current SDK or GitHub implementation, or an individual payment, settlement or funding outcome.

## Key takeaways

- The documented channel is a Braintree In-Person card reader. Once an approved and enabled location is paired to the reader, the customer selects the PayPal/Venmo QRC option on that reader, the reader displays a generated QR code, and the customer scans it with a PayPal or Venmo mobile app. Displaying or scanning the code is a request-flow step, not payment approval, authorization, capture, settlement or funding proof.
- Enablement is account- and location-scoped: the page calls for PayPal and Braintree onboarding with a Solutions Engineer, a Braintree merchant account association for each retail currency, PayPal account connection and third-party permissions, and a PayPal Payer ID for the receiving account. The location must have QR payments enabled and be paired to the reader; possession of a reader, account or Payer ID alone does not establish enablement.
- The setup section is sandbox-specific: it calls for PayPal sandbox Business and Personal accounts, uses the Business Account ID/Payer ID for location enablement, and uses the Personal account with separately granted PayPal and Venmo test-flight app access to scan codes on sandbox readers. These testing steps do not establish production availability or execution.
- A charge is requested from the reader through the ordinary in-person path. The page says the POS should poll until the in-store context becomes `COMPLETE` and handle the PayPal- or Venmo-specific `PaymentMethodSnapshot`; context completion and returned snapshot data must not be restated as authorization, approval, capture, settlement or funding without the transaction's applicable lifecycle evidence.
- QR Code payment methods do not support vaulting. The documented vault-after-transaction flag hides the QRC choices, while the optional QRC override controls reader display for no-vault versus reusable-token use cases; use the raw locator for exact request values and example shapes.
- For QRC transactions, the page supports referenced refunds and reversals. If neither can be completed, it describes an unreferenced refund to an alternate credit or debit card chosen by the customer; this is not a claim that any refund request will succeed.

## Consequential conditions

> [!warning] Limited-release approval and snapshot boundary
> The page requires additional approval before enabling the feature and directs prospective integrators to their Solutions Engineer plus Account Executive or Customer Success Manager. Its 2026-09-16 website snapshot does not prove current availability, merchant-specific approval, hardware or app operability, or parity with any SDK or GitHub version.

> [!warning] Order ID account-setting effect
> The page says a PayPal account may block multiple payments per invoice ID, causing repeated `orderId` transaction requests to be rejected and potentially affecting tests or split tender. It proposes a PayPal Block Payments setting change but says to consult a PayPal Solutions or Integration Engineer because the change may affect other integration components.

## Detail locators

- Limited-release reader flow and additional approval contacts: opening text and note, raw lines 14-19.
- Reader selection, QR generation and PayPal/Venmo mobile-app scan: `## Access New Customers and Enable Next Generation In-Person Checkout Experiences`, raw lines 22-30.
- Sandbox Business/Personal accounts, Account ID/Payer ID roles and specialist-assisted final setup: `## Sign Up for a PayPal Developer Account`, raw lines 33-52.
- Account onboarding, per-currency merchant-account association, PayPal connection permissions and consumer-app branding inputs: `## Pre-requisite Steps to Enabling QRC`, raw lines 55-64.
- New-location fields, Payer ID destination, `internalName` to settlement-report `storeId` propagation and the 64-character transaction-error condition: `### Step 1.1 - Creating a Location enabled for QRC`, raw lines 69-78.
- Existing-location enablement mutation and example response: `### Step 1.2 Updating an existing Location to enable QRC`, raw lines 81-85.
- Customer reader selection and app scan in the transaction flow: `### Step 2 - Make a transaction with QRC`, raw lines 86-90.
- No-vault support boundary, automatic hiding with the vaulting flag, optional QRC override values and request/response example: `#### Vaulting and QRC`, raw lines 93-102.
- Polling, in-store context completion and PayPal/Venmo snapshot fields: `### Step 3 - Look for a New Payment Method Snapshot`, raw lines 105-109.
- Sandbox-reader end-to-end testing, test-flight app access, mobile OS and store-account email requirements: `## Testing QRC Flows End to End`, raw lines 110-115.
- Duplicate-invoice blocking, repeated `orderId` and split-tender implications, account setting path and consultation warning: `## Use of the orderId field for PayPal and Venmo Transactions`, raw lines 118-123.
- Referenced-refund, reversal and alternate-card unreferenced-refund scope: `## Refunding Transactions with QRC`, raw lines 126-128.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/in-person/guides/paypal-and-venmo-qrc-2026-09-16|Braintree PayPal and Venmo QRC guide]] - complete collected page for the limited-release reader flow, account and sandbox prerequisites, location enablement, no-vault condition, response handling, order-ID setting and refund routes
