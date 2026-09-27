# Checkout Components 5.0.435 delta review

- Work item: `github-b87716491900a0da3802`.
- Boundary: `@paypal/checkout-components@5.0.434` (`79fa938be54dd364bb251e5b5caa49c7c809030a`) to `@paypal/checkout-components@5.0.435` (`1f668d5ebfba91a6e636f2453aeaba36d65cb5c7`).
- User approved focused reading for this item. Complete cumulative wiki source/changelog, package, new release entry, release/comparison metadata and authored test diff reviewed. Generated code and unchanged history verified mechanically, not semantically reread in full.
- Verified SHA-256 and byte counts of all 213 prior and 214 current capsule files; 211 common files unchanged. Package objects differ only by version. Prior changelog is a byte-identical suffix.
- Compared the complete before/after lines of both `dist/button.js` and `dist/test/button.js` in `diff.patch`. Replacing each distinct `data-v-[0-9a-f]{8}` identifier with an encounter-order token yields exact equality for both bundles. Seven identifiers change consistently. This is not runtime or visual testing.
- Current raw bundle is retained; prior raw capsule omitted it. Upstream diff says modified, despite packet's retained-evidence added classification.
- New test mocks Zoid create and asserts the existing configuration title for no funding source and Venmo. No authored runtime implementation change, dependency-range change, public-export change or new merchant migration established.
- Grounding: raw `CHANGELOG.md:3`, "chore: add test for button iframe title"; raw `package.json:3`, `"version": "5.0.435"`; added test in comparison patch, "uses the plain PayPal label when no funding source is set" and "appends the funding source to the label when one is set".
- Concept audit: update existing PayPal Checkout concept with this maintenance boundary; no new concept or cross-company comparison. Preserve prior accessibility attempts/reverts and monitoring limitations. No new contradiction found.
- No upstream tests, screen-reader/browser checks, or payment flows executed. Separate release notes unavailable. Collection policy unchanged; excluded test content remains in the comparison patch.
