# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    account_type: Required[
        Annotated[
            Literal[
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
            PropertyInfo(alias="accountType"),
        ]
    ]
    """
    The classification of this account, indicating its purpose within the chart of
    accounts.

    **NOTE**: You cannot create an account of type `non_posting` through the API
    because QuickBooks creates these accounts behind the scenes.
    """

    name: Required[str]
    """The case-insensitive name of this account.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two accounts
    could both have the `name` "Accounts-Payable", but they could have unique
    `fullName` values, such as "Corporate:Accounts-Payable" and
    "Finance:Accounts-Payable".

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The account's account number, which appears in the QuickBooks chart of accounts,
    reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    bank_account_number: Annotated[str, PropertyInfo(alias="bankAccountNumber")]
    """The bank account number or identifying note for this account.

    Access to this field may be restricted based on permissions.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The account's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    description: str
    """A description of this account."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this account is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    opening_balance: Annotated[str, PropertyInfo(alias="openingBalance")]
    """The amount of money in, or the value of, this account as of
    `openingBalanceDate`.

    On a bank statement, this would be the amount of money in the account at the
    beginning of the statement period.
    """

    opening_balance_date: Annotated[Union[str, date], PropertyInfo(alias="openingBalanceDate", format="iso8601")]
    """
    The date of the opening balance of this account, in ISO 8601 format
    (YYYY-MM-DD).
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent account one level above this one in the hierarchy.

    For example, if this account has a `fullName` of "Corporate:Accounts-Payable",
    its parent has a `fullName` of "Corporate". If this account is at the top level,
    this field will be `null`.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for transactions with this account, determining
    whether the transactions are taxable or non-taxable. This can be overridden at
    the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    tax_line_id: Annotated[float, PropertyInfo(alias="taxLineId")]
    """The identifier of the tax line associated with this account."""
