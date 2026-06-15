# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SalesTaxGroupItemUpdateParams", "Barcode"]


class SalesTaxGroupItemUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the sales-tax group item
    object you are updating, which you can get by fetching the object first. Provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    barcode: Barcode
    """The sales-tax group item's barcode."""

    description: str
    """
    The sales-tax group item's description that will appear on sales forms that
    include this item.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax group item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax group item, unique across all
    sales-tax group items.

    **NOTE**: Sales-tax group items do not have a `fullName` field because they are
    not hierarchical objects, which is why `name` is unique for them but not for
    objects that have parents.

    Maximum length: 31 characters.
    """

    sales_tax_item_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="salesTaxItemIds")]
    """The sales-tax items that make up this sales-tax group item.

    QuickBooks Desktop applies these sales-tax items together as one tax selection
    while tracking each sales tax separately.
    """


class Barcode(TypedDict, total=False):
    """The sales-tax group item's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""
