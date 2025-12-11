# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryItemUpdateParams", "Barcode"]


class InventoryItemUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the inventory item object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    asset_account_id: Annotated[str, PropertyInfo(alias="assetAccountId")]
    """
    The asset account used to track the current value of this inventory item in
    inventory.
    """

    barcode: Barcode
    """The inventory item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The inventory item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    cogs_account_id: Annotated[str, PropertyInfo(alias="cogsAccountId")]
    """
    The Cost of Goods Sold (COGS) account for this inventory item, tracking the
    original direct costs of producing goods sold.
    """

    force_unit_of_measure_change: Annotated[bool, PropertyInfo(alias="forceUnitOfMeasureChange")]
    """
    Indicates whether to allow changing the inventory item's unit-of-measure set
    (using the `unitOfMeasureSetId` field) when the base unit of the new
    unit-of-measure set does not match that of the currently assigned set. Without
    setting this field to `true` in this scenario, the request will fail with an
    error; hence, this field is equivalent to accepting the warning prompt in the
    QuickBooks UI.

    NOTE: Changing the base unit requires you to update the item's
    quantities-on-hand and cost to reflect the new unit; otherwise, these values
    will be inaccurate. Alternatively, consider creating a new item with the desired
    unit-of-measure set and deactivating the old item.
    """

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """The income account used to track revenue from sales of this inventory item."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    maximum_quantity_on_hand: Annotated[float, PropertyInfo(alias="maximumQuantityOnHand")]
    """The maximum quantity of this inventory item desired in inventory."""

    name: str
    """The case-insensitive name of this inventory item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two inventory
    items could both have the `name` "Cabinet", but they could have unique
    `fullName` values, such as "Kitchen:Cabinet" and "Inventory:Cabinet".

    Maximum length: 31 characters.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory item one level above this one in the hierarchy.

    For example, if this inventory item has a `fullName` of "Kitchen:Cabinet", its
    parent has a `fullName` of "Kitchen". If this inventory item is at the top
    level, this field will be `null`.
    """

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """The preferred vendor from whom this inventory item is typically purchased."""

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this inventory item is purchased from vendors, represented as
    a decimal string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this inventory item that appears on purchase forms (e.g.,
    checks, bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this inventory item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    reorder_point: Annotated[float, PropertyInfo(alias="reorderPoint")]
    """
    The minimum quantity of this inventory item at which QuickBooks prompts for
    reordering.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this inventory item that appears on sales forms (e.g.,
    invoices, sales receipts) when sold to customers.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this inventory item is sold to customers, represented as a
    decimal string.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for this inventory item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sku: str
    """
    The inventory item's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this inventory item, which consists of a
    base unit and related units.
    """

    update_existing_transactions_cogs_account: Annotated[
        bool, PropertyInfo(alias="updateExistingTransactionsCogsAccount")
    ]
    """
    When `true`, applies the new COGS account (specified by the `cogsAccountId`
    field) to all existing transactions that use this inventory item. This updates
    historical data and should be used with caution. The update will fail if any
    affected transaction falls within a closed accounting period. If this parameter
    is not specified, QuickBooks will prompt the user before making any changes.
    """

    update_existing_transactions_income_account: Annotated[
        bool, PropertyInfo(alias="updateExistingTransactionsIncomeAccount")
    ]
    """
    When `true`, applies the new income account (specified by the `incomeAccountId`
    field) to all existing transactions that use this inventory item. This updates
    historical data and should be used with caution. The update will fail if any
    affected transaction falls within a closed accounting period. If this parameter
    is not specified, QuickBooks will prompt the user before making any changes.
    """


class Barcode(TypedDict, total=False):
    """The inventory item's barcode."""

    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""
