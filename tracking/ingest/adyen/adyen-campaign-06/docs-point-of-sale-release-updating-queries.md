# Fixed retrieval answers — docs-point-of-sale-release-updating

## 1. Who controls terminal software updates, and what must happen for a scheduled update to install?

**Purpose and scope:** The 2026-09-15 Adyen Docs snapshot covers software on Adyen payment terminals used with Terminal API integrations or standalone solutions. It is a policy and operating-condition source, not a terminal inventory or a POS SDK release ledger.

**Capability:** Adyen describes gradual, monitored automatic monthly rollout as its default. Manual rollout is exceptional, requires Adyen approval, and is limited to LTS terminal software; merchants request it in Customer Area at least two business days ahead. Adyen says it does not actively monitor manually updated terminals.

**Prerequisites and warnings:** A terminal installs after reboot at its configurable restart hour, default 6:00 AM local time. It must have been powered on and network-connected for at least one maintenance interval before that hour, default 180 minutes. Failed installation leaves the previous software in use. A submitted manual request or scheduled window does not establish that a particular terminal updated.

**Retrieval route:** [[adyen-terminal-management]] → [[source-adyen-docs-point-of-sale-release-updating]] → `Manual updating` and `Update to a new release` in [[raw/adyen/docs/point-of-sale/release-updating/2026-09-15|pinned raw]]. Provider catalog entry is pending coordinator promotion.

## 2. Which LTS versions can a merchant manually choose, and does this page prove a current supported release or beta state?

**Purpose and scope:** This is a dated description of terminal software maintenance and beta release process, not a live device/version status check.

**Capability:** The page says terminals on the approved manual strategy can update to any of the three latest LTS versions, while Adyen fixes newly found issues only in the latest LTS version. It describes LTS maintenance as typically about four to five months. Beta terminals receive a new release near the start of automatic rollout; Adyen handles setup and monitoring, with enrollment through an Adyen contact.

**Prerequisites and warnings:** The page's 1.126/1.130/1.133 dates are planned and explicitly subject to change. It does not establish which releases are currently supported or which devices have updated. Beta merchants are expected to keep terminals active, brief staff and report issues; Adyen's mitigation steps do not guarantee no disruption. Check current terminal release notes and account/device state for a present decision.

**Retrieval route:** [[adyen-terminal-management]] → [[source-adyen-docs-point-of-sale-release-updating]] → `Long Term Support version` and `Beta testing` in [[raw/adyen/docs/point-of-sale/release-updating/2026-09-15|pinned raw]]. Provider catalog entry is pending coordinator promotion.
