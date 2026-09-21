<!-- Source URL: https://developer.paypal.com/braintree/graphql/integration_guides/uploading_files -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Uploading Files
slug: /graphql/integration_guides/uploading_files/
createTime: '2025-01-16T11:27:07.434Z'
updateTime: '2025-05-01T16:36:49.117Z'
---



# Uploading Files for Mutations

Some of our mutations require merchants to upload files along with their calls to the GraphQL API. Since GraphQL does not natively support file uploads, this involves delivering a payload with a different Content-Type and an attached file. We partially implement the [GraphQL Multipart Request Spec](https://github.com/jaydenseric/graphql-multipart-request-spec), but we only offer support for uploading a single file at a time. Currently, the only mutation that requires this is [createDisputeFileEvidence](/braintree/graphql/reference/#Mutation--createDisputeFileEvidence). If you are uploading a file with this mutation, your mutation will look like this:

### Mutation
```graphql
mutation CreateDisputeFileEvidence($input: CreateDisputeFileEvidenceInput!) {
  createDisputeFileEvidence(input: $input) {
    dispute {
      id
    }
    evidence {
      id
      category
      createdAt
      sentToProcessorAt
      url
    }
  }
}

```

Then you will need to tweak your Content-Type and attach a file along with that mutation when you actually make the request.

This mutation supports files of these types: PNG, JPG, JPEG, and PDF. Files uploaded with this mutation must be 4 MB or less.


### CURL
```bash
curl https://payments.sandbox.braintree-api.com/graphql \
  -H "Braintree-Version: 2021-06-01" \
  -H "Authorization: BASE64_ENCODED(YOUR_PUBLIC_KEY:YOUR_PRIVATE_KEY)" \
  -H "Accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F 'operations={
    "query": "mutation CreateDisputeFileEvidence($input: CreateDisputeFileEvidenceInput!) { createDisputeFileEvidence(input: $input) { evidence { id url } } }",
    "variables": {
      "input": {
        "disputeId": "YOUR_DISPUTE_ID"
      },
      "file": null
    }
  };type=application/json' \
  -F 'map={ "file_to_upload": "variables.file" }' \
  -F 'file_to_upload=@YOUR_IMAGE.png;type=image/jpg'
```
The important things to notice here are:


- The-H "Content-Type: multipart/form-data"header change, instead ofapplication/json. This allows us to upload files to GraphQL.
- The-Fflag with anoperationsobject. Theoperationsname is required. This is where you will pass your GraphQL query and variables, as you would for any other GraphQL API operation. Note that you must specify atypeofapplication/json.
- The"file": nullkey/value pair somewhere in youroperationsJSON object. The path to thisfilekey must be specified in themap(see below).
- The-Fflag with the location of the file to upload on your system, as well as the file type. The file type must be a valid[MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types).
- The-Fflag with amapobject. Themapname is required. This is what links the location of thefilekey in youroperationsJSON (atvariables.filein this example) to the label (file_to_uploadin this example) specifying where the file path and type are specified.

The Braintree-Version and Authorization headers are the same as a standard GraphQL request.

The response to this mutation will be structured identically to any other GraphQL API response.

