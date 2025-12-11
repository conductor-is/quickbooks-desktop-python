# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.qbd import payment_method_list_params, payment_method_create_params
from ..._base_client import make_request_options
from ...types.qbd.payment_method import PaymentMethod
from ...types.qbd.payment_method_list_response import PaymentMethodListResponse

__all__ = ["PaymentMethodsResource", "AsyncPaymentMethodsResource"]


class PaymentMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return PaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return PaymentMethodsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        payment_method_type: Literal[
            "american_express",
            "cash",
            "check",
            "debit_card",
            "discover",
            "e_check",
            "gift_card",
            "master_card",
            "other",
            "other_credit_card",
            "visa",
        ],
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethod:
        """
        Creates a new payment method.

        Args:
          name: The case-insensitive unique name of this payment method, unique across all
              payment methods.

              **NOTE**: Payment methods do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          payment_method_type: This payment method's type.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this payment method is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/payment-methods",
            body=maybe_transform(
                {
                    "name": name,
                    "payment_method_type": payment_method_type,
                    "is_active": is_active,
                },
                payment_method_create_params.PaymentMethodCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethod,
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
    ) -> PaymentMethod:
        """
        Retrieves a payment method by ID.

        **IMPORTANT:** If you need to fetch multiple specific payment methods by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the payment method to retrieve.

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
            f"/quickbooks-desktop/payment-methods/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethod,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        payment_method_type: Literal[
            "american_express",
            "cash",
            "check",
            "debit_card",
            "discover",
            "e_check",
            "gift_card",
            "master_card",
            "other",
            "other_credit_card",
            "visa",
        ]
        | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodListResponse:
        """Returns a list of payment methods.

        NOTE: QuickBooks Desktop does not support
        pagination for payment methods; hence, there is no `cursor` parameter. Users
        typically have few payment methods.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific payment methods by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              payment methods. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all payment methods without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because payment methods typically have low record counts.

          name_contains: Filter for payment methods whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for payment methods whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for payment methods whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific payment methods by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a payment method.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for payment methods whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for payment methods whose `name` is alphabetically less than or equal to
              this value.

          payment_method_type: Filter for payment methods of this type.

          status: Filter for payment methods that are active, inactive, or both.

          updated_after: Filter for payment methods updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for payment methods updated on or before this date/time. Accepts the
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
        return self._get(
            "/quickbooks-desktop/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "payment_method_type": payment_method_type,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    payment_method_list_params.PaymentMethodListParams,
                ),
            ),
            cast_to=PaymentMethodListResponse,
        )


class AsyncPaymentMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncPaymentMethodsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        payment_method_type: Literal[
            "american_express",
            "cash",
            "check",
            "debit_card",
            "discover",
            "e_check",
            "gift_card",
            "master_card",
            "other",
            "other_credit_card",
            "visa",
        ],
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethod:
        """
        Creates a new payment method.

        Args:
          name: The case-insensitive unique name of this payment method, unique across all
              payment methods.

              **NOTE**: Payment methods do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          payment_method_type: This payment method's type.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this payment method is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/payment-methods",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "payment_method_type": payment_method_type,
                    "is_active": is_active,
                },
                payment_method_create_params.PaymentMethodCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethod,
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
    ) -> PaymentMethod:
        """
        Retrieves a payment method by ID.

        **IMPORTANT:** If you need to fetch multiple specific payment methods by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the payment method to retrieve.

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
            f"/quickbooks-desktop/payment-methods/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethod,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        payment_method_type: Literal[
            "american_express",
            "cash",
            "check",
            "debit_card",
            "discover",
            "e_check",
            "gift_card",
            "master_card",
            "other",
            "other_credit_card",
            "visa",
        ]
        | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentMethodListResponse:
        """Returns a list of payment methods.

        NOTE: QuickBooks Desktop does not support
        pagination for payment methods; hence, there is no `cursor` parameter. Users
        typically have few payment methods.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          ids: Filter for specific payment methods by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              payment methods. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all payment methods without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because payment methods typically have low record counts.

          name_contains: Filter for payment methods whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for payment methods whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for payment methods whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific payment methods by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a payment method.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for payment methods whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for payment methods whose `name` is alphabetically less than or equal to
              this value.

          payment_method_type: Filter for payment methods of this type.

          status: Filter for payment methods that are active, inactive, or both.

          updated_after: Filter for payment methods updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for payment methods updated on or before this date/time. Accepts the
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
        return await self._get(
            "/quickbooks-desktop/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "names": names,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "payment_method_type": payment_method_type,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    payment_method_list_params.PaymentMethodListParams,
                ),
            ),
            cast_to=PaymentMethodListResponse,
        )


class PaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.create = to_raw_response_wrapper(
            payment_methods.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payment_methods.list,
        )


class AsyncPaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.create = async_to_raw_response_wrapper(
            payment_methods.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payment_methods.list,
        )


class PaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.create = to_streamed_response_wrapper(
            payment_methods.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payment_methods.list,
        )


class AsyncPaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.create = async_to_streamed_response_wrapper(
            payment_methods.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_methods.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_methods.list,
        )
