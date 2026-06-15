# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesTaxPaymentCheck", "Address", "BankAccount", "CustomField", "Line", "LineSalesTaxItem", "Vendor"]


class Address(BaseModel):
    """The address that is printed on the sales-tax payment check."""

    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class BankAccount(BaseModel):
    """
    The bank account from which the funds are being drawn for this sales-tax payment check; e.g., Checking or Savings. This sales-tax payment check will decrease the balance of this account.
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


class LineSalesTaxItem(BaseModel):
    """
    The sales-tax item whose payable balance this sales-tax payment check line is paying.
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


class Line(BaseModel):
    id: str
    """
    The unique identifier assigned by QuickBooks to this sales-tax payment check
    line. This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """
    The sales-tax payment amount paid toward this line's sales-tax item, represented
    as a decimal string.
    """

    object_type: Literal["qbd_sales_tax_payment_check_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_payment_check_line"`."""

    sales_tax_item: Optional[LineSalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item whose payable balance this sales-tax payment check line is
    paying.
    """

    tax_amount: Optional[str] = FieldInfo(alias="taxAmount", default=None)
    """
    The sales-tax amount due on this sales-tax payment check line, represented as a
    decimal string. QuickBooks Desktop returns this field only for Australian
    company files.
    """


class Vendor(BaseModel):
    """
    The sales-tax agency, represented as a QuickBooks vendor, receiving this sales-tax payment check. This must match the tax vendor associated with the sales-tax items in the payment lines.
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


class SalesTaxPaymentCheck(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales-tax payment check.

    This ID is unique across all transaction types.
    """

    address: Optional[Address] = None
    """The address that is printed on the sales-tax payment check."""

    amount: str
    """
    The total monetary amount of this sales-tax payment check, represented as a
    decimal string. This equals the sum of the amounts in the sales-tax payment
    check lines.
    """

    bank_account: BankAccount = FieldInfo(alias="bankAccount")
    """
    The bank account from which the funds are being drawn for this sales-tax payment
    check; e.g., Checking or Savings. This sales-tax payment check will decrease the
    balance of this account.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales-tax payment check was created, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales-tax payment check object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this sales-tax payment check is included in the queue of
    documents for QuickBooks to print.
    """

    lines: List[Line]
    """
    The payment lines in this sales-tax payment check, each recording an amount paid
    toward a sales-tax item.
    """

    memo: Optional[str] = None
    """A memo or note for this sales-tax payment check."""

    object_type: Literal["qbd_sales_tax_payment_check"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_payment_check"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this sales-tax payment
    check, which can be used to identify the transaction in QuickBooks. This value
    is not required to be unique and can be arbitrarily changed by the QuickBooks
    user.

    **IMPORTANT**: For checks, this field is the check number.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this sales-tax payment check
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales-tax payment check was last updated, in ISO
    8601 format (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in
    the local timezone of the end-user's computer.
    """

    vendor: Optional[Vendor] = None
    """
    The sales-tax agency, represented as a QuickBooks vendor, receiving this
    sales-tax payment check. This must match the tax vendor associated with the
    sales-tax items in the payment lines.
    """
