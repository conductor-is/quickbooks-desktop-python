# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DiscountItemCreateParams", "Barcode"]


class DiscountItemCreateParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """
    The posting account to which transactions involving this discount item are
    posted for tracking discounts.
    """

    name: Required[str]
    """The case-insensitive name of this discount item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two discount
    items could both have the `name` "10% labor discount", but they could have
    unique `fullName` values, such as "Discounts:10% labor discount" and
    "Promotions:10% labor discount".

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    barcode: Barcode
    """The discount item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The discount item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    description: str
    """
    The discount item's description that will appear on sales forms that include
    this item.
    """

    discount_rate: Annotated[str, PropertyInfo(alias="discountRate")]
    """
    The monetary amount to subtract from the total or subtotal when applying this
    discount item to a transaction.

    **NOTE**: A flat rate discount applies to ALL lines recorded above it and
    distributes the discount amount equally across those lines, which affects tax
    calculations. For example, a $10 discount applied to a $100 taxable item and
    $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
    discount.
    """

    discount_rate_percent: Annotated[str, PropertyInfo(alias="discountRatePercent")]
    """
    The percentage amount to subtract from the total or subtotal when applying this
    discount item to a transaction.

    **NOTE**: A percentage discount only applies to the line immediately above it,
    so tax implications only affect that specific line.
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
    """Indicates whether this discount item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent discount item one level above this one in the hierarchy.

    For example, if this discount item has a `fullName` of "Discounts:10% labor
    discount", its parent has a `fullName` of "Discounts". If this discount item is
    at the top level, this field will be `null`.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for this discount item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """


class Barcode(TypedDict, total=False):
    """The discount item's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""
