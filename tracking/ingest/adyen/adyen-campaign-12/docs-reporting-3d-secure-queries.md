# Fixed retrieval checks — Adyen 3D Secure reporting hub

## Q1 — What is this page for, what is its scope, and what should not be inferred?

The captured page is a navigation hub for Adyen 3D Secure reporting, linking two separately named authentication reports and a conversion report (raw/adyen/docs/reporting/3d-secure/2026-09-15.md:15–32). Its brief purpose statement says their data can help analyze authentication and conversion rates, but gives no row population, field definitions, access roles, time-zone rule, rate formula, or payment outcome. Proposed canonical route: `[[index]]` → `[[adyen-index]]` → `[[adyen-reporting]]` → `[[source-adyen-docs-reporting-3d-secure]]` → `[[raw/adyen/docs/reporting/3d-secure/2026-09-15]]`; canonical URL: https://docs.adyen.com/reporting/3d-secure.

## Q2 — Which reports does it route to, and what qualifications apply?

The hub labels the **3DS Authentication report** link as **Latest version** and says it addresses why 3DS transactions authenticated and authentication performance (raw lines 21–24). It separately links the **3D Secure Authentication report** for why transactions authenticated (lines 26–28) and the **Conversion report** for detailed conversion information (lines 30–32). The latest label is true of this captured snapshot only; the linked reports own their distinct populations, fields, filters and timing. Authentication analysis or a conversion label must not be equated with authorization, capture, settlement or a guaranteed payment outcome. Use the same concept→source→raw route, then the respective report source for details.
