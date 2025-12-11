# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BuildAssemblyUpdateParams"]


class BuildAssemblyUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the build assembly object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """The ID of the End-User to receive this request."""

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this build assembly, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this build
    assembly is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this build assembly is stored.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this build assembly.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    mark_pending_if_required: Annotated[bool, PropertyInfo(alias="markPendingIfRequired")]
    """
    When `true`, the build assembly will be marked pending if there are insufficient
    quantities to complete the build assembly.
    """

    memo: str
    """A memo or note for this build assembly."""

    quantity_to_build: Annotated[float, PropertyInfo(alias="quantityToBuild")]
    """The number of build assembly to be built.

    The transaction will fail if the number specified here exceeds the number of
    on-hand components.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this build assembly, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    remove_pending: Annotated[bool, PropertyInfo(alias="removePending")]
    """
    When `true`, changes this build assembly's status from pending to non-pending,
    which effectively performs the build transaction. The operation will fail if
    there are insufficient component quantities on hand to complete the build.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this build assembly.

    This is used for tracking individual units of serialized inventory items.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this build assembly, in ISO 8601 format (YYYY-MM-DD)."""
