# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BuildAssembly",
    "CustomField",
    "InventoryAssemblyItem",
    "InventorySite",
    "InventorySiteLocation",
    "Line",
    "LineInventorySite",
    "LineInventorySiteLocation",
    "LineItem",
]


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


class InventoryAssemblyItem(BaseModel):
    """The inventory assembly item associated with this build assembly.

    An inventory assembly item is assembled or manufactured from other inventory items, and the items and/or assemblies that make up the assembly are called components.
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


class InventorySite(BaseModel):
    """
    The site location where inventory for the item associated with this build assembly is stored.
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


class InventorySiteLocation(BaseModel):
    """
    The specific location (e.g., bin or shelf) within the inventory site where the item associated with this build assembly is stored.
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


class LineInventorySite(BaseModel):
    """
    The site location where inventory for the item associated with this component item line is stored.
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


class LineInventorySiteLocation(BaseModel):
    """
    The specific location (e.g., bin or shelf) within the inventory site where the item associated with this component item line is stored.
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


class LineItem(BaseModel):
    """The item associated with this component item line.

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


class Line(BaseModel):
    description: Optional[str] = None
    """A description of this component item line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this component item line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[LineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this component
    item line is stored.
    """

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this component item line is stored.
    """

    item: Optional[LineItem] = None
    """The item associated with this component item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this component item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    quantity_needed: Optional[float] = FieldInfo(alias="quantityNeeded", default=None)
    """The quantity of this component item line that is needed to build the assembly.

    For example, if the `itemId` references a bolt, the `quantityNeeded` field
    indicates how many of these bolts are used in the assembly.
    """

    quantity_on_hand: Optional[float] = FieldInfo(alias="quantityOnHand", default=None)
    """The number of units of this component item line currently in inventory."""

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this component item line.

    This is used for tracking individual units of serialized inventory items.
    """


class BuildAssembly(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this build assembly.

    This ID is unique across all transaction types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this build assembly was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the build assembly object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    inventory_assembly_item: InventoryAssemblyItem = FieldInfo(alias="inventoryAssemblyItem")
    """The inventory assembly item associated with this build assembly.

    An inventory assembly item is assembled or manufactured from other inventory
    items, and the items and/or assemblies that make up the assembly are called
    components.
    """

    inventory_site: Optional[InventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this build
    assembly is stored.
    """

    inventory_site_location: Optional[InventorySiteLocation] = FieldInfo(alias="inventorySiteLocation", default=None)
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this build assembly is stored.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this build assembly has not been completed."""

    lines: List[Line]
    """The component item lines in this build assembly."""

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this build assembly.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    memo: Optional[str] = None
    """A memo or note for this build assembly."""

    object_type: Literal["qbd_build_assembly"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_build_assembly"`."""

    quantity_can_build: float = FieldInfo(alias="quantityCanBuild")
    """The number of this build assembly that can be built from the parts on hand."""

    quantity_on_hand: float = FieldInfo(alias="quantityOnHand")
    """The number of units of this build assembly currently in inventory."""

    quantity_on_sales_order: float = FieldInfo(alias="quantityOnSalesOrder")
    """
    The number of units of this build assembly that have been sold (as recorded in
    sales orders) but not yet fulfilled or delivered to customers.
    """

    quantity_to_build: float = FieldInfo(alias="quantityToBuild")
    """The number of build assembly to be built.

    The transaction will fail if the number specified here exceeds the number of
    on-hand components.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this build assembly, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this build assembly object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this build assembly.

    This is used for tracking individual units of serialized inventory items.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this build assembly, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this build assembly was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
