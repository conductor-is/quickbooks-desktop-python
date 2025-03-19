# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InventoryAdjustmentCreateParams",
    "Line",
    "LineAdjustLotNumber",
    "LineAdjustQuantity",
    "LineAdjustSerialNumber",
    "LineAdjustValue",
]


class InventoryAdjustmentCreateParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """
    The account to which this inventory adjustment is posted for tracking inventory
    value changes.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The inventory adjustment's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this inventory
    adjustment's line items unless overridden at the line item level.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this inventory adjustment."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system. This field is immutable and can only be set
    during object creation.

    **IMPORTANT**: This field must be formatted as a valid GUID; otherwise,
    QuickBooks will return an error.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this inventory
    adjustment is stored.
    """

    lines: Iterable[Line]
    """
    The inventory adjustment's item lines, each representing the adjustment of an
    inventory item's quantity, value, serial number, or lot number.
    """

    memo: str
    """A memo or note for this inventory adjustment."""

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this inventory adjustment,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    When left blank in this create request, this field will be left blank in
    QuickBooks (i.e., it does _not_ auto-increment).
    """


class LineAdjustLotNumber(TypedDict, total=False):
    adjust_count: Annotated[float, PropertyInfo(alias="adjustCount")]
    """
    The amount to adjust the count of the inventory item associated with this
    inventory adjustment line.
    """

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this inventory adjustment line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this inventory adjustment line is stored.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this inventory adjustment line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """


class LineAdjustQuantity(TypedDict, total=False):
    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this inventory adjustment line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this inventory adjustment line is stored.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this inventory adjustment line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    new_quantity: Annotated[float, PropertyInfo(alias="newQuantity")]
    """
    The new quantity for the inventory item associated with this inventory
    adjustment line.
    """

    quantity_difference: Annotated[float, PropertyInfo(alias="quantityDifference")]
    """
    Either a positive or negative number that shows the change in quantity for the
    inventory item associated with this inventory adjustment line. A positive number
    increases the quantity, while a negative number decreases it.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this inventory adjustment line.

    This is used for tracking individual units of serialized inventory items.
    """


class LineAdjustSerialNumber(TypedDict, total=False):
    add_serial_number: Annotated[str, PropertyInfo(alias="addSerialNumber")]
    """
    The serial number, which represents a unique unit of the inventory item
    associated with this inventory adjustment line, to add to inventory.
    """

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this inventory adjustment line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this inventory adjustment line is stored.
    """

    remove_serial_number: Annotated[str, PropertyInfo(alias="removeSerialNumber")]
    """
    The serial number, which represents a unique unit of the inventory item
    associated with this inventory adjustment line, to remove from inventory.
    """


class LineAdjustValue(TypedDict, total=False):
    new_quantity: Annotated[float, PropertyInfo(alias="newQuantity")]
    """
    The new quantity for the inventory item associated with this inventory
    adjustment line.
    """

    new_value: Annotated[str, PropertyInfo(alias="newValue")]
    """
    The new total value of the entire stock of the inventory item associated with
    this inventory adjustment line.

    **NOTE**: The new value does _not_ have to equal `quantityOnHand` times
    `purchaseCost`.
    """

    quantity_difference: Annotated[float, PropertyInfo(alias="quantityDifference")]
    """
    Either a positive or negative number that shows the change in quantity for the
    inventory item associated with this inventory adjustment line. A positive number
    increases the quantity, while a negative number decreases it.
    """

    value_difference: Annotated[float, PropertyInfo(alias="valueDifference")]
    """
    Either a positive or negative number that shows the change in the total value of
    the entire stock of the inventory item associated with this inventory adjustment
    line. A positive number increases the value, while a negative number decreases
    it.
    """


class Line(TypedDict, total=False):
    adjust_lot_number: Annotated[LineAdjustLotNumber, PropertyInfo(alias="adjustLotNumber")]
    """Adjusts the lot number of this inventory adjustment line."""

    adjust_quantity: Annotated[LineAdjustQuantity, PropertyInfo(alias="adjustQuantity")]
    """
    Adjusts the inventory quantity of this inventory item either by setting a new
    quantity or by adjusting the current quantity up or down.
    """

    adjust_serial_number: Annotated[LineAdjustSerialNumber, PropertyInfo(alias="adjustSerialNumber")]
    """Adjusts the serial number of this inventory adjustment line.

    This is used for tracking individual units of serialized inventory items.
    """

    adjust_value: Annotated[LineAdjustValue, PropertyInfo(alias="adjustValue")]
    """
    Adjusts the total value of the entire stock of this inventory item by setting a
    new monetary value, and optionally by setting a new quantity.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The inventory item associated with this inventory adjustment line."""
