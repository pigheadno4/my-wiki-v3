# Fixed-query probes — Adyen IAM

## Q1 — purpose, scope, and non-inference

**Question:** What does Adyen's IAM page cover, and does it prove an account has secure access controls enabled?

**Answer:** The page is general security guidance for all Adyen integration types. It discusses role-based access control (RBAC), SAML 2.0 single sign-on (SSO), and multifactor authentication (MFA) for application and Customer Area users. Adyen explicitly calls it incomplete, non-definitive advice. Customer Area support for these capabilities does not prove a particular merchant has configured RBAC, SSO, or MFA, that access removal is working, or that its security posture is adequate. This user-access route is separate from [[adyen-api-access|Adyen web service API credential permissions and key lifecycle]]. Read [[source-adyen-docs-development-resources-security-iam]] and [[adyen-customer-area-iam]]; evidence is [[raw/adyen/docs/development-resources/security/iam/2026-09-15|IAM raw snapshot]] lines 15–35 and 37–59.

## Q2 — central capability, prerequisites, and warnings

**Question:** What RBAC, SSO and MFA practices and Customer Area capabilities does the page identify?

**Answer:** It recommends assigning permissions by role/function, limiting access to what is needed, and documenting and regularly reviewing RBAC. The Customer Area supports accounts, roles and user permissions for that arrangement. It supports SSO using **SAML 2.0** and describes removing a departed employee's Customer Area access through an organization's SSO solution as an example. It supports MFA using an **authenticator app or SMS**; the captured page says one method per device and two registered devices per user. These are guidance and supported options, not requirements already enforced by Adyen for every account or evidence of a merchant's configuration. Setup details are routed to the linked account-structure, SSO and MFA pages, not specified here. Read [[source-adyen-docs-development-resources-security-iam]] and [[adyen-customer-area-iam]]; evidence is [[raw/adyen/docs/development-resources/security/iam/2026-09-15|IAM raw snapshot]] lines 37–65.
