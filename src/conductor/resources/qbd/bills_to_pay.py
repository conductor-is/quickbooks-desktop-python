# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ...types.qbd import bills_to_pay_list_params
from ..._base_client import make_request_options
from ...types.qbd.bills_to_pay_list_response import BillsToPayListResponse

__all__ = ["BillsToPayResource", "AsyncBillsToPayResource"]


class BillsToPayResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillsToPayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return BillsToPayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillsToPayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return BillsToPayResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        vendor_id: str,
        conductor_end_user_id: str,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        payables_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillsToPayListResponse:
        """
        Lists open vendor bills and available vendor credits for a specific QuickBooks
        Desktop vendor. Use each `bill.billId` as `applyToTransactions[].transactionId`
        in bill-payment requests. To apply a returned credit, place it under the target
        bill's `applyToTransactions[].applyCredits[]` entry, set `creditTransactionId`
        to `credit.creditTransactionId`, and choose an `appliedAmount` that does not
        exceed `credit.creditRemaining` or the target bill's remaining amount due.

        **NOTE:** QuickBooks Desktop does not support pagination for bills to pay;
        hence, there is no `cursor` parameter. Users typically have few bills to pay.

        Args:
          vendor_id: The vendor whose open bills and available credits should be returned.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_ids: Filter for open bills and available credits in these currencies.

          due_date: Filter the bill branch to open bills due on or before this date, in ISO 8601
              format (YYYY-MM-DD). If omitted, QuickBooks Desktop returns open bills from all
              due dates. Available credits can still be returned because credits do not have a
              due date.

          payables_account_id: Filter for open bills and available credits assigned to this Accounts-Payable
              account. If omitted, QuickBooks Desktop uses the default A/P account configured
              in the company file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/bills-to-pay",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "vendor_id": vendor_id,
                        "currency_ids": currency_ids,
                        "due_date": due_date,
                        "payables_account_id": payables_account_id,
                    },
                    bills_to_pay_list_params.BillsToPayListParams,
                ),
            ),
            cast_to=BillsToPayListResponse,
        )


class AsyncBillsToPayResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillsToPayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillsToPayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillsToPayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncBillsToPayResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        vendor_id: str,
        conductor_end_user_id: str,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        payables_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillsToPayListResponse:
        """
        Lists open vendor bills and available vendor credits for a specific QuickBooks
        Desktop vendor. Use each `bill.billId` as `applyToTransactions[].transactionId`
        in bill-payment requests. To apply a returned credit, place it under the target
        bill's `applyToTransactions[].applyCredits[]` entry, set `creditTransactionId`
        to `credit.creditTransactionId`, and choose an `appliedAmount` that does not
        exceed `credit.creditRemaining` or the target bill's remaining amount due.

        **NOTE:** QuickBooks Desktop does not support pagination for bills to pay;
        hence, there is no `cursor` parameter. Users typically have few bills to pay.

        Args:
          vendor_id: The vendor whose open bills and available credits should be returned.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_ids: Filter for open bills and available credits in these currencies.

          due_date: Filter the bill branch to open bills due on or before this date, in ISO 8601
              format (YYYY-MM-DD). If omitted, QuickBooks Desktop returns open bills from all
              due dates. Available credits can still be returned because credits do not have a
              due date.

          payables_account_id: Filter for open bills and available credits assigned to this Accounts-Payable
              account. If omitted, QuickBooks Desktop uses the default A/P account configured
              in the company file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/bills-to-pay",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "vendor_id": vendor_id,
                        "currency_ids": currency_ids,
                        "due_date": due_date,
                        "payables_account_id": payables_account_id,
                    },
                    bills_to_pay_list_params.BillsToPayListParams,
                ),
            ),
            cast_to=BillsToPayListResponse,
        )


class BillsToPayResourceWithRawResponse:
    def __init__(self, bills_to_pay: BillsToPayResource) -> None:
        self._bills_to_pay = bills_to_pay

        self.list = to_raw_response_wrapper(
            bills_to_pay.list,
        )


class AsyncBillsToPayResourceWithRawResponse:
    def __init__(self, bills_to_pay: AsyncBillsToPayResource) -> None:
        self._bills_to_pay = bills_to_pay

        self.list = async_to_raw_response_wrapper(
            bills_to_pay.list,
        )


class BillsToPayResourceWithStreamingResponse:
    def __init__(self, bills_to_pay: BillsToPayResource) -> None:
        self._bills_to_pay = bills_to_pay

        self.list = to_streamed_response_wrapper(
            bills_to_pay.list,
        )


class AsyncBillsToPayResourceWithStreamingResponse:
    def __init__(self, bills_to_pay: AsyncBillsToPayResource) -> None:
        self._bills_to_pay = bills_to_pay

        self.list = async_to_streamed_response_wrapper(
            bills_to_pay.list,
        )
