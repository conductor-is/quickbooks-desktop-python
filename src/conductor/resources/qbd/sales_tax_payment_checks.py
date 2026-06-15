# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import (
    sales_tax_payment_check_list_params,
    sales_tax_payment_check_create_params,
    sales_tax_payment_check_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.sales_tax_payment_check import SalesTaxPaymentCheck
from ...types.qbd.sales_tax_payment_check_void_response import SalesTaxPaymentCheckVoidResponse
from ...types.qbd.sales_tax_payment_check_delete_response import SalesTaxPaymentCheckDeleteResponse

__all__ = ["SalesTaxPaymentChecksResource", "AsyncSalesTaxPaymentChecksResource"]


class SalesTaxPaymentChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SalesTaxPaymentChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return SalesTaxPaymentChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesTaxPaymentChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return SalesTaxPaymentChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bank_account_id: str,
        lines: Iterable[sales_tax_payment_check_create_params.Line],
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        address: sales_tax_payment_check_create_params.Address | Omit = omit,
        external_id: str | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxPaymentCheck:
        """
        Creates a new sales-tax payment check.

        Args:
          bank_account_id: The bank account from which the funds are being drawn for this sales-tax payment
              check; e.g., Checking or Savings. This sales-tax payment check will decrease the
              balance of this account.

          lines: The payment lines in this sales-tax payment check, each recording an amount paid
              toward a sales-tax item.

          transaction_date: The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The sales-tax agency, represented as a QuickBooks vendor, receiving this
              sales-tax payment check. This must match the tax vendor associated with the
              sales-tax items in the payment lines.

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the sales-tax payment check.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_queued_for_print: Indicates whether this sales-tax payment check is included in the queue of
              documents for QuickBooks to print.

          memo: A memo or note for this sales-tax payment check.

          ref_number: The case-sensitive user-defined reference number for this sales-tax payment
              check, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user. When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

              **IMPORTANT**: For checks, this field is the check number.

              Maximum length: 11 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/sales-tax-payment-checks",
            body=maybe_transform(
                {
                    "bank_account_id": bank_account_id,
                    "lines": lines,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "address": address,
                    "external_id": external_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                },
                sales_tax_payment_check_create_params.SalesTaxPaymentCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
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
    ) -> SalesTaxPaymentCheck:
        """
        Retrieves a sales-tax payment check by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax payment checks
        by ID, use the list endpoint instead with the `ids` parameter. It accepts an
        array of IDs so you can batch the request into a single call, which is
        significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              retrieve.

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
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        address: sales_tax_payment_check_update_params.Address | Omit = omit,
        bank_account_id: str | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxPaymentCheck:
        """
        Updates an existing sales-tax payment check.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax payment check
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the sales-tax payment check.

          bank_account_id: The bank account from which the funds are being drawn for this sales-tax payment
              check; e.g., Checking or Savings. This sales-tax payment check will decrease the
              balance of this account.

          is_queued_for_print: Indicates whether this sales-tax payment check is included in the queue of
              documents for QuickBooks to print.

          memo: A memo or note for this sales-tax payment check.

          ref_number: The case-sensitive user-defined reference number for this sales-tax payment
              check, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user.

              **IMPORTANT**: For checks, this field is the check number.

              Maximum length: 11 characters.

          transaction_date: The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "address": address,
                    "bank_account_id": bank_account_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                sales_tax_payment_check_update_params.SalesTaxPaymentCheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> SyncCursorPage[SalesTaxPaymentCheck]:
        """Returns a list of sales-tax payment checks.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for sales-tax payment checks associated with these accounts.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax payment checks by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          item_ids: Filter for sales-tax payment checks containing these items.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales-tax payment checks whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales-tax payment checks whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales-tax payment checks whose `refNumber` is greater than or equal
              to this value. If omitted, the range will begin with the first number of the
              list. Uses a numerical comparison for values that contain only digits;
              otherwise, uses a lexicographical comparison.

          ref_numbers: Filter for specific sales-tax payment checks by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for sales-tax payment checks whose `refNumber` starts with this
              substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales-tax payment checks whose `refNumber` is less than or equal to
              this value. If omitted, the range will end with the last number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          transaction_date_from: Filter for sales-tax payment checks whose `date` field is on or after this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for sales-tax payment checks whose `date` field is on or before this
              date, in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for sales-tax payment checks updated on or after this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax payment checks updated on or before this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          vendor_ids: Filter for sales-tax payment checks paid to these vendors. These are the
              sales-tax agencies, represented as QuickBooks vendors, paid by these checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/sales-tax-payment-checks",
            page=SyncCursorPage[SalesTaxPaymentCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "item_ids": item_ids,
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
                    sales_tax_payment_check_list_params.SalesTaxPaymentCheckListParams,
                ),
            ),
            model=SalesTaxPaymentCheck,
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
    ) -> SalesTaxPaymentCheckDeleteResponse:
        """Permanently deletes a sales-tax payment check.

        The deletion will fail if the
        sales-tax payment check is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              delete.

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
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheckDeleteResponse,
        )

    def void(
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
    ) -> SalesTaxPaymentCheckVoidResponse:
        """
        Voids a sales-tax payment check by setting its amount to zero while keeping a
        record of it in QuickBooks. The void will fail if the sales-tax payment check is
        currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              void.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}/void", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheckVoidResponse,
        )


class AsyncSalesTaxPaymentChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSalesTaxPaymentChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesTaxPaymentChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesTaxPaymentChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncSalesTaxPaymentChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bank_account_id: str,
        lines: Iterable[sales_tax_payment_check_create_params.Line],
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        address: sales_tax_payment_check_create_params.Address | Omit = omit,
        external_id: str | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxPaymentCheck:
        """
        Creates a new sales-tax payment check.

        Args:
          bank_account_id: The bank account from which the funds are being drawn for this sales-tax payment
              check; e.g., Checking or Savings. This sales-tax payment check will decrease the
              balance of this account.

          lines: The payment lines in this sales-tax payment check, each recording an amount paid
              toward a sales-tax item.

          transaction_date: The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The sales-tax agency, represented as a QuickBooks vendor, receiving this
              sales-tax payment check. This must match the tax vendor associated with the
              sales-tax items in the payment lines.

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the sales-tax payment check.

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_queued_for_print: Indicates whether this sales-tax payment check is included in the queue of
              documents for QuickBooks to print.

          memo: A memo or note for this sales-tax payment check.

          ref_number: The case-sensitive user-defined reference number for this sales-tax payment
              check, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user. When left blank in this create request, this field will be left blank in
              QuickBooks (i.e., it does _not_ auto-increment).

              **IMPORTANT**: For checks, this field is the check number.

              Maximum length: 11 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/sales-tax-payment-checks",
            body=await async_maybe_transform(
                {
                    "bank_account_id": bank_account_id,
                    "lines": lines,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "address": address,
                    "external_id": external_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                },
                sales_tax_payment_check_create_params.SalesTaxPaymentCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
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
    ) -> SalesTaxPaymentCheck:
        """
        Retrieves a sales-tax payment check by ID.

        **IMPORTANT:** If you need to fetch multiple specific sales-tax payment checks
        by ID, use the list endpoint instead with the `ids` parameter. It accepts an
        array of IDs so you can batch the request into a single call, which is
        significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              retrieve.

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
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        address: sales_tax_payment_check_update_params.Address | Omit = omit,
        bank_account_id: str | Omit = omit,
        is_queued_for_print: bool | Omit = omit,
        memo: str | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SalesTaxPaymentCheck:
        """
        Updates an existing sales-tax payment check.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              update.

          revision_number: The current QuickBooks-assigned revision number of the sales-tax payment check
              object you are updating, which you can get by fetching the object first. Provide
              the most recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          address: The address that is printed on the sales-tax payment check.

          bank_account_id: The bank account from which the funds are being drawn for this sales-tax payment
              check; e.g., Checking or Savings. This sales-tax payment check will decrease the
              balance of this account.

          is_queued_for_print: Indicates whether this sales-tax payment check is included in the queue of
              documents for QuickBooks to print.

          memo: A memo or note for this sales-tax payment check.

          ref_number: The case-sensitive user-defined reference number for this sales-tax payment
              check, which can be used to identify the transaction in QuickBooks. This value
              is not required to be unique and can be arbitrarily changed by the QuickBooks
              user.

              **IMPORTANT**: For checks, this field is the check number.

              Maximum length: 11 characters.

          transaction_date: The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "address": address,
                    "bank_account_id": bank_account_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                sales_tax_payment_check_update_params.SalesTaxPaymentCheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheck,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        item_ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> AsyncPaginator[SalesTaxPaymentCheck, AsyncCursorPage[SalesTaxPaymentCheck]]:
        """Returns a list of sales-tax payment checks.

        Use the `cursor` parameter to
        paginate through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for sales-tax payment checks associated with these accounts.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          ids: Filter for specific sales-tax payment checks by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          item_ids: Filter for sales-tax payment checks containing these items.

          limit: The maximum number of objects to return. Accepts values ranging from 1 to 150,
              defaults to 150. When used with cursor-based pagination, this parameter controls
              how many results are returned per page. To paginate through results, combine
              this with the `cursor` parameter. Each response will include a `nextCursor`
              value that can be passed to subsequent requests to retrieve the next page of
              results.

          ref_number_contains: Filter for sales-tax payment checks whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for sales-tax payment checks whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for sales-tax payment checks whose `refNumber` is greater than or equal
              to this value. If omitted, the range will begin with the first number of the
              list. Uses a numerical comparison for values that contain only digits;
              otherwise, uses a lexicographical comparison.

          ref_numbers: Filter for specific sales-tax payment checks by their ref-number(s),
              case-sensitive. In QuickBooks, ref-numbers are not required to be unique and can
              be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for sales-tax payment checks whose `refNumber` starts with this
              substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for sales-tax payment checks whose `refNumber` is less than or equal to
              this value. If omitted, the range will end with the last number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          transaction_date_from: Filter for sales-tax payment checks whose `date` field is on or after this date,
              in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for sales-tax payment checks whose `date` field is on or before this
              date, in ISO 8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for sales-tax payment checks updated on or after this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for sales-tax payment checks updated on or before this date/time. Accepts
              the following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **end of the specified day** in the local timezone of the end-user's computer
                (e.g., `2025-01-01` → `2025-01-01T23:59:59`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          vendor_ids: Filter for sales-tax payment checks paid to these vendors. These are the
              sales-tax agencies, represented as QuickBooks vendors, paid by these checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/sales-tax-payment-checks",
            page=AsyncCursorPage[SalesTaxPaymentCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "item_ids": item_ids,
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
                    sales_tax_payment_check_list_params.SalesTaxPaymentCheckListParams,
                ),
            ),
            model=SalesTaxPaymentCheck,
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
    ) -> SalesTaxPaymentCheckDeleteResponse:
        """Permanently deletes a sales-tax payment check.

        The deletion will fail if the
        sales-tax payment check is currently in use or has any linked transactions that
        are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              delete.

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
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheckDeleteResponse,
        )

    async def void(
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
    ) -> SalesTaxPaymentCheckVoidResponse:
        """
        Voids a sales-tax payment check by setting its amount to zero while keeping a
        record of it in QuickBooks. The void will fail if the sales-tax payment check is
        currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the sales-tax payment check to
              void.

          conductor_end_user_id: The ID of the End-User to receive this request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            path_template("/quickbooks-desktop/sales-tax-payment-checks/{id}/void", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SalesTaxPaymentCheckVoidResponse,
        )


class SalesTaxPaymentChecksResourceWithRawResponse:
    def __init__(self, sales_tax_payment_checks: SalesTaxPaymentChecksResource) -> None:
        self._sales_tax_payment_checks = sales_tax_payment_checks

        self.create = to_raw_response_wrapper(
            sales_tax_payment_checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sales_tax_payment_checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sales_tax_payment_checks.update,
        )
        self.list = to_raw_response_wrapper(
            sales_tax_payment_checks.list,
        )
        self.delete = to_raw_response_wrapper(
            sales_tax_payment_checks.delete,
        )
        self.void = to_raw_response_wrapper(
            sales_tax_payment_checks.void,
        )


class AsyncSalesTaxPaymentChecksResourceWithRawResponse:
    def __init__(self, sales_tax_payment_checks: AsyncSalesTaxPaymentChecksResource) -> None:
        self._sales_tax_payment_checks = sales_tax_payment_checks

        self.create = async_to_raw_response_wrapper(
            sales_tax_payment_checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sales_tax_payment_checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sales_tax_payment_checks.update,
        )
        self.list = async_to_raw_response_wrapper(
            sales_tax_payment_checks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sales_tax_payment_checks.delete,
        )
        self.void = async_to_raw_response_wrapper(
            sales_tax_payment_checks.void,
        )


class SalesTaxPaymentChecksResourceWithStreamingResponse:
    def __init__(self, sales_tax_payment_checks: SalesTaxPaymentChecksResource) -> None:
        self._sales_tax_payment_checks = sales_tax_payment_checks

        self.create = to_streamed_response_wrapper(
            sales_tax_payment_checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sales_tax_payment_checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sales_tax_payment_checks.update,
        )
        self.list = to_streamed_response_wrapper(
            sales_tax_payment_checks.list,
        )
        self.delete = to_streamed_response_wrapper(
            sales_tax_payment_checks.delete,
        )
        self.void = to_streamed_response_wrapper(
            sales_tax_payment_checks.void,
        )


class AsyncSalesTaxPaymentChecksResourceWithStreamingResponse:
    def __init__(self, sales_tax_payment_checks: AsyncSalesTaxPaymentChecksResource) -> None:
        self._sales_tax_payment_checks = sales_tax_payment_checks

        self.create = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.delete,
        )
        self.void = async_to_streamed_response_wrapper(
            sales_tax_payment_checks.void,
        )
