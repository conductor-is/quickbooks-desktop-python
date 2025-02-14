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
from ...types.qbd import (
    credit_card_charge_list_params,
    credit_card_charge_create_params,
    credit_card_charge_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.credit_card_charge import CreditCardCharge
from ...types.qbd.credit_card_charge_delete_response import CreditCardChargeDeleteResponse

__all__ = ["CreditCardChargesResource", "AsyncCreditCardChargesResource"]


class CreditCardChargesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return CreditCardChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return CreditCardChargesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_line_groups: Iterable[credit_card_charge_create_params.ItemLineGroup] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCharge:
        """
        Creates a new credit card charge for the specified account.

        Args:
          account_id: The bank or credit card account to which money is owed for this credit card
              charge.

          transaction_date: The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this credit card charge's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card charge's expense lines, each representing one line in this
              expense.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          item_line_groups: The credit card charge's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The credit card charge's item lines, each representing the purchase of a
              specific item or service.

          memo: A memo or note for this credit card charge.

          payee_id: The vendor or company from whom merchandise or services were purchased for this
              credit card charge.

          ref_number: The case-sensitive user-defined reference number for this credit card charge,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this credit card charge, determining whether it is
              taxable or non-taxable. If set, this overrides any sales-tax codes defined on
              the payee. This can be overridden on the credit card charge's individual lines.

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
            "/quickbooks-desktop/credit-card-charges",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_line_groups": item_line_groups,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                credit_card_charge_create_params.CreditCardChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
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
    ) -> CreditCardCharge:
        """
        Retrieves a credit card charge by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to retrieve.

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
            f"/quickbooks-desktop/credit-card-charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_line_groups: Iterable[credit_card_charge_update_params.ItemLineGroup] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCharge:
        """
        Updates an existing credit card charge.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to update.

          revision_number: The current QuickBooks-assigned revision number of the credit card charge object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The bank or credit card account to which money is owed for this credit card
              charge.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this credit card
              charge. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this credit card
              charge. To modify or add individual item lines, use the field `itemLines`
              instead.

          exchange_rate: The market exchange rate between this credit card charge's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card charge's expense lines, each representing one line in this
              expense.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 expense lines for the credit card charge with this array. To keep any
                 existing expense lines, you must include them in this array even if they have
                 not changed. **Any expense lines not included will be removed.**

              2. To add a new expense line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any expense lines, omit this field entirely to
                 keep them unchanged.

          item_line_groups: The credit card charge's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item group lines for the credit card charge with this array. To keep any
                 existing item group lines, you must include them in this array even if they
                 have not changed. **Any item group lines not included will be removed.**

              2. To add a new item group line, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any item group lines, omit this field entirely
                 to keep them unchanged.

          item_lines: The credit card charge's item lines, each representing the purchase of a
              specific item or service.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the credit card charge with this array. To keep any existing
                 item lines, you must include them in this array even if they have not
                 changed. **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this credit card charge.

          payee_id: The vendor or company from whom merchandise or services were purchased for this
              credit card charge.

          ref_number: The case-sensitive user-defined reference number for this credit card charge,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this credit card charge, determining whether it is
              taxable or non-taxable. If set, this overrides any sales-tax codes defined on
              the payee. This can be overridden on the credit card charge's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          transaction_date: The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/credit-card-charges/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_line_groups": item_line_groups,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_charge_update_params.CreditCardChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
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
        limit: int | NotGiven = NOT_GIVEN,
        payee_ids: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> SyncCursorPage[CreditCardCharge]:
        """Returns a list of credit card charges.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for credit card charges associated with these accounts.

          currency_ids: Filter for credit card charges in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific credit card charges by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          payee_ids: Filter for credit card charges paid to these payees. These are the vendors or
              companies from whom merchandise or services were purchased for these credit card
              charges.

          ref_number_contains:
              Filter for credit card charges whose `refNumber` contains this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with:
              Filter for credit card charges whose `refNumber` ends with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card charges whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card charges by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for credit card charges whose `refNumber` starts with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card charges whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card charges created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for credit card charges created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for credit card charges updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for credit card charges updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/credit-card-charges",
            page=SyncCursorPage[CreditCardCharge],
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
                        "limit": limit,
                        "payee_ids": payee_ids,
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
                    credit_card_charge_list_params.CreditCardChargeListParams,
                ),
            ),
            model=CreditCardCharge,
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
    ) -> CreditCardChargeDeleteResponse:
        """Permanently deletes a a credit card charge.

        The deletion will fail if the credit
        card charge is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to delete.

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
            f"/quickbooks-desktop/credit-card-charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardChargeDeleteResponse,
        )


class AsyncCreditCardChargesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardChargesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditCardChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardChargesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncCreditCardChargesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_line_groups: Iterable[credit_card_charge_create_params.ItemLineGroup] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCharge:
        """
        Creates a new credit card charge for the specified account.

        Args:
          account_id: The bank or credit card account to which money is owed for this credit card
              charge.

          transaction_date: The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this credit card charge's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card charge's expense lines, each representing one line in this
              expense.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          item_line_groups: The credit card charge's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The credit card charge's item lines, each representing the purchase of a
              specific item or service.

          memo: A memo or note for this credit card charge.

          payee_id: The vendor or company from whom merchandise or services were purchased for this
              credit card charge.

          ref_number: The case-sensitive user-defined reference number for this credit card charge,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          sales_tax_code_id: The sales-tax code for this credit card charge, determining whether it is
              taxable or non-taxable. If set, this overrides any sales-tax codes defined on
              the payee. This can be overridden on the credit card charge's individual lines.

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
            "/quickbooks-desktop/credit-card-charges",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_line_groups": item_line_groups,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                credit_card_charge_create_params.CreditCardChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
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
    ) -> CreditCardCharge:
        """
        Retrieves a credit card charge by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to retrieve.

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
            f"/quickbooks-desktop/credit-card-charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_line_groups: Iterable[credit_card_charge_update_params.ItemLineGroup] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCharge:
        """
        Updates an existing credit card charge.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to update.

          revision_number: The current QuickBooks-assigned revision number of the credit card charge object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The bank or credit card account to which money is owed for this credit card
              charge.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this credit card
              charge. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this credit card
              charge. To modify or add individual item lines, use the field `itemLines`
              instead.

          exchange_rate: The market exchange rate between this credit card charge's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card charge's expense lines, each representing one line in this
              expense.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 expense lines for the credit card charge with this array. To keep any
                 existing expense lines, you must include them in this array even if they have
                 not changed. **Any expense lines not included will be removed.**

              2. To add a new expense line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any expense lines, omit this field entirely to
                 keep them unchanged.

          item_line_groups: The credit card charge's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item group lines for the credit card charge with this array. To keep any
                 existing item group lines, you must include them in this array even if they
                 have not changed. **Any item group lines not included will be removed.**

              2. To add a new item group line, include it here with the `id` field set to
                 `-1`.

              3. If you do not wish to modify any item group lines, omit this field entirely
                 to keep them unchanged.

          item_lines: The credit card charge's item lines, each representing the purchase of a
              specific item or service.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 item lines for the credit card charge with this array. To keep any existing
                 item lines, you must include them in this array even if they have not
                 changed. **Any item lines not included will be removed.**

              2. To add a new item line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any item lines, omit this field entirely to keep
                 them unchanged.

          memo: A memo or note for this credit card charge.

          payee_id: The vendor or company from whom merchandise or services were purchased for this
              credit card charge.

          ref_number: The case-sensitive user-defined reference number for this credit card charge,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code for this credit card charge, determining whether it is
              taxable or non-taxable. If set, this overrides any sales-tax codes defined on
              the payee. This can be overridden on the credit card charge's individual lines.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          transaction_date: The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/credit-card-charges/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_line_groups": item_line_groups,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_charge_update_params.CreditCardChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCharge,
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
        limit: int | NotGiven = NOT_GIVEN,
        payee_ids: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[CreditCardCharge, AsyncCursorPage[CreditCardCharge]]:
        """Returns a list of credit card charges.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for credit card charges associated with these accounts.

          currency_ids: Filter for credit card charges in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific credit card charges by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          payee_ids: Filter for credit card charges paid to these payees. These are the vendors or
              companies from whom merchandise or services were purchased for these credit card
              charges.

          ref_number_contains:
              Filter for credit card charges whose `refNumber` contains this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with:
              Filter for credit card charges whose `refNumber` ends with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card charges whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card charges by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for credit card charges whose `refNumber` starts with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card charges whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card charges created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for credit card charges created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for credit card charges updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for credit card charges updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/credit-card-charges",
            page=AsyncCursorPage[CreditCardCharge],
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
                        "limit": limit,
                        "payee_ids": payee_ids,
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
                    credit_card_charge_list_params.CreditCardChargeListParams,
                ),
            ),
            model=CreditCardCharge,
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
    ) -> CreditCardChargeDeleteResponse:
        """Permanently deletes a a credit card charge.

        The deletion will fail if the credit
        card charge is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card charge to delete.

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
            f"/quickbooks-desktop/credit-card-charges/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardChargeDeleteResponse,
        )


class CreditCardChargesResourceWithRawResponse:
    def __init__(self, credit_card_charges: CreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = to_raw_response_wrapper(
            credit_card_charges.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credit_card_charges.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credit_card_charges.update,
        )
        self.list = to_raw_response_wrapper(
            credit_card_charges.list,
        )
        self.delete = to_raw_response_wrapper(
            credit_card_charges.delete,
        )


class AsyncCreditCardChargesResourceWithRawResponse:
    def __init__(self, credit_card_charges: AsyncCreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = async_to_raw_response_wrapper(
            credit_card_charges.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credit_card_charges.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credit_card_charges.update,
        )
        self.list = async_to_raw_response_wrapper(
            credit_card_charges.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credit_card_charges.delete,
        )


class CreditCardChargesResourceWithStreamingResponse:
    def __init__(self, credit_card_charges: CreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = to_streamed_response_wrapper(
            credit_card_charges.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credit_card_charges.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_card_charges.update,
        )
        self.list = to_streamed_response_wrapper(
            credit_card_charges.list,
        )
        self.delete = to_streamed_response_wrapper(
            credit_card_charges.delete,
        )


class AsyncCreditCardChargesResourceWithStreamingResponse:
    def __init__(self, credit_card_charges: AsyncCreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = async_to_streamed_response_wrapper(
            credit_card_charges.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credit_card_charges.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_card_charges.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_card_charges.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credit_card_charges.delete,
        )
