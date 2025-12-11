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
from ...types.qbd import sales_tax_item_list_params, sales_tax_item_create_params, sales_tax_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.sales_tax_item import SalesTaxItem

__all__ = ["SalesTaxItemsResource", "AsyncSalesTaxItemsResource"]


class SalesTaxItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesTaxItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return SalesTaxItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesTaxItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return SalesTaxItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: sales_tax_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        sales_tax_return_line_id: str | Omit = omit,
        tax_rate: str | Omit = omit,
        tax_vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxItem:
        """
        Creates a new sales-tax item.

        Args:
          name: The case-insensitive unique name of this sales-tax item, unique across all
              sales-tax items.

              **NOTE**: Sales-tax items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax item's barcode.

          class_id: The sales-tax item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The sales-tax item's description that will appear on sales forms that include
              this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this sales-tax item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          sales_tax_return_line_id: The specific line on the sales tax return form where the tax collected using
              this sales-tax item should be reported.

          tax_rate: The tax rate defined by this sales-tax item, represented as a decimal string.
              For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
              of sales tax applied when this item is used in transactions. If a non-zero
              `taxRate` is specified, then the `taxVendor` field is required.

          tax_vendor_id: The tax agency (vendor) to whom collected sales taxes are owed for this
              sales-tax item. This field refers to a vendor in QuickBooks that represents the
              tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-tax-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                    "sales_tax_return_line_id": sales_tax_return_line_id,
                    "tax_rate": tax_rate,
                    "tax_vendor_id": tax_vendor_id,
                },
                sales_tax_item_create_params.SalesTaxItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
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
    ) -> SalesTaxItem:
        """
        Retrieves a sales-tax item by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax items by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax item to retrieve.

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
            f"/quickbooks-desktop/sales-tax-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: sales_tax_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        description: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        sales_tax_return_line_id: str | Omit = omit,
        tax_rate: str | Omit = omit,
        tax_vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxItem:
        """
        Updates an existing sales-tax item.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax item to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax item's barcode.

          class_id: The sales-tax item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The sales-tax item's description that will appear on sales forms that include
              this item.

          is_active: Indicates whether this sales-tax item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this sales-tax item, unique across all
              sales-tax items.

              **NOTE**: Sales-tax items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          sales_tax_return_line_id: The specific line on the sales tax return form where the tax collected using
              this sales-tax item should be reported.

          tax_rate: The tax rate defined by this sales-tax item, represented as a decimal string.
              For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
              of sales tax applied when this item is used in transactions. If a non-zero
              `taxRate` is specified, then the `taxVendor` field is required.

          tax_vendor_id: The tax agency (vendor) to whom collected sales taxes are owed for this
              sales-tax item. This field refers to a vendor in QuickBooks that represents the
              tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/sales-tax-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "sales_tax_return_line_id": sales_tax_return_line_id,
                    "tax_rate": tax_rate,
                    "tax_vendor_id": tax_vendor_id,
                },
                sales_tax_item_update_params.SalesTaxItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> SyncCursorPage[SalesTaxItem]:
        """Returns a list of sales-tax items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for sales-tax items of these classes. A class is a way end-users can
              categorize sales-tax items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax items by their QuickBooks-assigned unique
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

          name_contains: Filter for sales-tax items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales-tax items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales-tax items whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific sales-tax items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a sales-tax item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales-tax items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales-tax items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for sales-tax items that are active, inactive, or both.

          updated_after: Filter for sales-tax items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/sales-tax-items",
            page=SyncCursorPage[SalesTaxItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
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
                    sales_tax_item_list_params.SalesTaxItemListParams,
                ),
            ),
            model=SalesTaxItem,
        )


class AsyncSalesTaxItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesTaxItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesTaxItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesTaxItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncSalesTaxItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: sales_tax_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        sales_tax_return_line_id: str | Omit = omit,
        tax_rate: str | Omit = omit,
        tax_vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxItem:
        """
        Creates a new sales-tax item.

        Args:
          name: The case-insensitive unique name of this sales-tax item, unique across all
              sales-tax items.

              **NOTE**: Sales-tax items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax item's barcode.

          class_id: The sales-tax item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The sales-tax item's description that will appear on sales forms that include
              this item.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this sales-tax item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          sales_tax_return_line_id: The specific line on the sales tax return form where the tax collected using
              this sales-tax item should be reported.

          tax_rate: The tax rate defined by this sales-tax item, represented as a decimal string.
              For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
              of sales tax applied when this item is used in transactions. If a non-zero
              `taxRate` is specified, then the `taxVendor` field is required.

          tax_vendor_id: The tax agency (vendor) to whom collected sales taxes are owed for this
              sales-tax item. This field refers to a vendor in QuickBooks that represents the
              tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-tax-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "external_id": external_id,
                    "is_active": is_active,
                    "sales_tax_return_line_id": sales_tax_return_line_id,
                    "tax_rate": tax_rate,
                    "tax_vendor_id": tax_vendor_id,
                },
                sales_tax_item_create_params.SalesTaxItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
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
    ) -> SalesTaxItem:
        """
        Retrieves a sales-tax item by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax items by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax item to retrieve.

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
            f"/quickbooks-desktop/sales-tax-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: sales_tax_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        description: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        sales_tax_return_line_id: str | Omit = omit,
        tax_rate: str | Omit = omit,
        tax_vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxItem:
        """
        Updates an existing sales-tax item.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax item to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The sales-tax item's barcode.

          class_id: The sales-tax item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The sales-tax item's description that will appear on sales forms that include
              this item.

          is_active: Indicates whether this sales-tax item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this sales-tax item, unique across all
              sales-tax items.

              **NOTE**: Sales-tax items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          sales_tax_return_line_id: The specific line on the sales tax return form where the tax collected using
              this sales-tax item should be reported.

          tax_rate: The tax rate defined by this sales-tax item, represented as a decimal string.
              For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
              of sales tax applied when this item is used in transactions. If a non-zero
              `taxRate` is specified, then the `taxVendor` field is required.

          tax_vendor_id: The tax agency (vendor) to whom collected sales taxes are owed for this
              sales-tax item. This field refers to a vendor in QuickBooks that represents the
              tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/sales-tax-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "sales_tax_return_line_id": sales_tax_return_line_id,
                    "tax_rate": tax_rate,
                    "tax_vendor_id": tax_vendor_id,
                },
                sales_tax_item_update_params.SalesTaxItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> AsyncPaginator[SalesTaxItem, AsyncCursorPage[SalesTaxItem]]:
        """Returns a list of sales-tax items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for sales-tax items of these classes. A class is a way end-users can
              categorize sales-tax items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax items by their QuickBooks-assigned unique
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

          name_contains: Filter for sales-tax items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for sales-tax items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for sales-tax items whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific sales-tax items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a sales-tax item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for sales-tax items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for sales-tax items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for sales-tax items that are active, inactive, or both.

          updated_after: Filter for sales-tax items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/sales-tax-items",
            page=AsyncCursorPage[SalesTaxItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
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
                    sales_tax_item_list_params.SalesTaxItemListParams,
                ),
            ),
            model=SalesTaxItem,
        )


class SalesTaxItemsResourceWithRawResponse:
    def __init__(self, sales_tax_items: SalesTaxItemsResource) -> None:
        self._sales_tax_items = sales_tax_items

        self.create = to_raw_response_wrapper(
            sales_tax_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_tax_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_tax_items.update,
        )
        self.list = to_raw_response_wrapper(
            sales_tax_items.list,
        )


class AsyncSalesTaxItemsResourceWithRawResponse:
    def __init__(self, sales_tax_items: AsyncSalesTaxItemsResource) -> None:
        self._sales_tax_items = sales_tax_items

        self.create = async_to_raw_response_wrapper(
            sales_tax_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_tax_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_tax_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_tax_items.list,
        )


class SalesTaxItemsResourceWithStreamingResponse:
    def __init__(self, sales_tax_items: SalesTaxItemsResource) -> None:
        self._sales_tax_items = sales_tax_items

        self.create = to_streamed_response_wrapper(
            sales_tax_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_tax_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_tax_items.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_tax_items.list,
        )


class AsyncSalesTaxItemsResourceWithStreamingResponse:
    def __init__(self, sales_tax_items: AsyncSalesTaxItemsResource) -> None:
        self._sales_tax_items = sales_tax_items

        self.create = async_to_streamed_response_wrapper(
            sales_tax_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_tax_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_tax_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_tax_items.list,
        )
