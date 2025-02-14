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
from ...types.qbd import service_item_list_params, service_item_create_params, service_item_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.service_item import ServiceItem

__all__ = ["ServiceItemsResource", "AsyncServiceItemsResource"]


class ServiceItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return ServiceItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return ServiceItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: service_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Creates a new service item.

        Args:
          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two service items could both have the `name`
              "Web-Design", but they could have unique `fullName` values, such as
              "Consulting:Web-Design" and "Contracting:Web-Design".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Consulting:Web-Design", its parent has
              a `fullName` of "Consulting". If this service item is at the top level, this
              field will be `null`.

          sales_and_purchase_details: Details for service items that are both purchased and sold, such as reimbursable
              expenses or inventory items that are bought from vendors and sold to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating a service item, but never both because an
              item cannot have both configurations.

          sales_or_purchase_details: Details for service items that are exclusively sold or exclusively purchased,
              but not both. This typically applies to non-inventory items (like a purchased
              office supply that isn't resold) or service items (like consulting services that
              are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating a service item, but never both because
              an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this service item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit-of-measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/service-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_create_params.ServiceItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
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
    ) -> ServiceItem:
        """
        Retrieves a service item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to retrieve.

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
            f"/quickbooks-desktop/service-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: service_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_update_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_update_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Updates an existing service item.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to update.

          revision_number: The current QuickBooks-assigned revision number of the service item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the service item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two service items could both have the `name`
              "Web-Design", but they could have unique `fullName` values, such as
              "Consulting:Web-Design" and "Contracting:Web-Design".

              Maximum length: 31 characters.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Consulting:Web-Design", its parent has
              a `fullName` of "Consulting". If this service item is at the top level, this
              field will be `null`.

          sales_and_purchase_details: Details for service items that are both purchased and sold, such as reimbursable
              expenses or inventory items that are bought from vendors and sold to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying a service item because an item cannot
              have both configurations.

          sales_or_purchase_details: Details for service items that are exclusively sold or exclusively purchased,
              but not both. This typically applies to non-inventory items (like a purchased
              office supply that isn't resold) or service items (like consulting services that
              are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying a service item because an item cannot
              have both configurations.

          sales_tax_code_id: The default sales-tax code for this service item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit-of-measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/service-items/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_update_params.ServiceItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncCursorPage[ServiceItem]:
        """Returns a list of service items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for service items of these classes. A class is a way end-users can
              categorize service items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific service items by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a service item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a service item is under "Consulting" and has the `name`
              "Web-Design", its `fullName` would be "Consulting:Web-Design".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific service items by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for service items whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for service items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for service items whose `name` is alphabetically greater than or equal to
              this value.

          name_starts_with: Filter for service items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for service items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for service items that are active, inactive, or both.

          updated_after: Filter for service items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for service items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/service-items",
            page=SyncCursorPage[ServiceItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "cursor": cursor,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    service_item_list_params.ServiceItemListParams,
                ),
            ),
            model=ServiceItem,
        )


class AsyncServiceItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncServiceItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: service_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Creates a new service item.

        Args:
          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two service items could both have the `name`
              "Web-Design", but they could have unique `fullName` values, such as
              "Consulting:Web-Design" and "Contracting:Web-Design".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Consulting:Web-Design", its parent has
              a `fullName` of "Consulting". If this service item is at the top level, this
              field will be `null`.

          sales_and_purchase_details: Details for service items that are both purchased and sold, such as reimbursable
              expenses or inventory items that are bought from vendors and sold to customers.

              **IMPORTANT**: You must specify either `salesAndPurchaseDetails` or
              `salesOrPurchaseDetails` when creating a service item, but never both because an
              item cannot have both configurations.

          sales_or_purchase_details: Details for service items that are exclusively sold or exclusively purchased,
              but not both. This typically applies to non-inventory items (like a purchased
              office supply that isn't resold) or service items (like consulting services that
              are sold but not purchased).

              **IMPORTANT**: You must specify either `salesOrPurchaseDetails` or
              `salesAndPurchaseDetails` when creating a service item, but never both because
              an item cannot have both configurations.

          sales_tax_code_id: The default sales-tax code for this service item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit-of-measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/service-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_create_params.ServiceItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
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
    ) -> ServiceItem:
        """
        Retrieves a service item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to retrieve.

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
            f"/quickbooks-desktop/service-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        barcode: service_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_update_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_update_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Updates an existing service item.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to update.

          revision_number: The current QuickBooks-assigned revision number of the service item object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the service item's unit-of-measure set
              (using the `unitOfMeasureSetId` field) when the base unit of the new
              unit-of-measure set does not match that of the currently assigned set. Without
              setting this field to `true` in this scenario, the request will fail with an
              error; hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              NOTE: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              unit-of-measure set and deactivating the old item.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its hierarchical parent objects like
              `fullName` does. For example, two service items could both have the `name`
              "Web-Design", but they could have unique `fullName` values, such as
              "Consulting:Web-Design" and "Contracting:Web-Design".

              Maximum length: 31 characters.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Consulting:Web-Design", its parent has
              a `fullName` of "Consulting". If this service item is at the top level, this
              field will be `null`.

          sales_and_purchase_details: Details for service items that are both purchased and sold, such as reimbursable
              expenses or inventory items that are bought from vendors and sold to customers.

              **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
              `salesOrPurchaseDetails` when modifying a service item because an item cannot
              have both configurations.

          sales_or_purchase_details: Details for service items that are exclusively sold or exclusively purchased,
              but not both. This typically applies to non-inventory items (like a purchased
              office supply that isn't resold) or service items (like consulting services that
              are sold but not purchased).

              **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
              `salesAndPurchaseDetails` when modifying a service item because an item cannot
              have both configurations.

          sales_tax_code_id: The default sales-tax code for this service item, determining whether it is
              taxable or non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit-of-measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/service-items/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_update_params.ServiceItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[ServiceItem, AsyncCursorPage[ServiceItem]]:
        """Returns a list of service items.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for service items of these classes. A class is a way end-users can
              categorize service items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          full_names: Filter for specific service items by their full-name(s), case-insensitive. Like
              `id`, `fullName` is a unique identifier for a service item, formed by by
              combining the names of its parent objects with its own `name`, separated by
              colons. For example, if a service item is under "Consulting" and has the `name`
              "Web-Design", its `fullName` would be "Consulting:Web-Design".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific service items by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          name_contains: Filter for service items whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for service items whose `name` ends with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameStartsWith`.

          name_from: Filter for service items whose `name` is alphabetically greater than or equal to
              this value.

          name_starts_with: Filter for service items whose `name` starts with this substring,
              case-insensitive. NOTE: If you use this parameter, you cannot also use
              `nameContains` or `nameEndsWith`.

          name_to: Filter for service items whose `name` is alphabetically less than or equal to
              this value.

          status: Filter for service items that are active, inactive, or both.

          updated_after: Filter for service items updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for service items updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/service-items",
            page=AsyncCursorPage[ServiceItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "cursor": cursor,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    service_item_list_params.ServiceItemListParams,
                ),
            ),
            model=ServiceItem,
        )


class ServiceItemsResourceWithRawResponse:
    def __init__(self, service_items: ServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = to_raw_response_wrapper(
            service_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            service_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            service_items.update,
        )
        self.list = to_raw_response_wrapper(
            service_items.list,
        )


class AsyncServiceItemsResourceWithRawResponse:
    def __init__(self, service_items: AsyncServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = async_to_raw_response_wrapper(
            service_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            service_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            service_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            service_items.list,
        )


class ServiceItemsResourceWithStreamingResponse:
    def __init__(self, service_items: ServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = to_streamed_response_wrapper(
            service_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            service_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            service_items.update,
        )
        self.list = to_streamed_response_wrapper(
            service_items.list,
        )


class AsyncServiceItemsResourceWithStreamingResponse:
    def __init__(self, service_items: AsyncServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = async_to_streamed_response_wrapper(
            service_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            service_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            service_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            service_items.list,
        )
