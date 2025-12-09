# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PriceLevel", "Currency", "PerItemPriceLevel", "PerItemPriceLevelItem"]


class Currency(BaseModel):
    """The price level's currency.

    For built-in currencies, the name and code are standard international values. For user-defined currencies, all values are editable.
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


class PerItemPriceLevelItem(BaseModel):
    """The item associated with this per-item price level.

    This can refer to any good or service that the business buys or sells, including item types such as a service item, inventory item, or special calculation item like a discount item or sales-tax item.
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


class PerItemPriceLevel(BaseModel):
    custom_price: Optional[str] = FieldInfo(alias="customPrice", default=None)
    """
    The fixed amount custom price for this per-item price level that overrides the
    standard price for the specified item. Used when setting an absolute price value
    for the item in this price level.
    """

    custom_price_percent: Optional[str] = FieldInfo(alias="customPricePercent", default=None)
    """
    The fixed discount percentage for this per-item price level that modifies the
    specified item's standard price. Used to create a fixed percentage markup or
    discount specific to this item within this price level.
    """

    item: PerItemPriceLevelItem
    """The item associated with this per-item price level.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """


class PriceLevel(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this price level.

    This ID is unique across all price levels but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this price level was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    currency: Optional[Currency] = None
    """The price level's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    fixed_percentage: Optional[str] = FieldInfo(alias="fixedPercentage", default=None)
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

    is_active: bool = FieldInfo(alias="isActive")
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
    """

    object_type: Literal["qbd_price_level"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_price_level"`."""

    per_item_price_levels: List[PerItemPriceLevel] = FieldInfo(alias="perItemPriceLevels")
    """The per-item price level configurations for this price level."""

    price_level_type: Literal["fixed_percentage", "per_item"] = FieldInfo(alias="priceLevelType")
    """The price level's type."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this price level object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this price level was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
