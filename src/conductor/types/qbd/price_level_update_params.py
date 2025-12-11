# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PriceLevelUpdateParams", "PerItemPriceLevel"]


class PriceLevelUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the price level object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The price level's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    fixed_percentage: Annotated[str, PropertyInfo(alias="fixedPercentage")]
    """
    The fixed percentage adjustment applied to all items for this price level
    (instead of a per-item price level). Once you create the price level, you cannot
    change this.

    When this price level is applied to a customer, it automatically adjusts the
    `rate` and `amount` columns for applicable line items in sales orders and
    invoices for that customer. This value supports both positive and negative
    values - a value of "20" increases prices by 20%, while "-10" decreases prices
    by 10%.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this price level is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this price level, unique across all price
    levels.

    **NOTE**: Price levels do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    per_item_price_levels: Annotated[Iterable[PerItemPriceLevel], PropertyInfo(alias="perItemPriceLevels")]
    """The per-item price level configurations for this price level."""


class PerItemPriceLevel(TypedDict, total=False):
    adjust_percentage: Required[Annotated[str, PropertyInfo(alias="adjustPercentage")]]
    """
    The percentage adjustment for this per-item price level when using relative
    pricing. Specifies a percentage to modify pricing, using positive values (e.g.,
    "20") to increase prices by that percentage, or negative values (e.g., "-10") to
    apply a discount.
    """

    adjust_relative_to: Required[
        Annotated[Literal["cost", "current_custom_price", "standard_price"], PropertyInfo(alias="adjustRelativeTo")]
    ]
    """The base value reference for this per-item price level's percentage adjustment.

    Specifies which price to use as the starting point for the adjustment
    calculation in the price level.

    **NOTE:** The price level must use either a fixed pricing approach
    (`customPrice` or `customPricePercent`) or a relative adjustment approach
    (`adjustPercentage` with `adjustRelativeTo`) when configuring per-item price
    levels.
    """

    item_id: Required[Annotated[str, PropertyInfo(alias="itemId")]]
    """The item associated with this per-item price level.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    custom_price: Annotated[str, PropertyInfo(alias="customPrice")]
    """
    The fixed amount custom price for this per-item price level that overrides the
    standard price for the specified item. Used when setting an absolute price value
    for the item in this price level.
    """

    custom_price_percent: Annotated[str, PropertyInfo(alias="customPricePercent")]
    """
    The fixed discount percentage for this per-item price level that modifies the
    specified item's standard price. Used to create a fixed percentage markup or
    discount specific to this item within this price level.
    """
