# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import date_driven_term_list_params, date_driven_term_create_params
from ..._base_client import make_request_options
from ...types.qbd.date_driven_term import DateDrivenTerm
from ...types.qbd.date_driven_term_list_response import DateDrivenTermListResponse

__all__ = ["DateDrivenTermsResource", "AsyncDateDrivenTermsResource"]


class DateDrivenTermsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DateDrivenTermsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return DateDrivenTermsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DateDrivenTermsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return DateDrivenTermsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        due_day_of_month: float,
        name: str,
        conductor_end_user_id: str,
        discount_day_of_month: float | NotGiven = NOT_GIVEN,
        discount_percentage: str | NotGiven = NOT_GIVEN,
        grace_period_days: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTerm:
        """
        Creates a new date-driven term.

        Args:
          due_day_of_month: The day of the month when full payment is due without discount.

          name: The case-insensitive unique name of this date-driven term, unique across all
              date-driven terms.

              **NOTE**: Date-driven terms do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          discount_day_of_month: The day of the month within which payment must be received to qualify for the
              discount specified by `discountPercentage`.

          discount_percentage: The discount percentage applied to the payment if received on or before the
              specified `discountDayOfMonth`. The value is between 0 and 100.

          grace_period_days: The number of days before `dueDayOfMonth` when an invoice or bill issued within
              this threshold is considered due the following month. For example, with
              `dueDayOfMonth` set to 15 and `gracePeriodDays` set to 2, an invoice issued on
              the 13th would be due on the 15th of the next month, while an invoice issued on
              the 12th would be due on the 15th of the current month.

          is_active: Indicates whether this date-driven term is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/date-driven-terms",
            body=maybe_transform(
                {
                    "due_day_of_month": due_day_of_month,
                    "name": name,
                    "discount_day_of_month": discount_day_of_month,
                    "discount_percentage": discount_percentage,
                    "grace_period_days": grace_period_days,
                    "is_active": is_active,
                },
                date_driven_term_create_params.DateDrivenTermCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDrivenTerm,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTerm:
        """
        Retrieves a date-driven term by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the date-driven term to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/date-driven-terms/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDrivenTerm,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTermListResponse:
        """Returns a list of date-driven terms.

        NOTE: QuickBooks Desktop does not support
        pagination for date-driven terms; hence, there is no `cursor` parameter. Users
        typically have few date-driven terms.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific date-driven terms by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              date-driven terms. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all date-driven terms
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because date-driven terms typically have low record counts.

          name_contains: Filter for date-driven terms whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for date-driven terms whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for date-driven terms whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific date-driven terms by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a date-driven term.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for date-driven terms whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for date-driven terms whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for date-driven terms that are active, inactive, or both.

          updated_after: Filter for date-driven terms updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for date-driven terms updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/date-driven-terms",
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
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    date_driven_term_list_params.DateDrivenTermListParams,
                ),
            ),
            cast_to=DateDrivenTermListResponse,
        )


class AsyncDateDrivenTermsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDateDrivenTermsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDateDrivenTermsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDateDrivenTermsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncDateDrivenTermsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        due_day_of_month: float,
        name: str,
        conductor_end_user_id: str,
        discount_day_of_month: float | NotGiven = NOT_GIVEN,
        discount_percentage: str | NotGiven = NOT_GIVEN,
        grace_period_days: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTerm:
        """
        Creates a new date-driven term.

        Args:
          due_day_of_month: The day of the month when full payment is due without discount.

          name: The case-insensitive unique name of this date-driven term, unique across all
              date-driven terms.

              **NOTE**: Date-driven terms do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          discount_day_of_month: The day of the month within which payment must be received to qualify for the
              discount specified by `discountPercentage`.

          discount_percentage: The discount percentage applied to the payment if received on or before the
              specified `discountDayOfMonth`. The value is between 0 and 100.

          grace_period_days: The number of days before `dueDayOfMonth` when an invoice or bill issued within
              this threshold is considered due the following month. For example, with
              `dueDayOfMonth` set to 15 and `gracePeriodDays` set to 2, an invoice issued on
              the 13th would be due on the 15th of the next month, while an invoice issued on
              the 12th would be due on the 15th of the current month.

          is_active: Indicates whether this date-driven term is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/date-driven-terms",
            body=await async_maybe_transform(
                {
                    "due_day_of_month": due_day_of_month,
                    "name": name,
                    "discount_day_of_month": discount_day_of_month,
                    "discount_percentage": discount_percentage,
                    "grace_period_days": grace_period_days,
                    "is_active": is_active,
                },
                date_driven_term_create_params.DateDrivenTermCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDrivenTerm,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTerm:
        """
        Retrieves a date-driven term by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the date-driven term to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/date-driven-terms/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDrivenTerm,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        names: List[str] | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDrivenTermListResponse:
        """Returns a list of date-driven terms.

        NOTE: QuickBooks Desktop does not support
        pagination for date-driven terms; hence, there is no `cursor` parameter. Users
        typically have few date-driven terms.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific date-driven terms by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              date-driven terms. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all date-driven terms
              without limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because date-driven terms typically have low record counts.

          name_contains: Filter for date-driven terms whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for date-driven terms whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for date-driven terms whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific date-driven terms by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a date-driven term.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for date-driven terms whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for date-driven terms whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for date-driven terms that are active, inactive, or both.

          updated_after: Filter for date-driven terms updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for date-driven terms updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/date-driven-terms",
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
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    date_driven_term_list_params.DateDrivenTermListParams,
                ),
            ),
            cast_to=DateDrivenTermListResponse,
        )


class DateDrivenTermsResourceWithRawResponse:
    def __init__(self, date_driven_terms: DateDrivenTermsResource) -> None:
        self._date_driven_terms = date_driven_terms

        self.create = to_raw_response_wrapper(
            date_driven_terms.create,
        )
        self.retrieve = to_raw_response_wrapper(
            date_driven_terms.retrieve,
        )
        self.list = to_raw_response_wrapper(
            date_driven_terms.list,
        )


class AsyncDateDrivenTermsResourceWithRawResponse:
    def __init__(self, date_driven_terms: AsyncDateDrivenTermsResource) -> None:
        self._date_driven_terms = date_driven_terms

        self.create = async_to_raw_response_wrapper(
            date_driven_terms.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            date_driven_terms.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            date_driven_terms.list,
        )


class DateDrivenTermsResourceWithStreamingResponse:
    def __init__(self, date_driven_terms: DateDrivenTermsResource) -> None:
        self._date_driven_terms = date_driven_terms

        self.create = to_streamed_response_wrapper(
            date_driven_terms.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            date_driven_terms.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            date_driven_terms.list,
        )


class AsyncDateDrivenTermsResourceWithStreamingResponse:
    def __init__(self, date_driven_terms: AsyncDateDrivenTermsResource) -> None:
        self._date_driven_terms = date_driven_terms

        self.create = async_to_streamed_response_wrapper(
            date_driven_terms.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            date_driven_terms.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            date_driven_terms.list,
        )
