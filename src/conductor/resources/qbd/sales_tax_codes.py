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
from ...types.qbd import sales_tax_code_list_params, sales_tax_code_create_params, sales_tax_code_update_params
from ..._base_client import make_request_options
from ...types.qbd.sales_tax_code import SalesTaxCode
from ...types.qbd.sales_tax_code_list_response import SalesTaxCodeListResponse

__all__ = ["SalesTaxCodesResource", "AsyncSalesTaxCodesResource"]


class SalesTaxCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesTaxCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return SalesTaxCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesTaxCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return SalesTaxCodesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        is_taxable: bool,
        name: str,
        conductor_end_user_id: str,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesTaxCode:
        """
        Creates a new sales-tax code.

        Args:
          is_taxable: Indicates whether this sales-tax code is tracking taxable sales. This field
              cannot be modified once the sales-tax code has been used in a transaction.

          name: The case-insensitive unique name of this sales-tax code, unique across all
              sales-tax codes. This short name will appear on sales forms to identify the tax
              status of an item.

              **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 3 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          description: A description of this sales-tax code.

          is_active: Indicates whether this sales-tax code is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales-tax
              code's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-tax-codes",
            body=maybe_transform(
                {
                    "is_taxable": is_taxable,
                    "name": name,
                    "description": description,
                    "is_active": is_active,
                    "sales_tax_item_id": sales_tax_item_id,
                },
                sales_tax_code_create_params.SalesTaxCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
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
    ) -> SalesTaxCode:
        """
        Retrieves a sales-tax code by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax code to retrieve.

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
            f"/quickbooks-desktop/sales-tax-codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_taxable: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesTaxCode:
        """
        Updates an existing sales-tax code.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax code to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax code object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          description: A description of this sales-tax code.

          is_active: Indicates whether this sales-tax code is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          is_taxable: Indicates whether this sales-tax code is tracking taxable sales. This field
              cannot be modified once the sales-tax code has been used in a transaction.

          name: The case-insensitive unique name of this sales-tax code, unique across all
              sales-tax codes. This short name will appear on sales forms to identify the tax
              status of an item.

              **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 3 characters.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales-tax
              code's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/sales-tax-codes/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "description": description,
                    "is_active": is_active,
                    "is_taxable": is_taxable,
                    "name": name,
                    "sales_tax_item_id": sales_tax_item_id,
                },
                sales_tax_code_update_params.SalesTaxCodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
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
    ) -> SalesTaxCodeListResponse:
        """Returns a list of sales-tax codes.

        NOTE: QuickBooks Desktop does not support
        pagination for sales-tax codes; hence, there is no `cursor` parameter. Users
        typically have few sales-tax codes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific sales-tax codes by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              sales-tax codes. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all sales-tax codes without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because sales-tax codes typically have low record counts.

          name_contains: Filter for sales-tax codes whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for sales-tax codes whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for sales-tax codes whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific sales-tax codes by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a sales-tax code.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for sales-tax codes whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for sales-tax codes whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for sales-tax codes that are active, inactive, or both.

          updated_after: Filter for sales-tax codes updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for sales-tax codes updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/sales-tax-codes",
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
                    sales_tax_code_list_params.SalesTaxCodeListParams,
                ),
            ),
            cast_to=SalesTaxCodeListResponse,
        )


class AsyncSalesTaxCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesTaxCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesTaxCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesTaxCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncSalesTaxCodesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        is_taxable: bool,
        name: str,
        conductor_end_user_id: str,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesTaxCode:
        """
        Creates a new sales-tax code.

        Args:
          is_taxable: Indicates whether this sales-tax code is tracking taxable sales. This field
              cannot be modified once the sales-tax code has been used in a transaction.

          name: The case-insensitive unique name of this sales-tax code, unique across all
              sales-tax codes. This short name will appear on sales forms to identify the tax
              status of an item.

              **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 3 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          description: A description of this sales-tax code.

          is_active: Indicates whether this sales-tax code is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales-tax
              code's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-tax-codes",
            body=await async_maybe_transform(
                {
                    "is_taxable": is_taxable,
                    "name": name,
                    "description": description,
                    "is_active": is_active,
                    "sales_tax_item_id": sales_tax_item_id,
                },
                sales_tax_code_create_params.SalesTaxCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
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
    ) -> SalesTaxCode:
        """
        Retrieves a sales-tax code by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax code to retrieve.

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
            f"/quickbooks-desktop/sales-tax-codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_taxable: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesTaxCode:
        """
        Updates an existing sales-tax code.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax code to update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax code object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          description: A description of this sales-tax code.

          is_active: Indicates whether this sales-tax code is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          is_taxable: Indicates whether this sales-tax code is tracking taxable sales. This field
              cannot be modified once the sales-tax code has been used in a transaction.

          name: The case-insensitive unique name of this sales-tax code, unique across all
              sales-tax codes. This short name will appear on sales forms to identify the tax
              status of an item.

              **NOTE**: Sales-tax codes do not have a `fullName` field because they are not
              hierarchical objects, which is why `name` is unique for them but not for objects
              that have parents.

              Maximum length: 3 characters.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales-tax
              code's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/sales-tax-codes/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "description": description,
                    "is_active": is_active,
                    "is_taxable": is_taxable,
                    "name": name,
                    "sales_tax_item_id": sales_tax_item_id,
                },
                sales_tax_code_update_params.SalesTaxCodeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxCode,
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
    ) -> SalesTaxCodeListResponse:
        """Returns a list of sales-tax codes.

        NOTE: QuickBooks Desktop does not support
        pagination for sales-tax codes; hence, there is no `cursor` parameter. Users
        typically have few sales-tax codes.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          ids: Filter for specific sales-tax codes by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              sales-tax codes. This parameter will limit the response size, but you cannot
              fetch subsequent results using a cursor. For pagination, use the name-range
              parameters instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all sales-tax codes without
              limit, unlike paginated endpoints which default to 150 records. This is
              acceptable because sales-tax codes typically have low record counts.

          name_contains: Filter for sales-tax codes whose `name` contains this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for sales-tax codes whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for sales-tax codes whose `name` is alphabetically greater than or equal
              to this value.

          names: Filter for specific sales-tax codes by their name(s), case-insensitive. Like
              `id`, `name` is a unique identifier for a sales-tax code.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          name_starts_with: Filter for sales-tax codes whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for sales-tax codes whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for sales-tax codes that are active, inactive, or both.

          updated_after: Filter for sales-tax codes updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for sales-tax codes updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/sales-tax-codes",
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
                    sales_tax_code_list_params.SalesTaxCodeListParams,
                ),
            ),
            cast_to=SalesTaxCodeListResponse,
        )


class SalesTaxCodesResourceWithRawResponse:
    def __init__(self, sales_tax_codes: SalesTaxCodesResource) -> None:
        self._sales_tax_codes = sales_tax_codes

        self.create = to_raw_response_wrapper(
            sales_tax_codes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_tax_codes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_tax_codes.update,
        )
        self.list = to_raw_response_wrapper(
            sales_tax_codes.list,
        )


class AsyncSalesTaxCodesResourceWithRawResponse:
    def __init__(self, sales_tax_codes: AsyncSalesTaxCodesResource) -> None:
        self._sales_tax_codes = sales_tax_codes

        self.create = async_to_raw_response_wrapper(
            sales_tax_codes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_tax_codes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_tax_codes.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_tax_codes.list,
        )


class SalesTaxCodesResourceWithStreamingResponse:
    def __init__(self, sales_tax_codes: SalesTaxCodesResource) -> None:
        self._sales_tax_codes = sales_tax_codes

        self.create = to_streamed_response_wrapper(
            sales_tax_codes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_tax_codes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_tax_codes.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_tax_codes.list,
        )


class AsyncSalesTaxCodesResourceWithStreamingResponse:
    def __init__(self, sales_tax_codes: AsyncSalesTaxCodesResource) -> None:
        self._sales_tax_codes = sales_tax_codes

        self.create = async_to_streamed_response_wrapper(
            sales_tax_codes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_tax_codes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_tax_codes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_tax_codes.list,
        )
