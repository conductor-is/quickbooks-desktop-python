# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import deleted_list_object_list_params
from ..._base_client import make_request_options
from ...types.qbd.deleted_list_object_list_response import DeletedListObjectListResponse

__all__ = ["DeletedListObjectsResource", "AsyncDeletedListObjectsResource"]


class DeletedListObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeletedListObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return DeletedListObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletedListObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return DeletedListObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        object_types: List[
            Literal[
                "account",
                "billing_rate",
                "class",
                "currency",
                "customer",
                "customer_message",
                "customer_type",
                "date_driven_terms",
                "employee",
                "inventory_site",
                "item_discount",
                "item_fixed_asset",
                "item_group",
                "item_inventory",
                "item_inventory_assembly",
                "item_non_inventory",
                "item_other_charge",
                "item_payment",
                "item_sales_tax",
                "item_sales_tax_group",
                "item_service",
                "item_subtotal",
                "job_type",
                "other_name",
                "payment_method",
                "payroll_item_non_wage",
                "payroll_item_wage",
                "price_level",
                "sales_representative",
                "sales_tax_code",
                "ship_method",
                "standard_terms",
                "to_do",
                "unit_of_measure_set",
                "vehicle",
                "vendor",
                "vendor_type",
                "workers_comp_code",
            ]
        ],
        conductor_end_user_id: str,
        deleted_after: str | Omit = omit,
        deleted_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedListObjectListResponse:
        """
        Lists deleted non-transaction list-objects (e.g., customers, vendors, employees,
        items) from the last 90 days. Results are grouped by list-object type and
        ordered by actual delete time (ascending). For deleted transactions (e.g.,
        invoices, bills, estimates), see the deleted-transactions endpoint.

        Args:
          object_types: Filter for deleted list-objects by their list-object type(s).

          conductor_end_user_id: The ID of the End-User to receive this request.

          deleted_after: Filter for deleted list-objects deleted on or after this date/time, within the
              last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          deleted_before: Filter for deleted list-objects deleted on or before this date/time, within the
              last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

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
            "/quickbooks-desktop/deleted-list-objects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "object_types": object_types,
                        "deleted_after": deleted_after,
                        "deleted_before": deleted_before,
                    },
                    deleted_list_object_list_params.DeletedListObjectListParams,
                ),
            ),
            cast_to=DeletedListObjectListResponse,
        )


class AsyncDeletedListObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeletedListObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeletedListObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletedListObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncDeletedListObjectsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        object_types: List[
            Literal[
                "account",
                "billing_rate",
                "class",
                "currency",
                "customer",
                "customer_message",
                "customer_type",
                "date_driven_terms",
                "employee",
                "inventory_site",
                "item_discount",
                "item_fixed_asset",
                "item_group",
                "item_inventory",
                "item_inventory_assembly",
                "item_non_inventory",
                "item_other_charge",
                "item_payment",
                "item_sales_tax",
                "item_sales_tax_group",
                "item_service",
                "item_subtotal",
                "job_type",
                "other_name",
                "payment_method",
                "payroll_item_non_wage",
                "payroll_item_wage",
                "price_level",
                "sales_representative",
                "sales_tax_code",
                "ship_method",
                "standard_terms",
                "to_do",
                "unit_of_measure_set",
                "vehicle",
                "vendor",
                "vendor_type",
                "workers_comp_code",
            ]
        ],
        conductor_end_user_id: str,
        deleted_after: str | Omit = omit,
        deleted_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedListObjectListResponse:
        """
        Lists deleted non-transaction list-objects (e.g., customers, vendors, employees,
        items) from the last 90 days. Results are grouped by list-object type and
        ordered by actual delete time (ascending). For deleted transactions (e.g.,
        invoices, bills, estimates), see the deleted-transactions endpoint.

        Args:
          object_types: Filter for deleted list-objects by their list-object type(s).

          conductor_end_user_id: The ID of the End-User to receive this request.

          deleted_after: Filter for deleted list-objects deleted on or after this date/time, within the
              last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          deleted_before: Filter for deleted list-objects deleted on or before this date/time, within the
              last 90 days (QuickBooks limit). Accepts the following ISO 8601 formats:

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
            "/quickbooks-desktop/deleted-list-objects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "object_types": object_types,
                        "deleted_after": deleted_after,
                        "deleted_before": deleted_before,
                    },
                    deleted_list_object_list_params.DeletedListObjectListParams,
                ),
            ),
            cast_to=DeletedListObjectListResponse,
        )


class DeletedListObjectsResourceWithRawResponse:
    def __init__(self, deleted_list_objects: DeletedListObjectsResource) -> None:
        self._deleted_list_objects = deleted_list_objects

        self.list = to_raw_response_wrapper(
            deleted_list_objects.list,
        )


class AsyncDeletedListObjectsResourceWithRawResponse:
    def __init__(self, deleted_list_objects: AsyncDeletedListObjectsResource) -> None:
        self._deleted_list_objects = deleted_list_objects

        self.list = async_to_raw_response_wrapper(
            deleted_list_objects.list,
        )


class DeletedListObjectsResourceWithStreamingResponse:
    def __init__(self, deleted_list_objects: DeletedListObjectsResource) -> None:
        self._deleted_list_objects = deleted_list_objects

        self.list = to_streamed_response_wrapper(
            deleted_list_objects.list,
        )


class AsyncDeletedListObjectsResourceWithStreamingResponse:
    def __init__(self, deleted_list_objects: AsyncDeletedListObjectsResource) -> None:
        self._deleted_list_objects = deleted_list_objects

        self.list = async_to_streamed_response_wrapper(
            deleted_list_objects.list,
        )
