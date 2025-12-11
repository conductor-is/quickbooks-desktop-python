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
from ...types.qbd import vendor_credit_list_params, vendor_credit_create_params, vendor_credit_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.vendor_credit import VendorCredit
from ...types.qbd.vendor_credit_delete_response import VendorCreditDeleteResponse

__all__ = ["VendorCreditsResource", "AsyncVendorCreditsResource"]


class VendorCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VendorCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return VendorCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VendorCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return VendorCreditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | Omit = omit,
        expense_lines: Iterable[vendor_credit_create_params.ExpenseLine] | Omit = omit,
        external_id: str | Omit = omit,
        item_group_lines: Iterable[vendor_credit_create_params.ItemGroupLine] | Omit = omit,
        item_lines: Iterable[vendor_credit_create_params.ItemLine] | Omit = omit,
        memo: str | Omit = omit,
        payables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorCredit:
        """
        Creates a vendor credit to capture returns, rebates, or other amounts a vendor
        owes so you can apply the credit when recording future bill payments.

        Args:
          transaction_date: The date of this vendor credit, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this vendor credit for goods or services purchased.

          conductor_end_user_id: The ID of the End-User to receive this request.

          exchange_rate: The market exchange rate between this vendor credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The vendor credit's expense lines, each representing one line in this expense.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          item_group_lines: The vendor credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The vendor credit's item lines, each representing the purchase of a specific
              item or service.

          memo: A memo or note for this vendor credit.

          payables_account_id: The Accounts-Payable (A/P) account to which this vendor credit is assigned, used
              to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/P account.

              **IMPORTANT**: If this vendor credit is linked to other transactions, this A/P
              account must match the `payablesAccount` used in those other transactions.

          ref_number: The case-sensitive user-defined reference number for this vendor credit, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this vendor credit, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the vendor credit's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/vendor-credits",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                vendor_credit_create_params.VendorCreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
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
    ) -> VendorCredit:
        """
        Retrieves a vendor credit by ID.

        **IMPORTANT:** If you need to fetch multiple specific vendor credits by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        NOTE: The response automatically includes any linked transactions.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to retrieve.

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
            f"/quickbooks-desktop/vendor-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        clear_expense_lines: bool | Omit = omit,
        clear_item_lines: bool | Omit = omit,
        exchange_rate: float | Omit = omit,
        expense_lines: Iterable[vendor_credit_update_params.ExpenseLine] | Omit = omit,
        item_group_lines: Iterable[vendor_credit_update_params.ItemGroupLine] | Omit = omit,
        item_lines: Iterable[vendor_credit_update_params.ItemLine] | Omit = omit,
        memo: str | Omit = omit,
        payables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorCredit:
        """
        Updates a vendor credit before you apply it to bills, letting you adjust the
        amounts, memo, or line allocations that make up the credit.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to update.

          revision_number: The current QuickBooks-assigned revision number of the vendor credit object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this vendor
              credit. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this vendor credit.
              To modify or add individual item lines, use the field `itemLines` instead.

          exchange_rate: The market exchange rate between this vendor credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The vendor credit's expense lines, each representing one line in this expense.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 expense lines for the vendor credit with this array. To keep any existing
                 expense lines, you must include them in this array even if they have not
                 changed. **Any expense lines not included will be removed.**

              2. To add a new expense line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any expense lines, omit this field entirely to
                 keep them unchanged.

          item_group_lines: The vendor credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item group lines for the vendor credit with this array. To keep any existing
                 item group lines, you must include them in this array even if they have not
                 changed. **Any item group lines not included will be removed.**

              2. To add a new item group line, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any item group lines, omit this field entirely
                 to keep them unchanged.

          item_lines: The vendor credit's item lines, each representing the purchase of a specific
              item or service.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the vendor credit with this array. To keep any existing item
                 lines, you must include them in this array even if they have not changed.
                 **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this vendor credit.

          payables_account_id: The Accounts-Payable (A/P) account to which this vendor credit is assigned, used
              to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/P account.

              **IMPORTANT**: If this vendor credit is linked to other transactions, this A/P
              account must match the `payablesAccount` used in those other transactions.

          ref_number: The case-sensitive user-defined reference number for this vendor credit, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this vendor credit, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the vendor credit's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          transaction_date: The date of this vendor credit, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this vendor credit for goods or services purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/vendor-credits/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                },
                vendor_credit_update_params.VendorCreditUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
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
        vendor_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[VendorCredit]:
        """Returns a list of vendor credits.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for vendor credits associated with these accounts.

          currency_ids: Filter for vendor credits in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific vendor credits by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding vendor credit.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for vendor credits whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for vendor credits whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for vendor credits whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific vendor credits by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for vendor credits whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for vendor credits whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for vendor credits whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for vendor credits whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for vendor credits updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for vendor credits updated on or before this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          vendor_ids: Filter for vendor credits received from these vendors. These are the vendors who
              owe the QuickBooks user money.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/vendor-credits",
            page=SyncCursorPage[VendorCredit],
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
                    vendor_credit_list_params.VendorCreditListParams,
                ),
            ),
            model=VendorCredit,
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
    ) -> VendorCreditDeleteResponse:
        """Permanently deletes a a vendor credit.

        The deletion will fail if the vendor
        credit is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to delete.

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
            f"/quickbooks-desktop/vendor-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCreditDeleteResponse,
        )


class AsyncVendorCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVendorCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVendorCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVendorCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncVendorCreditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | Omit = omit,
        expense_lines: Iterable[vendor_credit_create_params.ExpenseLine] | Omit = omit,
        external_id: str | Omit = omit,
        item_group_lines: Iterable[vendor_credit_create_params.ItemGroupLine] | Omit = omit,
        item_lines: Iterable[vendor_credit_create_params.ItemLine] | Omit = omit,
        memo: str | Omit = omit,
        payables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorCredit:
        """
        Creates a vendor credit to capture returns, rebates, or other amounts a vendor
        owes so you can apply the credit when recording future bill payments.

        Args:
          transaction_date: The date of this vendor credit, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this vendor credit for goods or services purchased.

          conductor_end_user_id: The ID of the End-User to receive this request.

          exchange_rate: The market exchange rate between this vendor credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The vendor credit's expense lines, each representing one line in this expense.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          item_group_lines: The vendor credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The vendor credit's item lines, each representing the purchase of a specific
              item or service.

          memo: A memo or note for this vendor credit.

          payables_account_id: The Accounts-Payable (A/P) account to which this vendor credit is assigned, used
              to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/P account.

              **IMPORTANT**: If this vendor credit is linked to other transactions, this A/P
              account must match the `payablesAccount` used in those other transactions.

          ref_number: The case-sensitive user-defined reference number for this vendor credit, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this vendor credit, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the vendor credit's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/vendor-credits",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                vendor_credit_create_params.VendorCreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
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
    ) -> VendorCredit:
        """
        Retrieves a vendor credit by ID.

        **IMPORTANT:** If you need to fetch multiple specific vendor credits by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        NOTE: The response automatically includes any linked transactions.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to retrieve.

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
            f"/quickbooks-desktop/vendor-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        clear_expense_lines: bool | Omit = omit,
        clear_item_lines: bool | Omit = omit,
        exchange_rate: float | Omit = omit,
        expense_lines: Iterable[vendor_credit_update_params.ExpenseLine] | Omit = omit,
        item_group_lines: Iterable[vendor_credit_update_params.ItemGroupLine] | Omit = omit,
        item_lines: Iterable[vendor_credit_update_params.ItemLine] | Omit = omit,
        memo: str | Omit = omit,
        payables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        sales_tax_code_id: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        vendor_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorCredit:
        """
        Updates a vendor credit before you apply it to bills, letting you adjust the
        amounts, memo, or line allocations that make up the credit.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to update.

          revision_number: The current QuickBooks-assigned revision number of the vendor credit object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this vendor
              credit. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this vendor credit.
              To modify or add individual item lines, use the field `itemLines` instead.

          exchange_rate: The market exchange rate between this vendor credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The vendor credit's expense lines, each representing one line in this expense.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 expense lines for the vendor credit with this array. To keep any existing
                 expense lines, you must include them in this array even if they have not
                 changed. **Any expense lines not included will be removed.**

              2. To add a new expense line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any expense lines, omit this field entirely to
                 keep them unchanged.

          item_group_lines: The vendor credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item group lines for the vendor credit with this array. To keep any existing
                 item group lines, you must include them in this array even if they have not
                 changed. **Any item group lines not included will be removed.**

              2. To add a new item group line, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any item group lines, omit this field entirely
                 to keep them unchanged.

          item_lines: The vendor credit's item lines, each representing the purchase of a specific
              item or service.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the vendor credit with this array. To keep any existing item
                 lines, you must include them in this array even if they have not changed.
                 **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this vendor credit.

          payables_account_id: The Accounts-Payable (A/P) account to which this vendor credit is assigned, used
              to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/P account.

              **IMPORTANT**: If this vendor credit is linked to other transactions, this A/P
              account must match the `payablesAccount` used in those other transactions.

          ref_number: The case-sensitive user-defined reference number for this vendor credit, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this vendor credit, determining whether it is taxable or
              non-taxable. If set, this overrides any sales-tax codes defined on the vendor.
              This can be overridden on the vendor credit's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          transaction_date: The date of this vendor credit, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this vendor credit for goods or services purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/vendor-credits/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                },
                vendor_credit_update_params.VendorCreditUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCredit,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
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
        vendor_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VendorCredit, AsyncCursorPage[VendorCredit]]:
        """Returns a list of vendor credits.

        Use the `cursor` parameter to paginate through
        the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for vendor credits associated with these accounts.

          currency_ids: Filter for vendor credits in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific vendor credits by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding vendor credit.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for vendor credits whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for vendor credits whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for vendor credits whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific vendor credits by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for vendor credits whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for vendor credits whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for vendor credits whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for vendor credits whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for vendor credits updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for vendor credits updated on or before this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          vendor_ids: Filter for vendor credits received from these vendors. These are the vendors who
              owe the QuickBooks user money.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/vendor-credits",
            page=AsyncCursorPage[VendorCredit],
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
                    vendor_credit_list_params.VendorCreditListParams,
                ),
            ),
            model=VendorCredit,
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
    ) -> VendorCreditDeleteResponse:
        """Permanently deletes a a vendor credit.

        The deletion will fail if the vendor
        credit is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the vendor credit to delete.

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
            f"/quickbooks-desktop/vendor-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorCreditDeleteResponse,
        )


class VendorCreditsResourceWithRawResponse:
    def __init__(self, vendor_credits: VendorCreditsResource) -> None:
        self._vendor_credits = vendor_credits

        self.create = to_raw_response_wrapper(
            vendor_credits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vendor_credits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vendor_credits.update,
        )
        self.list = to_raw_response_wrapper(
            vendor_credits.list,
        )
        self.delete = to_raw_response_wrapper(
            vendor_credits.delete,
        )


class AsyncVendorCreditsResourceWithRawResponse:
    def __init__(self, vendor_credits: AsyncVendorCreditsResource) -> None:
        self._vendor_credits = vendor_credits

        self.create = async_to_raw_response_wrapper(
            vendor_credits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vendor_credits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vendor_credits.update,
        )
        self.list = async_to_raw_response_wrapper(
            vendor_credits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vendor_credits.delete,
        )


class VendorCreditsResourceWithStreamingResponse:
    def __init__(self, vendor_credits: VendorCreditsResource) -> None:
        self._vendor_credits = vendor_credits

        self.create = to_streamed_response_wrapper(
            vendor_credits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vendor_credits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vendor_credits.update,
        )
        self.list = to_streamed_response_wrapper(
            vendor_credits.list,
        )
        self.delete = to_streamed_response_wrapper(
            vendor_credits.delete,
        )


class AsyncVendorCreditsResourceWithStreamingResponse:
    def __init__(self, vendor_credits: AsyncVendorCreditsResource) -> None:
        self._vendor_credits = vendor_credits

        self.create = async_to_streamed_response_wrapper(
            vendor_credits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vendor_credits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vendor_credits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vendor_credits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vendor_credits.delete,
        )
