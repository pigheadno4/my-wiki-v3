---
title: "GitHub changelog: Adyen/adyen-web"
type: source
date_ingested: 2026-07-26
original_format: github-repo
raw_files:
  - "github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json"
tags: [adyen, checkout, web-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-web`. Cumulative implementation knowledge belongs in [[source-github-adyen-web]] and the linked immutable snapshots.

## `@adyen/adyen-web@6.41.0` (2026-07-16)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | Initial baseline | `6.41.0` | `b19eec7054340a1526c87d450fd7dfff75794ed9` | Full |

**Important findings:** The release propagates `healthcare` through `onBinLookup`, detects a missing valid domain in a 3DS2 challenge notification URL, replaces deprecated `keypress` handling, removes explicit `any` types in several Components, hides component-level installments in Sessions, and restores Drop-in `aria-checked` state when the first method remains closed.

**Developer or merchant impact:** Define installments when creating the Session, not on the Card Component, for Sessions integrations. Invalid 3DS2 challenge notification domains now fail before an unfinishable challenge is rendered. Drop-in integrations using `openFirstPaymentMethod=false` gain corrected assistive state.

**Migration action:** Review any Sessions integration that supplies Card installments locally and move that configuration to Session creation. No other breaking migration is documented for this patch.

**Updated source sections:** Sessions and advanced flow; Card behavior; 3D Secure 2 and action safety; accessibility; Adyen company summary; co-badged-cards implementation evidence.

**Evidence boundary:** This is the first retained Adyen Web baseline, so no prior exact-SHA comparison exists. Patch findings come from upstream release notes and the complete retained source capsule; broader source-page findings describe accumulated `6.41.0` behavior.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`
- Card session guard: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/Card.tsx`
- 3DS2 challenge validation: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx`
- Drop-in payment-method item: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Dropin/components/PaymentMethod/PaymentMethodItem/PaymentMethodItem.tsx`
