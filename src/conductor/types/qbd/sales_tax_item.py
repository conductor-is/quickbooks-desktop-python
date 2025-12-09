# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesTaxItem", "Class", "CustomField", "SalesTaxReturnLine", "TaxVendor"]


class Class(BaseModel):
    """The sales-tax item's class.

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


class SalesTaxReturnLine(BaseModel):
    """
    The specific line on the sales tax return form where the tax collected using this sales-tax item should be reported.
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


class TaxVendor(BaseModel):
    """
    The tax agency (vendor) to whom collected sales taxes are owed for this sales-tax item. This field refers to a vendor in QuickBooks that represents the tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is required.
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


class SalesTaxItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales-tax item.

    This ID is unique across all sales-tax items but not across different QuickBooks
    object types.
    """

    barcode: Optional[str] = None
    """The sales-tax item's barcode."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The sales-tax item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales-tax item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales-tax item object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """
    The sales-tax item's description that will appear on sales forms that include
    this item.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    is_active: bool = FieldInfo(alias="isActive")
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
    """

    object_type: Literal["qbd_sales_tax_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_item"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this sales-tax item object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_tax_return_line: Optional[SalesTaxReturnLine] = FieldInfo(alias="salesTaxReturnLine", default=None)
    """
    The specific line on the sales tax return form where the tax collected using
    this sales-tax item should be reported.
    """

    tax_rate: Optional[str] = FieldInfo(alias="taxRate", default=None)
    """The tax rate defined by this sales-tax item, represented as a decimal string.

    For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
    of sales tax applied when this item is used in transactions. If a non-zero
    `taxRate` is specified, then the `taxVendor` field is required.
    """

    tax_vendor: Optional[TaxVendor] = FieldInfo(alias="taxVendor", default=None)
    """
    The tax agency (vendor) to whom collected sales taxes are owed for this
    sales-tax item. This field refers to a vendor in QuickBooks that represents the
    tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
    required.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales-tax item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
