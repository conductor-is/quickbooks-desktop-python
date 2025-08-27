# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import deleted_transaction_list_params
from ..._base_client import make_request_options
from ...types.qbd.deleted_transaction_list_response import DeletedTransactionListResponse

__all__ = ["DeletedTransactionsResource", "AsyncDeletedTransactionsResource"]


class DeletedTransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeletedTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return DeletedTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletedTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return DeletedTransactionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        transaction_types: List[
            Literal[
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "deposit",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item_receipt",
                "journal_entry",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "time_tracking",
                "transfer_inventory",
                "vehicle_mileage",
                "vendor_credit",
            ]
        ],
        conductor_end_user_id: str,
        deleted_after: str | NotGiven = NOT_GIVEN,
        deleted_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedTransactionListResponse:
        """
        Lists deleted transactions of the specified type(s) (e.g., invoice, bill,
        estimate) in the last 90 days. Results are grouped by transaction type and
        ordered by actual delete time (ascending). NOTE: For deleted non-transaction
        list-objects (e.g., customer, vendor, employee), see the deleted-list-objects
        endpoint.

        Args:
          transaction_types: Filter for deleted transactions by their transaction type(s).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          deleted_after: Filter for deleted transactions deleted on or after this date/time, within the
              last 90 days (QuickBooks limit). Format: ISO 8601. Accepts date-only
              (YYYY-MM-DD), datetime without timezone (YYYY-MM-DDTHH:mm:ss), or datetime with
              timezone (YYYY-MM-DDTHH:mm:ss±HH:mm). **NOTE**: Date-only and timezone-less
              datetimes are passed through for QuickBooks Desktop to interpret in the
              QuickBooks Desktop host machine’s local timezone. If the datetime includes a
              timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
              interpret the timestamp.

          deleted_before: Filter for deleted transactions deleted on or before this date/time, within the
              last 90 days (QuickBooks limit). Format: ISO 8601. Accepts date-only
              (YYYY-MM-DD), datetime without timezone (YYYY-MM-DDTHH:mm:ss), or datetime with
              timezone (YYYY-MM-DDTHH:mm:ss±HH:mm). **NOTE**: Date-only and timezone-less
              datetimes are passed through for QuickBooks Desktop to interpret in the
              QuickBooks Desktop host machine’s local timezone. If the datetime includes a
              timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
              interpret the timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/deleted-transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transaction_types": transaction_types,
                        "deleted_after": deleted_after,
                        "deleted_before": deleted_before,
                    },
                    deleted_transaction_list_params.DeletedTransactionListParams,
                ),
            ),
            cast_to=DeletedTransactionListResponse,
        )


class AsyncDeletedTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeletedTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeletedTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletedTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncDeletedTransactionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        transaction_types: List[
            Literal[
                "ar_refund_credit_card",
                "bill",
                "bill_payment_check",
                "bill_payment_credit_card",
                "build_assembly",
                "charge",
                "check",
                "credit_card_charge",
                "credit_card_credit",
                "credit_memo",
                "deposit",
                "estimate",
                "inventory_adjustment",
                "invoice",
                "item_receipt",
                "journal_entry",
                "purchase_order",
                "receive_payment",
                "sales_order",
                "sales_receipt",
                "sales_tax_payment_check",
                "time_tracking",
                "transfer_inventory",
                "vehicle_mileage",
                "vendor_credit",
            ]
        ],
        conductor_end_user_id: str,
        deleted_after: str | NotGiven = NOT_GIVEN,
        deleted_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedTransactionListResponse:
        """
        Lists deleted transactions of the specified type(s) (e.g., invoice, bill,
        estimate) in the last 90 days. Results are grouped by transaction type and
        ordered by actual delete time (ascending). NOTE: For deleted non-transaction
        list-objects (e.g., customer, vendor, employee), see the deleted-list-objects
        endpoint.

        Args:
          transaction_types: Filter for deleted transactions by their transaction type(s).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          deleted_after: Filter for deleted transactions deleted on or after this date/time, within the
              last 90 days (QuickBooks limit). Format: ISO 8601. Accepts date-only
              (YYYY-MM-DD), datetime without timezone (YYYY-MM-DDTHH:mm:ss), or datetime with
              timezone (YYYY-MM-DDTHH:mm:ss±HH:mm). **NOTE**: Date-only and timezone-less
              datetimes are passed through for QuickBooks Desktop to interpret in the
              QuickBooks Desktop host machine’s local timezone. If the datetime includes a
              timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
              interpret the timestamp.

          deleted_before: Filter for deleted transactions deleted on or before this date/time, within the
              last 90 days (QuickBooks limit). Format: ISO 8601. Accepts date-only
              (YYYY-MM-DD), datetime without timezone (YYYY-MM-DDTHH:mm:ss), or datetime with
              timezone (YYYY-MM-DDTHH:mm:ss±HH:mm). **NOTE**: Date-only and timezone-less
              datetimes are passed through for QuickBooks Desktop to interpret in the
              QuickBooks Desktop host machine’s local timezone. If the datetime includes a
              timezone (e.g., `+05:30` or `Z`), QuickBooks Desktop uses that timezone to
              interpret the timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/deleted-transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "transaction_types": transaction_types,
                        "deleted_after": deleted_after,
                        "deleted_before": deleted_before,
                    },
                    deleted_transaction_list_params.DeletedTransactionListParams,
                ),
            ),
            cast_to=DeletedTransactionListResponse,
        )


class DeletedTransactionsResourceWithRawResponse:
    def __init__(self, deleted_transactions: DeletedTransactionsResource) -> None:
        self._deleted_transactions = deleted_transactions

        self.list = to_raw_response_wrapper(
            deleted_transactions.list,
        )


class AsyncDeletedTransactionsResourceWithRawResponse:
    def __init__(self, deleted_transactions: AsyncDeletedTransactionsResource) -> None:
        self._deleted_transactions = deleted_transactions

        self.list = async_to_raw_response_wrapper(
            deleted_transactions.list,
        )


class DeletedTransactionsResourceWithStreamingResponse:
    def __init__(self, deleted_transactions: DeletedTransactionsResource) -> None:
        self._deleted_transactions = deleted_transactions

        self.list = to_streamed_response_wrapper(
            deleted_transactions.list,
        )


class AsyncDeletedTransactionsResourceWithStreamingResponse:
    def __init__(self, deleted_transactions: AsyncDeletedTransactionsResource) -> None:
        self._deleted_transactions = deleted_transactions

        self.list = async_to_streamed_response_wrapper(
            deleted_transactions.list,
        )
