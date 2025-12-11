# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.qbd import unit_of_measure_set_list_params, unit_of_measure_set_create_params
from ..._base_client import make_request_options
from ...types.qbd.unit_of_measure_set import UnitOfMeasureSet
from ...types.qbd.unit_of_measure_set_list_response import UnitOfMeasureSetListResponse

__all__ = ["UnitOfMeasureSetsResource", "AsyncUnitOfMeasureSetsResource"]


class UnitOfMeasureSetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnitOfMeasureSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return UnitOfMeasureSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnitOfMeasureSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return UnitOfMeasureSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        base_unit: unit_of_measure_set_create_params.BaseUnit,
        name: str,
        unit_of_measure_type: Literal["area", "count", "length", "other", "time", "volume", "weight"],
        conductor_end_user_id: str,
        default_units: Iterable[unit_of_measure_set_create_params.DefaultUnit] | Omit = omit,
        is_active: bool | Omit = omit,
        related_units: Iterable[unit_of_measure_set_create_params.RelatedUnit] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitOfMeasureSet:
        """
        Creates a new unit-of-measure set.

        NOTE: The QuickBooks company file must have unit-of-measure enabled (either a
        single unit per item or multiple units per item). To support both
        configurations, prefix all UOM set names with "By the" (for example, "By the
        Barrel"); otherwise, the set may not appear in the QuickBooks UI when the
        company file is configured for a single unit per item.

        Args:
          base_unit: The unit-of-measure set's base unit used to track and price item quantities. If
              the company file is enabled for a single unit of measure per item, the base unit
              is the only unit available on transaction line items. If enabled for multiple
              units per item, the base unit is the default unless overridden by the set's
              default units.

          name: The case-insensitive unique name of this unit-of-measure set, unique across all
              unit-of-measure sets. To ensure this set appears in the QuickBooks UI for
              companies configured with a single unit per item, prefix the name with "By the"
              (e.g., "By the Barrel").

              **NOTE**: Unit-of-measure sets do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          unit_of_measure_type: The unit-of-measure set's type. Use "other" for a custom type defined in
              QuickBooks.

          conductor_end_user_id: The ID of the End-User to receive this request.

          default_units: The unit-of-measure set's default units to appear in the U/M field on
              transaction line items. You can specify separate defaults for purchases, sales,
              and shipping.

          is_active: Indicates whether this unit-of-measure set is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          related_units: The unit-of-measure set's related units, each specifying how many base units
              they represent (conversion ratio).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/unit-of-measure-sets",
            body=maybe_transform(
                {
                    "base_unit": base_unit,
                    "name": name,
                    "unit_of_measure_type": unit_of_measure_type,
                    "default_units": default_units,
                    "is_active": is_active,
                    "related_units": related_units,
                },
                unit_of_measure_set_create_params.UnitOfMeasureSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitOfMeasureSet,
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
    ) -> UnitOfMeasureSet:
        """
        Retrieves an unit-of-measure set by ID.

        **IMPORTANT:** If you need to fetch multiple specific unit-of-measure sets by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the unit-of-measure set to
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
            f"/quickbooks-desktop/unit-of-measure-sets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitOfMeasureSet,
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
    ) -> UnitOfMeasureSetListResponse:
        """Lists all unit-of-measure sets.

        NOTE: QuickBooks Desktop does not support
        pagination for unit-of-measure sets; hence, there is no cursor parameter. Users
        typically have few unit-of-measure sets.

        NOTE: The QuickBooks company file must have unit-of-measure enabled (either a
        single unit per item or multiple units per item).

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific unit-of-measure sets by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              unit-of-measure sets. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all unit-of-measure sets
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because unit-of-measure sets typically have low record counts.

          name_contains: Filter for unit-of-measure sets whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for unit-of-measure sets whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for unit-of-measure sets whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific unit-of-measure sets by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for an unit-of-measure set.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for unit-of-measure sets whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for unit-of-measure sets whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for unit-of-measure sets that are active, inactive, or both.

          updated_after: Filter for unit-of-measure sets updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for unit-of-measure sets updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/unit-of-measure-sets",
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
                    unit_of_measure_set_list_params.UnitOfMeasureSetListParams,
                ),
            ),
            cast_to=UnitOfMeasureSetListResponse,
        )


class AsyncUnitOfMeasureSetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnitOfMeasureSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUnitOfMeasureSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnitOfMeasureSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncUnitOfMeasureSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        base_unit: unit_of_measure_set_create_params.BaseUnit,
        name: str,
        unit_of_measure_type: Literal["area", "count", "length", "other", "time", "volume", "weight"],
        conductor_end_user_id: str,
        default_units: Iterable[unit_of_measure_set_create_params.DefaultUnit] | Omit = omit,
        is_active: bool | Omit = omit,
        related_units: Iterable[unit_of_measure_set_create_params.RelatedUnit] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitOfMeasureSet:
        """
        Creates a new unit-of-measure set.

        NOTE: The QuickBooks company file must have unit-of-measure enabled (either a
        single unit per item or multiple units per item). To support both
        configurations, prefix all UOM set names with "By the" (for example, "By the
        Barrel"); otherwise, the set may not appear in the QuickBooks UI when the
        company file is configured for a single unit per item.

        Args:
          base_unit: The unit-of-measure set's base unit used to track and price item quantities. If
              the company file is enabled for a single unit of measure per item, the base unit
              is the only unit available on transaction line items. If enabled for multiple
              units per item, the base unit is the default unless overridden by the set's
              default units.

          name: The case-insensitive unique name of this unit-of-measure set, unique across all
              unit-of-measure sets. To ensure this set appears in the QuickBooks UI for
              companies configured with a single unit per item, prefix the name with "By the"
              (e.g., "By the Barrel").

              **NOTE**: Unit-of-measure sets do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          unit_of_measure_type: The unit-of-measure set's type. Use "other" for a custom type defined in
              QuickBooks.

          conductor_end_user_id: The ID of the End-User to receive this request.

          default_units: The unit-of-measure set's default units to appear in the U/M field on
              transaction line items. You can specify separate defaults for purchases, sales,
              and shipping.

          is_active: Indicates whether this unit-of-measure set is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          related_units: The unit-of-measure set's related units, each specifying how many base units
              they represent (conversion ratio).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/unit-of-measure-sets",
            body=await async_maybe_transform(
                {
                    "base_unit": base_unit,
                    "name": name,
                    "unit_of_measure_type": unit_of_measure_type,
                    "default_units": default_units,
                    "is_active": is_active,
                    "related_units": related_units,
                },
                unit_of_measure_set_create_params.UnitOfMeasureSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitOfMeasureSet,
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
    ) -> UnitOfMeasureSet:
        """
        Retrieves an unit-of-measure set by ID.

        **IMPORTANT:** If you need to fetch multiple specific unit-of-measure sets by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the unit-of-measure set to
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
            f"/quickbooks-desktop/unit-of-measure-sets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitOfMeasureSet,
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
    ) -> UnitOfMeasureSetListResponse:
        """Lists all unit-of-measure sets.

        NOTE: QuickBooks Desktop does not support
        pagination for unit-of-measure sets; hence, there is no cursor parameter. Users
        typically have few unit-of-measure sets.

        NOTE: The QuickBooks company file must have unit-of-measure enabled (either a
        single unit per item or multiple units per item).

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific unit-of-measure sets by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              unit-of-measure sets. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all unit-of-measure sets
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because unit-of-measure sets typically have low record counts.

          name_contains: Filter for unit-of-measure sets whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for unit-of-measure sets whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for unit-of-measure sets whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific unit-of-measure sets by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for an unit-of-measure set.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for unit-of-measure sets whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for unit-of-measure sets whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for unit-of-measure sets that are active, inactive, or both.

          updated_after: Filter for unit-of-measure sets updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for unit-of-measure sets updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/unit-of-measure-sets",
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
                    unit_of_measure_set_list_params.UnitOfMeasureSetListParams,
                ),
            ),
            cast_to=UnitOfMeasureSetListResponse,
        )


class UnitOfMeasureSetsResourceWithRawResponse:
    def __init__(self, unit_of_measure_sets: UnitOfMeasureSetsResource) -> None:
        self._unit_of_measure_sets = unit_of_measure_sets

        self.create = to_raw_response_wrapper(
            unit_of_measure_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            unit_of_measure_sets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            unit_of_measure_sets.list,
        )


class AsyncUnitOfMeasureSetsResourceWithRawResponse:
    def __init__(self, unit_of_measure_sets: AsyncUnitOfMeasureSetsResource) -> None:
        self._unit_of_measure_sets = unit_of_measure_sets

        self.create = async_to_raw_response_wrapper(
            unit_of_measure_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            unit_of_measure_sets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            unit_of_measure_sets.list,
        )


class UnitOfMeasureSetsResourceWithStreamingResponse:
    def __init__(self, unit_of_measure_sets: UnitOfMeasureSetsResource) -> None:
        self._unit_of_measure_sets = unit_of_measure_sets

        self.create = to_streamed_response_wrapper(
            unit_of_measure_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            unit_of_measure_sets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            unit_of_measure_sets.list,
        )


class AsyncUnitOfMeasureSetsResourceWithStreamingResponse:
    def __init__(self, unit_of_measure_sets: AsyncUnitOfMeasureSetsResource) -> None:
        self._unit_of_measure_sets = unit_of_measure_sets

        self.create = async_to_streamed_response_wrapper(
            unit_of_measure_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            unit_of_measure_sets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            unit_of_measure_sets.list,
        )
