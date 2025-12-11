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
    non_inventory_item_list_params,
    non_inventory_item_create_params,
    non_inventory_item_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.non_inventory_item import NonInventoryItem

__all__ = ["NonInventoryItemsResource", "AsyncNonInventoryItemsResource"]


class NonInventoryItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NonInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return NonInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NonInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return NonInventoryItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: non_inventory_item_create_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: non_inventory_item_create_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sku: str | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NonInventoryItem:
        """
        Creates a new non-inventory item.

        Args:
          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its hierarchical parent objects
              like `fullName` does. For example, two non-inventory items could both have the
              `name` "Printer Ink Cartridge", but they could have unique `fullName` values,
              such as "Office Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating a non-inventory item, but never both
              because an item cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating a non-inventory item, but never both
              because an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this non-inventory item, determining whether it
              is taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The non-inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/non-inventory-items",
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
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_create_params.NonInventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> NonInventoryItem:
        """
        Retrieves a non-inventory item by ID.

        **IMPORTANT:** If you need to fetch multiple specific non-inventory items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to retrieve.

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
            f"/quickbooks-desktop/non-inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        force_unit_of_measure_change: bool | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: non_inventory_item_update_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: non_inventory_item_update_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sku: str | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NonInventoryItem:
        """Updates a non-inventory item.

        You can modify either `salesOrPurchaseDetails` or
        `salesAndPurchaseDetails`, but the item must keep the same configuration it was
        created with. When you change `postingAccount`, `incomeAccount`, or
        `expenseAccount`, include the matching `updateExistingTransactions...` flag so
        QuickBooks applies the new account to existing transactions and doesn’t reject
        the update when historical activity is present.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to update.

          revision_number: The current QuickBooks-assigned revision number of the non-inventory item object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the non-inventory item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its hierarchical parent objects
              like `fullName` does. For example, two non-inventory items could both have the
              `name` "Printer Ink Cartridge", but they could have unique `fullName` values,
              such as "Office Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

              Maximum length: 31 characters.

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying a non-inventory item because an item
              cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying a non-inventory item because an item
              cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this non-inventory item, determining whether it
              is taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The non-inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/non-inventory-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_update_params.NonInventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> SyncCursorPage[NonInventoryItem]:
        """Returns a list of non-inventory items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for non-inventory items of these classes. A class is a way end-users can
              categorize non-inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific non-inventory items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for a non-inventory item, formed by
              by combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a non-inventory item is under "Office Supplies" and has
              the `name` "Printer Ink Cartridge", its `fullName` would be "Office
              Supplies:Printer Ink Cartridge".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific non-inventory items by their QuickBooks-assigned unique
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

          name_contains: Filter for non-inventory items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for non-inventory items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for non-inventory items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for non-inventory items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for non-inventory items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for non-inventory items that are active, inactive, or both.

          updated_after: Filter for non-inventory items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for non-inventory items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/non-inventory-items",
            page=SyncCursorPage[NonInventoryItem],
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
                    non_inventory_item_list_params.NonInventoryItemListParams,
                ),
            ),
            model=NonInventoryItem,
        )


class AsyncNonInventoryItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNonInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNonInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNonInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncNonInventoryItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_create_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        external_id: str | Omit = omit,
        is_active: bool | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: non_inventory_item_create_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: non_inventory_item_create_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sku: str | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NonInventoryItem:
        """
        Creates a new non-inventory item.

        Args:
          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its hierarchical parent objects
              like `fullName` does. For example, two non-inventory items could both have the
              `name` "Printer Ink Cartridge", but they could have unique `fullName` values,
              such as "Office Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating a non-inventory item, but never both
              because an item cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating a non-inventory item, but never both
              because an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this non-inventory item, determining whether it
              is taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The non-inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/non-inventory-items",
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
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_create_params.NonInventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> NonInventoryItem:
        """
        Retrieves a non-inventory item by ID.

        **IMPORTANT:** If you need to fetch multiple specific non-inventory items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to retrieve.

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
            f"/quickbooks-desktop/non-inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_update_params.Barcode | Omit = omit,
        class_id: str | Omit = omit,
        force_unit_of_measure_change: bool | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        sales_and_purchase_details: non_inventory_item_update_params.SalesAndPurchaseDetails | Omit = omit,
        sales_or_purchase_details: non_inventory_item_update_params.SalesOrPurchaseDetails | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sku: str | Omit = omit,
        unit_of_measure_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NonInventoryItem:
        """Updates a non-inventory item.

        You can modify either `salesOrPurchaseDetails` or
        `salesAndPurchaseDetails`, but the item must keep the same configuration it was
        created with. When you change `postingAccount`, `incomeAccount`, or
        `expenseAccount`, include the matching `updateExistingTransactions...` flag so
        QuickBooks applies the new account to existing transactions and doesn’t reject
        the update when historical activity is present.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to update.

          revision_number: The current QuickBooks-assigned revision number of the non-inventory item object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the non-inventory item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its hierarchical parent objects
              like `fullName` does. For example, two non-inventory items could both have the
              `name` "Printer Ink Cartridge", but they could have unique `fullName` values,
              such as "Office Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

              Maximum length: 31 characters.

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying a non-inventory item because an item
              cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying a non-inventory item because an item
              cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this non-inventory item, determining whether it
              is taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The non-inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/non-inventory-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_update_params.NonInventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> AsyncPaginator[NonInventoryItem, AsyncCursorPage[NonInventoryItem]]:
        """Returns a list of non-inventory items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          class_ids: Filter for non-inventory items of these classes. A class is a way end-users can
              categorize non-inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific non-inventory items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for a non-inventory item, formed by
              by combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a non-inventory item is under "Office Supplies" and has
              the `name` "Printer Ink Cartridge", its `fullName` would be "Office
              Supplies:Printer Ink Cartridge".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ids: Filter for specific non-inventory items by their QuickBooks-assigned unique
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

          name_contains: Filter for non-inventory items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for non-inventory items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for non-inventory items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for non-inventory items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for non-inventory items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for non-inventory items that are active, inactive, or both.

          updated_after: Filter for non-inventory items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for non-inventory items updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/non-inventory-items",
            page=AsyncCursorPage[NonInventoryItem],
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
                    non_inventory_item_list_params.NonInventoryItemListParams,
                ),
            ),
            model=NonInventoryItem,
        )


class NonInventoryItemsResourceWithRawResponse:
    def __init__(self, non_inventory_items: NonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = to_raw_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            non_inventory_items.update,
        )
        self.list = to_raw_response_wrapper(
            non_inventory_items.list,
        )


class AsyncNonInventoryItemsResourceWithRawResponse:
    def __init__(self, non_inventory_items: AsyncNonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = async_to_raw_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            non_inventory_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            non_inventory_items.list,
        )


class NonInventoryItemsResourceWithStreamingResponse:
    def __init__(self, non_inventory_items: NonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = to_streamed_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            non_inventory_items.update,
        )
        self.list = to_streamed_response_wrapper(
            non_inventory_items.list,
        )


class AsyncNonInventoryItemsResourceWithStreamingResponse:
    def __init__(self, non_inventory_items: AsyncNonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = async_to_streamed_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            non_inventory_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            non_inventory_items.list,
        )
