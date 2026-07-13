<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/audit-logs.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit logs

The Metronome audit log tracks actions taken anywhere in the Metronome system (such as the [Metronome app](https://app.metronome.com/) or API). The log records metadata around that action, including who took it, when it occurred, and how the system responded to the action. This provides increased transparency and security, as users can monitor activity and identify any unauthorized actions or determine who made a change.

For each action taken, the log provides these details:

* the timestamp when the action was taken
* which user or API token took the action
* what resource was acted upon (for example, a customer with ID 123)
* what action was taken (for example, `add_plan`)
* whether the action was successful

You can access the Metronome audit log via the [/auditLogs](/api-reference/security/get-audit-logs) endpoint.

Example records from the audit log:

```json theme={null}
[  
  {  
    "id": "4a893288-336f-4216-9f39-84362e4d20b0",  
    "timestamp": "2023-04-32T18:31:55:00Z",  
    "actor": {  
      "id": "04b6506e-cb3c-43d4-912a-e9af03ad0f5b",  
      "name": "Developer API token"  
    },  
    "resource_type": "customer",  
    "resource_id": "aa02b4b9-adde-414a-b303-5078fc4d23fc",  
    "action": "add_plan",  
    "request_id": "71f232b6-a236-466d-b89b-f9bn0b90940b",  
    "status": "success"  
  },  
  {  
    "id": "f627572d-c5f1-4ba8-b227-093a901e787d",  
    "timestamp": "2023-04-32T20:25:15:00Z",  
    "actor": {  
      "id": "b80922a0-f611-4bf9-8cb9-a47ce377826c",  
      "name": "John Smith",  
      "email": "john@example.com"  
    },  
    "resource_type": "customer",  
    "resource_id": "aa02b4b9-adde-414a-b303-5078fc4d23fc",  
    "action": "change_name",  
    "request_id": "99b4556d-1c82-435a-b6c6-ce239de22fe6",  
    "status": "success"  
  }  
]
```
