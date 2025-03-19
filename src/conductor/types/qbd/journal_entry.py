# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "JournalEntry",
    "CreditLine",
    "CreditLineAccount",
    "CreditLineClass",
    "CreditLineEntity",
    "CreditLineSalesTaxItem",
    "Currency",
    "CustomField",
    "DebitLine",
    "DebitLineAccount",
    "DebitLineClass",
    "DebitLineEntity",
    "DebitLineSalesTaxItem",
]


class CreditLineAccount(BaseModel):
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


class CreditLineClass(BaseModel):
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


class CreditLineEntity(BaseModel):
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


class CreditLineSalesTaxItem(BaseModel):
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


class CreditLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this journal credit line.

    This ID is unique across all transaction line types.
    """

    account: CreditLineAccount
    """The account to which this journal credit line is being credited.

    This will increase the balance of this account.
    """

    amount: Optional[str] = None
    """
    The monetary amount of this journal credit line, represented as a decimal
    string.
    """

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this journal credit line."""

    class_: Optional[CreditLineClass] = FieldInfo(alias="class", default=None)
    """The journal credit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all journal credit lines unless overridden here, at the
    transaction line level.
    """

    entity: Optional[CreditLineEntity] = None
    """
    The customer, vendor, employee, or other entity associated with this journal
    credit line.

    **IMPORTANT**: If the journal credit line's `account` is an Accounts Receivable
    (A/R) account, this field must refer to a customer. If the journal credit line's
    `account` is an Accounts Payable (A/P) account, this field must refer to a
    vendor. If these requirements are not met, QuickBooks Desktop will not record
    the transaction.
    """

    memo: Optional[str] = None
    """A memo or note for this journal credit line."""

    object_type: Literal["qbd_journal_credit_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_journal_credit_line"`."""

    sales_tax_item: Optional[CreditLineSalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this journal
    credit line's transactions by applying a specific tax rate collected for a
    single tax agency. Unlike `salesTaxCode`, which only indicates general
    taxability, this field drives the actual tax calculation and reporting.
    """


class Currency(BaseModel):
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


class DebitLineAccount(BaseModel):
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


class DebitLineClass(BaseModel):
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


class DebitLineEntity(BaseModel):
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


class DebitLineSalesTaxItem(BaseModel):
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


class DebitLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this journal debit line.

    This ID is unique across all transaction line types.
    """

    account: Optional[DebitLineAccount] = None
    """The account to which this journal debit line is being debited.

    This will decrease the balance of this account.
    """

    amount: Optional[str] = None
    """
    The monetary amount of this journal debit line, represented as a decimal string.
    """

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this journal debit line."""

    class_: Optional[DebitLineClass] = FieldInfo(alias="class", default=None)
    """The journal debit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all journal debit lines unless overridden here, at the
    transaction line level.
    """

    entity: Optional[DebitLineEntity] = None
    """
    The customer, vendor, employee, or other entity associated with this journal
    debit line.

    **IMPORTANT**: If the journal debit line's `account` is an Accounts Receivable
    (A/R) account, this field must refer to a customer. If the journal debit line's
    `account` is an Accounts Payable (A/P) account, this field must refer to a
    vendor. If these requirements are not met, QuickBooks Desktop will not record
    the transaction.
    """

    memo: Optional[str] = None
    """A memo or note for this journal debit line."""

    object_type: Literal["qbd_journal_debit_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_journal_debit_line"`."""

    sales_tax_item: Optional[DebitLineSalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this journal
    debit line's transactions by applying a specific tax rate collected for a single
    tax agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """


class JournalEntry(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this journal entry.

    This ID is unique across all transaction types.
    """

    are_amounts_entered_in_home_currency: Optional[bool] = FieldInfo(
        alias="areAmountsEnteredInHomeCurrency", default=None
    )
    """
    Indicates whether the amounts in this journal entry were entered in the
    company's home currency rather than a foreign currency. When `true`, amounts are
    in the home currency regardless of the `currency` field.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this journal entry was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_lines: List[CreditLine] = FieldInfo(alias="creditLines")
    """The journal entry's credit lines."""

    currency: Optional[Currency] = None
    """The journal entry's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the journal entry object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    debit_lines: List[DebitLine] = FieldInfo(alias="debitLines")
    """The journal entry's debit lines."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this journal entry's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_adjustment: Optional[bool] = FieldInfo(alias="isAdjustment", default=None)
    """Indicates whether this journal entry is an adjustment entry.

    When `true`, QuickBooks retains the original entry information to maintain an
    audit trail of the adjustments.
    """

    is_home_currency_adjustment: Optional[bool] = FieldInfo(alias="isHomeCurrencyAdjustment", default=None)
    """
    Indicates whether this journal entry is an adjustment made in the company's home
    currency for a transaction that was originally recorded in a foreign currency.
    """

    object_type: Literal["qbd_journal_entry"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_journal_entry"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this journal entry, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this journal entry object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this journal entry, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this journal entry was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
