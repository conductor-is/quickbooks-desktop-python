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
from ...types.qbd import credit_card_refund_list_params, credit_card_refund_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.credit_card_refund import CreditCardRefund
from ...types.qbd.credit_card_refund_delete_response import CreditCardRefundDeleteResponse

__all__ = ["CreditCardRefundsResource", "AsyncCreditCardRefundsResource"]


class CreditCardRefundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return CreditCardRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return CreditCardRefundsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        refund_applied_to_transactions: Iterable[credit_card_refund_create_params.RefundAppliedToTransaction],
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        address: credit_card_refund_create_params.Address | Omit = omit,
        credit_card_transaction: credit_card_refund_create_params.CreditCardTransaction | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        refund_from_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditCardRefund:
        """
        Creates a credit card refund linked to one or more existing credit transactions,
        such as credit memos or overpayments. You must supply at least one entry in
        `refundAppliedToTransactions`, and the refund amount cannot exceed the available
        balance on the linked credits.

        Args:
          customer_id: The customer or customer-job associated with this credit card refund.

          refund_applied_to_transactions: The credit transactions to refund in this credit card refund. Each entry links
              this credit card refund to an existing credit (for example, a credit memo or
              unused receive-payment credit).

              **IMPORTANT**: The `refundAmount` for each linked credit cannot exceed that
              credit's remaining balance, and the combined `refundAmount` across all links
              cannot exceed this credit card refund's `totalAmount`.

          transaction_date: The date of this credit card refund, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the credit card refund.

          credit_card_transaction: The credit card transaction data for this credit card refund's payment when
              using QuickBooks Merchant Services (QBMS). If specifying this field, you must
              also specify the `paymentMethod` field.

          exchange_rate: The market exchange rate between this credit card refund's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          memo: A memo or note for this credit card refund.

          payment_method_id: The credit card refund's payment method (e.g., cash, check, credit card).

              **NOTE**: If this credit card refund contains credit card transaction data
              supplied from QuickBooks Merchant Services (QBMS) transaction responses, you
              must specify a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit card refund is
              assigned, used to track the amount owed. If not specified, QuickBooks Desktop
              will use its default A/R account.

              **IMPORTANT**: If this credit card refund is linked to other transactions, this
              A/R account must match the `receivablesAccount` used in all linked transactions.
              For example, when refunding a credit card payment, the A/R account must match
              the one used in each linked credit transaction being refunded.

          ref_number: The case-sensitive user-defined reference number for this credit card refund,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          refund_from_account_id: The account providing funds for this credit card refund. This is typically the
              Undeposited Funds account used to hold customer payments. If omitted, QuickBooks
              Desktop will use the default Undeposited Funds account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/credit-card-refunds",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "refund_applied_to_transactions": refund_applied_to_transactions,
                    "transaction_date": transaction_date,
                    "address": address,
                    "credit_card_transaction": credit_card_transaction,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "refund_from_account_id": refund_from_account_id,
                },
                credit_card_refund_create_params.CreditCardRefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefund,
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
    ) -> CreditCardRefund:
        """
        Retrieves a credit card refund by ID.

        **IMPORTANT:** If you need to fetch multiple specific credit card refunds by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card refund to retrieve.

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
            f"/quickbooks-desktop/credit-card-refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefund,
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
    ) -> SyncCursorPage[CreditCardRefund]:
        """Returns a list of credit card refunds.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for credit card refunds associated with these accounts.

          currency_ids: Filter for credit card refunds in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for credit card refunds refunded to these customers.

          ids: Filter for specific credit card refunds by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for credit card refunds whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for credit card refunds whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card refunds whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card refunds by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for credit card refunds whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card refunds whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card refunds whose `date` field is on or after this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for credit card refunds whose `date` field is on or before this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for credit card refunds updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for credit card refunds updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/credit-card-refunds",
            page=SyncCursorPage[CreditCardRefund],
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
                    credit_card_refund_list_params.CreditCardRefundListParams,
                ),
            ),
            model=CreditCardRefund,
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
    ) -> CreditCardRefundDeleteResponse:
        """Permanently deletes a a credit card refund.

        The deletion will fail if the credit
        card refund is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card refund to delete.

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
            f"/quickbooks-desktop/credit-card-refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefundDeleteResponse,
        )


class AsyncCreditCardRefundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditCardRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncCreditCardRefundsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        refund_applied_to_transactions: Iterable[credit_card_refund_create_params.RefundAppliedToTransaction],
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        address: credit_card_refund_create_params.Address | Omit = omit,
        credit_card_transaction: credit_card_refund_create_params.CreditCardTransaction | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        refund_from_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditCardRefund:
        """
        Creates a credit card refund linked to one or more existing credit transactions,
        such as credit memos or overpayments. You must supply at least one entry in
        `refundAppliedToTransactions`, and the refund amount cannot exceed the available
        balance on the linked credits.

        Args:
          customer_id: The customer or customer-job associated with this credit card refund.

          refund_applied_to_transactions: The credit transactions to refund in this credit card refund. Each entry links
              this credit card refund to an existing credit (for example, a credit memo or
              unused receive-payment credit).

              **IMPORTANT**: The `refundAmount` for each linked credit cannot exceed that
              credit's remaining balance, and the combined `refundAmount` across all links
              cannot exceed this credit card refund's `totalAmount`.

          transaction_date: The date of this credit card refund, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the credit card refund.

          credit_card_transaction: The credit card transaction data for this credit card refund's payment when
              using QuickBooks Merchant Services (QBMS). If specifying this field, you must
              also specify the `paymentMethod` field.

          exchange_rate: The market exchange rate between this credit card refund's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          memo: A memo or note for this credit card refund.

          payment_method_id: The credit card refund's payment method (e.g., cash, check, credit card).

              **NOTE**: If this credit card refund contains credit card transaction data
              supplied from QuickBooks Merchant Services (QBMS) transaction responses, you
              must specify a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this credit card refund is
              assigned, used to track the amount owed. If not specified, QuickBooks Desktop
              will use its default A/R account.

              **IMPORTANT**: If this credit card refund is linked to other transactions, this
              A/R account must match the `receivablesAccount` used in all linked transactions.
              For example, when refunding a credit card payment, the A/R account must match
              the one used in each linked credit transaction being refunded.

          ref_number: The case-sensitive user-defined reference number for this credit card refund,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          refund_from_account_id: The account providing funds for this credit card refund. This is typically the
              Undeposited Funds account used to hold customer payments. If omitted, QuickBooks
              Desktop will use the default Undeposited Funds account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/credit-card-refunds",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "refund_applied_to_transactions": refund_applied_to_transactions,
                    "transaction_date": transaction_date,
                    "address": address,
                    "credit_card_transaction": credit_card_transaction,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "refund_from_account_id": refund_from_account_id,
                },
                credit_card_refund_create_params.CreditCardRefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefund,
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
    ) -> CreditCardRefund:
        """
        Retrieves a credit card refund by ID.

        **IMPORTANT:** If you need to fetch multiple specific credit card refunds by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card refund to retrieve.

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
            f"/quickbooks-desktop/credit-card-refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefund,
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
    ) -> AsyncPaginator[CreditCardRefund, AsyncCursorPage[CreditCardRefund]]:
        """Returns a list of credit card refunds.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for credit card refunds associated with these accounts.

          currency_ids: Filter for credit card refunds in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for credit card refunds refunded to these customers.

          ids: Filter for specific credit card refunds by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for credit card refunds whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for credit card refunds whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card refunds whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card refunds by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for credit card refunds whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card refunds whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card refunds whose `date` field is on or after this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for credit card refunds whose `date` field is on or before this date, in
              ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for credit card refunds updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for credit card refunds updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/credit-card-refunds",
            page=AsyncCursorPage[CreditCardRefund],
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
                    credit_card_refund_list_params.CreditCardRefundListParams,
                ),
            ),
            model=CreditCardRefund,
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
    ) -> CreditCardRefundDeleteResponse:
        """Permanently deletes a a credit card refund.

        The deletion will fail if the credit
        card refund is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card refund to delete.

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
            f"/quickbooks-desktop/credit-card-refunds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardRefundDeleteResponse,
        )


class CreditCardRefundsResourceWithRawResponse:
    def __init__(self, credit_card_refunds: CreditCardRefundsResource) -> None:
        self._credit_card_refunds = credit_card_refunds

        self.create = to_raw_response_wrapper(
            credit_card_refunds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credit_card_refunds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            credit_card_refunds.list,
        )
        self.delete = to_raw_response_wrapper(
            credit_card_refunds.delete,
        )


class AsyncCreditCardRefundsResourceWithRawResponse:
    def __init__(self, credit_card_refunds: AsyncCreditCardRefundsResource) -> None:
        self._credit_card_refunds = credit_card_refunds

        self.create = async_to_raw_response_wrapper(
            credit_card_refunds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credit_card_refunds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            credit_card_refunds.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credit_card_refunds.delete,
        )


class CreditCardRefundsResourceWithStreamingResponse:
    def __init__(self, credit_card_refunds: CreditCardRefundsResource) -> None:
        self._credit_card_refunds = credit_card_refunds

        self.create = to_streamed_response_wrapper(
            credit_card_refunds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credit_card_refunds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            credit_card_refunds.list,
        )
        self.delete = to_streamed_response_wrapper(
            credit_card_refunds.delete,
        )


class AsyncCreditCardRefundsResourceWithStreamingResponse:
    def __init__(self, credit_card_refunds: AsyncCreditCardRefundsResource) -> None:
        self._credit_card_refunds = credit_card_refunds

        self.create = async_to_streamed_response_wrapper(
            credit_card_refunds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credit_card_refunds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_card_refunds.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credit_card_refunds.delete,
        )
