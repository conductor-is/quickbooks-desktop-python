# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import currency_list_params, currency_create_params, currency_update_params
from ..._base_client import make_request_options
from ...types.qbd.currency import Currency
from ...types.qbd.currency_list_response import CurrencyListResponse

__all__ = ["CurrenciesResource", "AsyncCurrenciesResource"]


class CurrenciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return CurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return CurrenciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency_code: str,
        name: str,
        conductor_end_user_id: str,
        currency_format: currency_create_params.CurrencyFormat | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """
        Creates a user-defined currency with the specified name and currency code.
        Exchange rates for user-defined currencies are not updated automatically by
        QuickBooks Desktop; update them manually as needed.

        Args:
          currency_code: The internationally accepted currency code used by this currency, typically
              based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
              QuickBooks currencies follow ISO 4217. For user-defined currencies, following
              ISO 4217 is recommended but not required. In many cases, the three-letter code
              is formed from the country's two-letter internet code plus a currency letter
              (e.g., BZ + D → BZD for Belize Dollar).

              Maximum length: 3 characters.

          name: The case-insensitive unique name of this currency, unique across all currencies.
              For built-in currencies, the name is the internationally accepted currency name
              and is not editable.

              **NOTE**: Currencies do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 64 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_format: Controls how this currency displays thousands separators, grouping, and decimal
              places.

          is_active: Indicates whether this currency is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/currencies",
            body=maybe_transform(
                {
                    "currency_code": currency_code,
                    "name": name,
                    "currency_format": currency_format,
                    "is_active": is_active,
                },
                currency_create_params.CurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """
        Retrieves a currency by ID.

        **IMPORTANT:** If you need to fetch multiple specific currencies by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the currency to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/currencies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        currency_code: str | Omit = omit,
        currency_format: currency_update_params.CurrencyFormat | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """Updates an existing currency.

        For built-in currencies, only the `isActive`
        status can be changed; name and currency code are not editable. For user-defined
        currencies, all fields in this request are editable.

        Args:
          id: The QuickBooks-assigned unique identifier of the currency to update.

          revision_number: The current QuickBooks-assigned revision number of the currency object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_code: The internationally accepted currency code used by this currency, typically
              based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
              QuickBooks currencies follow ISO 4217. For user-defined currencies, following
              ISO 4217 is recommended but not required. In many cases, the three-letter code
              is formed from the country's two-letter internet code plus a currency letter
              (e.g., BZ + D → BZD for Belize Dollar).

              Maximum length: 3 characters.

          currency_format: Controls how this currency displays thousands separators, grouping, and decimal
              places.

          is_active: Indicates whether this currency is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this currency, unique across all currencies.
              For built-in currencies, the name is the internationally accepted currency name
              and is not editable.

              **NOTE**: Currencies do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 64 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/currencies/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "currency_code": currency_code,
                    "currency_format": currency_format,
                    "is_active": is_active,
                    "name": name,
                },
                currency_update_params.CurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListResponse:
        """Returns a list of currencies.

        NOTE: QuickBooks Desktop does not support
        pagination for currencies; hence, there is no `cursor` parameter. Users
        typically have few currencies.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific currencies by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              currencies. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all currencies without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because currencies typically have low record counts.

          name_contains: Filter for currencies whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for currencies whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for currencies whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific currencies by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a currency.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for currencies whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for currencies whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for currencies that are active, inactive, or both.

          updated_after: Filter for currencies updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for currencies updated on or before this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/currencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )


class AsyncCurrenciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncCurrenciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency_code: str,
        name: str,
        conductor_end_user_id: str,
        currency_format: currency_create_params.CurrencyFormat | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """
        Creates a user-defined currency with the specified name and currency code.
        Exchange rates for user-defined currencies are not updated automatically by
        QuickBooks Desktop; update them manually as needed.

        Args:
          currency_code: The internationally accepted currency code used by this currency, typically
              based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
              QuickBooks currencies follow ISO 4217. For user-defined currencies, following
              ISO 4217 is recommended but not required. In many cases, the three-letter code
              is formed from the country's two-letter internet code plus a currency letter
              (e.g., BZ + D → BZD for Belize Dollar).

              Maximum length: 3 characters.

          name: The case-insensitive unique name of this currency, unique across all currencies.
              For built-in currencies, the name is the internationally accepted currency name
              and is not editable.

              **NOTE**: Currencies do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 64 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_format: Controls how this currency displays thousands separators, grouping, and decimal
              places.

          is_active: Indicates whether this currency is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/currencies",
            body=await async_maybe_transform(
                {
                    "currency_code": currency_code,
                    "name": name,
                    "currency_format": currency_format,
                    "is_active": is_active,
                },
                currency_create_params.CurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    async def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """
        Retrieves a currency by ID.

        **IMPORTANT:** If you need to fetch multiple specific currencies by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the currency to retrieve.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/currencies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        currency_code: str | Omit = omit,
        currency_format: currency_update_params.CurrencyFormat | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Currency:
        """Updates an existing currency.

        For built-in currencies, only the `isActive`
        status can be changed; name and currency code are not editable. For user-defined
        currencies, all fields in this request are editable.

        Args:
          id: The QuickBooks-assigned unique identifier of the currency to update.

          revision_number: The current QuickBooks-assigned revision number of the currency object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_code: The internationally accepted currency code used by this currency, typically
              based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
              QuickBooks currencies follow ISO 4217. For user-defined currencies, following
              ISO 4217 is recommended but not required. In many cases, the three-letter code
              is formed from the country's two-letter internet code plus a currency letter
              (e.g., BZ + D → BZD for Belize Dollar).

              Maximum length: 3 characters.

          currency_format: Controls how this currency displays thousands separators, grouping, and decimal
              places.

          is_active: Indicates whether this currency is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this currency, unique across all currencies.
              For built-in currencies, the name is the internationally accepted currency name
              and is not editable.

              **NOTE**: Currencies do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 64 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/currencies/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "currency_code": currency_code,
                    "currency_format": currency_format,
                    "is_active": is_active,
                    "name": name,
                },
                currency_update_params.CurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Currency,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListResponse:
        """Returns a list of currencies.

        NOTE: QuickBooks Desktop does not support
        pagination for currencies; hence, there is no `cursor` parameter. Users
        typically have few currencies.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific currencies by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              currencies. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all currencies without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because currencies typically have low record counts.

          name_contains: Filter for currencies whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for currencies whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for currencies whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific currencies by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a currency.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for currencies whose `name` starts with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for currencies whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for currencies that are active, inactive, or both.

          updated_after: Filter for currencies updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for currencies updated on or before this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/currencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )


class CurrenciesResourceWithRawResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.create = to_raw_response_wrapper(
            currencies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            currencies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            currencies.update,
        )
        self.list = to_raw_response_wrapper(
            currencies.list,
        )


class AsyncCurrenciesResourceWithRawResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.create = async_to_raw_response_wrapper(
            currencies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            currencies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            currencies.update,
        )
        self.list = async_to_raw_response_wrapper(
            currencies.list,
        )


class CurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.create = to_streamed_response_wrapper(
            currencies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            currencies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            currencies.update,
        )
        self.list = to_streamed_response_wrapper(
            currencies.list,
        )


class AsyncCurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.create = async_to_streamed_response_wrapper(
            currencies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            currencies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            currencies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            currencies.list,
        )
