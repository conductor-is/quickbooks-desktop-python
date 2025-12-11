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
from ...types.qbd import credit_memo_list_params, credit_memo_create_params, credit_memo_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.credit_memo import CreditMemo
from ...types.qbd.credit_memo_delete_response import CreditMemoDeleteResponse

__all__ = ["CreditMemosResource", "AsyncCreditMemosResource"]


class CreditMemosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditMemosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return CreditMemosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditMemosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return CreditMemosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: credit_memo_create_params.BillingAddress | Omit = omit,
        class_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[credit_memo_create_params.LineGroup] | Omit = omit,
        lines: Iterable[credit_memo_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        purchase_order_number: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: credit_memo_create_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        terms_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditMemo:
        """
        Creates a new credit memo.

        Args:
          customer_id: The customer or customer-job associated with this credit memo.

          transaction_date: The date of this credit memo, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The credit memo's billing address.

          class_id: The credit memo's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this credit memo's line items unless overridden at the
              line item level.

          customer_message_id: The message to display to the customer on the credit memo.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this credit memo when printed or displayed.

          due_date: The date by which this credit memo must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this credit memo's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_pending: Indicates whether this credit memo has not been completed.

          is_queued_for_email: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to print.

          line_groups: The credit memo's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              credit memo.

          lines: The credit memo's line items, each representing a single product or service
              sold.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              credit memo.

          memo: A memo or note for this credit memo that appears in the account register and
              customer register, but not on the credit memo itself.

          other_custom_field: A built-in custom field for additional information specific to this credit memo.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all credit memos for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this credit memo. This
              field is often used to cross-reference the credit memo with the customer's
              purchasing system.

              Maximum length: 25 characters.

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit memo is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this credit memo is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this credit memo, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user. When left blank
              in this create request, this field will be left blank in QuickBooks (i.e., it
              does _not_ auto-increment).

          sales_representative_id: The credit memo's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this credit memo, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this credit
              memo's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this credit memo is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The credit memo's shipping address.

          shipping_date: The date when the products or services for this credit memo were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this credit memo, such as standard mail or
              overnight delivery.

          terms_id: The credit memo's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/credit-memos",
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
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                },
                credit_memo_create_params.CreditMemoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
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
    ) -> CreditMemo:
        """
        Retrieves a credit memo by ID.

        **IMPORTANT:** If you need to fetch multiple specific credit memos by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        NOTE: The response automatically includes any linked transactions.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to retrieve.

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
            f"/quickbooks-desktop/credit-memos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: credit_memo_update_params.BillingAddress | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[credit_memo_update_params.LineGroup] | Omit = omit,
        lines: Iterable[credit_memo_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        purchase_order_number: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: credit_memo_update_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        terms_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditMemo:
        """
        Updates an existing credit memo.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to update.

          revision_number: The current QuickBooks-assigned revision number of the credit memo object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The credit memo's billing address.

          class_id: The credit memo's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this credit memo's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job associated with this credit memo.

          customer_message_id: The message to display to the customer on the credit memo.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this credit memo when printed or displayed.

          due_date: The date by which this credit memo must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this credit memo's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_pending: Indicates whether this credit memo has not been completed.

          is_queued_for_email: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to print.

          line_groups: The credit memo's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the credit memo with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The credit memo's line items, each representing a single product or service
              sold.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the credit memo with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this credit memo that appears in the account register and
              customer register, but not on the credit memo itself.

          other_custom_field: A built-in custom field for additional information specific to this credit memo.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all credit memos for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this credit memo. This
              field is often used to cross-reference the credit memo with the customer's
              purchasing system.

              Maximum length: 25 characters.

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit memo is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this credit memo is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this credit memo, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The credit memo's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this credit memo, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this credit
              memo's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this credit memo is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The credit memo's shipping address.

          shipping_date: The date when the products or services for this credit memo were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this credit memo, such as standard mail or
              overnight delivery.

          terms_id: The credit memo's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this credit memo, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/credit-memos/{id}",
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
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                credit_memo_update_params.CreditMemoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
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
        include_linked_transactions: bool | Omit = omit,
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
    ) -> SyncCursorPage[CreditMemo]:
        """Returns a list of credit memos.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for credit memos associated with these accounts.

          currency_ids: Filter for credit memos in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for credit memos created for these customers. These are the customers who
              are owed money.

          ids: Filter for specific credit memos by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding credit memo.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for credit memos whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for credit memos whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit memos whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific credit memos by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for credit memos whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit memos whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit memos whose `date` field is on or after this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for credit memos whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for credit memos updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for credit memos updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/credit-memos",
            page=SyncCursorPage[CreditMemo],
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
                    credit_memo_list_params.CreditMemoListParams,
                ),
            ),
            model=CreditMemo,
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
    ) -> CreditMemoDeleteResponse:
        """Permanently deletes a a credit memo.

        The deletion will fail if the credit memo
        is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to delete.

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
            f"/quickbooks-desktop/credit-memos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemoDeleteResponse,
        )


class AsyncCreditMemosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditMemosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditMemosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditMemosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncCreditMemosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: credit_memo_create_params.BillingAddress | Omit = omit,
        class_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[credit_memo_create_params.LineGroup] | Omit = omit,
        lines: Iterable[credit_memo_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        purchase_order_number: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: credit_memo_create_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        terms_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditMemo:
        """
        Creates a new credit memo.

        Args:
          customer_id: The customer or customer-job associated with this credit memo.

          transaction_date: The date of this credit memo, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The credit memo's billing address.

          class_id: The credit memo's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this credit memo's line items unless overridden at the
              line item level.

          customer_message_id: The message to display to the customer on the credit memo.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this credit memo when printed or displayed.

          due_date: The date by which this credit memo must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this credit memo's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_pending: Indicates whether this credit memo has not been completed.

          is_queued_for_email: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to print.

          line_groups: The credit memo's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              credit memo.

          lines: The credit memo's line items, each representing a single product or service
              sold.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating a
              credit memo.

          memo: A memo or note for this credit memo that appears in the account register and
              customer register, but not on the credit memo itself.

          other_custom_field: A built-in custom field for additional information specific to this credit memo.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all credit memos for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this credit memo. This
              field is often used to cross-reference the credit memo with the customer's
              purchasing system.

              Maximum length: 25 characters.

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit memo is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this credit memo is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this credit memo, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user. When left blank
              in this create request, this field will be left blank in QuickBooks (i.e., it
              does _not_ auto-increment).

          sales_representative_id: The credit memo's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this credit memo, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this credit
              memo's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this credit memo is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The credit memo's shipping address.

          shipping_date: The date when the products or services for this credit memo were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this credit memo, such as standard mail or
              overnight delivery.

          terms_id: The credit memo's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/credit-memos",
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
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                },
                credit_memo_create_params.CreditMemoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
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
    ) -> CreditMemo:
        """
        Retrieves a credit memo by ID.

        **IMPORTANT:** If you need to fetch multiple specific credit memos by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        NOTE: The response automatically includes any linked transactions.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to retrieve.

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
            f"/quickbooks-desktop/credit-memos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: credit_memo_update_params.BillingAddress | Omit = omit,
        class_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        customer_message_id: str | Omit = omit,
        document_template_id: str | Omit = omit,
        due_date: Union[str, date] | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_pending: bool | Omit = omit,
        is_queued_for_email: bool | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        line_groups: Iterable[credit_memo_update_params.LineGroup] | Omit = omit,
        lines: Iterable[credit_memo_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        other_custom_field: str | Omit = omit,
        purchase_order_number: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_representative_id: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        sales_tax_item_id: str | Omit = omit,
        shipment_origin: str | Omit = omit,
        shipping_address: credit_memo_update_params.ShippingAddress | Omit = omit,
        shipping_date: Union[str, date] | Omit = omit,
        shipping_method_id: str | Omit = omit,
        terms_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditMemo:
        """
        Updates an existing credit memo.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to update.

          revision_number: The current QuickBooks-assigned revision number of the credit memo object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          billing_address: The credit memo's billing address.

          class_id: The credit memo's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default. A class defined here is
              automatically used in this credit memo's line items unless overridden at the
              line item level.

          customer_id: The customer or customer-job associated with this credit memo.

          customer_message_id: The message to display to the customer on the credit memo.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this credit memo when printed or displayed.

          due_date: The date by which this credit memo must be paid, in ISO 8601 format
              (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this credit memo's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_pending: Indicates whether this credit memo has not been completed.

          is_queued_for_email: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to email to the customer.

          is_queued_for_print: Indicates whether this credit memo is included in the queue of documents for
              QuickBooks to print.

          line_groups: The credit memo's line item groups, each representing a predefined set of
              related items.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line item groups for the credit memo with this array. To keep any existing
                 line item groups, you must include them in this array even if they have not
                 changed. **Any line item groups not included will be removed.**

              2. To add a new line item group, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any line item groups, omit this field entirely
                 to keep them unchanged.

          lines: The credit memo's line items, each representing a single product or service
              sold.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 line items for the credit memo with this array. To keep any existing line
                 items, you must include them in this array even if they have not changed.
                 **Any line items not included will be removed.**

              2. To add a new line item, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any line items, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this credit memo that appears in the account register and
              customer register, but not on the credit memo itself.

          other_custom_field: A built-in custom field for additional information specific to this credit memo.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all credit memos for convenience. Developers
              often use this field for tracking information that doesn't fit into other
              standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
              which are line item fields, this exists at the transaction level. Hidden by
              default in the QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this credit memo. This
              field is often used to cross-reference the credit memo with the customer's
              purchasing system.

              Maximum length: 25 characters.

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit memo is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this credit memo is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this credit memo, which can
              be used to identify the transaction in QuickBooks. This value is not required to
              be unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The credit memo's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for this credit memo, determining whether it is taxable or
              non-taxable. This can be overridden at the transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this credit
              memo's transactions by applying a specific tax rate collected for a single tax
              agency. Unlike `salesTaxCode`, which only indicates general taxability, this
              field drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this credit memo is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The credit memo's shipping address.

          shipping_date: The date when the products or services for this credit memo were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this credit memo, such as standard mail or
              overnight delivery.

          terms_id: The credit memo's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this credit memo, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/credit-memos/{id}",
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
                    "is_pending": is_pending,
                    "is_queued_for_email": is_queued_for_email,
                    "is_queued_for_print": is_queued_for_print,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                credit_memo_update_params.CreditMemoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemo,
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
        include_linked_transactions: bool | Omit = omit,
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
    ) -> AsyncPaginator[CreditMemo, AsyncCursorPage[CreditMemo]]:
        """Returns a list of credit memos.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for credit memos associated with these accounts.

          currency_ids: Filter for credit memos in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for credit memos created for these customers. These are the customers who
              are owed money.

          ids: Filter for specific credit memos by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding credit memo.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for credit memos whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for credit memos whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit memos whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific credit memos by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for credit memos whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit memos whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit memos whose `date` field is on or after this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for credit memos whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for credit memos updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for credit memos updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/credit-memos",
            page=AsyncCursorPage[CreditMemo],
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
                    credit_memo_list_params.CreditMemoListParams,
                ),
            ),
            model=CreditMemo,
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
    ) -> CreditMemoDeleteResponse:
        """Permanently deletes a a credit memo.

        The deletion will fail if the credit memo
        is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit memo to delete.

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
            f"/quickbooks-desktop/credit-memos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditMemoDeleteResponse,
        )


class CreditMemosResourceWithRawResponse:
    def __init__(self, credit_memos: CreditMemosResource) -> None:
        self._credit_memos = credit_memos

        self.create = to_raw_response_wrapper(
            credit_memos.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credit_memos.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credit_memos.update,
        )
        self.list = to_raw_response_wrapper(
            credit_memos.list,
        )
        self.delete = to_raw_response_wrapper(
            credit_memos.delete,
        )


class AsyncCreditMemosResourceWithRawResponse:
    def __init__(self, credit_memos: AsyncCreditMemosResource) -> None:
        self._credit_memos = credit_memos

        self.create = async_to_raw_response_wrapper(
            credit_memos.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credit_memos.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credit_memos.update,
        )
        self.list = async_to_raw_response_wrapper(
            credit_memos.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credit_memos.delete,
        )


class CreditMemosResourceWithStreamingResponse:
    def __init__(self, credit_memos: CreditMemosResource) -> None:
        self._credit_memos = credit_memos

        self.create = to_streamed_response_wrapper(
            credit_memos.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credit_memos.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_memos.update,
        )
        self.list = to_streamed_response_wrapper(
            credit_memos.list,
        )
        self.delete = to_streamed_response_wrapper(
            credit_memos.delete,
        )


class AsyncCreditMemosResourceWithStreamingResponse:
    def __init__(self, credit_memos: AsyncCreditMemosResource) -> None:
        self._credit_memos = credit_memos

        self.create = async_to_streamed_response_wrapper(
            credit_memos.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credit_memos.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_memos.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_memos.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credit_memos.delete,
        )
