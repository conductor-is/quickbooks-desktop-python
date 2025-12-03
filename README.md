<!-- markdownlint-disable MD033 MD041 -->
<div align="center">
  <a href="https://conductor.is">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/conductor-is/quickbooks-desktop-api/assets/170023/162ee6a9-75ac-41e9-9f1e-2ecc1d88f841">
      <img alt="Conductor logo" src="https://github.com/conductor-is/quickbooks-desktop-api/assets/170023/d67464b8-53a7-4d33-afeb-05a2efde1fa8" width="325">
    </picture>
  </a>
  <h3>QuickBooks Desktop/Enterprise real-time API for Python, Node.js, and REST</h3>
  <a href="https://docs.conductor.is/quickstart">Quickstart</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://conductor.is">Website</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://docs.conductor.is">Docs</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://docs.conductor.is/qbd-api">Examples</a>
  <br />
  <br />
  <a href="https://pypi.org/project/conductor-py"><img src="https://img.shields.io/pypi/dm/conductor-py.svg?logo=pypi" alt="PyPI download count"></a>
  <a href="https://pypi.org/project/conductor-py"><img src="https://img.shields.io/pypi/v/conductor-py.svg?logo=pypi" alt="PyPI version"></a>
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Code coverage">
  <a href="LICENSE"><img src="https://img.shields.io/pypi/l/conductor-py.svg?color=blue&logo=github" alt="License" /></a>
  <hr />
</div>

<!-- prettier-ignore -->
[Conductor](https://conductor.is) is a real-time, fully-typed API for **QuickBooks Desktop** (sometimes called QuickBooks Enterprise). In just a few lines, get real-time access to fetch, create, or update _any_ QuickBooks Desktop object type and receive a fully-typed response.

⭐ **Follow our [Quickstart guide](https://docs.conductor.is/quickstart) to get started.**

The Conductor **Python** library provides convenient access to our QuickBooks Desktop API from any Python 3.9+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

- For Node.js (TypeScript/JavaScript), see [conductor-node](https://github.com/conductor-is/quickbooks-desktop-node).

## Documentation

The REST API documentation can be found on [docs.conductor.is](https://docs.conductor.is/api-ref). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
pip install conductor-py
```

## Key features

- **Any data type**: Query, create, or update any QuickBooks Desktop data type.
- **Real-time**: Get real-time updates on your QuickBooks Desktop data. No queues, no jobs, no cache layer -- just direct access to the data.
- **Modern API**: JSON-based REST API, replacing the old XML-based SOAP model.
- **Typed client libraries**: Fully typed libraries in Node.js and Python with autocomplete, inline docs, and type validation for endpoints, parameters, and responses.
- **Request handling**: Invisibly manages queues, timeouts, retries, and pagination.
- **Auto-pagination**: Automatically handles paginated responses to retrieve complete datasets.
- **Multi-company support**: Connects to multiple QuickBooks Desktop company files.
- **Validation**: Sanitizes and validates all inputs and outputs.
- **Unified error handling**: Streamlines error handling across the QuickBooks stack.
- **Authentication flow UI**: Simple UI for securely connecting QuickBooks Desktop accounts.
- **Dashboard**: UI to monitor and manage your QuickBooks Desktop connections and data.
- **Error resolution**: Detailed guides and instructions for resolving errors and handling edge cases.

## Usage

The full API of this library can be found with code samples at [docs.conductor.is/qbd-api](https://docs.conductor.is/qbd-api).

```python
import os
from conductor import Conductor

conductor = Conductor(
    api_key=os.environ.get("CONDUCTOR_SECRET_KEY"),  # This is the default and can be omitted
)

page = conductor.qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)
print(page.data)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `CONDUCTOR_SECRET_KEY="sk_conductor_..."` to your `.env` file
so that your API Key is not stored in source control.

## Async usage

Simply import `AsyncConductor` instead of `Conductor` and use `await` with each API call:

```python
import os
import asyncio
from conductor import AsyncConductor

conductor = AsyncConductor(
    api_key=os.environ.get("CONDUCTOR_SECRET_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    page = await conductor.qbd.invoices.list(
        conductor_end_user_id="YOUR_END_USER_ID",
    )
    print(page.data)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install conductor-py[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from conductor import DefaultAioHttpClient
from conductor import AsyncConductor


async def main() -> None:
    async with AsyncConductor(
        api_key=os.environ.get("CONDUCTOR_SECRET_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as conductor:
        page = await conductor.qbd.invoices.list(
            conductor_end_user_id="YOUR_END_USER_ID",
        )
        print(page.data)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Pagination

List methods in the Conductor API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
from conductor import Conductor

conductor = Conductor()

all_invoices = []
# Automatically fetches more pages as needed.
for invoice in conductor.qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
):
    # Do something with invoice here
    all_invoices.append(invoice)
print(all_invoices)
```

Or, asynchronously:

```python
import asyncio
from conductor import AsyncConductor

conductor = AsyncConductor()


async def main() -> None:
    all_invoices = []
    # Iterate through items across all pages, issuing requests as needed.
    async for invoice in conductor.qbd.invoices.list(
        conductor_end_user_id="YOUR_END_USER_ID",
    ):
        all_invoices.append(invoice)
    print(all_invoices)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await conductor.qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await conductor.qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)

print(f"next page cursor: {first_page.next_cursor}")  # => "next page cursor: ..."
for invoice in first_page.data:
    print(invoice.id)

# Remove `await` for non-async usage.
```

from datetime import date

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from conductor import Conductor

conductor = Conductor()

bill = conductor.qbd.bills.create(
    transaction_date=date.fromisoformat("2024-10-01"),
    vendor_id="80000001-1234567890",
    conductor_end_user_id="end_usr_1234567abcdefg",
    vendor_address={},
)
print(bill.vendor_address)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `conductor.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `conductor.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `conductor.APIError`.

```python
import conductor
from conductor import Conductor

conductor = Conductor()

try:
    conductor.qbd.invoices.list(
        conductor_end_user_id="YOUR_END_USER_ID",
    )
except conductor.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except conductor.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except conductor.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from conductor import Conductor

# Configure the default for all requests:
conductor = Conductor(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
conductor.with_options(max_retries=5).qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)
```

### Timeouts

By default requests time out after 2 minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from conductor import Conductor

# Configure the default for all requests:
conductor = Conductor(
    # 20 seconds (default is 2 minutes)
    timeout=20.0,
)

# More granular control:
conductor = Conductor(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
conductor.with_options(timeout=5.0).qbd.invoices.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `CONDUCTOR_LOG` to `info`.

```shell
$ export CONDUCTOR_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from conductor import Conductor

conductor = Conductor()
response = conductor.qbd.invoices.with_raw_response.list(
    conductor_end_user_id="YOUR_END_USER_ID",
)
print(response.headers.get('X-My-Header'))

invoice = response.parse()  # get the object that `qbd.invoices.list()` would have returned
print(invoice.id)
```

These methods return an [`APIResponse`](https://github.com/conductor-is/quickbooks-desktop-python/tree/main/src/conductor/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/conductor-is/quickbooks-desktop-python/tree/main/src/conductor/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with conductor.qbd.invoices.with_streaming_response.list(
    conductor_end_user_id="YOUR_END_USER_ID",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `conductor.get`, `conductor.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = conductor.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from conductor import Conductor, DefaultHttpxClient

conductor = Conductor(
    # Or use the `CONDUCTOR_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
conductor.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from conductor import Conductor

with Conductor() as conductor:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/conductor-is/quickbooks-desktop-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import conductor
print(conductor.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
