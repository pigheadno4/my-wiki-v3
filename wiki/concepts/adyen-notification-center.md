---
title: "Adyen Notification Center"
type: concept
category: technology
tags: [adyen, customer-area, notifications, service-status, chargebacks]
---

## Overview

Adyen's Customer Area Notification center presents notices about accessible merchant accounts and Adyen systems. A user can choose notification types and delivery by Email or the in-app center. This 2026-09-15 snapshot describes a user-notice interface, not a complete incident, payment, dispute, or settlement event stream.

## Delivery and scope

The center shows notices for merchant accounts the user account can access. Opening a notice marks it read, which affects its later display in the center but does not resolve the underlying event. Email is sent to the address linked to the user when its toggle is enabled. Chargeback notices also require selecting the merchant accounts whose fraud/dispute notices that user wants. Service-status messages identify the merchant account they apply to and may concern maintenance or downtime; the user may subscribe by email. The source does not state a specific user-role prerequisite or a notification-delivery timing guarantee.

## Sources

- [[source-adyen-docs-account-notification-center]] — 2026-09-15 Customer Area guide to accessible-account notifications, read state, Email/in-app subscriptions, chargeback account selection and service-status messages.
