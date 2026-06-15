# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxPaymentCheckUpdateParams", "Address"]


class SalesTaxPaymentCheckUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the sales-tax payment check
    object you are updating, which you can get by fetching the object first. Provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    address: Address
    """The address that is printed on the sales-tax payment check."""

    bank_account_id: Annotated[str, PropertyInfo(alias="bankAccountId")]
    """
    The bank account from which the funds are being drawn for this sales-tax payment
    check; e.g., Checking or Savings. This sales-tax payment check will decrease the
    balance of this account.
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
    user.

    **IMPORTANT**: For checks, this field is the check number.

    Maximum length: 11 characters.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this sales-tax payment check, in ISO 8601 format (YYYY-MM-DD)."""


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
