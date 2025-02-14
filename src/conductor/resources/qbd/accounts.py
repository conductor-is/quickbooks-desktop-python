# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal

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
from ...types.qbd import account_list_params, account_create_params, account_update_params
from ..._base_client import make_request_options
from ...types.qbd.account import Account
from ...types.qbd.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ],
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Creates a new financial account.

        Args:
          account_type: The classification of this account, indicating its purpose within the chart of
              accounts.

              **NOTE**: You cannot create an account of type `non_posting` through the API
              because QuickBooks creates these accounts behind the scenes.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two accounts could both have the `name` "Accounts-Payable",
              but they could have unique `fullName` values, such as
              "Corporate:Accounts-Payable" and "Finance:Accounts-Payable".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance of this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, this field will
              be `null`.

          sales_tax_code_id: The default sales-tax code for transactions with this account, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          tax_line_id: The identifier of the tax line associated with this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/accounts",
            body=maybe_transform(
                {
                    "account_type": account_type,
                    "name": name,
                    "account_number": account_number,
                    "bank_account_number": bank_account_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
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
    ) -> Account:
        """
        Retrieves an account by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to retrieve.

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
            f"/quickbooks-desktop/accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Updates an existing financial account.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to update.

          revision_number: The current QuickBooks-assigned revision number of the account object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          account_type: The classification of this account, indicating its purpose within the chart of
              accounts.

              **NOTE**: You cannot create an account of type `non_posting` through the API
              because QuickBooks creates these accounts behind the scenes.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two accounts could both have the `name` "Accounts-Payable",
              but they could have unique `fullName` values, such as
              "Corporate:Accounts-Payable" and "Finance:Accounts-Payable".

              Maximum length: 31 characters.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance of this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, this field will
              be `null`.

          sales_tax_code_id: The default sales-tax code for transactions with this account, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          tax_line_id: The identifier of the tax line associated with this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/accounts/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "account_type": account_type,
                    "bank_account_number": bank_account_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Returns a list of accounts.

        NOTE: QuickBooks Desktop does not support pagination
        for accounts; hence, there is no `cursor` parameter. Users typically have few
        accounts.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_type: Filter for accounts of this type.

          currency_ids: Filter for accounts in these currencies.

          full_names: Filter for specific accounts by their full-name(s), case-insensitive. Like `id`,
              `fullName` is a unique identifier for an account, formed by by combining the
              names of its parent objects with its own `name`, separated by colons. For
              example, if an account is under "Corporate" and has the `name`
              "Accounts-Payable", its `fullName` would be "Corporate:Accounts-Payable".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific accounts by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              accounts. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all accounts without limit,
              unlike paginated endpoints which default to 150 records. This is acceptable
              because accounts typically have low record counts.

          name_contains: Filter for accounts whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for accounts whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for accounts whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for accounts whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for accounts whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for accounts that are active, inactive, or both.

          updated_after: Filter for accounts updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for accounts updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_type": account_type,
                        "currency_ids": currency_ids,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ],
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Creates a new financial account.

        Args:
          account_type: The classification of this account, indicating its purpose within the chart of
              accounts.

              **NOTE**: You cannot create an account of type `non_posting` through the API
              because QuickBooks creates these accounts behind the scenes.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two accounts could both have the `name` "Accounts-Payable",
              but they could have unique `fullName` values, such as
              "Corporate:Accounts-Payable" and "Finance:Accounts-Payable".

              Maximum length: 31 characters.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance of this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, this field will
              be `null`.

          sales_tax_code_id: The default sales-tax code for transactions with this account, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          tax_line_id: The identifier of the tax line associated with this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/accounts",
            body=await async_maybe_transform(
                {
                    "account_type": account_type,
                    "name": name,
                    "account_number": account_number,
                    "bank_account_number": bank_account_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
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
    ) -> Account:
        """
        Retrieves an account by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to retrieve.

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
            f"/quickbooks-desktop/accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Updates an existing financial account.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to update.

          revision_number: The current QuickBooks-assigned revision number of the account object you are
              updating, which you can get by fetching the object first. Provide the most
              recent `revisionNumber` to ensure you're working with the latest data;
              otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs.

              Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
              the account number may not be visible in the user interface, but it can still be
              set and retrieved through the API.

          account_type: The classification of this account, indicating its purpose within the chart of
              accounts.

              **NOTE**: You cannot create an account of type `non_posting` through the API
              because QuickBooks creates these accounts behind the scenes.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks. Defaults to `true`.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its hierarchical parent objects like `fullName`
              does. For example, two accounts could both have the `name` "Accounts-Payable",
              but they could have unique `fullName` values, such as
              "Corporate:Accounts-Payable" and "Finance:Accounts-Payable".

              Maximum length: 31 characters.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance of this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, this field will
              be `null`.

          sales_tax_code_id: The default sales-tax code for transactions with this account, determining
              whether the transactions are taxable or non-taxable. This can be overridden at
              the transaction or transaction-line level.

              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          tax_line_id: The identifier of the tax line associated with this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/accounts/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_number": account_number,
                    "account_type": account_type,
                    "bank_account_number": bank_account_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        full_names: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """Returns a list of accounts.

        NOTE: QuickBooks Desktop does not support pagination
        for accounts; hence, there is no `cursor` parameter. Users typically have few
        accounts.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_type: Filter for accounts of this type.

          currency_ids: Filter for accounts in these currencies.

          full_names: Filter for specific accounts by their full-name(s), case-insensitive. Like `id`,
              `fullName` is a unique identifier for an account, formed by by combining the
              names of its parent objects with its own `name`, separated by colons. For
              example, if an account is under "Corporate" and has the `name`
              "Accounts-Payable", its `fullName` would be "Corporate:Accounts-Payable".

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          ids: Filter for specific accounts by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

              **NOTE**: If any of the values you specify in this parameter are not found, the
              request will fail.

          limit: The maximum number of objects to return.

              **IMPORTANT**: QuickBooks Desktop does not support cursor-based pagination for
              accounts. This parameter will limit the response size, but you cannot fetch
              subsequent results using a cursor. For pagination, use the name-range parameters
              instead (e.g., `nameFrom=A&nameTo=B`).

              When this parameter is omitted, the endpoint returns all accounts without limit,
              unlike paginated endpoints which default to 150 records. This is acceptable
              because accounts typically have low record counts.

          name_contains: Filter for accounts whose `name` contains this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameStartsWith` or
              `nameEndsWith`.

          name_ends_with: Filter for accounts whose `name` ends with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameStartsWith`.

          name_from: Filter for accounts whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for accounts whose `name` starts with this substring, case-insensitive.
              NOTE: If you use this parameter, you cannot also use `nameContains` or
              `nameEndsWith`.

          name_to: Filter for accounts whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for accounts that are active, inactive, or both.

          updated_after: Filter for accounts updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for accounts updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_type": account_type,
                        "currency_ids": currency_ids,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
