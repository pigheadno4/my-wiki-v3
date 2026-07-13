<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/billable-metrics-basic-filters.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create streaming billable metrics

export const List = ({marker, children}) => {
  return <>
            <style>
                {`
          .custom-list-from-snippet li {
            list-style-type: var(--marker-style);
            
            padding-left: 0 !important;

          }
          .custom-list-from-snippet li::marker {
            color: rgb(var(--gray-600));

          }
          .custom-list-from-snippet li::before {
            display: none;
          }
        `}
            </style>

            <ul className="custom-list-from-snippet" style={{
    '--marker-style': marker,
    'padding-inline-start': '1.5rem'
  }}>
                {children}
            </ul>
        </>;
};

The streaming`Basic Filters` editor is a structured query builder designed to provide out-of-the-box filters and aggregations on your usage stream. All metrics defined with the Basic Filters editor are created as streaming billable metrics.

Billable metrics can be created in both the [Metronome app](https://app.metronome.com/) or using the [Metronome API](/api-reference/billable-metrics/create-a-billable-metric).

For this example, create a metric to track "API Calls" for a hypothetical cloud service.

1. Navigate to the Billable Metrics section in Metronome.
2. Click `+ Add new Billable Metric`.
3. Choose `Basic filters`.
4. Name your metric (for example, `API Calls`).
5. Select the event type (for example, `api_request`).
6. Set filters:

   <List marker="lower-roman">
     * **Property 1**
         <List marker="disc">
           * `property_name`: "status"
           * `operator`: "In"
           * `value`: "success" (This ensures Metronome only counts successful API calls.)
         </List>
     * **Property 2**
         <List marker="disc">
           * `property_name`: "user\_id"
           * `operator`: "Exists"
           * (Metronome uses this as a group key to display API calls broken out by user.)
         </List>
   </List>
7. Choose the aggregation method:

   * To count the number of API calls, not sum or average them, select "Count".

   Streaming billable metrics support four aggregation types: `COUNT`, `SUM`, `MAX`, and `LATEST`. For other aggregation types, such as `UNIQUE`, use a [SQL billable metric](/guides/implement-metronome/core-concepts/billable-metrics-sql-editor).
8. Set a group key for `user_id`.
9. Review and save your metric.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/84OZCN1rCXvkxNrS/images/docs/get-started/core-concepts/billable-metrics/create_streaming_bm.png?fit=max&auto=format&n=84OZCN1rCXvkxNrS&q=85&s=08d9f7fe44e841095ecb7558c00527df" alt="Billable metric creation flow" width="1459" height="1090" data-path="images/docs/get-started/core-concepts/billable-metrics/create_streaming_bm.png" />
</Frame>

This billable metric counts all successful API calls broken out by `user_id`, providing a simple but effective measure of platform usage across an organization.

Prefer using the API? Here is an example request to set up the same metric:

```bash theme={null}
curl -X POST https://api.metronome.com/v1/billable-metrics/create \
 -H "Authorization: Bearer <TOKEN>" \
 -H "Content-Type: application/json" \
 -d '{
    "name":"API Calls",
    "event_type_filter": {
      "in_values": ["api_request"]
    },
    "property_filters": [
      {
        "name": "status",
        "exists": true,
        "in_values": ["success"]
      },
      {
        "name": "user_id",
        "exists": true
      }
    ],
    "aggregation_type": "COUNT",
    "group_keys": [["user_id"]]
  }'
```
