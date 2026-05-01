# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.qbd.payments_to_deposit_list_response import PaymentsToDepositListResponse

__all__ = ["PaymentsToDepositResource", "AsyncPaymentsToDepositResource"]


class PaymentsToDepositResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsToDepositResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsToDepositResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsToDepositResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return PaymentsToDepositResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentsToDepositListResponse:
        """
        Lists received customer payments that are currently available to include in a
        QuickBooks Desktop deposit. Use each result's `paymentTransactionId` and, when
        present, `paymentTransactionLineId` as the corresponding fields on a deposit
        line.

        **NOTE:** QuickBooks Desktop does not support pagination for payments to
        deposit; hence, there is no `cursor` parameter. Users typically have few
        payments to deposit.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/payments-to-deposit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentsToDepositListResponse,
        )


class AsyncPaymentsToDepositResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsToDepositResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsToDepositResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsToDepositResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncPaymentsToDepositResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentsToDepositListResponse:
        """
        Lists received customer payments that are currently available to include in a
        QuickBooks Desktop deposit. Use each result's `paymentTransactionId` and, when
        present, `paymentTransactionLineId` as the corresponding fields on a deposit
        line.

        **NOTE:** QuickBooks Desktop does not support pagination for payments to
        deposit; hence, there is no `cursor` parameter. Users typically have few
        payments to deposit.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/payments-to-deposit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentsToDepositListResponse,
        )


class PaymentsToDepositResourceWithRawResponse:
    def __init__(self, payments_to_deposit: PaymentsToDepositResource) -> None:
        self._payments_to_deposit = payments_to_deposit

        self.list = to_raw_response_wrapper(
            payments_to_deposit.list,
        )


class AsyncPaymentsToDepositResourceWithRawResponse:
    def __init__(self, payments_to_deposit: AsyncPaymentsToDepositResource) -> None:
        self._payments_to_deposit = payments_to_deposit

        self.list = async_to_raw_response_wrapper(
            payments_to_deposit.list,
        )


class PaymentsToDepositResourceWithStreamingResponse:
    def __init__(self, payments_to_deposit: PaymentsToDepositResource) -> None:
        self._payments_to_deposit = payments_to_deposit

        self.list = to_streamed_response_wrapper(
            payments_to_deposit.list,
        )


class AsyncPaymentsToDepositResourceWithStreamingResponse:
    def __init__(self, payments_to_deposit: AsyncPaymentsToDepositResource) -> None:
        self._payments_to_deposit = payments_to_deposit

        self.list = async_to_streamed_response_wrapper(
            payments_to_deposit.list,
        )
