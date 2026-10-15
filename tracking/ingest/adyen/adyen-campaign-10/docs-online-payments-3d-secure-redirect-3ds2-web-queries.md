# Fixed retrieval checks: Redirect 3D Secure for Web chooser

## Q1 — Purpose and available routes

**Query:** What integration choices does this Adyen Redirect 3D Secure for Web page offer?

**Expected answer:** It is a short navigation page for supporting card 3D Secure authentication through a redirect on a website. It links to Web Drop-in, described as Adyen's all-in-one UI solution, and Web Components, described as pre-built Components. The page was modified in 2019 and captured on 2026-09-15. Follow the separately retained child guides for implementation details.

**Raw locators:** title, description and metadata, lines 6–17; integration chooser and child links, lines 19–27. **Canonical retrieval route:** [[adyen-3d-secure]] → [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web]] → [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web/2026-09-15|pinned raw]].

## Q2 — Evidence boundary

**Query:** Does this chooser specify Web SDK or Checkout API versions, endpoint calls, prerequisites, authentication steps, liability shift or payment outcomes?

**Expected answer:** No. The page supplies only the redirect-Web purpose and the Drop-in/Components choice. It does not document version requirements, API request sequence, return handling, shopper authentication result, authorization, capture or liability shift. The linked child implementation guides are separate evidence and must be read for those claims; a navigation label alone does not establish their behavior.

**Raw locators:** complete page, lines 15–27. **Canonical retrieval route:** [[adyen-3d-secure]] → [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web]] → [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web/2026-09-15|pinned raw]].
