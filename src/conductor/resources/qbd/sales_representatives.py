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
from ...types.qbd import (
    sales_representative_list_params,
    sales_representative_create_params,
    sales_representative_update_params,
)
from ..._base_client import make_request_options
from ...types.qbd.sales_representative import SalesRepresentative
from ...types.qbd.sales_representative_list_response import SalesRepresentativeListResponse

__all__ = ["SalesRepresentativesResource", "AsyncSalesRepresentativesResource"]


class SalesRepresentativesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesRepresentativesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return SalesRepresentativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesRepresentativesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return SalesRepresentativesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        entity_id: str,
        initial: str,
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesRepresentative:
        """
        Creates a sales representative that references an existing employee, vendor, or
        other-name record so it can be assigned on sales forms.

        Args:
          entity_id: The sales representative's corresponding person entity in QuickBooks, stored as
              either an employee, vendor, or other-name entry.

          initial: The initials of this sales representative's name.

              Maximum length: 5 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this sales representative is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-representatives",
            body=maybe_transform(
                {
                    "entity_id": entity_id,
                    "initial": initial,
                    "is_active": is_active,
                },
                sales_representative_create_params.SalesRepresentativeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
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
    ) -> SalesRepresentative:
        """
        Retrieves a sales representative by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales representatives by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales representative to
              retrieve.

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
            f"/quickbooks-desktop/sales-representatives/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        entity_id: str | Omit = omit,
        initial: str | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesRepresentative:
        """
        Updates an existing sales representative.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales representative to update.

          revision_number: The current QuickBooks-assigned revision number of the sales representative
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          entity_id: The sales representative's corresponding person entity in QuickBooks, stored as
              either an employee, vendor, or other-name entry.

          initial: The initials of this sales representative's name.

              Maximum length: 5 characters.

          is_active: Indicates whether this sales representative is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/sales-representatives/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "entity_id": entity_id,
                    "initial": initial,
                    "is_active": is_active,
                },
                sales_representative_update_params.SalesRepresentativeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
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
    ) -> SalesRepresentativeListResponse:
        """Returns a list of sales representatives.

        NOTE: QuickBooks Desktop does not
        support pagination for sales representatives; hence, there is no `cursor`
        parameter. Users typically have few sales representatives.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific sales representatives by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              sales representatives. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all sales representatives
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because sales representatives typically have low record counts.

          name_contains: Filter for sales representatives whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales representatives whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales representatives whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific sales representatives by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for a sales representative.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales representatives whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales representatives whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for sales representatives that are active, inactive, or both.

          updated_after: Filter for sales representatives updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales representatives updated on or before this date/time. Accepts
              the following ISO 8601 formats:

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
            "/quickbooks-desktop/sales-representatives",
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
                    sales_representative_list_params.SalesRepresentativeListParams,
                ),
            ),
            cast_to=SalesRepresentativeListResponse,
        )


class AsyncSalesRepresentativesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesRepresentativesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesRepresentativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesRepresentativesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncSalesRepresentativesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        entity_id: str,
        initial: str,
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesRepresentative:
        """
        Creates a sales representative that references an existing employee, vendor, or
        other-name record so it can be assigned on sales forms.

        Args:
          entity_id: The sales representative's corresponding person entity in QuickBooks, stored as
              either an employee, vendor, or other-name entry.

          initial: The initials of this sales representative's name.

              Maximum length: 5 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this sales representative is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-representatives",
            body=await async_maybe_transform(
                {
                    "entity_id": entity_id,
                    "initial": initial,
                    "is_active": is_active,
                },
                sales_representative_create_params.SalesRepresentativeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
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
    ) -> SalesRepresentative:
        """
        Retrieves a sales representative by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales representatives by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales representative to
              retrieve.

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
            f"/quickbooks-desktop/sales-representatives/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        entity_id: str | Omit = omit,
        initial: str | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesRepresentative:
        """
        Updates an existing sales representative.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales representative to update.

          revision_number: The current QuickBooks-assigned revision number of the sales representative
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          entity_id: The sales representative's corresponding person entity in QuickBooks, stored as
              either an employee, vendor, or other-name entry.

          initial: The initials of this sales representative's name.

              Maximum length: 5 characters.

          is_active: Indicates whether this sales representative is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/sales-representatives/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "entity_id": entity_id,
                    "initial": initial,
                    "is_active": is_active,
                },
                sales_representative_update_params.SalesRepresentativeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesRepresentative,
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
    ) -> SalesRepresentativeListResponse:
        """Returns a list of sales representatives.

        NOTE: QuickBooks Desktop does not
        support pagination for sales representatives; hence, there is no `cursor`
        parameter. Users typically have few sales representatives.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific sales representatives by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              sales representatives. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all sales representatives
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because sales representatives typically have low record counts.

          name_contains: Filter for sales representatives whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales representatives whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales representatives whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific sales representatives by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for a sales representative.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales representatives whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales representatives whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for sales representatives that are active, inactive, or both.

          updated_after: Filter for sales representatives updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales representatives updated on or before this date/time. Accepts
              the following ISO 8601 formats:

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
            "/quickbooks-desktop/sales-representatives",
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
                    sales_representative_list_params.SalesRepresentativeListParams,
                ),
            ),
            cast_to=SalesRepresentativeListResponse,
        )


class SalesRepresentativesResourceWithRawResponse:
    def __init__(self, sales_representatives: SalesRepresentativesResource) -> None:
        self._sales_representatives = sales_representatives

        self.create = to_raw_response_wrapper(
            sales_representatives.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_representatives.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_representatives.update,
        )
        self.list = to_raw_response_wrapper(
            sales_representatives.list,
        )


class AsyncSalesRepresentativesResourceWithRawResponse:
    def __init__(self, sales_representatives: AsyncSalesRepresentativesResource) -> None:
        self._sales_representatives = sales_representatives

        self.create = async_to_raw_response_wrapper(
            sales_representatives.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_representatives.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_representatives.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_representatives.list,
        )


class SalesRepresentativesResourceWithStreamingResponse:
    def __init__(self, sales_representatives: SalesRepresentativesResource) -> None:
        self._sales_representatives = sales_representatives

        self.create = to_streamed_response_wrapper(
            sales_representatives.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_representatives.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_representatives.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_representatives.list,
        )


class AsyncSalesRepresentativesResourceWithStreamingResponse:
    def __init__(self, sales_representatives: AsyncSalesRepresentativesResource) -> None:
        self._sales_representatives = sales_representatives

        self.create = async_to_streamed_response_wrapper(
            sales_representatives.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_representatives.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_representatives.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_representatives.list,
        )
