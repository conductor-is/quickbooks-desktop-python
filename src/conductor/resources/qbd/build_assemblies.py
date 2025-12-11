# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...types.qbd import build_assembly_list_params, build_assembly_create_params, build_assembly_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.build_assembly import BuildAssembly
from ...types.qbd.build_assembly_delete_response import BuildAssemblyDeleteResponse

__all__ = ["BuildAssembliesResource", "AsyncBuildAssembliesResource"]


class BuildAssembliesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BuildAssembliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return BuildAssembliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuildAssembliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return BuildAssembliesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inventory_assembly_item_id: str,
        quantity_to_build: float,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        expiration_date: Union[str, date] | Omit = omit,
        external_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        inventory_site_location_id: str | Omit = omit,
        lot_number: str | Omit = omit,
        mark_pending_if_required: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildAssembly:
        """
        Creates a build assembly transaction that consumes component quantities and
        increases the finished assembly on hand. If components are short you can mark
        the build as pending instead of failing.

        Args:
          inventory_assembly_item_id: The inventory assembly item associated with this build assembly. An inventory
              assembly item is assembled or manufactured from other inventory items, and the
              items and/or assemblies that make up the assembly are called components.

          quantity_to_build: The number of build assembly to be built. The transaction will fail if the
              number specified here exceeds the number of on-hand components.

          transaction_date: The date of this build assembly, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          expiration_date: The expiration date for the serial number or lot number of the item associated
              with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
              relevant for perishable or time-sensitive inventory items. Note that this field
              is only supported on QuickBooks Desktop 2023 or later.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this build
              assembly is stored.

          inventory_site_location_id: The specific location (e.g., bin or shelf) within the inventory site where the
              item associated with this build assembly is stored.

          lot_number: The lot number of the item associated with this build assembly. Used for
              tracking groups of inventory items that are purchased or manufactured together.

          mark_pending_if_required: When `true`, the build assembly will be marked pending if there are insufficient
              quantities to complete the build assembly.

          memo: A memo or note for this build assembly.

          ref_number: The case-sensitive user-defined reference number for this build assembly, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          serial_number: The serial number of the item associated with this build assembly. This is used
              for tracking individual units of serialized inventory items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/build-assemblies",
            body=maybe_transform(
                {
                    "inventory_assembly_item_id": inventory_assembly_item_id,
                    "quantity_to_build": quantity_to_build,
                    "transaction_date": transaction_date,
                    "expiration_date": expiration_date,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "inventory_site_location_id": inventory_site_location_id,
                    "lot_number": lot_number,
                    "mark_pending_if_required": mark_pending_if_required,
                    "memo": memo,
                    "ref_number": ref_number,
                    "serial_number": serial_number,
                },
                build_assembly_create_params.BuildAssemblyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
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
    ) -> BuildAssembly:
        """
        Retrieves a build assembly by ID.

        **IMPORTANT:** If you need to fetch multiple specific build assemblies by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to retrieve.

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
            f"/quickbooks-desktop/build-assemblies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        expiration_date: Union[str, date] | Omit = omit,
        inventory_site_id: str | Omit = omit,
        inventory_site_location_id: str | Omit = omit,
        lot_number: str | Omit = omit,
        mark_pending_if_required: bool | Omit = omit,
        memo: str | Omit = omit,
        quantity_to_build: float | Omit = omit,
        ref_number: str | Omit = omit,
        remove_pending: bool | Omit = omit,
        serial_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildAssembly:
        """
        Updates an existing build assembly.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to update.

          revision_number: The current QuickBooks-assigned revision number of the build assembly object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          expiration_date: The expiration date for the serial number or lot number of the item associated
              with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
              relevant for perishable or time-sensitive inventory items. Note that this field
              is only supported on QuickBooks Desktop 2023 or later.

          inventory_site_id: The site location where inventory for the item associated with this build
              assembly is stored.

          inventory_site_location_id: The specific location (e.g., bin or shelf) within the inventory site where the
              item associated with this build assembly is stored.

          lot_number: The lot number of the item associated with this build assembly. Used for
              tracking groups of inventory items that are purchased or manufactured together.

          mark_pending_if_required: When `true`, the build assembly will be marked pending if there are insufficient
              quantities to complete the build assembly.

          memo: A memo or note for this build assembly.

          quantity_to_build: The number of build assembly to be built. The transaction will fail if the
              number specified here exceeds the number of on-hand components.

          ref_number: The case-sensitive user-defined reference number for this build assembly, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          remove_pending: When `true`, changes this build assembly's status from pending to non-pending,
              which effectively performs the build transaction. The operation will fail if
              there are insufficient component quantities on hand to complete the build.

          serial_number: The serial number of the item associated with this build assembly. This is used
              for tracking individual units of serialized inventory items.

          transaction_date: The date of this build assembly, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/build-assemblies/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "expiration_date": expiration_date,
                    "inventory_site_id": inventory_site_id,
                    "inventory_site_location_id": inventory_site_location_id,
                    "lot_number": lot_number,
                    "mark_pending_if_required": mark_pending_if_required,
                    "memo": memo,
                    "quantity_to_build": quantity_to_build,
                    "ref_number": ref_number,
                    "remove_pending": remove_pending,
                    "serial_number": serial_number,
                    "transaction_date": transaction_date,
                },
                build_assembly_update_params.BuildAssemblyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_component_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        pending_status: Literal["all", "not_pending", "pending"] | Omit = omit,
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
    ) -> SyncCursorPage[BuildAssembly]:
        """Returns a list of build assemblies.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific build assemblies by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_component_line_items: Whether to include component line items in the response. Defaults to `true`.

          item_ids: Filter for build assemblies containing these items.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          pending_status: Filter for build assemblies that are pending, not pending, or both.

          ref_number_contains: Filter for build assemblies whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for build assemblies whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for build assemblies whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific build assemblies by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for build assemblies whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for build assemblies whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for build assemblies whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for build assemblies whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for build assemblies updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for build assemblies updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/build-assemblies",
            page=SyncCursorPage[BuildAssembly],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "include_component_line_items": include_component_line_items,
                        "item_ids": item_ids,
                        "limit": limit,
                        "pending_status": pending_status,
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
                    build_assembly_list_params.BuildAssemblyListParams,
                ),
            ),
            model=BuildAssembly,
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
    ) -> BuildAssemblyDeleteResponse:
        """Permanently deletes a a build assembly.

        The deletion will fail if the build
        assembly is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to delete.

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
            f"/quickbooks-desktop/build-assemblies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssemblyDeleteResponse,
        )


class AsyncBuildAssembliesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBuildAssembliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBuildAssembliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuildAssembliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncBuildAssembliesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inventory_assembly_item_id: str,
        quantity_to_build: float,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        expiration_date: Union[str, date] | Omit = omit,
        external_id: str | Omit = omit,
        inventory_site_id: str | Omit = omit,
        inventory_site_location_id: str | Omit = omit,
        lot_number: str | Omit = omit,
        mark_pending_if_required: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildAssembly:
        """
        Creates a build assembly transaction that consumes component quantities and
        increases the finished assembly on hand. If components are short you can mark
        the build as pending instead of failing.

        Args:
          inventory_assembly_item_id: The inventory assembly item associated with this build assembly. An inventory
              assembly item is assembled or manufactured from other inventory items, and the
              items and/or assemblies that make up the assembly are called components.

          quantity_to_build: The number of build assembly to be built. The transaction will fail if the
              number specified here exceeds the number of on-hand components.

          transaction_date: The date of this build assembly, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          expiration_date: The expiration date for the serial number or lot number of the item associated
              with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
              relevant for perishable or time-sensitive inventory items. Note that this field
              is only supported on QuickBooks Desktop 2023 or later.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this build
              assembly is stored.

          inventory_site_location_id: The specific location (e.g., bin or shelf) within the inventory site where the
              item associated with this build assembly is stored.

          lot_number: The lot number of the item associated with this build assembly. Used for
              tracking groups of inventory items that are purchased or manufactured together.

          mark_pending_if_required: When `true`, the build assembly will be marked pending if there are insufficient
              quantities to complete the build assembly.

          memo: A memo or note for this build assembly.

          ref_number: The case-sensitive user-defined reference number for this build assembly, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          serial_number: The serial number of the item associated with this build assembly. This is used
              for tracking individual units of serialized inventory items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/build-assemblies",
            body=await async_maybe_transform(
                {
                    "inventory_assembly_item_id": inventory_assembly_item_id,
                    "quantity_to_build": quantity_to_build,
                    "transaction_date": transaction_date,
                    "expiration_date": expiration_date,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "inventory_site_location_id": inventory_site_location_id,
                    "lot_number": lot_number,
                    "mark_pending_if_required": mark_pending_if_required,
                    "memo": memo,
                    "ref_number": ref_number,
                    "serial_number": serial_number,
                },
                build_assembly_create_params.BuildAssemblyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
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
    ) -> BuildAssembly:
        """
        Retrieves a build assembly by ID.

        **IMPORTANT:** If you need to fetch multiple specific build assemblies by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to retrieve.

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
            f"/quickbooks-desktop/build-assemblies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        expiration_date: Union[str, date] | Omit = omit,
        inventory_site_id: str | Omit = omit,
        inventory_site_location_id: str | Omit = omit,
        lot_number: str | Omit = omit,
        mark_pending_if_required: bool | Omit = omit,
        memo: str | Omit = omit,
        quantity_to_build: float | Omit = omit,
        ref_number: str | Omit = omit,
        remove_pending: bool | Omit = omit,
        serial_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuildAssembly:
        """
        Updates an existing build assembly.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to update.

          revision_number: The current QuickBooks-assigned revision number of the build assembly object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          expiration_date: The expiration date for the serial number or lot number of the item associated
              with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
              relevant for perishable or time-sensitive inventory items. Note that this field
              is only supported on QuickBooks Desktop 2023 or later.

          inventory_site_id: The site location where inventory for the item associated with this build
              assembly is stored.

          inventory_site_location_id: The specific location (e.g., bin or shelf) within the inventory site where the
              item associated with this build assembly is stored.

          lot_number: The lot number of the item associated with this build assembly. Used for
              tracking groups of inventory items that are purchased or manufactured together.

          mark_pending_if_required: When `true`, the build assembly will be marked pending if there are insufficient
              quantities to complete the build assembly.

          memo: A memo or note for this build assembly.

          quantity_to_build: The number of build assembly to be built. The transaction will fail if the
              number specified here exceeds the number of on-hand components.

          ref_number: The case-sensitive user-defined reference number for this build assembly, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          remove_pending: When `true`, changes this build assembly's status from pending to non-pending,
              which effectively performs the build transaction. The operation will fail if
              there are insufficient component quantities on hand to complete the build.

          serial_number: The serial number of the item associated with this build assembly. This is used
              for tracking individual units of serialized inventory items.

          transaction_date: The date of this build assembly, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/build-assemblies/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "expiration_date": expiration_date,
                    "inventory_site_id": inventory_site_id,
                    "inventory_site_location_id": inventory_site_location_id,
                    "lot_number": lot_number,
                    "mark_pending_if_required": mark_pending_if_required,
                    "memo": memo,
                    "quantity_to_build": quantity_to_build,
                    "ref_number": ref_number,
                    "remove_pending": remove_pending,
                    "serial_number": serial_number,
                    "transaction_date": transaction_date,
                },
                build_assembly_update_params.BuildAssemblyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssembly,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_component_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        pending_status: Literal["all", "not_pending", "pending"] | Omit = omit,
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
    ) -> AsyncPaginator[BuildAssembly, AsyncCursorPage[BuildAssembly]]:
        """Returns a list of build assemblies.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific build assemblies by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_component_line_items: Whether to include component line items in the response. Defaults to `true`.

          item_ids: Filter for build assemblies containing these items.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          pending_status: Filter for build assemblies that are pending, not pending, or both.

          ref_number_contains: Filter for build assemblies whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for build assemblies whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for build assemblies whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific build assemblies by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for build assemblies whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for build assemblies whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for build assemblies whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for build assemblies whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for build assemblies updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for build assemblies updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/build-assemblies",
            page=AsyncCursorPage[BuildAssembly],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "include_component_line_items": include_component_line_items,
                        "item_ids": item_ids,
                        "limit": limit,
                        "pending_status": pending_status,
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
                    build_assembly_list_params.BuildAssemblyListParams,
                ),
            ),
            model=BuildAssembly,
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
    ) -> BuildAssemblyDeleteResponse:
        """Permanently deletes a a build assembly.

        The deletion will fail if the build
        assembly is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the build assembly to delete.

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
            f"/quickbooks-desktop/build-assemblies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuildAssemblyDeleteResponse,
        )


class BuildAssembliesResourceWithRawResponse:
    def __init__(self, build_assemblies: BuildAssembliesResource) -> None:
        self._build_assemblies = build_assemblies

        self.create = to_raw_response_wrapper(
            build_assemblies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            build_assemblies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            build_assemblies.update,
        )
        self.list = to_raw_response_wrapper(
            build_assemblies.list,
        )
        self.delete = to_raw_response_wrapper(
            build_assemblies.delete,
        )


class AsyncBuildAssembliesResourceWithRawResponse:
    def __init__(self, build_assemblies: AsyncBuildAssembliesResource) -> None:
        self._build_assemblies = build_assemblies

        self.create = async_to_raw_response_wrapper(
            build_assemblies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            build_assemblies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            build_assemblies.update,
        )
        self.list = async_to_raw_response_wrapper(
            build_assemblies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            build_assemblies.delete,
        )


class BuildAssembliesResourceWithStreamingResponse:
    def __init__(self, build_assemblies: BuildAssembliesResource) -> None:
        self._build_assemblies = build_assemblies

        self.create = to_streamed_response_wrapper(
            build_assemblies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            build_assemblies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            build_assemblies.update,
        )
        self.list = to_streamed_response_wrapper(
            build_assemblies.list,
        )
        self.delete = to_streamed_response_wrapper(
            build_assemblies.delete,
        )


class AsyncBuildAssembliesResourceWithStreamingResponse:
    def __init__(self, build_assemblies: AsyncBuildAssembliesResource) -> None:
        self._build_assemblies = build_assemblies

        self.create = async_to_streamed_response_wrapper(
            build_assemblies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            build_assemblies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            build_assemblies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            build_assemblies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            build_assemblies.delete,
        )
