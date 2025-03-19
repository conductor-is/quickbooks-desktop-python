# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JournalEntryUpdateParams", "Line"]


class JournalEntryUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the journal entry object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

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

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The journal entry's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this journal entry's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    is_adjustment: Annotated[bool, PropertyInfo(alias="isAdjustment")]
    """Indicates whether this journal entry is an adjustment entry.

    When `true`, QuickBooks retains the original entry information to maintain an
    audit trail of the adjustments.
    """

    lines: Iterable[Line]
    """The journal entry's credit and debit lines.

    **IMPORTANT**: When updating journal entries, you must include ALL existing
    journal lines (both credit and debit) in your update request, even if you only
    want to modify a single line. QuickBooks will automatically delete any existing
    lines that are not included in the update request, which is why all lines must
    be provided in a single array when updating.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this journal entry, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this journal entry, in ISO 8601 format (YYYY-MM-DD)."""


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing journal line you wish
    to retain or update.

    **IMPORTANT**: Set this field to `-1` for new journal lines you wish to add.
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """The account to which this journal line is being credited or debited."""

    amount: str
    """The monetary amount of this journal line, represented as a decimal string."""

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this journal line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The journal line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all journal lines unless overridden here, at the
    transaction line level.
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """
    The customer, vendor, employee, or other entity associated with this journal
    line.

    **IMPORTANT**: If the journal line's `account` is an Accounts Receivable (A/R)
    account, this field must refer to a customer. If the journal line's `account` is
    an Accounts Payable (A/P) account, this field must refer to a vendor. If these
    requirements are not met, QuickBooks Desktop will not record the transaction.
    """

    journal_line_type: Annotated[Literal["debit", "credit"], PropertyInfo(alias="journalLineType")]
    """The type of journal line (debit or credit)."""

    memo: str
    """A memo or note for this journal line."""

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this journal
    line's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """
