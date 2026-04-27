# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InventoryAdjustmentVoidResponse"]


class InventoryAdjustmentVoidResponse(BaseModel):
    id: str
    """The QuickBooks-assigned unique identifier of the voided inventory adjustment."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """
    The date and time when this inventory adjustment was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss+hh:mm), which QuickBooks Desktop interprets in the local
    timezone of the end-user's computer.
    """

    object_type: Literal["qbd_inventory_adjustment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_adjustment"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the voided inventory
    adjustment.
    """

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """
    The date and time when this inventory adjustment was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss+hh:mm), which QuickBooks Desktop interprets in the
    local timezone of the end-user's computer.
    """

    voided: bool
    """Indicates whether the inventory adjustment was voided."""
