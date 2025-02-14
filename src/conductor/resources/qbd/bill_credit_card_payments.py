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
from ...types.qbd import bill_credit_card_payment_list_params, bill_credit_card_payment_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.bill_credit_card_payment import BillCreditCardPayment
from ...types.qbd.bill_credit_card_payment_delete_response import BillCreditCardPaymentDeleteResponse

__all__ = ["BillCreditCardPaymentsResource", "AsyncBillCreditCardPaymentsResource"]


class BillCreditCardPaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillCreditCardPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return BillCreditCardPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillCreditCardPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return BillCreditCardPaymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        apply_to_transactions: Iterable[bill_credit_card_payment_create_params.ApplyToTransaction],
        credit_card_account_id: str,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillCreditCardPayment:
        """
        Creates a new bill credit card payment.

        Args:
          apply_to_transactions: The bills to be paid by this bill credit card payment. This will create a link
              between this bill credit card payment and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          credit_card_account_id: The credit card account to which this bill credit card payment is being charged.
              This bill credit card payment will decrease the balance of this account.

          transaction_date: The date of this bill credit card payment, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent the bill(s) that this bill credit card payment is paying and
              who will receive this payment.

              **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
              `applyToTransactions`; otherwise, QuickBooks will say the `transactionId` in
              `applyToTransactions` "does not exist".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this bill credit card payment's currency and
              the home currency in QuickBooks at the time of this transaction. Represented as
              a decimal value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home
              currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          memo: A memo or note for this bill credit card payment.

          payables_account_id: The Accounts-Payable (A/P) account to which this bill credit card payment is
              assigned, used to track the amount owed. If not specified, QuickBooks Desktop
              will use its default A/P account.

              **IMPORTANT**: If this bill credit card payment is linked to other transactions,
              this A/P account must match the `payablesAccount` used in those other
              transactions.

          ref_number: The case-sensitive user-defined reference number for this bill credit card
              payment, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user. When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/bill-credit-card-payments",
            body=maybe_transform(
                {
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_account_id": credit_card_account_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                },
                bill_credit_card_payment_create_params.BillCreditCardPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPayment,
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
    ) -> BillCreditCardPayment:
        """
        Retrieves a bill credit card payment by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill credit card payment to
              retrieve.

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
            f"/quickbooks-desktop/bill-credit-card-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPayment,
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
    ) -> SyncCursorPage[BillCreditCardPayment]:
        """Returns a list of bill credit card payments.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bill credit card payments associated with these accounts.

          currency_ids: Filter for bill credit card payments in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific bill credit card payments by their QuickBooks-assigned
              unique identifier(s).

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

          ref_number_contains: Filter for bill credit card payments whose `refNumber` contains this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for bill credit card payments whose `refNumber` ends with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for bill credit card payments whose `refNumber` is greater than or equal
              to this value. If omitted, the range will begin with the first number of the
              list. Uses a numerical comparison for values that contain only digits;
              otherwise, uses a lexicographical comparison.

          ref_numbers: Filter for specific bill credit card payments by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for bill credit card payments whose `refNumber` starts with this
              substring. NOTE: If you use this parameter, you cannot also use
              `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bill credit card payments whose `refNumber` is less than or equal to
              this value. If omitted, the range will end with the last number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          transaction_date_from: Filter for bill credit card payments created on or after this date, in ISO 8601
              format (YYYY-MM-DD).

          transaction_date_to: Filter for bill credit card payments created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for bill credit card payments updated on or after this date and time, in
              ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
              the time is assumed to be 00:00:00 of that day.

          updated_before: Filter for bill credit card payments updated on or before this date and time, in
              ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
              the time is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bill credit card payments sent to these vendors. These are the
              vendors who sent the bills paid by these credit card payments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bill-credit-card-payments",
            page=SyncCursorPage[BillCreditCardPayment],
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
                    bill_credit_card_payment_list_params.BillCreditCardPaymentListParams,
                ),
            ),
            model=BillCreditCardPayment,
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
    ) -> BillCreditCardPaymentDeleteResponse:
        """Permanently deletes a a bill credit card payment.

        The deletion will fail if the
        bill credit card payment is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill credit card payment to
              delete.

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
            f"/quickbooks-desktop/bill-credit-card-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPaymentDeleteResponse,
        )


class AsyncBillCreditCardPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillCreditCardPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillCreditCardPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillCreditCardPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncBillCreditCardPaymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        apply_to_transactions: Iterable[bill_credit_card_payment_create_params.ApplyToTransaction],
        credit_card_account_id: str,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillCreditCardPayment:
        """
        Creates a new bill credit card payment.

        Args:
          apply_to_transactions: The bills to be paid by this bill credit card payment. This will create a link
              between this bill credit card payment and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          credit_card_account_id: The credit card account to which this bill credit card payment is being charged.
              This bill credit card payment will decrease the balance of this account.

          transaction_date: The date of this bill credit card payment, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent the bill(s) that this bill credit card payment is paying and
              who will receive this payment.

              **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
              `applyToTransactions`; otherwise, QuickBooks will say the `transactionId` in
              `applyToTransactions` "does not exist".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this bill credit card payment's currency and
              the home currency in QuickBooks at the time of this transaction. Represented as
              a decimal value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home
              currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          memo: A memo or note for this bill credit card payment.

          payables_account_id: The Accounts-Payable (A/P) account to which this bill credit card payment is
              assigned, used to track the amount owed. If not specified, QuickBooks Desktop
              will use its default A/P account.

              **IMPORTANT**: If this bill credit card payment is linked to other transactions,
              this A/P account must match the `payablesAccount` used in those other
              transactions.

          ref_number: The case-sensitive user-defined reference number for this bill credit card
              payment, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user. When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/bill-credit-card-payments",
            body=await async_maybe_transform(
                {
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_account_id": credit_card_account_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                },
                bill_credit_card_payment_create_params.BillCreditCardPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPayment,
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
    ) -> BillCreditCardPayment:
        """
        Retrieves a bill credit card payment by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill credit card payment to
              retrieve.

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
            f"/quickbooks-desktop/bill-credit-card-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPayment,
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
    ) -> AsyncPaginator[BillCreditCardPayment, AsyncCursorPage[BillCreditCardPayment]]:
        """Returns a list of bill credit card payments.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bill credit card payments associated with these accounts.

          currency_ids: Filter for bill credit card payments in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific bill credit card payments by their QuickBooks-assigned
              unique identifier(s).

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

          ref_number_contains: Filter for bill credit card payments whose `refNumber` contains this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for bill credit card payments whose `refNumber` ends with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for bill credit card payments whose `refNumber` is greater than or equal
              to this value. If omitted, the range will begin with the first number of the
              list. Uses a numerical comparison for values that contain only digits;
              otherwise, uses a lexicographical comparison.

          ref_numbers: Filter for specific bill credit card payments by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ref_number_starts_with: Filter for bill credit card payments whose `refNumber` starts with this
              substring. NOTE: If you use this parameter, you cannot also use
              `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bill credit card payments whose `refNumber` is less than or equal to
              this value. If omitted, the range will end with the last number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          transaction_date_from: Filter for bill credit card payments created on or after this date, in ISO 8601
              format (YYYY-MM-DD).

          transaction_date_to: Filter for bill credit card payments created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for bill credit card payments updated on or after this date and time, in
              ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
              the time is assumed to be 00:00:00 of that day.

          updated_before: Filter for bill credit card payments updated on or before this date and time, in
              ISO 8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD),
              the time is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bill credit card payments sent to these vendors. These are the
              vendors who sent the bills paid by these credit card payments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bill-credit-card-payments",
            page=AsyncCursorPage[BillCreditCardPayment],
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
                    bill_credit_card_payment_list_params.BillCreditCardPaymentListParams,
                ),
            ),
            model=BillCreditCardPayment,
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
    ) -> BillCreditCardPaymentDeleteResponse:
        """Permanently deletes a a bill credit card payment.

        The deletion will fail if the
        bill credit card payment is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill credit card payment to
              delete.

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
            f"/quickbooks-desktop/bill-credit-card-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillCreditCardPaymentDeleteResponse,
        )


class BillCreditCardPaymentsResourceWithRawResponse:
    def __init__(self, bill_credit_card_payments: BillCreditCardPaymentsResource) -> None:
        self._bill_credit_card_payments = bill_credit_card_payments

        self.create = to_raw_response_wrapper(
            bill_credit_card_payments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bill_credit_card_payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bill_credit_card_payments.list,
        )
        self.delete = to_raw_response_wrapper(
            bill_credit_card_payments.delete,
        )


class AsyncBillCreditCardPaymentsResourceWithRawResponse:
    def __init__(self, bill_credit_card_payments: AsyncBillCreditCardPaymentsResource) -> None:
        self._bill_credit_card_payments = bill_credit_card_payments

        self.create = async_to_raw_response_wrapper(
            bill_credit_card_payments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bill_credit_card_payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bill_credit_card_payments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bill_credit_card_payments.delete,
        )


class BillCreditCardPaymentsResourceWithStreamingResponse:
    def __init__(self, bill_credit_card_payments: BillCreditCardPaymentsResource) -> None:
        self._bill_credit_card_payments = bill_credit_card_payments

        self.create = to_streamed_response_wrapper(
            bill_credit_card_payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bill_credit_card_payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bill_credit_card_payments.list,
        )
        self.delete = to_streamed_response_wrapper(
            bill_credit_card_payments.delete,
        )


class AsyncBillCreditCardPaymentsResourceWithStreamingResponse:
    def __init__(self, bill_credit_card_payments: AsyncBillCreditCardPaymentsResource) -> None:
        self._bill_credit_card_payments = bill_credit_card_payments

        self.create = async_to_streamed_response_wrapper(
            bill_credit_card_payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bill_credit_card_payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bill_credit_card_payments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bill_credit_card_payments.delete,
        )
