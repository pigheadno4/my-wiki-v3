<!-- Source URL: https://docs.stripe.com/api/terminal/configuration/list -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# List all Configurations

Returns a list of `Configuration` objects.

## Request

```curl
curl -G https://api.stripe.com/v1/terminal/configurations \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/configurations",
  "has_more": false,
  "data": [
    {
      "id": "tmc_FQqbaQCiy0m1xc",
      "object": "terminal.configuration",
      "is_account_default": false,
      "livemode": false
    }
  ]
}
```

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `is_account_default` (boolean, optional)
  if present, only return the account default or non-default configurations.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` configurations, starting after configurations `configurations`. Each entry in the array is a separate Terminal `configurations` object. If no more configurations are available, the resulting array will be empty.
