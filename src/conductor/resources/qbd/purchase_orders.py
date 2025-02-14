# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date

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
from ...types.qbd import purchase_order_list_params, purchase_order_create_params, purchase_order_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.purchase_order import PurchaseOrder
from ...types.qbd.purchase_order_delete_response import PurchaseOrderDeleteResponse

__all__ = ["PurchaseOrdersResource", "AsyncPurchaseOrdersResource"]


class PurchaseOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurchaseOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return PurchaseOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchaseOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return PurchaseOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        class_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expected_date: Union[str, date] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inventory_site_id: str | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[purchase_order_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[purchase_order_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field1: str | NotGiven = NOT_GIVEN,
        other_custom_field2: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: purchase_order_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        ship_to_entity_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_address: purchase_order_create_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        vendor_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrder:
        """
        Creates a new purchase order.

        Args:
          transaction_date: The date of this purchase order, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_id: The purchase order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this purchase order's line items unless overridden at the
              line item level.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this purchase order when printed or displayed.

          due_date: The date by which this purchase order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this purchase order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expected_date: The date on which shipment of this purchase order is expected to be completed,
              in ISO 8601 format (YYYY-MM-DD).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this purchase
              order is stored.

          is_queued_for_email: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The purchase order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              purchase order.

          lines: The purchase order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              purchase order.

          memo: A memo or note for this purchase order that appears in reports, but not on the
              purchase order.

          other_custom_field1: A built-in custom field for additional information specific to this purchase
              order. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all purchase orders for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Hidden by default in the QuickBooks UI.

          other_custom_field2: A second built-in custom field for additional information specific to this
              purchase order. Unlike the user-defined fields in the `customFields` array, this
              is a standard QuickBooks field that exists for all purchase orders for
              convenience. Like `otherCustomField1`, developers often use this field for
              tracking information that doesn't fit into other standard QuickBooks fields.
              Hidden by default in the QuickBooks UI.

          ref_number: The case-sensitive user-defined reference number for this purchase order, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this purchase order, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the purchase order's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          shipment_origin: The origin location from where the product associated with this purchase order
              is shipped. This is the point at which ownership and liability for goods
              transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
              this field, which stands for "freight on board". This field is informational and
              has no accounting implications.

          shipping_address: The purchase order's shipping address.

          shipping_method_id: The shipping method used for this purchase order, such as standard mail or
              overnight delivery.

          ship_to_entity_id: The customer, vendor, employee, or other entity to whom this purchase order is
              to be shipped.

          terms_id: The purchase order's payment terms, defining when payment is due and any
              applicable discounts.

          vendor_address: The address of the vendor who sent this purchase order.

          vendor_id: The vendor who sent this purchase order for goods or services purchased.

          vendor_message: A message to be printed on this purchase order for the vendor to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/purchase-orders",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "class_id": class_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expected_date": expected_date,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field1": other_custom_field1,
                    "other_custom_field2": other_custom_field2,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_method_id": shipping_method_id,
                    "ship_to_entity_id": ship_to_entity_id,
                    "terms_id": terms_id,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                    "vendor_message": vendor_message,
                },
                purchase_order_create_params.PurchaseOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
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
    ) -> PurchaseOrder:
        """
        Retrieves a purchase order by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to retrieve.

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
            f"/quickbooks-desktop/purchase-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        class_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expected_date: Union[str, date] | NotGiven = NOT_GIVEN,
        inventory_site_id: str | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[purchase_order_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[purchase_order_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field1: str | NotGiven = NOT_GIVEN,
        other_custom_field2: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: purchase_order_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        ship_to_entity_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        vendor_address: purchase_order_update_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        vendor_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrder:
        """
        Updates an existing purchase order.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to update.

          revision_number: The current QuickBooks-assigned revision number of the purchase order object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_id: The purchase order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this purchase order's line items unless overridden at the
              line item level.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this purchase order when printed or displayed.

          due_date: The date by which this purchase order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this purchase order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expected_date: The date on which shipment of this purchase order is expected to be completed,
              in ISO 8601 format (YYYY-MM-DD).

          inventory_site_id: The site location where inventory for the item associated with this purchase
              order is stored.

          is_manually_closed: Indicates whether this purchase order has been manually marked as closed, even
              if all items have not been received or the sale has not been cancelled. Once the
              purchase order is marked as closed, all of its line items become closed as well.
              You cannot change `isManuallyClosed` to `false` after the purchase order has
              been fully received.

          is_queued_for_email: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The purchase order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the purchase order with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The purchase order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the purchase order with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this purchase order that appears in reports, but not on the
              purchase order.

          other_custom_field1: A built-in custom field for additional information specific to this purchase
              order. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all purchase orders for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Hidden by default in the QuickBooks UI.

          other_custom_field2: A second built-in custom field for additional information specific to this
              purchase order. Unlike the user-defined fields in the `customFields` array, this
              is a standard QuickBooks field that exists for all purchase orders for
              convenience. Like `otherCustomField1`, developers often use this field for
              tracking information that doesn't fit into other standard QuickBooks fields.
              Hidden by default in the QuickBooks UI.

          ref_number: The case-sensitive user-defined reference number for this purchase order, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this purchase order, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the purchase order's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          shipment_origin: The origin location from where the product associated with this purchase order
              is shipped. This is the point at which ownership and liability for goods
              transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
              this field, which stands for "freight on board". This field is informational and
              has no accounting implications.

          shipping_address: The purchase order's shipping address.

          shipping_method_id: The shipping method used for this purchase order, such as standard mail or
              overnight delivery.

          ship_to_entity_id: The customer, vendor, employee, or other entity to whom this purchase order is
              to be shipped.

          terms_id: The purchase order's payment terms, defining when payment is due and any
              applicable discounts.

          transaction_date: The date of this purchase order, in ISO 8601 format (YYYY-MM-DD).

          vendor_address: The address of the vendor who sent this purchase order.

          vendor_id: The vendor who sent this purchase order for goods or services purchased.

          vendor_message: A message to be printed on this purchase order for the vendor to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/purchase-orders/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "class_id": class_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expected_date": expected_date,
                    "inventory_site_id": inventory_site_id,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field1": other_custom_field1,
                    "other_custom_field2": other_custom_field2,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_method_id": shipping_method_id,
                    "ship_to_entity_id": ship_to_entity_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                    "vendor_message": vendor_message,
                },
                purchase_order_update_params.PurchaseOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: List[str] | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        vendor_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[PurchaseOrder]:
        """Returns a list of purchase orders.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for purchase orders associated with these accounts.

          currency_ids: Filter for purchase orders in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific purchase orders by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding purchase order.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for purchase orders whose `refNumber` contains this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for purchase orders whose `refNumber` ends with this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for purchase orders whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific purchase orders by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with:
              Filter for purchase orders whose `refNumber` starts with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for purchase orders whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for purchase orders created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for purchase orders created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for purchase orders updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for purchase orders updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for purchase orders sent to these vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/purchase-orders",
            page=SyncCursorPage[PurchaseOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "include_linked_transactions": include_linked_transactions,
                        "limit": limit,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "vendor_ids": vendor_ids,
                    },
                    purchase_order_list_params.PurchaseOrderListParams,
                ),
            ),
            model=PurchaseOrder,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrderDeleteResponse:
        """Permanently deletes a a purchase order.

        The deletion will fail if the purchase
        order is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to delete.

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
        return self._delete(
            f"/quickbooks-desktop/purchase-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrderDeleteResponse,
        )


class AsyncPurchaseOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurchaseOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchaseOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchaseOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncPurchaseOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        class_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expected_date: Union[str, date] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        inventory_site_id: str | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[purchase_order_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[purchase_order_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field1: str | NotGiven = NOT_GIVEN,
        other_custom_field2: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: purchase_order_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        ship_to_entity_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_address: purchase_order_create_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        vendor_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrder:
        """
        Creates a new purchase order.

        Args:
          transaction_date: The date of this purchase order, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_id: The purchase order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this purchase order's line items unless overridden at the
              line item level.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this purchase order when printed or displayed.

          due_date: The date by which this purchase order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this purchase order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expected_date: The date on which shipment of this purchase order is expected to be completed,
              in ISO 8601 format (YYYY-MM-DD).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          inventory_site_id: The site location where inventory for the item associated with this purchase
              order is stored.

          is_queued_for_email: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The purchase order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              purchase order.

          lines: The purchase order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              purchase order.

          memo: A memo or note for this purchase order that appears in reports, but not on the
              purchase order.

          other_custom_field1: A built-in custom field for additional information specific to this purchase
              order. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all purchase orders for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Hidden by default in the QuickBooks UI.

          other_custom_field2: A second built-in custom field for additional information specific to this
              purchase order. Unlike the user-defined fields in the `customFields` array, this
              is a standard QuickBooks field that exists for all purchase orders for
              convenience. Like `otherCustomField1`, developers often use this field for
              tracking information that doesn't fit into other standard QuickBooks fields.
              Hidden by default in the QuickBooks UI.

          ref_number: The case-sensitive user-defined reference number for this purchase order, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this purchase order, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the purchase order's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          shipment_origin: The origin location from where the product associated with this purchase order
              is shipped. This is the point at which ownership and liability for goods
              transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
              this field, which stands for "freight on board". This field is informational and
              has no accounting implications.

          shipping_address: The purchase order's shipping address.

          shipping_method_id: The shipping method used for this purchase order, such as standard mail or
              overnight delivery.

          ship_to_entity_id: The customer, vendor, employee, or other entity to whom this purchase order is
              to be shipped.

          terms_id: The purchase order's payment terms, defining when payment is due and any
              applicable discounts.

          vendor_address: The address of the vendor who sent this purchase order.

          vendor_id: The vendor who sent this purchase order for goods or services purchased.

          vendor_message: A message to be printed on this purchase order for the vendor to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/purchase-orders",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "class_id": class_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expected_date": expected_date,
                    "external_id": external_id,
                    "inventory_site_id": inventory_site_id,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field1": other_custom_field1,
                    "other_custom_field2": other_custom_field2,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_method_id": shipping_method_id,
                    "ship_to_entity_id": ship_to_entity_id,
                    "terms_id": terms_id,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                    "vendor_message": vendor_message,
                },
                purchase_order_create_params.PurchaseOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
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
    ) -> PurchaseOrder:
        """
        Retrieves a purchase order by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to retrieve.

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
            f"/quickbooks-desktop/purchase-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        class_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expected_date: Union[str, date] | NotGiven = NOT_GIVEN,
        inventory_site_id: str | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[purchase_order_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[purchase_order_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field1: str | NotGiven = NOT_GIVEN,
        other_custom_field2: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: purchase_order_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        ship_to_entity_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        vendor_address: purchase_order_update_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        vendor_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrder:
        """
        Updates an existing purchase order.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to update.

          revision_number: The current QuickBooks-assigned revision number of the purchase order object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_id: The purchase order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this purchase order's line items unless overridden at the
              line item level.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this purchase order when printed or displayed.

          due_date: The date by which this purchase order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this purchase order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expected_date: The date on which shipment of this purchase order is expected to be completed,
              in ISO 8601 format (YYYY-MM-DD).

          inventory_site_id: The site location where inventory for the item associated with this purchase
              order is stored.

          is_manually_closed: Indicates whether this purchase order has been manually marked as closed, even
              if all items have not been received or the sale has not been cancelled. Once the
              purchase order is marked as closed, all of its line items become closed as well.
              You cannot change `isManuallyClosed` to `false` after the purchase order has
              been fully received.

          is_queued_for_email: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this purchase order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The purchase order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the purchase order with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The purchase order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the purchase order with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this purchase order that appears in reports, but not on the
              purchase order.

          other_custom_field1: A built-in custom field for additional information specific to this purchase
              order. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all purchase orders for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Hidden by default in the QuickBooks UI.

          other_custom_field2: A second built-in custom field for additional information specific to this
              purchase order. Unlike the user-defined fields in the `customFields` array, this
              is a standard QuickBooks field that exists for all purchase orders for
              convenience. Like `otherCustomField1`, developers often use this field for
              tracking information that doesn't fit into other standard QuickBooks fields.
              Hidden by default in the QuickBooks UI.

          ref_number: The case-sensitive user-defined reference number for this purchase order, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this purchase order, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the purchase order's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          shipment_origin: The origin location from where the product associated with this purchase order
              is shipped. This is the point at which ownership and liability for goods
              transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
              this field, which stands for "freight on board". This field is informational and
              has no accounting implications.

          shipping_address: The purchase order's shipping address.

          shipping_method_id: The shipping method used for this purchase order, such as standard mail or
              overnight delivery.

          ship_to_entity_id: The customer, vendor, employee, or other entity to whom this purchase order is
              to be shipped.

          terms_id: The purchase order's payment terms, defining when payment is due and any
              applicable discounts.

          transaction_date: The date of this purchase order, in ISO 8601 format (YYYY-MM-DD).

          vendor_address: The address of the vendor who sent this purchase order.

          vendor_id: The vendor who sent this purchase order for goods or services purchased.

          vendor_message: A message to be printed on this purchase order for the vendor to read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/purchase-orders/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "class_id": class_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expected_date": expected_date,
                    "inventory_site_id": inventory_site_id,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field1": other_custom_field1,
                    "other_custom_field2": other_custom_field2,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_method_id": shipping_method_id,
                    "ship_to_entity_id": ship_to_entity_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                    "vendor_message": vendor_message,
                },
                purchase_order_update_params.PurchaseOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrder,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: List[str] | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        vendor_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PurchaseOrder, AsyncCursorPage[PurchaseOrder]]:
        """Returns a list of purchase orders.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for purchase orders associated with these accounts.

          currency_ids: Filter for purchase orders in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific purchase orders by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding purchase order.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for purchase orders whose `refNumber` contains this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for purchase orders whose `refNumber` ends with this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for purchase orders whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific purchase orders by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with:
              Filter for purchase orders whose `refNumber` starts with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for purchase orders whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for purchase orders created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for purchase orders created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for purchase orders updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for purchase orders updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for purchase orders sent to these vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/purchase-orders",
            page=AsyncCursorPage[PurchaseOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "include_linked_transactions": include_linked_transactions,
                        "limit": limit,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                        "vendor_ids": vendor_ids,
                    },
                    purchase_order_list_params.PurchaseOrderListParams,
                ),
            ),
            model=PurchaseOrder,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseOrderDeleteResponse:
        """Permanently deletes a a purchase order.

        The deletion will fail if the purchase
        order is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the purchase order to delete.

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
        return await self._delete(
            f"/quickbooks-desktop/purchase-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseOrderDeleteResponse,
        )


class PurchaseOrdersResourceWithRawResponse:
    def __init__(self, purchase_orders: PurchaseOrdersResource) -> None:
        self._purchase_orders = purchase_orders

        self.create = to_raw_response_wrapper(
            purchase_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            purchase_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            purchase_orders.update,
        )
        self.list = to_raw_response_wrapper(
            purchase_orders.list,
        )
        self.delete = to_raw_response_wrapper(
            purchase_orders.delete,
        )


class AsyncPurchaseOrdersResourceWithRawResponse:
    def __init__(self, purchase_orders: AsyncPurchaseOrdersResource) -> None:
        self._purchase_orders = purchase_orders

        self.create = async_to_raw_response_wrapper(
            purchase_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            purchase_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            purchase_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            purchase_orders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            purchase_orders.delete,
        )


class PurchaseOrdersResourceWithStreamingResponse:
    def __init__(self, purchase_orders: PurchaseOrdersResource) -> None:
        self._purchase_orders = purchase_orders

        self.create = to_streamed_response_wrapper(
            purchase_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            purchase_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            purchase_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            purchase_orders.list,
        )
        self.delete = to_streamed_response_wrapper(
            purchase_orders.delete,
        )


class AsyncPurchaseOrdersResourceWithStreamingResponse:
    def __init__(self, purchase_orders: AsyncPurchaseOrdersResource) -> None:
        self._purchase_orders = purchase_orders

        self.create = async_to_streamed_response_wrapper(
            purchase_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            purchase_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            purchase_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            purchase_orders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            purchase_orders.delete,
        )
