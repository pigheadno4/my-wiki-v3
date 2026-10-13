# Cartes Bancaires generic-concept reconciliation

**Semantic approval:** Approved as a narrow provider-attribution and route correction based on the reviewed Adyen snapshot and the existing Stripe raw. This is not approval to generalize Adyen's three automatic defenses into a merchant right to contest, or to generalize Stripe's merchant-contestation statement to Adyen.

In `wiki/concepts/cartes-bancaires.md`, replace the exact dispute bullet:

```markdown
- **Cannot contest** Cartes Bancaires disputes
```

with:

```markdown
- **Stripe processing:** Stripe says businesses cannot contest Cartes Bancaires disputes. For Adyen's distinct, limited automatic-defense grounds and its non-defendable reason code 45, see [[source-adyen-docs-risk-management-chargeback-guidelines-cartes-bancaires-chargebacks]] and [[adyen-risk-management]].
```

The existing `[[source-stripe-cartes-bancaires]]` source remains the authority for the Stripe statement. The Adyen source route should be added under the generic concept's `## Sources` as:

```markdown
- [[source-adyen-docs-risk-management-chargeback-guidelines-cartes-bancaires-chargebacks]] — Adyen-specific automatic-defense grounds and non-defendable reason code 45 (2026-09-15 webpage snapshot).
```

The root-index line `wiki/index.md:58` currently repeats the unqualified “cannot contest” claim. If the coordinator updates that navigational label in the same reconciliation, use “Stripe dispute contestation limit; Adyen automatic-defense route” in place of “cannot contest”.

Evidence: `raw/stripe-cartes-bancaires-2025.md:120-126` explicitly says businesses cannot contest disputes in a Stripe payment-method guide; `raw/adyen/docs/risk-management/chargeback-guidelines/cartes-bancaires-chargebacks/2026-09-15.md:18-24` says code 45 is not defendable and Adyen automatically defends for three specified grounds. The statements concern different provider handling and do not by themselves prove a universal rule for the CB network.
