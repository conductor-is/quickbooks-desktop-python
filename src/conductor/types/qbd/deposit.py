# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Deposit",
    "CashBack",
    "CashBackAccount",
    "Currency",
    "CustomField",
    "DepositToAccount",
    "Line",
    "LineAccount",
    "LineClass",
    "LineEntity",
    "LinePaymentMethod",
]


class CashBackAccount(BaseModel):
    """
    The account where this deposit cash-back line's cash-back amount is recorded, such as Petty Cash. This amount reduces the total credited to the deposit's destination account.
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


class CashBack(BaseModel):
    """
    Cash back taken out of this deposit and recorded to another account, such as Petty Cash.
    """

    id: str
    """The unique identifier assigned by QuickBooks to this deposit cash-back line.

    This ID is unique across all transaction line types.
    """

    account: CashBackAccount
    """
    The account where this deposit cash-back line's cash-back amount is recorded,
    such as Petty Cash. This amount reduces the total credited to the deposit's
    destination account.
    """

    amount: Optional[str] = None
    """
    The cash-back amount taken out of the deposit and recorded to this deposit
    cash-back line's account, represented as a decimal string.
    """

    memo: Optional[str] = None
    """A memo or note for this deposit cash-back line."""

    object_type: Literal["qbd_deposit_cash_back_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deposit_cash_back_line"`."""


class Currency(BaseModel):
    """The deposit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international values. For user-defined currencies, all values are editable.
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


class DepositToAccount(BaseModel):
    """The account where the funds for this deposit have been deposited."""

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


class LineAccount(BaseModel):
    """The account associated with this deposit line.

    For manual deposit lines, this is the account the funds were transferred from into the deposit's destination account.
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


class LineClass(BaseModel):
    """The deposit line's class.

    Classes can be used to categorize objects into meaningful segments, such as department, location, or type of work. In QuickBooks, class tracking is off by default.
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


class LineEntity(BaseModel):
    """
    The customer, vendor, employee, or person on QuickBooks's "Other Names" list associated with this deposit line.
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


class LinePaymentMethod(BaseModel):
    """The deposit line's payment method (e.g., cash, check, credit card)."""

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


class Line(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this deposit line.

    This ID is unique across all transaction line types.
    """

    account: Optional[LineAccount] = None
    """The account associated with this deposit line.

    For manual deposit lines, this is the account the funds were transferred from
    into the deposit's destination account.
    """

    amount: Optional[str] = None
    """
    The amount this deposit line contributes to the deposit's destination account,
    represented as a decimal string.
    """

    check_number: Optional[str] = FieldInfo(alias="checkNumber", default=None)
    """The check number of a check received for this deposit line."""

    class_: Optional[LineClass] = FieldInfo(alias="class", default=None)
    """The deposit line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    entity: Optional[LineEntity] = None
    """
    The customer, vendor, employee, or person on QuickBooks's "Other Names" list
    associated with this deposit line.
    """

    memo: Optional[str] = None
    """A memo or note for this deposit line."""

    object_type: Literal["qbd_deposit_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deposit_line"`."""

    payment_method: Optional[LinePaymentMethod] = FieldInfo(alias="paymentMethod", default=None)
    """The deposit line's payment method (e.g., cash, check, credit card)."""

    payment_transaction_id: Optional[str] = FieldInfo(alias="paymentTransactionId", default=None)
    """
    For payment-based deposit lines, the ID of the source payment included in this
    deposit line. For manual deposit lines, this is null.
    """

    payment_transaction_line_id: Optional[str] = FieldInfo(alias="paymentTransactionLineId", default=None)
    """
    For payment-based deposit lines, the line ID of the specific source payment line
    included in this deposit line. For manual deposit lines, this is null.
    """

    transaction_type: Optional[
        Literal[
            "ar_refund_credit_card",
            "bill",
            "bill_payment_check",
            "bill_payment_credit_card",
            "build_assembly",
            "charge",
            "check",
            "credit_card_charge",
            "credit_card_credit",
            "credit_memo",
            "deposit",
            "estimate",
            "inventory_adjustment",
            "invoice",
            "item_receipt",
            "journal_entry",
            "liability_adjustment",
            "paycheck",
            "payroll_liability_check",
            "purchase_order",
            "receive_payment",
            "sales_order",
            "sales_receipt",
            "sales_tax_payment_check",
            "transfer",
            "vendor_credit",
            "ytd_adjustment",
            "unknown",
        ]
    ] = FieldInfo(alias="transactionType", default=None)
    """The type of transaction for this deposit line."""


class Deposit(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this deposit.

    This ID is unique across all transaction types.
    """

    cash_back: Optional[CashBack] = FieldInfo(alias="cashBack", default=None)
    """
    Cash back taken out of this deposit and recorded to another account, such as
    Petty Cash.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this deposit was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    currency: Optional[Currency] = None
    """The deposit's currency.

    For built-in currencies, the name and code are standard ISO 4217 international
    values. For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the deposit object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    deposit_to_account: Optional[DepositToAccount] = FieldInfo(alias="depositToAccount", default=None)
    """The account where the funds for this deposit have been deposited."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this deposit's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    lines: List[Line]
    """
    The deposit's deposit lines, each representing either an existing payment
    selected for deposit or a manual transfer from another account into the deposit
    account.
    """

    memo: Optional[str] = None
    """A memo or note for this deposit."""

    object_type: Literal["qbd_deposit"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deposit"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this deposit object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    total_amount: Optional[str] = FieldInfo(alias="totalAmount", default=None)
    """
    The total monetary amount deposited into this deposit's destination account,
    represented as a decimal string.
    """

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    This deposit's total monetary amount converted to the home currency of the
    QuickBooks company file, represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this deposit, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this deposit was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
