# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxItemUpdateParams", "Barcode"]


class SalesTaxItemUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the sales-tax item object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    barcode: Barcode
    """The sales-tax item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales-tax item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    description: str
    """
    The sales-tax item's description that will appear on sales forms that include
    this item.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax item, unique across all
    sales-tax items.

    **NOTE**: Sales-tax items do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents.

    Maximum length: 31 characters.
    """

    sales_tax_return_line_id: Annotated[str, PropertyInfo(alias="salesTaxReturnLineId")]
    """
    The specific line on the sales tax return form where the tax collected using
    this sales-tax item should be reported.
    """

    tax_rate: Annotated[str, PropertyInfo(alias="taxRate")]
    """The tax rate defined by this sales-tax item, represented as a decimal string.

    For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
    of sales tax applied when this item is used in transactions. If a non-zero
    `taxRate` is specified, then the `taxVendor` field is required.
    """

    tax_vendor_id: Annotated[str, PropertyInfo(alias="taxVendorId")]
    """
    The tax agency (vendor) to whom collected sales taxes are owed for this
    sales-tax item. This field refers to a vendor in QuickBooks that represents the
    tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
    required.
    """


class Barcode(TypedDict, total=False):
    """The sales-tax item's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""
