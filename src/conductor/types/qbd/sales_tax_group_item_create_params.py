# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SalesTaxGroupItemCreateParams", "Barcode"]


class SalesTaxGroupItemCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this sales-tax group item, unique across all
    sales-tax group items.

    **NOTE**: Sales-tax group items do not have a `fullName` field because they are
    not hierarchical objects, which is why `name` is unique for them but not for
    objects that have parents.

    Maximum length: 31 characters.
    """

    sales_tax_item_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="salesTaxItemIds")]]
    """The sales-tax items that make up this sales-tax group item.

    QuickBooks Desktop applies these sales-tax items together as one tax selection
    while tracking each sales tax separately.
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

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax group item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """


class Barcode(TypedDict, total=False):
    """The sales-tax group item's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""
