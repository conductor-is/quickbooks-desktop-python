# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Currency", "CurrencyFormat"]


class CurrencyFormat(BaseModel):
    """
    Controls how this currency displays thousands separators, grouping, and decimal places.
    """

    decimal_places: Optional[Literal["0", "2"]] = FieldInfo(alias="decimalPlaces", default=None)
    """Controls the number of decimal places displayed for currency values.

    Use `0` to hide decimals or `2` to display cents.
    """

    decimal_separator: Optional[Literal["comma", "period"]] = FieldInfo(alias="decimalSeparator", default=None)
    """
    Controls the decimal separator when displaying currency values (for example,
    "1.00" vs "1,00"). Defaults to period.
    """

    thousand_separator: Optional[Literal["apostrophe", "comma", "period", "space"]] = FieldInfo(
        alias="thousandSeparator", default=None
    )
    """
    Controls the thousands separator when displaying currency values (for example,
    "1,000,000"). Defaults to comma.
    """

    thousand_separator_grouping: Optional[Literal["x_xx_xx_xxx", "xx_xxx_xxx"]] = FieldInfo(
        alias="thousandSeparatorGrouping", default=None
    )
    """
    Controls how digits are grouped for thousands when displaying currency values
    (for example, "10,000,000").
    """


class Currency(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this currency.

    This ID is unique across all currencies but not across different QuickBooks
    object types.
    """

    as_of_date: Optional[date] = FieldInfo(alias="asOfDate", default=None)
    """
    The date when the exchange rate for this currency was last updated, in ISO 8601
    format (YYYY-MM-DD).
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this currency was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    currency_code: str = FieldInfo(alias="currencyCode")
    """
    The internationally accepted currency code used by this currency, typically
    based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
    QuickBooks currencies follow ISO 4217. For user-defined currencies, following
    ISO 4217 is recommended but not required. In many cases, the three-letter code
    is formed from the country's two-letter internet code plus a currency letter
    (e.g., BZ + D → BZD for Belize Dollar).
    """

    currency_format: Optional[CurrencyFormat] = FieldInfo(alias="currencyFormat", default=None)
    """
    Controls how this currency displays thousands separators, grouping, and decimal
    places.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this currency's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this currency is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    is_user_defined_currency: Optional[bool] = FieldInfo(alias="isUserDefinedCurrency", default=None)
    """
    Indicates whether this currency was created by a QuickBooks user (`true`) or is
    a built-in currency (`false`).
    """

    name: str
    """The case-insensitive unique name of this currency, unique across all currencies.

    For built-in currencies, the name is the internationally accepted currency name
    and is not editable.

    **NOTE**: Currencies do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.
    """

    object_type: Literal["qbd_currency"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_currency"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this currency object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this currency was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
