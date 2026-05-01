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
from ...types.qbd import deposit_list_params, deposit_create_params, deposit_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.deposit import Deposit
from ...types.qbd.deposit_void_response import DepositVoidResponse
from ...types.qbd.deposit_delete_response import DepositDeleteResponse

__all__ = ["DepositsResource", "AsyncDepositsResource"]


class DepositsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return DepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return DepositsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        deposit_to_account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        cash_back: deposit_create_params.CashBack | Omit = omit,
        currency_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        lines: Iterable[deposit_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deposit:
        """Creates a deposit into a QuickBooks Desktop bank or other asset account.

        Lines
        can either reference existing payments waiting to be deposited, using
        `paymentTransactionId` and optionally `paymentTransactionLineId`, or describe a
        manual transfer from another account using `accountId` and related line details.

        Args:
          deposit_to_account_id: The account where the funds for this deposit will be deposited.

          transaction_date: The date of this deposit, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          cash_back: Cash back taken out of this deposit and recorded to another account, such as
              Petty Cash.

          currency_id: The deposit's currency. For built-in currencies, the name and code are standard
              ISO 4217 international values. For user-defined currencies, all values are
              editable.

          exchange_rate: The market exchange rate between this deposit's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          lines: The deposit's deposit lines, each representing either an existing payment
              selected for deposit or a manual transfer from another account into the deposit
              account.

          memo: A memo or note for this deposit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/deposits",
            body=maybe_transform(
                {
                    "deposit_to_account_id": deposit_to_account_id,
                    "transaction_date": transaction_date,
                    "cash_back": cash_back,
                    "currency_id": currency_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "lines": lines,
                    "memo": memo,
                },
                deposit_create_params.DepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
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
    ) -> Deposit:
        """
        Retrieves a deposit by ID.

        **IMPORTANT:** If you need to fetch multiple specific deposits by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to retrieve.

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
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        cash_back: deposit_update_params.CashBack | Omit = omit,
        currency_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        lines: Iterable[deposit_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deposit:
        """
        Updates an existing deposit.

        **NOTE:** If you include `lines`, QuickBooks Desktop replaces that line list
        with the array you send, so include unchanged lines you want to keep and use
        `id: "-1"` for new lines.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to update.

          revision_number: The current QuickBooks-assigned revision number of the deposit object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          cash_back: Cash back taken out of this deposit and recorded to another account, such as
              Petty Cash.

          currency_id: The deposit's currency. For built-in currencies, the name and code are standard
              ISO 4217 international values. For user-defined currencies, all values are
              editable.

          deposit_to_account_id: The account where the funds for this deposit will be deposited.

          exchange_rate: The market exchange rate between this deposit's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          lines: The deposit's deposit lines, each representing either an existing payment
              selected for deposit or a manual transfer from another account into the deposit
              account.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 deposit lines for the deposit with this array. To keep any existing deposit
                 lines, you must include them in this array even if they have not changed.
                 **Any deposit lines not included will be removed.**

              2. To add a new deposit line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any deposit lines, omit this field entirely to
                 keep them unchanged.

          memo: A memo or note for this deposit.

          transaction_date: The date of this deposit, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "cash_back": cash_back,
                    "currency_id": currency_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "lines": lines,
                    "memo": memo,
                    "transaction_date": transaction_date,
                },
                deposit_update_params.DepositUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> SyncCursorPage[Deposit]:
        """Returns a list of deposits.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for deposits associated with these accounts.

          currency_ids: Filter for deposits in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for deposits associated with these entities (customers, vendors,
              employees, etc.). These are the entities referenced on the deposit's manual
              lines.

          ids: Filter for specific deposits by their QuickBooks-assigned unique identifier(s).

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

          transaction_date_from: Filter for deposits whose `date` field is on or after this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for deposits whose `date` field is on or before this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for deposits updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for deposits updated on or before this date/time. Accepts the following
              ISO 8601 formats:

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
            "/quickbooks-desktop/deposits",
            page=SyncCursorPage[Deposit],
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
                        "entity_ids": entity_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    deposit_list_params.DepositListParams,
                ),
            ),
            model=Deposit,
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
    ) -> DepositDeleteResponse:
        """Permanently deletes a a deposit.

        The deletion will fail if the deposit is
        currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to delete.

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
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositDeleteResponse,
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
    ) -> DepositVoidResponse:
        """
        Voids a deposit by setting its amount to zero while keeping a record of it in
        QuickBooks. The void will fail if the deposit is currently in use or has any
        linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to void.

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
            path_template("/quickbooks-desktop/deposits/{id}/void", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositVoidResponse,
        )


class AsyncDepositsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDepositsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDepositsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepositsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncDepositsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        deposit_to_account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        cash_back: deposit_create_params.CashBack | Omit = omit,
        currency_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        lines: Iterable[deposit_create_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deposit:
        """Creates a deposit into a QuickBooks Desktop bank or other asset account.

        Lines
        can either reference existing payments waiting to be deposited, using
        `paymentTransactionId` and optionally `paymentTransactionLineId`, or describe a
        manual transfer from another account using `accountId` and related line details.

        Args:
          deposit_to_account_id: The account where the funds for this deposit will be deposited.

          transaction_date: The date of this deposit, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          cash_back: Cash back taken out of this deposit and recorded to another account, such as
              Petty Cash.

          currency_id: The deposit's currency. For built-in currencies, the name and code are standard
              ISO 4217 international values. For user-defined currencies, all values are
              editable.

          exchange_rate: The market exchange rate between this deposit's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          lines: The deposit's deposit lines, each representing either an existing payment
              selected for deposit or a manual transfer from another account into the deposit
              account.

          memo: A memo or note for this deposit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/deposits",
            body=await async_maybe_transform(
                {
                    "deposit_to_account_id": deposit_to_account_id,
                    "transaction_date": transaction_date,
                    "cash_back": cash_back,
                    "currency_id": currency_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "lines": lines,
                    "memo": memo,
                },
                deposit_create_params.DepositCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
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
    ) -> Deposit:
        """
        Retrieves a deposit by ID.

        **IMPORTANT:** If you need to fetch multiple specific deposits by ID, use the
        list endpoint instead with the `ids` parameter. It accepts an array of IDs so
        you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to retrieve.

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
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        cash_back: deposit_update_params.CashBack | Omit = omit,
        currency_id: str | Omit = omit,
        deposit_to_account_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        lines: Iterable[deposit_update_params.Line] | Omit = omit,
        memo: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deposit:
        """
        Updates an existing deposit.

        **NOTE:** If you include `lines`, QuickBooks Desktop replaces that line list
        with the array you send, so include unchanged lines you want to keep and use
        `id: "-1"` for new lines.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to update.

          revision_number: The current QuickBooks-assigned revision number of the deposit object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          cash_back: Cash back taken out of this deposit and recorded to another account, such as
              Petty Cash.

          currency_id: The deposit's currency. For built-in currencies, the name and code are standard
              ISO 4217 international values. For user-defined currencies, all values are
              editable.

          deposit_to_account_id: The account where the funds for this deposit will be deposited.

          exchange_rate: The market exchange rate between this deposit's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          lines: The deposit's deposit lines, each representing either an existing payment
              selected for deposit or a manual transfer from another account into the deposit
              account.

              **IMPORTANT**:

              1. Including this array in your update request will **REPLACE** all existing
                 deposit lines for the deposit with this array. To keep any existing deposit
                 lines, you must include them in this array even if they have not changed.
                 **Any deposit lines not included will be removed.**

              2. To add a new deposit line, include it here with the `id` field set to `-1`.

              3. If you do not wish to modify any deposit lines, omit this field entirely to
                 keep them unchanged.

          memo: A memo or note for this deposit.

          transaction_date: The date of this deposit, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "cash_back": cash_back,
                    "currency_id": currency_id,
                    "deposit_to_account_id": deposit_to_account_id,
                    "exchange_rate": exchange_rate,
                    "lines": lines,
                    "memo": memo,
                    "transaction_date": transaction_date,
                },
                deposit_update_params.DepositUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deposit,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: SequenceNotStr[str] | Omit = omit,
        currency_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_line_items: bool | Omit = omit,
        limit: int | Omit = omit,
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
    ) -> AsyncPaginator[Deposit, AsyncCursorPage[Deposit]]:
        """Returns a list of deposits.

        Use the `cursor` parameter to paginate through the
        results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for deposits associated with these accounts.

          currency_ids: Filter for deposits in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for deposits associated with these entities (customers, vendors,
              employees, etc.). These are the entities referenced on the deposit's manual
              lines.

          ids: Filter for specific deposits by their QuickBooks-assigned unique identifier(s).

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

          transaction_date_from: Filter for deposits whose `date` field is on or after this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for deposits whose `date` field is on or before this date, in ISO 8601
              format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for deposits updated on or after this date/time. Accepts the following
              ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for deposits updated on or before this date/time. Accepts the following
              ISO 8601 formats:

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
            "/quickbooks-desktop/deposits",
            page=AsyncCursorPage[Deposit],
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
                        "entity_ids": entity_ids,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    deposit_list_params.DepositListParams,
                ),
            ),
            model=Deposit,
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
    ) -> DepositDeleteResponse:
        """Permanently deletes a a deposit.

        The deletion will fail if the deposit is
        currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to delete.

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
            path_template("/quickbooks-desktop/deposits/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositDeleteResponse,
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
    ) -> DepositVoidResponse:
        """
        Voids a deposit by setting its amount to zero while keeping a record of it in
        QuickBooks. The void will fail if the deposit is currently in use or has any
        linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the deposit to void.

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
            path_template("/quickbooks-desktop/deposits/{id}/void", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DepositVoidResponse,
        )


class DepositsResourceWithRawResponse:
    def __init__(self, deposits: DepositsResource) -> None:
        self._deposits = deposits

        self.create = to_raw_response_wrapper(
            deposits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deposits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            deposits.update,
        )
        self.list = to_raw_response_wrapper(
            deposits.list,
        )
        self.delete = to_raw_response_wrapper(
            deposits.delete,
        )
        self.void = to_raw_response_wrapper(
            deposits.void,
        )


class AsyncDepositsResourceWithRawResponse:
    def __init__(self, deposits: AsyncDepositsResource) -> None:
        self._deposits = deposits

        self.create = async_to_raw_response_wrapper(
            deposits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deposits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            deposits.update,
        )
        self.list = async_to_raw_response_wrapper(
            deposits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deposits.delete,
        )
        self.void = async_to_raw_response_wrapper(
            deposits.void,
        )


class DepositsResourceWithStreamingResponse:
    def __init__(self, deposits: DepositsResource) -> None:
        self._deposits = deposits

        self.create = to_streamed_response_wrapper(
            deposits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deposits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            deposits.update,
        )
        self.list = to_streamed_response_wrapper(
            deposits.list,
        )
        self.delete = to_streamed_response_wrapper(
            deposits.delete,
        )
        self.void = to_streamed_response_wrapper(
            deposits.void,
        )


class AsyncDepositsResourceWithStreamingResponse:
    def __init__(self, deposits: AsyncDepositsResource) -> None:
        self._deposits = deposits

        self.create = async_to_streamed_response_wrapper(
            deposits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deposits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            deposits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            deposits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deposits.delete,
        )
        self.void = async_to_streamed_response_wrapper(
            deposits.void,
        )
