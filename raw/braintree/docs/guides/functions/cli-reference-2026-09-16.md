<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/functions/cli-reference -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: CLI Reference
slug: /docs/guides/functions/cli-reference/
createTime: '2025-04-01T23:01:21.361Z'
updateTime: '2025-04-01T23:01:21.438Z'
---



# CLI Reference


**AVAILABILITY**
We're building functions with the same proven expertise and rock solid foundations you expect from Braintree. Take a look at our documentation preview to get a jump start on what you'll make with functions. Email [functions-requests@braintreepayments.com](mailto:functions-requests@braintreepayments.com) to learn more.


## Installation

Before installing thebraintree-functions-cli, make sure you have[Node.js](https://nodejs.org/en/download/)installed on your machine.
**NOTE**
Version [8.xor10.x](https://nodejs.org/en/download/releases/) is required. We recommend using a tool such as [nvm](https://github.com/creationix/nvm) to manage node versions.

To install the CLI globally, run:
### bash
```bash
$ npm i -g @braintree/functions-cli
```
This will make thebtfnsnamespace available to you from the command line. If you would
prefer to not install this package globally, use the[npx](https://www.npmjs.com/package/npx)command:
### bash
```bash
$ npx btfns <command>
```

### Uninstall

If installed globally:
### bash
```bash
$ npm uninstall -g @braintree/functions-cli
```

## Options

| Option | Description |
| --- | --- |
| -v, --version | show installed version |


## CLI Commands

| Command | Description |
| --- | --- |
| [`deploy`](#deploy) | Deploy your function |
| [`help`](#help) | Display help for btfns |
| [`init`](#init) | Create a new function |
| [`login`](#login) | Login to your Braintree account for deployment and testing |
| [`logout`](#logout) | Log out of your Braintree account |
| [`ls`](#ls) | List functions, events, or triggers |
| [`package`](#package) | Package your function in order to publish to Braintree's function ecosystem |
| [`publish`](#publish) | Publish your function to share with others |
| [`test`](#test) | Simulate function invocation to test your code before deployment |
| [`generate-test-data`](#generate-test-data) | Generate JSON files to mock expected payloads for testing |


## deploy

Deploy your function.
### bash
```bash
$ btfns deploy
```

### deployOptions

| Option | Description |
| --- | --- |
| -h, --help | show command help |
| --production | deploys function to production environment |


## help

Displays commands and version of your installation ofbtfns.
## init

Create a new function.
### bash
```bash
$ btfns init MyFunction --template=dataExport --events=transaction.settled
```

### initOptions

| Option | Description |
| --- | --- |
| -t, --template=templateType | creates configuration and javascript files for type. valid types: `dataExport`, `dataImport`, `paymentMethod` |
| -h, --help | show command help |
| -T, --triggers=trigger | triggers associated to the function, use `btfn ls --triggers` to see all |
| -e, --events=event | events associated to a `dataExport` function, use `btfns ls --events` to see all |


## login

Login to a Braintree account.
### bash
```bash
$ btfns login -e sandbox -m merchantId
```

### loginOptions

| Option | Description |
| --- | --- |
| -e, --environment | set environment |
| -h, --help | show command help |
| -m, --merchant | set merchant ID |
| -u, --user | set username |


## logout

Logout of your Braintree account.
### bash
```bash
$ btfns logout
```

## ls

List functions, events, or triggers.
### bash
```bash
$ btfns ls --functions -e sandbox
```

### lsOptions

| Option | Description |
| --- | --- |
| -h, --help | show command help |
| -e, --environment | set environment |
| --functions | list functions deployed to your account |
| --triggers | list triggers available to be used by a function |
| --events | list events available to be used by a function |


## package

Package and publish your function to share with others.
### bash
```bash
$ btfns package .
```

### packageOptions

| Option | Description |
| --- | --- |
| -h, --help | show command help |


## publish

Package and publish your function to share with others.
### bash
```bash
$ btfns publish . -v 1.0.0
```

### publishOptions

| Option | Description |
| --- | --- |
| -h, --help | show command help |
| -v, --version | sets version of function |


## test

Simulate function invocation to test your code before deployment. Depending on your template type
the appropriate payload will be sent to your function.
### bash
```bash
$ btfns test -p tests/sample.json
```

### testOptions

| Option | Description |
| --- | --- |
| -h, --help | See available options for the `test` command |
| -p, --test-payload | Path to a test `json` file with a pre-build payload |


## generate-test-data

Generate JSON files to mock expected payloads for testing. Running this command will write a JSON
file to the__tests__directory generated by your project.
### bash
```bash
$ btfns generate-test-data -o test/sample.json
```

### generate-test-dataOptions

| Option | Description |
| --- | --- |
| -h, --help | See available options for the `test` command |
| -o, --output | The name and path of the generated file (defaults to `**tests**/.json`) |

