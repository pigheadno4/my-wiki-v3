# Fixed retrieval checks — docs-platforms-automatic-split-configuration-manage-split-configurations-api

Source stem: `source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-api`
Canonical URL: https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations/api
Pinned raw: `raw/adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/api/2026-09-15.md`

## Q1. What does this page cover and what is needed to manage a profile?

Answer: It is the 2026-09-15 Adyen for Platforms Management API guide for listing/getting merchant-account split configuration profiles, adding/removing rules, editing conditions and split logic, updating descriptions, and deleting profiles. It requires the platform-model integration, the Management API SplitConfiguration read-and-write role, and the relevant resource IDs for edits; card-region conditions are a pilot. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-automatic-split-configuration.md` → `wiki/sources/adyen/source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-api.md` → pinned raw lines 15–39, 292–294, 509–511, 2716–2722, 2980–2986, 3275–3279, 3515–3519, 3667–3669.

## Q2. What changes can affect previously authorized payments and what update/deletion cautions matter?

Answer: New rules, changed conditions, and changed split logic are re-evaluated at capture, so they can affect transactions authorized before the change and captured after it. A condition PATCH must include every condition or omitted ones return to defaults; a split-logic PATCH must include all existing instructions or undefined types book to the platform liable account. The only rule cannot be deleted; delete the profile separately. Refund split-ratio logic is disallowed for stores with multiple partial captures. The raw examples are inconsistent on `acquiringFees` spelling and some curl/SDK/response fields, so do not infer identical payloads or exact resulting values from those illustrations. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-automatic-split-configuration.md` → `wiki/sources/adyen/source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-api.md` → pinned raw lines 563–575, 972–977, 2257–2287, 2646–2714, 2749–2769, 2842–2893, 2980–3013, 3113–3183, 3230–3273, 3515–3519.
