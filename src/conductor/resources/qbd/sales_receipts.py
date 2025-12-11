# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

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
from ...types.qbd import sales_receipt_list_params, sales_receipt_create_params, sales_receipt_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.sales_receipt import SalesReceipt
from ...types.qbd.sales_receipt_delete_response import SalesReceiptDeleteResponse

__all__ = ["SalesReceiptsResource", "AsyncSalesReceiptsResource"]


class SalesReceiptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesReceiptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return SalesReceiptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesReceiptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return SalesReceiptsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: sales_receipt_create_params.BillingAddress | Omit = omit,
        check_number: str | Omit = omit,
        class_id: str | Omit = omit,
        credit_card_transaction: sales_receipt_create_params.CreditCardTransaction | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[sales_receipt_create_params.LineGroup] | Omit = omit,
        lines: Iterable[sales_receipt_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: sales_receipt_create_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesReceipt:
        """Creates a sales receipt for a sale paid in full.

        If you include credit card
        transaction details, QuickBooks requires the payment method to reference a
        credit card type and automatically deposits the funds to Undeposited Funds
        rather than a specific bank account.

        Args:
          transaction_date: The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The sales receipt's billing address.

          check_number: The check number of a check received for this sales receipt.

          class_id: The sales receipt's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales receipt's line items unless overridden at the
              line item level.

          credit_card_transaction: The credit card transaction data for this sales receipt's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          customer_id: The customer or customer-job to which the payment for this sales receipt is
              credited.

          customer_message_id: The message to display to the customer on the sales receipt.

          deposit_to_account_id: The account where the funds for this sales receipt will be or have been
              deposited.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales receipt when printed or displayed.

          due_date: The date by which this sales receipt must be paid, in ISO 8601 format
              (YYYY-MM-DD).

              **NOTE**: For sales receipts, this field is often `null` because sales receipts
              are generally used for point-of-sale payments, where full payment is received at
              the time of purchase.

          exchange_rate: The market exchange rate between this sales receipt's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_pending: Indicates whether this sales receipt has not been completed.

          is_queued_for_email: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales receipt's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales receipt.

          lines: The sales receipt's line items, each representing a single product or service
              sold.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales receipt.

          memo: A memo or note for this sales receipt that appears in reports, but not on the
              sales receipt.

          other_custom_field: A built-in custom field for additional information specific to this sales
              receipt. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all sales receipts for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Unlike `otherCustomField1` and
              `otherCustomField2`, which are line item fields, this exists at the transaction
              level. Hidden by default in the QuickBooks UI.

          payment_method_id: The sales receipt's payment method (e.g., cash, check, credit card).

              **NOTE**: If this sales receipt contains credit card transaction data supplied
              from QuickBooks Merchant Services (QBMS) transaction responses, you must specify
              a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          ref_number: The case-sensitive user-defined reference number for this sales receipt, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_representative_id: The sales receipt's sales representative. Sales representatives can be
              employees, vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this sales receipt, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              receipt's transactions by applying a specific tax rate collected for a single
              tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

              For sales receipts, while using this field to specify a single tax item/group
              that applies uniformly is recommended, complex tax scenarios may require
              alternative approaches. In such cases, you can set this field to a 0% tax item
              (conventionally named "Tax Calculated On Invoice") and handle tax calculations
              through line items instead. When using line items for taxes, note that only
              individual tax items (not tax groups) can be used, subtotals can help apply a
              tax to multiple items but only the first tax line after a subtotal is calculated
              automatically (subsequent tax lines require manual amounts), and the rate column
              will always display the actual tax amount rather than the rate percentage.

          shipment_origin: The origin location from where the product associated with this sales receipt is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales receipt's shipping address.

          shipping_date: The date when the products or services for this sales receipt were shipped or
              are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales receipt, such as standard mail or
              overnight delivery.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-receipts",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "check_number": check_number,
                    "class_id": class_id,
                    "credit_card_transaction": credit_card_transaction,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "payment_method_id": payment_method_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                },
                sales_receipt_create_params.SalesReceiptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
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
    ) -> SalesReceipt:
        """
        Retrieves a sales receipt by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales receipts by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to retrieve.

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
            f"/quickbooks-desktop/sales-receipts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: sales_receipt_update_params.BillingAddress | Omit = omit,
        check_number: str | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[sales_receipt_update_params.LineGroup] | Omit = omit,
        lines: Iterable[sales_receipt_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: sales_receipt_update_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesReceipt:
        """Updates an existing sales receipt.

        Credit card payments still have to use a
        credit-card payment method and remain deposited to Undeposited Funds, so don’t
        switch the deposit account in those scenarios.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to update.

          revision_number: The current QuickBooks-assigned revision number of the sales receipt object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The sales receipt's billing address.

          check_number: The check number of a check received for this sales receipt.

          class_id: The sales receipt's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales receipt's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job to which the payment for this sales receipt is
              credited.

          customer_message_id: The message to display to the customer on the sales receipt.

          deposit_to_account_id: The account where the funds for this sales receipt will be or have been
              deposited.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales receipt when printed or displayed.

          due_date: The date by which this sales receipt must be paid, in ISO 8601 format
              (YYYY-MM-DD).

              **NOTE**: For sales receipts, this field is often `null` because sales receipts
              are generally used for point-of-sale payments, where full payment is received at
              the time of purchase.

          exchange_rate: The market exchange rate between this sales receipt's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_pending: Indicates whether this sales receipt has not been completed.

          is_queued_for_email: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales receipt's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the sales receipt with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The sales receipt's line items, each representing a single product or service
              sold.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the sales receipt with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this sales receipt that appears in reports, but not on the
              sales receipt.

          other_custom_field: A built-in custom field for additional information specific to this sales
              receipt. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all sales receipts for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Unlike `otherCustomField1` and
              `otherCustomField2`, which are line item fields, this exists at the transaction
              level. Hidden by default in the QuickBooks UI.

          payment_method_id: The sales receipt's payment method (e.g., cash, check, credit card).

          ref_number: The case-sensitive user-defined reference number for this sales receipt, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The sales receipt's sales representative. Sales representatives can be
              employees, vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this sales receipt, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              receipt's transactions by applying a specific tax rate collected for a single
              tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

              For sales receipts, while using this field to specify a single tax item/group
              that applies uniformly is recommended, complex tax scenarios may require
              alternative approaches. In such cases, you can set this field to a 0% tax item
              (conventionally named "Tax Calculated On Invoice") and handle tax calculations
              through line items instead. When using line items for taxes, note that only
              individual tax items (not tax groups) can be used, subtotals can help apply a
              tax to multiple items but only the first tax line after a subtotal is calculated
              automatically (subsequent tax lines require manual amounts), and the rate column
              will always display the actual tax amount rather than the rate percentage.

          shipment_origin: The origin location from where the product associated with this sales receipt is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales receipt's shipping address.

          shipping_date: The date when the products or services for this sales receipt were shipped or
              are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales receipt, such as standard mail or
              overnight delivery.

          transaction_date: The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/sales-receipts/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "check_number": check_number,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "payment_method_id": payment_method_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "transaction_date": transaction_date,
                },
                sales_receipt_update_params.SalesReceiptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        limit: int | Omit = omit,
        ref_number_contains: str | Omit = omit,
        ref_number_ends_with: str | Omit = omit,
        ref_number_from: str | Omit = omit,
        ref_numbers: SequenceNotStr[str] | Omit = omit,
        ref_number_starts_with: str | Omit = omit,
        ref_number_to: str | Omit = omit,
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
    ) -> SyncCursorPage[SalesReceipt]:
        """Returns a list of sales receipts.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for sales receipts associated with these accounts.

          currency_ids: Filter for sales receipts in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for sales receipts created for these customers.

          ids: Filter for specific sales receipts by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales receipts whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales receipts whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales receipts whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific sales receipts by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for sales receipts whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales receipts whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for sales receipts whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for sales receipts whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for sales receipts updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales receipts updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/sales-receipts",
            page=SyncCursorPage[SalesReceipt],
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
                        "customer_ids": customer_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
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
                    sales_receipt_list_params.SalesReceiptListParams,
                ),
            ),
            model=SalesReceipt,
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
    ) -> SalesReceiptDeleteResponse:
        """Permanently deletes a a sales receipt.

        The deletion will fail if the sales
        receipt is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to delete.

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
            f"/quickbooks-desktop/sales-receipts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceiptDeleteResponse,
        )


class AsyncSalesReceiptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesReceiptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesReceiptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesReceiptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncSalesReceiptsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: sales_receipt_create_params.BillingAddress | Omit = omit,
        check_number: str | Omit = omit,
        class_id: str | Omit = omit,
        credit_card_transaction: sales_receipt_create_params.CreditCardTransaction | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[sales_receipt_create_params.LineGroup] | Omit = omit,
        lines: Iterable[sales_receipt_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: sales_receipt_create_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesReceipt:
        """Creates a sales receipt for a sale paid in full.

        If you include credit card
        transaction details, QuickBooks requires the payment method to reference a
        credit card type and automatically deposits the funds to Undeposited Funds
        rather than a specific bank account.

        Args:
          transaction_date: The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The sales receipt's billing address.

          check_number: The check number of a check received for this sales receipt.

          class_id: The sales receipt's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales receipt's line items unless overridden at the
              line item level.

          credit_card_transaction: The credit card transaction data for this sales receipt's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          customer_id: The customer or customer-job to which the payment for this sales receipt is
              credited.

          customer_message_id: The message to display to the customer on the sales receipt.

          deposit_to_account_id: The account where the funds for this sales receipt will be or have been
              deposited.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales receipt when printed or displayed.

          due_date: The date by which this sales receipt must be paid, in ISO 8601 format
              (YYYY-MM-DD).

              **NOTE**: For sales receipts, this field is often `null` because sales receipts
              are generally used for point-of-sale payments, where full payment is received at
              the time of purchase.

          exchange_rate: The market exchange rate between this sales receipt's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_pending: Indicates whether this sales receipt has not been completed.

          is_queued_for_email: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales receipt's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales receipt.

          lines: The sales receipt's line items, each representing a single product or service
              sold.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              sales receipt.

          memo: A memo or note for this sales receipt that appears in reports, but not on the
              sales receipt.

          other_custom_field: A built-in custom field for additional information specific to this sales
              receipt. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all sales receipts for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Unlike `otherCustomField1` and
              `otherCustomField2`, which are line item fields, this exists at the transaction
              level. Hidden by default in the QuickBooks UI.

          payment_method_id: The sales receipt's payment method (e.g., cash, check, credit card).

              **NOTE**: If this sales receipt contains credit card transaction data supplied
              from QuickBooks Merchant Services (QBMS) transaction responses, you must specify
              a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          ref_number: The case-sensitive user-defined reference number for this sales receipt, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_representative_id: The sales receipt's sales representative. Sales representatives can be
              employees, vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this sales receipt, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              receipt's transactions by applying a specific tax rate collected for a single
              tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

              For sales receipts, while using this field to specify a single tax item/group
              that applies uniformly is recommended, complex tax scenarios may require
              alternative approaches. In such cases, you can set this field to a 0% tax item
              (conventionally named "Tax Calculated On Invoice") and handle tax calculations
              through line items instead. When using line items for taxes, note that only
              individual tax items (not tax groups) can be used, subtotals can help apply a
              tax to multiple items but only the first tax line after a subtotal is calculated
              automatically (subsequent tax lines require manual amounts), and the rate column
              will always display the actual tax amount rather than the rate percentage.

          shipment_origin: The origin location from where the product associated with this sales receipt is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales receipt's shipping address.

          shipping_date: The date when the products or services for this sales receipt were shipped or
              are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales receipt, such as standard mail or
              overnight delivery.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-receipts",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "check_number": check_number,
                    "class_id": class_id,
                    "credit_card_transaction": credit_card_transaction,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "payment_method_id": payment_method_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                },
                sales_receipt_create_params.SalesReceiptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
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
    ) -> SalesReceipt:
        """
        Retrieves a sales receipt by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales receipts by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to retrieve.

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
            f"/quickbooks-desktop/sales-receipts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: sales_receipt_update_params.BillingAddress | Omit = omit,
        check_number: str | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[sales_receipt_update_params.LineGroup] | Omit = omit,
        lines: Iterable[sales_receipt_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: sales_receipt_update_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesReceipt:
        """Updates an existing sales receipt.

        Credit card payments still have to use a
        credit-card payment method and remain deposited to Undeposited Funds, so don’t
        switch the deposit account in those scenarios.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to update.

          revision_number: The current QuickBooks-assigned revision number of the sales receipt object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The sales receipt's billing address.

          check_number: The check number of a check received for this sales receipt.

          class_id: The sales receipt's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this sales receipt's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job to which the payment for this sales receipt is
              credited.

          customer_message_id: The message to display to the customer on the sales receipt.

          deposit_to_account_id: The account where the funds for this sales receipt will be or have been
              deposited.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this sales receipt when printed or displayed.

          due_date: The date by which this sales receipt must be paid, in ISO 8601 format
              (YYYY-MM-DD).

              **NOTE**: For sales receipts, this field is often `null` because sales receipts
              are generally used for point-of-sale payments, where full payment is received at
              the time of purchase.

          exchange_rate: The market exchange rate between this sales receipt's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_pending: Indicates whether this sales receipt has not been completed.

          is_queued_for_email: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this sales receipt is included in the queue of documents for
              QuickBooks to print.

          line_groups: The sales receipt's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the sales receipt with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The sales receipt's line items, each representing a single product or service
              sold.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the sales receipt with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this sales receipt that appears in reports, but not on the
              sales receipt.

          other_custom_field: A built-in custom field for additional information specific to this sales
              receipt. Unlike the user-defined fields in the `customFields` array, this is a
              standard QuickBooks field that exists for all sales receipts for convenience.
              Developers often use this field for tracking information that doesn't fit into
              other standard QuickBooks fields. Unlike `otherCustomField1` and
              `otherCustomField2`, which are line item fields, this exists at the transaction
              level. Hidden by default in the QuickBooks UI.

          payment_method_id: The sales receipt's payment method (e.g., cash, check, credit card).

          ref_number: The case-sensitive user-defined reference number for this sales receipt, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The sales receipt's sales representative. Sales representatives can be
              employees, vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this sales receipt, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this sales
              receipt's transactions by applying a specific tax rate collected for a single
              tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

              For sales receipts, while using this field to specify a single tax item/group
              that applies uniformly is recommended, complex tax scenarios may require
              alternative approaches. In such cases, you can set this field to a 0% tax item
              (conventionally named "Tax Calculated On Invoice") and handle tax calculations
              through line items instead. When using line items for taxes, note that only
              individual tax items (not tax groups) can be used, subtotals can help apply a
              tax to multiple items but only the first tax line after a subtotal is calculated
              automatically (subsequent tax lines require manual amounts), and the rate column
              will always display the actual tax amount rather than the rate percentage.

          shipment_origin: The origin location from where the product associated with this sales receipt is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The sales receipt's shipping address.

          shipping_date: The date when the products or services for this sales receipt were shipped or
              are expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this sales receipt, such as standard mail or
              overnight delivery.

          transaction_date: The date of this sales receipt, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/sales-receipts/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "check_number": check_number,
                    "class_id": class_id,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "payment_method_id": payment_method_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "transaction_date": transaction_date,
                },
                sales_receipt_update_params.SalesReceiptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceipt,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        limit: int | Omit = omit,
        ref_number_contains: str | Omit = omit,
        ref_number_ends_with: str | Omit = omit,
        ref_number_from: str | Omit = omit,
        ref_numbers: SequenceNotStr[str] | Omit = omit,
        ref_number_starts_with: str | Omit = omit,
        ref_number_to: str | Omit = omit,
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
    ) -> AsyncPaginator[SalesReceipt, AsyncCursorPage[SalesReceipt]]:
        """Returns a list of sales receipts.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for sales receipts associated with these accounts.

          currency_ids: Filter for sales receipts in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for sales receipts created for these customers.

          ids: Filter for specific sales receipts by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales receipts whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales receipts whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales receipts whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific sales receipts by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for sales receipts whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales receipts whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for sales receipts whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for sales receipts whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for sales receipts updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales receipts updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/sales-receipts",
            page=AsyncCursorPage[SalesReceipt],
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
                        "customer_ids": customer_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
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
                    sales_receipt_list_params.SalesReceiptListParams,
                ),
            ),
            model=SalesReceipt,
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
    ) -> SalesReceiptDeleteResponse:
        """Permanently deletes a a sales receipt.

        The deletion will fail if the sales
        receipt is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales receipt to delete.

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
            f"/quickbooks-desktop/sales-receipts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesReceiptDeleteResponse,
        )


class SalesReceiptsResourceWithRawResponse:
    def __init__(self, sales_receipts: SalesReceiptsResource) -> None:
        self._sales_receipts = sales_receipts

        self.create = to_raw_response_wrapper(
            sales_receipts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_receipts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_receipts.update,
        )
        self.list = to_raw_response_wrapper(
            sales_receipts.list,
        )
        self.delete = to_raw_response_wrapper(
            sales_receipts.delete,
        )


class AsyncSalesReceiptsResourceWithRawResponse:
    def __init__(self, sales_receipts: AsyncSalesReceiptsResource) -> None:
        self._sales_receipts = sales_receipts

        self.create = async_to_raw_response_wrapper(
            sales_receipts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_receipts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_receipts.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_receipts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sales_receipts.delete,
        )


class SalesReceiptsResourceWithStreamingResponse:
    def __init__(self, sales_receipts: SalesReceiptsResource) -> None:
        self._sales_receipts = sales_receipts

        self.create = to_streamed_response_wrapper(
            sales_receipts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_receipts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_receipts.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_receipts.list,
        )
        self.delete = to_streamed_response_wrapper(
            sales_receipts.delete,
        )


class AsyncSalesReceiptsResourceWithStreamingResponse:
    def __init__(self, sales_receipts: AsyncSalesReceiptsResource) -> None:
        self._sales_receipts = sales_receipts

        self.create = async_to_streamed_response_wrapper(
            sales_receipts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_receipts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_receipts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_receipts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sales_receipts.delete,
        )
