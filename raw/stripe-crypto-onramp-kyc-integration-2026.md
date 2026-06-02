<!-- Source URL: https://docs.stripe.com/crypto/onramp/kyc-integration-guide -->
<!-- Fetched: 2026-05-11 -->

# Integrate the KYC tier system for the Embedded Components onramp

Learn about KYC verification tiers, the information required for each, and how to detect when a user's purchase amount is limited by their verification level.

All users must pass KYC verification before they can buy crypto with the onramp. Users can provide additional information to increase their purchase limits. This guide covers the KYC tiers, the information required for each tier, and how you can detect when a user’s purchase amount is limited by the amount of KYC information provided.

## Before you begin

Before you begin, [integrate the Embedded Components Onramp](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md).

## KYC tier comparison

The following table summarizes the requirements for each KYC tier.

| KYC tier | User inputs                 |
| -------- | --------------------------- |
| L0       | Name, phone, email, address |
| L1       | + Date of birth, SSN        |
| L2       | + Photo ID, selfie          |

## KYC API

### Use attachKYCInfo for L0 and L1 KYC

Call `attachKYCInfo` to initiate the L0 and L1 KYC verification processes for a user.

The fields collected by `attachKYCInfo` depend on the tier:

- **L0**: `firstName`, `lastName`, `address`
- **L1**: All L0 fields, plus `dateOfBirth`, `idNumber`, `idType`

L0 and L1 verification are asynchronous. Call this API and check the verification status before you create an onramp session. [Creating a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) returns a `400` error if the user has pending verifications. Continue retrieving the verification result until no verification remains pending. See [Determine whether a user is verified](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md#determine-whether-a-user-is-verified) for details.

### Use verifyIdentity for L2 KYC

Call `verifyIdentity` to present a Stripe-hosted flow where the user uploads an identity document and a selfie.

L2 verification is asynchronous. Your backend must call the [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API with the `customerId`. The API returns the L2 verification status in `id_document_verified`.

### Handling KYC error for createCryptoPaymentToken

Users must submit their L0 KYC information before you can collect payment methods. If a user hasn’t completed L0 verification, `createCryptoPaymentToken` returns a `crypto_onramp_missing_minimum_identity_verification` error. Handle this error by prompting the user to submit their L0 KYC information.

### Determining a user’s current KYC tier

[Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) with the `customerId` and inspect the `kyc_tiers` field to determine a user’s current KYC tier. The user’s current tier is the highest tier where `verification_status` is not `not_available` or `not_started`.

The `verification_status` values for each tier are:

| Value           | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| `not_available` | Verification is not supported for the user’s region.            |
| `not_started`   | The user hasn’t provided the required fields for this tier yet. |
| `pending`       | Verification has been submitted and is processing.              |
| `rejected`      | Verification failed.                                            |
| `verified`      | Verification completed successfully.                            |

For example, given the following `kyc_tiers` response:

```json
"kyc_tiers": [
  { "tier": "l0", "verification_status": "verified", "verification_errors": [] },
  { "tier": "l1", "verification_status": "verified", "verification_errors": [] },
  { "tier": "l2", "verification_status": "not_started", "verification_errors": [] }
]
```

The user’s current tier is L1 because it is the highest tier that is not `not_available` or `not_started`.

After [Retrieving a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md), use the following snippet to determine the user’s current KYC tier from the `kyc_tiers` field in the response:

```js
// Iterates from the highest tier (l2) to the lowest (l0) and returns the first tier
// whose verification_status is "pending", "rejected", or "verified" (meaning the user
// has at least attempted that tier). Returns undefined if no tier has been started.
const currentTier = ["l2", "l1", "l0"].find((t) =>
  ["pending", "rejected", "verified"].includes(
    customer.kyc_tiers.find((k) => k.tier === t)?.verification_status,
  ),
);
```

You can also use the `provided_fields` field to determine a user’s tier:

| User | Provided fields                                                                                                                            |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| L0   | `first_name`, `last_name`, `address_line_1`, (`address_line_2`), `address_city`, `address_state`, `address_postal_code`, `address_country` |
| L1   | All L0 fields, plus `id_number`, `id_type`, `dob`                                                                                          |
| L2   | All L1 fields, plus `id_document`, `selfie`                                                                                                |

### Determine whether a user is verified

After retrieving the user’s current KYC tier, check whether the tier entry for that tier has `verification_status: "verified"`. If so, the user is verified at that tier.

The following table summarizes how to use the `kyc_tiers` field to check verification status:

| User | Verified                                                                      |
| ---- | ----------------------------------------------------------------------------- |
| L0   | The `kyc_tiers` entry with `tier: "l0"` has `verification_status: "verified"` |
| L1   | The `kyc_tiers` entry with `tier: "l1"` has `verification_status: "verified"` |
| L2   | The `kyc_tiers` entry with `tier: "l2"` has `verification_status: "verified"` |

The deprecated `verifications` field can also be used to determine verification status:

| User | Verified                                           |
| ---- | -------------------------------------------------- |
| L0   | `kyc_verified: true`, `phone_verified: true`       |
| L1   | `kyc_verified: true`                               |
| L2   | `kyc_verified: true`, `id_document_verified: true` |

### Interpret limit errors from CryptoOnrampSession

Your backend must [Create a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) to create a [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/object.md). If the user reaches a purchase limit, the `Create a CryptoOnrampSession` API returns an HTTP `400` error with a JSON object that describes the error. Your application can use these errors to request more information from the user so they can complete the transaction.

If creating a CryptoOnrampSession returns an HTTP `400` error with one of the following error codes, [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) with the `customerId` to determine the next step.

- `crypto_onramp_missing_minimum_identity_verification`
- `crypto_onramp_missing_identity_verification`
- `crypto_onramp_missing_document_verification`

The following table summarizes how to use both the error code from [Creating a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) and the `kyc_tiers` field from [Retrieving a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) to determine the next step.

| Error code                                                                                                    | Meaning                                                                                                     | Next step |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------- |
| `crypto_onramp_missing_minimum_identity_verification`                                                         | L0 verification failed. The customer must provide full L0 data to complete the transaction:                 |
| - The user is an L0 user and they didn’t pass the minimum identity verification required to create a session. | Prompt the user to provide valid L0 KYC information, including name, phone, email, and address.             |
| `crypto_onramp_missing_identity_verification`                                                                 | L1 verification is required. The customer must provide full or partial L1 data to complete the transaction: |

- The user is an L1 user and they didn’t pass the L1 identity verification required to create a session.
- The user is a verified L0 user but the transaction requires L1 verification. | Inspect [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API response `kyc_tiers` to determine the next step.
- If the user’s current tier is L1, prompt the user to provide full L1 KYC information, including name, address, date of birth and Social Security number.
- If the user’s current tier is L0, prompt the user to provide only `dob`, `id_number`, `id_type`, then upload partially with `attachKYCInfo` (only include these three fields). |
  | `crypto_onramp_missing_document_verification` | L2 verification is required. The customer must provide a photo ID and selfie to complete the transaction:
- The user is an L2 user and they didn’t pass the L2 document identity verification required to create a session.
- The user is a verified L0 user but the transaction requires L2 verification.
- The user is a verified L1 user but the transaction requires L2 verification. | Inspect [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API response `kyc_tiers` to determine the next step.
- If the user’s current tier is L2, prompt the user to complete L2 KYC verification with `verifyIdentity`.
- If the user’s current tier is L0, prompt the user to collect only `dob`, `id_number`, `id_type`, upload partially with `attachKYCInfo`, then prompt the user to complete L2 KYC verification with `verifyIdentity`.
- If the user’s current tier is L1, prompt the user to complete L2 KYC verification with `verifyIdentity`. |
