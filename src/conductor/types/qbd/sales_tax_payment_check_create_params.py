# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxPaymentCheckCreateParams", "Line", "Address"]


class SalesTaxPaymentCheckCreateParams(TypedDict, total=False):
    bank_account_id: Required[Annotated[str, PropertyInfo(alias="bankAccountId")]]
    """
    The bank account from which the funds are being drawn for this sales-tax payment
    check; e.g., Checking or Savings. This sales-tax payment check will decrease the
    balance of this account.
    """

    lines: Required[Iterable[Line]]
    """
    The payment lines in this sales-tax payment check, each recording an amount paid
    toward a sales-tax item.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD)."""

    vendor_id: Required[Annotated[str, PropertyInfo(alias="vendorId")]]
    """
    The sales-tax agency, represented as a QuickBooks vendor, receiving this
    sales-tax payment check. This must match the tax vendor associated with the
    sales-tax items in the payment lines.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    address: Address
    """The address that is printed on the sales-tax payment check."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this sales-tax payment check is included in the queue of
    documents for QuickBooks to print.
    """

    memo: str
    """A memo or note for this sales-tax payment check."""

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this sales-tax payment
    check, which can be used to identify the transaction in QuickBooks. This value
    is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).

    **IMPORTANT**: For checks, this field is the check number.

    Maximum length: 11 characters.
    """


class Line(TypedDict, total=False):
    amount: Required[str]
    """
    The sales-tax payment amount paid toward this line's sales-tax item, represented
    as a decimal string.

    Decimal string format: exactly 2 decimal places when cents are included and up
    to 13 digits before the decimal point (for example, "123.45").
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item whose payable balance this sales-tax payment check line is
    paying.
    """


class Address(TypedDict, total=False):
    """The address that is printed on the sales-tax payment check."""

    city: str
    """The city, district, suburb, town, or village name of the address.

    Maximum length: 31 characters.
    """

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name).

    Maximum length: 41 characters.
    """

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).

    Maximum length: 41 characters.
    """

    line3: str
    """The third line of the address, if needed.

    Maximum length: 41 characters.
    """

    line4: str
    """The fourth line of the address, if needed.

    Maximum length: 41 characters.
    """

    line5: str
    """The fifth line of the address, if needed.

    Maximum length: 41 characters.
    """

    note: str
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address.

    Maximum length: 13 characters.
    """

    state: str
    """The state, county, province, or region name of the address.

    Maximum length: 21 characters.
    """
