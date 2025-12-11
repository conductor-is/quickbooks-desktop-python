# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CurrencyCreateParams", "CurrencyFormat"]


class CurrencyCreateParams(TypedDict, total=False):
    currency_code: Required[Annotated[str, PropertyInfo(alias="currencyCode")]]
    """
    The internationally accepted currency code used by this currency, typically
    based on the ISO 4217 standard (for example, USD for US Dollars). Built-in
    QuickBooks currencies follow ISO 4217. For user-defined currencies, following
    ISO 4217 is recommended but not required. In many cases, the three-letter code
    is formed from the country's two-letter internet code plus a currency letter
    (e.g., BZ + D → BZD for Belize Dollar).

    Maximum length: 3 characters.
    """

    name: Required[str]
    """The case-insensitive unique name of this currency, unique across all currencies.

    For built-in currencies, the name is the internationally accepted currency name
    and is not editable.

    **NOTE**: Currencies do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 64 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    currency_format: Annotated[CurrencyFormat, PropertyInfo(alias="currencyFormat")]
    """
    Controls how this currency displays thousands separators, grouping, and decimal
    places.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this currency is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """


class CurrencyFormat(TypedDict, total=False):
    """
    Controls how this currency displays thousands separators, grouping, and decimal places.
    """

    decimal_places: Annotated[Literal["0", "2"], PropertyInfo(alias="decimalPlaces")]
    """Controls the number of decimal places displayed for currency values.

    Use `0` to hide decimals or `2` to display cents.
    """

    decimal_separator: Annotated[Literal["comma", "period"], PropertyInfo(alias="decimalSeparator")]
    """
    Controls the decimal separator when displaying currency values (for example,
    "1.00" vs "1,00"). Defaults to period.
    """

    thousand_separator: Annotated[
        Literal["apostrophe", "comma", "period", "space"], PropertyInfo(alias="thousandSeparator")
    ]
    """
    Controls the thousands separator when displaying currency values (for example,
    "1,000,000"). Defaults to comma.
    """

    thousand_separator_grouping: Annotated[
        Literal["x_xx_xx_xxx", "xx_xxx_xxx"], PropertyInfo(alias="thousandSeparatorGrouping")
    ]
    """
    Controls how digits are grouped for thousands when displaying currency values
    (for example, "10,000,000").
    """
