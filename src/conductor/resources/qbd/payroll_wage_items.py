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
from ...types.qbd import payroll_wage_item_list_params, payroll_wage_item_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.payroll_wage_item import PayrollWageItem

__all__ = ["PayrollWageItemsResource", "AsyncPayrollWageItemsResource"]


class PayrollWageItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayrollWageItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return PayrollWageItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayrollWageItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return PayrollWageItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        expense_account_id: str,
        name: str,
        wage_type: Literal[
            "bonus",
            "commission",
            "hourly_overtime",
            "hourly_regular",
            "hourly_sick",
            "hourly_vacation",
            "salary_regular",
            "salary_sick",
            "salary_vacation",
        ],
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        overtime_multiplier: str | Omit = omit,
        rate: str | Omit = omit,
        rate_percent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayrollWageItem:
        """
        Creates a new payroll wage item.

        Args:
          expense_account_id: The expense account used to track wage expenses paid through this payroll wage
              item.

          name: The case-insensitive unique name of this payroll wage item, unique across all
              payroll wage items.

              **NOTE**: Payroll wage items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          wage_type: Categorizes how this payroll wage item calculates pay - can be hourly (regular,
              overtime, sick, or vacation), salary (regular, sick, or vacation), bonus, or
              commission based.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this payroll wage item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          overtime_multiplier: The overtime pay multiplier for this payroll wage item, represented as a decimal
              string. For example, `"1.5"` represents time-and-a-half pay.

          rate: The default rate for this payroll wage item, represented as a decimal string.
              Only one of `rate` and `ratePercent` can be set.

          rate_percent: The default rate for this payroll wage item expressed as a percentage. Only one
              of `rate` and `ratePercent` can be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/payroll-wage-items",
            body=maybe_transform(
                {
                    "expense_account_id": expense_account_id,
                    "name": name,
                    "wage_type": wage_type,
                    "is_active": is_active,
                    "overtime_multiplier": overtime_multiplier,
                    "rate": rate,
                    "rate_percent": rate_percent,
                },
                payroll_wage_item_create_params.PayrollWageItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayrollWageItem,
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
    ) -> PayrollWageItem:
        """
        Retrieves a payroll wage item by ID.

        **IMPORTANT:** If you need to fetch multiple specific payroll wage items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the payroll wage item to retrieve.

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
            f"/quickbooks-desktop/payroll-wage-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayrollWageItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PayrollWageItem]:
        """Returns a list of payroll wage items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific payroll wage items by their QuickBooks-assigned unique
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

          name_contains: Filter for payroll wage items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for payroll wage items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for payroll wage items whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific payroll wage items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a payroll wage item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for payroll wage items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for payroll wage items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for payroll wage items that are active, inactive, or both.

          updated_after: Filter for payroll wage items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for payroll wage items updated on or before this date/time. Accepts the
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
        return self._get_api_list(
            "/quickbooks-desktop/payroll-wage-items",
            page=SyncCursorPage[PayrollWageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
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
                    payroll_wage_item_list_params.PayrollWageItemListParams,
                ),
            ),
            model=PayrollWageItem,
        )


class AsyncPayrollWageItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayrollWageItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayrollWageItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayrollWageItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncPayrollWageItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        expense_account_id: str,
        name: str,
        wage_type: Literal[
            "bonus",
            "commission",
            "hourly_overtime",
            "hourly_regular",
            "hourly_sick",
            "hourly_vacation",
            "salary_regular",
            "salary_sick",
            "salary_vacation",
        ],
        conductor_end_user_id: str,
        is_active: bool | Omit = omit,
        overtime_multiplier: str | Omit = omit,
        rate: str | Omit = omit,
        rate_percent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayrollWageItem:
        """
        Creates a new payroll wage item.

        Args:
          expense_account_id: The expense account used to track wage expenses paid through this payroll wage
              item.

          name: The case-insensitive unique name of this payroll wage item, unique across all
              payroll wage items.

              **NOTE**: Payroll wage items do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          wage_type: Categorizes how this payroll wage item calculates pay - can be hourly (regular,
              overtime, sick, or vacation), salary (regular, sick, or vacation), bonus, or
              commission based.

          conductor_end_user_id: The ID of the End-User to receive this request.

          is_active: Indicates whether this payroll wage item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks. Defaults to `true`.

          overtime_multiplier: The overtime pay multiplier for this payroll wage item, represented as a decimal
              string. For example, `"1.5"` represents time-and-a-half pay.

          rate: The default rate for this payroll wage item, represented as a decimal string.
              Only one of `rate` and `ratePercent` can be set.

          rate_percent: The default rate for this payroll wage item expressed as a percentage. Only one
              of `rate` and `ratePercent` can be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/payroll-wage-items",
            body=await async_maybe_transform(
                {
                    "expense_account_id": expense_account_id,
                    "name": name,
                    "wage_type": wage_type,
                    "is_active": is_active,
                    "overtime_multiplier": overtime_multiplier,
                    "rate": rate,
                    "rate_percent": rate_percent,
                },
                payroll_wage_item_create_params.PayrollWageItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayrollWageItem,
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
    ) -> PayrollWageItem:
        """
        Retrieves a payroll wage item by ID.

        **IMPORTANT:** If you need to fetch multiple specific payroll wage items by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the payroll wage item to retrieve.

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
            f"/quickbooks-desktop/payroll-wage-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayrollWageItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        name_contains: str | Omit = omit,
        name_ends_with: str | Omit = omit,
        name_from: str | Omit = omit,
        names: SequenceNotStr[str] | Omit = omit,
        name_starts_with: str | Omit = omit,
        name_to: str | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        updated_after: str | Omit = omit,
        updated_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayrollWageItem, AsyncCursorPage[PayrollWageItem]]:
        """Returns a list of payroll wage items.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific payroll wage items by their QuickBooks-assigned unique
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

          name_contains: Filter for payroll wage items whose `name` contains this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for payroll wage items whose `name` ends with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for payroll wage items whose `name` is alphabetically greater than or
              equal to this value.

          names: Filter for specific payroll wage items by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a payroll wage item.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for payroll wage items whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for payroll wage items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for payroll wage items that are active, inactive, or both.

          updated_after: Filter for payroll wage items updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for payroll wage items updated on or before this date/time. Accepts the
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
        return self._get_api_list(
            "/quickbooks-desktop/payroll-wage-items",
            page=AsyncCursorPage[PayrollWageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
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
                    payroll_wage_item_list_params.PayrollWageItemListParams,
                ),
            ),
            model=PayrollWageItem,
        )


class PayrollWageItemsResourceWithRawResponse:
    def __init__(self, payroll_wage_items: PayrollWageItemsResource) -> None:
        self._payroll_wage_items = payroll_wage_items

        self.create = to_raw_response_wrapper(
            payroll_wage_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payroll_wage_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payroll_wage_items.list,
        )


class AsyncPayrollWageItemsResourceWithRawResponse:
    def __init__(self, payroll_wage_items: AsyncPayrollWageItemsResource) -> None:
        self._payroll_wage_items = payroll_wage_items

        self.create = async_to_raw_response_wrapper(
            payroll_wage_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payroll_wage_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payroll_wage_items.list,
        )


class PayrollWageItemsResourceWithStreamingResponse:
    def __init__(self, payroll_wage_items: PayrollWageItemsResource) -> None:
        self._payroll_wage_items = payroll_wage_items

        self.create = to_streamed_response_wrapper(
            payroll_wage_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payroll_wage_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payroll_wage_items.list,
        )


class AsyncPayrollWageItemsResourceWithStreamingResponse:
    def __init__(self, payroll_wage_items: AsyncPayrollWageItemsResource) -> None:
        self._payroll_wage_items = payroll_wage_items

        self.create = async_to_streamed_response_wrapper(
            payroll_wage_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payroll_wage_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payroll_wage_items.list,
        )
