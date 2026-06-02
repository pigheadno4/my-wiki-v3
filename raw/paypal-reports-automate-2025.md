<!-- Source URL: https://docs.paypal.ai/grow/reports-analytics/manage-automate -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage and automate reports

PayPal offers several options to automate and schedule the generation and delivery of reports, helping you streamline reconciliation, compliance, and business intelligence processes.

Automate your reporting workflows using PayPal's scheduling APIs, SFTP delivery, and webhook integrations to ensure consistent, timely access to your business data.

## Getting started

### Prerequisites

- PayPal Business account with API access
- Understanding of your reporting schedule needs
- Technical capability for automation setup
- Secure storage for automated reports

### Scheduling options

#### Payflow reporting API scheduling

The [Transaction Search API](https://developer.paypal.com/docs/api/transaction-search/v1/) allows you to programmatically retrieve transaction history for a PayPal account. You can use this API to get transaction data with various query parameters and filters.

It takes a maximum of three hours for executed transactions to appear in the API calls, and it provides transaction data for the previous three years.

```javascript theme={null}
// Create scheduled report template
const createScheduledReport = async (templateData) => {
  const response = await fetch("/v1/reporting/templates/schedule", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      template_id: templateData.template_id,
      schedule_type: "DAILY", // WEEKLY, MONTHLY
      delivery_method: "SFTP",
      start_date: "2024-01-01",
      frequency: 1,
    }),
  });

  return await response.json();
};
```

#### SFTP automation setup

PayPal offers [SFTP access](https://developer.paypal.com/docs/reports/sftp-reports/) for secure retrieval of reports that are updated daily. Reports like the Transaction Detail Report are generated and placed on SFTP on a 24-hour basis in CSV format. The Transaction Detail Report is generated and put on PayPal's website and the Secure Dropbox by no later than 12:00PM daily.

##### Steps for SFTP configuration

1. **Request SFTP access**
   - Contact PayPal support for SFTP credentials
   - Provide security requirements and IP restrictions
   - Configure firewall and access controls

2. **Set Up automated retrieval**
   - Schedule daily report downloads
   - Reports available by 12 PM in leading time zone
   - Implement secure file transfer protocols

3. **Process retrieved files**
   - Automate file parsing and validation
   - Integrate with your business systems
   - Archive processed reports securely

##### Sample SFTP integration

```javascript theme={null}
// SFTP file retrieval automation
const downloadDailyReports = async () => {
  const sftp = new SFTP();

  try {
    await sftp.connect(sftpConfig);
    const files = await sftp.list("/reports/daily");

    for (const file of files) {
      if (isNewReport(file)) {
        await sftp.get(file.name, `./downloads/${file.name}`);
        await processReport(file.name);
      }
    }
  } finally {
    await sftp.end();
  }
};
```

#### Webhook automation

PayPal's REST APIs use webhooks for event notification, which are HTTP callbacks that receive notification messages for events. You can subscribe webhook listeners to events and automate responses when transactions occur. You can use webhooks for reporting by collecting information from webhook notifications to create reports based on different triggers, such as subscription cancellations.

##### Webhook setup for reporting

1. **Configure webhook endpoints**
   - Set up secure HTTPS endpoints
   - Implement signature verification
   - Handle event processing logic

2. **Event-driven report generation**
   - Trigger reports based on specific events
   - Process transaction completion webhooks
   - Generate custom reports on demand

##### Webhook processing example

````javascript theme={null}
// Webhook-triggered report generation
app.post('/webhook/transaction-complete', async (req, res) => {
  const event = req.body;

  if (event.event_type === 'PAYMENT.CAPTURE.COMPLETED') {
    await generateTransactionReport(event.resource.id);
  }

  res.status(200).send('OK');
});

### Management operations

#### Update scheduled reports

```javascript
// Modify existing schedule
const updateSchedule = async (scheduleId, updates) => {
  return await fetch(`/v1/reporting/schedules/${scheduleId}`, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(updates)
  });
};
````

#### Delete report schedules

```javascript theme={null}
// Remove scheduled report
const deleteSchedule = async (scheduleId) => {
  return await fetch(`/v1/reporting/schedules/${scheduleId}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
};
```

## Best practices

- Monitor automation health regularly
- Implement failure notifications
- Maintain backup scheduling methods
- Secure all automated processes
- Test schedule changes in sandbox first
