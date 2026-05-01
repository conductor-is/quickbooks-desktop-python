# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DepositDeleteResponse"]


class DepositDeleteResponse(BaseModel):
    id: str
    """The QuickBooks-assigned unique identifier of the deleted deposit."""

    deleted: bool
    """Indicates whether the deposit was deleted."""

    object_type: Literal["qbd_deposit"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_deposit"`."""
