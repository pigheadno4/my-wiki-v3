---
title: "Adyen for Platforms PCI security questionnaires"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/pci-forms"
raw_files:
  - "adyen/docs/platforms/onboard-users/pci-forms/2026-09-15.md"
tags: [adyen, platforms, onboarding, pci-dss, saq, verification]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms guide describes how platform users sign PCI DSS Self-Assessment Questionnaires (SAQs) before card processing and how a platform using its own onboarding UI can generate, present, sign and retrieve the documents through the Legal Entity Management API. Signing is a user's declaration and documented onboarding step, not independent proof of current PCI compliance, Adyen verification approval, card-processing capability or a payment outcome. [[adyen-platforms]]

## Responsibilities and prerequisites

- The page says **platform users**, because they connect directly with card schemes, must meet PCI DSS requirements for cardholder-data handling and sign an SAQ before processing card payments. Sales channels determine whether one or more SAQs are required. Adyen supplies simplified questionnaires and, when multiple apply, the user signs once. The platform must not treat the signature alone as an audit of the cardholder-data environment.
- The documented flow requires an Adyen for Platforms setup, Legal Entity Management API credentials and a `balancePlatform.accountHolder.updated` webhook subscription. Before beginning, create the main/user legal entity and the individual signer's legal entity, business lines covering supported sales channels, and the user's account holder. The business-line `salesChannels` affect which/how many documents are required. Main organization and individual signer have different legal-entity IDs.
- In hosted onboarding, users sign in Adyen's hosted page; to display questionnaires, add payment methods to the user's store **or** require signing through hosted onboarding settings. For a custom UI, the platform must generate, display and submit questionnaires through the Legal Entity Management API. These are alternative presentation routes, not a single mandatory UI design.

## Custom UI sequence and status boundaries

- Listen to `balancePlatform.accountHolder.updated` and inspect `verificationErrors` to determine whether PCI forms are required. The included **test** example shows `sendToTransferInstrument` with `requested: true`, `enabled: true`, `allowed: false` and `verificationStatus: invalid`, plus an unsigned-forms error; those flags are distinct and the example does not establish another account holder's actual capability.
- Generate simplified templates at `/legalEntities/{id}/pciQuestionnaires/generatePciTemplates` using the **organization** legal-entity ID. English is default, with an optional ISO 639-1 language. `additionalSalesChannels` is optional when stores/payment methods already supply the relevant channels. The response includes base64 content and `pciTemplateReferences`; an **empty** reference array means the user is not required to sign. Decode and present any required forms to the user. The Adyen Document Viewer is an available presentation aid, with npm recommended over the embed option; neither installation choice changes form requirements.
- After the user declares and signs, submit `/legalEntities/{id}/pciQuestionnaires/signPciTemplates` for the **main** legal entity with the individual signer's `signedBy` legal-entity ID and the required `pciTemplateReferences`. The response lists signed SAQ document IDs. The guide then offers list and download endpoints; returned document metadata includes `createdAt` and `validUntil`, and the downloaded content is base64 PDF. Example timestamps, signed IDs and an API response do not establish current validity, acceptance of a particular user, PCI compliance, or card-processing authorization. Check actual account-holder verification/capability status separately.

## Detail locators

- **User PCI responsibility and sales-channel-dependent SAQs:** raw lines 19–25.
- **Platform/credential/webhook/resource prerequisites and hosted vs custom UI:** raw lines 27–45.
- **Webhook verification error and test capability flags:** raw lines 47–99.
- **Template generation, optional language/channels, empty references and viewer:** raw lines 101–359.
- **Signer identity, signing request, returned IDs, list/download and validity metadata:** raw lines 361–636.

## Related

- [[adyen-platforms]]
- [[adyen-pci-dss-compliance]] — broader PCI context

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/pci-forms/2026-09-15|Adyen Platforms PCI forms — collected 2026-09-15]]
