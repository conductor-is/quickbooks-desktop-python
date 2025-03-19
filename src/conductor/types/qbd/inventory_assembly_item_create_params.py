# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryAssemblyItemCreateParams", "Barcode", "Line"]


class InventoryAssemblyItemCreateParams(TypedDict, total=False):
    asset_account_id: Required[Annotated[str, PropertyInfo(alias="assetAccountId")]]
    """
    The asset account used to track the current value of this inventory assembly
    item in inventory.
    """

    cogs_account_id: Required[Annotated[str, PropertyInfo(alias="cogsAccountId")]]
    """
    The Cost of Goods Sold (COGS) account for this inventory assembly item, tracking
    the original direct costs of producing goods sold.
    """

    income_account_id: Required[Annotated[str, PropertyInfo(alias="incomeAccountId")]]
    """
    The income account used to track revenue from sales of this inventory assembly
    item.
    """

    name: Required[str]
    """The case-insensitive name of this inventory assembly item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two inventory
    assembly items could both have the `name` "Deluxe Kit", but they could have
    unique `fullName` values, such as "Assemblies:Deluxe Kit" and "Inventory:Deluxe
    Kit".

    Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    barcode: Barcode
    """The inventory assembly item's barcode."""

    build_notification_threshold: Annotated[float, PropertyInfo(alias="buildNotificationThreshold")]
    """
    The inventory assembly item's minimum quantity threshold that triggers a build
    notification in QuickBooks. When the sum of `quantityOnHand` (current inventory)
    and `quantityOnOrder` (pending purchase orders) drops below this threshold,
    QuickBooks will notify users that more units need to be built or assembled. This
    helps ensure adequate inventory levels for inventory assembly items.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The inventory assembly item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    inventory_date: Annotated[Union[str, date], PropertyInfo(alias="inventoryDate", format="iso8601")]
    """
    The date when this inventory assembly item was converted into an inventory item
    from some other type of item, in ISO 8601 format (YYYY-MM-DD).
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory assembly item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    lines: Iterable[Line]
    """The inventory assembly item's lines."""

    maximum_quantity_on_hand: Annotated[float, PropertyInfo(alias="maximumQuantityOnHand")]
    """The maximum quantity of this inventory assembly item desired in inventory."""

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory assembly item one level above this one in the hierarchy.

    For example, if this inventory assembly item has a `fullName` of
    "Assemblies:Deluxe Kit", its parent has a `fullName` of "Assemblies". If this
    inventory assembly item is at the top level, this field will be `null`.
    """

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """
    The preferred vendor from whom this inventory assembly item is typically
    purchased.
    """

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this inventory assembly item is purchased from vendors,
    represented as a decimal string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this inventory assembly item that appears on purchase forms
    (e.g., checks, bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this inventory assembly item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    quantity_on_hand: Annotated[float, PropertyInfo(alias="quantityOnHand")]
    """The current quantity of this inventory assembly item available in inventory.

    To change the `quantityOnHand` for an inventory assembly item, you must create
    an inventory-adjustment instead of updating this inventory assembly item
    directly.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this inventory assembly item that appears on sales forms
    (e.g., invoices, sales receipts) when sold to customers.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this inventory assembly item is sold to customers,
    represented as a decimal string.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for this inventory assembly item, determining whether
    it is taxable or non-taxable. This can be overridden at the transaction-line
    level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    total_value: Annotated[str, PropertyInfo(alias="totalValue")]
    """The total value of this inventory assembly item.

    If `totalValue` is provided, `quantityOnHand` must also be provided and must be
    greater than zero. If both `quantityOnHand` and `purchaseCost` are provided,
    then `totalValue` will be set to `quantityOnHand` times `purchaseCost`,
    regardless of what `totalValue` is explicitly set to.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this inventory assembly item, which
    consists of a base unit and related units.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""


class Line(TypedDict, total=False):
    inventory_item_id: Annotated[str, PropertyInfo(alias="inventoryItemId")]
    """The inventory item associated with this inventory assembly item line."""

    quantity: float
    """The quantity of the item associated with this inventory assembly item line.

    This field cannot be cleared.

    **NOTE**: Do not use this field if the associated item is a discount item.
    """
