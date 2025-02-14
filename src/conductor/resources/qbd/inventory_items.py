# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
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
from ...types.qbd import inventory_item_list_params, inventory_item_create_params, inventory_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.inventory_item import InventoryItem

__all__ = ["InventoryItemsResource", "AsyncInventoryItemsResource"]


class InventoryItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return InventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return InventoryItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        asset_account_id: str,
        cogs_account_id: str,
        income_account_id: str,
        name: str,
        conductor_end_user_id: str,
        barcode: inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inventory_date: Union[str, date] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        maximum_quantity_on_hand: float | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        quantity_on_hand: float | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sku: str | NotGiven = NOT_GIVEN,
        total_value: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Creates a new inventory item.

        Args:
          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          income_account_id: The income account used to track revenue from sales of this inventory item.

          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two inventory items could both have the `name`
              "Cabinet", but they could have unique `fullName` values, such as
              "Kitchen:Cabinet" and "Inventory:Cabinet".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_date: The date when this inventory item was converted into an inventory item from some
              other type of item, in ISO 8601 format (YYYY-MM-DD).

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          maximum_quantity_on_hand: The maximum quantity of this inventory item desired in inventory.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
              parent has a `fullName` of "Kitchen". If this inventory item is at the top
              level, this field will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when it is ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          quantity_on_hand: The current quantity of this inventory item available in inventory. To change
              the `quantityOnHand` for an inventory item, you must create an
              inventory-adjustment instead of updating this inventory item directly.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The default sales-tax code for this inventory item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          total_value: The total value of this inventory item. If `totalValue` is provided,
              `quantityOnHand` must also be provided and must be greater than zero. If both
              `quantityOnHand` and `purchaseCost` are provided, then `totalValue` will be set
              to `quantityOnHand` times `purchaseCost`, regardless of what `totalValue` is
              explicitly set to.

          unit_of_measure_set_id: The unit-of-measure set associated with this inventory item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/inventory-items",
            body=maybe_transform(
                {
                    "asset_account_id": asset_account_id,
                    "cogs_account_id": cogs_account_id,
                    "income_account_id": income_account_id,
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "inventory_date": inventory_date,
                    "is_active": is_active,
                    "maximum_quantity_on_hand": maximum_quantity_on_hand,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "quantity_on_hand": quantity_on_hand,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "total_value": total_value,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                inventory_item_create_params.InventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> InventoryItem:
        """
        Retrieves an inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to retrieve.

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
            f"/quickbooks-desktop/inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        asset_account_id: str | NotGiven = NOT_GIVEN,
        barcode: inventory_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        cogs_account_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        income_account_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        maximum_quantity_on_hand: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sku: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        update_existing_transactions_cogs_account: bool | NotGiven = NOT_GIVEN,
        update_existing_transactions_income_account: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Updates an existing inventory item.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          force_unit_of_measure_change: Indicates whether to allow changing the inventory item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          income_account_id: The income account used to track revenue from sales of this inventory item.

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          maximum_quantity_on_hand: The maximum quantity of this inventory item desired in inventory.

          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two inventory items could both have the `name`
              "Cabinet", but they could have unique `fullName` values, such as
              "Kitchen:Cabinet" and "Inventory:Cabinet".

              Maximum length: 31 characters.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
              parent has a `fullName` of "Kitchen". If this inventory item is at the top
              level, this field will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when it is ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The default sales-tax code for this inventory item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this inventory item, which consists of a
              base unit and related units.

          update_existing_transactions_cogs_account: When `true`, applies the new COGS account (specified by the `cogsAccountId`
              field) to all existing transactions that use this inventory item. This updates
              historical data and should be used with caution. The update will fail if any
              affected transaction falls within a closed accounting period. If this parameter
              is not specified, QuickBooks will prompt the user before making any changes.

          update_existing_transactions_income_account: When `true`, applies the new income account (specified by the `incomeAccountId`
              field) to all existing transactions that use this inventory item. This updates
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
            f"/quickbooks-desktop/inventory-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "asset_account_id": asset_account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "cogs_account_id": cogs_account_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "income_account_id": income_account_id,
                    "is_active": is_active,
                    "maximum_quantity_on_hand": maximum_quantity_on_hand,
                    "name": name,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                    "update_existing_transactions_cogs_account": update_existing_transactions_cogs_account,
                    "update_existing_transactions_income_account": update_existing_transactions_income_account,
                },
                inventory_item_update_params.InventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> SyncCursorPage[InventoryItem]:
        """Returns a list of inventory items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory items of these classes. A class is a way end-users can
              categorize inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific inventory items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for an inventory item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if an inventory item is under "Kitchen" and has the `name`
              "Cabinet", its `fullName` would be "Kitchen:Cabinet".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific inventory items by their QuickBooks-assigned unique
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

          name_contains: Filter for inventory items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for inventory items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for inventory items whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for inventory items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for inventory items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for inventory items that are active, inactive, or both.

          updated_after: Filter for inventory items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

              **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedAfter`
              parameter may not correctly filter inventory items by their updated dates. To
              accurately retrieve the desired inventory items, we recommend avoiding this
              parameter and instead fetching a broader dataset, then filtering the results
              locally using the `updatedAt` property.

          updated_before: Filter for inventory items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

              **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedBefore`
              parameter may not correctly filter inventory items by their updated dates. To
              accurately retrieve the desired inventory items, we recommend avoiding this
              parameter and instead fetching a broader dataset, then filtering the results
              locally using the `updatedAt` property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/inventory-items",
            page=SyncCursorPage[InventoryItem],
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
                    inventory_item_list_params.InventoryItemListParams,
                ),
            ),
            model=InventoryItem,
        )


class AsyncInventoryItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncInventoryItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        asset_account_id: str,
        cogs_account_id: str,
        income_account_id: str,
        name: str,
        conductor_end_user_id: str,
        barcode: inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inventory_date: Union[str, date] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        maximum_quantity_on_hand: float | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        quantity_on_hand: float | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sku: str | NotGiven = NOT_GIVEN,
        total_value: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Creates a new inventory item.

        Args:
          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          income_account_id: The income account used to track revenue from sales of this inventory item.

          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two inventory items could both have the `name`
              "Cabinet", but they could have unique `fullName` values, such as
              "Kitchen:Cabinet" and "Inventory:Cabinet".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_date: The date when this inventory item was converted into an inventory item from some
              other type of item, in ISO 8601 format (YYYY-MM-DD).

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          maximum_quantity_on_hand: The maximum quantity of this inventory item desired in inventory.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
              parent has a `fullName` of "Kitchen". If this inventory item is at the top
              level, this field will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when it is ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          quantity_on_hand: The current quantity of this inventory item available in inventory. To change
              the `quantityOnHand` for an inventory item, you must create an
              inventory-adjustment instead of updating this inventory item directly.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The default sales-tax code for this inventory item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          total_value: The total value of this inventory item. If `totalValue` is provided,
              `quantityOnHand` must also be provided and must be greater than zero. If both
              `quantityOnHand` and `purchaseCost` are provided, then `totalValue` will be set
              to `quantityOnHand` times `purchaseCost`, regardless of what `totalValue` is
              explicitly set to.

          unit_of_measure_set_id: The unit-of-measure set associated with this inventory item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/inventory-items",
            body=await async_maybe_transform(
                {
                    "asset_account_id": asset_account_id,
                    "cogs_account_id": cogs_account_id,
                    "income_account_id": income_account_id,
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "inventory_date": inventory_date,
                    "is_active": is_active,
                    "maximum_quantity_on_hand": maximum_quantity_on_hand,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "quantity_on_hand": quantity_on_hand,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "total_value": total_value,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                inventory_item_create_params.InventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> InventoryItem:
        """
        Retrieves an inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to retrieve.

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
            f"/quickbooks-desktop/inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        asset_account_id: str | NotGiven = NOT_GIVEN,
        barcode: inventory_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        cogs_account_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        income_account_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        maximum_quantity_on_hand: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sku: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        update_existing_transactions_cogs_account: bool | NotGiven = NOT_GIVEN,
        update_existing_transactions_income_account: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Updates an existing inventory item.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          force_unit_of_measure_change: Indicates whether to allow changing the inventory item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          income_account_id: The income account used to track revenue from sales of this inventory item.

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          maximum_quantity_on_hand: The maximum quantity of this inventory item desired in inventory.

          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two inventory items could both have the `name`
              "Cabinet", but they could have unique `fullName` values, such as
              "Kitchen:Cabinet" and "Inventory:Cabinet".

              Maximum length: 31 characters.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
              parent has a `fullName` of "Kitchen". If this inventory item is at the top
              level, this field will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when it is ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The default sales-tax code for this inventory item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sku: The inventory item's stock keeping unit (SKU), which is sometimes the
              manufacturer's part number.

          unit_of_measure_set_id: The unit-of-measure set associated with this inventory item, which consists of a
              base unit and related units.

          update_existing_transactions_cogs_account: When `true`, applies the new COGS account (specified by the `cogsAccountId`
              field) to all existing transactions that use this inventory item. This updates
              historical data and should be used with caution. The update will fail if any
              affected transaction falls within a closed accounting period. If this parameter
              is not specified, QuickBooks will prompt the user before making any changes.

          update_existing_transactions_income_account: When `true`, applies the new income account (specified by the `incomeAccountId`
              field) to all existing transactions that use this inventory item. This updates
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
            f"/quickbooks-desktop/inventory-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "asset_account_id": asset_account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "cogs_account_id": cogs_account_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "income_account_id": income_account_id,
                    "is_active": is_active,
                    "maximum_quantity_on_hand": maximum_quantity_on_hand,
                    "name": name,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sku": sku,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                    "update_existing_transactions_cogs_account": update_existing_transactions_cogs_account,
                    "update_existing_transactions_income_account": update_existing_transactions_income_account,
                },
                inventory_item_update_params.InventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> AsyncPaginator[InventoryItem, AsyncCursorPage[InventoryItem]]:
        """Returns a list of inventory items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory items of these classes. A class is a way end-users can
              categorize inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific inventory items by their full-name(s), case-insensitive.
              Like `id`, `fullName` is a unique identifier for an inventory item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if an inventory item is under "Kitchen" and has the `name`
              "Cabinet", its `fullName` would be "Kitchen:Cabinet".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific inventory items by their QuickBooks-assigned unique
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

          name_contains: Filter for inventory items whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for inventory items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for inventory items whose `name` is alphabetically greater than or equal
              to this value.

          name_starts_with: Filter for inventory items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for inventory items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for inventory items that are active, inactive, or both.

          updated_after: Filter for inventory items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

              **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedAfter`
              parameter may not correctly filter inventory items by their updated dates. To
              accurately retrieve the desired inventory items, we recommend avoiding this
              parameter and instead fetching a broader dataset, then filtering the results
              locally using the `updatedAt` property.

          updated_before: Filter for inventory items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

              **WARNING**: Due to a known issue in QuickBooks Desktop, the `updatedBefore`
              parameter may not correctly filter inventory items by their updated dates. To
              accurately retrieve the desired inventory items, we recommend avoiding this
              parameter and instead fetching a broader dataset, then filtering the results
              locally using the `updatedAt` property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/inventory-items",
            page=AsyncCursorPage[InventoryItem],
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
                    inventory_item_list_params.InventoryItemListParams,
                ),
            ),
            model=InventoryItem,
        )


class InventoryItemsResourceWithRawResponse:
    def __init__(self, inventory_items: InventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = to_raw_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            inventory_items.update,
        )
        self.list = to_raw_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithRawResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = async_to_raw_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            inventory_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            inventory_items.list,
        )


class InventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: InventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = to_streamed_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            inventory_items.update,
        )
        self.list = to_streamed_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = async_to_streamed_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            inventory_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            inventory_items.list,
        )
