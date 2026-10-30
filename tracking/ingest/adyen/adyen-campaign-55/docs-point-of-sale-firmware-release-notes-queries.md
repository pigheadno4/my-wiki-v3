# Q1 — Which terminal software versions does this captured release note recommend for manual-update fleets, and what is the Engage boundary?

Source stem: `source-adyen-docs-point-of-sale-firmware-release-notes`
Canonical URL: https://docs.adyen.com/point-of-sale/firmware-release-notes

The 2026-09-15 snapshot's introduction names Android LTS v1.133, v1.130, or v1.126 and Verifone Engage v1.120 for manual-update terminals. Its dated entries qualify that list: v1.126 patch maintenance ended 15 June 2026, before this capture; v1.130 says maintenance until September 2026; v1.133 says until the end of February 2027. Consult the specific release entry and update strategy before selecting a maintained version. The page says 1.120 is the last *major* Engage release because of the PCI PTS 6 transition, while the 1.120 entry says patch maintenance continues until 2030 and that downgrading Engage from 1.120.17 to an earlier patch is impossible. This is release guidance; it does not show a specific terminal's installed version or rollout status. Locators: pinned raw lines 20–35, 139–145, 293–295, 594–596, 1019–1023, 1133–1179. Full raw: `raw/adyen/docs/point-of-sale/firmware-release-notes/2026-09-15.md`.

# Q2 — Can version 1.127 be deployed to S1U2, and did its listed app-unassignment issue persist in the LTS line?

Source stem: `source-adyen-docs-point-of-sale-firmware-release-notes`
Canonical URL: https://docs.adyen.com/point-of-sale/firmware-release-notes

No: the 1.127 entry explicitly says it is unavailable for S1U2 and lists Adyen application unassignment after updating on some terminals. The 1.126 LTS entry separately says patches 1.126.3–1.126.5 are unavailable for S1U2 and lists app unassignment on some terminals after those patches; its 1.126.6 fix says that issue was fixed. These are version/model-qualified release notes, not a claim that a specific device was updated or repaired. Locators: pinned raw lines 558–572 and 594–665. Full raw: `raw/adyen/docs/point-of-sale/firmware-release-notes/2026-09-15.md`.
