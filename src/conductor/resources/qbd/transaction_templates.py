# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.qbd.transaction_template_list_response import TransactionTemplateListResponse

__all__ = ["TransactionTemplatesResource", "AsyncTransactionTemplatesResource"]


class TransactionTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return TransactionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return TransactionTemplatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionTemplateListResponse:
        """Returns a list of transaction templates.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/transaction-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionTemplateListResponse,
        )


class AsyncTransactionTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncTransactionTemplatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionTemplateListResponse:
        """Returns a list of transaction templates.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/transaction-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionTemplateListResponse,
        )


class TransactionTemplatesResourceWithRawResponse:
    def __init__(self, transaction_templates: TransactionTemplatesResource) -> None:
        self._transaction_templates = transaction_templates

        self.list = to_raw_response_wrapper(
            transaction_templates.list,
        )


class AsyncTransactionTemplatesResourceWithRawResponse:
    def __init__(self, transaction_templates: AsyncTransactionTemplatesResource) -> None:
        self._transaction_templates = transaction_templates

        self.list = async_to_raw_response_wrapper(
            transaction_templates.list,
        )


class TransactionTemplatesResourceWithStreamingResponse:
    def __init__(self, transaction_templates: TransactionTemplatesResource) -> None:
        self._transaction_templates = transaction_templates

        self.list = to_streamed_response_wrapper(
            transaction_templates.list,
        )


class AsyncTransactionTemplatesResourceWithStreamingResponse:
    def __init__(self, transaction_templates: AsyncTransactionTemplatesResource) -> None:
        self._transaction_templates = transaction_templates

        self.list = async_to_streamed_response_wrapper(
            transaction_templates.list,
        )
