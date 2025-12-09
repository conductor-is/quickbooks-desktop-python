# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ItemSite", "InventoryAssemblyItem", "InventoryItem", "InventorySite", "InventorySiteLocation"]


class InventoryAssemblyItem(BaseModel):
    """The inventory assembly item associated with this item site.

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


class InventoryItem(BaseModel):
    """The inventory item associated with this item site."""

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
    The site location where inventory for the item associated with this item site is stored.
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
    The specific location (e.g., bin or shelf) within the inventory site where the item associated with this item site is stored.
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


class ItemSite(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this item site.

    This ID is unique across all item sites but not across different QuickBooks
    object types.
    """

    assembly_build_point: Optional[float] = FieldInfo(alias="assemblyBuildPoint", default=None)
    """The inventory level of this item site at which a new build assembly should
    begin.

    When the combined `quantityOnHand` and `quantityOnPurchaseOrders` drops below
    this point, QuickBooks flags the need to build additional units.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this item site was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    inventory_assembly_item: Optional[InventoryAssemblyItem] = FieldInfo(alias="inventoryAssemblyItem", default=None)
    """The inventory assembly item associated with this item site.

    An inventory assembly item is assembled or manufactured from other inventory
    items, and the items and/or assemblies that make up the assembly are called
    components.
    """

    inventory_item: Optional[InventoryItem] = FieldInfo(alias="inventoryItem", default=None)
    """The inventory item associated with this item site."""

    inventory_site: Optional[InventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this item site is
    stored.
    """

    inventory_site_location: Optional[InventorySiteLocation] = FieldInfo(alias="inventorySiteLocation", default=None)
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item site is stored.
    """

    object_type: Literal["qbd_item_site"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_site"`."""

    quantity_on_hand: Optional[float] = FieldInfo(alias="quantityOnHand", default=None)
    """The number of units of this item site currently in inventory."""

    quantity_on_pending_transfers: Optional[float] = FieldInfo(alias="quantityOnPendingTransfers", default=None)
    """
    The number of units of this item site that are currently on pending inventory
    transfer transactions.
    """

    quantity_on_purchase_orders: Optional[float] = FieldInfo(alias="quantityOnPurchaseOrders", default=None)
    """
    The number of units of this item site that are currently listed on outstanding
    purchase orders and have not yet been received.
    """

    quantity_on_sales_orders: Optional[float] = FieldInfo(alias="quantityOnSalesOrders", default=None)
    """
    The number of units of this item site that are currently listed on outstanding
    sales orders and have not yet been fulfilled or delivered to customers.
    """

    quantity_required_by_pending_build_transactions: Optional[float] = FieldInfo(
        alias="quantityRequiredByPendingBuildTransactions", default=None
    )
    """The number of units of this item site required by pending build transactions."""

    quantity_to_be_built_by_pending_build_transactions: Optional[float] = FieldInfo(
        alias="quantityToBeBuiltByPendingBuildTransactions", default=None
    )
    """
    The number of units of this item site that are scheduled to be built on pending
    build transactions.
    """

    reorder_level: Optional[float] = FieldInfo(alias="reorderLevel", default=None)
    """The inventory level at which QuickBooks prompts you to reorder this item site."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this item site object, which
    changes each time the object is modified. When updating this object, you must
    provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this item site was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
