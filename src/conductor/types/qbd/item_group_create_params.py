# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemGroupCreateParams", "Barcode", "Line"]


class ItemGroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this item group, unique across all item
    groups.

    **NOTE**: Item groups do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    should_print_items_in_group: Required[Annotated[bool, PropertyInfo(alias="shouldPrintItemsInGroup")]]
    """
    Indicates whether the individual items in this item group and their separate
    amounts appear on printed forms.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    barcode: Barcode
    """The item group's barcode."""

    description: str
    """
    The item group's description that will appear on sales forms that include this
    item.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this item group is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    lines: Iterable[Line]
    """The item lines in this item group."""

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
