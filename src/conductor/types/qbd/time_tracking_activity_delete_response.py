# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TimeTrackingActivityDeleteResponse"]


class TimeTrackingActivityDeleteResponse(BaseModel):
    id: str
    """
    The QuickBooks-assigned unique identifier of the deleted time tracking activity.
    """

    deleted: bool
    """Indicates whether the time tracking activity was deleted."""

    object_type: Literal["qbd_time_tracking_activity"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_time_tracking_activity"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the deleted time tracking
    activity.
    """
