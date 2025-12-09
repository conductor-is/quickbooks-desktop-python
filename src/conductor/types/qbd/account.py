# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Account", "Currency", "CustomField", "Parent", "SalesTaxCode", "TaxLineDetails"]


class Currency(BaseModel):
    """The account's currency.

    For built-in currencies, the name and code are standard international values. For user-defined currencies, all values are editable.
    """

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class Parent(BaseModel):
    """The parent account one level above this one in the hierarchy.

    For example, if this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a `fullName` of "Corporate". If this account is at the top level, this field will be `null`.
    """

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class SalesTaxCode(BaseModel):
    """
    The default sales-tax code for transactions with this account, determining whether the transactions are taxable or non-taxable. This can be overridden at the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign the default non-taxable code to all sales.
    """

    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class TaxLineDetails(BaseModel):
    """The account's tax line details, used for tax reporting purposes."""

    tax_line_id: float = FieldInfo(alias="taxLineId")
    """The identifier of the tax line associated with this account.

    You can see a list of all available values for this field by calling the
    endpoint for account tax lines.
    """

    tax_line_name: Optional[str] = FieldInfo(alias="taxLineName", default=None)
    """
    The name of the tax line associated with this account, as it appears on the tax
    form.
    """


class Account(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this account.

    This ID is unique across all accounts but not across different QuickBooks object
    types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The account's account number, which appears in the QuickBooks chart of accounts,
    reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

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
    ] = FieldInfo(alias="accountType")
    """
    The classification of this account, indicating its purpose within the chart of
    accounts.

    **NOTE**: You cannot create an account of type `non_posting` through the API
    because QuickBooks creates these accounts behind the scenes.
    """

    balance: Optional[str] = None
    """
    The current balance of this account only, excluding balances from any
    subordinate accounts, represented as a decimal string. Compare with
    `totalBalance`. Note that income accounts and balance sheet accounts may not
    have balances.
    """

    bank_account_number: Optional[str] = FieldInfo(alias="bankAccountNumber", default=None)
    """The bank account number or identifying note for this account.

    Access to this field may be restricted based on permissions.
    """

    cash_flow_classification: Optional[Literal["financing", "investing", "none", "not_applicable", "operating"]] = (
        FieldInfo(alias="cashFlowClassification", default=None)
    )
    """Indicates how this account is classified for cash flow reporting.

    If `none`, the account has not been classified. If `not_applicable`, the account
    does not qualify to be classified (e.g., a bank account tracking cash
    transactions is not part of a cash flow report).
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this account was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    currency: Optional[Currency] = None
    """The account's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the account object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this account."""

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this account, formed by
    combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if an account is under "Corporate" and has the
    `name` "Accounts-Payable", its `fullName` would be "Corporate:Accounts-Payable".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    account objects. However, `fullName` can still be arbitrarily changed by the
    QuickBooks user when they modify the underlying `name` field.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this account is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    is_tax_account: Optional[bool] = FieldInfo(alias="isTaxAccount", default=None)
    """Indicates whether this account is used for tracking taxes."""

    name: str
    """The case-insensitive name of this account.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two accounts
    could both have the `name` "Accounts-Payable", but they could have unique
    `fullName` values, such as "Corporate:Accounts-Payable" and
    "Finance:Accounts-Payable".
    """

    object_type: Literal["qbd_account"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_account"`."""

    parent: Optional[Parent] = None
    """The parent account one level above this one in the hierarchy.

    For example, if this account has a `fullName` of "Corporate:Accounts-Payable",
    its parent has a `fullName` of "Corporate". If this account is at the top level,
    this field will be `null`.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this account object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The default sales-tax code for transactions with this account, determining
    whether the transactions are taxable or non-taxable. This can be overridden at
    the transaction or transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    special_account_type: Optional[
        Literal[
            "accounts_payable",
            "accounts_receivable",
            "condense_item_adjustment_expenses",
            "cost_of_goods_sold",
            "direct_deposit_liabilities",
            "estimates",
            "exchange_gain_loss",
            "inventory_assets",
            "item_receipt_account",
            "opening_balance_equity",
            "payroll_expenses",
            "payroll_liabilities",
            "petty_cash",
            "purchase_orders",
            "reconciliation_differences",
            "retained_earnings",
            "sales_orders",
            "sales_tax_payable",
            "uncategorized_expenses",
            "uncategorized_income",
            "undeposited_funds",
        ]
    ] = FieldInfo(alias="specialAccountType", default=None)
    """
    Indicates if this account is a special account automatically created by
    QuickBooks for specific purposes.
    """

    sublevel: float
    """The depth level of this account in the hierarchy.

    A top-level account has a `sublevel` of 0; each subsequent sublevel increases
    this number by 1. For example, an account with a `fullName` of
    "Corporate:Accounts-Payable" would have a `sublevel` of 1.
    """

    tax_line_details: Optional[TaxLineDetails] = FieldInfo(alias="taxLineDetails", default=None)
    """The account's tax line details, used for tax reporting purposes."""

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)
    """
    The combined balance of this account and all its sub-accounts, represented as a
    decimal string. For example, the `totalBalance` for XYZ Bank would be the total
    of the balances of all its sub-accounts (checking, savings, and so on). If XYZ
    Bank did not have any sub-accounts, `totalBalance` and `balance` would be the
    same.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this account was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
