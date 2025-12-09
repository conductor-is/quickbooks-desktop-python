# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DiscountItem", "Account", "Class", "CustomField", "Parent", "SalesTaxCode"]


class Account(BaseModel):
    """
    The posting account to which transactions involving this discount item are posted for tracking discounts.
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


class Class(BaseModel):
    """The discount item's class.

    Classes can be used to categorize objects into meaningful segments, such as department, location, or type of work. In QuickBooks, class tracking is off by default.
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


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: str = FieldInfo(alias="ownerId")
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class Parent(BaseModel):
    """The parent discount item one level above this one in the hierarchy.

    For example, if this discount item has a `fullName` of "Discounts:10% labor discount", its parent has a `fullName` of "Discounts". If this discount item is at the top level, this field will be `null`.
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


class SalesTaxCode(BaseModel):
    """
    The default sales-tax code for this discount item, determining whether it is taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign the default non-taxable code to all sales.
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


class DiscountItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this discount item.

    This ID is unique across all discount items but not across different QuickBooks
    object types.
    """

    account: Account
    """
    The posting account to which transactions involving this discount item are
    posted for tracking discounts.
    """

    barcode: Optional[str] = None
    """The discount item's barcode."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The discount item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this discount item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the discount item object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """
    The discount item's description that will appear on sales forms that include
    this item.
    """

    discount_rate: Optional[str] = FieldInfo(alias="discountRate", default=None)
    """
    The monetary amount to subtract from the total or subtotal when applying this
    discount item to a transaction.

    **NOTE**: A flat rate discount applies to ALL lines recorded above it and
    distributes the discount amount equally across those lines, which affects tax
    calculations. For example, a $10 discount applied to a $100 taxable item and
    $100 non-taxable item would result in a $5 taxable discount and $5 non-taxable
    discount.
    """

    discount_rate_percent: Optional[str] = FieldInfo(alias="discountRatePercent", default=None)
    """
    The percentage amount to subtract from the total or subtotal when applying this
    discount item to a transaction.

    **NOTE**: A percentage discount only applies to the line immediately above it,
    so tax implications only affect that specific line.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this discount item, formed
    by combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if a discount item is under "Discounts" and
    has the `name` "10% labor discount", its `fullName` would be "Discounts:10%
    labor discount".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    discount item objects. However, `fullName` can still be arbitrarily changed by
    the QuickBooks user when they modify the underlying `name` field.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this discount item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """The case-insensitive name of this discount item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two discount
    items could both have the `name` "10% labor discount", but they could have
    unique `fullName` values, such as "Discounts:10% labor discount" and
    "Promotions:10% labor discount".
    """

    object_type: Literal["qbd_discount_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_discount_item"`."""

    parent: Optional[Parent] = None
    """The parent discount item one level above this one in the hierarchy.

    For example, if this discount item has a `fullName` of "Discounts:10% labor
    discount", its parent has a `fullName` of "Discounts". If this discount item is
    at the top level, this field will be `null`.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this discount item object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The default sales-tax code for this discount item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sublevel: float
    """The depth level of this discount item in the hierarchy.

    A top-level discount item has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, a discount item with a `fullName` of
    "Discounts:10% labor discount" would have a `sublevel` of 1.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this discount item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
