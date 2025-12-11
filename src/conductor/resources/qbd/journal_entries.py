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
from ...types.qbd import journal_entry_list_params, journal_entry_create_params, journal_entry_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.journal_entry import JournalEntry
from ...types.qbd.journal_entry_delete_response import JournalEntryDeleteResponse

__all__ = ["JournalEntriesResource", "AsyncJournalEntriesResource"]


class JournalEntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JournalEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return JournalEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JournalEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return JournalEntriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        are_amounts_entered_in_home_currency: bool | Omit = omit,
        credit_lines: Iterable[journal_entry_create_params.CreditLine] | Omit = omit,
        currency_id: str | Omit = omit,
        debit_lines: Iterable[journal_entry_create_params.DebitLine] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_adjustment: bool | Omit = omit,
        is_home_currency_adjustment: bool | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JournalEntry:
        """Creates a journal entry with balanced debit and credit lines.

        QuickBooks Desktop
        requires total debits to equal total credits, and any line that posts to
        Accounts Receivable or Accounts Payable must include the related customer or
        vendor reference.

        Args:
          transaction_date: The date of this journal entry, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          are_amounts_entered_in_home_currency: Indicates whether the amounts in this journal entry were entered in the
              company's home currency rather than a foreign currency. When `true`, amounts are
              in the home currency regardless of the `currency` field.

          credit_lines: The journal entry's credit lines.

          currency_id: The journal entry's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          debit_lines: The journal entry's debit lines.

          exchange_rate: The market exchange rate between this journal entry's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_adjustment: Indicates whether this journal entry is an adjustment entry. When `true`,
              QuickBooks retains the original entry information to maintain an audit trail of
              the adjustments.

          is_home_currency_adjustment: Indicates whether this journal entry is an adjustment made in the company's home
              currency for a transaction that was originally recorded in a foreign currency.

          ref_number: The case-sensitive user-defined reference number for this journal entry, which
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
            "/quickbooks-desktop/journal-entries",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "are_amounts_entered_in_home_currency": are_amounts_entered_in_home_currency,
                    "credit_lines": credit_lines,
                    "currency_id": currency_id,
                    "debit_lines": debit_lines,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_adjustment": is_adjustment,
                    "is_home_currency_adjustment": is_home_currency_adjustment,
                    "ref_number": ref_number,
                },
                journal_entry_create_params.JournalEntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
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
    ) -> JournalEntry:
        """
        Retrieves a journal entry by ID.

        **IMPORTANT:** If you need to fetch multiple specific journal entries by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to retrieve.

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
            f"/quickbooks-desktop/journal-entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        are_amounts_entered_in_home_currency: bool | Omit = omit,
        currency_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_adjustment: bool | Omit = omit,
        lines: Iterable[journal_entry_update_params.Line] | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JournalEntry:
        """Updates an existing journal entry.

        Keep the debits and credits in balance, and
        include the related customer or vendor on any A/R or A/P line you submit in the
        update body.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to update.

          revision_number: The current QuickBooks-assigned revision number of the journal entry object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          are_amounts_entered_in_home_currency: Indicates whether the amounts in this journal entry were entered in the
              company's home currency rather than a foreign currency. When `true`, amounts are
              in the home currency regardless of the `currency` field.

          currency_id: The journal entry's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          exchange_rate: The market exchange rate between this journal entry's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_adjustment: Indicates whether this journal entry is an adjustment entry. When `true`,
              QuickBooks retains the original entry information to maintain an audit trail of
              the adjustments.

          lines: The journal entry's credit and debit lines.

              **IMPORTANT**: When updating journal entries, you must include ALL existing
              journal lines (both credit and debit) in your update request, even if you only
              want to modify a single line. QuickBooks will automatically delete any existing
              lines that are not included in the update request, which is why all lines must
              be provided in a single array when updating.

          ref_number: The case-sensitive user-defined reference number for this journal entry, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          transaction_date: The date of this journal entry, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/journal-entries/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "are_amounts_entered_in_home_currency": are_amounts_entered_in_home_currency,
                    "currency_id": currency_id,
                    "exchange_rate": exchange_rate,
                    "is_adjustment": is_adjustment,
                    "lines": lines,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                journal_entry_update_params.JournalEntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
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
    ) -> SyncCursorPage[JournalEntry]:
        """Returns a list of journal entries.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for journal entries associated with these accounts.

          currency_ids: Filter for journal entries in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for journal entries associated with these entities (customers, vendors,
              employees, etc.).

          ids: Filter for specific journal entries by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for journal entries whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for journal entries whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for journal entries whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific journal entries by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for journal entries whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for journal entries whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for journal entries whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for journal entries whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for journal entries updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for journal entries updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/journal-entries",
            page=SyncCursorPage[JournalEntry],
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
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            model=JournalEntry,
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
    ) -> JournalEntryDeleteResponse:
        """Permanently deletes a a journal entry.

        The deletion will fail if the journal
        entry is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to delete.

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
            f"/quickbooks-desktop/journal-entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntryDeleteResponse,
        )


class AsyncJournalEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJournalEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJournalEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJournalEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/quickbooks-desktop-python#with_streaming_response
        """
        return AsyncJournalEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        are_amounts_entered_in_home_currency: bool | Omit = omit,
        credit_lines: Iterable[journal_entry_create_params.CreditLine] | Omit = omit,
        currency_id: str | Omit = omit,
        debit_lines: Iterable[journal_entry_create_params.DebitLine] | Omit = omit,
        exchange_rate: float | Omit = omit,
        external_id: str | Omit = omit,
        is_adjustment: bool | Omit = omit,
        is_home_currency_adjustment: bool | Omit = omit,
        ref_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JournalEntry:
        """Creates a journal entry with balanced debit and credit lines.

        QuickBooks Desktop
        requires total debits to equal total credits, and any line that posts to
        Accounts Receivable or Accounts Payable must include the related customer or
        vendor reference.

        Args:
          transaction_date: The date of this journal entry, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the End-User to receive this request.

          are_amounts_entered_in_home_currency: Indicates whether the amounts in this journal entry were entered in the
              company's home currency rather than a foreign currency. When `true`, amounts are
              in the home currency regardless of the `currency` field.

          credit_lines: The journal entry's credit lines.

          currency_id: The journal entry's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          debit_lines: The journal entry's debit lines.

          exchange_rate: The market exchange rate between this journal entry's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you, the developer, can provide for tracking
              this object in your external system. This field is immutable and can only be set
              during object creation.

              **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
              QuickBooks will return an error.

          is_adjustment: Indicates whether this journal entry is an adjustment entry. When `true`,
              QuickBooks retains the original entry information to maintain an audit trail of
              the adjustments.

          is_home_currency_adjustment: Indicates whether this journal entry is an adjustment made in the company's home
              currency for a transaction that was originally recorded in a foreign currency.

          ref_number: The case-sensitive user-defined reference number for this journal entry, which
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
            "/quickbooks-desktop/journal-entries",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "are_amounts_entered_in_home_currency": are_amounts_entered_in_home_currency,
                    "credit_lines": credit_lines,
                    "currency_id": currency_id,
                    "debit_lines": debit_lines,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_adjustment": is_adjustment,
                    "is_home_currency_adjustment": is_home_currency_adjustment,
                    "ref_number": ref_number,
                },
                journal_entry_create_params.JournalEntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
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
    ) -> JournalEntry:
        """
        Retrieves a journal entry by ID.

        **IMPORTANT:** If you need to fetch multiple specific journal entries by ID, use
        the list endpoint instead with the `ids` parameter. It accepts an array of IDs
        so you can batch the request into a single call, which is significantly faster.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to retrieve.

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
            f"/quickbooks-desktop/journal-entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        are_amounts_entered_in_home_currency: bool | Omit = omit,
        currency_id: str | Omit = omit,
        exchange_rate: float | Omit = omit,
        is_adjustment: bool | Omit = omit,
        lines: Iterable[journal_entry_update_params.Line] | Omit = omit,
        ref_number: str | Omit = omit,
        transaction_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JournalEntry:
        """Updates an existing journal entry.

        Keep the debits and credits in balance, and
        include the related customer or vendor on any A/R or A/P line you submit in the
        update body.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to update.

          revision_number: The current QuickBooks-assigned revision number of the journal entry object you
              are updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the End-User to receive this request.

          are_amounts_entered_in_home_currency: Indicates whether the amounts in this journal entry were entered in the
              company's home currency rather than a foreign currency. When `true`, amounts are
              in the home currency regardless of the `currency` field.

          currency_id: The journal entry's currency. For built-in currencies, the name and code are
              standard international values. For user-defined currencies, all values are
              editable.

          exchange_rate: The market exchange rate between this journal entry's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_adjustment: Indicates whether this journal entry is an adjustment entry. When `true`,
              QuickBooks retains the original entry information to maintain an audit trail of
              the adjustments.

          lines: The journal entry's credit and debit lines.

              **IMPORTANT**: When updating journal entries, you must include ALL existing
              journal lines (both credit and debit) in your update request, even if you only
              want to modify a single line. QuickBooks will automatically delete any existing
              lines that are not included in the update request, which is why all lines must
              be provided in a single array when updating.

          ref_number: The case-sensitive user-defined reference number for this journal entry, which
              can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          transaction_date: The date of this journal entry, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/journal-entries/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "are_amounts_entered_in_home_currency": are_amounts_entered_in_home_currency,
                    "currency_id": currency_id,
                    "exchange_rate": exchange_rate,
                    "is_adjustment": is_adjustment,
                    "lines": lines,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                journal_entry_update_params.JournalEntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntry,
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
    ) -> AsyncPaginator[JournalEntry, AsyncCursorPage[JournalEntry]]:
        """Returns a list of journal entries.

        Use the `cursor` parameter to paginate
        through the results.

        Args:
          conductor_end_user_id: The ID of the End-User to receive this request.

          account_ids: Filter for journal entries associated with these accounts.

          currency_ids: Filter for journal entries in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Do not include this parameter on the first call. Use the
              `nextCursor` value returned in the previous response to request subsequent
              results.

          entity_ids: Filter for journal entries associated with these entities (customers, vendors,
              employees, etc.).

          ids: Filter for specific journal entries by their QuickBooks-assigned unique
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

          ref_number_contains: Filter for journal entries whose `refNumber` contains this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberStartsWith`
              or `refNumberEndsWith`.

          ref_number_ends_with: Filter for journal entries whose `refNumber` ends with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for journal entries whose `refNumber` is greater than or equal to this
              value. If omitted, the range will begin with the first number of the list. Uses
              a numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific journal entries by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will return an error.

          ref_number_starts_with: Filter for journal entries whose `refNumber` starts with this substring.

              **NOTE**: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for journal entries whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for journal entries whose `date` field is on or after this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **start of the
              specified day** in the local timezone of the end-user's computer (e.g.,
              `2025-01-01` → `2025-01-01T00:00:00`).

          transaction_date_to: Filter for journal entries whose `date` field is on or before this date, in ISO
              8601 format (YYYY-MM-DD).

              **NOTE:** QuickBooks Desktop interprets this date as the **end of the specified
              day** in the local timezone of the end-user's computer (e.g., `2025-01-01` →
              `2025-01-01T23:59:59`).

          updated_after: Filter for journal entries updated on or after this date/time. Accepts the
              following ISO 8601 formats:

              - **date-only** (YYYY-MM-DD) - QuickBooks Desktop interprets the date as the
                **start of the specified day** in the local timezone of the end-user's
                computer (e.g., `2025-01-01` → `2025-01-01T00:00:00`).
              - **datetime without timezone** (YYYY-MM-DDTHH:mm:ss) - QuickBooks Desktop
                interprets the timestamp in the local timezone of the end-user's computer.
              - **datetime with timezone** (YYYY-MM-DDTHH:mm:ss±HH:mm) - QuickBooks Desktop
                interprets the timestamp using the specified timezone.

          updated_before: Filter for journal entries updated on or before this date/time. Accepts the
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
            "/quickbooks-desktop/journal-entries",
            page=AsyncCursorPage[JournalEntry],
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
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            model=JournalEntry,
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
    ) -> JournalEntryDeleteResponse:
        """Permanently deletes a a journal entry.

        The deletion will fail if the journal
        entry is currently in use or has any linked transactions that are in use.

        Args:
          id: The QuickBooks-assigned unique identifier of the journal entry to delete.

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
            f"/quickbooks-desktop/journal-entries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntryDeleteResponse,
        )


class JournalEntriesResourceWithRawResponse:
    def __init__(self, journal_entries: JournalEntriesResource) -> None:
        self._journal_entries = journal_entries

        self.create = to_raw_response_wrapper(
            journal_entries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            journal_entries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            journal_entries.update,
        )
        self.list = to_raw_response_wrapper(
            journal_entries.list,
        )
        self.delete = to_raw_response_wrapper(
            journal_entries.delete,
        )


class AsyncJournalEntriesResourceWithRawResponse:
    def __init__(self, journal_entries: AsyncJournalEntriesResource) -> None:
        self._journal_entries = journal_entries

        self.create = async_to_raw_response_wrapper(
            journal_entries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            journal_entries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            journal_entries.update,
        )
        self.list = async_to_raw_response_wrapper(
            journal_entries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            journal_entries.delete,
        )


class JournalEntriesResourceWithStreamingResponse:
    def __init__(self, journal_entries: JournalEntriesResource) -> None:
        self._journal_entries = journal_entries

        self.create = to_streamed_response_wrapper(
            journal_entries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            journal_entries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            journal_entries.update,
        )
        self.list = to_streamed_response_wrapper(
            journal_entries.list,
        )
        self.delete = to_streamed_response_wrapper(
            journal_entries.delete,
        )


class AsyncJournalEntriesResourceWithStreamingResponse:
    def __init__(self, journal_entries: AsyncJournalEntriesResource) -> None:
        self._journal_entries = journal_entries

        self.create = async_to_streamed_response_wrapper(
            journal_entries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            journal_entries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            journal_entries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            journal_entries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            journal_entries.delete,
        )
