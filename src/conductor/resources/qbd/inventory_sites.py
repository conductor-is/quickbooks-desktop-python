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
from ...types.qbd import inventory_site_list_params, inventory_site_create_params, inventory_site_update_params
from ..._base_client import make_request_options
from ...types.qbd.inventory_site import InventorySite
from ...types.qbd.inventory_site_list_response import InventorySiteListResponse

__all__ = ["InventorySitesResource", "AsyncInventorySitesResource"]


class InventorySitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventorySitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return InventorySitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventorySitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return InventorySitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        address: inventory_site_create_params.Address | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventorySite:
        """
        Creates a new inventory site.

        Args:
          name: The case-insensitive unique name of this inventory site, unique across all
              inventory sites.

              **NOTE**: Inventory sites do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          address: The inventory site's address.

          description: A description of this inventory site.

          email: The inventory site's email address.

          is_active: Indicates whether this inventory site is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent inventory site one level above this one in the hierarchy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/inventory-sites",
            body=maybe_transform(
                {
                    "name": name,
                    "address": address,
                    "description": description,
                    "email": email,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                inventory_site_create_params.InventorySiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
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
    ) -> InventorySite:
        """
        Retrieves an inventory site by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory site to retrieve.

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
            f"/quickbooks-desktop/inventory-sites/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        address: inventory_site_update_params.Address | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventorySite:
        """
        Updates an existing inventory site.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory site to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory site object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          address: The inventory site's address.

          contact: The name of the primary contact person for this inventory site.

          description: A description of this inventory site.

          email: The inventory site's email address.

          fax: The inventory site's fax number.

          is_active: Indicates whether this inventory site is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this inventory site, unique across all
              inventory sites.

              **NOTE**: Inventory sites do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          parent_id: The parent inventory site one level above this one in the hierarchy.

          phone: The inventory site's primary telephone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/inventory-sites/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "address": address,
                    "contact": contact,
                    "description": description,
                    "email": email,
                    "fax": fax,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "phone": phone,
                },
                inventory_site_update_params.InventorySiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> InventorySiteListResponse:
        """Returns a list of inventory sites.

        NOTE: QuickBooks Desktop does not support
        pagination for inventory sites; hence, there is no `cursor` parameter. Users
        typically have few inventory sites.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific inventory sites by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_contains: Filter for inventory sites whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for inventory sites whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for inventory sites whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific inventory sites by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for an inventory site.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for inventory sites whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for inventory sites whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for inventory sites that are active, inactive, or both.

          updated_after: Filter for inventory sites updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for inventory sites updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/inventory-sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
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
                    inventory_site_list_params.InventorySiteListParams,
                ),
            ),
            cast_to=InventorySiteListResponse,
        )


class AsyncInventorySitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventorySitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventorySitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventorySitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncInventorySitesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        address: inventory_site_create_params.Address | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventorySite:
        """
        Creates a new inventory site.

        Args:
          name: The case-insensitive unique name of this inventory site, unique across all
              inventory sites.

              **NOTE**: Inventory sites do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          address: The inventory site's address.

          description: A description of this inventory site.

          email: The inventory site's email address.

          is_active: Indicates whether this inventory site is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent inventory site one level above this one in the hierarchy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/inventory-sites",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "address": address,
                    "description": description,
                    "email": email,
                    "is_active": is_active,
                    "parent_id": parent_id,
                },
                inventory_site_create_params.InventorySiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
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
    ) -> InventorySite:
        """
        Retrieves an inventory site by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory site to retrieve.

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
            f"/quickbooks-desktop/inventory-sites/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        address: inventory_site_update_params.Address | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventorySite:
        """
        Updates an existing inventory site.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory site to update.

          revision_number: The current QuickBooks-assigned revision number of the inventory site object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          address: The inventory site's address.

          contact: The name of the primary contact person for this inventory site.

          description: A description of this inventory site.

          email: The inventory site's email address.

          fax: The inventory site's fax number.

          is_active: Indicates whether this inventory site is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive unique name of this inventory site, unique across all
              inventory sites.

              **NOTE**: Inventory sites do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 31 characters.

          parent_id: The parent inventory site one level above this one in the hierarchy.

          phone: The inventory site's primary telephone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/inventory-sites/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "address": address,
                    "contact": contact,
                    "description": description,
                    "email": email,
                    "fax": fax,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "phone": phone,
                },
                inventory_site_update_params.InventorySiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventorySite,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> InventorySiteListResponse:
        """Returns a list of inventory sites.

        NOTE: QuickBooks Desktop does not support
        pagination for inventory sites; hence, there is no `cursor` parameter. Users
        typically have few inventory sites.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific inventory sites by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_contains: Filter for inventory sites whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for inventory sites whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for inventory sites whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific inventory sites by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for an inventory site.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for inventory sites whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for inventory sites whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for inventory sites that are active, inactive, or both.

          updated_after: Filter for inventory sites updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for inventory sites updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/inventory-sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
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
                    inventory_site_list_params.InventorySiteListParams,
                ),
            ),
            cast_to=InventorySiteListResponse,
        )


class InventorySitesResourceWithRawResponse:
    def __init__(self, inventory_sites: InventorySitesResource) -> None:
        self._inventory_sites = inventory_sites

        self.create = to_raw_response_wrapper(
            inventory_sites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inventory_sites.retrieve,
        )
        self.update = to_raw_response_wrapper(
            inventory_sites.update,
        )
        self.list = to_raw_response_wrapper(
            inventory_sites.list,
        )


class AsyncInventorySitesResourceWithRawResponse:
    def __init__(self, inventory_sites: AsyncInventorySitesResource) -> None:
        self._inventory_sites = inventory_sites

        self.create = async_to_raw_response_wrapper(
            inventory_sites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inventory_sites.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            inventory_sites.update,
        )
        self.list = async_to_raw_response_wrapper(
            inventory_sites.list,
        )


class InventorySitesResourceWithStreamingResponse:
    def __init__(self, inventory_sites: InventorySitesResource) -> None:
        self._inventory_sites = inventory_sites

        self.create = to_streamed_response_wrapper(
            inventory_sites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inventory_sites.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            inventory_sites.update,
        )
        self.list = to_streamed_response_wrapper(
            inventory_sites.list,
        )


class AsyncInventorySitesResourceWithStreamingResponse:
    def __init__(self, inventory_sites: AsyncInventorySitesResource) -> None:
        self._inventory_sites = inventory_sites

        self.create = async_to_streamed_response_wrapper(
            inventory_sites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inventory_sites.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            inventory_sites.update,
        )
        self.list = async_to_streamed_response_wrapper(
            inventory_sites.list,
        )
