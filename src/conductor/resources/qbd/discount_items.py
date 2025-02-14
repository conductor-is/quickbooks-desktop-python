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
from ...types.qbd import discount_item_list_params, discount_item_create_params, discount_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.discount_item import DiscountItem

__all__ = ["DiscountItemsResource", "AsyncDiscountItemsResource"]


class DiscountItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiscountItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return DiscountItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscountItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return DiscountItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        conductor_end_user_id: str,
        barcode: discount_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        discount_rate: str | NotGiven = NOT_GIVEN,
        discount_rate_percent: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscountItem:
        """
        Creates a new discount item.

        Args:
          account_id: The posting account to which transactions involving this discount item are
              posted for tracking discounts.

          name: The case-insensitive name of this discount item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two discount items could both have the `name` "10%
              labor discount", but they could have unique `fullName` values, such as
              "Discounts:10% labor discount" and "Promotions:10% labor discount".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The discount item's barcode.

          class_id: The discount item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The discount item's description that will appear on sales forms that include
              this item.

          discount_rate: The monetary amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A flat rate discount applies to ALL lines recorded above it and
              distributes the discount amount equally across those lines, which affects tax
              calculations. For example, a $10 discount applied to a $100 taxable item and
              $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
              discount.

          discount_rate_percent: The percentage amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A percentage discount only applies to the line immediately above it,
              so tax implications only affect that specific line.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this discount item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent discount item one level above this one in the hierarchy. For example,
              if this discount item has a `fullName` of "Discounts:10% labor discount", its
              parent has a `fullName` of "Discounts". If this discount item is at the top
              level, this field will be `null`.

          sales_tax_code_id: The default sales-tax code for this discount item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/discount-items",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "discount_rate": discount_rate,
                    "discount_rate_percent": discount_rate_percent,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                discount_item_create_params.DiscountItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
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
    ) -> DiscountItem:
        """
        Retrieves a discount item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the discount item to retrieve.

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
            f"/quickbooks-desktop/discount-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        barcode: discount_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        discount_rate: str | NotGiven = NOT_GIVEN,
        discount_rate_percent: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        update_existing_transactions_account: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscountItem:
        """
        Updates an existing discount item.

        Args:
          id: The QuickBooks-assigned unique identifier of the discount item to update.

          revision_number: The current QuickBooks-assigned revision number of the discount item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The posting account to which transactions involving this discount item are
              posted for tracking discounts.

          barcode: The discount item's barcode.

          class_id: The discount item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The discount item's description that will appear on sales forms that include
              this item.

          discount_rate: The monetary amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A flat rate discount applies to ALL lines recorded above it and
              distributes the discount amount equally across those lines, which affects tax
              calculations. For example, a $10 discount applied to a $100 taxable item and
              $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
              discount.

          discount_rate_percent: The percentage amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A percentage discount only applies to the line immediately above it,
              so tax implications only affect that specific line.

          is_active: Indicates whether this discount item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this discount item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two discount items could both have the `name` "10%
              labor discount", but they could have unique `fullName` values, such as
              "Discounts:10% labor discount" and "Promotions:10% labor discount".

              Maximum length: 31 characters.

          parent_id: The parent discount item one level above this one in the hierarchy. For example,
              if this discount item has a `fullName` of "Discounts:10% labor discount", its
              parent has a `fullName` of "Discounts". If this discount item is at the top
              level, this field will be `null`.

          sales_tax_code_id: The default sales-tax code for this discount item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          update_existing_transactions_account: When `true`, applies the new account (specified by the `accountId` field) to all
              existing transactions associated with this discount item. This updates
              historical data and should be used with caution. The update will fail if any
              affected transaction falls within a closed accounting period. If this parameter
              is not specified, QuickBooks will prompt the user before making any changes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/discount-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "discount_rate": discount_rate,
                    "discount_rate_percent": discount_rate_percent,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "update_existing_transactions_account": update_existing_transactions_account,
                },
                discount_item_update_params.DiscountItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncCursorPage[DiscountItem]:
        """Returns a list of discount items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for discount items of these classes. A class is a way end-users can
              categorize discount items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific discount items by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a discount item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a discount item is under "Discounts" and has the `name`
              "10% labor discount", its `fullName` would be "Discounts:10% labor discount".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific discount items by their QuickBooks-assigned unique
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

          name_contains: Filter for discount items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for discount items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for discount items whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for discount items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for discount items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for discount items that are active, inactive, or both.

          updated_after: Filter for discount items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for discount items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/discount-items",
            page=SyncCursorPage[DiscountItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "cursor": cursor,
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
                    discount_item_list_params.DiscountItemListParams,
                ),
            ),
            model=DiscountItem,
        )


class AsyncDiscountItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiscountItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscountItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscountItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncDiscountItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        conductor_end_user_id: str,
        barcode: discount_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        discount_rate: str | NotGiven = NOT_GIVEN,
        discount_rate_percent: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscountItem:
        """
        Creates a new discount item.

        Args:
          account_id: The posting account to which transactions involving this discount item are
              posted for tracking discounts.

          name: The case-insensitive name of this discount item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two discount items could both have the `name` "10%
              labor discount", but they could have unique `fullName` values, such as
              "Discounts:10% labor discount" and "Promotions:10% labor discount".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The discount item's barcode.

          class_id: The discount item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The discount item's description that will appear on sales forms that include
              this item.

          discount_rate: The monetary amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A flat rate discount applies to ALL lines recorded above it and
              distributes the discount amount equally across those lines, which affects tax
              calculations. For example, a $10 discount applied to a $100 taxable item and
              $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
              discount.

          discount_rate_percent: The percentage amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A percentage discount only applies to the line immediately above it,
              so tax implications only affect that specific line.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this discount item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent discount item one level above this one in the hierarchy. For example,
              if this discount item has a `fullName` of "Discounts:10% labor discount", its
              parent has a `fullName` of "Discounts". If this discount item is at the top
              level, this field will be `null`.

          sales_tax_code_id: The default sales-tax code for this discount item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/discount-items",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "discount_rate": discount_rate,
                    "discount_rate_percent": discount_rate_percent,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                discount_item_create_params.DiscountItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
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
    ) -> DiscountItem:
        """
        Retrieves a discount item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the discount item to retrieve.

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
            f"/quickbooks-desktop/discount-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        barcode: discount_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        discount_rate: str | NotGiven = NOT_GIVEN,
        discount_rate_percent: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        update_existing_transactions_account: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscountItem:
        """
        Updates an existing discount item.

        Args:
          id: The QuickBooks-assigned unique identifier of the discount item to update.

          revision_number: The current QuickBooks-assigned revision number of the discount item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The posting account to which transactions involving this discount item are
              posted for tracking discounts.

          barcode: The discount item's barcode.

          class_id: The discount item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          description: The discount item's description that will appear on sales forms that include
              this item.

          discount_rate: The monetary amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A flat rate discount applies to ALL lines recorded above it and
              distributes the discount amount equally across those lines, which affects tax
              calculations. For example, a $10 discount applied to a $100 taxable item and
              $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
              discount.

          discount_rate_percent: The percentage amount to subtract from the total or subtotal when applying this
              discount item to a transaction.

              **NOTE**: A percentage discount only applies to the line immediately above it,
              so tax implications only affect that specific line.

          is_active: Indicates whether this discount item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this discount item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two discount items could both have the `name` "10%
              labor discount", but they could have unique `fullName` values, such as
              "Discounts:10% labor discount" and "Promotions:10% labor discount".

              Maximum length: 31 characters.

          parent_id: The parent discount item one level above this one in the hierarchy. For example,
              if this discount item has a `fullName` of "Discounts:10% labor discount", its
              parent has a `fullName` of "Discounts". If this discount item is at the top
              level, this field will be `null`.

          sales_tax_code_id: The default sales-tax code for this discount item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          update_existing_transactions_account: When `true`, applies the new account (specified by the `accountId` field) to all
              existing transactions associated with this discount item. This updates
              historical data and should be used with caution. The update will fail if any
              affected transaction falls within a closed accounting period. If this parameter
              is not specified, QuickBooks will prompt the user before making any changes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/discount-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "description": description,
                    "discount_rate": discount_rate,
                    "discount_rate_percent": discount_rate_percent,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "update_existing_transactions_account": update_existing_transactions_account,
                },
                discount_item_update_params.DiscountItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[DiscountItem, AsyncCursorPage[DiscountItem]]:
        """Returns a list of discount items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for discount items of these classes. A class is a way end-users can
              categorize discount items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific discount items by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a discount item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a discount item is under "Discounts" and has the `name`
              "10% labor discount", its `fullName` would be "Discounts:10% labor discount".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific discount items by their QuickBooks-assigned unique
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

          name_contains: Filter for discount items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for discount items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for discount items whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for discount items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for discount items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for discount items that are active, inactive, or both.

          updated_after: Filter for discount items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for discount items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/discount-items",
            page=AsyncCursorPage[DiscountItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "cursor": cursor,
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
                    discount_item_list_params.DiscountItemListParams,
                ),
            ),
            model=DiscountItem,
        )


class DiscountItemsResourceWithRawResponse:
    def __init__(self, discount_items: DiscountItemsResource) -> None:
        self._discount_items = discount_items

        self.create = to_raw_response_wrapper(
            discount_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            discount_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            discount_items.update,
        )
        self.list = to_raw_response_wrapper(
            discount_items.list,
        )


class AsyncDiscountItemsResourceWithRawResponse:
    def __init__(self, discount_items: AsyncDiscountItemsResource) -> None:
        self._discount_items = discount_items

        self.create = async_to_raw_response_wrapper(
            discount_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            discount_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            discount_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            discount_items.list,
        )


class DiscountItemsResourceWithStreamingResponse:
    def __init__(self, discount_items: DiscountItemsResource) -> None:
        self._discount_items = discount_items

        self.create = to_streamed_response_wrapper(
            discount_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            discount_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            discount_items.update,
        )
        self.list = to_streamed_response_wrapper(
            discount_items.list,
        )


class AsyncDiscountItemsResourceWithStreamingResponse:
    def __init__(self, discount_items: AsyncDiscountItemsResource) -> None:
        self._discount_items = discount_items

        self.create = async_to_streamed_response_wrapper(
            discount_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            discount_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            discount_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            discount_items.list,
        )
