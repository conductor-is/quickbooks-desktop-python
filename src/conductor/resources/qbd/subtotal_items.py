# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import subtotal_item_list_params, subtotal_item_create_params, subtotal_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.subtotal_item import SubtotalItem

__all__ = ["SubtotalItemsResource", "AsyncSubtotalItemsResource"]


class SubtotalItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubtotalItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return SubtotalItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubtotalItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return SubtotalItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: subtotal_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Creates a new subtotal item.

        Args:
          name: The case-insensitive unique name of this subtotal item, unique across all
              subtotal items.

              **NOTE**: Subtotal items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The subtotal item's barcode.

          description: The subtotal item's description that will appear on sales forms that include
              this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this subtotal item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/subtotal-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                },
                subtotal_item_create_params.SubtotalItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Retrieves a subtotal item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the subtotal item to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/subtotal-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: subtotal_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Updates an existing subtotal item.

        Args:
          id: The QuickBooks-assigned unique identifier of the subtotal item to update.

          revision_number: The current QuickBooks-assigned revision number of the subtotal item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The subtotal item's barcode.

          description: The subtotal item's description that will appear on sales forms that include
              this item.

          is_active: Indicates whether this subtotal item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this subtotal item, unique across all
              subtotal items.

              **NOTE**: Subtotal items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/subtotal-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                },
                subtotal_item_update_params.SubtotalItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[SubtotalItem]:
        """Returns a list of subtotal items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific subtotal items by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for subtotal items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for subtotal items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for subtotal items whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific subtotal items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a subtotal item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for subtotal items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for subtotal items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for subtotal items that are active, inactive, or both.

          updated_after: Filter for subtotal items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for subtotal items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/subtotal-items",
            page=SyncCursorPage[SubtotalItem],
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
                    subtotal_item_list_params.SubtotalItemListParams,
                ),
            ),
            model=SubtotalItem,
        )


class AsyncSubtotalItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubtotalItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubtotalItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubtotalItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncSubtotalItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: subtotal_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Creates a new subtotal item.

        Args:
          name: The case-insensitive unique name of this subtotal item, unique across all
              subtotal items.

              **NOTE**: Subtotal items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The subtotal item's barcode.

          description: The subtotal item's description that will appear on sales forms that include
              this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this subtotal item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/subtotal-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                },
                subtotal_item_create_params.SubtotalItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Retrieves a subtotal item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the subtotal item to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/subtotal-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: subtotal_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubtotalItem:
        """
        Updates an existing subtotal item.

        Args:
          id: The QuickBooks-assigned unique identifier of the subtotal item to update.

          revision_number: The current QuickBooks-assigned revision number of the subtotal item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The subtotal item's barcode.

          description: The subtotal item's description that will appear on sales forms that include
              this item.

          is_active: Indicates whether this subtotal item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this subtotal item, unique across all
              subtotal items.

              **NOTE**: Subtotal items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/subtotal-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                },
                subtotal_item_update_params.SubtotalItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubtotalItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SubtotalItem, AsyncCursorPage[SubtotalItem]]:
        """Returns a list of subtotal items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific subtotal items by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for subtotal items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for subtotal items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for subtotal items whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific subtotal items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a subtotal item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for subtotal items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for subtotal items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for subtotal items that are active, inactive, or both.

          updated_after: Filter for subtotal items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for subtotal items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/subtotal-items",
            page=AsyncCursorPage[SubtotalItem],
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
                    subtotal_item_list_params.SubtotalItemListParams,
                ),
            ),
            model=SubtotalItem,
        )


class SubtotalItemsResourceWithRawResponse:
    def __init__(self, subtotal_items: SubtotalItemsResource) -> None:
        self._subtotal_items = subtotal_items

        self.create = to_raw_response_wrapper(
            subtotal_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subtotal_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            subtotal_items.update,
        )
        self.list = to_raw_response_wrapper(
            subtotal_items.list,
        )


class AsyncSubtotalItemsResourceWithRawResponse:
    def __init__(self, subtotal_items: AsyncSubtotalItemsResource) -> None:
        self._subtotal_items = subtotal_items

        self.create = async_to_raw_response_wrapper(
            subtotal_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subtotal_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            subtotal_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            subtotal_items.list,
        )


class SubtotalItemsResourceWithStreamingResponse:
    def __init__(self, subtotal_items: SubtotalItemsResource) -> None:
        self._subtotal_items = subtotal_items

        self.create = to_streamed_response_wrapper(
            subtotal_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subtotal_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            subtotal_items.update,
        )
        self.list = to_streamed_response_wrapper(
            subtotal_items.list,
        )


class AsyncSubtotalItemsResourceWithStreamingResponse:
    def __init__(self, subtotal_items: AsyncSubtotalItemsResource) -> None:
        self._subtotal_items = subtotal_items

        self.create = async_to_streamed_response_wrapper(
            subtotal_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subtotal_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            subtotal_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subtotal_items.list,
        )
