# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable

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
from ..._base_client import make_request_options
from ...types.quickbooks_desktop import credit_card_charge_list_params, credit_card_charge_create_params
from ...types.quickbooks_desktop.qbd_credit_card_charge import QbdCreditCardCharge
from ...types.quickbooks_desktop.credit_card_charge_list_response import CreditCardChargeListResponse

__all__ = ["CreditCardChargesResource", "AsyncCreditCardChargesResource"]


class CreditCardChargesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardChargesResourceWithRawResponse:
        return CreditCardChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardChargesResourceWithStreamingResponse:
        return CreditCardChargesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_charge_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCreditCardCharge:
        """
        Creates a credit card charge for the specified account.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          ref_number: The user-defined identifier for the transaction. It is not required to be unique
              and can be arbitrarily changed by the QuickBooks user. Case sensitive.

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
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_charge_create_params.CreditCardChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCreditCardCharge,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        account_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payee_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ref_number: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: str | NotGiven = NOT_GIVEN,
        transaction_date_to: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardChargeListResponse:
        """
        Returns a list of credit card charges.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: The QuickBooks-assigned unique identifier of the transaction to return. You can
              provide one or multiple instances of this parameter to fetch specific
              transactions.

          cursor: The pagination token to use with the `cursor` request parameter to fetch the
              next set of results. This value was returned in the `nextCursor` field of the
              previous response when using the `limit` parameter.

          include_line_items: Whether to include line items in the response.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Include this parameter to paginate through the results. The `nextCursor` field
              in the response will contain the value to use with the `cursor` request
              parameter to fetch the next set of results.

          ref_number: The user-defined identifier for the transaction. It is not required to be unique
              and can be arbitrarily changed by the QuickBooks user. Case sensitive. You can
              provide one or multiple instances of this parameter to fetch specific
              transactions.

          ref_number_contains: Filter for transactions whose `refNumber` contains this substring. If you use
              this parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for transactions whose `refNumber` ends with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for transactions whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_number_starts_with: Filter for transactions whose `refNumber` starts with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for transactions whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for transactions created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for transactions created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/credit-card-charges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "account_id": account_id,
                        "cursor": cursor,
                        "include_line_items": include_line_items,
                        "limit": limit,
                        "payee_id": payee_id,
                        "ref_number": ref_number,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
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
            cast_to=CreditCardChargeListResponse,
        )


class AsyncCreditCardChargesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardChargesResourceWithRawResponse:
        return AsyncCreditCardChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardChargesResourceWithStreamingResponse:
        return AsyncCreditCardChargesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_charge_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_charge_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_charge_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCreditCardCharge:
        """
        Creates a credit card charge for the specified account.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          ref_number: The user-defined identifier for the transaction. It is not required to be unique
              and can be arbitrarily changed by the QuickBooks user. Case sensitive.

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
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_charge_create_params.CreditCardChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCreditCardCharge,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        account_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payee_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ref_number: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: str | NotGiven = NOT_GIVEN,
        transaction_date_to: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardChargeListResponse:
        """
        Returns a list of credit card charges.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: The QuickBooks-assigned unique identifier of the transaction to return. You can
              provide one or multiple instances of this parameter to fetch specific
              transactions.

          cursor: The pagination token to use with the `cursor` request parameter to fetch the
              next set of results. This value was returned in the `nextCursor` field of the
              previous response when using the `limit` parameter.

          include_line_items: Whether to include line items in the response.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Include this parameter to paginate through the results. The `nextCursor` field
              in the response will contain the value to use with the `cursor` request
              parameter to fetch the next set of results.

          ref_number: The user-defined identifier for the transaction. It is not required to be unique
              and can be arbitrarily changed by the QuickBooks user. Case sensitive. You can
              provide one or multiple instances of this parameter to fetch specific
              transactions.

          ref_number_contains: Filter for transactions whose `refNumber` contains this substring. If you use
              this parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for transactions whose `refNumber` ends with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for transactions whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_number_starts_with: Filter for transactions whose `refNumber` starts with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for transactions whose `refNumber` is less than or equal to this value.
              If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for transactions created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for transactions created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/credit-card-charges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "account_id": account_id,
                        "cursor": cursor,
                        "include_line_items": include_line_items,
                        "limit": limit,
                        "payee_id": payee_id,
                        "ref_number": ref_number,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
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
            cast_to=CreditCardChargeListResponse,
        )


class CreditCardChargesResourceWithRawResponse:
    def __init__(self, credit_card_charges: CreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = to_raw_response_wrapper(
            credit_card_charges.create,
        )
        self.list = to_raw_response_wrapper(
            credit_card_charges.list,
        )


class AsyncCreditCardChargesResourceWithRawResponse:
    def __init__(self, credit_card_charges: AsyncCreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = async_to_raw_response_wrapper(
            credit_card_charges.create,
        )
        self.list = async_to_raw_response_wrapper(
            credit_card_charges.list,
        )


class CreditCardChargesResourceWithStreamingResponse:
    def __init__(self, credit_card_charges: CreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = to_streamed_response_wrapper(
            credit_card_charges.create,
        )
        self.list = to_streamed_response_wrapper(
            credit_card_charges.list,
        )


class AsyncCreditCardChargesResourceWithStreamingResponse:
    def __init__(self, credit_card_charges: AsyncCreditCardChargesResource) -> None:
        self._credit_card_charges = credit_card_charges

        self.create = async_to_streamed_response_wrapper(
            credit_card_charges.create,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_card_charges.list,
        )
