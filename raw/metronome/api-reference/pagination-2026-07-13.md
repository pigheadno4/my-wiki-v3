<!-- Source URL: https://docs.metronome.com/api-reference/pagination.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Pagination

Calling any list method that returns multiple results, such as `/customers`, may require pagination: multiple calls to fetch all the results. Metronome provides two URL parameters on all list endpoints for this purpose:

* `limit` customizes how many results are returned per page
* `next_page` specifies the cursor to use as a starting point to fetch the next set of results

When a returned response contains a `next_page` value, more records exist than were returned. Include that `next_page` value in a subsequent query to fetch the next set of results. To fetch every result, repeat this process until `next_page` is null.

```bash theme={null}
GET /v1/customers?limit=10
```

```json theme={null}
{
  "data": [
    {
      "id": 1
    },
    {
      "id": 2
    },
    // ...
  ]
  // The next_page cursor that can be passed in the URL
  // to get the next set of results.
  "next_page": "0c34b75b47491b73db66d46737d9a87"
}
```

Given the above response, you can provide the `next_page` cursor with the next request.

```bash theme={null}
GET /v1/customers?limit=10&next_page=0c34b75b47491b73db66d46737d9a87
```

```json theme={null}
{
  "data": [
    {
      "id": 3
    }
  ],
  // If no next_page value is returned, this is the last page of results.
  "next_page": null
}
```

<Tip>
  **BEST PRACTICES FOR LIMIT**

  To make a quick API call to inspect the response format, set `limit=1`. To load many results with as few API calls as possible, set `limit=50`. For performance reasons, `limit` is capped at `100`.
</Tip>
