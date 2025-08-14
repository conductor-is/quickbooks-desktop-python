# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .deleted_list_object import DeletedListObject

__all__ = ["DeletedListObjectListResponse"]


class DeletedListObjectListResponse(BaseModel):
    data: List[DeletedListObject]
    """The array of deleted list-objects."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
