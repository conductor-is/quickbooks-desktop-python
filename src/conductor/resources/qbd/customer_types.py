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
from ...types.qbd import customer_type_list_params, customer_type_create_params
from ..._base_client import make_request_options
from ...types.qbd.customer_type import CustomerType
from ...types.qbd.customer_type_list_response import CustomerTypeListResponse

__all__ = ["CustomerTypesResource", "AsyncCustomerTypesResource"]


class CustomerTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return CustomerTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return CustomerTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerType:
        """
        Creates a new customer type.

        Args:
          name: The case-insensitive name of this customer type. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two customer types could both have the `name`
              "Healthcare", but they could have unique `fullName` values, such as
              "Industry:Healthcare" and "Region:Healthcare".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this customer type is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent customer type one level above this one in the hierarchy. For example,
              if this customer type has a `fullName` of "Industry:Healthcare", its parent has
              a `fullName` of "Industry". If this customer type is at the top level, this
              field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/customer-types",
            body=maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                customer_type_create_params.CustomerTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerType,
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
    ) -> CustomerType:
        """
        Retrieves a customer type by ID.

        **IMPORTANT:** If you need to fetch multiple specific customer types by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer type to retrieve.

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
            f"/quickbooks-desktop/customer-types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerType,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
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
    ) -> CustomerTypeListResponse:
        """Returns a list of customer types.

        NOTE: QuickBooks Desktop does not support
        pagination for customer types; hence, there is no `cursor` parameter. Users
        typically have few customer types.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          full_names: Filter for specific customer types by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a customer type, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a customer type is under "Industry" and has the `name`
              "Healthcare", its `fullName` would be "Industry:Healthcare".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific customer types by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              customer types. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all customer types without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because customer types typically have low record counts.

          name_contains: Filter for customer types whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for customer types whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for customer types whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for customer types whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for customer types whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for customer types that are active, inactive, or both.

          updated_after: Filter for customer types updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for customer types updated on or before this date/time. Accepts the
              following ISO 8601 formats:

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
            "/quickbooks-desktop/customer-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    customer_type_list_params.CustomerTypeListParams,
                ),
            ),
            cast_to=CustomerTypeListResponse,
        )


class AsyncCustomerTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncCustomerTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerType:
        """
        Creates a new customer type.

        Args:
          name: The case-insensitive name of this customer type. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two customer types could both have the `name`
              "Healthcare", but they could have unique `fullName` values, such as
              "Industry:Healthcare" and "Region:Healthcare".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this customer type is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent customer type one level above this one in the hierarchy. For example,
              if this customer type has a `fullName` of "Industry:Healthcare", its parent has
              a `fullName` of "Industry". If this customer type is at the top level, this
              field will be `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/customer-types",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                customer_type_create_params.CustomerTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerType,
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
    ) -> CustomerType:
        """
        Retrieves a customer type by ID.

        **IMPORTANT:** If you need to fetch multiple specific customer types by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer type to retrieve.

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
            f"/quickbooks-desktop/customer-types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerType,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        full_names: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
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
    ) -> CustomerTypeListResponse:
        """Returns a list of customer types.

        NOTE: QuickBooks Desktop does not support
        pagination for customer types; hence, there is no `cursor` parameter. Users
        typically have few customer types.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          full_names: Filter for specific customer types by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a customer type, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a customer type is under "Industry" and has the `name`
              "Healthcare", its `fullName` would be "Industry:Healthcare".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific customer types by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              customer types. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all customer types without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because customer types typically have low record counts.

          name_contains: Filter for customer types whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for customer types whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for customer types whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for customer types whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for customer types whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for customer types that are active, inactive, or both.

          updated_after: Filter for customer types updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for customer types updated on or before this date/time. Accepts the
              following ISO 8601 formats:

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
            "/quickbooks-desktop/customer-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    customer_type_list_params.CustomerTypeListParams,
                ),
            ),
            cast_to=CustomerTypeListResponse,
        )


class CustomerTypesResourceWithRawResponse:
    def __init__(self, customer_types: CustomerTypesResource) -> None:
        self._customer_types = customer_types

        self.create = to_raw_response_wrapper(
            customer_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customer_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            customer_types.list,
        )


class AsyncCustomerTypesResourceWithRawResponse:
    def __init__(self, customer_types: AsyncCustomerTypesResource) -> None:
        self._customer_types = customer_types

        self.create = async_to_raw_response_wrapper(
            customer_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customer_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            customer_types.list,
        )


class CustomerTypesResourceWithStreamingResponse:
    def __init__(self, customer_types: CustomerTypesResource) -> None:
        self._customer_types = customer_types

        self.create = to_streamed_response_wrapper(
            customer_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customer_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            customer_types.list,
        )


class AsyncCustomerTypesResourceWithStreamingResponse:
    def __init__(self, customer_types: AsyncCustomerTypesResource) -> None:
        self._customer_types = customer_types

        self.create = async_to_streamed_response_wrapper(
            customer_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customer_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            customer_types.list,
        )
