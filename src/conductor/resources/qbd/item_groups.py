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
from ...types.qbd import item_group_list_params, item_group_create_params, item_group_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.item_group import ItemGroup

__all__ = ["ItemGroupsResource", "AsyncItemGroupsResource"]


class ItemGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return ItemGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return ItemGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        should_print_items_in_group: bool,
        conductor_end_user_id: str,
        barcode: item_group_create_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        lines: Iterable[item_group_create_params.Line] | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGroup:
        """
        Creates a new item group.

        Args:
          name: The case-insensitive unique name of this item group, unique across all item
              groups.

              **NOTE**: Item groups do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          should_print_items_in_group: Indicates whether the individual items in this item group and their separate
              amounts appear on printed forms.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The item group's barcode.

          description: The item group's description that will appear on sales forms that include this
              item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this item group is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          lines: The item lines in this item group.

          unit_of_measure_set_id: The unit-of-measure set associated with this item group, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/item-groups",
            body=maybe_transform(
                {
                    "name": name,
                    "should_print_items_in_group": should_print_items_in_group,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                    "lines": lines,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                item_group_create_params.ItemGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
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
    ) -> ItemGroup:
        """
        Retrieves an item group by ID.

        **IMPORTANT:** If you need to fetch multiple specific item groups by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the item group to retrieve.

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
            f"/quickbooks-desktop/item-groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: item_group_update_params.Barcode | Omit = omit,
        clear_item_lines: bool | Omit = omit,
        description: str | Omit = omit,
        force_unit_of_measure_change: bool | Omit = omit,
        is_active: bool | Omit = omit,
        lines: Iterable[item_group_update_params.Line] | Omit = omit,
        name: str | Omit = omit,
        should_print_items_in_group: bool | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGroup:
        """
        Updates an existing item group.

        Args:
          id: The QuickBooks-assigned unique identifier of the item group to update.

          revision_number: The current QuickBooks-assigned revision number of the item group object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The item group's barcode.

          clear_item_lines: When `true`, removes all existing item lines associated with this item group. To
              modify or add individual item lines, use the field `itemLines` instead.

          description: The item group's description that will appear on sales forms that include this
              item.

          force_unit_of_measure_change: Indicates whether to allow changing the item group's unit-of-measure set (using
              the `unitOfMeasureSetId` field) when the base unit of the new unit-of-measure
              set does not match that of the currently assigned set. Without setting this
              field to `true` in this scenario, the request will fail with an error; hence,
              this field is equivalent to accepting the warning prompt in the QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this item group is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          lines: The item lines in this item group.

          name: The case-insensitive unique name of this item group, unique across all item
              groups.

              **NOTE**: Item groups do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          should_print_items_in_group: Indicates whether the individual items in this item group and their separate
              amounts appear on printed forms.

          unit_of_measure_set_id: The unit-of-measure set associated with this item group, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/item-groups/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "clear_item_lines": clear_item_lines,
                    "description": description,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "lines": lines,
                    "name": name,
                    "should_print_items_in_group": should_print_items_in_group,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                item_group_update_params.ItemGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
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
    ) -> SyncCursorPage[ItemGroup]:
        """Returns a list of item groups.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific item groups by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for item groups whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for item groups whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for item groups whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific item groups by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an item group.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for item groups whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for item groups whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for item groups that are active, inactive, or both.

          updated_after: Filter for item groups updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for item groups updated on or before this date/time. Accepts the
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
        return self._get_api_list(
            "/quickbooks-desktop/item-groups",
            page=SyncCursorPage[ItemGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
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
                    item_group_list_params.ItemGroupListParams,
                ),
            ),
            model=ItemGroup,
        )


class AsyncItemGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncItemGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        should_print_items_in_group: bool,
        conductor_end_user_id: str,
        barcode: item_group_create_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        lines: Iterable[item_group_create_params.Line] | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGroup:
        """
        Creates a new item group.

        Args:
          name: The case-insensitive unique name of this item group, unique across all item
              groups.

              **NOTE**: Item groups do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          should_print_items_in_group: Indicates whether the individual items in this item group and their separate
              amounts appear on printed forms.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The item group's barcode.

          description: The item group's description that will appear on sales forms that include this
              item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this item group is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          lines: The item lines in this item group.

          unit_of_measure_set_id: The unit-of-measure set associated with this item group, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/item-groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "should_print_items_in_group": should_print_items_in_group,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                    "lines": lines,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                item_group_create_params.ItemGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
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
    ) -> ItemGroup:
        """
        Retrieves an item group by ID.

        **IMPORTANT:** If you need to fetch multiple specific item groups by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the item group to retrieve.

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
            f"/quickbooks-desktop/item-groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: item_group_update_params.Barcode | Omit = omit,
        clear_item_lines: bool | Omit = omit,
        description: str | Omit = omit,
        force_unit_of_measure_change: bool | Omit = omit,
        is_active: bool | Omit = omit,
        lines: Iterable[item_group_update_params.Line] | Omit = omit,
        name: str | Omit = omit,
        should_print_items_in_group: bool | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemGroup:
        """
        Updates an existing item group.

        Args:
          id: The QuickBooks-assigned unique identifier of the item group to update.

          revision_number: The current QuickBooks-assigned revision number of the item group object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The item group's barcode.

          clear_item_lines: When `true`, removes all existing item lines associated with this item group. To
              modify or add individual item lines, use the field `itemLines` instead.

          description: The item group's description that will appear on sales forms that include this
              item.

          force_unit_of_measure_change: Indicates whether to allow changing the item group's unit-of-measure set (using
              the `unitOfMeasureSetId` field) when the base unit of the new unit-of-measure
              set does not match that of the currently assigned set. Without setting this
              field to `true` in this scenario, the request will fail with an error; hence,
              this field is equivalent to accepting the warning prompt in the QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this item group is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          lines: The item lines in this item group.

          name: The case-insensitive unique name of this item group, unique across all item
              groups.

              **NOTE**: Item groups do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          should_print_items_in_group: Indicates whether the individual items in this item group and their separate
              amounts appear on printed forms.

          unit_of_measure_set_id: The unit-of-measure set associated with this item group, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/item-groups/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "clear_item_lines": clear_item_lines,
                    "description": description,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "lines": lines,
                    "name": name,
                    "should_print_items_in_group": should_print_items_in_group,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                item_group_update_params.ItemGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemGroup,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
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
    ) -> AsyncPaginator[ItemGroup, AsyncCursorPage[ItemGroup]]:
        """Returns a list of item groups.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific item groups by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for item groups whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for item groups whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for item groups whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific item groups by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for an item group.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for item groups whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for item groups whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for item groups that are active, inactive, or both.

          updated_after: Filter for item groups updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for item groups updated on or before this date/time. Accepts the
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
        return self._get_api_list(
            "/quickbooks-desktop/item-groups",
            page=AsyncCursorPage[ItemGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
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
                    item_group_list_params.ItemGroupListParams,
                ),
            ),
            model=ItemGroup,
        )


class ItemGroupsResourceWithRawResponse:
    def __init__(self, item_groups: ItemGroupsResource) -> None:
        self._item_groups = item_groups

        self.create = to_raw_response_wrapper(
            item_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            item_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            item_groups.update,
        )
        self.list = to_raw_response_wrapper(
            item_groups.list,
        )


class AsyncItemGroupsResourceWithRawResponse:
    def __init__(self, item_groups: AsyncItemGroupsResource) -> None:
        self._item_groups = item_groups

        self.create = async_to_raw_response_wrapper(
            item_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            item_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            item_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            item_groups.list,
        )


class ItemGroupsResourceWithStreamingResponse:
    def __init__(self, item_groups: ItemGroupsResource) -> None:
        self._item_groups = item_groups

        self.create = to_streamed_response_wrapper(
            item_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            item_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            item_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            item_groups.list,
        )


class AsyncItemGroupsResourceWithStreamingResponse:
    def __init__(self, item_groups: AsyncItemGroupsResource) -> None:
        self._item_groups = item_groups

        self.create = async_to_streamed_response_wrapper(
            item_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            item_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            item_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            item_groups.list,
        )
