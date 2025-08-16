# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .unit_of_measure_set import UnitOfMeasureSet

__all__ = ["UnitOfMeasureSetListResponse"]


class UnitOfMeasureSetListResponse(BaseModel):
    data: List[UnitOfMeasureSet]
    """The array of unit-of-measure sets."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
