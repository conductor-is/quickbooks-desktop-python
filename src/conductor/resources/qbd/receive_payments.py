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
from ...types.qbd import receive_payment_list_params, receive_payment_create_params, receive_payment_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.receive_payment import ReceivePayment
from ...types.qbd.receive_payment_delete_response import ReceivePaymentDeleteResponse

__all__ = ["ReceivePaymentsResource", "AsyncReceivePaymentsResource"]


class ReceivePaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReceivePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return ReceivePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReceivePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return ReceivePaymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        total_amount: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        apply_to_transactions: Iterable[receive_payment_create_params.ApplyToTransaction] | Omit = omit,
        credit_card_transaction: receive_payment_create_params.CreditCardTransaction | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_auto_apply: bool | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReceivePayment:
        """
        Records a customer payment and optionally applies it to specific invoices or
        credits. All allocations must target the same accounts receivable account as
        those invoices, and each one has to include a payment amount, discount, or
        credit so QuickBooks can close out the balance.

        Args:
          customer_id: The customer or customer-job to which the payment for this receive-payment is
              credited.

          total_amount: The total monetary amount of this receive-payment, represented as a decimal
              string.

              **NOTE**: The sum of the `paymentAmount` amounts in the `applyToTransactions`
              array cannot exceed the `totalAmount`, or you will receive an error.

          transaction_date: The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          apply_to_transactions: The invoices to be paid by this receive-payment. This will create a link between
              this receive-payment and the specified invoices.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target invoice must have `isPaid=false`, otherwise,
              QuickBooks will report this object as "cannot be found".

              **NOTE**: You must specify either `isAutoApply` or `applyToTransactions` when
              creating a receive-payment, but never both.

          credit_card_transaction: The credit card transaction data for this receive-payment's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          deposit_to_account_id: The account where the funds for this receive-payment will be or have been
              deposited. If omitted, QuickBooks will use the default Undeposited Funds
              account.

          exchange_rate: The market exchange rate between this receive-payment's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_auto_apply: When `true`, QuickBooks applies `totalAmount` to any outstanding transaction
              that exactly matches `totalAmount`. If no exact match is found, this
              receive-payment is applied to the oldest outstanding transaction for the
              customer-job. When `false`, QuickBooks records the payment but does not apply it
              to any specific transaction, causing the amount to appear as a credit on the
              customer-job's next transaction.

              **IMPORTANT**: You must specify either `isAutoApply` or `applyToTransactions`
              when creating a receive-payment, but never both.

          memo: A memo or note for this receive-payment that will be displayed at the beginning
              of reports containing details about this receive-payment.

          payment_method_id: The receive-payment's payment method (e.g., cash, check, credit card).

              **NOTE**: If this receive-payment contains credit card transaction data supplied
              from QuickBooks Merchant Services (QBMS) transaction responses, you must specify
              a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this receive-payment, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/receive-payments",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "total_amount": total_amount,
                    "transaction_date": transaction_date,
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_transaction": credit_card_transaction,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_auto_apply": is_auto_apply,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                },
                receive_payment_create_params.ReceivePaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
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
    ) -> ReceivePayment:
        """
        Retrieves a receive-payment by ID.

        **IMPORTANT:** If you need to fetch multiple specific receive-payments by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to retrieve.

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
            f"/quickbooks-desktop/receive-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        apply_to_transactions: Iterable[receive_payment_update_params.ApplyToTransaction] | Omit = omit,
        credit_card_transaction: receive_payment_update_params.CreditCardTransaction | Omit = omit,
        customer_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        total_amount: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReceivePayment:
        """Updates a received payment.

        When you resubmit applications to invoices, keep
        them on the same accounts receivable account and include the payment amount,
        discount, or credit on every allocation you send.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to update.

          revision_number: The current QuickBooks-assigned revision number of the receive-payment object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          apply_to_transactions: The invoices to be paid by this receive-payment. This will create a link between
              this receive-payment and the specified invoices.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target invoice must have `isPaid=false`, otherwise,
              QuickBooks will report this object as "cannot be found".

          credit_card_transaction: The credit card transaction data for this receive-payment's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          customer_id: The customer or customer-job to which the payment for this receive-payment is
              credited.

          deposit_to_account_id: The account where the funds for this receive-payment will be or have been
              deposited.

          exchange_rate: The market exchange rate between this receive-payment's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          memo: A memo or note for this receive-payment that will be displayed at the beginning
              of reports containing details about this receive-payment.

          payment_method_id: The receive-payment's payment method (e.g., cash, check, credit card).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this receive-payment, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          total_amount: The total monetary amount of this receive-payment, represented as a decimal
              string.

              **NOTE**: The sum of the `paymentAmount` amounts in the `applyToTransactions`
              array cannot exceed the `totalAmount`, or you will receive an error.

          transaction_date: The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/receive-payments/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_transaction": credit_card_transaction,
                    "customer_id": customer_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "total_amount": total_amount,
                    "transaction_date": transaction_date,
                },
                receive_payment_update_params.ReceivePaymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
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
    ) -> SyncCursorPage[ReceivePayment]:
        """Returns a list of receive-payments.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for receive-payments associated with these accounts.

          currency_ids: Filter for receive-payments in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for receive-payments received from these customers.

          ids: Filter for specific receive-payments by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for receive-payments whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for receive-payments whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for receive-payments whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific receive-payments by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for receive-payments whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for receive-payments whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for receive-payments whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for receive-payments whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for receive-payments updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for receive-payments updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/receive-payments",
            page=SyncCursorPage[ReceivePayment],
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
                    receive_payment_list_params.ReceivePaymentListParams,
                ),
            ),
            model=ReceivePayment,
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
    ) -> ReceivePaymentDeleteResponse:
        """Permanently deletes a a receive-payment.

        The deletion will fail if the
        receive-payment is currently in use or has any linked transactions that are in
        use.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to delete.

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
            f"/quickbooks-desktop/receive-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePaymentDeleteResponse,
        )


class AsyncReceivePaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReceivePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReceivePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReceivePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncReceivePaymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        total_amount: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        apply_to_transactions: Iterable[receive_payment_create_params.ApplyToTransaction] | Omit = omit,
        credit_card_transaction: receive_payment_create_params.CreditCardTransaction | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_auto_apply: bool | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReceivePayment:
        """
        Records a customer payment and optionally applies it to specific invoices or
        credits. All allocations must target the same accounts receivable account as
        those invoices, and each one has to include a payment amount, discount, or
        credit so QuickBooks can close out the balance.

        Args:
          customer_id: The customer or customer-job to which the payment for this receive-payment is
              credited.

          total_amount: The total monetary amount of this receive-payment, represented as a decimal
              string.

              **NOTE**: The sum of the `paymentAmount` amounts in the `applyToTransactions`
              array cannot exceed the `totalAmount`, or you will receive an error.

          transaction_date: The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          apply_to_transactions: The invoices to be paid by this receive-payment. This will create a link between
              this receive-payment and the specified invoices.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target invoice must have `isPaid=false`, otherwise,
              QuickBooks will report this object as "cannot be found".

              **NOTE**: You must specify either `isAutoApply` or `applyToTransactions` when
              creating a receive-payment, but never both.

          credit_card_transaction: The credit card transaction data for this receive-payment's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          deposit_to_account_id: The account where the funds for this receive-payment will be or have been
              deposited. If omitted, QuickBooks will use the default Undeposited Funds
              account.

          exchange_rate: The market exchange rate between this receive-payment's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_auto_apply: When `true`, QuickBooks applies `totalAmount` to any outstanding transaction
              that exactly matches `totalAmount`. If no exact match is found, this
              receive-payment is applied to the oldest outstanding transaction for the
              customer-job. When `false`, QuickBooks records the payment but does not apply it
              to any specific transaction, causing the amount to appear as a credit on the
              customer-job's next transaction.

              **IMPORTANT**: You must specify either `isAutoApply` or `applyToTransactions`
              when creating a receive-payment, but never both.

          memo: A memo or note for this receive-payment that will be displayed at the beginning
              of reports containing details about this receive-payment.

          payment_method_id: The receive-payment's payment method (e.g., cash, check, credit card).

              **NOTE**: If this receive-payment contains credit card transaction data supplied
              from QuickBooks Merchant Services (QBMS) transaction responses, you must specify
              a credit card payment method (e.g., "Visa", "MasterCard", etc.).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this receive-payment, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.
              When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/receive-payments",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "total_amount": total_amount,
                    "transaction_date": transaction_date,
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_transaction": credit_card_transaction,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_auto_apply": is_auto_apply,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                },
                receive_payment_create_params.ReceivePaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
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
    ) -> ReceivePayment:
        """
        Retrieves a receive-payment by ID.

        **IMPORTANT:** If you need to fetch multiple specific receive-payments by ID,
        use the list endpoint instead with the `ids` parameter. It accepts an array of
        IDs so you can batch the request into a single call, which is significantly
        faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to retrieve.

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
            f"/quickbooks-desktop/receive-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        apply_to_transactions: Iterable[receive_payment_update_params.ApplyToTransaction] | Omit = omit,
        credit_card_transaction: receive_payment_update_params.CreditCardTransaction | Omit = omit,
        customer_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        memo: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        receivables_account_id: str | Omit = omit,
        ref_number: str | Omit = omit,
        total_amount: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReceivePayment:
        """Updates a received payment.

        When you resubmit applications to invoices, keep
        them on the same accounts receivable account and include the payment amount,
        discount, or credit on every allocation you send.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to update.

          revision_number: The current QuickBooks-assigned revision number of the receive-payment object
              you are updating, which you can get by fetching the object first. Provide the
              most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          apply_to_transactions: The invoices to be paid by this receive-payment. This will create a link between
              this receive-payment and the specified invoices.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target invoice must have `isPaid=false`, otherwise,
              QuickBooks will report this object as "cannot be found".

          credit_card_transaction: The credit card transaction data for this receive-payment's payment when using
              QuickBooks Merchant Services (QBMS). If specifying this field, you must also
              specify the `paymentMethod` field.

          customer_id: The customer or customer-job to which the payment for this receive-payment is
              credited.

          deposit_to_account_id: The account where the funds for this receive-payment will be or have been
              deposited.

          exchange_rate: The market exchange rate between this receive-payment's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          memo: A memo or note for this receive-payment that will be displayed at the beginning
              of reports containing details about this receive-payment.

          payment_method_id: The receive-payment's payment method (e.g., cash, check, credit card).

          receivables_account_id: The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default A/R account.

              **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
              account must match the `receivablesAccount` used in all linked transactions.

          ref_number: The case-sensitive user-defined reference number for this receive-payment, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          total_amount: The total monetary amount of this receive-payment, represented as a decimal
              string.

              **NOTE**: The sum of the `paymentAmount` amounts in the `applyToTransactions`
              array cannot exceed the `totalAmount`, or you will receive an error.

          transaction_date: The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/receive-payments/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "apply_to_transactions": apply_to_transactions,
                    "credit_card_transaction": credit_card_transaction,
                    "customer_id": customer_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "memo": memo,
                    "payment_method_id": payment_method_id,
                    "receivables_account_id": receivables_account_id,
                    "ref_number": ref_number,
                    "total_amount": total_amount,
                    "transaction_date": transaction_date,
                },
                receive_payment_update_params.ReceivePaymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePayment,
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
    ) -> AsyncPaginator[ReceivePayment, AsyncCursorPage[ReceivePayment]]:
        """Returns a list of receive-payments.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for receive-payments associated with these accounts.

          currency_ids: Filter for receive-payments in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          customer_ids: Filter for receive-payments received from these customers.

          ids: Filter for specific receive-payments by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for receive-payments whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for receive-payments whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for receive-payments whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific receive-payments by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for receive-payments whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for receive-payments whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for receive-payments whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for receive-payments whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for receive-payments updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for receive-payments updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/receive-payments",
            page=AsyncCursorPage[ReceivePayment],
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
                    receive_payment_list_params.ReceivePaymentListParams,
                ),
            ),
            model=ReceivePayment,
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
    ) -> ReceivePaymentDeleteResponse:
        """Permanently deletes a a receive-payment.

        The deletion will fail if the
        receive-payment is currently in use or has any linked transactions that are in
        use.

        Args:
          id: The QuickBooks-assigned unique identifier of the receive-payment to delete.

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
            f"/quickbooks-desktop/receive-payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReceivePaymentDeleteResponse,
        )


class ReceivePaymentsResourceWithRawResponse:
    def __init__(self, receive_payments: ReceivePaymentsResource) -> None:
        self._receive_payments = receive_payments

        self.create = to_raw_response_wrapper(
            receive_payments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            receive_payments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            receive_payments.update,
        )
        self.list = to_raw_response_wrapper(
            receive_payments.list,
        )
        self.delete = to_raw_response_wrapper(
            receive_payments.delete,
        )


class AsyncReceivePaymentsResourceWithRawResponse:
    def __init__(self, receive_payments: AsyncReceivePaymentsResource) -> None:
        self._receive_payments = receive_payments

        self.create = async_to_raw_response_wrapper(
            receive_payments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            receive_payments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            receive_payments.update,
        )
        self.list = async_to_raw_response_wrapper(
            receive_payments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            receive_payments.delete,
        )


class ReceivePaymentsResourceWithStreamingResponse:
    def __init__(self, receive_payments: ReceivePaymentsResource) -> None:
        self._receive_payments = receive_payments

        self.create = to_streamed_response_wrapper(
            receive_payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            receive_payments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            receive_payments.update,
        )
        self.list = to_streamed_response_wrapper(
            receive_payments.list,
        )
        self.delete = to_streamed_response_wrapper(
            receive_payments.delete,
        )


class AsyncReceivePaymentsResourceWithStreamingResponse:
    def __init__(self, receive_payments: AsyncReceivePaymentsResource) -> None:
        self._receive_payments = receive_payments

        self.create = async_to_streamed_response_wrapper(
            receive_payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            receive_payments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            receive_payments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            receive_payments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            receive_payments.delete,
        )
