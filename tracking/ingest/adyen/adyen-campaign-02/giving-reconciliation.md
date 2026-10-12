# Narrow Adyen Giving placement reconciliation

The existing `wiki/concepts/adyen-giving.md` is a provider-specific Giving concept, but its only source is the Advanced-flow guide. Its broad title makes the approved Giving overview a necessary retrieval route. The Web v6 upgrade source also changes an important version-specific implementation fact. Keep the existing Advanced-flow paragraph intact and insert the following immediately before `## Sources`:

```markdown
## Web version boundary

The captured Advanced-flow guide lists Web Components v5.0.0 or later and describes a Giving Component. The separate Web v6 upgrade guide says that from v6 onward an Adyen Giving integration must use the Giving Campaign Manager Component. These statements overlap for v6, and the snapshots do not explain how the two Components relate. Treat the Advanced-flow Component steps as guide-scoped and verify the version-specific route before implementation. [[source-adyen-docs-online-payments-donations-integration-options-advanced-flow]] [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]]
```

In that concept's `## Sources`, insert the first bullet before the current Advanced-flow bullet and the second bullet after it:

```markdown
- [[source-adyen-docs-online-payments-donations]] — Giving overview for nonprofit and campaign setup, eligibility, donation options, campaign lifecycle, and terms (webpage snapshot, 2026-09-15).
- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]] — Web v5-to-v6 migration guide; Step 8 requires the Giving Campaign Manager Component from v6 onward (webpage snapshot, 2026-09-15).
```

For the reciprocal overview retrieval backlink, insert this line under `## Related` in the already promoted `wiki/sources/adyen/source-adyen-docs-online-payments-donations.md`, alongside `[[adyen-online-payments]]`:

```markdown
- [[adyen-giving]]
```

Placement: the version boundary belongs in the Giving concept because it qualifies its principal Web Components flow; the two source bullets belong in `## Sources` because they route to the broad Giving overview and the specific v6 change. The overview source's `## Related` backlink gives a reader who enters through the existing `adyen-online-payments` concept a direct path to the new provider concept. The v6 source target is approved but not yet promoted; add its concept link when promoting that source. Evidence: approved overview receipt's source summary and quotes at raw lines 23, 25, 122, 147, and 232; fully read Advanced-flow raw lines 25–37 and 429–453; fully read Web v6 raw lines 464–466. This proposal preserves the unresolved v5-or-later versus v6 wording instead of treating the two Component names as equivalent or asserting that the older route was withdrawn.
