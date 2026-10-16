# Fixed retrieval checks — Adyen Oracle Simphony

## Q1 — Purpose, scope, and non-inference

**Question:** What Oracle product and payment integration does this page describe, and what should not be inferred from it?

**Expected answer:** It describes Oracle Simphony, a hospitality POS/back-office platform, using OPI to send payment requests to Adyen terminals for Pay at counter or optional Pay at table. It is not a guide to Oracle Xstore retail POS or OPERA hotel PMS. The page gives no specific terminal-model list, exact plugin version, current merchant entitlement, or proof of a live payment, refund, terminal boarding or settlement. The Pay at table steps are a described user flow, not an execution record.

**Raw locators:** Intro lines 15–25; `Supported versions` lines 27–29; `How it works` lines 39–43; `Features` lines 45–64.

**Canonical wiki route:** [[adyen-index]] → [[adyen-oracle-simphony]] → [[source-adyen-docs-plugins-oracle-simphony]] (new Simphony concept/index route proposed for coordinator creation).

## Q2 — Central capability, prerequisites, and warnings

**Question:** What are the stated OPI compatibility and enablement conditions, and how do Pay at counter and Pay at table differ?

**Expected answer:** Adyen says its payment terminals implement OPI 6.2 and its plugin can integrate with a Simphony device compatible with OPI 6.2 and later. First create an Adyen test account, then contact Support to enable OPI in Customer Area. OPI maps a transaction to a terminal list and routes the Simphony request to a specified terminal. Pay at counter is the default: the POS sends billing information to the terminal. Optional Pay at table presents bills on a portable terminal, with print, split and tip steps described. The page does not provide a tested-terminal/model matrix or guarantee that every feature and later OPI revision works for a given installation; approval in the example is not verified merchant payment success.

**Raw locators:** `Supported versions` lines 27–29; `Get started` lines 31–37; `How it works` lines 39–43; `Features` lines 45–64.

**Canonical wiki route:** [[adyen-index]] → [[adyen-oracle-simphony]] → [[source-adyen-docs-plugins-oracle-simphony]] → [[raw/adyen/docs/plugins/oracle-simphony/2026-09-15|pinned raw snapshot]].
