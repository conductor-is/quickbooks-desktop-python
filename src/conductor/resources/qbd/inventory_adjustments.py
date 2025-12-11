# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

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
    inventory_adjustment_list_params,
    inventory_adjustment_create_params,
    inventory_adjustment_update_params,
)
from ..._base_client import make_request_options
from ...types.qbd.inventory_adjustment import InventoryAdjustment
from ...types.qbd.inventory_adjustment_list_response import InventoryAdjustmentListResponse
from ...types.qbd.inventory_adjustment_delete_response import InventoryAdjustmentDeleteResponse

__all__ = ["InventoryAdjustmentsResource", "AsyncInventoryAdjustmentsResource"]


class InventoryAdjustmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventoryAdjustmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return InventoryAdjustmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoryAdjustmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return InventoryAdjustmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        external_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        lines: Iterable[inventory_adjustment_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustment:
        """
        Creates an inventory adjustment to correct on-hand quantities or values.
        QuickBooks requires single-user mode unless you're on Enterprise with Advanced
        Inventory enabled.

        Args:
          account_id: The account to which this inventory adjustment is posted for tracking inventory
              value changes.

          transaction_date: The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          class_id: The inventory adjustment's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this inventory adjustment's line items unless overridden
              at the line item level.

          customer_id: The customer or customer-job associated with this inventory adjustment.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this inventory
              adjustment is stored.

          lines: The inventory adjustment's item lines, each representing the adjustment of an
              inventory item's quantity, value, serial number, or lot number.

          memo: A memo or note for this inventory adjustment.

          ref_number: The case-sensitive user-defined reference number for this inventory adjustment,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/inventory-adjustments",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "lines": lines,
                    "memo": memo,
                    "ref_number": ref_number,
                },
                inventory_adjustment_create_params.InventoryAdjustmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
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
    ) -> InventoryAdjustment:
        """
        Retrieves an inventory adjustment by ID.

        **IMPORTANT:** If you need to fetch multiple specific inventory adjustments by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to
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
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        lines: Iterable[inventory_adjustment_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustment:
        """
        Updates an existing inventory adjustment.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory adjustment
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_id: The account to which this inventory adjustment is posted for tracking inventory
              value changes.

          class_id: The inventory adjustment's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this inventory adjustment's line items unless overridden
              at the line item level.

          customer_id: The customer or customer-job associated with this inventory adjustment.

          inventory_site_id: The site location where inventory for the item associated with this inventory
              adjustment is stored.

          lines: The inventory adjustment's item lines, each representing the adjustment of an
              inventory item's quantity, value, serial number, or lot number.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the inventory adjustment with this array. To keep any existing
                 item lines, you must include them in this array even if they have not
                 changed. **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this inventory adjustment.

          ref_number: The case-sensitive user-defined reference number for this inventory adjustment,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          transaction_date: The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "inventory_site_id": inventory_site_id,
                    "lines": lines,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                inventory_adjustment_update_params.InventoryAdjustmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        ref_number_contains: str | Omit = omit,
        ref_number_ends_with: str | Omit = omit,
        ref_number_from: str | Omit = omit,
        ref_numbers: SequenceNotStr[str] | Omit = omit,
        ref_number_starts_with: str | Omit = omit,
        ref_number_to: str | Omit = omit,
        transaction_date_from: Union[str, date] | Omit = omit,
        transaction_date_to: Union[str, date] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustmentListResponse:
        """Returns a list of inventory adjustments.

        NOTE: QuickBooks Desktop does not
        support pagination for inventory adjustments; hence, there is no `cursor`
        parameter. Users typically have few inventory adjustments.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for inventory adjustments associated with these accounts.

          customer_ids: Filter for inventory adjustments associated with these customers.

          ids: Filter for specific inventory adjustments by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          item_ids: Filter for inventory adjustments containing these inventory items.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              inventory adjustments. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all inventory adjustments
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because inventory adjustments typically have low record counts.

          ref_number_contains: Filter for inventory adjustments whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for inventory adjustments whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for inventory adjustments whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific inventory adjustments by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for inventory adjustments whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for inventory adjustments whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for inventory adjustments whose `date` field is on or after this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for inventory adjustments whose `date` field is on or before this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for inventory adjustments updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for inventory adjustments updated on or before this date/time. Accepts
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
            "/quickbooks-desktop/inventory-adjustments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "customer_ids": customer_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "item_ids": item_ids,
                        "limit": limit,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    inventory_adjustment_list_params.InventoryAdjustmentListParams,
                ),
            ),
            cast_to=InventoryAdjustmentListResponse,
        )

    def delete(
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
    ) -> InventoryAdjustmentDeleteResponse:
        """Permanently deletes a an inventory adjustment.

        The deletion will fail if the
        inventory adjustment is currently in use or has any linked transactions that are
        in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to delete.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._delete(
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustmentDeleteResponse,
        )


class AsyncInventoryAdjustmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventoryAdjustmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoryAdjustmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoryAdjustmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncInventoryAdjustmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        external_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        lines: Iterable[inventory_adjustment_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustment:
        """
        Creates an inventory adjustment to correct on-hand quantities or values.
        QuickBooks requires single-user mode unless you're on Enterprise with Advanced
        Inventory enabled.

        Args:
          account_id: The account to which this inventory adjustment is posted for tracking inventory
              value changes.

          transaction_date: The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          class_id: The inventory adjustment's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this inventory adjustment's line items unless overridden
              at the line item level.

          customer_id: The customer or customer-job associated with this inventory adjustment.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this inventory
              adjustment is stored.

          lines: The inventory adjustment's item lines, each representing the adjustment of an
              inventory item's quantity, value, serial number, or lot number.

          memo: A memo or note for this inventory adjustment.

          ref_number: The case-sensitive user-defined reference number for this inventory adjustment,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/inventory-adjustments",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "lines": lines,
                    "memo": memo,
                    "ref_number": ref_number,
                },
                inventory_adjustment_create_params.InventoryAdjustmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
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
    ) -> InventoryAdjustment:
        """
        Retrieves an inventory adjustment by ID.

        **IMPORTANT:** If you need to fetch multiple specific inventory adjustments by
        ID, use the list endpoint instead with the `ids` parameter. It accepts an array
        of IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to
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
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        lines: Iterable[inventory_adjustment_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustment:
        """
        Updates an existing inventory adjustment.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory adjustment
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          account_id: The account to which this inventory adjustment is posted for tracking inventory
              value changes.

          class_id: The inventory adjustment's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this inventory adjustment's line items unless overridden
              at the line item level.

          customer_id: The customer or customer-job associated with this inventory adjustment.

          inventory_site_id: The site location where inventory for the item associated with this inventory
              adjustment is stored.

          lines: The inventory adjustment's item lines, each representing the adjustment of an
              inventory item's quantity, value, serial number, or lot number.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the inventory adjustment with this array. To keep any existing
                 item lines, you must include them in this array even if they have not
                 changed. **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this inventory adjustment.

          ref_number: The case-sensitive user-defined reference number for this inventory adjustment,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          transaction_date: The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "inventory_site_id": inventory_site_id,
                    "lines": lines,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                inventory_adjustment_update_params.InventoryAdjustmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustment,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        ref_number_contains: str | Omit = omit,
        ref_number_ends_with: str | Omit = omit,
        ref_number_from: str | Omit = omit,
        ref_numbers: SequenceNotStr[str] | Omit = omit,
        ref_number_starts_with: str | Omit = omit,
        ref_number_to: str | Omit = omit,
        transaction_date_from: Union[str, date] | Omit = omit,
        transaction_date_to: Union[str, date] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InventoryAdjustmentListResponse:
        """Returns a list of inventory adjustments.

        NOTE: QuickBooks Desktop does not
        support pagination for inventory adjustments; hence, there is no `cursor`
        parameter. Users typically have few inventory adjustments.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for inventory adjustments associated with these accounts.

          customer_ids: Filter for inventory adjustments associated with these customers.

          ids: Filter for specific inventory adjustments by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          item_ids: Filter for inventory adjustments containing these inventory items.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              inventory adjustments. This parameter will limit the response size, but you
              cannot fetch subsequent results using a cursor. For pagination, use the
              name-range parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all inventory adjustments
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because inventory adjustments typically have low record counts.

          ref_number_contains: Filter for inventory adjustments whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for inventory adjustments whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for inventory adjustments whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific inventory adjustments by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for inventory adjustments whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for inventory adjustments whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for inventory adjustments whose `date` field is on or after this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for inventory adjustments whose `date` field is on or before this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for inventory adjustments updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for inventory adjustments updated on or before this date/time. Accepts
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
            "/quickbooks-desktop/inventory-adjustments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_ids": account_ids,
                        "customer_ids": customer_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "item_ids": item_ids,
                        "limit": limit,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    inventory_adjustment_list_params.InventoryAdjustmentListParams,
                ),
            ),
            cast_to=InventoryAdjustmentListResponse,
        )

    async def delete(
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
    ) -> InventoryAdjustmentDeleteResponse:
        """Permanently deletes a an inventory adjustment.

        The deletion will fail if the
        inventory adjustment is currently in use or has any linked transactions that are
        in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory adjustment to delete.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._delete(
            f"/quickbooks-desktop/inventory-adjustments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryAdjustmentDeleteResponse,
        )


class InventoryAdjustmentsResourceWithRawResponse:
    def __init__(self, inventory_adjustments: InventoryAdjustmentsResource) -> None:
        self._inventory_adjustments = inventory_adjustments

        self.create = to_raw_response_wrapper(
            inventory_adjustments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inventory_adjustments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            inventory_adjustments.update,
        )
        self.list = to_raw_response_wrapper(
            inventory_adjustments.list,
        )
        self.delete = to_raw_response_wrapper(
            inventory_adjustments.delete,
        )


class AsyncInventoryAdjustmentsResourceWithRawResponse:
    def __init__(self, inventory_adjustments: AsyncInventoryAdjustmentsResource) -> None:
        self._inventory_adjustments = inventory_adjustments

        self.create = async_to_raw_response_wrapper(
            inventory_adjustments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inventory_adjustments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            inventory_adjustments.update,
        )
        self.list = async_to_raw_response_wrapper(
            inventory_adjustments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            inventory_adjustments.delete,
        )


class InventoryAdjustmentsResourceWithStreamingResponse:
    def __init__(self, inventory_adjustments: InventoryAdjustmentsResource) -> None:
        self._inventory_adjustments = inventory_adjustments

        self.create = to_streamed_response_wrapper(
            inventory_adjustments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inventory_adjustments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            inventory_adjustments.update,
        )
        self.list = to_streamed_response_wrapper(
            inventory_adjustments.list,
        )
        self.delete = to_streamed_response_wrapper(
            inventory_adjustments.delete,
        )


class AsyncInventoryAdjustmentsResourceWithStreamingResponse:
    def __init__(self, inventory_adjustments: AsyncInventoryAdjustmentsResource) -> None:
        self._inventory_adjustments = inventory_adjustments

        self.create = async_to_streamed_response_wrapper(
            inventory_adjustments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inventory_adjustments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            inventory_adjustments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            inventory_adjustments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            inventory_adjustments.delete,
        )
