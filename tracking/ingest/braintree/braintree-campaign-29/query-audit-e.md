# C29 query audit E

Result: **4/4 PASS**. Repository read-only; only this handoff artifact written.

## Answers and verdicts

1. **Checkout UI navigation — PASS.** [[index]] → [[braintree-index]] → [[braintree-web-drop-in]] → [[source-braintree-start-checkout-ui-comparison]] → `raw/braintree/docs/start/checkout-ui-comparison-2026-09-16.md`. Provider index has the source under “Checkout UI and Hosted Fields orientation website guides”; the concept’s Related section supplies the reciprocal route. Raw heading `# Checkout UIs`, line 14.

2. **Checkout UI distinctions — PASS.** Drop-in is ready-made with customization options; Custom UI gives merchant-owned colors/layout (raw lines 16–18, 25). Both columns cover web/native apps; Custom UI routes web to Hosted Fields and native to mobile SDKs (20–24, 33). Both *typically* qualify for SAQ A, with the custom statement conditional on Hosted Fields/mobile SDKs (26), not merchant compliance proof. Drop-in provides up to 23 languages; merchants supply custom translations (27). Both list Basic/Premium Fraud Management Tools (32). Payment-method row/asterisk/mobile-only formatting is flattened (28–31), so do not reconstruct qualifier associations. This 2026-09-16 snapshot identifies selection routes, not present SDK compatibility, account/method eligibility or execution; separately retained lifecycle evidence requires current verification before implementation planning. [[source-braintree-start-checkout-ui-comparison]]

3. **Hosted Fields navigation — PASS.** [[index]] → [[braintree-index]] → [[braintree-web-sdk]] → [[source-braintree-start-hosted-fields]] → `raw/braintree/docs/start/hosted-fields-2026-09-16.md`. Provider orientation section and concept Related section both expose the promoted source. Raw heading `# Hosted Fields`, line 14.

4. **Hosted Fields role/integration — PASS.** JavaScript card-entry for merchant-styled desktop/mobile websites uses custom iframes for certain sensitive fields (16, 19–21), brand styling and card-validity/UI events (29–36). Data goes client→Braintree without raw payment information touching the merchant server; a secure one-time-use nonce substitutes for it (39–45). Integration is server SDK→JavaScript web client→add Hosted Fields; other methods are optional, with separate native-client routes if needed (48–57). The captured native links explicitly route iOS v5/Android v4, while the deeper client reference is JavaScript v3 (57–59); neither makes all unversioned start prose a version-specific support statement. SAQ A eligibility/minimized scope wording (24–26, 45) is not assessed compliance. Drop-in is the separate preformatted option (61); events and nonce are not authorization, settlement or completed payment. [[source-braintree-start-hosted-fields]]

## Route, hashes and gaps

Read full CLAUDE.md, rules/query-and-synthesis.md, root/provider indexes, both relevant concepts, promoted sources and both pinned raws. Raw SHA-256 matches manifest:

- Hosted Fields: `9f359f2bcf54fa3ec89a6cd40703c74cc2809b68bc0dff06566bf4661d9a04cb`
- Checkout UI: `8b4ada4a4d06bcede14a072a29b0dcd447a525661c16cb6f79d759b9cb7b94dd`

Bounded filename sweep covered checkout UI/start Hosted Fields/Hosted Fields overview/setup routes. It found the two pinned pages and Android v5/iOS v7 setup pages; these adjacent setup pages are not needed for the fixed orientation questions and were not treated as evidence. Linked examples, client references and setup guides remain navigation-only here. No blocking evidence gap or promotion request; flattened method qualifiers, current support and merchant PCI/eligibility are explicit answer boundaries, not reconstructed facts. No catalog or raw edits.

analysis_end_utc: 2026-10-02 15:34:38 UTC
