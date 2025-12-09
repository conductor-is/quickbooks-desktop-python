# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InventoryItem",
    "AssetAccount",
    "Class",
    "CogsAccount",
    "CustomField",
    "IncomeAccount",
    "Parent",
    "PreferredVendor",
    "PurchaseTaxCode",
    "SalesTaxCode",
    "UnitOfMeasureSet",
]


class AssetAccount(BaseModel):
    """
    The asset account used to track the current value of this inventory item in inventory.
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
    """The inventory item's class.

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


class CogsAccount(BaseModel):
    """
    The Cost of Goods Sold (COGS) account for this inventory item, tracking the original direct costs of producing goods sold.
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


class IncomeAccount(BaseModel):
    """The income account used to track revenue from sales of this inventory item."""

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


class Parent(BaseModel):
    """The parent inventory item one level above this one in the hierarchy.

    For example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its parent has a `fullName` of "Kitchen". If this inventory item is at the top level, this field will be `null`.
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


class PreferredVendor(BaseModel):
    """The preferred vendor from whom this inventory item is typically purchased."""

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


class PurchaseTaxCode(BaseModel):
    """The tax code applied to purchases of this inventory item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
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
    The default sales-tax code for this inventory item, determining whether it is taxable or non-taxable. This can be overridden at the transaction-line level.

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


class UnitOfMeasureSet(BaseModel):
    """
    The unit-of-measure set associated with this inventory item, which consists of a base unit and related units.
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
    id: str
    """The unique identifier assigned by QuickBooks to this inventory item.

    This ID is unique across all inventory items but not across different QuickBooks
    object types.
    """

    asset_account: AssetAccount = FieldInfo(alias="assetAccount")
    """
    The asset account used to track the current value of this inventory item in
    inventory.
    """

    average_cost: Optional[str] = FieldInfo(alias="averageCost", default=None)
    """
    The average cost per unit of this inventory item, represented as a decimal
    string.
    """

    barcode: Optional[str] = None
    """The inventory item's barcode."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The inventory item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    cogs_account: CogsAccount = FieldInfo(alias="cogsAccount")
    """
    The Cost of Goods Sold (COGS) account for this inventory item, tracking the
    original direct costs of producing goods sold.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this inventory item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the inventory item object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The case-insensitive fully-qualified unique name of this inventory item, formed
    by combining the names of its hierarchical parent objects with its own `name`,
    separated by colons. For example, if an inventory item is under "Kitchen" and
    has the `name` "Cabinet", its `fullName` would be "Kitchen:Cabinet".

    **NOTE**: Unlike `name`, `fullName` is guaranteed to be unique across all
    inventory item objects. However, `fullName` can still be arbitrarily changed by
    the QuickBooks user when they modify the underlying `name` field.
    """

    income_account: IncomeAccount = FieldInfo(alias="incomeAccount")
    """The income account used to track revenue from sales of this inventory item."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    maximum_quantity_on_hand: Optional[float] = FieldInfo(alias="maximumQuantityOnHand", default=None)
    """The maximum quantity of this inventory item desired in inventory."""

    name: str
    """The case-insensitive name of this inventory item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two inventory
    items could both have the `name` "Cabinet", but they could have unique
    `fullName` values, such as "Kitchen:Cabinet" and "Inventory:Cabinet".
    """

    object_type: Literal["qbd_inventory_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_item"`."""

    parent: Optional[Parent] = None
    """The parent inventory item one level above this one in the hierarchy.

    For example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
    parent has a `fullName` of "Kitchen". If this inventory item is at the top
    level, this field will be `null`.
    """

    preferred_vendor: Optional[PreferredVendor] = FieldInfo(alias="preferredVendor", default=None)
    """The preferred vendor from whom this inventory item is typically purchased."""

    purchase_cost: Optional[str] = FieldInfo(alias="purchaseCost", default=None)
    """
    The cost at which this inventory item is purchased from vendors, represented as
    a decimal string.
    """

    purchase_description: Optional[str] = FieldInfo(alias="purchaseDescription", default=None)
    """
    The description of this inventory item that appears on purchase forms (e.g.,
    checks, bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code: Optional[PurchaseTaxCode] = FieldInfo(alias="purchaseTaxCode", default=None)
    """The tax code applied to purchases of this inventory item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    quantity_on_hand: Optional[float] = FieldInfo(alias="quantityOnHand", default=None)
    """The number of units of this inventory item currently in inventory.

    `quantityOnHand` multiplied by `averageCost` equals `totalValue` for inventory
    item lists. To change the `quantityOnHand` for an inventory item, you must use
    an inventory-adjustment instead of updating the inventory item directly.
    """

    quantity_on_purchase_order: Optional[float] = FieldInfo(alias="quantityOnPurchaseOrder", default=None)
    """
    The number of units of this inventory item that have been ordered from vendors
    (as recorded in purchase orders) but not yet received.
    """

    quantity_on_sales_order: Optional[float] = FieldInfo(alias="quantityOnSalesOrder", default=None)
    """
    The number of units of this inventory item that have been sold (as recorded in
    sales orders) but not yet fulfilled or delivered to customers.
    """

    reorder_point: Optional[float] = FieldInfo(alias="reorderPoint", default=None)
    """
    The minimum quantity of this inventory item at which QuickBooks prompts for
    reordering.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current QuickBooks-assigned revision number of this inventory item object,
    which changes each time the object is modified. When updating this object, you
    must provide the most recent `revisionNumber` to ensure you're working with the
    latest data; otherwise, the update will return an error.
    """

    sales_description: Optional[str] = FieldInfo(alias="salesDescription", default=None)
    """
    The description of this inventory item that appears on sales forms (e.g.,
    invoices, sales receipts) when sold to customers.
    """

    sales_price: Optional[str] = FieldInfo(alias="salesPrice", default=None)
    """
    The price at which this inventory item is sold to customers, represented as a
    decimal string.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The default sales-tax code for this inventory item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sku: Optional[str] = None
    """
    The inventory item's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    sublevel: float
    """The depth level of this inventory item in the hierarchy.

    A top-level inventory item has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, an inventory item with a `fullName` of
    "Kitchen:Cabinet" would have a `sublevel` of 1.
    """

    unit_of_measure_set: Optional[UnitOfMeasureSet] = FieldInfo(alias="unitOfMeasureSet", default=None)
    """
    The unit-of-measure set associated with this inventory item, which consists of a
    base unit and related units.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this inventory item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """
