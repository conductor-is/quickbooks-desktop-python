# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryAdjustmentUpdateParams", "Line"]


class InventoryAdjustmentUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the inventory adjustment
    object you are updating, which you can get by fetching the object first. Provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    The account to which this inventory adjustment is posted for tracking inventory
    value changes.
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

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this inventory
    adjustment is stored.
    """

    lines: Iterable[Line]
    """
    The inventory adjustment's item lines, each representing the adjustment of an
    inventory item's quantity, value, serial number, or lot number.

    **IMPORTANT**:

    1. Including this array in your update request will **REPLACE** all existing
       item lines for the inventory adjustment with this array. To keep any existing
       item lines, you must include them in this array even if they have not
       changed. **Any item lines not included will be removed.**

    2. To add a new item line, include it here with the `id` field set to `-1`.

    3. If you do not wish to modify any item lines, omit this field entirely to keep
       them unchanged.
    """

    memo: str
    """A memo or note for this inventory adjustment."""

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this inventory adjustment,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this inventory adjustment, in ISO 8601 format (YYYY-MM-DD)."""


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing inventory adjustment
    line you wish to retain or update.

    **IMPORTANT**: Set this field to `-1` for new inventory adjustment lines you
    wish to add.
    """

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

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The inventory item associated with this inventory adjustment line."""

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this inventory adjustment line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
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

    value_difference: Annotated[float, PropertyInfo(alias="valueDifference")]
    """
    Either a positive or negative number that shows the change in the total value of
    the entire stock of the inventory item associated with this inventory adjustment
    line. A positive number increases the value, while a negative number decreases
    it.
    """
