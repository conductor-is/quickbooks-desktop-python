# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
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
from ...types.qbd import sales_order_list_params, sales_order_create_params, sales_order_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.sales_order import SalesOrder
from ...types.qbd.sales_order_delete_response import SalesOrderDeleteResponse

__all__ = ["SalesOrdersResource", "AsyncSalesOrdersResource"]


class SalesOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return SalesOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return SalesOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: sales_order_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[sales_order_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[sales_order_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_channel_name: Literal["blank", "ecommerce"] | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_store_name: str | NotGiven = NOT_GIVEN,
        sales_store_type: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: sales_order_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesOrder:
        """
        Creates a new sales order.

        Args:
          customer_id: The customer or customer-job associated with this sales order.

          transaction_date: The date of this sales order, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The sales order's billing address.

          class_id: The sales order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales order's line items unless overridden at the
              line item level.

          customer_message_id: The message to display to the customer on the sales order.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales order when printed or displayed.

          due_date: The date by which this sales order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this sales order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_manually_closed: Indicates whether this sales order has been manually marked as closed, even if
              it has not been invoiced.

          is_queued_for_email: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales order.

          lines: The sales order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales order.

          memo: A memo or note for this sales order.

          other_custom_field: A built-in custom field for additional information specific to this sales order.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all sales orders for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this sales order. This
              field is often used to cross-reference the sales order with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this sales order, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user. When left blank
              in this create request, this field will be left blank in QuickBooks (i.e., it
              does _not_ auto-increment).

          sales_channel_name: The type of the sales channel for this sales order.

          sales_representative_id: The sales order's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_store_name: The name of the sales store for this sales order.

          sales_store_type: The type of the sales store for this sales order.

          sales_tax_code_id: The sales-tax code for this sales order, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              order's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this sales order is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales order's shipping address.

          shipping_date: The date when the products or services for this sales order were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales order, such as standard mail or
              overnight delivery.

          terms_id: The sales order's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-orders",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_channel_name": sales_channel_name,
                    "sales_representative_id": sales_representative_id,
                    "sales_store_name": sales_store_name,
                    "sales_store_type": sales_store_type,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                },
                sales_order_create_params.SalesOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
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
    ) -> SalesOrder:
        """
        Retrieves a sales order by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to retrieve.

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
            f"/quickbooks-desktop/sales-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: sales_order_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[sales_order_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[sales_order_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_channel_name: Literal["blank", "ecommerce"] | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_store_name: str | NotGiven = NOT_GIVEN,
        sales_store_type: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: sales_order_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesOrder:
        """
        Updates an existing sales order.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to update.

          revision_number: The current QuickBooks-assigned revision number of the sales order object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The sales order's billing address.

          class_id: The sales order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales order's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job associated with this sales order.

          customer_message_id: The message to display to the customer on the sales order.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales order when printed or displayed.

          due_date: The date by which this sales order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this sales order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_manually_closed: Indicates whether this sales order has been manually marked as closed, even if
              it has not been invoiced.

          is_queued_for_email: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the sales order with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The sales order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the sales order with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this sales order.

          other_custom_field: A built-in custom field for additional information specific to this sales order.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all sales orders for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this sales order. This
              field is often used to cross-reference the sales order with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this sales order, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user.

          sales_channel_name: The type of the sales channel for this sales order.

          sales_representative_id: The sales order's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_store_name: The name of the sales store for this sales order.

          sales_store_type: The type of the sales store for this sales order.

          sales_tax_code_id: The sales-tax code for this sales order, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              order's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this sales order is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales order's shipping address.

          shipping_date: The date when the products or services for this sales order were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales order, such as standard mail or
              overnight delivery.

          terms_id: The sales order's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this sales order, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/sales-orders/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_channel_name": sales_channel_name,
                    "sales_representative_id": sales_representative_id,
                    "sales_store_name": sales_store_name,
                    "sales_store_type": sales_store_type,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                sales_order_update_params.SalesOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[SalesOrder]:
        """Returns a list of sales orders.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          currency_ids: Filter for sales orders in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for sales orders created for these customers.

          ids: Filter for specific sales orders by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding sales order.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales orders whose `refNumber` contains this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales orders whose `refNumber` ends with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales orders whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific sales orders by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for sales orders whose `refNumber` starts with this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales orders whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for sales orders created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for sales orders created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for sales orders updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for sales orders updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/sales-orders",
            page=SyncCursorPage[SalesOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "customer_ids": customer_ids,
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
                    },
                    sales_order_list_params.SalesOrderListParams,
                ),
            ),
            model=SalesOrder,
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
    ) -> SalesOrderDeleteResponse:
        """Permanently deletes a a sales order.

        The deletion will fail if the sales order
        is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to delete.

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
            f"/quickbooks-desktop/sales-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrderDeleteResponse,
        )


class AsyncSalesOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncSalesOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: sales_order_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[sales_order_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[sales_order_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_channel_name: Literal["blank", "ecommerce"] | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_store_name: str | NotGiven = NOT_GIVEN,
        sales_store_type: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: sales_order_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesOrder:
        """
        Creates a new sales order.

        Args:
          customer_id: The customer or customer-job associated with this sales order.

          transaction_date: The date of this sales order, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The sales order's billing address.

          class_id: The sales order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales order's line items unless overridden at the
              line item level.

          customer_message_id: The message to display to the customer on the sales order.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales order when printed or displayed.

          due_date: The date by which this sales order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this sales order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_manually_closed: Indicates whether this sales order has been manually marked as closed, even if
              it has not been invoiced.

          is_queued_for_email: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales order.

          lines: The sales order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales order.

          memo: A memo or note for this sales order.

          other_custom_field: A built-in custom field for additional information specific to this sales order.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all sales orders for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this sales order. This
              field is often used to cross-reference the sales order with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this sales order, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user. When left blank
              in this create request, this field will be left blank in QuickBooks (i.e., it
              does _not_ auto-increment).

          sales_channel_name: The type of the sales channel for this sales order.

          sales_representative_id: The sales order's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_store_name: The name of the sales store for this sales order.

          sales_store_type: The type of the sales store for this sales order.

          sales_tax_code_id: The sales-tax code for this sales order, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              order's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this sales order is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales order's shipping address.

          shipping_date: The date when the products or services for this sales order were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales order, such as standard mail or
              overnight delivery.

          terms_id: The sales order's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-orders",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_channel_name": sales_channel_name,
                    "sales_representative_id": sales_representative_id,
                    "sales_store_name": sales_store_name,
                    "sales_store_type": sales_store_type,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                },
                sales_order_create_params.SalesOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
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
    ) -> SalesOrder:
        """
        Retrieves a sales order by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to retrieve.

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
            f"/quickbooks-desktop/sales-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: sales_order_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_manually_closed: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[sales_order_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[sales_order_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_channel_name: Literal["blank", "ecommerce"] | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_store_name: str | NotGiven = NOT_GIVEN,
        sales_store_type: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: sales_order_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SalesOrder:
        """
        Updates an existing sales order.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to update.

          revision_number: The current QuickBooks-assigned revision number of the sales order object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The sales order's billing address.

          class_id: The sales order's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales order's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job associated with this sales order.

          customer_message_id: The message to display to the customer on the sales order.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales order when printed or displayed.

          due_date: The date by which this sales order must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this sales order's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_manually_closed: Indicates whether this sales order has been manually marked as closed, even if
              it has not been invoiced.

          is_queued_for_email: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales order is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales order's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the sales order with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The sales order's line items, each representing a single product or service
              ordered.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the sales order with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this sales order.

          other_custom_field: A built-in custom field for additional information specific to this sales order.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all sales orders for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this sales order. This
              field is often used to cross-reference the sales order with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this sales order, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user.

          sales_channel_name: The type of the sales channel for this sales order.

          sales_representative_id: The sales order's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_store_name: The name of the sales store for this sales order.

          sales_store_type: The type of the sales store for this sales order.

          sales_tax_code_id: The sales-tax code for this sales order, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              order's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this sales order is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales order's shipping address.

          shipping_date: The date when the products or services for this sales order were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales order, such as standard mail or
              overnight delivery.

          terms_id: The sales order's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this sales order, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/sales-orders/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_manually_closed": is_manually_closed,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_channel_name": sales_channel_name,
                    "sales_representative_id": sales_representative_id,
                    "sales_store_name": sales_store_name,
                    "sales_store_type": sales_store_type,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                sales_order_update_params.SalesOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrder,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SalesOrder, AsyncCursorPage[SalesOrder]]:
        """Returns a list of sales orders.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          currency_ids: Filter for sales orders in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for sales orders created for these customers.

          ids: Filter for specific sales orders by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding sales order.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales orders whose `refNumber` contains this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales orders whose `refNumber` ends with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales orders whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific sales orders by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for sales orders whose `refNumber` starts with this substring. NOTE: If
              you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales orders whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for sales orders created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for sales orders created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for sales orders updated on or after this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 00:00:00 of that day.

          updated_before: Filter for sales orders updated on or before this date and time, in ISO 8601
              format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
              is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/sales-orders",
            page=AsyncCursorPage[SalesOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "customer_ids": customer_ids,
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
                    },
                    sales_order_list_params.SalesOrderListParams,
                ),
            ),
            model=SalesOrder,
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
    ) -> SalesOrderDeleteResponse:
        """Permanently deletes a a sales order.

        The deletion will fail if the sales order
        is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales order to delete.

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
            f"/quickbooks-desktop/sales-orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesOrderDeleteResponse,
        )


class SalesOrdersResourceWithRawResponse:
    def __init__(self, sales_orders: SalesOrdersResource) -> None:
        self._sales_orders = sales_orders

        self.create = to_raw_response_wrapper(
            sales_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_orders.update,
        )
        self.list = to_raw_response_wrapper(
            sales_orders.list,
        )
        self.delete = to_raw_response_wrapper(
            sales_orders.delete,
        )


class AsyncSalesOrdersResourceWithRawResponse:
    def __init__(self, sales_orders: AsyncSalesOrdersResource) -> None:
        self._sales_orders = sales_orders

        self.create = async_to_raw_response_wrapper(
            sales_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_orders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sales_orders.delete,
        )


class SalesOrdersResourceWithStreamingResponse:
    def __init__(self, sales_orders: SalesOrdersResource) -> None:
        self._sales_orders = sales_orders

        self.create = to_streamed_response_wrapper(
            sales_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_orders.list,
        )
        self.delete = to_streamed_response_wrapper(
            sales_orders.delete,
        )


class AsyncSalesOrdersResourceWithStreamingResponse:
    def __init__(self, sales_orders: AsyncSalesOrdersResource) -> None:
        self._sales_orders = sales_orders

        self.create = async_to_streamed_response_wrapper(
            sales_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_orders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sales_orders.delete,
        )
