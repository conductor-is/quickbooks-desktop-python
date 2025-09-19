# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import end_user_create_params, end_user_passthrough_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.end_user import EndUser
from ..types.end_user_list_response import EndUserListResponse
from ..types.end_user_delete_response import EndUserDeleteResponse
from ..types.end_user_passthrough_response import EndUserPassthroughResponse

__all__ = ["EndUsersResource", "AsyncEndUsersResource"]


class EndUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return EndUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return EndUsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_name: str,
        email: str,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUser:
        """
        Creates an end-user.

        Args:
          company_name: The end-user's company name that will be shown elsewhere in Conductor.

          email: The end-user's email address for identification purposes. Setting this field
              will not cause any emails to be sent.

          source_id: The end-user's unique identifier from your system. Maps users between your
              database and Conductor. Must be unique for each user. If you have only one user,
              you may use any string value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/end-users",
            body=maybe_transform(
                {
                    "company_name": company_name,
                    "email": email,
                    "source_id": source_id,
                },
                end_user_create_params.EndUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUser:
        """
        Retrieves an end-user object.

        Args:
          id: The ID of the end-user to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/end-users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserListResponse:
        """Returns a list of your end-users."""
        return self._get(
            "/end-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserDeleteResponse:
        """
        Permanently deletes an end-user object and all of its connections.

        Args:
          id: The ID of the end-user to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/end-users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserDeleteResponse,
        )

    def passthrough(
        self,
        integration_slug: Literal["quickbooks_desktop"],
        *,
        id: str,
        qbd_payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserPassthroughResponse:
        """
        Sends a request directly to the specified integration connection (e.g.,
        QuickBooks Desktop) on behalf of the end-user.

        Args:
          id: The ID of the end-user who owns the integration connection.

          integration_slug: The integration identifier for the end-user's connection.

          qbd_payload: The request body to send to the integration connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_slug:
            raise ValueError(f"Expected a non-empty value for `integration_slug` but received {integration_slug!r}")
        return self._post(
            f"/end-users/{id}/passthrough/{integration_slug}",
            body=maybe_transform(qbd_payload, end_user_passthrough_params.EndUserPassthroughParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserPassthroughResponse,
        )


class AsyncEndUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEndUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncEndUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_name: str,
        email: str,
        source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUser:
        """
        Creates an end-user.

        Args:
          company_name: The end-user's company name that will be shown elsewhere in Conductor.

          email: The end-user's email address for identification purposes. Setting this field
              will not cause any emails to be sent.

          source_id: The end-user's unique identifier from your system. Maps users between your
              database and Conductor. Must be unique for each user. If you have only one user,
              you may use any string value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/end-users",
            body=await async_maybe_transform(
                {
                    "company_name": company_name,
                    "email": email,
                    "source_id": source_id,
                },
                end_user_create_params.EndUserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUser:
        """
        Retrieves an end-user object.

        Args:
          id: The ID of the end-user to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/end-users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUser,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserListResponse:
        """Returns a list of your end-users."""
        return await self._get(
            "/end-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserDeleteResponse:
        """
        Permanently deletes an end-user object and all of its connections.

        Args:
          id: The ID of the end-user to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/end-users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserDeleteResponse,
        )

    async def passthrough(
        self,
        integration_slug: Literal["quickbooks_desktop"],
        *,
        id: str,
        qbd_payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EndUserPassthroughResponse:
        """
        Sends a request directly to the specified integration connection (e.g.,
        QuickBooks Desktop) on behalf of the end-user.

        Args:
          id: The ID of the end-user who owns the integration connection.

          integration_slug: The integration identifier for the end-user's connection.

          qbd_payload: The request body to send to the integration connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_slug:
            raise ValueError(f"Expected a non-empty value for `integration_slug` but received {integration_slug!r}")
        return await self._post(
            f"/end-users/{id}/passthrough/{integration_slug}",
            body=await async_maybe_transform(qbd_payload, end_user_passthrough_params.EndUserPassthroughParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndUserPassthroughResponse,
        )


class EndUsersResourceWithRawResponse:
    def __init__(self, end_users: EndUsersResource) -> None:
        self._end_users = end_users

        self.create = to_raw_response_wrapper(
            end_users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            end_users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            end_users.list,
        )
        self.delete = to_raw_response_wrapper(
            end_users.delete,
        )
        self.passthrough = to_raw_response_wrapper(
            end_users.passthrough,
        )


class AsyncEndUsersResourceWithRawResponse:
    def __init__(self, end_users: AsyncEndUsersResource) -> None:
        self._end_users = end_users

        self.create = async_to_raw_response_wrapper(
            end_users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            end_users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            end_users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            end_users.delete,
        )
        self.passthrough = async_to_raw_response_wrapper(
            end_users.passthrough,
        )


class EndUsersResourceWithStreamingResponse:
    def __init__(self, end_users: EndUsersResource) -> None:
        self._end_users = end_users

        self.create = to_streamed_response_wrapper(
            end_users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            end_users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            end_users.list,
        )
        self.delete = to_streamed_response_wrapper(
            end_users.delete,
        )
        self.passthrough = to_streamed_response_wrapper(
            end_users.passthrough,
        )


class AsyncEndUsersResourceWithStreamingResponse:
    def __init__(self, end_users: AsyncEndUsersResource) -> None:
        self._end_users = end_users

        self.create = async_to_streamed_response_wrapper(
            end_users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            end_users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            end_users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            end_users.delete,
        )
        self.passthrough = async_to_streamed_response_wrapper(
            end_users.passthrough,
        )
