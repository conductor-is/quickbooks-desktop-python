# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .deleted_transaction import DeletedTransaction

__all__ = ["DeletedTransactionListResponse"]


class DeletedTransactionListResponse(BaseModel):
    data: List[DeletedTransaction]
    """The array of deleted transactions."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
