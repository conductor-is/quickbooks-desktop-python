# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import (
    sales_tax_group_item_list_params,
    sales_tax_group_item_create_params,
    sales_tax_group_item_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.sales_tax_group_item import SalesTaxGroupItem

__all__ = ["SalesTaxGroupItemsResource", "AsyncSalesTaxGroupItemsResource"]


class SalesTaxGroupItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesTaxGroupItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return SalesTaxGroupItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesTaxGroupItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return SalesTaxGroupItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        sales_tax_item_ids: SequenceNotStr[str],
        conductor_end_user_id: str,
        barcode: sales_tax_group_item_create_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxGroupItem:
        """
        Creates a new sales-tax group item.

        Args:
          name: The case-insensitive unique name of this sales-tax group item, unique across all
              sales-tax group items.

              **NOTE**: Sales-tax group items do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          sales_tax_item_ids: The sales-tax items that make up this sales-tax group item. QuickBooks Desktop
              applies these sales-tax items together as one tax selection while tracking each
              sales tax separately.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax group item's barcode.

          description: The sales-tax group item's description that will appear on sales forms that
              include this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this sales-tax group item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-tax-group-items",
            body=maybe_transform(
                {
                    "name": name,
                    "sales_tax_item_ids": sales_tax_item_ids,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                },
                sales_tax_group_item_create_params.SalesTaxGroupItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
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
    ) -> SalesTaxGroupItem:
        """
        Retrieves a sales-tax group item by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax group items by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax group item to
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
            path_template("/quickbooks-desktop/sales-tax-group-items/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: sales_tax_group_item_update_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        sales_tax_item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxGroupItem:
        """
        Updates an existing sales-tax group item.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax group item to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax group item
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax group item's barcode.

          description: The sales-tax group item's description that will appear on sales forms that
              include this item.

          is_active: Indicates whether this sales-tax group item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this sales-tax group item, unique across all
              sales-tax group items.

              **NOTE**: Sales-tax group items do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          sales_tax_item_ids: The sales-tax items that make up this sales-tax group item. QuickBooks Desktop
              applies these sales-tax items together as one tax selection while tracking each
              sales tax separately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            path_template("/quickbooks-desktop/sales-tax-group-items/{id}", id=id),
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "sales_tax_item_ids": sales_tax_item_ids,
                },
                sales_tax_group_item_update_params.SalesTaxGroupItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
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
    ) -> SyncCursorPage[SalesTaxGroupItem]:
        """Returns a list of sales-tax group items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax group items by their QuickBooks-assigned unique
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

          name_contains: Filter for sales-tax group items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales-tax group items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales-tax group items whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific sales-tax group items by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for a sales-tax group item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales-tax group items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales-tax group items whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for sales-tax group items that are active, inactive, or both.

          updated_after: Filter for sales-tax group items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax group items updated on or before this date/time. Accepts
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
        return self._get_api_list(
            "/quickbooks-desktop/sales-tax-group-items",
            page=SyncCursorPage[SalesTaxGroupItem],
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
                    sales_tax_group_item_list_params.SalesTaxGroupItemListParams,
                ),
            ),
            model=SalesTaxGroupItem,
        )


class AsyncSalesTaxGroupItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesTaxGroupItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesTaxGroupItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesTaxGroupItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncSalesTaxGroupItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        sales_tax_item_ids: SequenceNotStr[str],
        conductor_end_user_id: str,
        barcode: sales_tax_group_item_create_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxGroupItem:
        """
        Creates a new sales-tax group item.

        Args:
          name: The case-insensitive unique name of this sales-tax group item, unique across all
              sales-tax group items.

              **NOTE**: Sales-tax group items do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          sales_tax_item_ids: The sales-tax items that make up this sales-tax group item. QuickBooks Desktop
              applies these sales-tax items together as one tax selection while tracking each
              sales tax separately.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax group item's barcode.

          description: The sales-tax group item's description that will appear on sales forms that
              include this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this sales-tax group item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-tax-group-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sales_tax_item_ids": sales_tax_item_ids,
                    "barcode": barcode,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                },
                sales_tax_group_item_create_params.SalesTaxGroupItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
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
    ) -> SalesTaxGroupItem:
        """
        Retrieves a sales-tax group item by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax group items by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax group item to
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
            path_template("/quickbooks-desktop/sales-tax-group-items/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: sales_tax_group_item_update_params.Barcode | Omit = omit,
        description: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        sales_tax_item_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxGroupItem:
        """
        Updates an existing sales-tax group item.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax group item to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax group item
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax group item's barcode.

          description: The sales-tax group item's description that will appear on sales forms that
              include this item.

          is_active: Indicates whether this sales-tax group item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this sales-tax group item, unique across all
              sales-tax group items.

              **NOTE**: Sales-tax group items do not have a `fullName` field because they are
              not hierarchical objects, which is why `name` is unique for them but not for
              objects that have parents.

              Maximum length: 31 characters.

          sales_tax_item_ids: The sales-tax items that make up this sales-tax group item. QuickBooks Desktop
              applies these sales-tax items together as one tax selection while tracking each
              sales tax separately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            path_template("/quickbooks-desktop/sales-tax-group-items/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "sales_tax_item_ids": sales_tax_item_ids,
                },
                sales_tax_group_item_update_params.SalesTaxGroupItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxGroupItem,
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
    ) -> AsyncPaginator[SalesTaxGroupItem, AsyncCursorPage[SalesTaxGroupItem]]:
        """Returns a list of sales-tax group items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax group items by their QuickBooks-assigned unique
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

          name_contains: Filter for sales-tax group items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales-tax group items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales-tax group items whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific sales-tax group items by their name(s), case-insensitive.
              Like `id`, `name` is a unique identifier for a sales-tax group item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales-tax group items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales-tax group items whose `name` is alphabetically less than or
              equal to this value.

          status: Filter for sales-tax group items that are active, inactive, or both.

          updated_after: Filter for sales-tax group items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax group items updated on or before this date/time. Accepts
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
        return self._get_api_list(
            "/quickbooks-desktop/sales-tax-group-items",
            page=AsyncCursorPage[SalesTaxGroupItem],
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
                    sales_tax_group_item_list_params.SalesTaxGroupItemListParams,
                ),
            ),
            model=SalesTaxGroupItem,
        )


class SalesTaxGroupItemsResourceWithRawResponse:
    def __init__(self, sales_tax_group_items: SalesTaxGroupItemsResource) -> None:
        self._sales_tax_group_items = sales_tax_group_items

        self.create = to_raw_response_wrapper(
            sales_tax_group_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_tax_group_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_tax_group_items.update,
        )
        self.list = to_raw_response_wrapper(
            sales_tax_group_items.list,
        )


class AsyncSalesTaxGroupItemsResourceWithRawResponse:
    def __init__(self, sales_tax_group_items: AsyncSalesTaxGroupItemsResource) -> None:
        self._sales_tax_group_items = sales_tax_group_items

        self.create = async_to_raw_response_wrapper(
            sales_tax_group_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_tax_group_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_tax_group_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_tax_group_items.list,
        )


class SalesTaxGroupItemsResourceWithStreamingResponse:
    def __init__(self, sales_tax_group_items: SalesTaxGroupItemsResource) -> None:
        self._sales_tax_group_items = sales_tax_group_items

        self.create = to_streamed_response_wrapper(
            sales_tax_group_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_tax_group_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_tax_group_items.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_tax_group_items.list,
        )


class AsyncSalesTaxGroupItemsResourceWithStreamingResponse:
    def __init__(self, sales_tax_group_items: AsyncSalesTaxGroupItemsResource) -> None:
        self._sales_tax_group_items = sales_tax_group_items

        self.create = async_to_streamed_response_wrapper(
            sales_tax_group_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_tax_group_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_tax_group_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_tax_group_items.list,
        )
