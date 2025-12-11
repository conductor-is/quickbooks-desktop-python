# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.qbd import price_level_list_params, price_level_create_params, price_level_update_params
from ..._base_client import make_request_options
from ...types.qbd.price_level import PriceLevel
from ...types.qbd.price_level_list_response import PriceLevelListResponse

__all__ = ["PriceLevelsResource", "AsyncPriceLevelsResource"]


class PriceLevelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceLevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return PriceLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceLevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return PriceLevelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        currency_id: str | Omit = omit,
        fixed_percentage: str | Omit = omit,
        is_active: bool | Omit = omit,
        per_item_price_levels: Iterable[price_level_create_params.PerItemPriceLevel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceLevel:
        """
        Creates a new price level.

        Args:
          name: The case-insensitive unique name of this price level, unique across all price
              levels.

              **NOTE**: Price levels do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_id: The price level's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          fixed_percentage: The fixed percentage adjustment applied to all items for this price level
              (instead of a per-item price level). Once you create the price level, you cannot
              change this.

              When this price level is applied to a customer, it automatically adjusts the
              `rate` and `amount` columns for applicable line items in sales orders and
              invoices for that customer. This value supports both positive and negative
              values - a value of "20" increases prices by 20%, while "-10" decreases prices
              by 10%.

          is_active: Indicates whether this price level is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          per_item_price_levels: The per-item price level configurations for this price level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/price-levels",
            body=maybe_transform(
                {
                    "name": name,
                    "currency_id": currency_id,
                    "fixed_percentage": fixed_percentage,
                    "is_active": is_active,
                    "per_item_price_levels": per_item_price_levels,
                },
                price_level_create_params.PriceLevelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
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
    ) -> PriceLevel:
        """
        Retrieves a price level by ID.

        **IMPORTANT:** If you need to fetch multiple specific price levels by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the price level to retrieve.

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
            f"/quickbooks-desktop/price-levels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        currency_id: str | Omit = omit,
        fixed_percentage: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        per_item_price_levels: Iterable[price_level_update_params.PerItemPriceLevel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceLevel:
        """
        Updates an existing price level.

        Args:
          id: The QuickBooks-assigned unique identifier of the price level to update.

          revision_number: The current QuickBooks-assigned revision number of the price level object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_id: The price level's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          fixed_percentage: The fixed percentage adjustment applied to all items for this price level
              (instead of a per-item price level). Once you create the price level, you cannot
              change this.

              When this price level is applied to a customer, it automatically adjusts the
              `rate` and `amount` columns for applicable line items in sales orders and
              invoices for that customer. This value supports both positive and negative
              values - a value of "20" increases prices by 20%, while "-10" decreases prices
              by 10%.

          is_active: Indicates whether this price level is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this price level, unique across all price
              levels.

              **NOTE**: Price levels do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          per_item_price_levels: The per-item price level configurations for this price level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/price-levels/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "currency_id": currency_id,
                    "fixed_percentage": fixed_percentage,
                    "is_active": is_active,
                    "name": name,
                    "per_item_price_levels": per_item_price_levels,
                },
                price_level_update_params.PriceLevelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> PriceLevelListResponse:
        """Returns a list of price levels.

        NOTE: QuickBooks Desktop does not support
        pagination for price levels; hence, there is no `cursor` parameter. Users
        typically have few price levels.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_ids: Filter for price levels in these currencies.

          ids: Filter for specific price levels by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          item_ids: Filter for price levels containing these items.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              price levels. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all price levels without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because price levels typically have low record counts.

          name_contains: Filter for price levels whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for price levels whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for price levels whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific price levels by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a price level.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for price levels whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for price levels whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for price levels that are active, inactive, or both.

          updated_after: Filter for price levels updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for price levels updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/price-levels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_ids": currency_ids,
                        "ids": ids,
                        "item_ids": item_ids,
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
                    price_level_list_params.PriceLevelListParams,
                ),
            ),
            cast_to=PriceLevelListResponse,
        )


class AsyncPriceLevelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceLevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceLevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncPriceLevelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        currency_id: str | Omit = omit,
        fixed_percentage: str | Omit = omit,
        is_active: bool | Omit = omit,
        per_item_price_levels: Iterable[price_level_create_params.PerItemPriceLevel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceLevel:
        """
        Creates a new price level.

        Args:
          name: The case-insensitive unique name of this price level, unique across all price
              levels.

              **NOTE**: Price levels do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_id: The price level's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          fixed_percentage: The fixed percentage adjustment applied to all items for this price level
              (instead of a per-item price level). Once you create the price level, you cannot
              change this.

              When this price level is applied to a customer, it automatically adjusts the
              `rate` and `amount` columns for applicable line items in sales orders and
              invoices for that customer. This value supports both positive and negative
              values - a value of "20" increases prices by 20%, while "-10" decreases prices
              by 10%.

          is_active: Indicates whether this price level is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          per_item_price_levels: The per-item price level configurations for this price level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/price-levels",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "currency_id": currency_id,
                    "fixed_percentage": fixed_percentage,
                    "is_active": is_active,
                    "per_item_price_levels": per_item_price_levels,
                },
                price_level_create_params.PriceLevelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
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
    ) -> PriceLevel:
        """
        Retrieves a price level by ID.

        **IMPORTANT:** If you need to fetch multiple specific price levels by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the price level to retrieve.

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
            f"/quickbooks-desktop/price-levels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        currency_id: str | Omit = omit,
        fixed_percentage: str | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        per_item_price_levels: Iterable[price_level_update_params.PerItemPriceLevel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceLevel:
        """
        Updates an existing price level.

        Args:
          id: The QuickBooks-assigned unique identifier of the price level to update.

          revision_number: The current QuickBooks-assigned revision number of the price level object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_id: The price level's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          fixed_percentage: The fixed percentage adjustment applied to all items for this price level
              (instead of a per-item price level). Once you create the price level, you cannot
              change this.

              When this price level is applied to a customer, it automatically adjusts the
              `rate` and `amount` columns for applicable line items in sales orders and
              invoices for that customer. This value supports both positive and negative
              values - a value of "20" increases prices by 20%, while "-10" decreases prices
              by 10%.

          is_active: Indicates whether this price level is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this price level, unique across all price
              levels.

              **NOTE**: Price levels do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          per_item_price_levels: The per-item price level configurations for this price level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/price-levels/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "currency_id": currency_id,
                    "fixed_percentage": fixed_percentage,
                    "is_active": is_active,
                    "name": name,
                    "per_item_price_levels": per_item_price_levels,
                },
                price_level_update_params.PriceLevelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceLevel,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> PriceLevelListResponse:
        """Returns a list of price levels.

        NOTE: QuickBooks Desktop does not support
        pagination for price levels; hence, there is no `cursor` parameter. Users
        typically have few price levels.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          currency_ids: Filter for price levels in these currencies.

          ids: Filter for specific price levels by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          item_ids: Filter for price levels containing these items.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              price levels. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all price levels without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because price levels typically have low record counts.

          name_contains: Filter for price levels whose `name` contains this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for price levels whose `name` ends with this substring, case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for price levels whose `name` is alphabetically greater than or equal to
              this value.

          names: Filter for specific price levels by their name(s), case-insensitive. Like `id`,
              `name` is a unique identifier for a price level.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          name_starts_with: Filter for price levels whose `name` starts with this substring,
              case-insensitive.

              **NOTE**: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for price levels whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for price levels that are active, inactive, or both.

          updated_after: Filter for price levels updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for price levels updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/price-levels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency_ids": currency_ids,
                        "ids": ids,
                        "item_ids": item_ids,
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
                    price_level_list_params.PriceLevelListParams,
                ),
            ),
            cast_to=PriceLevelListResponse,
        )


class PriceLevelsResourceWithRawResponse:
    def __init__(self, price_levels: PriceLevelsResource) -> None:
        self._price_levels = price_levels

        self.create = to_raw_response_wrapper(
            price_levels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            price_levels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            price_levels.update,
        )
        self.list = to_raw_response_wrapper(
            price_levels.list,
        )


class AsyncPriceLevelsResourceWithRawResponse:
    def __init__(self, price_levels: AsyncPriceLevelsResource) -> None:
        self._price_levels = price_levels

        self.create = async_to_raw_response_wrapper(
            price_levels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            price_levels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            price_levels.update,
        )
        self.list = async_to_raw_response_wrapper(
            price_levels.list,
        )


class PriceLevelsResourceWithStreamingResponse:
    def __init__(self, price_levels: PriceLevelsResource) -> None:
        self._price_levels = price_levels

        self.create = to_streamed_response_wrapper(
            price_levels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            price_levels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            price_levels.update,
        )
        self.list = to_streamed_response_wrapper(
            price_levels.list,
        )


class AsyncPriceLevelsResourceWithStreamingResponse:
    def __init__(self, price_levels: AsyncPriceLevelsResource) -> None:
        self._price_levels = price_levels

        self.create = async_to_streamed_response_wrapper(
            price_levels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            price_levels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            price_levels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            price_levels.list,
        )
