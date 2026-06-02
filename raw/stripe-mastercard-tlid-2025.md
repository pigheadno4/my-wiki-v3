<!-- Source URL: https://docs.stripe.com/payments/mastercard-tlid -->
<!-- Fetched: 2026-05-01 -->

# Mastercard Transaction Link ID

Learn more about Mastercard's Transaction Link ID (TLID).

Transaction Link ID (TLID) is a unique identifier that Mastercard generates for each transaction. It links transactions across authorization and clearing messages, similar to the network transaction ID or NTID. TLIDs are 22 characters long, alphanumeric (`A-Z`, `a-z`), case sensitive, and can include `-` and `_`. For example:

- `e7R9d3L2-Q9vS6pP1_WzEh`
- `Z0fE_2qV-3pWft4vHt7Ki6M`

## Review the timeline

Starting June 2, 2026, Mastercard requires acquirers and businesses to retain TLIDs for:

- Cardholder-initiated transactions (CITs) that store card credentials for future use.
- Account status inquiry (ASI) requests.

Starting October 23, 2026, Mastercard requires you to send the TLID retained from the original CIT with merchant-initiated transactions (MITs).

Note that no changes are expected to NTID. Its use continues in parallel with TLID.

| Date             | Requirement                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| June 2, 2026     | Retain TLIDs from CITs that set up future card use and from ASI requests. The acquirer or business must retain these TLIDs. |
| October 23, 2026 | Send the TLID retained from the original CIT or ASI request with all subsequent MITs as the economically related TLID.      |

## Understand the impact

Stripe will store TLIDs for all businesses when Mastercard provides them. Stripe will populate the economically related TLID on an MIT if Stripe has a saved TLID, for example when the original CIT was processed with Stripe.

If the CIT was processed before June 2, 2026, Stripe will send the TLID from the earliest authorized MIT after June 2, 2026, as Mastercard recommends.
