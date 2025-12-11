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
from ...types.qbd import other_charge_item_list_params, other_charge_item_create_params, other_charge_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.other_charge_item import OtherChargeItem

__all__ = ["OtherChargeItemsResource", "AsyncOtherChargeItemsResource"]


class OtherChargeItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OtherChargeItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return OtherChargeItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OtherChargeItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return OtherChargeItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: other_charge_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: other_charge_item_create_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: other_charge_item_create_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherChargeItem:
        """
        Creates a new other charge item.

        Args:
          name: The case-insensitive name of this other charge item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two other charge items could both have the `name`
              "Overnight Delivery", but they could have unique `fullName` values, such as
              "Shipping Charges:Overnight Delivery" and "Misc Fees:Overnight Delivery".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The other charge item's barcode.

          class_id: The other charge item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this other charge item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent other charge item one level above this one in the hierarchy. For
              example, if this other charge item has a `fullName` of "Shipping
              Charges:Overnight Delivery", its parent has a `fullName` of "Shipping Charges".
              If this other charge item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for other charge items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating an other charge item, but never both
              because an item cannot have both configurations.

          sales_or_purchase_details: Details for other charge items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating an other charge item, but never both
              because an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this other charge item, determining whether it is
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
            "/quickbooks-desktop/other-charge-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                other_charge_item_create_params.OtherChargeItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
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
    ) -> OtherChargeItem:
        """
        Retrieves an other charge item by ID.

        **IMPORTANT:** If you need to fetch multiple specific other charge items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the other charge item to retrieve.

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
            f"/quickbooks-desktop/other-charge-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: other_charge_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: other_charge_item_update_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: other_charge_item_update_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherChargeItem:
        """
        Updates an existing other charge item.

        Args:
          id: The QuickBooks-assigned unique identifier of the other charge item to update.

          revision_number: The current QuickBooks-assigned revision number of the other charge item object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The other charge item's barcode.

          class_id: The other charge item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          is_active: Indicates whether this other charge item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this other charge item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two other charge items could both have the `name`
              "Overnight Delivery", but they could have unique `fullName` values, such as
              "Shipping Charges:Overnight Delivery" and "Misc Fees:Overnight Delivery".

              Maximum length: 31 characters.

          parent_id: The parent other charge item one level above this one in the hierarchy. For
              example, if this other charge item has a `fullName` of "Shipping
              Charges:Overnight Delivery", its parent has a `fullName` of "Shipping Charges".
              If this other charge item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for other charge items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying an other charge item because an item
              cannot have both configurations.

          sales_or_purchase_details: Details for other charge items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying an other charge item because an item
              cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this other charge item, determining whether it is
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/other-charge-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                other_charge_item_update_params.OtherChargeItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
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
    ) -> SyncCursorPage[OtherChargeItem]:
        """Returns a list of other charge items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for other charge items of these classes. A class is a way end-users can
              categorize other charge items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific other charge items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for an other charge item, formed by
              by combining the names of its parent objects with its own `name`, separated by
              colons. For example, if an other charge item is under "Shipping Charges" and has
              the `name` "Overnight Delivery", its `fullName` would be "Shipping
              Charges:Overnight Delivery".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific other charge items by their QuickBooks-assigned unique
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

          name_contains: Filter for other charge items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for other charge items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for other charge items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for other charge items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for other charge items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for other charge items that are active, inactive, or both.

          updated_after: Filter for other charge items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for other charge items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/other-charge-items",
            page=SyncCursorPage[OtherChargeItem],
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
                    other_charge_item_list_params.OtherChargeItemListParams,
                ),
            ),
            model=OtherChargeItem,
        )


class AsyncOtherChargeItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOtherChargeItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOtherChargeItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOtherChargeItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncOtherChargeItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: other_charge_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: other_charge_item_create_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: other_charge_item_create_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherChargeItem:
        """
        Creates a new other charge item.

        Args:
          name: The case-insensitive name of this other charge item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two other charge items could both have the `name`
              "Overnight Delivery", but they could have unique `fullName` values, such as
              "Shipping Charges:Overnight Delivery" and "Misc Fees:Overnight Delivery".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The other charge item's barcode.

          class_id: The other charge item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this other charge item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent other charge item one level above this one in the hierarchy. For
              example, if this other charge item has a `fullName` of "Shipping
              Charges:Overnight Delivery", its parent has a `fullName` of "Shipping Charges".
              If this other charge item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for other charge items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating an other charge item, but never both
              because an item cannot have both configurations.

          sales_or_purchase_details: Details for other charge items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating an other charge item, but never both
              because an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this other charge item, determining whether it is
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
            "/quickbooks-desktop/other-charge-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                other_charge_item_create_params.OtherChargeItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
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
    ) -> OtherChargeItem:
        """
        Retrieves an other charge item by ID.

        **IMPORTANT:** If you need to fetch multiple specific other charge items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the other charge item to retrieve.

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
            f"/quickbooks-desktop/other-charge-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: other_charge_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: other_charge_item_update_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: other_charge_item_update_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtherChargeItem:
        """
        Updates an existing other charge item.

        Args:
          id: The QuickBooks-assigned unique identifier of the other charge item to update.

          revision_number: The current QuickBooks-assigned revision number of the other charge item object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The other charge item's barcode.

          class_id: The other charge item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          is_active: Indicates whether this other charge item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this other charge item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two other charge items could both have the `name`
              "Overnight Delivery", but they could have unique `fullName` values, such as
              "Shipping Charges:Overnight Delivery" and "Misc Fees:Overnight Delivery".

              Maximum length: 31 characters.

          parent_id: The parent other charge item one level above this one in the hierarchy. For
              example, if this other charge item has a `fullName` of "Shipping
              Charges:Overnight Delivery", its parent has a `fullName` of "Shipping Charges".
              If this other charge item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for other charge items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying an other charge item because an item
              cannot have both configurations.

          sales_or_purchase_details: Details for other charge items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying an other charge item because an item
              cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this other charge item, determining whether it is
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/other-charge-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                other_charge_item_update_params.OtherChargeItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtherChargeItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
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
    ) -> AsyncPaginator[OtherChargeItem, AsyncCursorPage[OtherChargeItem]]:
        """Returns a list of other charge items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for other charge items of these classes. A class is a way end-users can
              categorize other charge items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific other charge items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for an other charge item, formed by
              by combining the names of its parent objects with its own `name`, separated by
              colons. For example, if an other charge item is under "Shipping Charges" and has
              the `name` "Overnight Delivery", its `fullName` would be "Shipping
              Charges:Overnight Delivery".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific other charge items by their QuickBooks-assigned unique
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

          name_contains: Filter for other charge items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for other charge items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for other charge items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for other charge items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for other charge items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for other charge items that are active, inactive, or both.

          updated_after: Filter for other charge items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for other charge items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/other-charge-items",
            page=AsyncCursorPage[OtherChargeItem],
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
                    other_charge_item_list_params.OtherChargeItemListParams,
                ),
            ),
            model=OtherChargeItem,
        )


class OtherChargeItemsResourceWithRawResponse:
    def __init__(self, other_charge_items: OtherChargeItemsResource) -> None:
        self._other_charge_items = other_charge_items

        self.create = to_raw_response_wrapper(
            other_charge_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            other_charge_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            other_charge_items.update,
        )
        self.list = to_raw_response_wrapper(
            other_charge_items.list,
        )


class AsyncOtherChargeItemsResourceWithRawResponse:
    def __init__(self, other_charge_items: AsyncOtherChargeItemsResource) -> None:
        self._other_charge_items = other_charge_items

        self.create = async_to_raw_response_wrapper(
            other_charge_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            other_charge_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            other_charge_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            other_charge_items.list,
        )


class OtherChargeItemsResourceWithStreamingResponse:
    def __init__(self, other_charge_items: OtherChargeItemsResource) -> None:
        self._other_charge_items = other_charge_items

        self.create = to_streamed_response_wrapper(
            other_charge_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            other_charge_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            other_charge_items.update,
        )
        self.list = to_streamed_response_wrapper(
            other_charge_items.list,
        )


class AsyncOtherChargeItemsResourceWithStreamingResponse:
    def __init__(self, other_charge_items: AsyncOtherChargeItemsResource) -> None:
        self._other_charge_items = other_charge_items

        self.create = async_to_streamed_response_wrapper(
            other_charge_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            other_charge_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            other_charge_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            other_charge_items.list,
        )
