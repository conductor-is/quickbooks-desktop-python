# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JournalEntryCreateParams", "CreditLine", "DebitLine"]


class JournalEntryCreateParams(TypedDict, total=False):
    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this journal entry, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    are_amounts_entered_in_home_currency: Annotated[bool, PropertyInfo(alias="areAmountsEnteredInHomeCurrency")]
    """
    Indicates whether the amounts in this journal entry were entered in the
    company's home currency rather than a foreign currency. When `true`, amounts are
    in the home currency regardless of the `currency` field.
    """

    credit_lines: Annotated[Iterable[CreditLine], PropertyInfo(alias="creditLines")]
    """The journal entry's credit lines."""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The journal entry's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    debit_lines: Annotated[Iterable[DebitLine], PropertyInfo(alias="debitLines")]
    """The journal entry's debit lines."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this journal entry's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_adjustment: Annotated[bool, PropertyInfo(alias="isAdjustment")]
    """Indicates whether this journal entry is an adjustment entry.

    When `true`, QuickBooks retains the original entry information to maintain an
    audit trail of the adjustments.
    """

    is_home_currency_adjustment: Annotated[bool, PropertyInfo(alias="isHomeCurrencyAdjustment")]
    """
    Indicates whether this journal entry is an adjustment made in the company's home
    currency for a transaction that was originally recorded in a foreign currency.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this journal entry, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).
    """


class CreditLine(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """The account to which this journal credit line is being credited.

    This will increase the balance of this account.
    """

    amount: str
    """
    The monetary amount of this journal credit line, represented as a decimal
    string.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this journal credit line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The journal credit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all journal credit lines unless overridden here, at the
    transaction line level.
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """
    The customer, vendor, employee, or other entity associated with this journal
    credit line.

    **IMPORTANT**: If the journal credit line's `account` is an Accounts Receivable
    (A/R) account, this field must refer to a customer. If the journal credit line's
    `account` is an Accounts Payable (A/P) account, this field must refer to a
    vendor. If these requirements are not met, QuickBooks Desktop will not record
    the transaction.
    """

    memo: str
    """A memo or note for this journal credit line."""

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this journal
    credit line's transactions by applying a specific tax rate collected for a
    single tax agency. Unlike `salesTaxCode`, which only indicates general
    taxability, this field drives the actual tax calculation and reporting.
    """


class DebitLine(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """The account to which this journal debit line is being debited.

    This will decrease the balance of this account.
    """

    amount: str
    """
    The monetary amount of this journal debit line, represented as a decimal string.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this journal debit line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The journal debit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all journal debit lines unless overridden here, at the
    transaction line level.
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """
    The customer, vendor, employee, or other entity associated with this journal
    debit line.

    **IMPORTANT**: If the journal debit line's `account` is an Accounts Receivable
    (A/R) account, this field must refer to a customer. If the journal debit line's
    `account` is an Accounts Payable (A/P) account, this field must refer to a
    vendor. If these requirements are not met, QuickBooks Desktop will not record
    the transaction.
    """

    memo: str
    """A memo or note for this journal debit line."""

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this journal
    debit line's transactions by applying a specific tax rate collected for a single
    tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """
