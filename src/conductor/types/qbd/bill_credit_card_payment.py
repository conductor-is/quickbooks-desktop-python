# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..custom_field import CustomField
from ..receivable_transaction import ReceivableTransaction

__all__ = ["BillCreditCardPayment", "CreditCardAccount", "Currency", "PayablesAccount", "Vendor"]


class CreditCardAccount(BaseModel):
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


class PayablesAccount(BaseModel):
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


class Vendor(BaseModel):
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


class BillCreditCardPayment(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this bill credit card payment.

    This ID is unique across all transaction types.
    """

    amount: Optional[str] = None
    """
    The monetary amount of this bill credit card payment, represented as a decimal
    string.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The total monetary amount for this bill credit card payment converted to the
    home currency of the QuickBooks company file. Represented as a decimal string.
    """

    applied_to_transactions: List[ReceivableTransaction] = FieldInfo(alias="appliedToTransactions")
    """The bill(s) paid by this bill credit card payment."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this bill credit card payment was created, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """

    credit_card_account: CreditCardAccount = FieldInfo(alias="creditCardAccount")
    """The credit card account to which this bill credit card payment is being charged.

    This bill credit card payment will decrease the balance of this account.
    """

    currency: Optional[Currency] = None
    """The bill credit card payment's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the bill credit card payment object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this bill credit card payment's currency and
    the home currency in QuickBooks at the time of this transaction. Represented as
    a decimal value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home
    currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    memo: Optional[str] = None
    """A memo or note for this bill credit card payment."""

    object_type: Literal["qbd_bill_credit_card_payment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill_credit_card_payment"`."""

    payables_account: Optional[PayablesAccount] = FieldInfo(alias="payablesAccount", default=None)
    """
    The Accounts-Payable (A/P) account to which this bill credit card payment is
    assigned, used to track the amount owed. If not specified, QuickBooks Desktop
    will use its default A/P account.

    **IMPORTANT**: If this bill credit card payment is linked to other transactions,
    this A/P account must match the `payablesAccount` used in those other
    transactions.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this bill credit card
    payment, which can be used to identify the transaction in QuickBooks. This value
    is not required to be unique and can be arbitrarily changed by the QuickBooks
    user.

    **IMPORTANT**: For checks, this field is the check number.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this bill credit card payment object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this bill credit card payment, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this bill credit card payment was last updated, in ISO
    8601 format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's
    time zone in QuickBooks.
    """

    vendor: Optional[Vendor] = None
    """
    The vendor who sent the bill(s) that this bill credit card payment is paying and
    who will receive this payment.

    **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
    `applyToTransactions`.
    """
