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
from ...types.qbd import (
    time_tracking_activity_list_params,
    time_tracking_activity_create_params,
    time_tracking_activity_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.time_tracking_activity import TimeTrackingActivity
from ...types.qbd.time_tracking_activity_delete_response import TimeTrackingActivityDeleteResponse

__all__ = ["TimeTrackingActivitiesResource", "AsyncTimeTrackingActivitiesResource"]


class TimeTrackingActivitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeTrackingActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return TimeTrackingActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeTrackingActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return TimeTrackingActivitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        duration: str,
        entity_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_status: Literal["billable", "has_been_billed", "not_billable"] | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        external_id: str | Omit = omit,
        note: str | Omit = omit,
        payroll_wage_item_id: str | Omit = omit,
        service_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTrackingActivity:
        """
        Creates a new time tracking activity.

        Args:
          duration: The time spent performing the service during this time tracking activity, in ISO
              8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
              represented as PT1H30M.

              **NOTE**: Although seconds can be specified when creating a time tracking
              activity, they are not returned in responses since QuickBooks Desktop's UI does
              not display seconds.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          entity_id: The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
              being tracked in this time tracking activity. This cannot refer to a customer -
              use the `customer` field to associate a customer or customer-job with this time
              tracking activity.

          transaction_date: The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_status: The billing status of this time tracking activity.

              **IMPORTANT**: When this field is set to "billable" for time tracking
              activities, both `customer` and `serviceItem` are required so that an invoice
              can be created.

          class_id: The time tracking activity's class. Classes can be used to categorize objects
              into meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          customer_id: The customer or customer-job to which this time tracking activity could be
              billed. If `billingStatus` is set to "billable", this field is required.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          note: A note or comment about this time tracking activity.

          payroll_wage_item_id: The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
              tracking activity. This field can only be used for time tracking if: (1) the
              person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
              data to create paychecks" preference is enabled in their payroll settings.

          service_item_id: The type of service performed during this time tracking activity, referring to
              billable or purchasable services such as specialized labor, consulting hours,
              and professional fees.

              **NOTE**: This field is not required if no `customer` is specified. However, if
              `billingStatus` is set to "billable", both this field and `customer` are
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/time-tracking-activities",
            body=maybe_transform(
                {
                    "duration": duration,
                    "entity_id": entity_id,
                    "transaction_date": transaction_date,
                    "billing_status": billing_status,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "external_id": external_id,
                    "note": note,
                    "payroll_wage_item_id": payroll_wage_item_id,
                    "service_item_id": service_item_id,
                },
                time_tracking_activity_create_params.TimeTrackingActivityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
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
    ) -> TimeTrackingActivity:
        """
        Retrieves a time tracking activity by ID.

        **IMPORTANT:** If you need to fetch multiple specific time tracking activities
        by ID, use the list endpoint instead with the `ids` parameter. It accepts an
        array of IDs so you can batch the request into a single call, which is
        significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              retrieve.

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
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
        )

    def update(
        self,
        id: str,
        *,
        duration: str,
        entity_id: str,
        revision_number: str,
        conductor_end_user_id: str,
        billing_status: Literal["billable", "has_been_billed", "not_billable"] | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        note: str | Omit = omit,
        payroll_wage_item_id: str | Omit = omit,
        service_item_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTrackingActivity:
        """
        Updates an existing time tracking activity.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              update.

          duration: The time spent performing the service during this time tracking activity, in ISO
              8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
              represented as PT1H30M.

              **NOTE**: Although seconds can be specified when creating a time tracking
              activity, they are not returned in responses since QuickBooks Desktop's UI does
              not display seconds.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          entity_id: The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
              being tracked in this time tracking activity. This cannot refer to a customer -
              use the `customer` field to associate a customer or customer-job with this time
              tracking activity.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          revision_number: The current QuickBooks-assigned revision number of the time tracking activity
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_status: The billing status of this time tracking activity.

              **IMPORTANT**: When this field is set to "billable" for time tracking
              activities, both `customer` and `serviceItem` are required so that an invoice
              can be created.

          class_id: The time tracking activity's class. Classes can be used to categorize objects
              into meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          customer_id: The customer or customer-job to which this time tracking activity could be
              billed. If `billingStatus` is set to "billable", this field is required.

          note: A note or comment about this time tracking activity.

          payroll_wage_item_id: The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
              tracking activity. This field can only be used for time tracking if: (1) the
              person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
              data to create paychecks" preference is enabled in their payroll settings.

          service_item_id: The type of service performed during this time tracking activity, referring to
              billable or purchasable services such as specialized labor, consulting hours,
              and professional fees.

              **NOTE**: This field is not required if no `customer` is specified. However, if
              `billingStatus` is set to "billable", both this field and `customer` are
              required.

          transaction_date: The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "entity_id": entity_id,
                    "revision_number": revision_number,
                    "billing_status": billing_status,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "note": note,
                    "payroll_wage_item_id": payroll_wage_item_id,
                    "service_item_id": service_item_id,
                    "transaction_date": transaction_date,
                },
                time_tracking_activity_update_params.TimeTrackingActivityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> SyncCursorPage[TimeTrackingActivity]:
        """Returns a list of time tracking activities.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for time tracking activities tracking the time of these employees,
              vendors, or persons on QuickBooks's "Other Names" list.

          ids: Filter for specific time tracking activities by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          transaction_date_from: Filter for time tracking activities whose `date` field is on or after this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for time tracking activities whose `date` field is on or before this
              date, in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for time tracking activities updated on or after this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for time tracking activities updated on or before this date/time. Accepts
              the following ISO 8601 formats:

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
            "/quickbooks-desktop/time-tracking-activities",
            page=SyncCursorPage[TimeTrackingActivity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "entity_ids": entity_ids,
                        "ids": ids,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    time_tracking_activity_list_params.TimeTrackingActivityListParams,
                ),
            ),
            model=TimeTrackingActivity,
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
    ) -> TimeTrackingActivityDeleteResponse:
        """Permanently deletes a a time tracking activity.

        The deletion will fail if the
        time tracking activity is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              delete.

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
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivityDeleteResponse,
        )


class AsyncTimeTrackingActivitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeTrackingActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeTrackingActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeTrackingActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncTimeTrackingActivitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        duration: str,
        entity_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_status: Literal["billable", "has_been_billed", "not_billable"] | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        external_id: str | Omit = omit,
        note: str | Omit = omit,
        payroll_wage_item_id: str | Omit = omit,
        service_item_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTrackingActivity:
        """
        Creates a new time tracking activity.

        Args:
          duration: The time spent performing the service during this time tracking activity, in ISO
              8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
              represented as PT1H30M.

              **NOTE**: Although seconds can be specified when creating a time tracking
              activity, they are not returned in responses since QuickBooks Desktop's UI does
              not display seconds.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          entity_id: The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
              being tracked in this time tracking activity. This cannot refer to a customer -
              use the `customer` field to associate a customer or customer-job with this time
              tracking activity.

          transaction_date: The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_status: The billing status of this time tracking activity.

              **IMPORTANT**: When this field is set to "billable" for time tracking
              activities, both `customer` and `serviceItem` are required so that an invoice
              can be created.

          class_id: The time tracking activity's class. Classes can be used to categorize objects
              into meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          customer_id: The customer or customer-job to which this time tracking activity could be
              billed. If `billingStatus` is set to "billable", this field is required.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          note: A note or comment about this time tracking activity.

          payroll_wage_item_id: The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
              tracking activity. This field can only be used for time tracking if: (1) the
              person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
              data to create paychecks" preference is enabled in their payroll settings.

          service_item_id: The type of service performed during this time tracking activity, referring to
              billable or purchasable services such as specialized labor, consulting hours,
              and professional fees.

              **NOTE**: This field is not required if no `customer` is specified. However, if
              `billingStatus` is set to "billable", both this field and `customer` are
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/time-tracking-activities",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "entity_id": entity_id,
                    "transaction_date": transaction_date,
                    "billing_status": billing_status,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "external_id": external_id,
                    "note": note,
                    "payroll_wage_item_id": payroll_wage_item_id,
                    "service_item_id": service_item_id,
                },
                time_tracking_activity_create_params.TimeTrackingActivityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
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
    ) -> TimeTrackingActivity:
        """
        Retrieves a time tracking activity by ID.

        **IMPORTANT:** If you need to fetch multiple specific time tracking activities
        by ID, use the list endpoint instead with the `ids` parameter. It accepts an
        array of IDs so you can batch the request into a single call, which is
        significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              retrieve.

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
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
        )

    async def update(
        self,
        id: str,
        *,
        duration: str,
        entity_id: str,
        revision_number: str,
        conductor_end_user_id: str,
        billing_status: Literal["billable", "has_been_billed", "not_billable"] | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        note: str | Omit = omit,
        payroll_wage_item_id: str | Omit = omit,
        service_item_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeTrackingActivity:
        """
        Updates an existing time tracking activity.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              update.

          duration: The time spent performing the service during this time tracking activity, in ISO
              8601 format for time intervals (PTnHnMnS). For example, 1 hour and 30 minutes is
              represented as PT1H30M.

              **NOTE**: Although seconds can be specified when creating a time tracking
              activity, they are not returned in responses since QuickBooks Desktop's UI does
              not display seconds.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          entity_id: The employee, vendor, or person on QuickBooks's "Other Names" list whose time is
              being tracked in this time tracking activity. This cannot refer to a customer -
              use the `customer` field to associate a customer or customer-job with this time
              tracking activity.

              **IMPORTANT**: This field is required for updating time tracking activities,
              even if the field is not being modified, because of a bug in QuickBooks itself.

          revision_number: The current QuickBooks-assigned revision number of the time tracking activity
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_status: The billing status of this time tracking activity.

              **IMPORTANT**: When this field is set to "billable" for time tracking
              activities, both `customer` and `serviceItem` are required so that an invoice
              can be created.

          class_id: The time tracking activity's class. Classes can be used to categorize objects
              into meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          customer_id: The customer or customer-job to which this time tracking activity could be
              billed. If `billingStatus` is set to "billable", this field is required.

          note: A note or comment about this time tracking activity.

          payroll_wage_item_id: The payroll wage item (e.g., Regular Pay, Overtime Pay) to use for this time
              tracking activity. This field can only be used for time tracking if: (1) the
              person specified in `entity` is an employee in QuickBooks, and (2) the "Use time
              data to create paychecks" preference is enabled in their payroll settings.

          service_item_id: The type of service performed during this time tracking activity, referring to
              billable or purchasable services such as specialized labor, consulting hours,
              and professional fees.

              **NOTE**: This field is not required if no `customer` is specified. However, if
              `billingStatus` is set to "billable", both this field and `customer` are
              required.

          transaction_date: The date of this time tracking activity, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "entity_id": entity_id,
                    "revision_number": revision_number,
                    "billing_status": billing_status,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "note": note,
                    "payroll_wage_item_id": payroll_wage_item_id,
                    "service_item_id": service_item_id,
                    "transaction_date": transaction_date,
                },
                time_tracking_activity_update_params.TimeTrackingActivityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivity,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> AsyncPaginator[TimeTrackingActivity, AsyncCursorPage[TimeTrackingActivity]]:
        """Returns a list of time tracking activities.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for time tracking activities tracking the time of these employees,
              vendors, or persons on QuickBooks's "Other Names" list.

          ids: Filter for specific time tracking activities by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          transaction_date_from: Filter for time tracking activities whose `date` field is on or after this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for time tracking activities whose `date` field is on or before this
              date, in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for time tracking activities updated on or after this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for time tracking activities updated on or before this date/time. Accepts
              the following ISO 8601 formats:

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
            "/quickbooks-desktop/time-tracking-activities",
            page=AsyncCursorPage[TimeTrackingActivity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "entity_ids": entity_ids,
                        "ids": ids,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    time_tracking_activity_list_params.TimeTrackingActivityListParams,
                ),
            ),
            model=TimeTrackingActivity,
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
    ) -> TimeTrackingActivityDeleteResponse:
        """Permanently deletes a a time tracking activity.

        The deletion will fail if the
        time tracking activity is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the time tracking activity to
              delete.

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
            f"/quickbooks-desktop/time-tracking-activities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeTrackingActivityDeleteResponse,
        )


class TimeTrackingActivitiesResourceWithRawResponse:
    def __init__(self, time_tracking_activities: TimeTrackingActivitiesResource) -> None:
        self._time_tracking_activities = time_tracking_activities

        self.create = to_raw_response_wrapper(
            time_tracking_activities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            time_tracking_activities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            time_tracking_activities.update,
        )
        self.list = to_raw_response_wrapper(
            time_tracking_activities.list,
        )
        self.delete = to_raw_response_wrapper(
            time_tracking_activities.delete,
        )


class AsyncTimeTrackingActivitiesResourceWithRawResponse:
    def __init__(self, time_tracking_activities: AsyncTimeTrackingActivitiesResource) -> None:
        self._time_tracking_activities = time_tracking_activities

        self.create = async_to_raw_response_wrapper(
            time_tracking_activities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            time_tracking_activities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            time_tracking_activities.update,
        )
        self.list = async_to_raw_response_wrapper(
            time_tracking_activities.list,
        )
        self.delete = async_to_raw_response_wrapper(
            time_tracking_activities.delete,
        )


class TimeTrackingActivitiesResourceWithStreamingResponse:
    def __init__(self, time_tracking_activities: TimeTrackingActivitiesResource) -> None:
        self._time_tracking_activities = time_tracking_activities

        self.create = to_streamed_response_wrapper(
            time_tracking_activities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            time_tracking_activities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            time_tracking_activities.update,
        )
        self.list = to_streamed_response_wrapper(
            time_tracking_activities.list,
        )
        self.delete = to_streamed_response_wrapper(
            time_tracking_activities.delete,
        )


class AsyncTimeTrackingActivitiesResourceWithStreamingResponse:
    def __init__(self, time_tracking_activities: AsyncTimeTrackingActivitiesResource) -> None:
        self._time_tracking_activities = time_tracking_activities

        self.create = async_to_streamed_response_wrapper(
            time_tracking_activities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            time_tracking_activities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            time_tracking_activities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            time_tracking_activities.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            time_tracking_activities.delete,
        )
