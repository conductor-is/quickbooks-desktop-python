# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import item_site_list_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.item_site import ItemSite

__all__ = ["ItemSitesResource", "AsyncItemSitesResource"]


class ItemSitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemSitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return ItemSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemSitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return ItemSitesResourceWithStreamingResponse(self)

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
    ) -> ItemSite:
        """
        Retrieves an item site by ID.

        **IMPORTANT:** If you need to fetch multiple specific item sites by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the item site to retrieve.

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
            f"/quickbooks-desktop/item-sites/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemSite,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
            "all_except_fixed_asset",
            "assembly",
            "discount",
            "fixed_asset",
            "inventory",
            "inventory_and_assembly",
            "non_inventory",
            "other_charge",
            "payment",
            "sales",
            "sales_tax",
            "service",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        site_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ItemSite]:
        """Returns a list of item sites.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific item sites by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          item_ids: Filter for item sites for these items.

          item_type: Filter for item sites that match this item type.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          site_ids: Filter for item sites at these sites. A site represents a physical location,
              such as a warehouse or store.

          status: Filter for item sites that are active, inactive, or both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/item-sites",
            page=SyncCursorPage[ItemSite],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "limit": limit,
                        "site_ids": site_ids,
                        "status": status,
                    },
                    item_site_list_params.ItemSiteListParams,
                ),
            ),
            model=ItemSite,
        )


class AsyncItemSitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemSitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemSitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncItemSitesResourceWithStreamingResponse(self)

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
    ) -> ItemSite:
        """
        Retrieves an item site by ID.

        **IMPORTANT:** If you need to fetch multiple specific item sites by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the item site to retrieve.

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
            f"/quickbooks-desktop/item-sites/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemSite,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
        item_type: Literal[
            "all_except_fixed_asset",
            "assembly",
            "discount",
            "fixed_asset",
            "inventory",
            "inventory_and_assembly",
            "non_inventory",
            "other_charge",
            "payment",
            "sales",
            "sales_tax",
            "service",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        site_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["active", "all", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ItemSite, AsyncCursorPage[ItemSite]]:
        """Returns a list of item sites.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific item sites by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          item_ids: Filter for item sites for these items.

          item_type: Filter for item sites that match this item type.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          site_ids: Filter for item sites at these sites. A site represents a physical location,
              such as a warehouse or store.

          status: Filter for item sites that are active, inactive, or both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/item-sites",
            page=AsyncCursorPage[ItemSite],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "item_ids": item_ids,
                        "item_type": item_type,
                        "limit": limit,
                        "site_ids": site_ids,
                        "status": status,
                    },
                    item_site_list_params.ItemSiteListParams,
                ),
            ),
            model=ItemSite,
        )


class ItemSitesResourceWithRawResponse:
    def __init__(self, item_sites: ItemSitesResource) -> None:
        self._item_sites = item_sites

        self.retrieve = to_raw_response_wrapper(
            item_sites.retrieve,
        )
        self.list = to_raw_response_wrapper(
            item_sites.list,
        )


class AsyncItemSitesResourceWithRawResponse:
    def __init__(self, item_sites: AsyncItemSitesResource) -> None:
        self._item_sites = item_sites

        self.retrieve = async_to_raw_response_wrapper(
            item_sites.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            item_sites.list,
        )


class ItemSitesResourceWithStreamingResponse:
    def __init__(self, item_sites: ItemSitesResource) -> None:
        self._item_sites = item_sites

        self.retrieve = to_streamed_response_wrapper(
            item_sites.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            item_sites.list,
        )


class AsyncItemSitesResourceWithStreamingResponse:
    def __init__(self, item_sites: AsyncItemSitesResource) -> None:
        self._item_sites = item_sites

        self.retrieve = async_to_streamed_response_wrapper(
            item_sites.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            item_sites.list,
        )
