<!-- Source URL: https://docs.paypal.ai/growth/payouts/plan -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Plan your integration

Ensure you understand the integration patterns and payout methods available, before using PayPal Payouts to efficiently send payouts to your recipients.

## Choose integration pattern

PayPal Payouts provides three integration patterns to send payouts efficiently. Each integration pattern is designed to meet different business needs based on payout volume, automation requirements, and user's technical capabilities.

### 1. Payouts Web UI file upload

- **What it is**: A manual tool that lets you upload payout files from the PayPal account dashboard.
- **How it works**: You log into your PayPal account, go to the Payouts section, and upload the payouts file. PayPal processes the file and sends payouts.
- **Who should use it**: Best for businesses that send payouts less frequently and do not require automation. This integration pattern works well for businesses with limited technical expertise.
- **Key benefits**: Provides easy access from the PayPal dashboard and requires no technical setup.

### 2. Large-batch file transfer

- **What it is**: A batch processing tool that lets you send payouts by uploading files safely through SFTP (Secure File Transfer Protocol) to PayPal's DropZone.
- **How it works**: You prepare a payout file in the right format and upload it to the DropZone. PayPal processes the file and sends the payouts.
- **Who should use it**: Best for businesses that need to send large-scale payouts and prefer batch processing over real-time API calls. This integration pattern requires some technical skills to set up and manage SFTP.
- **Key benefits**: Handles large numbers of payouts efficiently and keeps file transfers secure.

### 3. Payouts API

- **What it is**: RESTful API that lets you to programmatically send payouts to multiple recipients.
- **How it works**: You integrate PayPal’s Payouts API into your system to automate payouts.
- **Who should use it**: Best for businesses with frequent, high payout volumes that require automation. This integration pattern works well for businesses with developers and technical expertise.
- **Key benefits**: Provides scalability, real-time processing, and full control over payouts.

## Choose payout method

You can send payouts to PayPal accounts and Venmo users. Each Send money section provides information that enables you to integrate the selected integration pattern and send payouts.
