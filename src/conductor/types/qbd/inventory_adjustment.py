# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InventoryAdjustment",
    "Account",
    "Class",
    "Customer",
    "CustomField",
    "InventorySite",
    "Line",
    "LineInventorySiteLocation",
    "LineItem",
]


class Account(BaseModel):
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


class Customer(BaseModel):
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


class InventorySite(BaseModel):
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


class LineInventorySiteLocation(BaseModel):
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


class LineItem(BaseModel):
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


class Line(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this inventory adjustment line.

    This ID is unique across all transaction line types.
    """

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this inventory adjustment line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this inventory adjustment line is stored.
    """

    item: Optional[LineItem] = None
    """The inventory item associated with this inventory adjustment line."""

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this inventory adjustment line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_inventory_adjustment_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_adjustment_line"`."""

    quantity_difference: Optional[float] = FieldInfo(alias="quantityDifference", default=None)
    """
    Either a positive or negative number that shows the change in quantity for the
    inventory item associated with this inventory adjustment line. A positive number
    increases the quantity, while a negative number decreases it.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this inventory adjustment line.

    This is used for tracking individual units of serialized inventory items.
    """

    serial_number_action: Optional[Literal["added", "removed"]] = FieldInfo(alias="serialNumberAction", default=None)
    """
    Indicates whether this inventory adjustment line's serial number was added or
    removed from the inventory.
    """

    value_difference: Optional[float] = FieldInfo(alias="valueDifference", default=None)
    """
    Either a positive or negative number that shows the change in the total value of
    the entire stock of the inventory item associated with this inventory adjustment
    line. A positive number increases the value, while a negative number decreases
    it.
    """


class InventoryAdjustment(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this inventory adjustment.

    This ID is unique across all transaction types.
    """

    account: Account
    """
    The account to which this inventory adjustment is posted for tracking inventory
    value changes.
    """

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The inventory adjustment's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this inventory
    adjustment's line items unless overridden at the line item level.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this inventory adjustment was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    customer: Optional[Customer] = None
    """The customer or customer-job associated with this inventory adjustment."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the inventory adjustment object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    inventory_site: Optional[InventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this inventory
    adjustment is stored.
    """

    lines: List[Line]
    """
    The inventory adjustment's item lines, each representing the adjustment of an
    inventory item's quantity, value, serial number, or lot number.
    """

    memo: Optional[str] = None
    """A memo or note for this inventory adjustment."""

    object_type: Literal["qbd_inventory_adjustment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_adjustment"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this inventory adjustment,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this inventory adjustment
    object, which changes each time the object is modified. When updating this
    object, you must provide the most recent `revisionNumber` to ensure you're
    working with the latest data; otherwise, the update will return an error.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this inventory adjustment was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """
