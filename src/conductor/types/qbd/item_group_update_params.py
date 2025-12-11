# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemGroupUpdateParams", "Barcode", "Line"]


class ItemGroupUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the item group object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    barcode: Barcode
    """The item group's barcode."""

    clear_item_lines: Annotated[bool, PropertyInfo(alias="clearItemLines")]
    """When `true`, removes all existing item lines associated with this item group.

    To modify or add individual item lines, use the field `itemLines` instead.
    """

    description: str
    """
    The item group's description that will appear on sales forms that include this
    item.
    """

    force_unit_of_measure_change: Annotated[bool, PropertyInfo(alias="forceUnitOfMeasureChange")]
    """
    Indicates whether to allow changing the item group's unit-of-measure set (using
    the `unitOfMeasureSetId` field) when the base unit of the new unit-of-measure
    set does not match that of the currently assigned set. Without setting this
    field to `true` in this scenario, the request will fail with an error; hence,
    this field is equivalent to accepting the warning prompt in the QuickBooks UI.

    NOTE: Changing the base unit requires you to update the item's
    quantities-on-hand and cost to reflect the new unit; otherwise, these values
    will be inaccurate. Alternatively, consider creating a new item with the desired
    unit-of-measure set and deactivating the old item.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this item group is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    lines: Iterable[Line]
    """The item lines in this item group."""

    name: str
    """
    The case-insensitive unique name of this item group, unique across all item
    groups.

    **NOTE**: Item groups do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    should_print_items_in_group: Annotated[bool, PropertyInfo(alias="shouldPrintItemsInGroup")]
    """
    Indicates whether the individual items in this item group and their separate
    amounts appear on printed forms.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this item group, which consists of a
    base unit and related units.
    """


class Barcode(TypedDict, total=False):
    """The item group's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""


class Line(TypedDict, total=False):
    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this item group line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    quantity: float
    """The quantity of the item group associated with this item group line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item group is a discount item
    group.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this item group line.

    Must be a valid unit within the item's available units of measure.
    """
