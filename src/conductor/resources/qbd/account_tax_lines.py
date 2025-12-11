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
from ...types.qbd.account_tax_line_list_response import AccountTaxLineListResponse

__all__ = ["AccountTaxLinesResource", "AsyncAccountTaxLinesResource"]


class AccountTaxLinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountTaxLinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AccountTaxLinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountTaxLinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AccountTaxLinesResourceWithStreamingResponse(self)

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
    ) -> AccountTaxLineListResponse:
        """Returns a list of account tax lines.

        NOTE: QuickBooks Desktop does not support
        pagination for account tax lines; hence, there is no `cursor` parameter. Users
        typically have few account tax lines.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/account-tax-lines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTaxLineListResponse,
        )


class AsyncAccountTaxLinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountTaxLinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountTaxLinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountTaxLinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncAccountTaxLinesResourceWithStreamingResponse(self)

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
    ) -> AccountTaxLineListResponse:
        """Returns a list of account tax lines.

        NOTE: QuickBooks Desktop does not support
        pagination for account tax lines; hence, there is no `cursor` parameter. Users
        typically have few account tax lines.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/account-tax-lines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTaxLineListResponse,
        )


class AccountTaxLinesResourceWithRawResponse:
    def __init__(self, account_tax_lines: AccountTaxLinesResource) -> None:
        self._account_tax_lines = account_tax_lines

        self.list = to_raw_response_wrapper(
            account_tax_lines.list,
        )


class AsyncAccountTaxLinesResourceWithRawResponse:
    def __init__(self, account_tax_lines: AsyncAccountTaxLinesResource) -> None:
        self._account_tax_lines = account_tax_lines

        self.list = async_to_raw_response_wrapper(
            account_tax_lines.list,
        )


class AccountTaxLinesResourceWithStreamingResponse:
    def __init__(self, account_tax_lines: AccountTaxLinesResource) -> None:
        self._account_tax_lines = account_tax_lines

        self.list = to_streamed_response_wrapper(
            account_tax_lines.list,
        )


class AsyncAccountTaxLinesResourceWithStreamingResponse:
    def __init__(self, account_tax_lines: AsyncAccountTaxLinesResource) -> None:
        self._account_tax_lines = account_tax_lines

        self.list = async_to_streamed_response_wrapper(
            account_tax_lines.list,
        )
